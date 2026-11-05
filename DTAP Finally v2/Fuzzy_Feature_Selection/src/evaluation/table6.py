"""Table 6 beyond the standard-start columns, on the full-data feature-selection instances.

For one instance (called from convergence.py, command `run_all.py hu2022`):
  - methods DTAP, AC (all-convex comparator), balanced DTAP, SG-const, sampled SG-dyn, tuned SG-dyn;
  - standard start (uniform weights) and the Dirichlet starts of TABLE6_CONFIG;
  - tuned SG-dyn: L = c * L_hat, c chosen on the tuning starts by (max successes, min total evaluations,
    min total best residual), ties -> smallest c; tuning records and cost;
  - F3 activity, raw trajectories, threshold metadata;
  - witness: the evaluated point with the largest slack min_i (b_i - F_i(w)) over all evaluation runs,
    checked later by `independent_check` on freshly built matrices.
`assemble_table6` builds table6.txt / .csv, tuning_records.json and witnesses from the per-dataset files.
"""
import gzip
import json
import os
import time

import numpy as np

from src.common import config
from src.common.consts import RESULTS_DIR
from src.data_processors.loaders import load_dataset, scale_train_test
from src.problem_formulation.constraints import values
from src.problem_formulation.matrices import build_matrices
from src.problem_formulation.thresholds import build_threshold_config, dataset_adaptive_config, prepare_from_prep
from src.solvers import DtapSolver, HuSolver, estimate_holder_modulus

METHODS = ["dtap", "ac", "balanced", "sg_const", "sg_dyn_sampled", "sg_dyn_tuned"]
LABELS = {"dtap": "DTAP", "ac": "AC", "balanced": "Balanced", "sg_const": "SG-const",
          "sg_dyn_sampled": "Sampled", "sg_dyn_tuned": "Tuned"}
DATASET_DIR = os.path.join(str(RESULTS_DIR), "hu2022", "datasets")
WITNESS_DIR = os.path.join(str(RESULTS_DIR), "witnesses")
THRESHOLD_DIR = os.path.join(str(RESULTS_DIR), "thresholds")


def dirichlet_start(seed: int, p: int, kind: str) -> np.ndarray:
    if kind == "default_rng":
        return np.random.default_rng(seed).dirichlet(np.ones(p))
    raise ValueError(f"unknown start generator {kind!r}")


def _solve(method: str, prep: dict, th: dict, w0, *, L: float = None, record: bool = False):
    seed = int(config.TABLE6_CONFIG["modulus_seed"])
    if method in ("dtap", "ac", "balanced"):
        solver = DtapSolver(prep, th, config.DTAP_PARAMS, config.DTAP_GAMMA,
                            weight="balanced" if method == "balanced" else "proportional",
                            assignment="all_convex" if method == "ac" else "split")
    elif method == "sg_const":
        solver = HuSolver(prep, th, mode="const", params=config.HU_PARAMS)
    else:
        solver = HuSolver(prep, th, mode="dyn", params=config.HU_PARAMS, holder_modulus=L)
    return solver.solve(w_init=w0, seed=seed, record=record)


def _traj(res) -> dict:
    return dict(J=[float(x) for x in res.J_history], Jcvx=[float(x) for x in res.J_cvx_history],
                Jps=[float(x) for x in res.J_nc_history])


def threshold_metadata(name: str, n: int, p: int, class_counts, thresholds: dict) -> dict:
    adp = dataset_adaptive_config(n, p, len(class_counts), class_counts)
    return dict(dataset=name, n=n, p=p, percentiles={k: adp[k] for k in ("f1_percentile", "f2_percentile",
                                                                             "f3_percentile")},
                sampling=dict(n_samples=3000, seed=42, plus_vertices=True),
                b1=float(thresholds["b1"]), b2=float(thresholds["b2"]), b3=float(thresholds["b3"]))


def run_table6_extras(name: str, prep: dict, prepared: dict) -> dict:
    cfg = config.TABLE6_CONFIG
    eps = float(config.DTAP_PARAMS["epsilon"])
    th = prepared["thresholds"]
    b = np.array([th["b1"], th["b2"], th["b3"]], float)
    p = int(prep["m"])
    L_hat = estimate_holder_modulus(prep, n_samples=cfg["n_samples_L"], random_state=cfg["modulus_seed"])

    runs, best = [], dict(slack=-np.inf)
    kinds = [cfg["start_rng"]]

    def evaluate(method, label, kind, w0, L=None):
        res = _solve(method, prep, th, w0, L=L, record=True)
        F = res.F_history
        slack = (b[None, :] - F).min(axis=1)
        i = int(np.argmax(slack))
        if slack[i] > best["slack"]:
            best.update(slack=float(slack[i]), w=res.X_history[i].tolist(), method=method, start=label,
                        start_rng=kind, iteration=i)
        rec = dict(method=method, start=label, start_rng=kind,
                   evals=int(res.iter_count),
                   success=bool(res.best_J <= eps), best_J=float(res.best_J),
                   f3_active=int((F[:, 2] - b[2] > eps).sum()), time_sec=float(res.time_sec),
                   trajectory=_traj(res))
        runs.append(rec)
        return res, rec

    standard = {}
    for m in METHODS[:-1]:  # tuned SG-dyn depends on the tuning starts; run below
        res, _ = evaluate(m, "standard", "-", None, L=L_hat if m == "sg_dyn_sampled" else None)
        standard[m] = res

    tuning = {}
    for kind in kinds:
        tune_starts = [dirichlet_start(s, p, kind) for s in cfg["tune_seeds"]]
        trials = []
        for c in cfg["c_grid"]:
            recs = []
            for s, w0 in zip(cfg["tune_seeds"], tune_starts):
                r = _solve("sg_dyn_tuned", prep, th, w0, L=c * L_hat)
                recs.append(dict(seed=s, evals=int(r.iter_count), success=bool(r.best_J <= eps),
                                 best_J=float(r.best_J), time_sec=float(r.time_sec), trajectory=_traj(r)))
            trials.append(dict(c=c, successes=sum(x["success"] for x in recs), evals=sum(x["evals"] for x in recs),
                               best_J=sum(x["best_J"] for x in recs), time_sec=sum(x["time_sec"] for x in recs),
                               runs=recs))
        k = min(range(len(trials)),
                key=lambda i: (-trials[i]["successes"], trials[i]["evals"], trials[i]["best_J"], i))
        c_star = trials[k]["c"]
        tuning[kind] = dict(c=c_star, L=c_star * L_hat, evals=sum(t["evals"] for t in trials),
                            time_sec=sum(t["time_sec"] for t in trials), trials=trials)

    # The standard-start tuned run depends on c, hence on the tuning starts.
    for kind in kinds:
        evaluate("sg_dyn_tuned", "standard", kind, None, L=tuning[kind]["L"])
        for s in cfg["eval_seeds"]:
            w0 = dirichlet_start(s, p, kind)
            for m in METHODS:
                L = L_hat if m == "sg_dyn_sampled" else (tuning[kind]["L"] if m == "sg_dyn_tuned" else None)
                evaluate(m, str(s), kind, w0, L=L)

    return dict(dataset=name, L_hat=L_hat, tuning=tuning, runs=runs,
                witness_candidates=dict(
                    witness=dict(w=best.get("w"), method=best.get("method"), start=best.get("start"),
                                 start_rng=best.get("start_rng"), iteration=best.get("iteration"),
                                 slack_in_run=best["slack"])))


def independent_check(name: str, candidates: dict) -> dict:
    """Rebuild the instance from the data and evaluate F at the saved witness points."""
    cfg_entry = config.DATASETS[name]
    X, y = load_dataset(name, cfg_entry)
    thr_cfg = build_threshold_config(dataset_adaptive_config(int(X.shape[0]), int(X.shape[1]),
                                                             len(np.unique(y)), np.bincount(y)))
    Xsc, _ = scale_train_test(X, X)
    prep = build_matrices(Xsc, y)
    th = prepare_from_prep(prep, thr_cfg)["thresholds"]
    b = np.array([th["b1"], th["b2"], th["b3"]], float)
    out = dict(dataset=name, b=b.tolist(), fisher_min=float(np.min(prep["rho"])))
    for key, cand in candidates.items():
        if cand.get("w") is None:
            out[key] = None
            continue
        w = np.asarray(cand["w"], float)
        F = values(w, prep)
        s = b - F
        out[key] = dict(cand, F=F.tolist(), slacks=s.tolist(), min_slack=float(s.min()),
                        strictly_feasible=bool(np.all(s > 0)), on_simplex=bool(np.all(w >= 0)),
                        sum_w=float(w.sum()))
    return out


def save_dataset(name: str, payload: dict) -> None:
    os.makedirs(DATASET_DIR, exist_ok=True)
    with gzip.open(os.path.join(DATASET_DIR, f"{name}.json.gz"), "wt", encoding="utf-8") as f:
        json.dump(payload, f)


def load_datasets() -> dict:
    out = {}
    for name in config.DATASETS:
        path = os.path.join(DATASET_DIR, f"{name}.json.gz")
        if os.path.isfile(path):
            with gzip.open(path, "rt", encoding="utf-8") as f:
                out[name] = json.load(f)
    return out


def assemble_table6(data: dict) -> str:
    """table6.txt/.csv, tuning_records.json, witnesses/feature_witnesses.json."""
    out_dir = os.path.join(str(RESULTS_DIR), "hu2022")
    os.makedirs(WITNESS_DIR, exist_ok=True)
    os.makedirs(THRESHOLD_DIR, exist_ok=True)
    budget = int(config.DTAP_PARAMS["max_iter"])
    texts = []
    kinds = [config.TABLE6_CONFIG["start_rng"]]
    for kind in kinds:
        data_k = {n: d for n, d in data.items() if kind in d["extras"]["tuning"]}
        lines = [f"Table 6 (full-data instances), random starts: Dirichlet(1), {kind}; "
                 f"datasets present: {len(data_k)}/9", "",
                 f"{'Dataset':16s}{'DTAP':>7s}{'AC':>7s}{'SG-const':>10s}{'Sampled':>9s}{'Tuned':>7s}"
                 f"{'F3 activity':>13s}{'c':>9s}"]
        csv = ["dataset,dtap,ac,sg_const,sampled,tuned,f3_active,dtap_evals,c"]
        totals = {m: [0, 0] for m in METHODS}
        std_succ = {"sg_dyn_sampled": [0, 0], "sg_dyn_tuned": [0, 0]}
        cost_evals = cost_time = 0.0
        for name, d in data_k.items():
            ext = d["extras"]
            runs = [r for r in ext["runs"] if r["start_rng"] in ("-", kind)]
            std = {r["method"]: r for r in runs if r["start"] == "standard"}

            def cell(m):
                r = std[m]
                return f"{r['evals']}{'' if r['success'] else '†'}"
            for m in METHODS:
                for r in runs:
                    if r["method"] == m:
                        totals[m][0] += int(r["success"])
                        totals[m][1] += 1
            for m in std_succ:
                std_succ[m][0] += int(std[m]["success"])
                std_succ[m][1] += 1
            tu = ext["tuning"][kind]
            cost_evals += tu["evals"]
            cost_time += tu["time_sec"]
            f3 = f"{std['dtap']['f3_active']}/{std['dtap']['evals']}"
            lines.append(f"{name:16s}{cell('dtap'):>7s}{cell('ac'):>7s}{cell('sg_const'):>10s}"
                         f"{cell('sg_dyn_sampled'):>9s}{cell('sg_dyn_tuned'):>7s}{f3:>13s}{tu['c']:>9.4g}")
            csv.append(",".join([name] + [cell(m) for m in ("dtap", "ac", "sg_const", "sg_dyn_sampled",
                                                              "sg_dyn_tuned")]
                                + [str(std["dtap"]["f3_active"]), str(std["dtap"]["evals"]), repr(tu["c"])]))
        lines += ["", f"† = tolerance not reached within {budget} evaluated points.",
                  "Successes over the standard start and the evaluation starts (all datasets present):"]
        lines += [f"  {LABELS[m]:9s} {totals[m][0]}/{totals[m][1]}" for m in METHODS]
        lines.append(f"Standard-start successes: sampled SG-dyn {std_succ['sg_dyn_sampled'][0]}/"
                     f"{std_succ['sg_dyn_sampled'][1]}, tuned SG-dyn {std_succ['sg_dyn_tuned'][0]}/"
                     f"{std_succ['sg_dyn_tuned'][1]}")
        lines.append(f"Tuning searches: {int(cost_evals)} evaluated points, {cost_time:.2f} s solver time "
                     "(L_hat sampling, preprocessing and search overhead excluded)")
        text = "\n".join(lines) + "\n"
        with open(os.path.join(out_dir, "table6.txt"), "w", encoding="utf-8") as f:
            f.write(text)
        with open(os.path.join(out_dir, "table6.csv"), "w", encoding="utf-8") as f:
            f.write("\n".join(csv) + "\n")
        texts.append(text)

    records = {name: {kind: dict(c=t["c"], L=t["L"], L_hat=d["extras"]["L_hat"], evals=t["evals"],
                                 time_sec=t["time_sec"],
                                 trials=[{k: v for k, v in tr.items() if k != "runs"} for tr in t["trials"]])
                      for kind, t in d["extras"]["tuning"].items()} for name, d in data.items()}
    with open(os.path.join(out_dir, "tuning_records.json"), "w", encoding="utf-8") as f:
        json.dump(records, f, indent=1)

    checks = {name: d["witness_check"] for name, d in data.items()}
    wit = dict(checks)
    vals = [w["witness"]["min_slack"] for w in checks.values() if w.get("witness")]
    wit["smallest_min_slack"] = min(vals) if vals else None
    wit["all_strictly_feasible"] = all(w["witness"]["strictly_feasible"] for w in checks.values()
                                       if w.get("witness")) if vals else None
    wit["smallest_fisher"] = min(w["fisher_min"] for w in checks.values()) if checks else None
    with open(os.path.join(WITNESS_DIR, "feature_witnesses.json"), "w", encoding="utf-8") as f:
        json.dump(wit, f, indent=1)
    for name, d in data.items():
        with open(os.path.join(THRESHOLD_DIR, f"{name}_full.json"), "w", encoding="utf-8") as f:
            json.dump(d["thresholds"], f, indent=1)
    return "\n".join(texts)
