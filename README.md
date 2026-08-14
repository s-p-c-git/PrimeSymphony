# Prime Symphony
## A Tryst with AI and the Riemann Hypothesis

### The Cantilever Beam of Number Theory 📐

> **Scope / disclaimer.** This top-level project is an *exploratory, heuristic*
> study that models prime distribution through a physical "cantilever beam"
> analogy. It is **not** a proof of the Riemann Hypothesis, and its parallels to
> control theory, quantum chaos, and cosmology are illustrative metaphors rather
> than rigorous theorems. The figures in `images/` and `papers/` are schematic or
> synthetic illustrations — several are rendered from random data in
> `src/visualizations.py` — and should not be read as derived numerical results.
> For this project's rigorous, reproducible, peer-review-targeted contribution,
> see **[`shifted-prime-tension/`](shifted-prime-tension/)**.

## 🧬 Overview

This project explores a Structural Stability *analogy* for the distribution of
prime numbers. By modeling the number line as a physical "Cantilever Beam," it
highlights a subsequence of primes ("Limit Orphans") associated with a small
arithmetic tension limit ($\tau \le 1/3$), and borrows control-theory and
Laplace-transform language as an intuition-building lens. These are heuristics and
visual metaphors meant to motivate the rigorous work in `shifted-prime-tension/` —
not standalone theorems.

## 🚀 Themes explored (heuristic)

1. **The 1/3 Tension Limit**: among isolated "orphan" primes $P$ with $P-2 = 3q$,
   the quantity $q/(3q)$ sits at $1/3$ — an elementary arithmetic observation used
   here as a motivating image, not a deep theorem.

2. **Stability "Flatline"**: a density ratio for these orphans appears to settle
   near a constant related to the twin-prime constant — presented as an empirical
   observation to be made precise in the rigorous subproject.

3. **Damping analogy**: Laplace / control-theory language is used metaphorically to
   describe error dissipation. This is an analogy, **not** a stability proof.

## 📂 Repository Structure

* **`shifted-prime-tension/`**: the rigorous, reproducible subproject — **start here**.
* `papers/`: the exploratory cantilever-beam essay and research log.
* `src/`: Python script that renders the illustrative figures.
* `images/`: high-resolution renderings of those illustrative figures.

## 💻 Reproduction (illustrative figures)

These commands regenerate the schematic/synthetic figures only. For the verified
numerical pipeline, follow `shifted-prime-tension/README.md` instead.

1. Install dependencies:

        pip install -r requirements.txt

2. Render the figures:

        python src/visualizations.py


## Shifted-Prime Tension

The [`shifted-prime-tension/`](shifted-prime-tension/) subproject proves a
classification of the shifted-prime smallest-factor classes
`S_k(q) = {p : spf(p+k) = q}` via splitting in the quadratic fields `Q(√d_q)`, with
the canonical case `k=2` identifying the "limit orphans" as exactly the primes that
split in `Z[ω]`. It pairs this classification with a Dirichlet-series decomposition of
the tension function `T_k(p) = 1/spf(p+k)` and a spectral verification tying the prime
error term to the nontrivial zeros of `ζ(s)` and `L(s, χ₋₃)`.

**Key result.** A high-precision Turing's-method (argument-principle) computation
gives zero counts **consistent with** all zeros of `ζ(s)` and `L(s, χ₋₃)` with
`|Im s| < 60` lying on the critical line `Re(s) = 1/2` (winding numbers 26 and 44;
§5). This is a bounded *numerical* verification, **not a certified proof**, and
makes no claim toward proving the Riemann Hypothesis.

The reproducible pipeline covers all of it: classification + period-6 law (step0/step1),
MCMC density fit `π_O/π → 1/2` with decay exponent δ ≈ 0.51 (step2), FFT spectral match
of the error term to both zero families (step3), the Turing's-method box
(step4/step4b — high-precision numerical, not a proof), and a primes-to-zeros
Newton refinement (step5). It adds two dependencies
beyond this repo's base set — `mpmath` and `sympy` (see
`shifted-prime-tension/requirements.txt`).

See [`shifted-prime-tension/README.md`](shifted-prime-tension/README.md) for the full
result table and step-by-step reproduction commands.

## 📜 Citation

If you use this framework in your research, please cite it using the CITATION.cff file provided.

An investigation by Sadagopan Chakravarthy (ORCID:
[0009-0004-6166-9864](https://orcid.org/0009-0004-6166-9864)), with computational
assistance from Claude (Anthropic). AI was used as a computational assistant, not as
an author or co-author.
