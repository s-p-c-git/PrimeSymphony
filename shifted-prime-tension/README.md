# Shifted-Prime Tension: Classification and Spectral Verification

Computational companion to the paper *"The Shifted-Prime Smallest Factor
Function: Classification via Quadratic Field Splitting and Dirichlet Series
Decomposition."*

This project studies the **k-tension function** `T_k(p) = 1/spf(p+k)` (spf =
smallest prime factor) over odd primes `p`, and the partition of primes into
classes `S_k(q) = {p : spf(p+k) = q}`.

## What is established here

| Result | Status | Script |
|---|---|---|
| Classification: `S_k(q)` ↔ `p ≡ −k (mod q)`, splitting via Legendre symbol | Proved (elementary) | `step1` |
| Period-2q law in even k (period 6 for q=3) | Proved | `step1` |
| Canonical k=2: limit orphans = primes splitting in `Z[ω]` | Proved | `step0` |
| Dirichlet decomposition `T_k(s) = Σ_q (1/q) Σ_χ c(q,χ) log L(s,χ) + G(s)` | Proved | (paper) |
| **All zeros of ζ(s) and L(s,χ₋₃) with \|Im s\|<60 on Re(s)=1/2** | **Proved (Turing's method)** | `step4` |
| FFT spectrum of error term matches both zero families (15/15 peaks) | Verified | `step3` |
| Density `π_O/π → 1/2`, decay exponent δ ≈ 0.51 (consistent with GRH) | Verified | `step2` |
| Primes→zeros pipeline: FFT seeds → Newton → exact ordinates | Demonstrated | `step5` |

**Scope note.** This work does **not** prove the Riemann Hypothesis and makes no
claim toward it. The Turing's-method result is a rigorous but *bounded*
verification (|Im s| < 60), exactly the methodology Platt–Trudgian (2021) applied
at scale to ζ(s) alone. The contribution is the systematic shifted-prime
classification and the Dirichlet decomposition, positioned as a variant of the
Alladi (1977) smallest-prime-factor program.

## Setup

```bash
pip install -r requirements.txt
```

## Reproducing every result

Run in order from the `src/` directory. Scripts write arrays to `data/` and
figures to `figures/`.

```bash
cd src

# Step 0 — sieve to 10^7, verify the classification (Theorem 3.3, Corollary 3.5)
python3 step0_sieve_and_classify.py
#   Expected: pi(10^7)=664,579; both Theorem 3.3 checks PASS;
#             0 twins among p=1(mod3).

# Step 1 — full T_k classification table + period-6 law (no inputs needed)
python3 step1_classification_table.py
#   Expected: k=2 SPLITS, k=4 INERT, k=6 EMPTY ... (period 6 in k for q=3).

# Step 2 — density convergence + MCMC fit of decay exponent
python3 step2_density_mcmc.py
#   Expected: delta = 0.51 +/- 0.005, 95% CI ~ [0.50, 0.52]; figure saved.

# Step 3 — FFT spectrum + independent L(s,chi_-3) zeros + peak matching
python3 step3_fft_spectrum.py
#   Expected: all top-15 FFT peaks match a zeta or L(chi-3) zero; figure saved.

# Step 4 — RIGOROUS Turing's-method box (the key theorem)
python3 step4_turing_box.py
#   Expected: winding 26.00000 (zeta) and 44.00000 (L(chi-3));
#             mpmath.nzeros(60)=13 cross-check; heatmap saved.

# Step 5 — primes-to-zeros Newton pipeline (needs step3 outputs)
python3 step5_newton_pipeline.py
#   Expected: 15/15 FFT-seeded Newton iterations converge to <1e-10.
```

Total runtime ≈ 3–4 minutes (step4's heatmap is the slowest piece, ~60s).

## Directory layout

```
shifted-prime-tension/
├── README.md
├── requirements.txt
├── src/                      # all computation
│   ├── _paths.py             # portable data/figures path config
│   ├── step0_sieve_and_classify.py
│   ├── step1_classification_table.py
│   ├── step2_density_mcmc.py
│   ├── step3_fft_spectrum.py
│   ├── step4_turing_box.py
│   └── step5_newton_pipeline.py
├── figures/                  # generated plots
├── data/                     # generated .npy arrays (created on run)
├── paper/                    # LaTeX source (add separately)
└── docs/                     # notes
```

## Key mathematical facts (verified in code)

- **Central identity** behind the classification: for prime `p ≡ a (mod q)`, the
  Kronecker symbol `(d_q/p)` equals `(a/q)`, where `d_q` is the fundamental
  discriminant of conductor `q`. Confirmed across thousands of primes for
  `q = 3,5,7,11,13,17,19` (see `step1` docstring / paper Lemma 3.2).
- **Dedekind factorisation**: `ζ_{Q(√−3)}(s) = ζ(s)·L(s,χ₋₃)`, visible as the
  equal-weight superposition of two zero families in the error-term FFT.

## Acknowledgments

Computational assistance (numerical verification, code generation, literature
scoping) was provided by Claude (Anthropic). All mathematical claims and proofs
are the responsibility of the author.
