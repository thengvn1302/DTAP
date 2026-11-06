#!/usr/bin/env python3
"""Split DTAP Finally v2/main_document.tex into numbered sentences for the sentence review.

Writes sentences.json: [{id, sec, text, words}]. Tables and the bibliography are skipped
(captions are kept); displayed formulas are shown as [công thức (n)]."""
import json, re, subprocess, shutil, tempfile
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
TEX = ROOT / "DTAP Finally v2" / "main_document.tex"

def aux_labels():
    d = Path(tempfile.mkdtemp())
    shutil.copy(TEX, d / "m.tex"); shutil.copy(TEX.parent / "interact.cls", d)
    for _ in range(2):
        subprocess.run(["pdflatex", "-interaction=nonstopmode", "m.tex"], cwd=d, capture_output=True)
    t = (d / "m.aux").read_text(errors="replace")
    L = {m.group(1): m.group(2) for m in re.finditer(r"\\newlabel\{([^}]*)\}\{\{([^}]*)\}", t)}
    C = {m.group(1): m.group(2) for m in re.finditer(r"\\bibcite\{([^}]*)\}\{\{([^}]*)\}", t)}
    return L, C

L, C = aux_labels()

def brace(s, i):
    d = 0
    for j in range(i, len(s)):
        if s[j] == "{": d += 1
        elif s[j] == "}":
            d -= 1
            if d == 0: return j
    raise ValueError

def sub_cmd(s, cmd, fn, nargs=1):
    out, i, pat = "", 0, "\\" + cmd
    while True:
        k = s.find(pat, i)
        if k < 0: return out + s[i:]
        e = k + len(pat)
        if e < len(s) and s[e].isalpha():
            out += s[i:e]; i = e; continue
        args, p, ok = [], e, True
        for _ in range(nargs):
            while p < len(s) and s[p] == " ": p += 1
            if p >= len(s) or s[p] != "{": ok = False; break
            q = brace(s, p); args.append(s[p + 1:q]); p = q + 1
        if not ok:
            out += s[i:e]; i = e; continue
        out += s[i:k] + fn(*args); i = p

def readable(s):
    s = sub_cmd(s, "eqref", lambda a: "(" + L.get(a, "?") + ")")
    s = sub_cmd(s, "ref", lambda a: L.get(a, "?"))
    for c in ("citep", "citet", "cite"):
        s = sub_cmd(s, c, lambda a: "[" + ", ".join(C.get(x.strip(), "?") for x in a.split(",")) + "]")
    s = re.sub(r"\\label\{[^}]*\}", "", s)
    s = s.replace("\\dtap{}", "DTAP").replace("\\dtap", "DTAP")
    s = re.sub(r"\\(smallskip|medskip|noindent)(?![a-zA-Z])\s*", " ", s)
    s = sub_cmd(s, "emph", lambda a: a); s = sub_cmd(s, "textup", lambda a: a)
    s = sub_cmd(s, "textbf", lambda a: a); s = sub_cmd(s, "texttt", lambda a: a)
    s = s.replace("~", " ").replace('H\\"older', "Hölder").replace("Fej\\'er", "Fejér").replace("L\\'opez", "López")
    s = re.sub(r"\\(smallskip|medskip|noindent|small|par)\b\s*", "", s)
    return re.sub(r"\s+", " ", s).strip()

src = TEX.read_text(encoding="utf-8")
body = src[src.index("\\begin{abstract}"):src.index("\\begin{thebibliography}")]
# displays -> placeholders carrying the equation number
def disp(m):
    lab = re.findall(r"\\label\{([^}]*)\}", m.group(0))
    nums = [L.get(x, "?") for x in lab]
    return " [công thức" + (" (" + ", ".join(nums) + ")" if nums else "") + "] "
body = re.sub(r"\\begin\{(equation|align|aligned)\*?\}.*?\\end\{\1\*?\}", disp, body, flags=re.S)
body = re.sub(r"\\\[.*?\\\]", " [công thức] ", body, flags=re.S)
# tables: keep caption only
def tab(m):
    cap = re.search(r"\\caption\{", m.group(0))
    if not cap: return "\n\n"
    i = cap.end() - 1; j = brace(m.group(0), i)
    return "\n\n[Chú thích bảng] " + m.group(0)[i + 1:j] + "\n\n"
body = re.sub(r"\\begin\{table\}.*?\\end\{table\}", tab, body, flags=re.S)
body = re.sub(r"(?<!\\)%[^\n]*", "", body)

units, sec, after_caption = [], "Abstract", False
ABBR = r"(?<!et al\.)(?<!e\.g\.)(?<!i\.e\.)(?<!\bvs\.)(?<!Sec\.)(?<!resp\.)"
for block in re.split(r"\n\s*\n", body):
    for piece in re.split(r"(\\(?:sub)*section\*?\{[^}]*\}|\\paragraph\*?\{[^}]*\}|\\item(?:\[[^\]]*\])?|\\algstep\{[^}]*\}|\\caption\{)", block):
        m = re.match(r"\\((?:sub)*section)\*?\{([^}]*)\}", piece)
        if m:
            sec = readable(m.group(2)); units.append(("Tiêu đề", sec)); continue
        m = re.match(r"\\paragraph\*?\{([^}]*)\}", piece)
        if m: units.append(("Tiêu đề đoạn", readable(m.group(1)))); continue
        m = re.match(r"\\algstep\{([^}]*)\}", piece)
        if m: units.append(("Thuật toán", readable(m.group(1)))); continue
        if piece.startswith("\\item"): continue
        if piece == "\\caption{":
            after_caption = True; continue
        if after_caption:
            depth = 0
            for k, ch in enumerate(piece):
                depth += (ch == "{") - (ch == "}")
                if depth < 0:
                    piece = piece[:k] + " " + piece[k + 1:]
                    break
            after_caption = False
        t = re.sub(r"\\(begin|end)\{[^}]*\}(\[[^\]]*\])?(\{[^}]*\})?", " ", piece)
        t = readable(t)
        if not t or re.fullmatch(r"[\s\[\]a-zA-Zàáâãèéêìíòóôõùúăđĩũơưạ-ỹ\d(),]*công thức[^.]*", t) and len(t) < 30:
            if t: units.append((sec, t))
            continue
        t = t.replace("i.e.\\ ", "i.e. ").replace("e.g.\\ ", "e.g. ").replace("}\\noindent", " ").replace("\\\\", " ")
        for s in re.split(ABBR + r"(?<=[.?!])\s+(?=[A-Z\[(\$])|(?<=thức\])\s+(?=[A-Z])|(?<=\)\])\s+(?=[A-Z])", t):
            s = s.strip()
            if len(s) > 2: units.append((sec, s))

out = []
for k, (where, s) in enumerate(units, 1):
    n = len(re.sub(r"\$[^$]*\$", "X", s).split())
    out.append({"id": k, "sec": where, "text": s, "words": n})
json.dump(out, open(Path(__file__).with_name("sentences.json"), "w"), ensure_ascii=False, indent=1)
print(len(out), "units;", sum(1 for x in out if x["words"] > 30), "over 30 words")
