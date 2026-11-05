#!/usr/bin/env python3
"""Typeset v1_v2_changes.md as a side-by-side PDF: "Before" on the left, "After" on the right.

Within each item, a sentence and its revised form sit on the same row (correspondence set by
hand in MANUAL where sentences were split, merged or reordered); a deleted or added sentence
has an empty cell on the other side. Each English sentence is followed by its translation.

Usage:  python side_by_side.py      (writes v1_v2_side_by_side.pdf; needs lualatex)
"""
import re
import shutil
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "v1_v2_changes.md"
WORK = ROOT / "build_side_by_side"
OUT = ROOT / "v1_v2_side_by_side.pdf"


# ----------------------------------------------------------------------------- parse
def parse(md):
    """Return a list of blocks: ('section', title) | ('item', title, old, new, notes) |
    ('appendix', rows)."""
    lines = md.split("\n")
    blocks, cur, side, i = [], None, None, 0

    def flush():
        nonlocal cur
        if cur:
            blocks.append(("item", cur["title"], cur["old"], cur["new"], cur["notes"]))
        cur = None

    while i < len(lines):
        l = lines[i]
        if l.startswith("## Phụ lục"):
            flush()
            rows = []
            for r in lines[i + 1:]:
                if r.startswith("|") and not r.startswith("|---") and "Vị trí" not in r:
                    rows.append([c.strip() for c in r.strip().strip("|").split("|")])
            blocks.append(("appendix", l[3:].strip(), rows))
            break
        if l.startswith("## ") and not l.startswith("## F."):
            flush()
            blocks.append(("section", l[3:].strip()))
        elif l.startswith("### ") or l.startswith("## F."):
            flush()
            if l.startswith("## F."):
                blocks.append(("section", l[3:].strip()))
            cur = {"title": l.lstrip("#").strip(), "old": [], "new": [], "notes": []}
            side = None
        elif cur is not None:
            s = l.strip()
            if s.startswith("**Trước**"):
                side = "old"
            elif s.startswith("**Sau**"):
                side = "new"
            elif s.startswith("- **Trước:**") or s.startswith("- **Sau:**"):
                side = "old" if "Trước" in s[:12] else "new"
                body = s.split(":**", 1)[1].strip()
                en, vi = body, ""
                if i + 1 < len(lines) and lines[i + 1].strip().startswith("→"):
                    vi = lines[i + 1].strip()[1:].strip()
                    i += 1
                elif " → " in body:                     # inline translation (keywords)
                    en, vi = body.split(" → ", 1)
                if en.startswith("*(") or re.match(r"\((Ba câu|Câu về)", en):
                    cur["notes"].append(("Trước: " if side == "old" else "Sau: ") + en.strip("*"))
                else:
                    cur[side].append([en, vi])
            elif re.match(r"\d+\. ", s) and side:
                en = re.sub(r"^\d+\. ", "", s)
                vi = ""
                if i + 1 < len(lines) and lines[i + 1].strip().startswith("→"):
                    vi = lines[i + 1].strip()[1:].strip()
                    i += 1
                if en.startswith("*(") or re.match(r"\((Ba câu|Câu về)", en):
                    cur["notes"].append(("Trước: " if side == "old" else "Sau: ") + en.strip("*"))
                else:
                    cur[side].append([en, vi])
            elif s.startswith("*(") or s.startswith("*Trước:") or s.startswith("*(Ghi chú"):
                cur["notes"].append(s.strip("*"))
        i += 1
    flush()
    return blocks


# ----------------------------------------------------------------------------- align
# Correspondence of sentences, set by hand for the items whose sentences were split, merged or
# reordered: item number -> list of (old sentence numbers, new sentence numbers), in the order of
# the new text. Items not listed with equally many old and new sentences are paired in order.
MANUAL = {
    2: [([1], [1]), ([2], [2]), ([3], [3]), ([], [4]), ([4, 5], [5]), ([6], [6])],
    4: [([1], []), ([2], [1]), ([3], [2]), ([4, 5], [3])],
    6: [([1], [1, 2]), ([2], [3]), ([3, 4, 5, 6], [4]), ([7, 8, 9], [5])],
    7: [([1, 2], [1]), ([3, 4], [2]), ([5], [])],
    8: [([1], [1]), ([2, 3], [2]), ([4, 5], [3])],
    10: [([1], [1]), ([2], [])],
    15: [([1, 2], [1]), ([3], [2])],
    19: [([1, 3], [1]), ([2], [2])],
    22: [([], [1]), ([1], [2, 3]), ([2], [4]), ([3], [5, 6])],
    26: [([1], [1]), ([2], [2]), ([3], [3, 4, 5, 6]), ([4], [7])],
    30: [([1], [1]), ([2], [])],
    38: [([1, 2], [1]), ([3, 4], [2]), ([5, 18], [3]), ([6, 7, 8, 9], [4]), ([15, 16], [5]),
         ([11], [6]), ([12, 13, 14], [7]), ([10, 17], [8])],
    40: [([1, 2], [1])],
    42: [([1], [1, 2])],
    43: [([3, 4], [1]), ([1, 2], [2]), ([5], [])],
    46: [([1], [1, 2])],
    48: [([1], [1]), ([2], [2, 3]), ([3], [4]), ([4], [5])],
    49: [([1], [1]), ([2, 3], [2]), ([4], [3]), ([5], [])],
    57: [([1, 2], [1]), ([3, 4], [2]), ([6, 7], [3]), ([8], [4]), ([9, 10], [5]), ([5], [])],
}


def align(old, new, item=None):
    """Rows (left, right) for one item. A side is (number, [en, vi]), ('ref', text) or None."""
    if item in MANUAL:
        groups = MANUAL[item]
        used_o = sorted(i for g in groups for i in g[0])
        used_n = sorted(j for g in groups for j in g[1])
        assert used_o == list(range(1, len(old) + 1)), (item, used_o, len(old))
        assert used_n == list(range(1, len(new) + 1)), (item, used_n, len(new))
    elif len(old) == len(new) or not old or not new:
        k = max(len(old), len(new))
        groups = [([i + 1] if i < len(old) else [], [i + 1] if i < len(new) else []) for i in range(k)]
    else:
        raise SystemExit(f"item {item}: {len(old)} old vs {len(new)} new sentences; add it to MANUAL")
    rows = []
    for olds, news in groups:
        for k in range(max(len(olds), len(news))):
            if k < len(olds):
                left = (olds[k], old[olds[k] - 1])
            elif olds:
                left = ("ref", f"(cùng nhóm với câu [{olds[0]}] ở trên)")
            else:
                left = None
            if k < len(news):
                right = (news[k], new[news[k] - 1])
            elif news:
                right = ("ref", f"(cùng nhóm với câu [{news[0]}] ở trên)")
            else:
                right = None
            rows.append((left, right))
    return rows


# ----------------------------------------------------------------------------- latex
def tex(s):
    """Markdown fragment with $math$ -> LaTeX."""
    parts = re.split(r"(\$[^$]*\$)", s)
    out = []
    for p in parts:
        if p.startswith("$") and p.endswith("$") and len(p) > 1:
            out.append(p)
            continue
        p = p.replace("\\", "\\textbackslash{}")
        for a, b in (("&", "\\&"), ("%", "\\%"), ("#", "\\#"), ("_", "\\_"), ("{", "\\{"),
                     ("}", "\\}"), ("~", "\\textasciitilde{}")):
            p = p.replace(a, b)
        p = p.replace("\\textbackslash\\{\\}", "\\textbackslash{}")
        p = re.sub(r"\*\*(.+?)\*\*", r"\\textbf{\1}", p)
        p = re.sub(r"\*(.+?)\*", r"\\emph{\1}", p)
        p = re.sub(r"`([^`]*)`", r"\\texttt{\1}", p)
        out.append(p)
    return "".join(out)


def cell(x):
    if x is None:
        return "\\emptycell"
    if x[0] == "ref":
        return "{\\color{gray}\\footnotesize " + x[1] + "}"
    num, (en, vi) = x
    if en.strip().startswith("*(xóa"):
        return "\\emptycell{}\\par\\vi{" + tex(en.strip("*")) + "}"
    body = "\\num{" + str(num) + "}\\en{" + tex(en) + "}"
    if vi:
        body += "\\par\\vi{" + tex(vi) + "}"
    return body


HEAD = r"""\documentclass[10pt]{article}
\usepackage[a4paper,landscape,margin=1.4cm]{geometry}
\usepackage{fontspec}
\setmainfont{Latin Modern Roman}
\usepackage{amsmath,amssymb}
\usepackage{xcolor,colortbl}
\usepackage{longtable,array,booktabs}
\usepackage{fancyhdr}
\pagestyle{fancy}\fancyhf{}\renewcommand{\headrulewidth}{0pt}
\fancyfoot[C]{\thepage}
\fancyfoot[R]{\footnotesize DTAP Finally $\to$ DTAP Finally v2}
\setlength{\parindent}{0pt}
\definecolor{oldbg}{HTML}{FDF1F0}
\definecolor{newbg}{HTML}{EEF7EE}
\definecolor{vicol}{HTML}{3A4A6B}
\definecolor{itembg}{HTML}{E6E9EF}
\newcommand{\en}[1]{#1}
\newcommand{\vi}[1]{{\color{vicol}\itshape #1}}
\newcommand{\num}[1]{{\color{gray}\footnotesize[#1]}\ }
\newcommand{\emptycell}{{\color{gray}---}}
\setlength{\tabcolsep}{6pt}
\renewcommand{\arraystretch}{1.08}
\begin{document}
\begin{center}
{\Large\bfseries Đối chiếu trước và sau chỉnh sửa}\\[3pt]
\texttt{DTAP Finally/main\_document.tex} (Trước) \quad$\to$\quad \texttt{DTAP Finally v2/main\_document.tex} (Sau)
\end{center}
\smallskip
{\small Mỗi hàng đặt câu cũ cạnh câu mới tương ứng; số trong ngoặc vuông là thứ tự câu trong đoạn (để biết khi câu bị đảo chỗ). Ô ``---'' nghĩa là câu bị xóa (bên Sau) hoặc câu mới thêm (bên Trước); ``(cùng nhóm với câu [k] ở trên)'' nghĩa là nhiều câu ở một bên ứng với một câu ở bên kia (câu được gộp hoặc tách).
Dưới mỗi câu tiếng Anh là bản dịch tiếng Việt (chữ nghiêng, màu xanh). Thay đổi chỉ về ký hiệu ghi ở Phụ lục cuối tài liệu.
Số mục, công thức, tài liệu tham khảo theo bản PDF.}
\medskip

\begin{longtable}{@{}>{\columncolor{oldbg}\raggedright\arraybackslash}p{0.485\linewidth}
                  @{\hspace{0.015\linewidth}}
                  >{\columncolor{newbg}\raggedright\arraybackslash}p{0.485\linewidth}@{}}
\toprule
\textbf{Trước (DTAP Finally)} & \textbf{Sau (DTAP Finally v2)}\\
\midrule
\endhead
\bottomrule
\endfoot
"""


def build(blocks):
    out = [HEAD]
    for b in blocks:
        if b[0] == "section":
            out.append("\\multicolumn{2}{@{}l@{}}{\\rule{0pt}{14pt}\\large\\bfseries " + tex(b[1]) + "}\\\\*[2pt]\n")
        elif b[0] == "item":
            _, title, old, new, notes = b
            out.append("\\multicolumn{2}{@{}>{\\columncolor{itembg}}l@{}}{\\bfseries " + tex(title)
                       + "}\\\\*\n")
            m = re.match(r"(\d+)\.", title)
            num = int(m.group(1)) if m else 57          # the Conclusion is item 57
            for o, n in align(old, new, num):
                out.append(cell(o) + " & " + cell(n) + "\\\\\n")
            for note in notes:
                out.append("\\multicolumn{2}{@{}p{0.985\\linewidth}@{}}{\\footnotesize\\itshape "
                           + tex(note) + "}\\\\\n")
            out.append("\\addlinespace[4pt]\n")
        elif b[0] == "appendix":
            out.append("\\end{longtable}\n\n\\section*{" + tex(b[1]) + "}\n")
            out.append("\\begin{longtable}{@{}p{0.32\\linewidth}p{0.3\\linewidth}p{0.36\\linewidth}@{}}\n"
                       "\\toprule\\textbf{Vị trí} & \\textbf{Trước} & \\textbf{Sau}\\\\\\midrule\n\\endhead\n"
                       "\\bottomrule\n\\endfoot\n")
            for r in b[2]:
                out.append(" & ".join(tex(c) for c in r) + "\\\\\n")
            out.append("\\end{longtable}\n\\end{document}\n")
            return "".join(out)
    out.append("\\end{longtable}\n\\end{document}\n")
    return "".join(out)


def main():
    blocks = parse(SRC.read_text(encoding="utf-8"))
    n_items = sum(1 for b in blocks if b[0] == "item")
    n_old = sum(len(b[2]) for b in blocks if b[0] == "item")
    n_new = sum(len(b[3]) for b in blocks if b[0] == "item")
    print(f"items: {n_items}, before sentences: {n_old}, after sentences: {n_new}")
    missing = [(b[1], s[0][:50]) for b in blocks if b[0] == "item" for s in b[2] + b[3] if not s[1]]
    if missing:
        print("without translation:", missing)
    if WORK.exists():
        shutil.rmtree(WORK)
    WORK.mkdir()
    (WORK / "sbs.tex").write_text(build(blocks), encoding="utf-8")
    for _ in range(3):
        subprocess.run(["lualatex", "-interaction=nonstopmode", "sbs.tex"], cwd=WORK,
                       capture_output=True)
    log = (WORK / "sbs.log").read_text(encoding="utf-8", errors="replace")
    errs = [l for l in log.split("\n") if l.startswith("!")]
    print("LaTeX errors:", len(errs), errs[:5])
    miss = sorted(set(re.findall(r"Missing character: There is no (.) ", log)))
    print("missing glyphs:", miss)
    shutil.copy(WORK / "sbs.pdf", OUT)
    print("written", OUT.name)


if __name__ == "__main__":
    main()
