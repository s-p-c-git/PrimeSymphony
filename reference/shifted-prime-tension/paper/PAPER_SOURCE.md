# Paper Source (Markdown reference)

This is the full paper text in Markdown. Convert to LaTeX in `main.tex`
(see CLAUDE_CODE_INSTRUCTIONS.md, Prompt 6). Title, abstract, theorem
statements, and proofs are final as of packaging.

---

**Title:** The Shifted-Prime Smallest Factor Function: Classification via
Quadratic Field Splitting and Dirichlet Series Decomposition

**MSC 2020:** 11N05, 11N13, 11R11, 11M06

**Keywords:** smallest prime factor, shifted primes, quadratic splitting,
Eisenstein integers, Dirichlet series, L-functions, prime zeta function

---

## Abstract

For an even positive integer k and odd prime p, define the k-tension function
T_k(p) = 1/spf(p+k), where spf denotes the smallest prime factor. We study the
partition of odd primes into classes S_k(q) = {p prime : spf(p+k) = q} for primes
q. We prove that for even k, the class S_k(q) is characterised by the congruence
p ≡ −k (mod q), and its splitting behaviour in the quadratic field Q(√d_q) —
where d_q denotes the fundamental discriminant of conductor q — is determined by
the Legendre symbol (d_q/(−k mod q)). In particular, for the canonical case k=2,
the dominant ceiling class T(p)=1/3 consists exactly of the rational primes
splitting in the Eisenstein integer ring Z[ω], following a strict period-6 law in
k for the q=3 level and period 2q for general prime q. We further prove that the
associated Dirichlet series T_k(s) = Σ_{p>2} T_k(p)·p^{−s} decomposes for
Re(s) > 1 as an explicit sum of logarithms of Dirichlet L-functions, with the
series extending analytically to Re(s) > 1/2. Computational verification via
Fourier analysis of the prime-counting error term and a self-contained Turing's
method box argument confirms the decomposition. To the authors' knowledge, the
systematic study of the family {S_k(q)} and the associated Dirichlet series
decomposition is new, constituting a shifted-prime variant of the
smallest-prime-factor program initiated by Alladi (1977).

---

## NOTE

The full body (Sections 1–7, all theorem statements and proofs, the comparison
table with Alladi's framework, and the reference list) is reproduced in the
conversation that generated this bundle. Paste it section-by-section into
main.tex per Prompt 6. The proofs requiring care for the referee:

- **Lemma 3.2** (discriminant/conductor): for q ≡ 3 (mod 4), −q ≡ 1 (mod 4) so
  the fundamental discriminant is −q with conductor q (not 4q). Both cases reduce
  splitting to p mod q.
- **Theorem 4.1** (decomposition): G(s) converges absolutely for Re(s) > 1 (the
  sieve-correction terms need Re(s) > 1; only the prime-power terms reach
  Re(s) > 1/2). State this precisely — do not claim Re(s) > 1/2 for all of G(s).
- **Outer sum over q**: converges for Re(s) > 1 via the bound q^{1−2σ}, since
  primes in S_k(q) satisfy p ≥ q²−k.
- **Coefficients** c(q,χ) = χ̄(−k mod q)/φ(q) are algebraic (roots of unity over
  φ(q)), not rational — state as "explicitly computable algebraic coefficients."
- **Restrict to even k** explicitly: for odd k, p+k is even so spf=2 and the
  classification degenerates.

## Acknowledgments (required in the paper)

The author thanks Claude (Anthropic) for computational assistance in numerical
verification, code generation, and literature scoping. All mathematical claims
and proofs are the responsibility of the author.
