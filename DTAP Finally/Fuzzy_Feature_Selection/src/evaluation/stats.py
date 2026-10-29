"""Tables 1-5 and the Section 4.3 numbers from the saved comparison results (`run_all.py stats`).

Input : results/comparison.csv (majority-vote row, theta = 0.9, of each classification dataset).
Output: results/stats/{table1..table5}.txt and stats.json.

Table 4 and Table 5 use the unrounded scores.
Table 5: exact two-sided signed-rank test (zero differences omitted, midranks, all 2^n signs
enumerated, p = 1 when every difference is zero), Holm over the four DTAP-baseline comparisons
of each metric, and the tie-corrected asymptotic Friedman test over the five selection methods.
"""
import itertools
import json
import os

import numpy as np
import pandas as pd
from scipy import stats as st

from src.common import config
from src.common.consts import RESULTS_DIR

STATS_DIR = os.path.join(str(RESULTS_DIR), "stats")
SELECTORS = ["n_fscore", "afrsfcv", "dtap", "hu_const", "hu_dyn"]
LABELS = {"full": "Full", "n_fscore": "N-Fscore", "afrsfcv": "AFRSFCV", "dtap": "DTAP",
          "hu_const": "SG-const", "hu_dyn": "SG-dyn"}
METRICS = [("svm_acc", "Accuracy, SVM", 2), ("knn_acc", "Accuracy, 5-NN", 2),
           ("svm_roc", "AUC, SVM", 4), ("knn_roc", "AUC, 5-NN", 4)]
BASELINES = ["n_fscore", "afrsfcv", "hu_const", "hu_dyn"]


def signed_rank_exact(d: np.ndarray) -> float:
    d = np.asarray(d, float)
    d = d[d != 0]
    n = len(d)
    if n == 0:
        return 1.0
    ranks = st.rankdata(np.abs(d))
    total = ranks.sum()
    w_plus = ranks[d > 0].sum()
    observed = min(w_plus, total - w_plus)
    hits = 0
    for signs in itertools.product((0, 1), repeat=n):
        s = float(np.dot(signs, ranks))
        if min(s, total - s) <= observed + 1e-9:
            hits += 1
    return hits / 2 ** n


def holm(p: list) -> list:
    order = np.argsort(p, kind="stable")
    adj, running = [0.0] * len(p), 0.0
    for i, j in enumerate(order):
        running = max(running, min(1.0, (len(p) - i) * p[j]))
        adj[j] = running
    return adj


def _majority_rows(df: pd.DataFrame) -> pd.DataFrame:
    df = df[np.isclose(df.theta, 0.9) & (df.vote_threshold == df.outer_folds // 2 + 1)]
    present = [d for d in config.CLASSIFICATION_DATASETS if d in set(df.dataset)]
    return df.set_index("dataset").loc[present]


def _score(rows: pd.DataFrame, method: str, metric: str) -> np.ndarray:
    col = f"raw_{metric}" if method == "full" else f"{method}_{metric}"
    return rows[col].to_numpy(float)


def run_stats(csv_path: str = None) -> dict:
    csv_path = csv_path or os.path.join(str(RESULTS_DIR), "comparison.csv")
    rows = _majority_rows(pd.read_csv(csv_path))
    names = list(rows.index)
    complete = len(names) == len(config.CLASSIFICATION_DATASETS)
    flag = "" if complete else f"  [INCOMPLETE: {len(names)}/8 classification datasets present: {names}]"
    os.makedirs(STATS_DIR, exist_ok=True)
    out = dict(datasets=names, complete=complete)
    texts = {}

    # Table 1 (n, p, r).
    t1 = [f"Table 1: dataset sizes{flag}", f"{'Dataset':14s}{'n':>8s}{'p':>5s}{'r':>5s}"]
    out["table1"] = {d: dict(n=int(rows.loc[d, "n"]), p=int(rows.loc[d, "m"]), r=int(rows.loc[d, "r"])) for d in names}
    t1 += [f"{d:14s}{v['n']:>8d}{v['p']:>5d}{v['r']:>5d}" for d, v in out["table1"].items()]
    texts["table1"] = t1

    # Table 2 (selected count / Nogueira stability).
    out["table2"] = {d: {m: dict(n_sel=int(rows.loc[d, f"{m}_n_sel"]), stability=float(rows.loc[d, f"{m}_nogueira"]))
                         for m in SELECTORS} for d in names}
    t2 = [f"Table 2: |A*| / Nogueira stability{flag}",
          f"{'Dataset':14s}{'p':>4s}" + "".join(f"{LABELS[m]:>11s}" for m in SELECTORS)]
    for d in names:
        t2.append(f"{d:14s}{out['table1'][d]['p']:>4d}" + "".join(
            f"{str(out['table2'][d][m]['n_sel']) + '/' + format(out['table2'][d][m]['stability'], '.3f'):>11s}"
            for m in SELECTORS))
    texts["table2"] = t2

    # Table 3 (accuracy % / macro OvR AUC) and the SG exceptions.
    out["table3"] = {d: {m: {met: float(_score(rows.loc[[d]], m, met)[0]) for met, _, _ in METRICS}
                         for m in ["full"] + SELECTORS} for d in names}
    t3 = [f"Table 3: accuracy (%) / macro one-vs-rest AUC{flag}",
          f"{'Dataset':14s}{'Clf':5s}" + "".join(f"{LABELS[m]:>15s}" for m in ["full", "n_fscore", "afrsfcv", "dtap"])]
    for d in names:
        for clf in ("svm", "knn"):
            t3.append(f"{d:14s}{('SVM' if clf == 'svm' else '5-NN'):5s}" + "".join(
                f"{format(out['table3'][d][m][clf + '_acc'], '.2f') + '/' + format(out['table3'][d][m][clf + '_roc'], '.4f'):>15s}"
                for m in ["full", "n_fscore", "afrsfcv", "dtap"]))
    exceptions = {}
    for d in names:
        for m in ("hu_const", "hu_dyn"):
            if rows.loc[d, f"{m}_voted_feat"] != rows.loc[d, "dtap_voted_feat"]:
                exceptions.setdefault(d, {})[m] = {k: out["table3"][d][m][k] for k, _, _ in METRICS}
    out["sg_exceptions"] = exceptions
    t3.append("SG exceptions (voted mask differs from DTAP): " + (json.dumps(exceptions) if exceptions else "none"))
    texts["table3"] = t3

    # Table 4 (unweighted means).
    means = {m: {met: float(np.mean(_score(rows, m, met))) for met, _, _ in METRICS} for m in ["full"] + SELECTORS}
    out["table4"] = means
    t4 = [f"Table 4: unweighted means{flag}",
          f"{'Method':10s}" + "".join(f"{lab:>16s}" for _, lab, _ in METRICS)]
    t4 += [f"{LABELS[m]:10s}" + "".join(f"{format(means[m][met], '.' + str(dec) + 'f'):>16s}"
                                        for met, _, dec in METRICS) for m in ["full"] + SELECTORS]
    texts["table4"] = t4

    # Table 5 (signed-rank tests with Holm adjustment; Friedman).
    t5 = [f"Table 5: raw / Holm-adjusted signed-rank p; tie-corrected Friedman{flag}",
          f"{'Metric':16s}" + "".join(f"{LABELS[m]:>16s}" for m in BASELINES) + f"{'Friedman':>10s}"]
    res5 = {}
    for met, lab, _ in METRICS:
        raw = [signed_rank_exact(_score(rows, "dtap", met) - _score(rows, b, met)) for b in BASELINES]
        adj = holm(raw)
        fried = float(st.friedmanchisquare(*[_score(rows, m, met) for m in SELECTORS]).pvalue) \
            if len(names) >= 2 else float("nan")
        res5[met] = dict(raw=dict(zip(BASELINES, raw)), holm=dict(zip(BASELINES, adj)), friedman=fried)
        t5.append(f"{lab:16s}" + "".join(f"{format(r, '.4f') + '/' + format(a, '.4f'):>16s}"
                                         for r, a in zip(raw, adj)) + f"{fried:>10.4f}")
    out["table5"] = res5
    texts["table5"] = t5

    # Section 4.3 numbers.
    frac = [out["table2"][d]["dtap"]["n_sel"] / out["table1"][d]["p"] for d in names]
    t3u = out["table4"]
    out["section43"] = dict(
        dtap_mean_retained_pct=100 * float(np.mean(frac)),
        dtap_mean_stability=float(np.mean([out["table2"][d]["dtap"]["stability"] for d in names])),
        nfscore_mean_stability=float(np.mean([out["table2"][d]["n_fscore"]["stability"] for d in names])),
        full_minus_dtap_svm=t3u["full"]["svm_acc"] - t3u["dtap"]["svm_acc"],
        full_minus_dtap_knn=t3u["full"]["knn_acc"] - t3u["dtap"]["knn_acc"],
        dtap_minus_nfscore_svm=t3u["dtap"]["svm_acc"] - t3u["n_fscore"]["svm_acc"],
        dtap_minus_afrsfcv_svm=t3u["dtap"]["svm_acc"] - t3u["afrsfcv"]["svm_acc"],
        sg_mask_equal_datasets=[d for d in names if d not in exceptions],
        svm_base_adjusted_p=[out["table5"][met]["holm"][b] for met in ("svm_acc", "svm_roc")
                             for b in ("n_fscore", "afrsfcv")])
    s = out["section43"]
    texts["section43"] = [f"Section 4.3 numbers{flag}"] + [f"{k}: {v}" for k, v in s.items()]

    for key, lines in texts.items():
        with open(os.path.join(STATS_DIR, f"{key}.txt"), "w", encoding="utf-8") as f:
            f.write("\n".join(lines) + "\n")
    with open(os.path.join(STATS_DIR, "stats.json"), "w", encoding="utf-8") as f:
        json.dump(out, f, indent=1)
    print("\n\n".join("\n".join(v) for v in texts.values()))
    return out
