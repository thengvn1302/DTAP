# 5-seed check run (cloud container)

Seeds 43-46 of the classification study (Tables 2-5), run in the cloud container with the package
code of commit d8875da (`config.SEED`), scikit-learn 1.9.1 / NumPy 2.5.3 / SciPy 1.18.1, one BLAS
thread per process. Seed 42 is the saved `results/comparison.csv` of the package.

- `comparison_seed_<s>.csv`: the `comparison.csv` of seed s (all rows, as written by `run_all.py comparison`).
- `seeds_summary.{txt,json}`: mean +- sample std over seeds 42-46 (same computation as `run_all.py seeds`).

This is a cross-check only; the reference run is `python run_all.py seeds` on the machine of the saved
results. Its `results/seeds/seed_<s>/comparison.csv` should match these files up to library versions.
