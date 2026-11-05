from abc import ABC, abstractmethod
from dataclasses import dataclass, field

import numpy as np

from src.common.consts import Method


def _empty() -> np.ndarray:
    return np.empty(0)


@dataclass
class SolverResult:
    """Outcome of a weight solver. History fields are empty when not applicable."""

    w: np.ndarray
    time_sec: float
    iter_count: int
    best_J: float = float("inf")
    J_history: np.ndarray = field(default_factory=_empty)
    J_cvx_history: np.ndarray = field(default_factory=_empty)
    J_nc_history: np.ndarray = field(default_factory=_empty)
    loss_history: np.ndarray = field(default_factory=_empty)
    policy: str = ""
    holder_modulus: float = float("nan")  # L, estimated only by SG-dyn
    step_size: float = float("nan")       # constant step v, used only by SG-const
    dist_w0: float = float("nan")
    F_history: np.ndarray = field(default_factory=_empty)  # (iters, 3) constraint values, only if record=True
    X_history: np.ndarray = field(default_factory=_empty)  # (iters, dim) evaluated points, only if record=True


class Solver(ABC):
    """Common interface for the feature-weight solvers.

    A solver is constructed with everything it needs (preprocessed matrices,
    thresholds, hyperparameters) and produces a weight vector via `solve()`.
    """

    method: Method

    @abstractmethod
    def solve(self, *, w_init: np.ndarray = None, seed: int = 42) -> SolverResult:
        raise NotImplementedError
