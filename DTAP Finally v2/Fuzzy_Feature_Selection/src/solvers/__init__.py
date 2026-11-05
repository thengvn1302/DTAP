"""Feature-weight solvers behind a common Solver interface."""
import numpy as np

from src.common.config import (
    AFRSFCV_PARAMS, DTAP_GAMMA, DTAP_PARAMS, HU_PARAMS, N_FSCORE_PARAMS,
)
from src.common.consts import Method
from src.solvers.afrsfcv import AfrsfcvSolver, tune_afrsfcv
from src.solvers.base import Solver, SolverResult
from src.solvers.dtap import DtapSolver, make_gamma_schedule
from src.solvers.hu2022 import HuSolver, estimate_holder_modulus
from src.solvers.nfscore import NFscoreSolver

__all__ = [
    "Solver", "SolverResult", "DtapSolver", "HuSolver", "AfrsfcvSolver", "NFscoreSolver",
    "make_gamma_schedule", "estimate_holder_modulus", "tune_afrsfcv", "build_solver",
]


def build_solver(method: Method, prep: dict, thresholds: dict = None, *,
                 X_train: np.ndarray = None, y_train: np.ndarray = None,
                 seed: int = 42) -> Solver:
    """Construct the solver for `method`, handling AFRSFCV's optional grid search."""
    if method == Method.DTAP:
        return DtapSolver(prep, thresholds, DTAP_PARAMS, DTAP_GAMMA)

    if method == Method.HU_CONST:
        return HuSolver(prep, thresholds, mode="const", params=HU_PARAMS)
    if method == Method.HU_DYN:
        return HuSolver(prep, thresholds, mode="dyn", params=HU_PARAMS)

    if method == Method.N_FSCORE:
        return NFscoreSolver(prep, **N_FSCORE_PARAMS)

    if method == Method.AFRSFCV:
        ap = AFRSFCV_PARAMS
        if ap.get("grid_enabled", True) and X_train is not None and y_train is not None:
            from src.common.config import SVM_PARAMS
            l1, l2 = tune_afrsfcv(
                X_train, y_train, prep,
                lambda1_grid=ap["lambda1_grid"], lambda2_grid=ap["lambda2_grid"],
                lr=ap["lr"], max_iter=ap["max_iter"], seed=seed,
                val_fraction=ap.get("val_fraction", 0.2), theta=ap.get("theta", 0.9),
                svm_params=SVM_PARAMS)
        else:
            l1, l2 = ap["lambda1"], ap["lambda2"]
        return AfrsfcvSolver(prep, lambda1=l1, lambda2=l2, lr=ap["lr"], max_iter=ap["max_iter"])

    raise ValueError(f"Unknown method: {method!r}")
