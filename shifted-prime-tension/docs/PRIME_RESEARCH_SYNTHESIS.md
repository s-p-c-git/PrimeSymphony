# PrimeSymphony — Research Synthesis & Provable Results

**Researcher / Author:** Sadagopan Chakravarthy (ORCID: 0009-0004-6166-9864) | **Project:** PrimeSymphony
**Companion to:** PRIME_RESEARCH_CONTEXT.md (read that first for framing/guardrails)
**Status:** Consolidated synthesis + two completed Tier-1 deep dives (proven).
All numbers below are MEASURED unless marked "conjectured."

═══════════════════════════════════════════════════════════════════════
PART A — THE SIX-LENS SYNTHESIS
═══════════════════════════════════════════════════════════════════════

## A1. WHAT WAS EXPLORED
Five connected threads:
- **A** Tension function T_k(p)=1/spf(p+k): full value spectrum, ceiling class, partition.
- **B** Algebraic structure of the ceiling class (Eisenstein, quadratic splitting, Dedekind zeta).
- **C** Spectral/analytic side (error term FFT, zeros of ζ and L(χ₋₃), Turing's box, primes↔zeros).
- **D** Seed-function question (are γ_n derivable from prime functions?).
- **E** Cosmological/geometric framing (−1/0/+1, infinity↔infinitesimal).

## A2. WHAT WAS FOUND (measured)
- **Tension spectrum sharply structured.** frac(spf(p+2)=q) is exactly 1/(q−1) for q=3
  (0.4998 measured) but falls below for larger q (sieve effect). NOW DERIVED — see Part B.
- **Ceiling class = Eisenstein split primes.** T(p)=1/3 ⟺ p≡1(3) ⟺ splits in Z[ω].
  ζ_{Q(√−3)}(s)=ζ(s)·L(s,χ₋₃). (Proved; classical.)
- **Exactly-one-maximum theorem** (NEW, proven — see Part B). Every isolated prime has
  max tension 1/3 on EXACTLY one side, determined by p mod 3.
- **Primes↔zeros bridge real and directional.** 60 zeros reconstruct ψ(100) to ±0.14.
- **DECISIVE: γ_n are GUE-distributed, not prime-patterned.** zero-gaps vs prime-gaps
  r=−0.29 (noise); vs GUE density r=+0.68 (match). mean gap 2.52, range [0.85,6.89],
  level repulsion (no gap near 0).
- **−1/0/+1 is real on the LOG axis** with center = the number 1 (not 0). log(1/p)=−log(p)
  reflects primes through the identity. Deeper: functional equation s↔1−s centered Re=1/2.

## A3. WHAT WAS INFERRED
- **Tension hierarchy is a SIEVE CASCADE, not a Galois/field hierarchy.** Earlier conjecture
  (each 1/q → a quadratic field split class) was FALSE for q>3 (those are inert). Correct
  picture: nested sieve (avoid 3, then 5, …); only q=3 coincides with a splitting class.
- **Seed-function dream fails for a DEEP reason.** γ_n are GUE → statistically orthogonal to
  prime arithmetic → no prime seed can generate them. Informative failure: points to
  Hilbert–Pólya (spectral) as the only coherent route.
- **All threads converge on the SPECTRAL interpretation.** Functional-equation symmetry (E),
  GUE statistics (D), L-function pair (B) independently → "γ_n = eigenvalues of an operator."

## A4. WHAT GOT MISSED (now partly fixed)
- ✓ FIXED: two-sided joint distribution (Part B, deep dive #2).
- ✓ FIXED: the sub-1/(q−1) deficits — now derived (Part B, deep dive #1).
- ✓ FIXED: free-side distribution (Part B, LO3) and sum-to-twin check (Part B, LO4).
- STILL OPEN: spectral statistics of L(χ₋₃) zeros directly; whether COMBINED
  {γ_n(ζ)}∪{γ_n(χ₋₃)} looks like ONE GUE spectrum (the key two-function test).
- STILL OPEN: prime-inverse / P(s)=Σp^{−s} side computed quantitatively.
- STILL OPEN: whether tension spectrum is identical across different shifts k.

## A5. FURTHER INVESTIGATION (ranked)
- **Tier 1 (finishable):** ✓ deficit formula DONE; ✓ joint distribution DONE. Both proven below.
- **Tier 2 (the prize):** combined-spectrum pair-correlation test for {γ(ζ)}∪{γ(χ₋₃)} —
  one GUE spectrum or two superposed? First checkable probe toward a two-function operator.
  Then: candidate-operator (Bender-Brody-Müller / Dedekind variant) spectral matching.
- **Tier 3 (foundational):** quantify the infinitesimal mirror via P(s).

## A6. PATTERNS / INTERPOLATION vs EXTRAPOLATION (the core methodological lesson)
- **Trap (measured):** γ_n ~ 12.78·n^0.609 fits first 50 at R²=0.997 (great interpolation) but
  is WRONG extrapolated — true law γ_n ~ 2πn/log n (exponent→1). Power law and n/log n are
  near-identical over one decade, diverge beyond. ANY pattern fit to first few dozen
  primes/zeros MUST be extrapolation-tested before belief. (This is the discarded-documents
  failure genre: fit a constant to a finite range, call it fundamental.)
- **Trap (measured):** tension fractions "~ q^−1.75" is an interpolated fit; the TRUE law is
  the Mertens product (Part B). Power law interpolates; product is the real extrapolant.
- **Reliable (measured):** GUE level repulsion extrapolates — theorem-backed, not a fit.
  The CONTRAST is the lesson: GUE statistics extrapolate; naive power fits don't.
- **Behaviour:** zeros→primes is a convergent sum (extrapolates); primes→zeros needs
  inversion (no closed form). This directional asymmetry is WHY the seed dream fails.

═══════════════════════════════════════════════════════════════════════
PART B — TIER-1 DEEP DIVES (PROVEN, MEASURED AT N = 5×10⁶)
═══════════════════════════════════════════════════════════════════════

## B1. DEEP DIVE #1 — The Tension-Fraction Formula (singular series)

**RESULT (proven, verified to <1% over 348,510 primes):**

  frac( spf(p+2) = q )  =  (1/(q−1)) · ∏_{r prime, 3≤r<q} (r−2)/(r−1)

equivalently, since (1 − 1/(r−1)) = (r−2)/(r−1), the same product written two ways.

**Derivation.** Among primes p, the event q|(p+2) has density 1/(q−1) by the PNT for
arithmetic progressions (p ≡ −2 mod q, one of φ(q)=q−1 admissible classes). For spf(p+2)=q
we additionally need r∤(p+2) for every odd prime r<q. Among primes p with q|(p+2), the
local density that a given smaller prime r does NOT divide p+2 is (r−2)/(r−1) [of the r−1
admissible residues of p mod r, exactly one makes p+2≡0, leaving r−2]. The conditions across
distinct r are asymptotically independent (CRT), so they multiply. This is a Hardy–Littlewood
singular series / local-density product.

**Measured verification (ratio measured/predicted):**
  q=3: 0.9996 | q=5: 1.0009 | q=7: 0.9989 | q=11: 0.9993 | q=13: 1.0021
  q=17: 0.9908 | q=19: 1.0031 | q=23: 0.9942 | q=29: 1.0140 | q=31: 0.9886
All within ~1% (deviations are finite-N sampling + the o(1) in CRT independence).

**Sum check:** Σ_{q<200} frac(q) = 0.8627, approaching 1 − (twin fraction ≈ 0.10) ≈ 0.90,
with slow tail convergence (the series Σ 1/(q−1)·∏ converges slowly). Consistent.

**Status:** This is the explicit local-density law for the tension spectrum. Almost
certainly known to the shifted-prime-factor community (Hardy–Littlewood-type), but now
DERIVED and VERIFIED in-project. Clean, closed-form, correct.

## B2. DEEP DIVE #2 — The Exactly-One-Maximum Theorem (fully proven, NEW framing)

**THEOREM.** For every isolated prime p>3 (both p−2, p+2 composite), exactly ONE of
spf(p−2), spf(p+2) equals 3. Both-equal-3 and neither-equal-3 are impossible.

**PROOF.** Every prime p>3 has p≡1 or p≡2 (mod 3).
  • p≡1(3): p+2≡0(3) and p+2>3 composite ⇒ spf(p+2)=3.  Also p−2≡2(3) ⇒ 3∤(p−2) ⇒ spf(p−2)≠3.
  • p≡2(3): p−2≡0(3) and p−2>3 composite ⇒ spf(p−2)=3.  Also p+2≡1(3) ⇒ 3∤(p+2) ⇒ spf(p+2)≠3.
Either way, exactly one side has spf=3, i.e. tension exactly 1/3. ∎

**Measured (283,586 isolated primes):**
  exactly-one-side-=3: 1.000000 | both: 0.000000 | neither: 0.000000. Perfect.

**COROLLARY (Tension Handedness — a clean binary invariant).**
Every isolated prime carries maximum tension on exactly one side; the side is determined
by p mod 3:
    p ≡ 1 (mod 3)  ⟺  max tension on the RIGHT (p+2 side)  ["right-handed"]
    p ≡ 2 (mod 3)  ⟺  max tension on the LEFT  (p−2 side)  ["left-handed"]
Handedness balance measured: right 0.4998 / left 0.5002 (≈50/50, as Dirichlet predicts).

**The "free side" follows the single-side law.** Given the forced-3 side, the OTHER side's
spf distribution matches the Part-B1 tension law. E.g. for right-handed primes (p≡1 mod3),
the left side spf(p−2): q=5→0.3075, q=7→0.1537, q=11→0.0770, q=13→0.0575 — i.e. the
free side is governed by frac(q)/(1−twin) renormalized over the p≡2(3)-type local densities.

**Joint-distribution structure (the surprise).** The (spf(p−2), spf(p+2)) joint table is NOT
a smooth correlation — it is a near-perfect CROSS: one index is pinned to 3, the other ranges
freely. Independence ratio = 2.0 on the cross arms, 0 in the interior. The Pearson value
(r=−0.064) is misleadingly mild; the Spearman (−0.861) reveals the true near-deterministic
"one side is always 3" structure. (Lesson: rank correlation caught what linear correlation hid.)

**Two-sided tension sum.** T(p−2)+T(p+2)=1/spf(p−2)+1/spf(p+2) has a hard MAXIMUM of
1/3+1/5 = 0.5333 (one side forced to 3, the other can be at best 5), first achieved at p=23
with (spf−,spf+)=(3,5). Measured max = 0.5333 exactly. The "both at 1/3 = 0.667" ceiling is
structurally unreachable.

**Status:** FULLY PROVEN, elementary, and a genuinely clean structural statement. The
"handedness = p mod 3" invariant is the nicest small result the cantilever line has produced.
Likely folklore-adjacent but the framing (isolated-prime handedness as a binary invariant
tracking p mod 3, with the free side following the singular-series law) is a tidy package.

## B3. LEFTOVER LO3 — The Free-Side Distribution (derived & verified)

**RESULT.** For a right-handed isolated prime (p≡1 mod 3, so spf(p+2)=3 is the FORCED side),
the FREE side spf(p−2) follows the DD1 singular series with the r=3 factor REMOVED (3 is
already accounted on the forced side), renormalised to the conditional support:

  P(spf(p−2)=q | right-handed) = norm · (1/(q−1)) · ∏_{5≤r<q prime} (r−2)/(r−1)

where norm ≈ 1.2407 = 1/(sum of the series over its support). The SHAPE is exact —
measured/predicted within 1.5% for all q (q=5: 0.991, q=7: 0.991, q=13: 0.989, q=31: 0.991).

**Methodological note (important).** The raw (un-renormalised) prediction was off by a
CONSTANT factor of 1.24 across every q. A constant-factor discrepancy is ALWAYS a missing
normalisation, never a wrong model — the shape was correct from the start. (This is a clean
live instance of the diagnostic discipline: distinguish constant-factor (normalisation) from
shape (model) errors.)

## B4. LEFTOVER LO4 — Sum-to-(1 − twin-fraction) Check (verified)

**RESULT.** Σ_q frac(spf(p+2)=q) over odd primes q, plus the twin-right fraction, → 1:
  theoretical sum (q<2000) = 0.9027, twin-right fraction = 0.0931, total = 0.9959 → 1.
The small residual is the slow tail of the singular series (converges like the prime-reciprocal
sum). This confirms the DD1 formula is a complete probability distribution over the ceiling
prime q, with the twin primes accounting for the complementary mass.

═══════════════════════════════════════════════════════════════════════
PART C — STANDING NEXT-EXPERIMENT (for the next session)
═══════════════════════════════════════════════════════════════════════

**THE breakaway probe (Tier 2):** Compute the pair-correlation / nearest-neighbour spacing
statistics of the COMBINED zero set {γ_n(ζ)} ∪ {γ_n(χ₋₃)}, sorted by height. Test:
  (i) Does the union look like ONE GUE spectrum (→ single self-adjoint operator plausible)?
  (ii) Or like a SUPERPOSITION of two independent GUE spectra (→ Poisson-like spacing at
       small scale, since independent eigenvalues don't repel across the two families)?
Result (i) would be the first computational evidence FOR a two-function Hilbert–Pólya
operator whose spectrum is the Dedekind-zeta zero set. Result (ii) would say the two
L-functions' zeros are spectrally independent — also informative.
Method: Montgomery pair-correlation + nearest-neighbour spacing histogram vs Wigner surmise
vs Poisson. ~50–100 zeros of each suffice for a first look; mpmath + the existing pipeline.
DISCIPLINE: compute, don't assert. Extrapolation-test any fitted pattern. Mark
ESTABLISHED/OPEN/SPECULATIVE.

═══════════════════════════════════════════════════════════════════════
ONE-LINE STANDING SUMMARY
═══════════════════════════════════════════════════════════════════════
Two clean proven results now in hand (the singular-series tension-fraction law and the
exactly-one-maximum / handedness theorem). The decisive empirical fact is that the zeta
zeros are GUE-distributed and statistically orthogonal to prime arithmetic — which both
explains why no prime-seed formula for γ_n exists and points all roads to the spectral
(Hilbert–Pólya) interpretation. Next checkable step: does {γ(ζ)}∪{γ(χ₋₃)} form one
random-matrix spectrum or two?

---

## Attribution

**Author:** Sadagopan Chakravarthy — ORCID: [0009-0004-6166-9864](https://orcid.org/0009-0004-6166-9864).
All mathematical claims, results, and their correctness are the author's
responsibility. Computational assistance — code, numerical verification, and
drafting — was provided by Claude (Anthropic), credited as an assistant, not as
an author.
