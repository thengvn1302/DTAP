"""Accuracy-vs-#features curves: computation, persistence, and grid figures.

Curve data is keyed by Method.value (a string) so it round-trips through JSON.
"""
import json
import math
import os
from typing import Dict, List

import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC

from src.common.config import DATASETS
from src.common.consts import METHOD_REGISTRY, RESULTS_DIR, Method


def topk_accuracy_curve(w, X_train, y_train, X_test, y_test, svm_params, knn_k) -> dict:
    """SVM and KNN accuracy for each top-k feature subset (k = 1..m)."""
    m = len(w)
    order = np.argsort(w)[::-1]
    svm_curve, knn_curve = [], []
    for k in range(1, m + 1):
        idx = order[:k]
        Xtr, Xte = X_train[:, idx], X_test[:, idx]
        try:
            svm_acc = SVC(**svm_params, random_state=42).fit(Xtr, y_train).score(Xte, y_test)
        except Exception:
            svm_acc = 0.0
        try:
            knn_acc = KNeighborsClassifier(n_neighbors=knn_k).fit(Xtr, y_train).score(Xte, y_test)
        except Exception:
            knn_acc = 0.0
        svm_curve.append(float(svm_acc))
        knn_curve.append(float(knn_acc))
    return dict(svm=svm_curve, knn=knn_curve)


def aggregate_topk_curves(fold_curves: List[dict], m: int) -> dict:
    """Average accuracy curves across folds."""
    if not fold_curves:
        return dict(svm_mean=[], knn_mean=[])
    svm_stack = np.array([fc["svm"] for fc in fold_curves if fc])
    knn_stack = np.array([fc["knn"] for fc in fold_curves if fc])
    return dict(
        svm_mean=svm_stack.mean(axis=0).tolist() if svm_stack.size else [],
        knn_mean=knn_stack.mean(axis=0).tolist() if knn_stack.size else [],
    )


def save_curve_data(name: str, curve_data: dict, save_dir: str = None) -> None:
    """Append/update curve data JSON at <results>/curve_data.json."""
    save_dir = save_dir or str(RESULTS_DIR)
    os.makedirs(save_dir, exist_ok=True)
    path = os.path.join(save_dir, "curve_data.json")
    all_data = {}
    if os.path.isfile(path):
        with open(path, encoding="utf-8") as f:
            all_data = json.load(f)
    all_data[name] = curve_data
    with open(path, "w", encoding="utf-8") as f:
        json.dump(all_data, f)


def load_curve_data(save_dir: str = None) -> dict:
    save_dir = save_dir or str(RESULTS_DIR)
    path = os.path.join(save_dir, "curve_data.json")
    if not os.path.isfile(path):
        return {}
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def render_grid_figure(all_curves: Dict[str, dict], metric: str, out_path: str, dpi: int = 300) -> None:
    """Grid figure: accuracy vs number of selected features, one panel per dataset."""
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    ordered_names = [n for n in DATASETS if n in all_curves]
    ordered_names += [n for n in all_curves if n not in ordered_names]
    n = len(ordered_names)
    if n == 0:
        return

    try:
        plt.style.use("seaborn-v0_8-whitegrid")
    except OSError:
        plt.style.use("ggplot")

    ncols = min(3, n)
    nrows = math.ceil(n / ncols)
    fig, axes = plt.subplots(nrows, ncols, figsize=(6.0 * ncols, 3.5 * nrows), squeeze=False)

    for idx, ds in enumerate(ordered_names):
        r, c = divmod(idx, ncols)
        ax = axes[r][c]
        rec = all_curves[ds]
        methods = rec.get("methods", {})

        all_vals = []
        for mth_id, mdata in methods.items():
            try:
                method = Method(mth_id)
            except ValueError:
                continue
            curve = mdata.get(f"{metric}_mean")
            if not curve:
                continue
            style = METHOD_REGISTRY[method]
            lw = 2.0 if method == Method.DTAP else 1.8
            pct = [v * 100 for v in curve]
            all_vals.extend(pct)
            ax.plot(range(1, len(pct) + 1), pct,
                    label=style.label, color=style.color, ls=style.linestyle, lw=lw)

        raw_val = rec.get(f"raw_{metric}")
        if raw_val is not None:
            ax.axhline(raw_val * 100, color="#78909C", ls=":", lw=1.5, label="All features")

        ax.set_title(f"{ds}  ({rec.get('n', '?')} samples, {rec.get('m', '?')} features, "
                     f"{rec.get('r', '?')} classes)", fontsize=9, fontweight="bold")
        ax.set_xlabel("Number of selected features", fontsize=8)
        ax.set_ylabel(f"{metric.upper()} Accuracy (%)", fontsize=8)
        ax.tick_params(labelsize=8)
        if all_vals:
            ax.set_ylim(max(0.0, min(all_vals) - 5.0), 102.0)
        ax.legend(loc="lower right", fontsize=7, framealpha=0.9)

    for idx in range(n, nrows * ncols):
        r, c = divmod(idx, ncols)
        axes[r][c].set_visible(False)

    fig.suptitle(f"Accuracy vs Number of Selected Features — {metric.upper()}",
                 fontsize=14, fontweight="bold")
    fig.tight_layout(rect=[0, 0, 1, 0.97])
    fig.savefig(out_path, dpi=dpi, bbox_inches="tight")
    plt.close(fig)


def plot_all_curves(save_dir: str = None, dpi: int = 150) -> None:
    save_dir = save_dir or str(RESULTS_DIR)
    all_curves = load_curve_data(save_dir)
    if not all_curves:
        print("No curve data to plot.")
        return
    for metric in ("svm", "knn"):
        out = os.path.join(save_dir, f"curve_{metric}.png")
        render_grid_figure(all_curves, metric, out, dpi=dpi)
        print(f"  Saved: {out}")
