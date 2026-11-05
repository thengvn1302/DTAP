"""Constraint values and gradients for the combined 3-constraint model.

    F1(w) = ||I - sum_k w_k R_k(D)||_F^2   (convex,        from Model II)
    F2(w) = ||1 - P w||^2                  (convex,        from Model II)
    F3(w) = (w^T G w) / (rho^T w)          (pseudoconvex,  from Model I)

Convex track: indices {F1, F2}.  Pseudoconvex track: {F3}.
"""
import numpy as np


def _fused(w: np.ndarray, M_list: list) -> np.ndarray:
    """sum_k w_k M_k where each M_k is (n, r)."""
    return sum(w[k] * M_list[k] for k in range(len(w)))


def value_f1(w: np.ndarray, prep: dict) -> float:
    """F1(w) = ||I - sum_k w_k R_k(D)||_F^2."""
    fused = _fused(w, prep["approx_matrices"])
    return float(np.sum((prep["I_mat"] - fused) ** 2))


def value_f2(w: np.ndarray, prep: dict) -> float:
    """F2(w) = ||1 - P w||^2."""
    return float(np.sum((np.ones(prep["n"]) - prep["P"] @ w) ** 2))


def value_f3(w: np.ndarray, prep: dict) -> float:
    """F3(w) = (w^T G w) / (rho^T w)."""
    den = max(float(prep["rho"] @ w), 1e-15)
    return float(w @ prep["G"] @ w) / den


def grad_f1(w: np.ndarray, prep: dict) -> np.ndarray:
    """grad F1 = 2 * [-<I - Mw, M_l>_F]_{l=1..m}."""
    M_list = prep["approx_matrices"]
    residual = prep["I_mat"] - _fused(w, M_list)
    g = np.array([-np.sum(residual * M_list[l]) for l in range(prep["m"])])
    return 2.0 * g


def grad_f2(w: np.ndarray, prep: dict) -> np.ndarray:
    """grad F2 = 2 P^T (P w - 1)."""
    P = prep["P"]
    return 2.0 * P.T @ (P @ w - np.ones(prep["n"]))


def grad_f3(w: np.ndarray, prep: dict) -> np.ndarray:
    """grad F3 = (2 G w (rho^T w) - (w^T G w) rho) / (rho^T w)^2."""
    G, rho = prep["G"], prep["rho"]
    den = max(float(rho @ w), 1e-15)
    Gw = G @ w
    quad = float(w @ Gw)
    return (2.0 * Gw * den - quad * rho) / (den ** 2)


def values(w: np.ndarray, prep: dict) -> np.ndarray:
    """[F1, F2, F3] as an array (constraint order 0, 1, 2)."""
    return np.array([value_f1(w, prep), value_f2(w, prep), value_f3(w, prep)], float)


def gradients(w: np.ndarray, prep: dict) -> list:
    """[grad F1, grad F2, grad F3] (constraint order 0, 1, 2)."""
    return [grad_f1(w, prep), grad_f2(w, prep), grad_f3(w, prep)]
