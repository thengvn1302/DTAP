# Feature Selection via Nonlinear Split Feasibility (DTAP)

Feature selection cast as a single nonlinear split-feasibility problem on the
probability simplex and solved by **DTAP** (Dual-Track Adaptive Projection).
Three box constraints are taken directly from two published models:

```
F1(w) = ||I - sum_k w_k R_k(D)||^2   (convex,        Model II — AFRSFCV)
F2(w) = ||1 - P w||^2                (convex,        Model II — AFRSFCV)
F3(w) = (w^T G w) / (rho^T w)        (pseudoconvex,  Model I  — fractional)
```

DTAP runs a Polyak step on the convex track {F1, F2}, a safe diminishing step on
the pseudoconvex track {F3}, mixes them by their violation share, and projects
onto the simplex — needing no Lipschitz constant and no projection onto Omega.

## Layout

```text
src/
  common/              consts (paths, Method enum, registry), config, logging, hashes (SHA256SUMS)
  data_processors/     dataset loading + scaling
  problem_formulation/ what the problem IS
    matrices.py          fuzzy rough-set + Fisher/redundancy matrices (inputs of F)
    constraints.py       F1/F2/F3 values and gradients
    thresholds.py        box Omega (b) — DATC + Dirichlet-sampled thresholds
    simplex.py           base set K (projection) + cumulative-weight selection
    problems.py          problem adapters: feature selection on the simplex, test (47) on a box
  solvers/             how the problem is SOLVED
    base.py              Solver ABC + SolverResult
    dtap.py afrsfcv.py nfscore.py hu2022.py  + build_solver() factory
  evaluation/          comparison, convergence (+ table6), stats, metrics, curves, synthetic (test (47))
run_all.py             CLI entry point
SHA256SUMS             hashes of every code, data and result file
results/               saved outputs (see "Saved results")
```

## Setup

```bash
conda activate hust-moe        # numpy, scikit-learn, scipy, pandas, matplotlib
export PYTHONPATH=.            # so `import src...` resolves from the project root
```

Environment of the saved results in `results/`: Python 3.13.4, NumPy 2.1.3, SciPy 1.15.3,
scikit-learn 1.6.1, pandas 2.3.3, matplotlib 3.10.3, Windows 11, default number of BLAS threads
(OpenBLAS 0.3.27).

## Checking the package

```bash
sha256sum -c SHA256SUMS            # Linux / Git Bash
python run_all.py hashes --check   # any OS; also reports files not listed
python run_all.py all --reuse      # runs every step, reusing the saved per-dataset results
```

## Measured cost (this machine: 7.4 GB RAM, about 1-2.5 GB free during the runs)

Wall time / peak resident memory of the process:

| Command | Datasets | Wall time | Peak memory |
|---|---|---|---|
| `comparison` | Glass, Diabetes, Segmentation, Abalone, Yeast, Movement_libras | 283.5 s | 0.42 GB |
| `comparison` | Spambase / Satimage / Pendigits | 389.5 / 691.5 / 1199.2 s | 0.49 / 0.80 / 1.96 GB |
| `hu2022` | the six light datasets (per dataset 11-128 s) | 297.1 s | 0.67 GB |
| `hu2022` | Spambase / Satimage / Pendigits | 300.9 / 462.6 / 869.8 s | 0.78 / 1.39 / 3.60 GB |
| `synthetic` | test (47) | 29.0 s | 0.20 GB |
| `synthetic --dtap-sweep` | test (47) | 6.6 s | 0.16 GB |
| `stats`, `q1`, `hashes`, `hu2022 --assemble-only` | - | 3-6 s | < 0.35 GB |
| `all --reuse` | every step, reusing the saved datasets | 43.2 s | 0.46 GB |

A full `python run_all.py all` therefore takes about 1.3 hours on this machine and needs about 3.6 GB of
free memory (Pendigits in `hu2022`).

The feature oracles of this package use the uncompressed formulas. Evaluation counts do not depend on
this, but solver times do: the nine tuning searches of `hu2022` take 179 744 evaluated points and
532.8 s of solver time here, whereas the solver times reported in the paper were measured with
compressed quadratic-form oracles.

## Witnesses, tuning records and threshold metadata

- `results/witnesses/feature_witnesses.json`: for each full-data instance, the witness = among all points
  evaluated by the Table 6 runs (every method, standard and random starts), the point with the largest
  slack min_i (b_i - F_i(w)), re-evaluated on matrices rebuilt from the data. The file gives w, F(w), b,
  the slacks, whether all three inequalities hold strictly, and the smallest Fisher score.
- `results/synthetic/witness_47.json`: slacks of the exact witness -e1/10 of test (47) in all nine
  configurations, compared with 19/100, 31/25 and kappa log(300/221).
- `results/hu2022/tuning_records.json`, `results/synthetic/synthetic_tuning.json`: every grid value with its
  successes, evaluations, best residuals and solver time, and the chosen value.
- `results/thresholds/<dataset>_full.json` and `<dataset>_folds.json`: percentile levels and thresholds
  b1, b2, b3 of every instance (full data and every fold).
- Raw trajectories (J, J_cvx, J_ps per evaluated point): `results/hu2022/datasets/*.json.gz`,
  `results/synthetic/*trajectories.json.gz`, `results/hu2022/q2_curves.json`.

## Saved results

`results/` holds every output of Tables 1-8 for all eight classification datasets and all nine
Table 6 instances, the raw trajectories, tuning records, witnesses and threshold metadata. To rebuild
only the combined files from the saved per-dataset results, or to check that the whole pipeline runs,
use `python run_all.py all --reuse`; to recompute everything, use `python run_all.py all`
(about 1.3 hours, see above).

## Drivers

Run from the project root:

| Command | Paper | Output (under `results/`) |
|---|---|---|
| `python run_all.py all [--reuse]` | Tables 1-8 | runs every step below in this order; `--reuse` keeps the datasets already saved |
| `python run_all.py comparison [--datasets ..] [--methods ..] [--skip-existing]` | Tables 2, 3 (raw) | `comparison.{csv,txt}`, `comparison/<dataset>.{csv,txt}`, `comparison/<dataset>_folds.json` (fold masks), `thresholds/<dataset>_folds.json`, curve data |
| `python run_all.py stats` | Tables 1-5, Section 4.3 numbers | `stats/table1..table5.txt`, `stats/section43.txt`, `stats/stats.json` |
| `python run_all.py hu2022 [--datasets ..] [--no-plots] [--skip-existing] [--assemble-only]` | Table 6 and its text | `hu2022/table6.{txt,csv}`, `hu2022/tuning_records.json`, `hu2022/datasets/<dataset>.json.gz` (all runs, raw trajectories), `hu2022/q2_*`, `witnesses/feature_witnesses.json`, `thresholds/<dataset>_full.json` |
| `python run_all.py q1` | (not in the paper) | `curve_{svm,knn}.png` |
| `python run_all.py synthetic [--out DIR]` | Table 7 | `synthetic/{table7.txt, synthetic_runs.csv, synthetic_tuning.json, synthetic_trajectories.json.gz, witness_47.json}` |
| `python run_all.py synthetic --dtap-sweep [--out DIR]` | Table 8 | `synthetic/{table8.txt, synthetic_sweep.csv, synthetic_sweep_trajectories.json.gz}` |
| `python run_all.py hashes [--check]` | - | writes / checks `SHA256SUMS` |

`comparison` and `hu2022` save one file set per dataset and rebuild the combined files from every dataset saved
so far, so large datasets can be run one at a time (`--datasets Pendigits`).
`--datasets` and `--methods` take comma lists (or `all`); method ids are
`n_fscore, afrsfcv, dtap, hu_const, hu_dyn`.

`data/` holds the nine datasets of the paper (eight for Tables 1-5, plus Movement_libras for Table 6).
Tables 4 and 5 are computed from the unrounded scores. Table 6 random starts are Dirichlet(1) samples
from `np.random.default_rng(seed)` (`config.TABLE6_CONFIG`).

## Test problem (47)

`synthetic` runs the nonconvex pseudoconvex test on K = [-2, 2]^d with
F1 = ||x + e1||^2 <= 1, F2 = ||x - e2||^2 <= 9/4, F3 = kappa log(1 + ||x - e1||^2) <= kappa log 3,
for d in {2, 10, 50} and kappa in {0.3, 1, 3} (`config.SYNTHETIC_CONFIG`).
Each configuration is solved from the standard start 1.5 * 1 and three random starts
(`np.random.default_rng`, seeds 2101-2103) by DTAP, balanced DTAP, SG-const (nu = 1e-3),
tuned SG-const, sampled SG-dyn (L_hat from 500 uniform points, seed 42) and tuned SG-dyn.
Tuned variants select nu or c (L = c * L_hat) on the grid 10^{-3}, 10^{-2.5}, ..., 10^{1}
using the tuning starts (seeds 1101-1103).
`--dtap-sweep` changes one DTAP parameter at a time (rho_cvx, delta, and gamma_k = a / (k + 0.5)^s)
for kappa in {0.3, 1} (`config.SYNTHETIC_SWEEP`).

## Methods

| Id | Label | Role |
|---|---|---|
| `dtap` | DTAP | proposed solver |
| `n_fscore` | N-Fscore | Model I baseline (projection neural network) |
| `afrsfcv` | AFRSFCV | Model II baseline (softmax gradient descent) |
| `hu_const` | SG-const | Hu (2022) subgradient, constant step |
| `hu_dyn` | SG-dyn | Hu (2022) subgradient, dynamic step (Holder modulus) |
