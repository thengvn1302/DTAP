"""AFRSFCV baseline (Model II) — softmax-reparameterized gradient descent.

Minimizes  1/2||I - sum_k w_k R_k(D)||^2 + lambda1/2||1 - P w||^2 + lambda2/2||w||^2
with w(tau) = softmax(tau), so w stays on the simplex for every tau.
"""
import time
from typing import Tuple

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

from src.common.consts import Method
from src.problem_formulation.simplex import select_features
from src.solvers.base import Solver, SolverResult


def _softmax(tau: np.ndarray) -> np.ndarray:
    e = np.exp(tau - tau.max())
    return e / e.sum()


def _loss(w: np.ndarray, prep: dict, lambda1: float, lambda2: float) -> float:
    M_list, P, I_mat = prep["approx_matrices"], prep["P"], prep["I_mat"]
    n, m = prep["n"], prep["m"]
    fused = sum(w[k] * M_list[k] for k in range(m))
    t1 = 0.5 * np.sum((I_mat - fused) ** 2)
    t2 = 0.5 * lambda1 * np.sum((np.ones(n) - P @ w) ** 2)
    t3 = 0.5 * lambda2 * np.sum(w ** 2)
    return float(t1 + t2 + t3)


def _grad_w(w: np.ndarray, prep: dict, lambda1: float, lambda2: float) -> np.ndarray:
    M_list, P, I_mat = prep["approx_matrices"], prep["P"], prep["I_mat"]
    n, m = prep["n"], prep["m"]
    residual = I_mat - sum(w[k] * M_list[k] for k in range(m))
    grad = np.array([-np.sum(residual * M_list[l]) for l in range(m)])
    grad += lambda1 * (P.T @ P @ w - P.T @ np.ones(n))
    grad += lambda2 * w
    return grad


class AfrsfcvSolver(Solver):
    method = Method.AFRSFCV

    def __init__(self, prep: dict, lambda1: float = 0.5, lambda2: float = 0.5,
                 lr: float = 0.01, max_iter: int = 500):
        self.prep = prep
        self.lambda1 = lambda1
        self.lambda2 = lambda2
        self.lr = lr
        self.max_iter = max_iter

    def solve(self, *, w_init: np.ndarray = None, seed: int = 42) -> SolverResult:
        prep = self.prep
        m = prep["m"]
        tau = np.random.RandomState(seed).randn(m) * 0.01

        loss_history = []
        t0 = time.time()
        for _ in range(self.max_iter):
            w = _softmax(tau)
            loss_history.append(_loss(w, prep, self.lambda1, self.lambda2))
            gw = _grad_w(w, prep, self.lambda1, self.lambda2)
            jac = np.diag(w) - np.outer(w, w)   # softmax Jacobian
            tau = tau - self.lr * (jac.T @ gw)

        return SolverResult(
            w=_softmax(tau),
            time_sec=time.time() - t0,
            iter_count=len(loss_history),
            loss_history=np.array(loss_history),
            policy="afrsfcv",
        )


def tune_afrsfcv(X_train: np.ndarray, y_train: np.ndarray, prep: dict,
                 lambda1_grid: list, lambda2_grid: list, lr: float, max_iter: int,
                 seed: int = 42, val_fraction: float = 0.2, theta: float = 0.9,
                 svm_params: dict = None) -> Tuple[float, float]:
    """Select (lambda1, lambda2) by SVM accuracy on an inner validation split."""
    svm_params = svm_params or dict(kernel="rbf", C=1.0, gamma="scale")

    try:
        itr_idx, ival_idx = train_test_split(
            np.arange(len(y_train)), test_size=val_fraction,
            stratify=y_train, random_state=seed)
    except ValueError:
        rng = np.random.RandomState(seed)
        perm = rng.permutation(len(y_train))
        cut = max(int(len(np.unique(y_train))), int(len(y_train) * val_fraction))
        ival_idx, itr_idx = perm[:cut], perm[cut:]

    X_itr, y_itr = X_train[itr_idx], y_train[itr_idx]
    X_ival, y_ival = X_train[ival_idx], y_train[ival_idx]

    best_acc, best_l1, best_l2 = -1.0, lambda1_grid[0], lambda2_grid[0]
    for l1 in lambda1_grid:
        for l2 in lambda2_grid:
            w = AfrsfcvSolver(prep, lambda1=l1, lambda2=l2, lr=lr, max_iter=max_iter).solve(seed=seed).w
            idx, _ = select_features(w, theta)
            if len(idx) == 0:
                idx = np.arange(prep["m"])
            try:
                acc = SVC(**svm_params, random_state=42).fit(X_itr[:, idx], y_itr).score(X_ival[:, idx], y_ival)
            except Exception:
                acc = 0.0
            if acc > best_acc:
                best_acc, best_l1, best_l2 = acc, l1, l2

    return best_l1, best_l2
