"""
Step 5 — The primes-to-zeros pipeline: FFT peaks as Newton seeds.

Supplements Section 5.3. Demonstrates that the FFT peaks from step3 (derived
from prime data) serve as Newton seeds that converge to the exact zero
ordinates of zeta(s) and L(s, chi_{-3}) to machine precision in 3-5 iterations.

Pipeline:
    primes -> sieve -> psi_O -> FFT -> approximate gamma -> Newton -> exact zero

Inputs (from data/): fft_peaks.npy, lchi3_zeros.npy   (run step3 first)
"""
import numpy as np
import mpmath as mp
from _paths import DATA

mp.mp.dps = 30

peak_g = np.load(DATA / 'fft_peaks.npy')
lchi3_zeros = np.load(DATA / 'lchi3_zeros.npy')

# reference zeta zeros (mpmath gives these exactly; listed for matching)
zeta_zeros = np.array([float(mp.im(mp.zetazero(n))) for n in range(1, 14)])


def theta(t):
    s = mp.mpc(0.25, t/2)
    return mp.im(mp.loggamma(s)) - (t/2)*mp.log(mp.pi)


def Z_zeta(t):
    return (mp.e**(1j*theta(t)) * mp.zeta(mp.mpc(0.5, t))).real


def L_chi3(s):
    return mp.mpf(3)**(-s) * (mp.zeta(s, mp.mpf(1)/3) - mp.zeta(s, mp.mpf(2)/3))


def Z_chi3(t):
    s = mp.mpc(0.5, t)
    return ((mp.mpf(3)/mp.pi)**((s+1)/2) * mp.gamma((s+1)/2) * L_chi3(s)).real


def newton(Zf, seed, iters=6, tol=mp.mpf('1e-25')):
    t = mp.mpf(float(seed))
    for k in range(iters):
        Zt = Zf(t)
        if abs(Zt) < tol:
            return t, k
        t = t - Zt / mp.diff(Zf, t)
    return t, iters


resolution = 0.6822
print(f"{'FFT seed':>9} {'family':>10} {'seed err':>9} {'iters':>6} {'refined':>16} {'final err':>11}")
n_ok = 0
for gp in peak_g[:15]:
    dz, dl = np.abs(zeta_zeros - gp), np.abs(lchi3_zeros - gp)
    jz, jl = dz.argmin(), dl.argmin()
    if dz[jz] < dl[jl] and dz[jz] < resolution:
        fam, true_val, Zf = 'zeta', zeta_zeros[jz], Z_zeta
    elif dl[jl] < resolution:
        fam, true_val, Zf = 'L(chi-3)', lchi3_zeros[jl], Z_chi3
    else:
        continue
    refined, it = newton(Zf, gp)
    err = abs(float(refined) - true_val)
    n_ok += (err < 1e-10)
    print(f"{gp:9.3f} {fam:>10} {abs(gp-true_val):9.4f} {it:6d} {float(refined):16.10f} {err:11.1e}")

print(f"\n{n_ok}/15 converged to machine precision (err < 1e-10).")
print("Pipeline: prime FFT peaks -> Newton on Riemann-Siegel Z -> exact ordinates.")
