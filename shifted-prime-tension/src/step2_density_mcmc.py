"""
Step 2 — Density convergence of limit orphans and MCMC fit of the decay exponent.

Supports: Section 5.4 (density convergence), Corollary 5.1 (error bounds).

Computes pi_O(x)/pi(x) -> 1/2 and fits
    log(RMS |pi_O/pi - 1/2|) = a - delta * log(x)
via Metropolis-Hastings MCMC. Expected: delta ~ 0.51, consistent with the
GRH-conditional sqrt(x) bound (delta = 1/2).

Inputs (from data/):  primes.npy, limit_orphans.npy   (run step0 first)
Outputs (to figures/): density_convergence.png
Outputs (to data/):    mcmc_delta_samples.npy
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from _paths import DATA, FIGURES

primes = np.load(DATA / 'primes.npy')
limit_orphans = np.load(DATA / 'limit_orphans.npy')
N = primes[-1]

x_grid = np.unique(np.round(np.logspace(3, np.log10(N), 600)).astype(np.int64))
x_grid = x_grid[x_grid <= N]
pi_x = np.searchsorted(primes, x_grid, side='right')
pi_O_x = np.searchsorted(limit_orphans, x_grid, side='right')
deviation = pi_O_x / pi_x - 0.5
log_x = np.log(x_grid.astype(float))

# Bin into log-x windows; compute RMS deviation per bin
nbins = 14
edges = np.linspace(log_x.min(), log_x.max(), nbins + 1)
centers, rms = [], []
for i in range(nbins):
    m = (log_x >= edges[i]) & (log_x < edges[i+1] + (1e-9 if i == nbins-1 else 0))
    if m.sum() > 5:
        centers.append(log_x[m].mean())
        rms.append(np.sqrt(np.mean(deviation[m]**2)))
centers = np.array(centers)
log_rms = np.log(np.array(rms))


def log_post(p):
    a, delta, log_sigma = p
    sigma = np.exp(log_sigma)
    if sigma <= 0 or not (-1.0 < delta < 2.0):
        return -np.inf
    resid = log_rms - (a - delta * centers)
    ll = -0.5 * np.sum((resid / sigma)**2) - len(resid) * log_sigma
    lp = -0.5 * (a / 5.0)**2 - 0.5 * ((delta - 0.5) / 1.0)**2
    return ll + lp


rng = np.random.default_rng(7)
step = np.array([0.1, 0.05, 0.1])
theta = np.array([-1.0, 0.5, -1.0])
cur = log_post(theta)
for _ in range(15):  # adaptive tuning toward ~25% acceptance
    acc = 0
    for _ in range(500):
        prop = theta + step * rng.standard_normal(3)
        lp = log_post(prop)
        if np.log(rng.random()) < lp - cur:
            theta, cur, acc = prop, lp, acc + 1
    rate = acc / 500
    if rate < 0.15:
        step *= 0.7
    elif rate > 0.40:
        step *= 1.3

n_iter = 100_000
chain = np.zeros((n_iter, 3))
chain[0] = theta
cur = log_post(chain[0])
acc = 0
for i in range(1, n_iter):
    prop = chain[i-1] + step * rng.standard_normal(3)
    lp = log_post(prop)
    if np.log(rng.random()) < lp - cur:
        chain[i], cur, acc = prop, lp, acc + 1
    else:
        chain[i] = chain[i-1]

post = chain[5000:]
delta_s = post[:, 1]
print(f"MCMC acceptance: {acc/n_iter:.3f}")
print(f"delta = {delta_s.mean():.4f} +/- {delta_s.std():.4f}")
print(f"95% CI: [{np.percentile(delta_s,2.5):.4f}, {np.percentile(delta_s,97.5):.4f}]")
print(f"Consistent with delta=1/2 (GRH-conditional sqrt(x) bound): "
      f"{'YES' if abs(delta_s.mean()-0.5) < 3*delta_s.std() else 'NO'}")

np.save(DATA / 'mcmc_delta_samples.npy', delta_s)

fig, ax = plt.subplots(1, 3, figsize=(15, 4.5))
ax[0].plot(x_grid, deviation, lw=0.5, color='steelblue')
ax[0].axhline(0, color='k', ls='--', lw=0.7)
ax[0].set_xscale('log')
ax[0].set_xlabel('x'); ax[0].set_ylabel(r'$\pi_O/\pi - 1/2$')
ax[0].set_title('Deviation from 1/2 density')

a_s = post[:, 0]
ax[1].scatter(centers, log_rms, color='darkred', s=30, zorder=5)
xs = np.linspace(centers.min(), centers.max(), 100)
preds = a_s[:, None] - delta_s[:, None] * xs[None, :]
lo, mid, hi = np.percentile(preds, [2.5, 50, 97.5], axis=0)
ax[1].plot(xs, mid, 'k-', lw=1.5, label=f'fit delta={delta_s.mean():.3f}')
ax[1].fill_between(xs, lo, hi, color='gray', alpha=0.3, label='95% CI')
ax[1].set_xlabel(r'$\log x$'); ax[1].set_ylabel(r'$\log$ RMS')
ax[1].set_title('Decay envelope (MCMC)'); ax[1].legend(fontsize=8)

ax[2].hist(delta_s, bins=50, color='seagreen', alpha=0.7, density=True)
ax[2].axvline(0.5, color='blue', ls=':', lw=2, label='delta=0.5 (GRH)')
ax[2].axvline(delta_s.mean(), color='k', lw=2, label=f'mean={delta_s.mean():.3f}')
ax[2].set_xlabel(r'$\delta$'); ax[2].set_title('Posterior over delta')
ax[2].legend(fontsize=8)

plt.tight_layout()
plt.savefig(FIGURES / 'density_convergence.png', dpi=130)
print(f"Saved density_convergence.png to {FIGURES}")
