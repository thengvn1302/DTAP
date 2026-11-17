"""Classification study (Tables 1-5) repeated over several seeds (`run_all.py seeds`).

Each seed s re-draws the 80/20 split, the fold partition, the solver seeds (s + fold index), the SVM
calibration and the threshold sampling (config.SEED). The base seed (42, the saved results) is read from
results/comparison.csv; every other seed runs `run_all.py comparison` on the eight classification datasets
in its own directory results/seeds/seed_<s>/ (same outputs as the base run). Datasets already saved there
are skipped, so an interrupted run resumes. The summary results/seeds/seeds_summary.{txt,json} gives

  * per dataset: mean +- sample std over seeds of |A*|, Nogueira stability, accuracy and AUC;
  * Table 4: unweighted mean over the datasets, then mean +- std over seeds;
  * Table 5: exact signed-rank + Holm and Friedman on the seed-averaged dataset scores, and per seed
             the range of the Holm-adjusted p-values and the number of seeds rejecting at 0.05;
  * the Section 4.3 numbers per seed.
The statistics follow src/evaluation/stats.py (majority-vote row, theta = 0.9).
"""
import itertools
import json
import os
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor

import numpy as np
import pandas as pd
from scipy import stats as st

from src.common import config
from src.common.consts import PROJECT_DIR, RESULTS_DIR

SEEDS_DIR = os.path.join(str(RESULTS_DIR), "seeds")
BASE_SEED = 42                       # seed of the saved results in results/
DATASETS = list(config.CLASSIFICATION_DATASETS)
SELECTORS = ["n_fscore", "afrsfcv", "dtap", "hu_const", "hu_dyn"]
BASELINES = ["n_fscore", "afrsfcv", "hu_const", "hu_dyn"]
LABELS = {"full": "Full", "n_fscore": "N-Fscore", "afrsfcv": "AFRSFCV", "dtap": "DTAP",
          "hu_const": "SG-const", "hu_dyn": "SG-dyn"}
METRICS = [("svm_acc", "Accuracy, SVM", 2), ("knn_acc", "Accuracy, 5-NN", 2),
           ("svm_roc", "AUC, SVM", 4), ("knn_roc", "AUC, 5-NN", 4)]


def signed_rank_exact(d):
    d = np.asarray(d, float)
    d = d[d != 0]
    n = len(d)
    if n == 0:
        return 1.0
    ranks = st.rankdata(np.abs(d))
    total = ranks.sum()
    observed = min(ranks[d > 0].sum(), total - ranks[d > 0].sum())
    hits = sum(1 for s in itertools.product((0, 1), repeat=n)
               if min(np.dot(s, ranks), total - np.dot(s, ranks)) <= observed + 1e-9)
    return hits / 2 ** n


def holm(p):
    order = np.argsort(p, kind="stable")
    adj, running = [0.0] * len(p), 0.0
    for i, j in enumerate(order):
        running = max(running, min(1.0, (len(p) - i) * p[j]))
        adj[j] = running
    return adj


def _majority_rows(csv):
    df = pd.read_csv(csv)
    df = df[np.isclose(df.theta, 0.9) & (df.vote_threshold == df.outer_folds // 2 + 1)]
    missing = [d for d in DATASETS if d not in set(df.dataset)]
    if missing:
        raise SystemExit(f"{csv}: missing datasets {missing}")
    return df.set_index("dataset").loc[DATASETS]


def col(method, metric):
    return f"raw_{metric}" if method == "full" else f"{method}_{metric}"


def tests(score):  # score[method][metric] -> array over datasets
    out = {}
    for met, _, _ in METRICS:
        raw = [signed_rank_exact(score["dtap"][met] - score[b][met]) for b in BASELINES]
        fried = float(st.friedmanchisquare(*[score[m][met] for m in SELECTORS]).pvalue)
        out[met] = dict(raw=raw, holm=holm(raw), friedman=fried)
    return out


def _seed_csv(seed: int, rerun_base: bool) -> str:
    if seed == BASE_SEED and not rerun_base:
        return os.path.join(str(RESULTS_DIR), "comparison.csv")
    return os.path.join(SEEDS_DIR, f"seed_{seed}", "comparison.csv")


def _run_one(seed: int, threads_one: bool) -> int:
    out = os.path.join(SEEDS_DIR, f"seed_{seed}")
    os.makedirs(out, exist_ok=True)
    env = dict(os.environ, FFS_SEED=str(seed), FFS_RESULTS_DIR=out, MPLBACKEND="Agg")
    if threads_one:
        for k in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
            env.setdefault(k, "1")
    cmd = [sys.executable, str(PROJECT_DIR / "run_all.py"), "comparison",
           "--datasets", ",".join(DATASETS), "--skip-existing"]
    print(f"  seed {seed}: running -> {out} (log: run.log)", flush=True)
    with open(os.path.join(out, "run.log"), "a", encoding="utf-8") as log:
        rc = subprocess.call(cmd, cwd=str(PROJECT_DIR), env=env, stdout=log, stderr=subprocess.STDOUT)
    print(f"  seed {seed}: finished (exit code {rc})", flush=True)
    return rc


def run_seeds(seeds=None, jobs: int = 1, rerun_base: bool = False, summary_only: bool = False) -> int:
    seeds = sorted({int(s) for s in (seeds or config.SEED_LIST)})
    todo = [] if summary_only else [s for s in seeds if s != BASE_SEED or rerun_base]
    if BASE_SEED in seeds and not rerun_base:
        print(f"  seed {BASE_SEED}: using the saved results/comparison.csv")
    if todo:
        with ThreadPoolExecutor(max_workers=max(1, int(jobs))) as ex:
            codes = list(ex.map(lambda s: _run_one(s, jobs > 1), todo))
        if any(codes):
            print(f"  some seeds failed: {dict(zip(todo, codes))}; see results/seeds/seed_<s>/run.log")
            return 1
    csvs = {s: _seed_csv(s, rerun_base) for s in seeds}
    missing = [p for p in csvs.values() if not os.path.isfile(p)]
    if missing:
        print(f"  missing results: {missing}")
        return 1
    summarize({s: _majority_rows(p) for s, p in csvs.items()}, SEEDS_DIR)
    return 0


def summarize(seeds: dict, out_dir: str) -> dict:
    S = sorted(seeds)
    os.makedirs(out_dir, exist_ok=True)
    pm = lambda v, d: f"{np.mean(v):.{d}f} +- {np.std(v, ddof=1):.{d}f}"
    L, J = [], {"seeds": S}

    # ---- per-dataset table (Tables 2 and 3) ----
    L.append(f"Seeds: {S}   (mean +- sample std over seeds; majority vote, theta = 0.9)\n")
    L.append("Table 2 (per dataset): |A*|  /  Nogueira stability")
    L.append(f"{'Dataset':14s}" + "".join(f"{LABELS[m]:>28s}" for m in SELECTORS))
    J["table2"] = {}
    for d in DATASETS:
        cells, J["table2"][d] = [], {}
        for m in SELECTORS:
            ns = [seeds[s].loc[d, f"{m}_n_sel"] for s in S]
            st_ = [seeds[s].loc[d, f"{m}_nogueira"] for s in S]
            J["table2"][d][m] = dict(n_sel=ns, stability=st_)
            cells.append(f"{pm(ns, 1)} / {pm(st_, 3)}")
        L.append(f"{d:14s}" + "".join(f"{c:>28s}" for c in cells))

    L.append("\nTable 3 (per dataset): accuracy (%) and macro OvR AUC")
    J["table3"] = {}
    for met, lab, dec in METRICS:
        L.append(f"  {lab}")
        L.append(f"  {'Dataset':14s}" + "".join(f"{LABELS[m]:>18s}" for m in ["full"] + SELECTORS))
        for d in DATASETS:
            vals = {m: [float(seeds[s].loc[d, col(m, met)]) for s in S] for m in ["full"] + SELECTORS}
            J["table3"].setdefault(d, {})[met] = vals
            L.append(f"  {d:14s}" + "".join(f"{pm(vals[m], dec):>18s}" for m in ["full"] + SELECTORS))

    # ---- Table 4 ----
    L.append("\nTable 4: unweighted mean over the 8 datasets; mean +- std over seeds")
    L.append(f"{'Method':10s}" + "".join(f"{lab:>20s}" for _, lab, _ in METRICS))
    J["table4"] = {}
    for m in ["full"] + SELECTORS:
        row = {met: [float(seeds[s][col(m, met)].mean()) for s in S] for met, _, _ in METRICS}
        J["table4"][m] = row
        L.append(f"{LABELS[m]:10s}" + "".join(f"{pm(row[met], dec):>20s}" for met, _, dec in METRICS))

    # ---- Table 5 ----
    avg = {m: {met: np.mean([seeds[s][col(m, met)].to_numpy(float) for s in S], axis=0)
               for met, _, _ in METRICS} for m in ["full"] + SELECTORS}
    t_avg = tests(avg)
    per_seed = {s: tests({m: {met: seeds[s][col(m, met)].to_numpy(float) for met, _, _ in METRICS}
                          for m in ["full"] + SELECTORS}) for s in S}
    J["table5_seed_averaged"] = t_avg
    J["table5_per_seed"] = {str(s): v for s, v in per_seed.items()}
    L.append("\nTable 5 (seed-averaged dataset scores): raw / Holm-adjusted exact signed-rank p; Friedman")
    L.append(f"{'Metric':16s}" + "".join(f"{LABELS[b]:>16s}" for b in BASELINES) + f"{'Friedman':>10s}")
    for met, lab, _ in METRICS:
        r = t_avg[met]
        L.append(f"{lab:16s}" + "".join(f"{a:.4f}/{h:.4f}".rjust(16) for a, h in zip(r['raw'], r['holm']))
                 + f"{r['friedman']:>10.4f}")
    L.append("\nTable 5 per seed: range [min, max] of the Holm-adjusted p over seeds; seeds rejecting at 0.05")
    for met, lab, _ in METRICS:
        cells = []
        for j, b in enumerate(BASELINES):
            h = [per_seed[s][met]["holm"][j] for s in S]
            cells.append(f"[{min(h):.3f},{max(h):.3f}] {sum(x < 0.05 for x in h)}/{len(S)}")
        L.append(f"{lab:16s}" + "".join(f"{c:>22s}" for c in cells))

    # ---- Section 4.3 numbers ----
    sec = {}
    for s in S:
        r = seeds[s]
        frac = (r["dtap_n_sel"] / r["m"]).mean() * 100
        sg_equal = [d for d in DATASETS if r.loc[d, "hu_const_voted_feat"] == r.loc[d, "dtap_voted_feat"]
                    and r.loc[d, "hu_dyn_voted_feat"] == r.loc[d, "dtap_voted_feat"]]
        sec[s] = dict(
            dtap_mean_retained_pct=float(frac),
            dtap_mean_stability=float(r["dtap_nogueira"].mean()),
            nfscore_mean_stability=float(r["n_fscore_nogueira"].mean()),
            full_minus_dtap_svm=float(r["raw_svm_acc"].mean() - r["dtap_svm_acc"].mean()),
            full_minus_dtap_knn=float(r["raw_knn_acc"].mean() - r["dtap_knn_acc"].mean()),
            dtap_minus_nfscore_svm=float(r["dtap_svm_acc"].mean() - r["n_fscore_svm_acc"].mean()),
            dtap_minus_afrsfcv_svm=float(r["dtap_svm_acc"].mean() - r["afrsfcv_svm_acc"].mean()),
            n_sg_mask_equal=len(sg_equal))
    J["section43"] = {str(s): v for s, v in sec.items()}
    L.append("\nSection 4.3 numbers: per seed, then mean +- std")
    keys = list(next(iter(sec.values())).keys())
    L.append(f"{'':26s}" + "".join(f"{s:>9d}" for s in S) + "   mean +- std")
    for k in keys:
        v = [sec[s][k] for s in S]
        L.append(f"{k:26s}" + "".join(f"{x:>9.3f}" for x in v) + f"   {pm(v, 3)}")

    with open(os.path.join(out_dir, "seeds_summary.txt"), "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")
    with open(os.path.join(out_dir, "seeds_summary.json"), "w", encoding="utf-8") as f:
        json.dump(J, f, indent=1, default=float)
    print("\n".join(L))
    print(f"\n  Saved: {os.path.join(out_dir, 'seeds_summary.txt')}")
    return J

