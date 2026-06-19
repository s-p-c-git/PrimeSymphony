"""
Step 1 — The T_k(p) = 1/spf(p+k) classification table.

Supports: Theorem 3.3 (Classification), Corollary 3.4 (period-2q law).

For each even shift k and prime q, the limit-q class {p : spf(p+k)=q} is
characterised by p = -k (mod q). Its splitting in Q(sqrt(d_q)) is given by
the Legendre symbol (d_q / (-k mod q)), where d_q is the fundamental
discriminant of conductor q.

Prints the full (k,q) classification table and the q=3 period-6 pattern.
No external inputs; self-contained.
"""
import numpy as np


def fundamental_disc(q):
    """Fundamental discriminant of the quadratic field of conductor q (odd prime q)."""
    return q if q % 4 == 1 else -q


def splitting_status(a, q):
    """Status of class p = a (mod q) in Q(sqrt(d_q)).

    For prime p = a (mod q), the Kronecker symbol (d_q / p) equals (a / q)
    by quadratic reciprocity (d_q has conductor q). The class splits iff a
    is a quadratic residue mod q, tested via Euler's criterion.
    """
    if a % q == 0:
        return 'EMPTY', ''
    sym = pow(a % q, (q - 1) // 2, q)   # 1 if QR, q-1 if non-residue
    status = 'SPLITS' if sym == 1 else 'INERT'
    d_str = str(q) if q % 4 == 1 else f'-{q}'
    return status, f'Q(sqrt({d_str}))'


K_vals = list(range(2, 32, 2))     # even shifts k = 2,4,...,30
Q_vals = [3, 5, 7, 11, 13]

print("=" * 70)
print("T_k(p) = 1/spf(p+k)  CLASSIFICATION TABLE")
print("limit-q class {p : spf(p+k)=q} <=> p = -k (mod q); status in Q(sqrt(d_q))")
print("=" * 70)

header = f"{'k':>3}"
for q in Q_vals:
    header += f" | q={q} a=-k%{q}"
print(header)
print("-" * 70)

for k in K_vals:
    row = f"{k:>3}"
    for q in Q_vals:
        a = (-k) % q
        status, _ = splitting_status(a, q)
        row += f" | a={a} {status[:3]:>5}"
    print(row)

print("\n" + "=" * 50)
print("q=3 DOMINANT CEILING (T=1/3): PERIOD-6 LAW IN k")
print("=" * 50)
print(f"{'k':>3} | {'a=-k%3':>6} | {'status in Q(sqrt(-3))':>22}")
for k in K_vals:
    a = (-k) % 3
    if a == 0:
        s = 'EMPTY (3|k)'
    else:
        s = splitting_status(a, 3)[0]
    print(f"{k:>3} | {a:>6} | {s:>22}")

print("\nKEY FINDING (Corollary 3.4):")
print("  k = 2 (mod 6): p = 1 (mod 3) -> SPLITS in Q(sqrt(-3))  [canonical k=2 case]")
print("  k = 4 (mod 6): p = 2 (mod 3) -> INERT  in Q(sqrt(-3))")
print("  k = 0 (mod 6): EMPTY (only p=3)")
print("  General prime q: period 2q in even k.")
