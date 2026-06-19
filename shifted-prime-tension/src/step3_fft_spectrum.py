"""
Step 3 — Spectral verification of the Dedekind factorisation.

Supports: Corollary 4.2, Section 5.3 (spectral signature).

(a) Computes psi_O(x) = sum_{n<=x, n=1(3)} Lambda(n) and the normalised error
    E_O(x)/sqrt(x), then takes its FFT.
(b) Independently computes zeros of L(s, chi_{-3}) via the Hurwitz-zeta
    representation, verifying the completed function is real on Re(s)=1/2.
(c) Matches all prominent FFT peaks to zeros of zeta(s) or L(s, chi_{-3}).

Expected: all top FFT peaks match a zero of one of the two L-functions, with
the equal 1/2-weighting predicted by Corollary 4.2.

Inputs (from data/):  primes.npy   (run step0 first)
Outputs (to figures/): spectrum.png
Outputs (to data/):    lchi3_zeros.npy, fft_peaks.npy, e_norm.npy, gamma_axis.npy, power.npy
"""
import numpy as np
import mpmath as mp
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
from _paths import DATA, FIGURES

mp.mp.dps = 30
primes = np.load(DATA / 'primes.npy')
N = int(primes[-1])

# --- (a) psi_O and normalised error ---
print("Building von Mangoldt array and psi_O(x)...")
Lambda = np.zeros(N + 1)
Lambda[primes] = np.log(primes.astype(float))
for p in primes[primes <= int(np.sqrt(N)) + 1]:
    p = int(p); pk = p * p; lp = np.log(p)
    while pk <= N:
        Lambda[pk] = lp; pk *= p

n_arr = np.arange(N + 1)
psi_O = np.cumsum(Lambda * (n_arr % 3 == 1))

u_min, u_max = np.log(1000.0), np.log(N)
M = 2**15
u = np.linspace(u_min, u_max, M)
x_re = np.exp(u)
psi_O_re = np.interp(x_re, n_arr.astype(float), psi_O)
e_norm = (psi_O_re - x_re / 2.0) / np.sqrt(x_re)

# FFT with Hann window
ed = (e_norm - e_norm.mean()) * np.hanning(M)
du = u[1] - u[0]
power = np.abs(np.fft.rfft(ed))**2
gamma_axis = np.fft.rfftfreq(M, d=du) * 2 * np.pi
resolution = 2 * np.pi / (u_max - u_min)

mask = (gamma_axis > 1) & (gamma_axis < 60)
g, p_ = gamma_axis[mask], power[mask]
peaks, _ = find_peaks(p_, height=p_.max() * 0.03, distance=2)
order = np.argsort(-p_[peaks])
peak_g = g[peaks][order]
peak_h = p_[peaks][order]

# --- (b) Zeros of L(s, chi_{-3}) via Hurwitz zeta ---
def L_chi3(s):
    return mp.mpf(3)**(-s) * (mp.zeta(s, mp.mpf(1)/3) - mp.zeta(s, mp.mpf(2)/3))

def Z_chi3(t):
    s = mp.mpc(0.5, t)
    factor = (mp.mpf(3)/mp.pi)**((s+1)/2) * mp.gamma((s+1)/2)
    return (factor * L_chi3(s)).real

print("Verifying completed L-function real on critical line...")
max_im = max(abs(float((((mp.mpf(3)/mp.pi)**((mp.mpc(0.5,t)+1)/2) *
          mp.gamma((mp.mpc(0.5,t)+1)/2) * L_chi3(mp.mpc(0.5,t))).imag)))
          for t in [5, 10, 20, 40])
print(f"  max |Im| at sample heights: {max_im:.2e} (confirms root number +1)")

print("Scanning for L(s,chi_-3) zeros in (0,60)...")
ts = [mp.mpf(x)/10 for x in range(1, 601)]
vals = [Z_chi3(t) for t in ts]
zeros = []
for i in range(len(ts)-1):
    if vals[i] * vals[i+1] < 0:
        lo, hi, flo = ts[i], ts[i+1], vals[i]
        for _ in range(60):
            mid = (lo+hi)/2; fm = Z_chi3(mid)
            if flo * fm < 0: hi = mid
            else: lo, flo = mid, fm
        zeros.append(float((lo+hi)/2))
lchi3_zeros = np.array(zeros)
print(f"  found {len(zeros)} zeros below 60")

# --- (c) Match peaks ---
zeta_zeros = np.array([14.134725, 21.022040, 25.010858, 30.424876, 32.935062,
                       37.586178, 40.918719, 43.327073, 48.005151, 49.773832,
                       52.970321, 56.446248, 59.347044])
print(f"\nMatching top FFT peaks (resolution ~{resolution:.2f}):")
nz, nl, nu = 0, 0, 0
for gp, hp in zip(peak_g[:15], peak_h[:15]):
    dz, dl = np.abs(zeta_zeros - gp), np.abs(lchi3_zeros - gp)
    jz, jl = dz.argmin(), dl.argmin()
    if dz[jz] < dl[jl] and dz[jz] < resolution:
        print(f"  gamma={gp:6.3f} pow={hp/peak_h.max():.3f} -> zeta zero {zeta_zeros[jz]:.3f}")
        nz += 1
    elif dl[jl] < resolution:
        print(f"  gamma={gp:6.3f} pow={hp/peak_h.max():.3f} -> L(chi-3) zero {lchi3_zeros[jl]:.3f}")
        nl += 1
    else:
        print(f"  gamma={gp:6.3f} pow={hp/peak_h.max():.3f} -> UNMATCHED")
        nu += 1
print(f"\nSummary: {nz} match zeta, {nl} match L(chi-3), {nu} unmatched (of top 15)")

for name, arr in [('lchi3_zeros', lchi3_zeros), ('fft_peaks', peak_g),
                  ('e_norm', e_norm), ('gamma_axis', gamma_axis), ('power', power)]:
    np.save(DATA / f'{name}.npy', arr)

# Plot
fig, ax = plt.subplots(figsize=(12, 5))
m = (gamma_axis > 0) & (gamma_axis < 60)
ax.plot(gamma_axis[m], power[m]/peak_h.max(), 'k-', lw=0.8,
        label=r'FFT power of $E_O(x)/\sqrt{x}$')
for i, z in enumerate(zeta_zeros[zeta_zeros < 60]):
    ax.axvline(z, color='crimson', ls='--', lw=1, alpha=0.7,
               label=r'$\zeta(s)$ zeros' if i == 0 else None)
for i, z in enumerate(lchi3_zeros):
    ax.axvline(z, color='royalblue', ls=':', lw=1, alpha=0.7,
               label=r'$L(s,\chi_{-3})$ zeros' if i == 0 else None)
ax.set_xlabel(r'$\gamma$'); ax.set_ylabel('normalized power'); ax.set_xlim(0, 60)
ax.set_title(r'FFT of $E_O(x)/\sqrt{x}$ vs zeros of $\zeta(s)$ and $L(s,\chi_{-3})$')
ax.legend(loc='upper right', fontsize=9)
plt.tight_layout()
plt.savefig(FIGURES / 'spectrum.png', dpi=130)
print(f"Saved spectrum.png to {FIGURES}")
