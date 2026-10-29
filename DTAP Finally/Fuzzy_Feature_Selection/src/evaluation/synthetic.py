"""Nonconvex pseudoconvex test (47): Table 7 (solver comparison) and Table 8 (DTAP parameter sweep).

Table 7, for each d in {2, 10, 50} and kappa in {0.3, 1, 3} (nine configurations):
  1. L_hat = largest gradient norm at 500 uniform points of K = [-2, 2]^d.
  2. Tuned SG-dyn: L = c * L_hat; tuned SG-const: step nu. Each is chosen on three tuning starts by
     (max successes, min total evaluations, min total best residual); ties -> smallest value.
  3. Evaluation on the standard start 1.5 * 1 and three random starts:
     DTAP (I_cvx = {1, 2}, I_ps = {3}), balanced DTAP, SG-const, tuned SG-const,
     sampled SG-dyn, tuned SG-dyn.
Table 8: DTAP under one-at-a-time changes of rho_cvx, delta, a and s (SYNTHETIC_SWEEP).
A run succeeds when J <= epsilon within the evaluation budget (DTAP_PARAMS).
"""
import gzip
import json
import os
import time

import numpy as np
import pandas as pd

from src.common import config
from src.common.consts import RESULTS_DIR
from src.problem_formulation.problems import LogBallProblem
from src.solvers import DtapSolver, HuSolver, estimate_holder_modulus

METHODS = ["dtap", "dtap_balanced", "sg_const", "sg_const_tuned", "sg_dyn_sampled", "sg_dyn_tuned"]
LABELS = {"dtap": "DTAP", "dtap_balanced": "Balanced", "sg_const": "SG-const",
          "sg_const_tuned": "Tuned SG-const", "sg_dyn_sampled": "Sampled SG-dyn",
          "sg_dyn_tuned": "Tuned SG-dyn"}


def random_start(seed: int, d: int, kind: str) -> np.ndarray:
    lo, hi = config.SYNTHETIC_CONFIG["start_box"]
    if kind == "default_rng":
        return np.random.default_rng(seed).uniform(lo, hi, size=d)
    raise ValueError(f"unknown start_rng {kind!r}")


def _starts(problem: LogBallProblem, seeds: list, kind: str) -> list:
    """Standard start followed by the seeded random starts, as (label, x0)."""
    return [("standard", problem.start())] + [(str(s), random_start(s, problem.dim, kind)) for s in seeds]


def _record(res, eps: float) -> dict:
    return dict(evals=int(res.iter_count), success=bool(res.best_J <= eps), best_J=float(res.best_J),
                f3_active=int((res.J_nc_history > eps).sum()), time_sec=float(res.time_sec))


def _run(method: str, problem: LogBallProblem, x0: np.ndarray, *, v_const: float = None,
         L: float = None, params: dict = None, gamma: dict = None) -> dict:
    eps = float(config.DTAP_PARAMS["epsilon"])
    th = problem.thresholds
    if method in ("dtap", "dtap_balanced"):
        res = DtapSolver(problem, th, params or config.DTAP_PARAMS, gamma or config.DTAP_GAMMA,
                         weight="balanced" if method == "dtap_balanced" else "proportional").solve(w_init=x0)
    elif method in ("sg_const", "sg_const_tuned"):
        res = HuSolver(problem, th, mode="const",
                       params={**config.HU_PARAMS, "v_const": v_const}).solve(w_init=x0)
    else:
        res = HuSolver(problem, th, mode="dyn", params=config.HU_PARAMS, holder_modulus=L).solve(w_init=x0)
    rec = _record(res, eps)
    rec["dist_best_from_x0"] = float(np.linalg.norm(res.w - x0))
    rec["trajectory"] = dict(J=[float(x) for x in res.J_history], Jcvx=[float(x) for x in res.J_cvx_history],
                             Jps=[float(x) for x in res.J_nc_history])
    return rec


def _tune(method: str, problem: LogBallProblem, grid: list, starts: list, kwargs) -> dict:
    """Grid search on the tuning starts; `kwargs(value)` gives the _run keyword arguments."""
    trials, trajectories = [], []
    for value in grid:
        recs = [_run(method, problem, x0, **kwargs(value)) for x0 in starts]
        trajectories += [dict(value=value, start=i, **r.pop("trajectory")) for i, r in enumerate(recs)]
        trials.append(dict(value=value, successes=sum(r["success"] for r in recs),
                           evals=sum(r["evals"] for r in recs),
                           best_J=sum(r["best_J"] for r in recs),
                           time_sec=sum(r["time_sec"] for r in recs)))
    best = min(range(len(trials)),
               key=lambda i: (-trials[i]["successes"], trials[i]["evals"], trials[i]["best_J"], i))
    return dict(value=trials[best]["value"], trials=trials, trajectories=trajectories,
                evals=sum(t["evals"] for t in trials), time_sec=sum(t["time_sec"] for t in trials))


def _save_trajectories(out_dir: str, name: str, payload) -> None:
    with gzip.open(os.path.join(out_dir, name), "wt", encoding="utf-8") as f:
        json.dump(payload, f)


def witness_47() -> list:
    """Slacks of the exact witness x = -e1/10 of (47): 19/100, 31/25, kappa log(300/221)."""
    cfg, out = config.SYNTHETIC_CONFIG, []
    for kappa in cfg["kappas"]:
        for d in cfg["dims"]:
            problem = LogBallProblem(d, kappa)
            x = -problem.e1 / 10.0
            th = problem.thresholds
            slack = np.array([th["b1"], th["b2"], th["b3"]]) - problem.values(x)
            exact = [19 / 100, 31 / 25, kappa * np.log(300 / 221)]
            out.append(dict(d=d, kappa=kappa, slacks=slack.tolist(), exact=exact,
                            max_abs_error=float(np.max(np.abs(slack - exact))),
                            in_K=bool(np.all(np.abs(x) <= 2.0))))
    return out


def _cell(g: pd.DataFrame) -> str:
    return f"{int(g.success.sum())} ({g.evals.median():g})"


def run_synthetic(start_rng: str = None, v_const: float = None, out_dir: str = None) -> dict:
    """Table 7."""
    cfg = config.SYNTHETIC_CONFIG
    start_rng = start_rng or cfg["start_rng"]
    v_const = float(config.HU_PARAMS["v_const"] if v_const is None else v_const)
    out_dir = str(out_dir or os.path.join(str(RESULTS_DIR), "synthetic"))
    os.makedirs(out_dir, exist_ok=True)

    rows, tuning, trajectories = [], [], dict(evaluation=[], tuning=[])
    t_all = time.time()
    for kappa in cfg["kappas"]:
        for d in cfg["dims"]:
            problem = LogBallProblem(d, kappa)
            L_hat = estimate_holder_modulus(problem, n_samples=cfg["n_samples_L"],
                                            random_state=cfg["modulus_seed"])
            tune_starts = [random_start(s, d, start_rng) for s in cfg["tune_seeds"]]
            dyn = _tune("sg_dyn_tuned", problem, cfg["c_grid"], tune_starts, lambda c: dict(L=c * L_hat))
            const = _tune("sg_const_tuned", problem, cfg["nu_grid"], tune_starts, lambda nu: dict(v_const=nu))
            for meth, tu in (("sg_dyn_tuned", dyn), ("sg_const_tuned", const)):
                trajectories["tuning"] += [dict(method=meth, d=d, kappa=kappa, **t) for t in tu.pop("trajectories")]
            tuning.append(dict(d=d, kappa=kappa, L_hat=L_hat,
                               c=dyn["value"], evals=dyn["evals"], time_sec=dyn["time_sec"], trials=dyn["trials"],
                               nu=const["value"], nu_evals=const["evals"], nu_time_sec=const["time_sec"],
                               nu_trials=const["trials"]))
            for label, x0 in _starts(problem, cfg["eval_seeds"], start_rng):
                ball_dist = float(np.linalg.norm(x0 + problem.e1)) - 1.0
                kwargs = dict(dtap={}, dtap_balanced={}, sg_const=dict(v_const=v_const),
                              sg_const_tuned=dict(v_const=const["value"]),
                              sg_dyn_sampled=dict(L=L_hat), sg_dyn_tuned=dict(L=dyn["value"] * L_hat))
                for method in METHODS:
                    rec = _run(method, problem, x0, **kwargs[method])
                    trajectories["evaluation"].append(dict(method=method, d=d, kappa=kappa, start=label,
                                                           **rec.pop("trajectory")))
                    rows.append(dict(method=method, d=d, kappa=kappa, start=label,
                                     dist_x0_to_F1_ball=ball_dist, **rec))

    df = pd.DataFrame(rows)
    df.to_csv(os.path.join(out_dir, "synthetic_runs.csv"), index=False)
    with open(os.path.join(out_dir, "synthetic_tuning.json"), "w", encoding="utf-8") as f:
        json.dump(tuning, f, indent=1)
    _save_trajectories(out_dir, "synthetic_trajectories.json.gz", trajectories)
    with open(os.path.join(out_dir, "witness_47.json"), "w", encoding="utf-8") as f:
        json.dump(witness_47(), f, indent=1)

    budget = int(config.DTAP_PARAMS["max_iter"])
    lines = [f"Table 7 (47): start_rng={start_rng}, SG-const nu={v_const:g}, L_hat seed={cfg['modulus_seed']}",
             "Each cell: successes/12 (median evaluated points, capped runs counted as "
             f"{budget}).", ""]
    lines.append("kappa  " + "  ".join(f"{LABELS[m]:>15s}" for m in METHODS))
    for kappa in cfg["kappas"]:
        cells = [_cell(df[(df.method == m) & (df.kappa == kappa)]) for m in METHODS]
        lines.append(f"{kappa:<6g} " + "  ".join(f"{c:>15s}" for c in cells))
    lines.append("")
    for m in METHODS:
        g = df[df.method == m]
        lines.append(f"{LABELS[m]:16s} successes {int(g.success.sum())}/{len(g)}")
    for m in ("dtap", "dtap_balanced"):
        g = df[df.method == m]
        lines.append(f"{LABELS[m]} runs with an F3 violation: {int((g.f3_active > 0).sum())}/{len(g)}; "
                     f"pooled F3 activity {int(g.f3_active.sum())}/{int(g.evals.sum())}; "
                     f"failures at kappa = {sorted(set(g[~g.success].kappa))}")
    lines.append(f"Tuning SG-dyn: {sum(t['evals'] for t in tuning)} evaluated points, "
                 f"{sum(t['time_sec'] for t in tuning):.2f} s solver time (L_hat sampling excluded)")
    lines.append(f"Tuning SG-const: {sum(t['nu_evals'] for t in tuning)} evaluated points, "
                 f"{sum(t['nu_time_sec'] for t in tuning):.2f} s solver time")
    lines.append("Chosen c per (d, kappa): " + ", ".join(
        f"({t['d']}, {t['kappa']:g}): {t['c']:.4g}" for t in tuning))
    lines.append("Chosen nu per (d, kappa): " + ", ".join(
        f"({t['d']}, {t['kappa']:g}): {t['nu']:.4g}" for t in tuning))
    sg = df[df.method == "sg_const"]
    lines.append(f"SG-const (nu={v_const:g}): max ||x_best - x0|| = {sg.dist_best_from_x0.max():.4f} "
                 f"(bound {(budget - 1) * v_const:.4f}); min distance from a start to "
                 f"{{||x + e1|| <= 1}} = {sg.dist_x0_to_F1_ball.min():.4f}")
    lines.append(f"Wall time {time.time() - t_all:.1f} s")
    text = "\n".join(lines) + "\n"
    with open(os.path.join(out_dir, "table7.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    print(text)
    return dict(runs=df, tuning=tuning, text=text)


def run_dtap_sweep(start_rng: str = None, out_dir: str = None) -> dict:
    """Table 8: DTAP on (47) under one-at-a-time parameter changes."""
    cfg, sweep = config.SYNTHETIC_CONFIG, config.SYNTHETIC_SWEEP
    start_rng = start_rng or cfg["start_rng"]
    out_dir = str(out_dir or os.path.join(str(RESULTS_DIR), "synthetic"))
    os.makedirs(out_dir, exist_ok=True)

    rows, trajectories = [], []
    t_all = time.time()
    for name, p_over, g_over in sweep["settings"]:
        params = {**config.DTAP_PARAMS, **p_over}
        gamma = {**config.DTAP_GAMMA, **g_over}
        for kappa in sweep["kappas"]:
            for d in cfg["dims"]:
                problem = LogBallProblem(d, kappa)
                for label, x0 in _starts(problem, cfg["eval_seeds"], start_rng):
                    rec = _run("dtap", problem, x0, params=params, gamma=gamma)
                    trajectories.append(dict(setting=name, d=d, kappa=kappa, start=label, **rec.pop("trajectory")))
                    rows.append(dict(setting=name, rho_cvx=params["rho_cvx"], delta=params["delta"],
                                     a=gamma.get("scale", 1.0), s=gamma["power"],
                                     d=d, kappa=kappa, start=label, **rec))

    df = pd.DataFrame(rows)
    df.to_csv(os.path.join(out_dir, "synthetic_sweep.csv"), index=False)
    _save_trajectories(out_dir, "synthetic_sweep_trajectories.json.gz", trajectories)
    lines = [f"Table 8 (47): DTAP, one-at-a-time changes; start_rng={start_rng}",
             "gamma_k = a / (k + 0.5)^s; baseline rho_cvx = 1.98, delta = 1e-3, a = 1, s = 0.55.",
             "Each cell: successes/12 (median evaluated points, capped runs counted as "
             f"{int(config.DTAP_PARAMS['max_iter'])}).", ""]
    lines.append(f"{'setting':18s}" + "".join(f"{'kappa = ' + format(k, 'g'):>16s}" for k in sweep["kappas"])
                 + f"{'total':>8s}")
    for name, _, _ in sweep["settings"]:
        g = df[df.setting == name]
        cells = [_cell(g[g.kappa == k]) for k in sweep["kappas"]]
        lines.append(f"{name:18s}" + "".join(f"{c:>16s}" for c in cells)
                     + f"{str(int(g.success.sum())) + '/' + str(len(g)):>8s}")
    lines.append(f"Wall time {time.time() - t_all:.1f} s")
    text = "\n".join(lines) + "\n"
    with open(os.path.join(out_dir, "table8.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    print(text)
    return dict(runs=df, text=text)
