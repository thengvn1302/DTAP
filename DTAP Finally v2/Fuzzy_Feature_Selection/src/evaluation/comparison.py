"""Outer hold-out + K-fold comparison of all solvers on each dataset.

For every dataset:
  1. Stratified 80/20 hold-out (test set never seen during CV).
  2. K-fold CV on the train pool: each fold runs every solver -> weight vector
     -> theta cut. Only feature sets are recorded (no SVM/KNN inside CV).
  3. Majority vote: keep a feature selected in >= vote_threshold folds.
  4. Train on the full pool with voted features, score on the hold-out.
  5. Accuracy-vs-#features curves from the fold-averaged weight vector.
"""
import os
import sys
from typing import List

import numpy as np
import pandas as pd
from sklearn.model_selection import StratifiedKFold, train_test_split

from src.common import config
from src.common.consts import RESULTS_DIR, Method, method_label
from src.data_processors.loaders import load_dataset, scale_train_test
from src.evaluation.curves import aggregate_topk_curves, plot_all_curves, save_curve_data, topk_accuracy_curve
from src.evaluation.metrics import mean_std, nogueira_stability, score_fold
from src.problem_formulation.matrices import build_matrices
from src.problem_formulation.simplex import select_features
from src.solvers import build_solver
from src.problem_formulation.thresholds import build_threshold_config, dataset_adaptive_config, prepare_from_prep


def _print_safe(text: str) -> None:
    try:
        print(text, flush=True)
    except UnicodeEncodeError:
        sys.stdout.buffer.write((text + "\n").encode("utf-8", errors="replace"))
        sys.stdout.flush()


def _comparison_methods() -> List[Method]:
    return list(getattr(config, "COMPARISON_METHODS", list(Method)))


def _vote_thr_list(n_folds: int) -> list:
    majority = n_folds // 2 + 1
    cfg = getattr(config, "VOTE_THRESHOLD_LIST", None)
    if cfg is None:
        return list(range(majority, n_folds + 1))
    valid = sorted({int(v) for v in cfg if majority <= int(v) <= n_folds})
    return valid or [majority]


def _effective_folds(y: np.ndarray, requested: int) -> int:
    counts = np.bincount(y)
    return max(2, min(requested, int(counts[counts > 0].min())))


def _pm(mean: float, std: float, d: int = 2) -> str:
    return f"{mean:.{d}f} ± {std:.{d}f}"


def _solve_weights(method: Method, prep: dict, prepared: dict, seed: int,
                   X_train=None, y_train=None):
    """Build and run the solver. Returns (w, time_sec, iter_count)."""
    solver = build_solver(method, prep, prepared["thresholds"],
                          X_train=X_train, y_train=y_train, seed=seed)
    res = solver.solve(w_init=prepared["w_init"], seed=seed)
    return res.w, float(res.time_sec), int(res.iter_count)


def run_single_dataset(name: str, cfg_entry: dict, theta_list=None, verbose: bool = True) -> dict:
    methods = _comparison_methods()
    theta_list = [float(t) for t in (theta_list or config.THETA_LIST)]

    X_raw, y = load_dataset(name, cfg_entry)
    n, m = X_raw.shape
    r = len(np.unique(y))

    if config.USE_DATC:
        adp = dataset_adaptive_config(n, m, r, np.bincount(y))
        threshold_cfg = build_threshold_config(adp)
    else:
        threshold_cfg = config.THRESHOLD_CONFIG

    # ── 1. Hold-out split ──
    test_frac = float(getattr(config, "TEST_FRACTION", 0.2))
    pool_idx, test_idx = train_test_split(
        np.arange(n), test_size=test_frac, stratify=y, random_state=42)
    X_pool, X_test = scale_train_test(X_raw[pool_idx], X_raw[test_idx])
    y_pool, y_test = y[pool_idx], y[test_idx]
    n_pool, n_test = len(y_pool), len(y_test)

    # ── 2. K-fold CV on the train pool (feature selection only) ──
    n_folds = _effective_folds(y_pool, config.N_FOLDS)
    vote_thr_list = _vote_thr_list(n_folds)
    majority = n_folds // 2 + 1
    skf = StratifiedKFold(n_splits=n_folds, shuffle=True, random_state=42)

    wl = {mth: {"time": [], "iters": [], "tpi": []} for mth in methods}
    feature_votes = {mth: {t: np.zeros(m, dtype=int) for t in theta_list} for mth in methods}
    fold_selections = {mth: {t: np.zeros((n_folds, m), dtype=int) for t in theta_list} for mth in methods}
    avg_w = {mth: np.zeros(m) for mth in methods}
    fold_thresholds = []
    max_lbl = max(len(method_label(mth)) for mth in methods)

    text = [
        f"Dataset: {name} - {cfg_entry.get('purpose', '')}",
        "",
        f" theta_list={theta_list}",
        "=" * 60,
        f" outer_folds={n_folds}  vote_thresholds={vote_thr_list}"
        f"  test_fraction={test_frac:.0%}  n_pool={n_pool}  n_test={n_test}",
        "Chi tiet tung fold (chon dac trung - khong danh gia SVM/KNN):",
    ]

    for fold_idx, (tr, _) in enumerate(skf.split(X_pool, y_pool), start=1):
        Xtr, ytr = X_pool[tr], y_pool[tr]
        seed = 42 + fold_idx

        prep = build_matrices(Xtr, ytr)
        prepared = prepare_from_prep(prep, threshold_cfg)
        thr = prepared["thresholds"]
        fold_thresholds.append(dict(fold=fold_idx, n_train=int(len(tr)),
                                    b1=float(thr["b1"]), b2=float(thr["b2"]), b3=float(thr["b3"])))

        text.append(
            f"  [Fold {fold_idx}/{n_folds}] | "
            f"b=(b1={thr['b1']:.6g}, b2={thr['b2']:.6g}, b3={thr['b3']:.6g})")

        weights = {}
        for mth in methods:
            w, t_sec, it = _solve_weights(mth, prep, prepared, seed, X_train=Xtr, y_train=ytr)
            weights[mth] = w
            avg_w[mth] += w
            wl[mth]["time"].append(t_sec)
            wl[mth]["iters"].append(it)
            wl[mth]["tpi"].append(t_sec / max(it, 1))
            lbl = f"{method_label(mth)}:"
            text.append(f"      {lbl:<{max_lbl + 2}} time={t_sec:.3f}s   iters={it}")

        for t in theta_list:
            text.append(f"    theta={t:g}:")
            for mth in methods:
                idx, n_sel = select_features(weights[mth], t)
                feature_votes[mth][t][idx] += 1
                fold_selections[mth][t][fold_idx - 1, idx] = 1
                lbl = f"{method_label(mth)}:"
                text.append(f"      {lbl:<{max_lbl + 2}} |A*|={n_sel:<3}  feat={sorted(idx.tolist())}")

    for mth in methods:
        avg_w[mth] /= n_folds

    nogueira_score = {
        mth: {t: nogueira_stability(fold_selections[mth][t]) for t in theta_list}
        for mth in methods
    }

    # ── 3. Solver timing summary ──
    raw_svm, raw_knn, raw_svm_roc, raw_knn_roc = score_fold(
        X_pool, y_pool, X_test, y_test, np.arange(m))

    timing_by_mth, t_entries = {}, []
    for mth in methods:
        tm_m, tm_s = mean_std(wl[mth]["time"])
        it_m, it_s = mean_std(wl[mth]["iters"])
        tp_m, tp_s = mean_std(wl[mth]["tpi"])
        timing_by_mth[mth] = dict(tm_m=tm_m, tm_s=tm_s, it_m=it_m, it_s=it_s, tp_m=tp_m, tp_s=tp_s)
        t_entries.append(dict(
            mth=mth,
            time_str=f"{_pm(tm_m, tm_s, 3)}s",
            iters_str=_pm(it_m, it_s, 1),
            tpi_str=f"{_pm(tp_m * 1e3, tp_s * 1e3, 4)}ms",
        ))

    w_time = max(len(e["time_str"]) for e in t_entries)
    w_iters = max(len(e["iters_str"]) for e in t_entries)
    w_tpi = max(len(e["tpi_str"]) for e in t_entries)

    text += ["", "Trung binh tren CV folds:"]
    for e in t_entries:
        lbl = f"{method_label(e['mth'])}:"
        text.append(
            f"  {lbl:<{max_lbl + 2}} time={e['time_str']:<{w_time}}"
            f"  iters={e['iters_str']:<{w_iters}}"
            f"  time/iter={e['tpi_str']:<{w_tpi}}")

    # ── 4. Vote + evaluate on hold-out ──
    def _roc_fmt(v):
        return f"{v:.4f}" if v == v else "   N/A"

    text += ["",
             f"Ket qua bau chon va danh gia tren hold-out test (n={n_test}):",
             f"Raw ({m} dac trung): SVM={raw_svm:.2f}  KNN={raw_knn:.2f}"
             f"  SVM-ROC={_roc_fmt(raw_svm_roc)}  KNN-ROC={_roc_fmt(raw_knn_roc)}"]

    rows = []
    for t in theta_list:
        text.append(f"theta = {t:g}")
        for vote_thr in vote_thr_list:
            suffix = " (majority)" if vote_thr == majority else (" (unanimous)" if vote_thr == n_folds else "")
            text.append(f"  vote>={vote_thr}/{n_folds}{suffix}:")

            row = dict(
                dataset=name, n=n, m=m, r=r, n_pool=n_pool, n_test=n_test,
                outer_folds=n_folds, vote_threshold=vote_thr,
                test_fraction=test_frac, knn_k=config.KNN_K, theta=t,
                raw_svm_acc=raw_svm, raw_knn_acc=raw_knn,
                raw_svm_roc=raw_svm_roc, raw_knn_roc=raw_knn_roc,
            )
            for mth in methods:
                votes = feature_votes[mth][t]
                voted_idx = np.where(votes >= vote_thr)[0]
                if len(voted_idx) == 0:
                    voted_idx = np.array([int(np.argmax(votes))])
                n_voted = len(voted_idx)
                sv, kn, sv_roc, kn_roc = score_fold(X_pool, y_pool, X_test, y_test, voted_idx)
                et = timing_by_mth[mth]
                nog = nogueira_score[mth][t]
                key = mth.value
                row.update({
                    f"{key}_voted_feat": str(sorted(voted_idx.tolist())),
                    f"{key}_n_sel": n_voted,
                    f"{key}_svm_acc": sv,
                    f"{key}_knn_acc": kn,
                    f"{key}_svm_roc": sv_roc,
                    f"{key}_knn_roc": kn_roc,
                    f"{key}_nogueira": nog,
                    f"{key}_time_mean": et["tm_m"],
                    f"{key}_time_std": et["tm_s"],
                    f"{key}_iters_mean": et["it_m"],
                    f"{key}_iters_std": et["it_s"],
                    f"{key}_time_per_iter_mean": et["tp_m"],
                    f"{key}_time_per_iter_std": et["tp_s"],
                })
                lbl = f"{method_label(mth)}:"
                text.append(
                    f"    {lbl:<{max_lbl + 2}} |A*|={n_voted:<3}"
                    f"  SVM={sv:6.2f}  KNN={kn:6.2f}"
                    f"  SVM-ROC={_roc_fmt(sv_roc)}  KNN-ROC={_roc_fmt(kn_roc)}"
                    f"  Nogueira={nog:.4f}"
                    f"  voted={sorted(voted_idx.tolist())}")
            rows.append(row)
        text.append("")

    text_str = "\n".join(text).rstrip() + "\n"
    if verbose:
        _print_safe(text_str)

    # ── 5. Curves on hold-out (ranked by avg weight vector) ──
    if config.CURVE_CONFIG.get("enabled", True):
        curve_data = dict(
            n=n, m=m, r=r,
            raw_svm=raw_svm / 100.0,
            raw_knn=raw_knn / 100.0,
            methods={
                mth.value: aggregate_topk_curves(
                    [topk_accuracy_curve(avg_w[mth], X_pool, y_pool, X_test, y_test,
                                         config.SVM_PARAMS, config.KNN_K)],
                    m)
                for mth in methods
            },
        )
        save_curve_data(name, curve_data)

    meta = dict(dataset=name, n=n, p=m, r=r, n_pool=n_pool, n_test=n_test, n_folds=n_folds,
                percentiles={k: threshold_cfg["sampling_based"][k]
                             for k in ("f1_percentile", "f2_percentile", "f3_percentile")},
                fold_thresholds=fold_thresholds,
                fold_selections={mth.value: {f"{t:g}": fold_selections[mth][t].tolist() for t in theta_list}
                                 for mth in methods})
    return dict(text=text_str, rows=rows, meta=meta)


COMPARISON_DIR = os.path.join(str(RESULTS_DIR), "comparison")


def _save_dataset(name: str, res: dict) -> None:
    """Per-dataset outputs, so the datasets can be run one at a time."""
    import json
    os.makedirs(COMPARISON_DIR, exist_ok=True)
    pd.DataFrame(res["rows"]).to_csv(os.path.join(COMPARISON_DIR, f"{name}.csv"), index=False)
    with open(os.path.join(COMPARISON_DIR, f"{name}.txt"), "w", encoding="utf-8") as f:
        f.write(res["text"])
    with open(os.path.join(COMPARISON_DIR, f"{name}_folds.json"), "w", encoding="utf-8") as f:
        json.dump(res["meta"], f, indent=1)
    thr_dir = os.path.join(str(RESULTS_DIR), "thresholds")
    os.makedirs(thr_dir, exist_ok=True)
    with open(os.path.join(thr_dir, f"{name}_folds.json"), "w", encoding="utf-8") as f:
        json.dump({k: res["meta"][k] for k in ("dataset", "n_folds", "percentiles", "fold_thresholds")}, f, indent=1)


def run_experiment_comparison(datasets=None):
    """Run the given datasets (None = all), then rebuild comparison.csv / .txt from every dataset saved so far."""
    names = list(datasets) if datasets is not None else list(config.DATASETS.keys())

    for name in names:
        cfg = config.DATASETS.get(name)
        if cfg is None:
            print(f"  [SKIP] {name}: not in config.DATASETS")
            continue
        try:
            _save_dataset(name, run_single_dataset(name, cfg))
        except Exception as e:
            import traceback
            print(f"  [SKIP] {name}: {e}", flush=True)
            traceback.print_exc()

    all_rows, blocks = [], []
    for name in config.DATASETS:
        csv_one = os.path.join(COMPARISON_DIR, f"{name}.csv")
        if os.path.isfile(csv_one):
            all_rows.extend(pd.read_csv(csv_one).to_dict("records"))
            with open(os.path.join(COMPARISON_DIR, f"{name}.txt"), encoding="utf-8") as f:
                blocks.append(f.read())

    if not all_rows:
        print("No results produced.", flush=True)
        return None

    os.makedirs(RESULTS_DIR, exist_ok=True)
    csv_path = os.path.join(RESULTS_DIR, "comparison.csv")
    txt_path = os.path.join(RESULTS_DIR, "comparison.txt")
    pd.DataFrame(all_rows).to_csv(csv_path, index=False)
    with open(txt_path, "w", encoding="utf-8") as f:
        f.write("\n".join(blocks).rstrip() + "\n")
    print(f"\n  Saved: {csv_path}\n  Saved: {txt_path}", flush=True)

    if config.CURVE_CONFIG.get("enabled", True):
        plot_all_curves(save_dir=str(RESULTS_DIR), dpi=config.CURVE_CONFIG["dpi"])

    return pd.DataFrame(all_rows)
