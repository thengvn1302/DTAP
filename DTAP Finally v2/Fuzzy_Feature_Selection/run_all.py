"""Entry point for the Fuzzy_FS experiments.

Run from the project root:

    python run_all.py all [--reuse]   (--reuse: keep the datasets already saved in results/)
    python run_all.py comparison [--datasets Glass,Diabetes] [--methods dtap,afrsfcv] [--skip-existing]
    python run_all.py stats
    python run_all.py hu2022     [--datasets ...] [--no-plots] [--skip-existing] [--assemble-only]
    python run_all.py q1
    python run_all.py synthetic  [--out DIR]
    python run_all.py synthetic --dtap-sweep [--out DIR]
    python run_all.py hashes     [--check]

Pipeline (`all`), Tables 2-8 in order:
    1. comparison -> comparison.csv / .txt, comparison/<dataset>.*, thresholds/<dataset>_folds.json, curve data
    2. stats      -> stats/table1..table5.txt, stats.json                       (Tables 1-5)
    3. hu2022     -> hu2022/q2_*, hu2022/table6.{txt,csv}, tuning_records.json, datasets/*.json.gz,
                     witnesses/feature_witnesses.json, thresholds/<dataset>_full.json   (Table 6)
    4. q1         -> curve_svm.png, curve_knn.png (not in the paper)
    5. synthetic  -> synthetic/{table7.txt, synthetic_runs.csv, synthetic_tuning.json,
                     synthetic_trajectories.json.gz, witness_47.json}             (Table 7)
    6. synthetic --dtap-sweep -> synthetic/{table8.txt, synthetic_sweep.csv, ...}  (Table 8)
    7. hashes     -> SHA256SUMS
"""
import argparse
import os
import sys
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(PROJECT_DIR))
os.environ.setdefault("LOKY_MAX_CPU_COUNT", "1")
for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

from src.common import config
from src.common.consts import RESULTS_DIR, Method
from src.evaluation.comparison import run_experiment_comparison
from src.evaluation.convergence import run_convergence
from src.evaluation.curves import load_curve_data, render_grid_figure
from src.evaluation.stats import run_stats
from src.evaluation.synthetic import run_dtap_sweep, run_synthetic
from src.common.hashes import check_sums, write_sums


def _parse_csv(value: str, allowed: list):
    if value is None or value.strip().lower() in {"", "all"}:
        return None
    items = [x.strip() for x in value.split(",") if x.strip()]
    bad = [x for x in items if x not in allowed]
    if bad:
        raise SystemExit(f"Unknown values {bad}; allowed: {allowed}")
    return items


def cmd_comparison(argv=None) -> int:
    p = argparse.ArgumentParser(prog="run_all.py comparison")
    p.add_argument("--datasets", default="all")
    p.add_argument("--methods", default="all",
                   help="comma list of method ids; default = config.COMPARISON_METHODS")
    p.add_argument("--skip-existing", action="store_true",
                   help="skip datasets already saved in results/comparison/ (the combined files are still rebuilt)")
    args = p.parse_args(argv)

    datasets = _parse_csv(args.datasets, list(config.DATASETS))
    method_ids = _parse_csv(args.methods, [m.value for m in Method])
    if method_ids is not None:
        config.COMPARISON_METHODS = [Method(mid) for mid in method_ids]
    if args.skip_existing:
        datasets = [d for d in (datasets or list(config.DATASETS))
                    if not os.path.isfile(os.path.join(str(RESULTS_DIR), "comparison", f"{d}.csv"))]
        print(f"  --skip-existing: running {datasets or 'no dataset'}")

    run_experiment_comparison(datasets=datasets)
    return 0


def cmd_hu2022(argv=None) -> int:
    p = argparse.ArgumentParser(prog="run_all.py hu2022")
    p.add_argument("--datasets", default="all")
    p.add_argument("--no-plots", action="store_true")
    p.add_argument("--assemble-only", action="store_true",
                   help="rebuild the Table 6 outputs from the saved per-dataset results without running")
    p.add_argument("--skip-existing", action="store_true",
                   help="skip datasets already saved in results/hu2022/datasets/ (the outputs are still rebuilt)")
    args = p.parse_args(argv)

    datasets = None if args.datasets == "all" else [d.strip() for d in args.datasets.split(",")]
    assemble_only = args.assemble_only
    if args.skip_existing:
        datasets = [d for d in (datasets or list(config.DATASETS))
                    if not os.path.isfile(os.path.join(str(RESULTS_DIR), "hu2022", "datasets", f"{d}.json.gz"))]
        print(f"  --skip-existing: running {datasets or 'no dataset'}")
        assemble_only = assemble_only or not datasets
    run_convergence(datasets=datasets, make_plots=not args.no_plots, assemble_only=assemble_only)
    return 0


def cmd_q1(argv=None) -> int:
    argparse.ArgumentParser(prog="run_all.py q1").parse_args(argv)
    all_curves = load_curve_data(str(RESULTS_DIR))
    if not all_curves:
        print("No curve data. Run: python run_all.py comparison")
        return 1
    for metric in ("svm", "knn"):
        out = os.path.join(str(RESULTS_DIR), f"curve_{metric}.png")
        render_grid_figure(all_curves, metric, out, dpi=config.CURVE_CONFIG["dpi"])
        print(f"  Saved: {out}")
    return 0


def cmd_synthetic(argv=None) -> int:
    p = argparse.ArgumentParser(prog="run_all.py synthetic")
    p.add_argument("--out", default=None, help="output directory (default: results/synthetic)")
    p.add_argument("--dtap-sweep", action="store_true",
                   help="run the DTAP parameter sweep (Table 8) instead of Table 7")
    args = p.parse_args(argv)

    if args.dtap_sweep:
        run_dtap_sweep(out_dir=args.out)
    else:
        run_synthetic(out_dir=args.out)
    return 0


def cmd_stats(argv=None) -> int:
    argparse.ArgumentParser(prog="run_all.py stats").parse_args(argv)
    if not os.path.isfile(os.path.join(str(RESULTS_DIR), "comparison.csv")):
        print("No comparison results. Run: python run_all.py comparison")
        return 1
    run_stats()
    return 0


def cmd_hashes(argv=None) -> int:
    p = argparse.ArgumentParser(prog="run_all.py hashes")
    p.add_argument("--check", action="store_true", help="verify SHA256SUMS instead of writing it")
    args = p.parse_args(argv)
    return check_sums() if args.check else write_sums()


_STEPS = {
    "comparison": cmd_comparison,
    "stats": cmd_stats,
    "hu2022": cmd_hu2022,
    "q1": cmd_q1,
    "synthetic": cmd_synthetic,
    "hashes": cmd_hashes,
}


def main(argv=None) -> int:
    argv = list(sys.argv[1:]) if argv is None else list(argv)
    step = argv[0] if argv else "all"
    rest = argv[1:]

    if step in ("-h", "--help"):
        print(__doc__)
        return 0

    if step == "all":
        if rest not in ([], ["--reuse"]):
            print("`all` takes only the optional flag --reuse.")
            return 2
        # --reuse: comparison and hu2022 skip the datasets already saved in results/ (the combined
        # outputs are rebuilt); every other step runs.
        reuse = ["--skip-existing"] if rest == ["--reuse"] else []
        order = [("comparison", lambda argv: cmd_comparison(reuse)), ("stats", cmd_stats),
                 ("hu2022", lambda argv: cmd_hu2022(reuse)),
                 ("q1", cmd_q1), ("synthetic", cmd_synthetic),
                 ("synthetic --dtap-sweep", lambda argv: cmd_synthetic(["--dtap-sweep"])),
                 ("hashes", cmd_hashes)]
        for i, (lbl, fn) in enumerate(order, 1):
            print(f"\n{'=' * 10} [{i}/{len(order)}] {lbl} {'=' * 10}")
            rc = fn([])
            if rc:
                return rc
        print("\nAll Fuzzy_FS steps finished.")
        return 0

    if step not in _STEPS:
        print(f"Unknown step '{step}'. Choose from: {', '.join(_STEPS)}, all")
        return 2

    return _STEPS[step](rest)


if __name__ == "__main__":
    raise SystemExit(main())
