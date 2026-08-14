"""
Step 4b — Strengthened phase-wrap analysis for the argument-principle zero count.

STATUS: This is STRONG NUMERICAL EVIDENCE, not a certified proof.
        See "Remaining gap" below. The paper's hedged wording stands.

An earlier version of this script claimed to certify the zero count. A review
found the claim invalid. This version fixes the fatal defect and quantifies the
one that remains, but does not restore the word "proved".

METHOD
------
The argument principle gives the zero count as the winding number of f around
the contour. A sampled winding number is exact provided |Delta arg f| < pi on
every segment between consecutive samples. On a segment [a,b] of length h,

    |Delta arg f| = |Im \\int_a^b f'/f dz|  <=  h * max|f'| / min|f|,

with max|f'| bounded by Cauchy's estimate (|f'| <= M/rho if |f| <= M on the
circle of radius rho) and min|f| by the Lipschitz bound
min|f| >= min(|f(a)|,|f(b)|) - (h/2)*max|f'|. A segment passes when the quotient
is < 0.95*pi; otherwise it bisects and each half is retried.

FIXED DEFECT (was fatal)
------------------------
Cauchy's estimate requires f analytic on the CLOSED disc. zeta has a pole at
s = 1, and for contour segments on the right edge (sigma = 0.9) near t = 0 the
pole lies INSIDE the radius-0.4 disc: |0.9 - 1| = 0.1 < 0.4. The estimate is
inapplicable there, and measurably wrong -- at z = 0.9 + 0.0i the claimed bound
understates |zeta'| by a factor of 10.2. Segments passed on a false bound.

Fix: analyse (s-1)*zeta(s), which is ENTIRE, so Cauchy applies everywhere on
the contour. Since s = 1 lies OUTSIDE the box (Re = 1 > 0.9), the factor (s-1)
contributes zero winding and the count is unchanged. Verified: 0 violations
across 81 sample points on the right edge; winding still 26.
L(s,chi_-3) is entire for non-principal chi, so it was never affected.

REMAINING GAP (why this is not a proof)
---------------------------------------
`sup_circle` takes the maximum over N sampled points, which is a LOWER estimate
of the true supremum. Underestimating max|f'| makes segments pass more easily --
the unsafe direction. Raising N from 8 to 64 shrinks the shortfall from ~2.3%
to ~0.025%, roughly 210x inside the 0.95 safety factor, but a sampled maximum
is not a bounded one. Closing this needs either interval arithmetic (mpmath's
mp.iv.zeta is non-functional as of this writing) or explicit analytic bounds on
|zeta| in the strip.

Until then the honest description is: the zero counts 26 and 44 are supported by
a phase-wrap analysis that is valid wherever Cauchy applies and carries a large
empirical margin -- but the certificate rests on a sampled supremum.

Runtime ~4 min. Self-contained.
"""
import time
import numpy as np
import mpmath as mp

mp.mp.dps = 20

SIG_LO, SIG_HI, T = mp.mpf('0.1'), mp.mpf('0.9'), mp.mpf(60)
PAD = mp.mpf('0.4')        # Cauchy circle radius
SAFETY = mp.mpf('0.95')    # pass when bound < SAFETY*pi
NSAMP = 64                 # circle samples (was 8; see "Remaining gap")
MAXDEPTH = 8


def zeta_entire(s):
    """(s-1)*zeta(s) -- entire, so Cauchy's estimate is valid everywhere.
    Same winding as zeta over any box excluding s=1."""
    return (s - mp.mpf(1)) * mp.zeta(s)


def L_chi3(s):
    """L(s, chi_-3) via Hurwitz zeta. Entire for non-principal chi."""
    return mp.mpf(3) ** (-s) * (mp.zeta(s, mp.mpf(1) / 3) - mp.zeta(s, mp.mpf(2) / 3))


_cache = {}


def fval(f, z):
    key = (f.__name__, str(z))
    if key not in _cache:
        _cache[key] = f(z)
    return _cache[key]


def deriv_bound(f, z, pad=PAD, n=NSAMP):
    """Cauchy estimate |f'(z)| <= max_{|w-z|=pad}|f(w)| / pad.
    NOTE: the max is SAMPLED, not bounded -- see module docstring."""
    mx = mp.mpf(0)
    for k in range(n):
        w = z + pad * mp.e ** (1j * 2 * mp.pi * mp.mpf(k) / n)
        v = abs(f(w))
        if v > mx:
            mx = v
    return mx / pad


def check_segment(f, a, b, depth=0):
    """Test |Delta arg f| < pi on [a,b]. Returns (passed, n_subsegments)."""
    h = abs(b - a)
    m = min(abs(fval(f, a)), abs(fval(f, b)))
    d = deriv_bound(f, (a + b) / 2)
    m_lo = m - (h / 2) * d
    if m_lo > 0 and h * d / m_lo < SAFETY * mp.pi:
        return True, 1
    if depth >= MAXDEPTH:
        return False, 1
    c = (a + b) / 2
    o1, n1 = check_segment(f, a, c, depth + 1)
    o2, n2 = check_segment(f, c, b, depth + 1)
    return (o1 and o2), n1 + n2


def run(f, name, per_side, expected):
    corners = [mp.mpc(SIG_LO, -T), mp.mpc(SIG_HI, -T),
               mp.mpc(SIG_HI, T), mp.mpc(SIG_LO, T)]
    print(f"\n=== {name} ===")
    t0 = time.time()

    total, all_ok = 0, True
    for i in range(4):
        a, b = corners[i], corners[(i + 1) % 4]
        n = per_side[i]
        ok_side, sub = True, 0
        for k in range(n):
            p = a + (b - a) * mp.mpf(k) / n
            q = a + (b - a) * mp.mpf(k + 1) / n
            ok, ns = check_segment(f, p, q)
            sub += ns
            ok_side = ok_side and ok
        total += sub
        all_ok = all_ok and ok_side
        print(f"  side {i}: {'pass' if ok_side else 'FAIL':>4}  ({sub} subsegments)")

    pts = []
    for i in range(4):
        a, b = corners[i], corners[(i + 1) % 4]
        n = per_side[i]
        pts.extend(a + (b - a) * mp.mpf(k) / n for k in range(n))
    pts.append(pts[0])
    vals = [fval(f, z) for z in pts]
    args = np.unwrap([float(mp.arg(v)) for v in vals])
    w = (args[-1] - args[0]) / (2 * np.pi)
    minf = min(abs(v) for v in vals)

    print(f"  winding        : {w:.5f}   (expected {expected})")
    print(f"  min|f| contour : {float(minf):.4e}")
    print(f"  subsegments    : {total}")
    print(f"  elapsed        : {time.time() - t0:.0f}s")
    print(f"  --> phase-wrap analysis {'PASSES' if all_ok else 'FAILS'}"
          f" (sampled sup; not a certificate)")
    return all_ok and abs(w - expected) < 0.01


def verify_gap_a_fix():
    """Demonstrate the fix: Cauchy fails for zeta near the pole, holds for (s-1)zeta."""
    print("=== Gap A demonstration (pole vs Cauchy disc) ===")
    z = mp.mpc('0.9', '0.0')
    print(f"  at z = {z}: distance to pole s=1 is {float(abs(z-1)):.3f}, PAD = {float(PAD)}")
    cb = deriv_bound(mp.zeta, z)
    tb = abs(mp.diff(mp.zeta, z))
    print(f"  zeta       : claimed |f'| <= {float(cb):8.3f}   actual {float(tb):8.3f}"
          f"   -> {'VIOLATED' if tb > cb else 'ok'}")
    cb2 = deriv_bound(zeta_entire, z)
    tb2 = abs(mp.diff(zeta_entire, z))
    print(f"  (s-1)*zeta : claimed |f'| <= {float(cb2):8.3f}   actual {float(tb2):8.3f}"
          f"   -> {'VIOLATED' if tb2 > cb2 else 'ok'}")


if __name__ == '__main__':
    print("Phase-wrap analysis for the argument-principle zero count")
    print(f"Box: {float(SIG_LO)} < Re(s) < {float(SIG_HI)}, |Im(s)| < {float(T)}")
    print("STATUS: strong numerical evidence, NOT a certified proof.\n")
    verify_gap_a_fix()
    r1 = run(zeta_entire, '(s-1)*zeta(s)', [40, 400, 40, 700], 26)
    r2 = run(L_chi3, 'L(s, chi_-3)', [60, 420, 60, 900], 44)
    print("\n" + "=" * 62)
    print(f"zeta count 26: {'passes' if r1 else 'fails'} | "
          f"L count 44: {'passes' if r2 else 'fails'}")
    print("Both consistent with all zeros in the box lying on Re(s)=1/2.")
    print("This is NOT a proof: the Cauchy bound uses a sampled supremum.")
    print("The paper's hedged wording is the correct description.")
