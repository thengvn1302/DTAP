"""SHA-256 hashes of every code, data and result file of the package (`run_all.py hashes`).

SHA256SUMS uses the `sha256sum` format ("<hash>  <relative/path>"), so it can also be checked with
`sha256sum -c SHA256SUMS` on Linux or Git Bash.
"""
import hashlib
import os

from src.common.consts import PROJECT_DIR

SUMS = "SHA256SUMS"
SKIP_DIRS = {"__pycache__", ".git"}


def _files():
    root = str(PROJECT_DIR)
    for base, dirs, files in os.walk(root):
        dirs[:] = sorted(d for d in dirs if d not in SKIP_DIRS)
        for name in sorted(files):
            if name == SUMS or name.endswith(".pyc"):
                continue
            path = os.path.join(base, name)
            yield os.path.relpath(path, root).replace(os.sep, "/"), path


def _sha256(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def write_sums() -> int:
    lines = [f"{_sha256(path)}  {rel}" for rel, path in _files()]
    with open(os.path.join(str(PROJECT_DIR), SUMS), "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(lines) + "\n")
    print(f"  Wrote {SUMS}: {len(lines)} files")
    return 0


def check_sums() -> int:
    path = os.path.join(str(PROJECT_DIR), SUMS)
    if not os.path.isfile(path):
        print(f"  {SUMS} not found")
        return 1
    listed, bad = {}, []
    with open(path, encoding="utf-8") as f:
        for line in f:
            if line.strip():
                digest, rel = line.rstrip("\n").split("  ", 1)
                listed[rel] = digest
    present = dict(_files())
    for rel, digest in listed.items():
        if rel not in present:
            bad.append(f"MISSING  {rel}")
        elif _sha256(present[rel]) != digest:
            bad.append(f"CHANGED  {rel}")
    bad += [f"UNLISTED {rel}" for rel in present if rel not in listed]
    for b in bad:
        print("  " + b)
    print(f"  {SUMS}: {len(listed)} listed, {len(bad)} problems")
    return 1 if bad else 0
