"""Problem adapters: the oracles a solver needs (values, gradients, projection onto K).

Both instances have the same constraint layout: F1, F2 on the convex track and
F3 on the pseudoconvex track.

    FeatureSelectionProblem : F1/F2/F3 of the feature-selection model on the simplex
    LogBallProblem          : the nonconvex pseudoconvex test (47) on the box [-2, 2]^d

Solvers still accept the feature-selection `prep` dict; `as_problem` wraps it.
"""
import numpy as np

from src.problem_formulation.constraints import grad_f1, grad_f2, grad_f3, gradients, values
from src.problem_formulation.simplex import project_simplex


class FeatureSelectionProblem:
    """F1-F3 of the feature-selection model on the probability simplex K."""

    def __init__(self, prep: dict):
        self.prep = prep
        self.dim = int(prep["m"])

    def values(self, w: np.ndarray) -> np.ndarray:
        return values(w, self.prep)

    def gradient(self, i: int, w: np.ndarray) -> np.ndarray:
        return (grad_f1, grad_f2, grad_f3)[i](w, self.prep)

    def gradients(self, w: np.ndarray) -> list:
        return gradients(w, self.prep)

    def project(self, y: np.ndarray) -> np.ndarray:
        return project_simplex(y)

    def start(self) -> np.ndarray:
        return np.ones(self.dim, dtype=np.float64) / self.dim

    def sample(self, rng: np.random.Generator, n: int) -> np.ndarray:
        """Points for the Holder-modulus estimate: uniform Dirichlet on the simplex."""
        return rng.dirichlet(np.ones(self.dim), size=int(n))


class LogBallProblem:
    """Test (47): K = [-2, 2]^d and
        F1(x) = ||x + e1||^2 <= 1,  F2(x) = ||x - e2||^2 <= 9/4,
        F3(x) = kappa * log(1 + ||x - e1||^2) <= kappa * log 3   (pseudoconvex, not convex).
    """

    def __init__(self, d: int, kappa: float):
        if d < 2:
            raise ValueError("d must be >= 2 (e2 is used)")
        self.dim = int(d)
        self.kappa = float(kappa)
        self.e1 = np.zeros(self.dim)
        self.e1[0] = 1.0
        self.e2 = np.zeros(self.dim)
        self.e2[1] = 1.0
        self.thresholds = dict(b1=1.0, b2=9.0 / 4.0, b3=self.kappa * np.log(3.0))

    def values(self, x: np.ndarray) -> np.ndarray:
        r2 = float(np.sum((x - self.e1) ** 2))
        return np.array([float(np.sum((x + self.e1) ** 2)),
                         float(np.sum((x - self.e2) ** 2)),
                         self.kappa * np.log1p(r2)], float)

    def gradient(self, i: int, x: np.ndarray) -> np.ndarray:
        if i == 0:
            return 2.0 * (x + self.e1)
        if i == 1:
            return 2.0 * (x - self.e2)
        u = x - self.e1
        return self.kappa * 2.0 * u / (1.0 + float(u @ u))

    def gradients(self, x: np.ndarray) -> list:
        return [self.gradient(i, x) for i in range(3)]

    def project(self, y: np.ndarray) -> np.ndarray:
        return np.clip(y, -2.0, 2.0)

    def start(self) -> np.ndarray:
        """Standard start 1.5 * 1."""
        return np.full(self.dim, 1.5)

    def sample(self, rng: np.random.Generator, n: int) -> np.ndarray:
        """Points for the Holder-modulus estimate: uniform in K."""
        return rng.uniform(-2.0, 2.0, size=(int(n), self.dim))


def as_problem(prep_or_problem):
    """Return a problem adapter; a feature-selection `prep` dict is wrapped."""
    if isinstance(prep_or_problem, dict):
        return FeatureSelectionProblem(prep_or_problem)
    return prep_or_problem
