#!/usr/bin/env python3
"""Write a copy of the revised manuscript in which added or modified text is red.

The journal asks for the changes to be highlighted in the revised manuscript. This
script writes "DTAP Finally/main_document_colored.tex" and its PDF (with
DTAP_NEW_DIR="DTAP Finally v2": into that folder instead); the original
main_document.tex is not touched.

The comparison is by content, sentence by sentence, not character by character:

* changes of form only are ignored: \\textsc{dtap} versus DTAP, emphasis, delimiter
  sizes (\\Bigl, \\left), ``:='' versus ``='', spacing, punctuation, line breaks and
  alignment inside formulas, and the wording of cross-references (``Appendix A''
  versus ``Section 4.2.1'', \\citealt versus \\citet);
* a sentence, formula, table cell or heading that occurs in the submitted version,
  here or elsewhere (moved text), stays black;
* a sentence with a few changed words has only those words in red;
* a sentence of which half or more changed, or a new one, is red as a whole;
* formulas and headings whose content changed are red as a whole;
* table cells are compared with the same row of the old table (bold face and the
  layout ``a / b'' versus two columns are form only): a cell is red when its value
  changed, or when its row or column is new;
* deleted text does not appear, and the references are not coloured.

Checks: removing the colour gives back main_document.tex character by character, and
the coloured PDF has the same text and line positions as the clean one.

Usage:  python make_colored.py [--report]
"""
import argparse
import difflib
import re
import shutil
import subprocess
import sys

import build_diff as bd
from assemble import matching_brace

OUT_TEX = bd.NEW_DIR / "main_document_colored.tex"
OUT_PDF = bd.NEW_DIR / "DTAP_OMS_colored.pdf"
WORK = bd.ROOT / "build_colored"
RED_SWITCH = r"\color{red}"
OPEN_TEXT = r"\leavevmode\textcolor{red}{"   # in running text
OPEN_HEAD = r"\textcolor{red}{"               # in heading titles and inside formulas

WORD_LEVEL_MIN = 0.6     # a unit at least this similar to an old one gets word-level marks
WHOLE_UNIT_FRAC = 0.5    # ... unless this fraction of its words changed
GAP_MERGE = 3            # unchanged runs of at most this many words between changes turn red
GLOBAL_MIN_LEN = 6       # units shorter than this only match within the aligned old block

DISPLAY_ENVS = ("equation", "equation*", "align", "align*", "gather", "gather*", "multline",
                "multline*", "displaymath")
ALIGN_ENVS = ("align", "align*", "gather", "gather*", "multline", "multline*")
TEXT_CMDS = {"emph", "textbf", "textit", "textup", "text", "mbox", "texttt", "underline",
             "textsuperscript", "algstep", "footnote", "uline", "textsl", "textrm"}
HEAD_CMDS = {"section", "subsection", "subsubsection", "paragraph", "caption"}
REF_CMDS = {"ref", "eqref", "pageref", "autoref", "cref", "Cref"}
CITE_CMDS = {"cite", "citep", "citet", "citealt", "citealp", "citeauthor"}
NEUTRAL_CMDS = {"label", "setlength", "renewcommand", "newcommand", "vspace", "hspace",
                "centering", "small", "footnotesize", "scriptsize", "normalsize", "large",
                "noindent", "smallskip", "medskip", "bigskip", "par", "maketitle", "raggedright",
                "newline", "clearpage", "newpage", "toprule", "midrule", "bottomrule", "cmidrule",
                "hline", "leavevmode", "protect", "relax", "hfill", "vfill", "indent", "appendix",
                "selectfont", "fontsize", "urlstyle", "nopagebreak", "pagebreak", "ldots", "dots",
                "cdots", "quad", "qquad"}
MENTION_WORDS = {"section", "sections", "subsection", "table", "tables", "appendix", "lemma",
                 "lemmas", "remark", "remarks", "theorem", "corollary", "corollaries",
                 "proposition", "definition", "assumption", "example", "algorithm", "figure",
                 "fig", "eq", "eqs", "equation", "claim", "stage", "step", "sec", "secs"}
ABBREVIATIONS = {"e.g.", "i.e.", "al.", "cf.", "vs.", "resp.", "fig.", "eq.", "eqs.", "sec.",
                 "no.", "et."}
BARRIERS = {"par", "begin", "end", "row", "cell", "item", "display", "hopen", "hclose"}


# --------------------------------------------------------------------------- tokens
class Tok:
    __slots__ = ("kind", "a", "b", "norm", "partner", "name", "red")

    def __init__(self, kind, a, b, norm=None, name=None):
        self.kind, self.a, self.b, self.norm, self.name = kind, a, b, norm, name
        self.partner = None
        self.red = False


def norm_math(s):
    s = re.sub(r"\\label\{[^}]*\}|\\nonumber|\\notag", "", s)
    s = re.sub(r"\\begin\{(split|aligned|gathered)\}|\\end\{(split|aligned|gathered)\}", "", s)
    s = re.sub(r"\\(left|right|[bB]igg?[lr]?|middle)(?![a-zA-Z])", "", s)
    s = re.sub(r"\\(displaystyle|textstyle|quad|qquad)(?![a-zA-Z])|\\[,;:! ]|~|&|\\\\(\[[^\]]*\])?", "", s)
    s = re.sub(r"\\leq(?![a-zA-Z])", r"\\le", s)
    s = re.sub(r"\\geq(?![a-zA-Z])", r"\\ge", s)
    s = re.sub(r"\\[lc]?dots(?![a-zA-Z])", r"\\dots", s)
    s = re.sub(r"\\[td]frac(?![a-zA-Z])", r"\\frac", s)
    s = re.sub(r"\\textup|\\mathrm(?=\{)|\\mathbf|\\boldsymbol|\\bm(?![a-zA-Z])", "", s)
    s = s.replace(":=", "=").replace("{", "").replace("}", "")
    s = re.sub(r"\s+", "", s)
    return s.rstrip(".,;")


def stem(w):
    """A light stemmer, so that ``studied'' and ``study'', or a plural, count as the same."""
    for suf, rep in (("ies", "y"), ("ied", "y"), ("ing", ""), ("ed", ""), ("es", ""), ("s", "")):
        if len(w) > len(suf) + 3 and w.endswith(suf):
            return w[:-len(suf)] + rep
    return w


ALIASES = {"rbfsvm": "svm"}       # names that were only shortened


def norm_word(raw):
    w = raw.replace("\\'", "").replace('\\"', "").replace("\\`", "").replace("\\^", "")
    w = re.sub(r"[^0-9A-Za-z]", "", w).lower()
    w = ALIASES.get(w, w)
    return stem(w) if w else None


def skip_args(s, i, end):
    """Index after the optional *, [..] and {..} arguments that start at i."""
    if i < end and s[i] == "*":
        i += 1
    while i < end:
        if s[i] == "[":
            depth = 0
            for k in range(i, end):
                if s[k] == "[":
                    depth += 1
                elif s[k] == "]":
                    depth -= 1
                    if depth == 0:
                        break
            i = k + 1
        elif s[i] == "{":
            i = matching_brace(s, i) + 1
        else:
            break
    return i


def find_env_end(s, i, env):
    """Index after the \\end{env} that closes the environment opened before i."""
    depth = 1
    pat = re.compile(r"\\(begin|end)\{%s\}" % re.escape(env))
    for m in pat.finditer(s, i):
        depth += 1 if m.group(1) == "begin" else -1
        if depth == 0:
            return m.end()
    raise ValueError("unclosed " + env)


def tokenize(s, i=0, end=None, out=None):
    if end is None:
        end = len(s)
    if out is None:
        out = []
    while i < end:
        c = s[i]
        if c == "%":
            j = s.find("\n", i, end)
            j = end if j < 0 else j
            out.append(Tok("ws", i, j))
            i = j
        elif c.isspace():
            j = i
            while j < end and s[j].isspace():
                j += 1
            out.append(Tok("par" if s[i:j].count("\n") >= 2 else "ws", i, j))
            i = j
        elif c == "~":
            out.append(Tok("ws", i, i + 1))
            i += 1
        elif c == "$":
            j = i + 1
            while s[j] != "$" or s[j - 1] == "\\":
                j += 1
            out.append(Tok("math", i, j + 1, norm_math(s[i + 1:j])))
            i = j + 1
        elif c == "&":
            out.append(Tok("cell", i, i + 1))
            i += 1
        elif c == "{":
            k = matching_brace(s, i)
            o = Tok("open", i, i + 1)
            out.append(o)
            tokenize(s, i + 1, k, out)
            cl = Tok("close", k, k + 1)
            o.partner, cl.partner = cl, o
            out.append(cl)
            i = k + 1
        elif c == "\\":
            i = tokenize_command(s, i, end, out)
        else:
            j = i
            while j < end:
                ch = s[j]
                if ch.isspace() or ch in "{}$&%~":
                    break
                if ch == "\\":
                    if j + 1 < end and s[j + 1] in "'\"`^=.%&_#$":
                        if s[j + 1] in "'\"`^=." and j + 2 < end and s[j + 2] == "{":
                            j = matching_brace(s, j + 2) + 1
                        else:
                            j += 2
                        continue
                    break
                j += 1
            raw = s[i:j]
            out.append(Tok("word", i, j, norm_word(raw), raw))
            i = j
    return out


def tokenize_command(s, i, end, out):
    if s.startswith("\\\\", i):
        j = skip_args(s, i + 2, end) if s[i + 2:i + 3] in ("[", "*") else i + 2
        out.append(Tok("row", i, j))
        return j
    if s[i + 1:i + 2] in (",", ";", "!", " ", ":", "\n"):
        out.append(Tok("ws", i, i + 2))
        return i + 2
    if s[i + 1:i + 2] == "[":
        j = s.index("\\]", i) + 2
        out.append(Tok("display", i, j, norm_math(s[i + 2:j - 2]), "displaymath"))
        return j
    if s[i + 1:i + 2] == "(":
        j = s.index("\\)", i) + 2
        out.append(Tok("math", i, j, norm_math(s[i + 2:j - 2])))
        return j
    m = re.match(r"\\([A-Za-z]+)", s[i:end])
    if not m:                                   # escaped character or accent: a word
        out.append(Tok("word", i, i + 2, None, s[i:i + 2]))
        return i + 2
    name = m.group(1)
    j = i + m.end()
    if name == "begin":
        env = s[j + 1:s.index("}", j)]
        k = s.index("}", j) + 1
        if env in DISPLAY_ENVS:
            e = find_env_end(s, k, env)
            body = s[k:e - len("\\end{%s}" % env)]
            out.append(Tok("display", i, e, norm_math(body), env))
            return e
        k = skip_args(s, k, end)
        out.append(Tok("begin", i, k, name=env))
        return k
    if name == "end":
        k = s.index("}", j) + 1
        out.append(Tok("end", i, k))
        return k
    if name == "item":
        k = skip_args(s, j, end)
        out.append(Tok("item", i, k))
        return k
    if name == "dtap":
        k = j + 2 if s.startswith("{}", j) else j
        out.append(Tok("word", i, k, "dtap", "DTAP"))
        return k
    if name == "textsc" and s.startswith("{", j):
        k = matching_brace(s, j)
        out.append(Tok("word", i, k + 1, norm_word(s[j + 1:k]), s[i:k + 1]))
        return k + 1
    if name in REF_CMDS:
        k = skip_args(s, j, end)
        out.append(Tok("ref", i, k, "REF"))
        return k
    if name in CITE_CMDS:
        k = skip_args(s, j, end)
        keys = re.findall(r"\{([^}]*)\}", s[j:k])
        keys = sorted(x.strip() for x in ",".join(keys).split(","))
        out.append(Tok("cite", i, k, "CITE:" + ",".join(keys)))
        return k
    if name in TEXT_CMDS or name in HEAD_CMDS:
        k = j + 1 if s[j:j + 1] == "*" else j
        k = skip_args(s, k, end) if s[k:k + 1] == "[" else k
        if s[k:k + 1] != "{":
            out.append(Tok("neutral", i, k))
            return k
        close = matching_brace(s, k)
        kind_o, kind_c = ("hopen", "hclose") if name in HEAD_CMDS else ("open", "close")
        o = Tok(kind_o, i, k + 1, name=name)
        out.append(o)
        tokenize(s, k + 1, close, out)
        cl = Tok(kind_c, close, close + 1, name=name)
        o.partner, cl.partner = cl, o
        out.append(cl)
        return close + 1
    if name in ("multirow", "multicolumn"):
        # only the last argument is text: compare it like any other cell content
        args, k = [], j
        while k < end and s[k] in "[{":
            e = skip_args(s, k, end) if s[k] == "[" else matching_brace(s, k) + 1
            if s[k] == "[":                 # skip_args also takes the braces that follow
                e = s.index("]", k) + 1
            args.append((k, e))
            k = e
        if len(args) >= 3 and s[args[-1][0]] == "{":
            a, e = args[-1]
            out.append(Tok("neutral", i, a))
            o = Tok("open", a, a + 1)
            out.append(o)
            tokenize(s, a + 1, e - 1, out)
            cl = Tok("close", e - 1, e)
            o.partner, cl.partner = cl, o
            out.append(cl)
            return e
    k = skip_args(s, j, end)
    if name in NEUTRAL_CMDS or k == j:
        out.append(Tok("neutral", i, k))
    else:
        out.append(Tok("cmd", i, k, norm_math(s[i:k])))
    return k


def content(t):
    return t.kind in ("word", "math", "ref", "cite", "cmd") and t.norm is not None


def suppress_mentions(toks):
    """``Section~\\ref{x}'' and ``Appendix~\\ref{y}'' only differ in how they refer."""
    last = None
    for t in toks:
        if t.kind == "ref" and last is not None and last.norm in MENTION_WORDS:
            last.norm = None
        if content(t) or t.kind == "ref":
            last = t


# --------------------------------------------------------------------------- units
def units(toks):
    """Split tokens into units: sentences, cells, heading titles and displays."""
    out, cur = [], []
    head_depth = 0

    def flush():
        nonlocal cur
        if any(content(t) for t in cur):
            out.append(("head" if head_depth else "text", cur))
        cur = []

    for t in toks:
        if t.kind == "display":
            flush()
            out.append(("display", [t]))
            continue
        if t.kind in BARRIERS:
            flush()
            if t.kind == "hopen":
                head_depth += 1
            elif t.kind == "hclose":
                head_depth -= 1
            continue
        cur.append(t)
        if t.kind == "word" and t.name and re.search(r"[.?!][)'\"]*$", t.name) \
                and t.name.lower() not in ABBREVIATIONS and not head_depth:
            flush()
    flush()
    return out


def unit_key(u):
    kind, toks = u
    if kind == "display":
        return ("D", toks[0].norm)
    return tuple(t.norm for t in toks if content(t))


def analyse(text):
    toks = tokenize(text)
    suppress_mentions(toks)
    return toks, units(toks)


# --------------------------------------------------------------------------- marking
class Corpus:
    def __init__(self, blocks):
        self.keys = {}
        self.sets = []
        for b in blocks:
            _, us = analyse(b)
            ks = [unit_key(u) for u in us]
            for k in ks:
                self.keys[k] = self.keys.get(k, 0) + 1
            self.sets.append((ks, [set(k) for k in ks]))

    def candidates(self, key, own):
        """Old units to compare with: those of the aligned block, then long ones anywhere."""
        if own is not None:
            yield from self.sets[own][0]
        if len(key) >= GLOBAL_MIN_LEN:
            ks = set(key)
            for oks, osets in self.sets:
                for k, kset in zip(oks, osets):
                    if k and len(ks & kset) >= 0.5 * len(ks | kset):
                        yield k


# --------------------------------------------------------------------------- tables
TABULAR_RE = re.compile(r"\\begin\{(tabular|longtable)\}(\{(?:[^{}]|\{[^{}]*\})*\})*(.*?)\\end\{\1\}", re.S)
NUMERIC_CELL_RE = re.compile(r"[\d.\s/()\-+]*\d[\d.\s/()\-+]*")


def split_cells(s, a, b):
    """Rows of (start, end) cell spans of a tabular body s[a:b], split at top-level & and \\\\."""
    rows, row, start, depth, k = [], [], a, 0, a
    while k < b:
        ch = s[k]
        if ch == "\\" and s.startswith("\\\\", k) and depth == 0:
            row.append((start, k))
            rows.append(row)
            row = []
            k += 2
            if k < b and s[k] == "*":
                k += 1
            start = k
            continue
        if ch == "\\":
            k += 2
            continue
        if ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
        elif ch == "&" and depth == 0:
            row.append((start, k))
            start = k + 1
        k += 1
    row.append((start, b))
    rows.append(row)
    return rows


def clean_cell(c):
    c = re.sub(r"\\(multirow|multicolumn)\{[^}]*\}\{[^}]*\}", "", c)
    c = re.sub(r"\\cmidrule(\([a-z]*\))?\{[^}]*\}", "", c)
    return c


def cell_words(c):
    c = re.sub(r"\\[A-Za-z]+", " ", clean_cell(c))
    return {w for w in (norm_word(x) for x in re.findall(r"[A-Za-z][A-Za-z\-]*", c)) if w}


def cell_numbers(c):
    c = re.sub(r"\\[A-Za-z]+", " ", clean_cell(c))
    return {float(x) for x in re.findall(r"\d+(?:\.\d+)?", c)}


def is_numeric(c):
    c = re.sub(r"\\(mathbf|textbf|dagger|,|;)|[${}~^]", "", clean_cell(c)).strip()
    return bool(c) and bool(NUMERIC_CELL_RE.fullmatch(c))


def parse_table(s, a, b):
    """Header cells, data rows grouped by their label, and all words of a table."""
    rows = split_cells(s, a, b)
    header, data, label, started = [], [], None, False
    for row in rows:
        first = s[row[0][0]:row[0][1]]
        if "\\midrule" in first:
            started = True
        cells = [(x, y, s[x:y]) for x, y in row]
        if not any(cell_words(c) or cell_numbers(c) for _, _, c in cells):
            continue
        if not started:
            header.append(cells)
            continue
        lab = cell_words(cells[0][2]), cell_numbers(cells[0][2])
        if lab[0] or lab[1]:
            label = (tuple(sorted(lab[0])), tuple(sorted(lab[1])))
        data.append((label, cells))
    return header, data


def expand_spans(cells):
    """Repeat a \\multicolumn{n} cell n times so that cells line up with columns."""
    out = []
    for cell in cells:
        m = re.match(r"\s*\\multicolumn\{(\d+)\}", cell[2])
        out.extend([cell] * (int(m.group(1)) if m else 1))
    return out


def column_names(header, ncols):
    names = []
    for j in range(ncols):
        name = ()
        for row in reversed([expand_spans(r) for r in header]):
            if j < len(row) and cell_words(row[j][2]):
                name = tuple(sorted(cell_words(row[j][2])))
                break
        names.append(name)
    return names


def table_key(rows):
    groups = {}
    for label, cells in rows:
        g = groups.setdefault(label, (set(), set()))
        for _, _, c in cells:
            g[0].update(cell_numbers(c))
            g[1].update(cell_words(c))
    return groups


def mark_tables(text, toks, old_text, stats):
    """Decide the colour of every table cell by its content; returns the decided spans."""
    old_tabs = [m for m in TABULAR_RE.finditer(old_text)] if old_text else []
    old_words, old_groups, old_header_words = set(), {}, set()
    old_cells = {}            # (row label, column name) -> numbers of the old cell(s)
    for m in old_tabs:
        oh, od = parse_table(old_text, m.start(3), m.end(3))
        old_words |= cell_words(old_text[m.start():m.end()])
        onames = column_names(oh, max([len(c) for _, c in od] + [0]))
        for label, cells in od:
            for j, (_, _, c) in enumerate(cells):
                if j < len(onames) and onames[j]:
                    old_cells.setdefault((label, onames[j]), set()).update(cell_numbers(c))
        for row in oh:
            for _, _, c in row:
                old_header_words |= cell_words(c)
        for k, v in table_key(od).items():
            g = old_groups.setdefault(k, (set(), set()))
            g[0].update(v[0])
            g[1].update(v[1])
    decided = []
    for m in TABULAR_RE.finditer(text):
        if not old_tabs:                      # a new table: everything red
            decided.append((m.start(3), m.end(3), True))
            continue
        header, data = parse_table(text, m.start(3), m.end(3))
        ncols = max([len(c) for _, c in data] + [len(r) for r in header] + [0])
        names = column_names(header, ncols)
        new_col = [False] * ncols
        for row in header:
            for j, (_, _, c) in enumerate(row):
                if cell_words(c) - old_words:
                    new_col[j] = True
        red_cells = {}
        col_has_num = [False] * ncols
        col_red = [False] * ncols
        for label, cells in data:
            g = old_groups.get(label)
            for j, (x, y, c) in enumerate(cells):
                if not (cell_words(c) or cell_numbers(c)):
                    continue
                if j == 0:
                    red = g is None
                elif is_numeric(c):
                    col_has_num[j] = True
                    same_cell = old_cells.get((label, names[j])) if j < len(names) else None
                    if same_cell is not None:     # the same row and column exist in the old table
                        red = not cell_numbers(c) <= same_cell
                    else:                         # the table was rearranged: compare with the row
                        red = g is None or new_col[j] or not cell_numbers(c) <= g[0]
                else:
                    red = g is None or bool(cell_words(c) - old_words)
                red_cells[(x, y)] = red
                col_red[j] |= red
                stats["cell_red" if red else "cell_black"] += 1
        for row in header:
            for j, (x, y, c) in enumerate(row):
                if not (cell_words(c) or cell_numbers(c)):
                    continue
                red = new_col[j] and (col_has_num[j] or col_red[j])
                red_cells[(x, y)] = red
                stats["cell_red" if red else "cell_black"] += 1
        for (x, y), red in red_cells.items():
            decided.append((x, y, red))
        decided.append((m.start(3), m.end(3), None))   # the rest of the table is decided too
    for x, y, red in decided:
        if red is None:
            continue
        for t in toks:
            if x <= t.a < y and (content(t) or t.kind == "display"):
                t.red = red
    return [(x, y) for x, y, red in decided if red is None or red is True] + \
           [(x, y) for x, y, red in decided if red is False]


def mark_block(text, own, corpus, stats, old_text=None):
    toks, us = analyse(text)
    own_keys = set(corpus.sets[own][0]) if own is not None else set()
    tables = mark_tables(text, toks, old_text, stats) if "\\begin{tabular}" in text else []
    for u in us:
        kind, utoks = u
        if any(x <= utoks[0].a < y for x, y in tables):
            continue
        key = unit_key(u)
        if kind == "display":
            hit = key in own_keys or (len(key[1] or "") >= 15 and key in corpus.keys)
            utoks[0].red = not hit
            stats["display_" + ("black" if hit else "red")] += 1
            continue
        ctoks = [t for t in utoks if content(t)]
        if key in own_keys or (len(key) >= GLOBAL_MIN_LEN and key in corpus.keys):
            stats["unit_same"] += 1
            continue
        if kind == "head":
            for t in ctoks:
                t.red = True
            stats["unit_red"] += 1
            continue
        best, best_r = None, 0.0
        for cand in corpus.candidates(key, own):
            if not cand or cand[0] == "D":
                continue
            sm = difflib.SequenceMatcher(None, cand, key, autojunk=False)
            if sm.real_quick_ratio() <= best_r or sm.quick_ratio() <= best_r:
                continue
            r = sm.ratio()
            if r > best_r:
                best, best_r = cand, r
        if best is None or best_r < WORD_LEVEL_MIN:
            for t in ctoks:
                t.red = True
            stats["unit_red"] += 1
            continue
        red = [False] * len(ctoks)
        sm = difflib.SequenceMatcher(None, best, key, autojunk=False)
        for tag, i1, i2, j1, j2 in sm.get_opcodes():
            if tag in ("replace", "insert"):
                for j in range(j1, j2):
                    red[j] = True
        idx = [j for j, r in enumerate(red) if r]
        for a, b in zip(idx, idx[1:]):
            if 1 < b - a <= GAP_MERGE + 1:
                for j in range(a + 1, b):
                    red[j] = True
        if sum(red) >= WHOLE_UNIT_FRAC * len(red):
            red = [True] * len(red)
        if any(red):
            stats["unit_red" if all(red) else "unit_words"] += 1
        else:
            stats["unit_form_only"] += 1
        for t, r in zip(ctoks, red):
            t.red = r
    return toks


def color_display(src, tok):
    env = tok.name
    if env == "displaymath" and src.startswith("\\["):
        return src[:2] + OPEN_HEAD + src[2:-2] + "}" + src[-2:]
    m = re.match(r"\\begin\{%s\}(\s*\\label\{[^}]*\})?" % re.escape(env), src)
    endtag = "\\end{%s}" % env
    head, body, tail = src[:m.end()], src[m.end():len(src) - len(endtag)], endtag
    if env not in ALIGN_ENVS:
        return head + OPEN_HEAD + body + "}" + tail
    # alignments: the colour is set at the start of every top-level cell
    out, depth, envdepth, k = [RED_SWITCH], 0, 0, 0
    while k < len(body):
        if body.startswith("\\begin{", k):
            envdepth += 1
        elif body.startswith("\\end{", k):
            envdepth -= 1
        ch = body[k]
        if depth == 0 and envdepth == 0 and body.startswith("\\\\", k):
            j = k + 2
            if body[j:j + 1] == "[":
                j = body.index("]", j) + 1
            out.append(body[k:j] + RED_SWITCH)
            k = j
            continue
        if ch == "\\" and k + 1 < len(body):
            out.append(body[k:k + 2])
            k += 2
            continue
        if ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
        out.append(ch)
        if depth == 0 and envdepth == 0 and ch == "&":
            out.append(RED_SWITCH)
        k += 1
    return head + "".join(out) + tail


def render(text, toks):
    """Insert the colour into the original text of a block."""
    ins = {}                      # position -> list of strings to insert there

    def add(pos, s):
        ins.setdefault(pos, []).append(s)

    depth, ctx_at = 0, []
    for t in toks:
        if t.kind == "hopen":
            depth += 1
        elif t.kind == "hclose":
            depth -= 1
        ctx_at.append(depth > 0)

    n = len(toks)
    i = 0
    while i < n:
        t = toks[i]
        if t.kind == "display" and t.red:
            add(t.a, ("DISPLAY", t))
            i += 1
            continue
        if not (content(t) and t.red):
            i += 1
            continue
        # grow a run of red content and the neutral tokens between them
        j, last = i, i
        while j + 1 < n:
            u = toks[j + 1]
            if u.kind in BARRIERS or (content(u) and not u.red):
                break
            j += 1
            if content(u) and u.red:
                last = j
        run = list(range(i, last + 1))
        ids = {id(toks[x]) for x in run}
        # split where a group would be cut in half
        segs, cur = [], []
        for k in run:
            tk = toks[k]
            if tk.kind in ("open", "close") and id(tk.partner) not in ids:
                segs.append(cur)
                cur = []
                continue
            cur.append(k)
        segs.append(cur)
        for seg in segs:
            cs = [k for k in seg if content(toks[k])]
            if not cs or not any(toks[k].red for k in cs):
                continue
            a, b = cs[0], cs[-1]
            add(toks[a].a, OPEN_HEAD if ctx_at[a] else OPEN_TEXT)
            add(toks[b].b, "}")
        i = last + 1

    out, pos = [], 0
    for p in sorted(ins):
        out.append(text[pos:p])
        disp = None
        for s in ins[p]:
            if isinstance(s, tuple):
                disp = s[1]
            else:
                out.append(s)
        if disp is not None:
            out.append(color_display(text[disp.a:disp.b], disp))
            pos = disp.b
        else:
            pos = p
    out.append(text[pos:])
    return "".join(out)


def uncolor(text):
    """Inverse of the colouring, used to check that no text was lost or changed."""
    out, pos = [], 0
    pat = re.compile(r"(\\leavevmode)?\\textcolor\{red\}\{")
    while True:
        m = pat.search(text, pos)
        if not m:
            break
        close = matching_brace(text, m.end() - 1)
        out.append(text[pos:m.start()])
        out.append(uncolor(text[m.end():close]))
        pos = close + 1
    out.append(text[pos:])
    return "".join(out).replace(RED_SWITCH, "")


def unit_text(src, utoks):
    return re.sub(r"\s+", " ", src[utoks[0].a:utoks[-1].b])


# --------------------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--report", action="store_true", help="print the decision for every unit")
    args = ap.parse_args()

    old_text = bd.OLD_TEX.read_text(encoding="utf-8")
    new_text = bd.NEW_TEX.read_text(encoding="utf-8")
    old_pre, old_body, old_bib, old_tail = bd.split_document(old_text)
    new_pre, new_body, new_bib, new_tail = bd.split_document(new_text)
    old, new, segs = bd.build_changes(old_body + "\n\n" + old_tail, new_body + "\n\n" + new_tail)
    corpus = Corpus(old)
    stats = {k: 0 for k in ("unit_same", "unit_form_only", "unit_words", "unit_red",
                            "display_black", "display_red", "cell_black", "cell_red")}

    start = new_text.index("\\begin{document}")
    bib_at = new_text.index("\\begin{thebibliography}")
    out, pos = [new_text[:start]], start
    for s in segs:
        k = s["kind"]
        if k in ("del", "movedfrom"):
            continue
        nb = new[s["j"]]
        at = new_text.index(nb, pos)
        assert at < bib_at, "block found after the references"
        out.append(new_text[pos:at])
        if k == "same":
            out.append(nb)
        else:
            own = s["i"] if k in ("edit", "rewrite", "movedto") else None
            toks = mark_block(nb, own, corpus, stats, old[own] if own is not None else None)
            out.append(render(nb, toks))
            if args.report:
                for _, ut in units(toks):
                    flags = [t.red for t in ut if content(t) or t.kind == "display"]
                    flag = "RED " if all(flags) else ("part" if any(flags) else "    ")
                    print(flag, unit_text(nb, ut)[:120])
        pos = at + len(nb)
    out.append(new_text[pos:])          # the references are copied unchanged
    doc = "".join(out)
    if uncolor(doc) != new_text:
        raise SystemExit("check failed: without the colour the file differs from main_document.tex")
    print("check: without the colour, the file equals main_document.tex character by character",
          file=sys.stderr)
    print("units:", stats, file=sys.stderr)

    OUT_TEX.write_text(doc, encoding="utf-8")
    if WORK.exists():
        shutil.rmtree(WORK)
    WORK.mkdir()
    shutil.copy(OUT_TEX, WORK / "colored.tex")
    shutil.copy(bd.NEW_DIR / "interact.cls", WORK / "interact.cls")
    for _ in range(3):
        subprocess.run(["pdflatex", "-interaction=nonstopmode", "colored.tex"], cwd=WORK,
                       capture_output=True)
    log = (WORK / "colored.log").read_text(encoding="utf-8", errors="replace")
    errors = [l for l in log.split("\n") if l.startswith("!")]
    shutil.copy(WORK / "colored.pdf", OUT_PDF)
    print("written:", OUT_TEX.name, "and", OUT_PDF.name, file=sys.stderr)
    print("LaTeX errors:", len(errors), file=sys.stderr)
    for e in errors[:10]:
        print("  ", e, file=sys.stderr)
    print("undefined references:", sorted(set(re.findall(r"Reference `([^']*)'", log))),
          file=sys.stderr)


if __name__ == "__main__":
    main()
