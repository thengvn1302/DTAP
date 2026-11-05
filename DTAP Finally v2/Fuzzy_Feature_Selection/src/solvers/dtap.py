"""DTAP — Dual-Track Adaptive Projection (proposed solver).

Convex track {F1, F2}: Polyak step  eta = rho_cvx * 2 Phi / ||g||^2.
Pseudoconvex track {F3}: safe step  eta = gamma_k / max(1, ||g||).
The two directions are mixed by mu = J_cvx / (J_cvx + J_nc), then projected
onto the base set K (the simplex for feature selection, a box for test (47)).
No Lipschitz constant and no projection onto Omega required.
"""
import time
from typing import Callable

import numpy as np

from src.common.config import DTAP_GAMMA, DTAP_PARAMS
from src.common.consts import Method
from src.problem_formulation.problems import as_problem
from src.solvers.base import Solver, SolverResult


def make_gamma_schedule(offset: float, power: float, scale: float = 1.0) -> Callable[[int], float]:
    """gamma_k = scale / (k + offset)^power, satisfying sum gamma_k = inf, sum gamma_k^2 < inf
    for power in (1/2, 1]."""
    if offset <= 0:
        raise ValueError("offset must be > 0")
    if power <= 0:
        raise ValueError("power must be > 0")
    if scale <= 0:
        raise ValueError("scale must be > 0")

    def _gamma(k: int) -> float:
        return scale / (k + offset) ** power

    return _gamma


class DtapSolver(Solver):
    method = Method.DTAP

    def __init__(self, prep, thresholds: dict, params: dict = None, gamma: dict = None,
                 weight: str = "proportional", assignment: str = "split"):
        """`prep` is the feature-selection prep dict or a problem adapter (problems.py).
        `weight`: "proportional" mu = J_cvx / (J_cvx + J_ps) (Algorithm 1), or "balanced"
        mu = 1/2 when both tracks are violated and full weight to the sole violated track.
        `assignment`: "split" I_cvx = {1, 2}, I_ps = {3}; "all_convex" I_cvx = {1, 2, 3}
        (the all-convex comparator AC: empty pseudoconvex track, mu = 1, Corollary 3.13)."""
        if weight not in ("proportional", "balanced"):
            raise ValueError(f"weight must be 'proportional' or 'balanced', got {weight!r}")
        if assignment not in ("split", "all_convex"):
            raise ValueError(f"assignment must be 'split' or 'all_convex', got {assignment!r}")
        self.weight = weight
        self.all_convex = assignment == "all_convex"
        self.prep = prep
        self.problem = as_problem(prep)
        self.thresholds = thresholds
        self.params = params or DTAP_PARAMS
        self.gamma_fn = make_gamma_schedule(**(gamma or DTAP_GAMMA))

    def solve(self, *, w_init: np.ndarray = None, seed: int = 42, record: bool = False) -> SolverResult:
        """`record=True` also returns the constraint values and the point at every evaluation."""
        problem = self.problem
        m = problem.dim
        rho_cvx = self.params["rho_cvx"]
        delta = self.params["delta"]
        epsilon = self.params["epsilon"]
        max_iter = self.params["max_iter"]
        b1, b2, b3 = self.thresholds["b1"], self.thresholds["b2"], self.thresholds["b3"]

        if w_init is None:
            w = problem.start()
        else:
            w = problem.project(np.asarray(w_init, dtype=np.float64).reshape(-1))

        best_w, best_J = w.copy(), float("inf")
        J_hist, Jc_hist, Jp_hist = [], [], []
        F_hist, X_hist = [], []
        t0 = time.time()

        for k_iter in range(max_iter):
            F = problem.values(w)
            v1 = max(F[0] - b1, 0.0)
            v2 = max(F[1] - b2, 0.0)
            v3 = max(F[2] - b3, 0.0)
            if record:
                F_hist.append(np.array(F, float))
                X_hist.append(w.copy())

            if self.all_convex:
                J_cvx = max(v1, v2, v3)
                J_nc = 0.0
            else:
                J_cvx = max(v1, v2)
                J_nc = v3
            J = max(J_cvx, J_nc)

            J_hist.append(J)
            Jc_hist.append(J_cvx)
            Jp_hist.append(J_nc)

            if J < best_J:
                best_J, best_w = J, w.copy()
            if J <= epsilon:
                break

            gamma_k = self.gamma_fn(k_iter)

            # Convex active set + Polyak direction.
            K_cvx = []
            if J_cvx > 0:
                if v1 >= J_cvx - delta:
                    K_cvx.append(("F1", v1))
                if v2 >= J_cvx - delta:
                    K_cvx.append(("F2", v2))
                if self.all_convex and v3 >= J_cvx - delta:
                    K_cvx.append(("F3", v3))
            g_cvx = np.zeros(m)
            Phi_cvx = 0.0
            for name, vi in K_cvx:
                gi = problem.gradient({"F1": 0, "F2": 1, "F3": 2}[name], w)
                g_cvx += vi * gi
                Phi_cvx += 0.5 * vi ** 2
            norm_cvx = float(np.linalg.norm(g_cvx))
            eta_cvx = rho_cvx * 2.0 * Phi_cvx / (norm_cvx ** 2) if norm_cvx > 1e-15 else 0.0

            # Pseudoconvex track: safe gamma step.
            g_nc = v3 * problem.gradient(2, w) if J_nc > 0 else np.zeros(m)
            norm_nc = float(np.linalg.norm(g_nc))
            eta_nc = gamma_k / max(1.0, norm_nc)

            # Soft-ratio combination + projection.
            if self.weight == "balanced" and J_cvx > 0 and J_nc > 0:
                mu = 0.5
            else:
                mu = J_cvx / (J_cvx + J_nc) if (J_cvx + J_nc) > 0 else 0.5
            y_step = w - (mu * eta_cvx * g_cvx + (1.0 - mu) * eta_nc * g_nc)
            w = problem.project(y_step)

        return SolverResult(
            w=best_w,
            time_sec=time.time() - t0,
            iter_count=len(J_hist),
            best_J=best_J,
            J_history=np.array(J_hist),
            J_cvx_history=np.array(Jc_hist),
            J_nc_history=np.array(Jp_hist),
            policy="dtap_ac" if self.all_convex else "dtap",
            F_history=np.array(F_hist) if record else np.empty(0),
            X_history=np.array(X_hist) if record else np.empty(0),
        )
