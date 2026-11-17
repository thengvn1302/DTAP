"""Hyperparameters and dataset registry for the combined 3-constraint model.

Combined feasibility system on the probability simplex K = Delta_{m-1}:
    F1(w) = ||I - sum_k w_k R_k(D)||^2   (convex, Model II)
    F2(w) = ||1 - P w||^2                (convex, Model II)
    F3(w) = (w^T G w) / (rho^T w)        (pseudoconvex, Model I)
"""
from typing import Dict, List

from src.common.consts import Method

# Methods included in the main comparison (order matters for tables/plots).
COMPARISON_METHODS: List[Method] = [
    Method.N_FSCORE, Method.AFRSFCV, Method.DTAP, Method.HU_CONST, Method.HU_DYN,
]

DTAP_PARAMS = dict(
    rho_cvx=1.98,      # Polyak step multiplier rho in (0, 2)
    delta=1e-3,        # approximate-active-set tolerance
    epsilon=1e-6,      # stop when J(w_k) <= epsilon
    max_iter=1000,
)
DTAP_GAMMA = dict(
    offset=0.5,        # gamma_k = 1 / (k + offset)^power
    power=0.55,
)

# Hu (2022) subgradient variants share DTAP's stopping budget.
# v_const is the constant step size of SG-const.
HU_PARAMS = {**DTAP_PARAMS, "max_iter": 1000, "v_const": 0.001}

# grid_enabled=False uses the fixed (lambda1, lambda2) below, matching the paper.
AFRSFCV_PARAMS = dict(
    lr=0.001,
    max_iter=1000,
    grid_enabled=False,
    lambda1=1.0,
    lambda2=0.5,
    lambda1_grid=[0.1, 0.5, 1.0, 2.0],
    lambda2_grid=[0.01, 0.1, 0.5],
    val_fraction=0.2,
    theta=0.90,
)

N_FSCORE_PARAMS = dict(
    epsilon=0.001,       # PNN time constant
    time_horizon=0.2,    # total integration time T
    num_steps=1000,      # explicit-Euler steps (fixed budget)
)

# f_i_percentile=p means b_i is the p-th percentile of F_i(w) sampled uniformly
# on the simplex, so ~p% of simplex points satisfy F_i <= b_i.
USE_DATC = True   # True = adaptive per-dataset percentiles; False = global below.

THRESHOLD_CONFIG = dict(
    method="sampling_based",
    sampling_based=dict(
        n_samples=3000,
        seed=42,
        f1_percentile=20,
        f2_percentile=12,
        f3_percentile=75,
    ),
)

PREPROCESSING = dict(
    discretization_bins=10,
    psd_diagonal_shift=1e-10,
    fisher_denominator_epsilon=1e-12,
    fisher_inf_replacement_factor=10.0,
)

THETA_LIST: List[float] = [0.9]
N_FOLDS = 10
TEST_FRACTION = 0.2          # stratified hold-out, random_state=42
VOTE_THRESHOLD_LIST = None   # None -> auto [majority .. n_folds]
SVM_PARAMS = dict(kernel="rbf", C=1.0, gamma="scale")
KNN_K = 5

DATASETS: Dict[str, dict] = {
    "Glass": dict(loader="csv:Glass.csv", purpose="214 mau | 9 dac trung | 6 lop | Mat can bang"),
    "Diabetes": dict(loader="csv:Diabetes.csv", purpose="768 mau | 8 dac trung | 2 lop | Mat can bang"),
    "Segmentation": dict(loader="csv:Segmentation.csv", purpose="2310 mau | 18 dac trung | 7 lop | Can bang"),
    "Abalone": dict(loader="csv:Abalone.csv", purpose="4177 mau | 8 dac trung | 3 lop | Can bang"),
    "Satimage": dict(loader="csv:Satimage.csv", purpose="6435 mau | 36 dac trung | 6 lop | Mat can bang"),
    "Movement_libras": dict(loader="csv:Movement_libras.csv", purpose="360 mau | 90 dac trung | 15 lop | Can bang"),
    "Yeast": dict(loader="csv:Yeast.csv", purpose="1484 mau | 7 dac trung | 10 lop | Mat can bang"),
    "Spambase": dict(loader="csv:Spambase.csv", purpose="4601 mau | 57 dac trung | 2 lop | Mat can bang"),
    "Pendigits": dict(loader="csv:Pendigits.csv", purpose="10992 mau | 16 dac trung | 10 lop | Can bang"),
}

# The eight datasets of the classification study (Tables 1-5); Movement_libras is used only in Table 6.
CLASSIFICATION_DATASETS: List[str] = ["Glass", "Diabetes", "Segmentation", "Abalone", "Satimage",
                                      "Yeast", "Spambase", "Pendigits"]

# Table 6 beyond the standard start (`run_all.py hu2022`): AC, balanced DTAP, tuned SG-dyn, random starts.
# Random starts are Dirichlet(1) samples from np.random.default_rng(seed).
TABLE6_CONFIG = dict(
    start_rng="default_rng",
    tune_seeds=[1101, 1102, 1103],
    eval_seeds=[2101, 2102, 2103],
    modulus_seed=42,             # L_hat: 500 Dirichlet points (as the sampled SG-dyn column)
    n_samples_L=500,
    c_grid=[10.0 ** e for e in (-3.0, -2.5, -2.0, -1.5, -1.0, -0.5, 0.0, 0.5, 1.0)],
)

CONVERGENCE_CONFIG = dict(
    datasets=list(DATASETS.keys()),
    theta=0.90,
    seed=42,
    dpi=300,
    y_log_scale=True,
)
CURVE_CONFIG = dict(enabled=True, dpi=300)

# Nonconvex pseudoconvex test (47) -> Table 7. DTAP uses DTAP_PARAMS/DTAP_GAMMA,
# SG-const uses HU_PARAMS["v_const"].
SYNTHETIC_CONFIG = dict(
    dims=[2, 10, 50],
    kappas=[0.3, 1.0, 3.0],
    standard_start=1.5,          # x0 = 1.5 * ones(d)
    start_box=(0.8, 1.8),        # random starts uniform in [0.8, 1.8]^d
    start_rng="default_rng",     # random starts: np.random.default_rng(seed)
    tune_seeds=[1101, 1102, 1103],
    eval_seeds=[2101, 2102, 2103],
    modulus_seed=42,             # L_hat: 500 uniform points in K
    n_samples_L=500,
    c_grid=[10.0 ** e for e in (-3.0, -2.5, -2.0, -1.5, -1.0, -0.5, 0.0, 0.5, 1.0)],
    # Tuned SG-const: step nu chosen on the same exponents and by the same rule as c of SG-dyn.
    nu_grid=[10.0 ** e for e in (-3.0, -2.5, -2.0, -1.5, -1.0, -0.5, 0.0, 0.5, 1.0)],
)

# One-at-a-time changes of the DTAP parameters on test (47) (`run_all.py synthetic --dtap-sweep`).
# gamma_k = a / (k + 0.5)^s; the baseline is DTAP_PARAMS / DTAP_GAMMA (a = 1, s = 0.55).
SYNTHETIC_SWEEP = dict(
    kappas=[0.3, 1.0],
    settings=[
        ("baseline", {}, {}),
        ("S1 rho_cvx = 1", {"rho_cvx": 1.0}, {}),
        ("S2 delta = 1e-1", {"delta": 1e-1}, {}),
        ("S3 a = 10", {}, {"scale": 10.0}),
        ("S4 a = 100", {}, {"scale": 100.0}),
        ("S5 s = 0.75", {}, {"power": 0.75}),
        ("S6 s = 1", {}, {"power": 1.0}),
    ],
)
