"""Constraint matrices and vectors of the unified 3-constraint model.

`build_matrices(X, y)` returns the `prep` dict that the constraints F1/F2/F3 and
the threshold calibration consume.

Model II (fuzzy rough set) provides the matrices for F1 and F2:
    approx_matrices : list of m arrays (n, r) — per-feature fuzzy lower approximation
    P               : (n, m) decision matrix
    I_mat           : (n, r) label-indicator matrix

Model I (fractional programming) provides the inputs for F3:
    rho : (m,)   Fisher score vector (relevance)
    G   : (m, m) PSD redundancy matrix (delta*I + S)

All outputs are bundled into a single `prep` dict consumed by the solvers.
"""
from typing import List, Tuple

import numpy as np

from src.common.config import PREPROCESSING


def _class_variance(X: np.ndarray, y: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    """sigma2[k, t] = Var(feature k | class t). Returns (sigma2, classes)."""
    n, m = X.shape
    classes = np.unique(y)
    r = len(classes)
    sigma2 = np.zeros((m, r))
    for t_idx, t in enumerate(classes):
        Xt = X[y == t]
        for k in range(m):
            sigma2[k, t_idx] = max(np.var(Xt[:, k]), 1e-10)
    return sigma2, classes


def _fuzzy_relation(X: np.ndarray, k: int, sigma2_k: np.ndarray, y: np.ndarray, classes) -> np.ndarray:
    """R_k(x_i, x_j) = exp(-[a_k(x_i) - a_k(x_j)]^2 / (2 * sigma2_{k, class(x_i)})).

    The bandwidth is indexed by the ROW (first argument) class — matches Eq. (7).
    """
    n = X.shape[0]
    xk = X[:, k]
    diff2 = (xk[:, None] - xk[None, :]) ** 2  # Numpy broadcast.
    class_idx = np.zeros(n, dtype=int)
    for t_idx, t in enumerate(classes):
        class_idx[y == t] = t_idx
    sigma2_row = sigma2_k[class_idx]
    return np.exp(-diff2 / (2.0 * sigma2_row[:, None]))


def _lower_approx(R_k: np.ndarray, y: np.ndarray, classes) -> np.ndarray:
    """Lower-approximation matrix M_k in R^{n x r}.

    M_k[i, t] = min_j max(1 - R_k(x_i, x_j), D_t(x_j)),  D_t(x_j) = 1{y[j] == t}.
    """
    n = R_k.shape[0]
    r = len(classes)
    approx = np.zeros((n, r))
    for t_idx, t in enumerate(classes):
        Dt = (y == t).astype(np.float64)
        term = np.maximum(1.0 - R_k, Dt[None, :])
        approx[:, t_idx] = term.min(axis=1)
    return approx


def _decision_matrix(approx_matrices: List[np.ndarray], y: np.ndarray, classes) -> np.ndarray:
    """P[i, k] = 1 iff argmax_t M_k[i, t] equals the true class of x_i."""
    n = approx_matrices[0].shape[0]
    m = len(approx_matrices)
    P = np.zeros((n, m))
    class_idx = np.zeros(n, dtype=int)
    for t_idx, t in enumerate(classes):
        class_idx[y == t] = t_idx
    for k in range(m):
        best = np.argmax(approx_matrices[k], axis=1)
        P[:, k] = (best == class_idx).astype(np.float64)
    return P


def _label_matrix(y: np.ndarray, classes) -> np.ndarray:
    """I_mat[i, t] = 1 iff y[i] == classes[t]."""
    n = len(y)
    r = len(classes)
    I = np.zeros((n, r))
    for t_idx, t in enumerate(classes):
        I[y == t, t_idx] = 1.0
    return I


def _fisher_score(X: np.ndarray, y: np.ndarray) -> np.ndarray:
    """Per-feature Fisher discriminant score: between-class / within-class variance."""
    X = np.asarray(X, dtype=float)
    n, p = X.shape
    mu = X.mean(axis=0)
    num = np.zeros(p)
    den = np.zeros(p)
    for c in np.unique(y):
        Xc = X[y == c]
        nc = Xc.shape[0]
        num += nc * (Xc.mean(axis=0) - mu) ** 2
        den += nc * Xc.var(axis=0, ddof=0)
    eps = float(PREPROCESSING.get("fisher_denominator_epsilon", 1e-12))
    with np.errstate(divide="ignore", invalid="ignore"):
        rho = num / (den + eps)
    rho[(num == 0) & (den == 0)] = 0.0
    return rho


def _sanitize_fisher(rho_raw: np.ndarray) -> np.ndarray:
    """Replace non-finite Fisher scores and clip to be non-negative."""
    rho = np.asarray(rho_raw, dtype=float).copy()
    finite = np.isfinite(rho)
    max_finite = float(np.max(rho[finite])) if np.any(finite) else 1.0
    if max_finite <= 0:
        max_finite = 1.0
    factor = float(PREPROCESSING.get("fisher_inf_replacement_factor", 10.0))
    rho[np.isnan(rho)] = 0.0
    rho[np.isposinf(rho)] = factor * max_finite
    rho[np.isneginf(rho)] = 0.0
    return np.maximum(rho, 0.0)


def _discretize(X: np.ndarray, n_bins: int) -> np.ndarray:
    """Equal-width histogram binning (Brown et al., 2012)."""
    X = np.asarray(X, dtype=float)
    n, p = X.shape
    Xd = np.zeros((n, p), dtype=np.int64)
    for j in range(p):
        col = X[:, j]
        cmin, cmax = np.nanmin(col), np.nanmax(col)
        if cmin == cmax:
            Xd[:, j] = 0
        else:
            edges = np.linspace(cmin, cmax, n_bins + 1)
            Xd[:, j] = np.clip(np.digitize(col, edges[1:-1], right=True), 0, n_bins - 1)
    return Xd


def _entropy(labels: np.ndarray) -> float:
    labels = np.asarray(labels, dtype=np.int64).ravel()
    if labels.size == 0:
        return 0.0
    _, inv = np.unique(labels, return_inverse=True)
    cnt = np.bincount(inv).astype(float)
    pr = cnt[cnt > 0] / labels.size
    return float(-np.sum(pr * np.log(pr)))


def _mi(hx: float, hy: float, hxy: float) -> float:
    return float(max(0.0, hx + hy - hxy))


def _supervised_similarity(X: np.ndarray, y: np.ndarray) -> np.ndarray:
    """Symmetric feature-pair similarity S via supervised multi-information."""
    n_bins = int(PREPROCESSING.get("discretization_bins", 10))
    Xd = _discretize(X, n_bins)
    y = np.asarray(y, dtype=np.int64) - int(np.min(y))
    n, p = Xd.shape
    cnum = int(np.max(y)) + 1
    hy = _entropy(y)
    base = max(n_bins + 1, int(Xd.max()) + 1)
    h_feat = np.zeros(p)
    mi_y = np.zeros(p)
    for i in range(p):
        xi = Xd[:, i]
        h_feat[i] = _entropy(xi)
        mi_y[i] = _mi(h_feat[i], hy, _entropy(xi * cnum + y))
    S = np.zeros((p, p), dtype=float)
    for i in range(p):
        xi = Xd[:, i]
        for j in range(i, p):
            denom = h_feat[i] + h_feat[j]
            if denom <= 0:
                sij = 0.0
            else:
                pair = xi * base + Xd[:, j]
                joint_mi = _mi(_entropy(pair), hy, _entropy(pair * cnum + y))
                multi = mi_y[i] + mi_y[j] - joint_mi
                sij = max(0.0, float(multi / denom))
            S[i, j] = S[j, i] = sij
    return S


def _make_psd(S: np.ndarray) -> np.ndarray:
    """Shift S to guarantee positive semi-definiteness: G = S + delta*I."""
    S = 0.5 * (S + S.T)
    lam_min = float(np.linalg.eigvalsh(S)[0]) if S.shape[0] > 1 else float(S[0, 0])
    delta = max(0.0, -lam_min) + float(PREPROCESSING.get("psd_diagonal_shift", 1e-10))
    return S + delta * np.eye(S.shape[0])


def build_matrices(X: np.ndarray, y: np.ndarray) -> dict:
    """Compute all inputs of the unified 3-constraint model.

    Parameters
    ----------
    X : (n, m) feature matrix — already min-max scaled.
    y : (n,) integer class labels.

    Returns
    -------
    prep : dict with keys approx_matrices, P, I_mat, rho, G, n, m, r.
    """
    n, m = X.shape

    sigma2, classes = _class_variance(X, y)
    r = len(classes)

    approx_matrices = []
    for k in range(m):
        Rk = _fuzzy_relation(X, k, sigma2[k], y, classes)
        approx_matrices.append(_lower_approx(Rk, y, classes))

    P = _decision_matrix(approx_matrices, y, classes)
    I_mat = _label_matrix(y, classes)

    rho = _sanitize_fisher(_fisher_score(X, y))
    G = _make_psd(_supervised_similarity(X, y))

    return dict(
        approx_matrices=approx_matrices,
        P=P,
        I_mat=I_mat,
        rho=rho,
        G=G,
        n=n, m=m, r=r,
    )
