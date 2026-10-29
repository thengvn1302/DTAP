#!/usr/bin/env python3
"""Build a marked-up PDF comparing the submitted and the revised DTAP manuscripts.

Additions are highlighted in yellow, deletions are struck through in red, and every
change carries a margin tag [Cn] that points to the change inventory printed at the
front of the document.  The comparison is done block by block (paragraphs and whole
environments):

* identical blocks are copied unchanged;
* blocks that were only edited are compared word by word with latexdiff;
* blocks that were largely rewritten are shown as the old block (deleted) followed
  by the new block (added);
* blocks that moved to another place are shown once, at the new place, compared
  word by word with their old version; the old place keeps a short pointer.

Usage:  python build_diff.py            (writes build/ and DTAP_changes_marked.pdf)
        python build_diff.py --list     (prints the change list only)
"""
import argparse
import difflib
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
OLD_TEX = REPO / "DTAP_submission" / "main_document_old.tex"
NEW_TEX = REPO / "DTAP Finally" / "main_document.tex"
OLD_DIR = REPO / "DTAP_submission"
NEW_DIR = REPO / "DTAP Finally"
NOTES = ROOT / "change_notes.json"
REVIEW = ROOT / "review_comments.json"
BUILD = ROOT / "build"
OUT_PDF = ROOT / "DTAP_changes_marked.pdf"

# Word-level comparison is used when two aligned blocks are at least this similar;
# below it the old block is shown deleted and the new block added in full.
WORD_LEVEL_MIN = 0.70
# Minimum similarity for two blocks to be aligned at all.
ALIGN_MIN = 0.35
# Minimum similarity for a deleted and an added block to count as a move.
MOVE_MIN = 0.55

HEADING_RE = re.compile(r"^\\(section|subsection|subsubsection|paragraph)\*?[\[{]")
BEGIN_RE = re.compile(r"\\begin\{([^}]+)\}")
END_RE = re.compile(r"\\end\{([^}]+)\}")
LABEL_RE = re.compile(r"\\label\{([^}]*)\}")
REF_RE = re.compile(r"\\(ref|eqref|pageref)\{([^}]*)\}")
BIBITEM_RE = re.compile(r"^\\bibitem(\[[^\]]*\])?\{([^}]*)\}")
THEOREM_ENVS = ("theorem", "lemma", "corollary", "proposition", "definition",
                "example", "assumption", "remark", "notation")


# --------------------------------------------------------------------------- parsing
def split_document(text):
    """Return (preamble, body, bibliography, tail) of a LaTeX source."""
    pre, rest = text.split("\\begin{document}", 1)
    body, _ = rest.rsplit("\\end{document}", 1)
    m = re.search(r"\\begin\{thebibliography\}\{[^}]*\}(.*?)\\end\{thebibliography\}", body, re.S)
    bib = m.group(1)
    head, tail = body[:m.start()], body[m.end():]
    return pre, head, bib, tail


def env_depth_change(line):
    """Change in environment depth plus brace depth caused by one source line."""
    line = re.sub(r"(?<!\\)%.*", "", line)
    opens = [e for e in BEGIN_RE.findall(line) if e != "document"]
    closes = [e for e in END_RE.findall(line) if e != "document"]
    plain = re.sub(r"\\[{}]", "", line)
    return len(opens) - len(closes) + plain.count("{") - plain.count("}")


def split_blocks(text):
    """Split a body into blocks: paragraphs, headings and balanced environments."""
    blocks, cur, depth = [], [], 0
    for line in text.split("\n"):
        stripped = line.strip()
        starts_float = bool(re.match(
            r"(\{\\[a-z]+\s*)?\\begin\{(table|figure|longtable|abstract|keywords|amscode|algorithm)\}",
            stripped))
        if depth == 0 and (HEADING_RE.match(stripped) or starts_float) and cur:
            blocks.append("\n".join(cur))
            cur = []
        if depth == 0 and stripped == "":
            if cur:
                blocks.append("\n".join(cur))
                cur = []
            continue
        cur.append(line)
        depth += env_depth_change(line)
        if depth < 0:
            depth = 0
        if depth == 0 and re.search(r"\\end\{(table|figure)\}\s*$", stripped):
            # every float is a block of its own
            blocks.append("\n".join(cur))
            cur = []
            continue
        if depth == 0 and HEADING_RE.match(stripped) and stripped.endswith("}") \
                and line == cur[0] and len(cur) == 1 and "\\label" in stripped:
            # a heading with its label on one line is a block of its own
            blocks.append("\n".join(cur))
            cur = []
    if cur:
        blocks.append("\n".join(cur))
    return [b for b in blocks if b.strip()]


def tokens(block):
    return re.findall(r"\\[A-Za-z]+|[A-Za-z0-9]+|[^\sA-Za-z0-9]", block)


def norm(block):
    return " ".join(block.split())


def similarity(a, b):
    ha, hb = heading_of(a), heading_of(b)
    if ha or hb:
        # headings are compared by their titles only; a heading never matches a paragraph
        if not (ha and hb) or ha[0] != hb[0]:
            return 0.0
        a, b = (re.sub(r"\\textsc|[{}]", "", h[1]).lower() for h in (ha, hb))
    ta, tb = tokens(a), tokens(b)
    if not ta or not tb:
        return 0.0
    sm = difflib.SequenceMatcher(None, ta, tb, autojunk=False)
    if sm.real_quick_ratio() < ALIGN_MIN or sm.quick_ratio() < ALIGN_MIN:
        return sm.quick_ratio() * 0.5
    return sm.ratio()


# --------------------------------------------------------------------------- alignment
def align(old, new):
    """Monotone alignment of block lists maximising total similarity.

    Returns a list of (i, j) with i or j possibly None.
    """
    n, m = len(old), len(new)
    exact = {}
    for j, b in enumerate(new):
        exact.setdefault(norm(b), []).append(j)
    sim = {}

    def s(i, j):
        key = (i, j)
        if key not in sim:
            sim[key] = 1.0 if norm(old[i]) == norm(new[j]) else similarity(old[i], new[j])
        return sim[key]

    # anchor on identical blocks first (unique on both sides), then align gaps by DP
    anchors = []
    sm = difflib.SequenceMatcher(None, [norm(b) for b in old], [norm(b) for b in new],
                                 autojunk=False)
    for blk in sm.get_matching_blocks():
        for k in range(blk.size):
            anchors.append((blk.a + k, blk.b + k))
    pairs = []
    prev_i, prev_j = 0, 0
    for (ai, aj) in anchors + [(n, m)]:
        pairs.extend(dp_align(range(prev_i, ai), range(prev_j, aj), s))
        if ai < n:
            pairs.append((ai, aj))
        prev_i, prev_j = ai + 1, aj + 1
    return pairs


def dp_align(irange, jrange, s):
    I, J = list(irange), list(jrange)
    if not I:
        return [(None, j) for j in J]
    if not J:
        return [(i, None) for i in I]
    n, m = len(I), len(J)
    best = [[0.0] * (m + 1) for _ in range(n + 1)]
    move = [[None] * (m + 1) for _ in range(n + 1)]
    for a in range(n + 1):
        for b in range(m + 1):
            if a == 0 and b == 0:
                continue
            cands = []
            if a > 0:
                cands.append((best[a - 1][b], "del"))
            if b > 0:
                cands.append((best[a][b - 1], "add"))
            if a > 0 and b > 0:
                v = s(I[a - 1], J[b - 1])
                if v >= ALIGN_MIN:
                    cands.append((best[a - 1][b - 1] + v, "match"))
            best[a][b], move[a][b] = max(cands, key=lambda t: t[0])
    out, a, b = [], n, m
    while a or b:
        mv = move[a][b]
        if mv == "match":
            out.append((I[a - 1], J[b - 1]))
            a, b = a - 1, b - 1
        elif mv == "del":
            out.append((I[a - 1], None))
            a -= 1
        else:
            out.append((None, J[b - 1]))
            b -= 1
    return out[::-1]


FLOAT_RE = re.compile(r"\\begin\{(table|figure|longtable)\}")


def float_labels(block):
    if not FLOAT_RE.search(block):
        return set()
    return set(LABEL_RE.findall(block))


def detect_moves(pairs, old, new):
    """Pair unmatched deleted and added blocks that are near copies of each other.

    Floats carrying the same label are always paired, so that an old table is shown
    next to its new version even when its layout changed completely.
    """
    dels = [i for i, j in pairs if j is None]
    adds = [j for i, j in pairs if i is None]
    cand = []
    for i in dels:
        for j in adds:
            if float_labels(old[i]) & float_labels(new[j]):
                cand.append((2.0, i, j))
                continue
            v = similarity(old[i], new[j])
            short = min(len(tokens(old[i])), len(tokens(new[j]))) < 25
            if v >= (0.85 if short else MOVE_MIN):
                cand.append((v, i, j))
    cand.sort(reverse=True)
    moved_old, moved_new = {}, {}
    for v, i, j in cand:
        if i in moved_old or j in moved_new:
            continue
        moved_old[i], moved_new[j] = j, i
    return moved_old, moved_new


# --------------------------------------------------------------------------- latex helpers
def old_ref_rewrite(text, new_labels):
    """Point references to labels that exist only in the old version at old:<label>."""
    def repl(m):
        keys = [k.strip() for k in m.group(2).split(",")]
        keys = [k if k in new_labels else "old:" + k for k in keys]
        return "\\%s{%s}" % (m.group(1), ",".join(keys))
    return REF_RE.sub(repl, text)


def neutralize_old(text, old_numbers):
    """Make an old block safe to typeset inside the new document as deleted text."""
    text = text.replace("\\appendix", "")
    # numbered headings become unnumbered red headings carrying the old number
    def head(m):
        level, title, rest = m.group(1), m.group(2), m.group(3)
        lab = LABEL_RE.search(rest or "")
        num = old_numbers.get(lab.group(1), "") if lab else ""
        return "\\DIFoldheading{%s}{%s}{%s}" % (level, num, title)
    text = re.sub(r"\\(section|subsection|subsubsection)\*?\{((?:[^{}]|\{[^{}]*\})*)\}((?:\\label\{[^}]*\})?)",
                  head, text)
    # (captions and theorem-like environments are converted by the renderer, which
    #  knows their old numbers)
    # numbered displays become unnumbered
    for env in ("equation", "align", "gather", "multline"):
        text = text.replace("\\begin{%s}" % env, "\\begin{%s*}" % env)
        text = text.replace("\\end{%s}" % env, "\\end{%s*}" % env)
    text = text.replace("\\begin{proof}", "\\DIFoldproof").replace("\\end{proof}", "\\DIFoldproofend")
    # labels in deleted text would clash with the new ones
    text = LABEL_RE.sub("", text)
    # longtables (appendix) become plain tabulars inside a minipage
    text = re.sub(r"\\begin\{longtable\}", r"\\begin{DIFoldlongtable}", text)
    text = re.sub(r"\\end\{longtable\}", r"\\end{DIFoldlongtable}", text)
    # footnotes in deleted text: keep text, drop the counter
    text = text.replace("\\footnote{", "\\DIFoldfootnote{")
    return text


def run_latexdiff(old_frag, new_frag, work):
    work.mkdir(parents=True, exist_ok=True)
    (work / "a.tex").write_text(old_frag + "\n", encoding="utf-8")
    (work / "b.tex").write_text(new_frag + "\n", encoding="utf-8")
    res = subprocess.run(
        ["latexdiff", "--math-markup=whole", "--graphics-markup=none", "--floattype=FLOATSAFE",
         "--config", "MINWORDSBLOCK=2",
         str(work / "a.tex"), str(work / "b.tex")],
        capture_output=True, text=True, encoding="utf-8")
    if res.returncode != 0:
        raise RuntimeError(res.stderr)
    out = res.stdout
    # latexdiff prints a header comment and, for fragments, no preamble
    out = "\n".join(l for l in out.split("\n") if not l.startswith("%DIF LATEXDIFF"))
    return out.strip("\n")


# --------------------------------------------------------------------------- main
def heading_of(block):
    m = re.match(r"\\(section|subsection|subsubsection)\*?\{((?:[^{}]|\{[^{}]*\})*)\}", block.strip())
    return (m.group(1), m.group(2)) if m else None


def snippet(block, n=110):
    t = re.sub(r"\s+", " ", block).strip()
    return t[:n]


def build_changes(old_body, new_body):
    old, new = split_blocks(old_body), split_blocks(new_body)
    pairs = align(old, new)
    moved_old, moved_new = detect_moves(pairs, old, new)
    # walk in order; group consecutive pure deletions / pure additions
    segs = []
    for i, j in pairs:
        if i is not None and j is not None:
            kind = "same" if norm(old[i]) == norm(new[j]) else (
                "edit" if similarity(old[i], new[j]) >= WORD_LEVEL_MIN else "rewrite")
        elif j is None:
            kind = "movedfrom" if i in moved_old else "del"
        else:
            kind = "movedto" if j in moved_new else "add"
            if kind == "movedto":
                i = moved_new[j]
        segs.append({"kind": kind, "i": i, "j": j})
    return old, new, segs


def group_changes(segs, old, new):
    """Assign change ids.

    Every changed block gets its own id, except that a deleted (added) heading and
    the deleted (added) blocks that follow it in the same section share one id, so
    that a removed or new subsection is a single entry in the inventory.
    """
    cid, run = 0, None          # run = ("del"|"add", section) while a heading run is open
    for s in segs:
        k = s["kind"]
        if k == "same":
            run = None
            continue
        if k == "movedfrom":    # shares the id of its new location, assigned below
            continue
        blk = old[s["i"]] if k == "del" else (new[s["j"]] if k == "add" else None)
        if k in ("del", "add") and run is not None and run[0] == k and heading_of(blk) is None:
            s["cid"] = cid
            continue
        cid += 1
        s["cid"] = cid
        run = (k, cid) if k in ("del", "add") and heading_of(blk) is not None else None
    to_cid = {s["i"]: s["cid"] for s in segs if s["kind"] == "movedto"}
    for s in segs:
        if s["kind"] == "movedfrom":
            s["cid"] = to_cid[s["i"]]
    return cid


def section_context(old, new, segs):
    """Attach the enclosing (new or old) section title to every segment."""
    cur_new, cur_old = "", ""
    for s in segs:
        if s["j"] is not None and s["kind"] not in ("movedfrom",):
            h = heading_of(new[s["j"]])
            if h:
                cur_new = h[1]
        if s["i"] is not None:
            h = heading_of(old[s["i"]])
            if h:
                cur_old = h[1]
        s["sec_new"], s["sec_old"] = cur_new, cur_old


def check_coverage(old, new, segs, old_src, new_src):
    """Every old and every new block must be shown exactly once, and the block split
    must not lose any text; otherwise a change could silently go missing."""
    squash = lambda t: re.sub(r"\s+", "", t)
    assert squash("".join(old)) == squash(old_src), "old text lost while splitting"
    assert squash("".join(new)) == squash(new_src), "new text lost while splitting"
    oi = sorted(s["i"] for s in segs if s["i"] is not None and s["kind"] != "movedto")
    nj = sorted(s["j"] for s in segs if s["j"] is not None and s["kind"] != "movedfrom")
    assert oi == list(range(len(old))), "an old block is missing or duplicated"
    assert nj == list(range(len(new))), "a new block is missing or duplicated"
    print("coverage: %d old blocks and %d new blocks, each shown exactly once" % (len(old), len(new)),
          file=sys.stderr)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    old_text = OLD_TEX.read_text(encoding="utf-8")
    new_text = NEW_TEX.read_text(encoding="utf-8")
    old_pre, old_body, old_bib, old_tail = split_document(old_text)
    new_pre, new_body, new_bib, new_tail = split_document(new_text)
    old, new, segs = build_changes(old_body + "\n\n" + old_tail, new_body + "\n\n" + new_tail)
    ncid = group_changes(segs, old, new)
    section_context(old, new, segs)
    check_coverage(old, new, segs, old_body + old_tail, new_body + new_tail)

    if args.list or args.json:
        rows = {}
        for s in segs:
            if s["kind"] == "same":
                continue
            r = rows.setdefault(s["cid"], {"cid": s["cid"], "kinds": [], "old": [], "new": [],
                                            "sec_new": s["sec_new"], "sec_old": s["sec_old"]})
            r["kinds"].append(s["kind"])
            if s["i"] is not None:
                r["old"].append(snippet(old[s["i"]]))
            if s["j"] is not None and s["kind"] != "movedfrom":
                r["new"].append(snippet(new[s["j"]]))
        if args.json:
            print(json.dumps(list(rows.values()), ensure_ascii=False, indent=1))
        else:
            for r in sorted(rows.values(), key=lambda r: r["cid"]):
                print("C%d %s | new§ %s | old§ %s" % (r["cid"], ",".join(r["kinds"]),
                                                     r["sec_new"][:30], r["sec_old"][:30]))
                for o in r["old"][:2]:
                    print("   - " + o)
                for n_ in r["new"][:2]:
                    print("   + " + n_)
        print("changes:", ncid, file=sys.stderr)
        return

    from assemble import assemble  # noqa: E402  (second stage, kept separate for clarity)
    assemble(old_text, new_text, old, new, segs, ncid,
             (old_pre, old_bib), (new_pre, new_bib))


if __name__ == "__main__":
    main()
