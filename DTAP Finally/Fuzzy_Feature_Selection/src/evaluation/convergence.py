"""Convergence experiment: violation J(w^k) per iteration for DTAP vs Hu (2022).

Runs on the full (unsplit) data of each dataset and records whether each method
reaches feasibility (J <= epsilon). DTAP and SG-const reach it on all datasets;
SG-dyn fails where the estimated Holder modulus is large.
"""
import gc
import json
import math
import time
from typing import List

import numpy as np
import pandas as pd

from src.common import config
from src.common.consts import CONVERGENCE_DIR, CONVERGENCE_STYLE, Method, method_label
from src.data_processors.loaders import load_dataset, scale_train_test
from src.evaluation.table6 import (assemble_table6, independent_check, load_datasets, run_table6_extras,
                                   save_dataset, threshold_metadata)
from src.problem_formulation.matrices import build_matrices
from src.solvers import DtapSolver, HuSolver
from src.problem_formulation.thresholds import build_threshold_config, dataset_adaptive_config, prepare_from_prep

Q2_METHODS: List[Method] = [Method.DTAP, Method.HU_CONST, Method.HU_DYN]


def _prepare(name: str, cfg_entry: dict):
    """Load the full dataset (no split) and prepare prep + thresholds."""
    X, y = load_dataset(name, cfg_entry)
    K = len(np.unique(y))
    if config.USE_DATC:
        thr_cfg = build_threshold_config(dataset_adaptive_config(int(X.shape[0]), int(X.shape[1]), K, np.bincount(y)))
    else:
        thr_cfg = config.THRESHOLD_CONFIG
    Xsc, _ = scale_train_test(X, X)
    prep = build_matrices(Xsc, y)
    prepared = prepare_from_prep(prep, thr_cfg)
    return prep, prepared, int(X.shape[0]), int(X.shape[1])


def _run_method(method: Method, prep: dict, prepared: dict, seed: int) -> dict:
    eps = float(config.DTAP_PARAMS["epsilon"])
    if method == Method.DTAP:
        solver = DtapSolver(prep, prepared["thresholds"], config.DTAP_PARAMS, config.DTAP_GAMMA)
    else:
        mode = "const" if method == Method.HU_CONST else "dyn"
        solver = HuSolver(prep, prepared["thresholds"], mode=mode, params=config.HU_PARAMS)
    res = solver.solve(w_init=prepared["w_init"], seed=seed)

    best_J = float(res.best_J if res.best_J != float("inf") else res.J_history[-1])
    return dict(
        J=np.asarray(res.J_history, float),
        Jcvx=np.asarray(res.J_cvx_history, float),
        Jps=np.asarray(res.J_nc_history, float),
        iters=int(res.iter_count),
        best_J=best_J,
        converged=bool(best_J <= eps),
        dist_w0=float(res.dist_w0),
        L=float(res.holder_modulus),
        v=float(res.step_size),
    )


def _run_dataset(name: str) -> None:
    """Standard-start runs (q2_*), Table 6 extras and the witness check for one dataset;
    saved to results/hu2022/datasets/<name>.json.gz."""
    seed = int(config.CONVERGENCE_CONFIG.get("seed", 42))
    t0 = time.time()
    prep, prepared, n_tr, p = _prepare(name, config.DATASETS[name])
    rows, curves = [], {"n_tr": n_tr, "p": p, "methods": {}}
    for method in Q2_METHODS:
        r = _run_method(method, prep, prepared, seed)
        curves["methods"][method.value] = {
            "J": list(map(float, r["J"])),
            "Jcvx": list(map(float, r["Jcvx"])),
            "Jps": list(map(float, r["Jps"])),
        }
        rows.append(dict(
            dataset=name, method=method.value, n_tr=n_tr, p=p,
            iters=r["iters"], converged=r["converged"],
            best_J=r["best_J"], dist_w0=r["dist_w0"], L=r["L"], v=r["v"]))
        print(f"  {name:14s} {method.value:9s}  iters={r['iters']:5d}  "
              f"conv={r['converged']}  best_J={r['best_J']:.2e}")

    extras = run_table6_extras(name, prep, prepared)
    class_counts = [int(c) for c in prep["I_mat"].sum(axis=0)]
    thresholds = threshold_metadata(name, n_tr, p, class_counts, prepared["thresholds"])
    del prep, prepared
    gc.collect()
    witness_check = independent_check(name, extras["witness_candidates"])
    save_dataset(name, dict(rows=rows, curves=curves, extras=extras, thresholds=thresholds,
                            witness_check=witness_check, wall_time_sec=time.time() - t0))
    print(f"  {name}: Table 6 extras saved ({time.time() - t0:.1f} s)")


def _plot_overlay(curves: dict, eps: float, out_path: str, dpi: int = 300) -> None:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    try:
        plt.style.use("seaborn-v0_8-whitegrid")
    except OSError:
        plt.style.use("ggplot")

    names = list(curves.keys())
    n = len(names)
    ncols = min(3, n) if n > 1 else 1
    nrows = math.ceil(n / ncols)
    fig, axes = plt.subplots(nrows, ncols, figsize=(4.2 * ncols, 3.2 * nrows), squeeze=False)

    for idx, ds in enumerate(names):
        ax = axes[idx // ncols][idx % ncols]
        rec = curves[ds]
        for method, st in CONVERGENCE_STYLE.items():
            J = rec["methods"].get(method.value, {}).get("J")
            if not J:
                continue
            Jp = np.maximum(np.asarray(J, float), 1e-16)
            ax.semilogy(range(len(Jp)), Jp, label=method_label(method),
                        color=st["color"], ls=st["ls"], lw=st["lw"], zorder=st["z"])
        ax.axhline(eps, color="0.4", ls=":", lw=1.0, zorder=0)
        ax.set_title(f"{ds}  ($n={rec['n_tr']},\\ p={rec['p']}$)", fontsize=9, fontweight="bold")
        ax.set_xlabel("Iteration", fontsize=8)
        ax.set_ylabel(r"$J(w^k)$", fontsize=8)
        ax.tick_params(labelsize=7)

    for j in range(n, nrows * ncols):
        axes[j // ncols][j % ncols].set_visible(False)

    handles, labels = axes[0][0].get_legend_handles_labels()
    fig.legend(handles, labels, loc="lower center", ncol=3, fontsize=9, bbox_to_anchor=(0.5, -0.02))
    fig.suptitle("Convergence: DTAP vs Hu (2022)", fontsize=12, fontweight="bold")
    fig.tight_layout(rect=(0, 0.04, 1, 1))
    fig.savefig(out_path, dpi=dpi, bbox_inches="tight")
    plt.close(fig)


def run_convergence(datasets=None, make_plots: bool = True, assemble_only: bool = False) -> pd.DataFrame:
    """Run the given datasets, then rebuild every Table 6 output from all datasets saved so far
    (so the datasets can be run one at a time). `assemble_only` skips the runs."""
    datasets = [] if assemble_only else (list(datasets) if datasets else list(config.DATASETS))
    CONVERGENCE_DIR.mkdir(parents=True, exist_ok=True)

    for name in datasets:
        if name not in config.DATASETS:
            print(f"  [SKIP] {name}: not configured")
            continue
        _run_dataset(name)

    data = load_datasets()
    datasets = list(data)
    df = pd.DataFrame([row for d in data.values() for row in d["rows"]])
    curves = {name: d["curves"] for name, d in data.items()}
    summary = {m: f"{sum(not r['converged'] for d in data.values() for r in d['rows'] if r['method'] == m.value)}"
                  f"/{len(datasets)}" for m in Q2_METHODS}
    df.to_csv(CONVERGENCE_DIR / "q2_convergence.csv", index=False)
    (CONVERGENCE_DIR / "q2_curves.json").write_text(json.dumps(curves), encoding="utf-8")

    if make_plots:
        try:
            eps = float(config.DTAP_PARAMS["epsilon"])
            _plot_overlay(curves, eps, str(CONVERGENCE_DIR / "q2_convergence_overlay.png"),
                          dpi=config.CONVERGENCE_CONFIG["dpi"])
            print(f"  Saved: {CONVERGENCE_DIR / 'q2_convergence_overlay.png'}")
        except Exception as exc:
            print(f"  [warn] overlay plot skipped: {exc}")

    n_ds = len([d for d in datasets if d in config.DATASETS])
    lines = ["ModelCombined Q2: DTAP vs Hu (2022)", "=" * 50, f"datasets: {n_ds}",
             "Reached feasibility (J<=eps) on:"]
    for m in Q2_METHODS:
        reached = n_ds - int(summary[m].split("/")[0])
        lines.append(f"  {m.value:10s}: {reached}/{n_ds}  (failed: {summary[m]})")
    (CONVERGENCE_DIR / "q2_summary.txt").write_text("\n".join(lines), encoding="utf-8")
    print("\n".join(lines))
    print(assemble_table6(data))
    print(f"\n  Saved Q2 artifacts -> {CONVERGENCE_DIR}")
    return df
