# 5-seed check run (cloud container)

Seeds 43-46 of the classification study (Tables 2-5), run in the cloud container with the package
code of commit d8875da (`config.SEED`), scikit-learn 1.9.1 / NumPy 2.5.3 / SciPy 1.18.1, one BLAS
thread per process. Seed 42 is the saved `results/comparison.csv` of the package.

- `comparison_seed_<s>.csv`: the `comparison.csv` of seed s (all rows, as written by `run_all.py comparison`).
- `seeds_summary.{txt,json}`: mean +- sample std over seeds 42-46 (same computation as `run_all.py seeds`).

This is a cross-check only; the reference run is `python run_all.py seeds` on the machine of the saved
results. Its `results/seeds/seed_<s>/comparison.csv` should match these files up to library versions.

## Comparison with the reference run (commit 1134028, `results/seeds/` of the package)

The reference run (Windows, Python 3.13.4, NumPy 2.1.3, SciPy 1.15.3, scikit-learn 1.6.1, the environment
of the saved results) and this cross-check agree on every voted feature mask, every |A*| and every SVM
accuracy and AUC. The differences are limited to:
- 5-NN accuracy / AUC, mostly of AFRSFCV and N-Fscore (few selected features, many tied distances:
  the neighbour tie-breaking differs between the scikit-learn versions), e.g. Satimage/AFRSFCV seed 43
  54.55 vs 53.69;
- iteration counts of SG-const / SG-dyn on Segmentation (floating-point order), and through one fold
  mask the Nogueira stability of DTAP / SG-dyn on Segmentation, seed 43 (0.7375 vs 0.7305).
The 5-seed summary changes by at most 0.05 in Table 4 (AFRSFCV 5-NN) and not at all in Table 5 or the
Section 4.3 numbers (DTAP stability seed 43: 0.740 vs 0.739). The reference values are those in
`results/seeds/seeds_summary.txt` of the package.
