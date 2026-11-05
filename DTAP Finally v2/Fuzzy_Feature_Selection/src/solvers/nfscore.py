"""N-Fscore baseline (Model I) — projection neural network (PNN).

Integrates the continuous-time PNN dynamics (Wang et al., 2021, Eqs 16-17) by
explicit Euler over a fixed time budget to minimize (w^T G w)/(rho^T w) on the
simplex. Only the PNN stage is used; feature selection then applies the shared
cumulative-weight rule.
"""
import time
from typing import List, Tuple

import numpy as np

from src.common.consts import Method
from src.problem_formulation.simplex import project_simplex
from src.solvers.base import Solver, SolverResult


class _PNN:
    """Projection neural network minimizing (w^T G w)/(rho^T w) on the simplex."""

    def __init__(self, G: np.ndarray, rho: np.ndarray, epsilon: float = 0.001):
        self.G = G
        self.rho = rho
        self.p = len(rho)
        self.eps = epsilon
        self.e = np.ones(self.p)
        self.P = np.outer(self.e, self.e) / self.p

    def _grad_f(self, w: np.ndarray) -> np.ndarray:
        den = float(self.rho @ w)
        if den <= 1e-15 or not np.isfinite(den):
            return -self.rho.copy()
        Gw = self.G @ w
        num = float(w @ Gw)
        return (2.0 * Gw * den - num * self.rho) / (den ** 2)

    def _dudt(self, u: np.ndarray) -> np.ndarray:
        g_u = np.maximum(u, 0.0)
        ImP = np.eye(self.p) - self.P
        w_c = g_u - self.P @ g_u + self.e / self.p
        return (-self.P @ g_u - ImP @ (u - g_u + self._grad_f(w_c)) + self.e / self.p) / self.eps

    def solve(self, time_horizon: float = 0.2, num_steps: int = 10000) -> Tuple[np.ndarray, List[float]]:
        u = np.full(self.p, 1.0 / self.p)
        t_eval = np.linspace(0, time_horizon, num_steps)
        history = []
        for i in range(len(t_eval) - 1):
            dt = t_eval[i + 1] - t_eval[i]
            u = u + dt * self._dudt(u)
            w = project_simplex(np.maximum(u, 0.0))
            den = float(self.rho @ w)
            history.append(float(w @ self.G @ w) / den if den > 1e-15 else float("inf"))
        w_final = project_simplex(np.maximum(u, 0.0))
        return w_final, history


class NFscoreSolver(Solver):
    method = Method.N_FSCORE

    def __init__(self, prep: dict, time_horizon: float = 0.2, num_steps: int = 10000,
                 epsilon: float = 0.001):
        self.prep = prep
        self.time_horizon = time_horizon
        self.num_steps = num_steps
        self.epsilon = epsilon

    def solve(self, *, w_init: np.ndarray = None, seed: int = 42) -> SolverResult:
        t0 = time.time()
        pnn = _PNN(self.prep["G"], self.prep["rho"], epsilon=self.epsilon)
        w_final, history = pnn.solve(time_horizon=self.time_horizon, num_steps=self.num_steps)
        return SolverResult(
            w=w_final,
            time_sec=time.time() - t0,
            iter_count=len(history),
            loss_history=np.array(history),
            policy="n_fscore",
        )
