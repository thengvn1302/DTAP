"""Hu et al. (2022) subgradient solver for quasi-convex feasibility.

Reference: Y. Hu, G. Li, C. K. W. Yu, T. L. Yip (2022), "Quasi-convex feasibility
problems: Subgradient methods and convergence rates", EJOR 298, 45-58.

All three constraints are quasi-convex on the simplex, so the method applies.
Two variants:
    const : constant step v (no modulus estimation)              -> SG-const
    dyn   : dynamic step via Holder modulus L (the cost DTAP avoids) -> SG-dyn
"""
import time

import numpy as np

from src.common.config import HU_PARAMS
from src.common.consts import Method
from src.problem_formulation.problems import as_problem
from src.solvers.base import Solver, SolverResult

CVX_IDX = (0, 1)   # F1, F2 (convex)
PS_IDX = (2,)      # F3 (pseudoconvex)

_HU_CONST_V = 0.1
_HU_DYN_V = (1.0, 1.0)
_HU_BETA = 1.0


def estimate_holder_modulus(prep, n_samples: int = 500, random_state=None) -> float:
    """Estimate the beta=1 Holder modulus L as the max gradient norm over a sample of K
    (Dirichlet on the simplex for feature selection, uniform on the box for test (47))."""
    problem = as_problem(prep)
    rng = np.random.default_rng(42 if random_state is None else random_state)
    W = problem.sample(rng, n_samples)
    Lmax = 0.0
    for w in W:
        for gi in problem.gradients(w):
            ng = float(np.linalg.norm(gi))
            if np.isfinite(ng) and ng > Lmax:
                Lmax = ng
    return max(Lmax, 1e-8)


class HuSolver(Solver):
    def __init__(self, prep, thresholds: dict, mode: str = "dyn", params: dict = None,
                 alpha: float = 1.0, beta: float = _HU_BETA, n_samples_L: int = 500,
                 holder_modulus: float = None):
        """`prep` is the feature-selection prep dict or a problem adapter (problems.py).
        `holder_modulus` fixes L for SG-dyn (e.g. a tuned c * L_hat); None = estimate it."""
        if mode not in ("const", "dyn"):
            raise ValueError(f"mode must be 'const' or 'dyn', got {mode!r}")
        self.prep = prep
        self.problem = as_problem(prep)
        self.holder_modulus = holder_modulus
        self.thresholds = thresholds
        self.mode = mode
        self.params = params or HU_PARAMS
        self.alpha = alpha
        self.beta = beta
        self.n_samples_L = n_samples_L
        self.method = Method.HU_CONST if mode == "const" else Method.HU_DYN

    def solve(self, *, w_init: np.ndarray = None, seed: int = 42, record: bool = False) -> SolverResult:
        """`record=True` also returns the constraint values and the point at every evaluation."""
        problem = self.problem
        m = problem.dim
        eps = float(self.params["epsilon"])
        max_iter = int(self.params["max_iter"])
        b = np.array([self.thresholds["b1"], self.thresholds["b2"], self.thresholds["b3"]], float)

        if w_init is None:
            w = problem.start()
        else:
            w = problem.project(np.asarray(w_init, float).reshape(-1))
        w0 = w.copy()

        t0 = time.time()

        if self.mode == "dyn":
            if self.holder_modulus is not None:
                L = float(self.holder_modulus)
            else:
                L = estimate_holder_modulus(problem, n_samples=self.n_samples_L, random_state=seed)
            vlo, vhi = _HU_DYN_V
            v = float("nan")
        else:
            v = float(self.params.get("v_const", _HU_CONST_V))
            L = float("nan")

        J_hist, Jc_hist, Jp_hist = [], [], []
        F_hist, X_hist = [], []
        best_w, best_J = w.copy(), float("inf")

        for _ in range(max_iter):
            vals = problem.values(w)
            viol = np.maximum(vals - b, 0.0)
            if record:
                F_hist.append(np.array(vals, float))
                X_hist.append(w.copy())

            Jc = float(np.max(viol[list(CVX_IDX)])) if any(viol[i] > 0 for i in CVX_IDX) else 0.0
            Jp = float(np.max(viol[list(PS_IDX)])) if any(viol[j] > 0 for j in PS_IDX) else 0.0
            J = max(Jc, Jp)

            J_hist.append(J)
            Jc_hist.append(Jc)
            Jp_hist.append(Jp)

            if J < best_J:
                best_J, best_w = J, w.copy()
            if J <= eps:
                break

            Fmax = float(np.max(viol))
            if Fmax <= 0.0:
                break

            # alpha-most-violated control rule.
            Ik = [i for i in range(3) if viol[i] >= self.alpha * Fmax]
            if not Ik:
                Ik = [int(np.argmax(viol))]
            lam = 1.0 / len(Ik)

            grads = problem.gradients(w)
            step = np.zeros(m)
            if self.mode == "const":
                for i in Ik:
                    if viol[i] > 0.0:
                        ng = float(np.linalg.norm(grads[i]))
                        if ng > 0:
                            step += lam * (grads[i] / ng)
                w = problem.project(w - v * step)
            else:
                vk = 0.5 * (vlo + vhi)
                for i in Ik:
                    if viol[i] > 0.0:
                        ng = float(np.linalg.norm(grads[i]))
                        if ng > 0:
                            coef = (viol[i] / L) ** (1.0 / self.beta)
                            step += lam * coef * (grads[i] / ng)
                w = problem.project(w - vk * step)

        return SolverResult(
            w=best_w,
            time_sec=time.time() - t0,
            iter_count=len(J_hist),
            best_J=best_J,
            J_history=np.array(J_hist),
            J_cvx_history=np.array(Jc_hist),
            J_nc_history=np.array(Jp_hist),
            policy=("hu_const" if self.mode == "const" else "hu_dyn"),
            holder_modulus=float(L),
            step_size=(float(v) if self.mode == "const" else float("nan")),
            dist_w0=float(np.linalg.norm(best_w - w0)),
            F_history=np.array(F_hist) if record else np.empty(0),
            X_history=np.array(X_hist) if record else np.empty(0),
        )
