"""Output-threshold calibration for the box constraint F_i(w) <= b_i.

Thresholds are calibrated by sampling w uniformly on the simplex (Dirichlet) and
taking the p_i-th percentile of F_i. Per-dataset percentiles come from DATC
(Dataset-Aware Threshold Calibration), which maps dataset shape -> percentiles.
"""
import numpy as np

from src.common.config import THRESHOLD_CONFIG
from src.problem_formulation.constraints import value_f1, value_f2, value_f3


def dataset_adaptive_config(n: int, m: int, K: int, class_counts) -> dict:
    """Adaptive (f1, f2, f3) threshold percentiles for a dataset (theta = 0.9 fixed)."""
    class_counts = np.asarray(class_counts, dtype=int)
    imbalance = int(class_counts.min()) / int(class_counts.max())
    sample_density = n / m

    # F1 — rough-set approximation error bound.
    if sample_density > 300:
        f1 = max(25, int(sample_density / 20))
    elif m >= 20:
        f1 = 20 if sample_density < 10 else (12 if sample_density < 20 else 5)
    elif m >= 12:
        f1 = 10 + K // 3
    elif m >= 6:
        f1 = 20 if K >= 5 else 15
    else:
        f1 = 12
    f1 = int(np.clip(f1, 5, 40))

    # F2 — membership constraint.
    if sample_density > 300:
        if K <= 3:
            f2 = 5
        elif m <= 20:
            f2 = K + m // 2
        else:
            f2 = int(round(10 + K * 2.5))
    elif m <= 5:
        f2 = 12
    elif m <= 10:
        f2 = 8
    elif m <= 20:
        f2 = K + m // 2
    else:
        f2 = int(round(10 + K * 2.5))
    f2 = int(np.clip(f2, 5, 25))

    # F3 — redundancy / relevance ratio.
    if K <= 3:
        f3 = 55 if m > 30 else 40
    elif m <= 20:
        f3 = 45 if sample_density > 100 else 55
    else:
        f3 = 65
    if imbalance < 0.1 and K > 2:
        f3 = min(75, f3 + 15)
    if K > 4 and 25 <= m <= 55 and sample_density < 300:
        f3 = min(80, f3 + 10)

    return dict(
        f1_percentile=f1,
        f2_percentile=f2,
        f3_percentile=f3,
        theta=0.9,
        _n=n, _m=m, _K=K,
        _imbalance=round(float(imbalance), 3),
        _sample_density=round(float(sample_density), 1),
    )


def build_threshold_config(adaptive: dict) -> dict:
    """Convert a DATC result into a THRESHOLD_CONFIG-compatible dict."""
    return dict(
        method="sampling_based",
        sampling_based=dict(
            n_samples=3000,
            seed=42,
            f1_percentile=adaptive["f1_percentile"],
            f2_percentile=adaptive["f2_percentile"],
            f3_percentile=adaptive["f3_percentile"],
        ),
    )


def _sampling_based_thresholds(prep: dict, params: dict) -> dict:
    m = prep["m"]
    rng = np.random.RandomState(int(params["seed"]))
    samples = rng.dirichlet(np.ones(m), size=int(params["n_samples"]))
    # Append the m simplex vertices so the pool covers the boundary, where F1/F2
    # attain near-minimum values that uniform Dirichlet sampling rarely reaches.
    samples = np.vstack([samples, np.eye(m)])

    f1 = [value_f1(w, prep) for w in samples]
    f2 = [value_f2(w, prep) for w in samples]
    f3 = [value_f3(w, prep) for w in samples]
    return dict(
        b1=float(np.percentile(f1, params["f1_percentile"])),
        b2=float(np.percentile(f2, params["f2_percentile"])),
        b3=float(np.percentile(f3, params["f3_percentile"])),
        method="sampling_based",
    )


def compute_thresholds(prep: dict, threshold_config: dict = None) -> dict:
    """Calibrate thresholds b1, b2, b3 for the given prep."""
    threshold_config = threshold_config or THRESHOLD_CONFIG
    method = threshold_config.get("method", "sampling_based")
    if method == "sampling_based":
        return _sampling_based_thresholds(prep, threshold_config.get("sampling_based", {}))
    raise ValueError(f"Unknown threshold method: {method!r}")


def prepare_from_prep(prep: dict, threshold_config: dict = None) -> dict:
    """Bundle prep + calibrated thresholds for the solvers."""
    thresholds = compute_thresholds(prep, threshold_config or THRESHOLD_CONFIG)
    return dict(prep=prep, thresholds=thresholds, w_init=None)
