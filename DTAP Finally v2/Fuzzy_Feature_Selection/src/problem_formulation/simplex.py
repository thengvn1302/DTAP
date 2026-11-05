from typing import Tuple

import numpy as np


def project_simplex(y: np.ndarray) -> np.ndarray:
    """Euclidean projection onto the probability simplex (Duchi et al., 2008). O(m log m)."""
    m = len(y)
    u = np.sort(y)[::-1]
    cssv = np.cumsum(u) - 1.0
    rho = np.nonzero(u * np.arange(1, m + 1) > cssv)[0][-1]
    lam = cssv[rho] / (rho + 1.0)
    return np.maximum(y - lam, 0.0)


def select_features(w: np.ndarray, theta: float = 0.90) -> Tuple[np.ndarray, int]:
    """Cumulative-weight feature selection: smallest top-k whose mass reaches theta.

    Returns (selected_indices, n_selected) with indices ordered by descending weight.
    """
    order = np.argsort(w)[::-1]
    w_sorted = w[order]
    total = w_sorted.sum()
    if total < 1e-15:
        return order[:1], 1
    cumsum = np.cumsum(w_sorted) / total
    s = int(np.searchsorted(cumsum, theta)) + 1
    s = min(s, len(w))
    return order[:s], s
