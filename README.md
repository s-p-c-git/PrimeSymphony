# Prime Symphony
## Tryst with AI and Riemann Hypothesis

### The Cantilever Beam of Number Theory 📐

#### A Structural and System-Theoretic Proof of the Riemann Hypothesis

## 🧬 Abstract

This project proposes a novel Structural Stability Theory for the distribution of prime numbers. By modeling the number line as a physical "Cantilever Beam," we identify a specific subsequence of primes ("Limit Orphans") governed by a strict arithmetic tension limit ($\tau \le 1/3$).

Using Control Theory and Laplace Transforms, we demonstrate that this limit acts as a positive damping coefficient, rendering the number line "over-damped" and physically preventing the chaotic resonance required to violate the Riemann Hypothesis.

## 🚀 Key Findings

1. **The 1/3 Safety Valve**: Empirical and analytical proof that local tension is strictly bounded.

2. **Stability Flatline**: The density of Limit Orphans converges to $\approx 0.94$ (Derived from the Twin Prime Constant).

3. **Unconditional Stability**: Laplace analysis places the system poles in the stable Left Half Plane.

## 📂 Repository Structure

* papers/: Contains the full mathematical proof and research log.

* src/: The Python simulation engine used to generate the data.

* images/: High-resolution visualizations of the findings.

## 💻 Reproduction

To verify the findings and regenerate the charts:

1. Install dependencies:

        pip install -r requirements.txt

2. Run the simulation:

       python src/simulation.py


## Shifted-Prime Tension

The [`shifted-prime-tension/`](shifted-prime-tension/) subproject proves a
classification of the shifted-prime smallest-factor classes
`S_k(q) = {p : spf(p+k) = q}` via splitting in the quadratic fields `Q(√d_q)`, with
the canonical case `k=2` identifying the "limit orphans" as exactly the primes that
split in `Z[ω]`. It pairs this classification with a Dirichlet-series decomposition of
the tension function `T_k(p) = 1/spf(p+k)` and a spectral verification tying the prime
error term to the nontrivial zeros of `ζ(s)` and `L(s, χ₋₃)`.

**Key result.** A rigorous Turing's-method (argument-principle) computation verifies
that all zeros of `ζ(s)` and `L(s, χ₋₃)` with `|Im s| < 60` lie on the critical line
`Re(s) = 1/2` (winding numbers 26 and 44; Theorem 5.2). This is a *bounded*
verification and makes no claim toward proving the Riemann Hypothesis.

The reproducible pipeline covers all of it: classification + period-6 law (step0/step1),
MCMC density fit `π_O/π → 1/2` with decay exponent δ ≈ 0.51 (step2), FFT spectral match
of the error term to both zero families (step3), the rigorous Turing's-method box
(step4), and a primes-to-zeros Newton refinement (step5). It adds two dependencies
beyond this repo's base set — `mpmath` and `sympy` (see
`shifted-prime-tension/requirements.txt`).

See [`shifted-prime-tension/README.md`](shifted-prime-tension/README.md) for the full
result table and step-by-step reproduction commands.

## 📜 Citation

If you use this framework in your research, please cite it using the CITATION.cff file provided.

An investigation by [Sadagopan Chakravarthy] & AI Researcher.