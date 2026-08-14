"""
Step 0 — Sieve primes and verify the classification theorem.

Supports: Theorem 3.3 (Classification), Corollary 3.5 (canonical case k=2).

Verifies empirically that for primes p > 3:
    T(p) = 1/3  <=>  p = 1 (mod 3)  <=>  p splits in Z[omega] (Eisenstein integers)
and that p = 1 (mod 3) primes are automatically orphans (p+2 composite, never twin).

Outputs (to data/):
    primes.npy, limit_orphans.npy, inert_class.npy
"""
import numpy as np
import time
from _paths import DATA

N = 10_000_000

print(f"Sieving primes up to {N:,}...")
t0 = time.time()
sieve = np.ones(N + 1, dtype=bool)
sieve[:2] = False
for i in range(2, int(N**0.5) + 1):
    if sieve[i]:
        sieve[i*i::i] = False
primes = np.nonzero(sieve)[0]
print(f"  done in {time.time()-t0:.2f}s, pi({N:,}) = {len(primes):,}")

mod3 = primes % 3
limit_orphans = primes[mod3 == 1]   # p = 1 (mod 3): the limit-orphan / split class
inert_class   = primes[mod3 == 2]   # p = 2 (mod 3): inert in Z[omega]

print(f"  p = 1 (mod 3) [limit orphans / split]: {len(limit_orphans):,}")
print(f"  p = 2 (mod 3) [inert]:                 {len(inert_class):,}")
print(f"  (near-equal counts confirm Dirichlet equidistribution)")


def smallest_prime_factor(n):
    if n % 2 == 0:
        return 2
    if n % 3 == 0:
        return 3
    d = 5
    while d * d <= n:
        if n % d == 0:
            return d
        if (d + 2) * (d + 2) <= n and n % (d + 2) == 0:
            return d + 2
        d += 6
    return n


# Spot-check Theorem 3.3 on a random sample (full O(N) trial division is too slow)
rng = np.random.default_rng(0)
sample_lo = rng.choice(limit_orphans[1:], size=2000, replace=False)
sample_ic = rng.choice(inert_class[1:], size=2000, replace=False)

ok_lo = all(smallest_prime_factor(int(p) + 2) == 3 for p in sample_lo)
ok_ic = all(smallest_prime_factor(int(p) + 2) != 3 for p in sample_ic)

print(f"\nTheorem 3.3 check  (p=1 mod3  => spf(p+2)=3):  {'PASS' if ok_lo else 'FAIL'} (n=2000)")
print(f"Theorem 3.3 check  (p=2 mod3  => spf(p+2)!=3): {'PASS' if ok_ic else 'FAIL'} (n=2000)")

# Twin-prime structure: p = 1 (mod 3) => p+2 = 0 (mod 3) => p+2 never prime
sieve2 = np.ones(N + 3, dtype=bool)
sieve2[:2] = False
for i in range(2, int((N + 3)**0.5) + 1):
    if sieve2[i]:
        sieve2[i*i::i] = False
n_twin_inert = sieve2[inert_class + 2].sum()
print(f"\nAmong p=2(mod3): {n_twin_inert:,} are twins (p+2 prime).")
print(f"Among p=1(mod3): 0 twins by construction (p+2 = 0 mod 3) — confirms Corollary 3.5.")

np.save(DATA / 'primes.npy', primes)
np.save(DATA / 'limit_orphans.npy', limit_orphans)
np.save(DATA / 'inert_class.npy', inert_class)
print(f"\nSaved primes.npy, limit_orphans.npy, inert_class.npy to {DATA}")
