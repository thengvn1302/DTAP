import sys
from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import Dict

PROJECT_DIR = Path(__file__).resolve().parents[2]
DATA_DIR = PROJECT_DIR / "data"
RESULTS_DIR = PROJECT_DIR / "results"
CONVERGENCE_DIR = RESULTS_DIR / "hu2022"

sys.path.append(str(PROJECT_DIR))


class Method(Enum):
    """Feature-selection weight solvers compared in the experiments."""

    N_FSCORE = "n_fscore"   # Model I baseline — projection neural network
    AFRSFCV = "afrsfcv"     # Model II baseline — softmax gradient descent
    DTAP = "dtap"           # proposed — dual-track adaptive projection
    HU_CONST = "hu_const"   # Hu (2022) subgradient, constant step (SG-const)
    HU_DYN = "hu_dyn"       # Hu (2022) subgradient, dynamic step (SG-dyn)


class Classifier(Enum):
    SVM = "svm"
    KNN = "knn"


@dataclass(frozen=True)
class MethodStyle:
    label: str        # human-readable name used in tables and figures
    color: str        # matplotlib colour
    linestyle: object  # matplotlib linestyle (str or dash tuple)
    kind: str         # "baseline" | "nsfp" | "hu"


# Single source of truth for labels / plot styles, keyed by Method.
METHOD_REGISTRY: Dict[Method, MethodStyle] = {
    Method.N_FSCORE: MethodStyle("N-Fscore", "#009E73", "-", "baseline"),
    Method.AFRSFCV: MethodStyle("AFRSFCV", "#0072B2", "-", "baseline"),
    Method.DTAP: MethodStyle("DTAP", "#D55E00", "-", "nsfp"),
    Method.HU_CONST: MethodStyle("SG-const", "#9333ea", "-.", "hu"),
    Method.HU_DYN: MethodStyle("SG-dyn", "#d97706", (0, (3, 1, 1, 1)), "hu"),
}

# Style for the DTAP-vs-Hu convergence overlay (line widths + z-order differ).
CONVERGENCE_STYLE: Dict[Method, dict] = {
    Method.DTAP: dict(color="#2563eb", ls="-", lw=2.0, z=5),
    Method.HU_CONST: dict(color="#9333ea", ls="-.", lw=1.5, z=2),
    Method.HU_DYN: dict(color="#d97706", ls=(0, (3, 1, 1, 1)), lw=1.5, z=1),
}


def method_label(method: Method) -> str:
    return METHOD_REGISTRY[method].label
