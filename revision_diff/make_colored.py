#!/usr/bin/env python3
"""Write a copy of the revised manuscript in which added or modified text is red.

The journal asks for the changes to be highlighted in the revised manuscript. This
script reuses the block comparison of build_diff.py and writes
"DTAP Finally/main_document_colored.tex" (the original main_document.tex is not
touched):

* blocks that are new, rewritten or moved are red as a whole;
* blocks that were only edited have their added words in red;
* deleted text does not appear (it is shown in the separate marked-up PDF);
* the references are not coloured.

As a check, removing every \\textcolor{red}{...} wrapper and the inserted colour
switches must give back main_document.tex character by character.

Usage:  python make_colored.py
"""
import re
import shutil
import subprocess
import sys
from pathlib import Path

import build_diff as bd
from assemble import math_switches, matching_brace

OUT_TEX = bd.NEW_DIR / "main_document_colored.tex"
OUT_PDF = bd.NEW_DIR / "DTAP_OMS_colored.pdf"
WORK = bd.ROOT / "build_colored"
RED_SWITCH = r"\color{red}"


def strip_deletions(frag):
    """Keep only the new text of a latexdiff fragment, with additions in red."""
    frag = re.sub(r"\\DIFdelbegin(FL)?\b.*?\\DIFdelend(FL)?\b", "", frag, flags=re.S)
    frag = "\n".join(l for l in frag.split("\n") if not l.lstrip().startswith("%DIF"))
    frag = re.sub(r"%DIFAUXCMD", "", frag)
    frag = re.sub(r"\\DIFadd(begin|end)(FL)?\b\s?", "", frag)
    # latexdiff protects citations as \mbox{\cite..{..}}\hskip0pt; restore the source form
    frag = re.sub(r"\\mbox\{\s*(\\cite[a-z]*\{[^}]*\})\s*\}\\hskip0pt", r"\1", frag)
    frag = re.sub(r"\\DIFadd(FL)?\{", r"\\textcolor{red}{", frag)
    frag = frag.replace(r"\DIFaddmath ", RED_SWITCH + " ")
    if "\\DIF" in frag:
        raise RuntimeError("unhandled latexdiff command in fragment:\n" + frag)
    return frag


OPEN_TXT = "\\leavevmode{\\color{red}%RED"     # start of a red run inside a paragraph
OPEN_ENV = "{\\color{red}%RED"                  # start of a red run inside an environment
CLOSE = "}%ENDRED"
GROUP_ENVS = ("abstract", "remark", "lemma", "proposition", "theorem", "corollary",
              "definition", "example", "assumption", "proof", "enumerate", "itemize")
HEAD_RE = re.compile(r"\\(section|subsection|subsubsection|paragraph)\*?\{")


def _open(marker, following):
    # the comment swallows the line end that follows, so no space is added; where the
    # original text has no line end there, one is added and the marker says so ("+")
    return marker if following.startswith("\n") else marker + "+\n"


def _close(following):
    return CLOSE if following.startswith("\n") else CLOSE + "+\n"


DISPLAY_END_RE = re.compile(r"(\\begin\{(equation|align|gather|multline)\*?\}|\\\[)((?:(?!\\begin\{(?:equation|align|gather|multline)\*?\}|\\\[).)*?)(\\end\{\2\*?\}|\\\])\s*$", re.S)
DISPLAY_LABEL_RE = re.compile(r"\\label\{[^}]*\}")


def _split_trailing_display(body):
    """Split off a displayed formula that ends the text, if any.

    Closing a colour group right after a display adds an empty line, so a trailing
    display is coloured from the inside instead (the colour ends with the display).
    """
    m = DISPLAY_END_RE.search(body)
    if not m:
        return body, ""
    return body[:m.start()], body[m.start():]


def _red_display(display):
    """Colour a displayed formula with \\textcolor, so that the colour ends inside it.

    A bare colour switch would be reset after the display, in horizontal mode, which
    adds an empty line below the formula.
    """
    m = re.match(r"(\\begin\{[a-z]+\*?\}|\\\[)(\\label\{[^}]*\})?", display)
    e = re.search(r"(\\end\{[a-z]+\*?\}|\\\])$", display)
    body = display[m.end():e.start()]
    if "&" in body or "\\\\" in body:
        raise RuntimeError("aligned display at the end of a new block: colour it by hand\n" + display)
    return display[:m.end()] + MARK_OPEN + body + "}" + display[e.start():]


def _red_run(text):
    """Colour a run of paragraph text, starting and ending inside the paragraph."""
    a = len(text) - len(text.lstrip())
    b = len(text.rstrip())
    if a >= b:
        return text
    body = text[a:b]
    if re.fullmatch(r"(\s*\\label\{[^}]*\})+\s*", body):
        return text                     # only labels: nothing to colour, no paragraph to start
    h = HEAD_RE.match(body)
    if h:                                   # heading: colour its title, then the text after it
        close = matching_brace(body, h.end() - 1)
        title = body[:h.end()] + MARK_OPEN + body[h.end():close] + "}" + body[close]
        rest = body[close + 1:]
        lab = re.match(r"(\s*\\label\{[^}]*\})+", rest)
        if lab:
            title += rest[:lab.end()]
            rest = rest[lab.end():]
        return text[:a] + title + _red_run(rest) + text[b:]
    before, display = _split_trailing_display(body)
    if display:
        if not before.strip():
            return text[:a] + _red_display(display) + text[b:]
        a2 = len(before.rstrip())
        return (text[:a] + _open(OPEN_TXT, before) + before[:a2] + _close(before[a2:]) + before[a2:]
                + _red_display(display) + text[b:])
    return (text[:a] + _open(OPEN_TXT, body) + body + _close(text[b:]) + text[b:])


def red_block(block):
    """Colour a whole block red without putting colour switches between paragraphs.

    A colour switch in vertical mode is a whatsit that stops \\addvspace from merging
    the spaces around lists and theorem-like environments, so the coloured copy would
    no longer have the layout of the original. The switches are therefore placed
    inside paragraphs, inside environments, in heading titles and inside floats.
    """
    m = re.match(r"\s*\\begin\{(table|figure)\}(\[[^\]]*\])?", block)
    if m:                                   # floats: the switch goes inside the float
        return block[:m.end()] + RED_SWITCH + block[m.end():]
    out, pos = [], 0
    pat = re.compile(r"\\begin\{(%s)\}(\[[^\]]*\])?(\\label\{[^}]*\})?" % "|".join(GROUP_ENVS))
    for m in pat.finditer(block):
        if m.start() < pos:
            continue
        env = m.group(1)
        endtag = "\\end{%s}" % env
        close_at = block.index(endtag, m.end())
        out.append(_red_run(block[pos:m.start()]))
        inner = block[m.end():close_at]
        b = len(inner.rstrip())
        before, display = _split_trailing_display(inner[:b])
        if display:
            a2 = len(before.rstrip())
            colored = (_open(OPEN_ENV, inner) + before[:a2] + _close(before[a2:]) + before[a2:]
                       + _red_display(display) + inner[b:])
        else:
            colored = _open(OPEN_ENV, inner) + inner[:b] + _close(inner[b:]) + inner[b:]
        out.append(m.group(0) + colored + endtag)
        pos = close_at + len(endtag)
    out.append(_red_run(block[pos:]))
    return "".join(out)


def uncolor(text):
    """Inverse of the colouring, used to check that no text was lost or changed."""
    out, pos = [], 0
    for m in re.finditer(r"\\textcolor\{red\}\{", text):
        if m.start() < pos:
            continue
        close = matching_brace(text, m.end() - 1)
        out.append(text[pos:m.start()])
        out.append(uncolor(text[m.end():close]))
        pos = close + 1
    out.append(text[pos:])
    text = "".join(out)
    for marker in (OPEN_TXT + "+\n", OPEN_TXT, OPEN_ENV + "+\n", OPEN_ENV, CLOSE + "+\n", CLOSE):
        text = text.replace(marker, "")
    return text.replace(RED_SWITCH, "")


MARK_OPEN = "\\textcolor{red}{"


def project(colored, original):
    """Carry the red mark-up of a latexdiff fragment over to the original block text.

    latexdiff changes white space (for example it leaves a space where deleted text
    was, as in ``maximum ,''), so its output is only used to decide which characters
    are red. The mark-up is inserted into the untouched original text, character by
    character, so that the original spacing and line breaks are kept exactly.
    """
    # latexdiff rewrites \frac12 as \frac{1}{2}; restore the source form where needed
    for m in set(re.findall(r"\\frac\{(\w)\}\{(\w)\}", colored)):
        a, b = m
        if "\\frac{%s}{%s}" % (a, b) not in original and "\\frac%s%s" % (a, b) in original:
            colored = colored.replace("\\frac{%s}{%s}" % (a, b), "\\frac%s%s" % (a, b))
    out, j, depth, opened = [], 0, 0, []
    i = 0

    def take_space():
        nonlocal j
        while j < len(original) and original[j].isspace():
            out.append(original[j])
            j += 1

    while i < len(colored):
        if colored.startswith(MARK_OPEN, i):
            take_space()
            out.append(MARK_OPEN)
            opened.append(depth)
            i += len(MARK_OPEN)
            continue
        if colored.startswith(RED_SWITCH, i):
            out.append(RED_SWITCH)
            i += len(RED_SWITCH)
            continue
        c = colored[i]
        if c.isspace():
            i += 1
            continue
        if c == "}" and opened and depth == opened[-1] and not colored[i - 1] == "\\":
            opened.pop()
            out.append("}")
            i += 1
            continue
        take_space()
        if j >= len(original) or original[j] != c:
            raise RuntimeError("cannot place the colour: %r vs %r" % (colored[i:i + 40], original[j:j + 40]))
        if c == "\\" and i + 1 < len(colored):      # escaped character: copy both
            out.append(original[j:j + 2])
            i += 2
            j += 2
            continue
        if c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
        out.append(c)
        i += 1
        j += 1
    out.append(original[j:])
    return "".join(out)


def main():
    old_text = bd.OLD_TEX.read_text(encoding="utf-8")
    new_text = bd.NEW_TEX.read_text(encoding="utf-8")
    old_pre, old_body, old_bib, old_tail = bd.split_document(old_text)
    new_pre, new_body, new_bib, new_tail = bd.split_document(new_text)
    old, new, segs = bd.build_changes(old_body + "\n\n" + old_tail, new_body + "\n\n" + new_tail)

    if WORK.exists():
        shutil.rmtree(WORK)
    new_labels = set(bd.LABEL_RE.findall(new_text))

    # every block is replaced in place, so the text between blocks (blank lines) and
    # everything outside the body (preamble, references) stays exactly as it is
    start = new_text.index("\\begin{document}")
    bib_at = new_text.index("\\begin{thebibliography}")
    out, pos, n = [new_text[:start]], start, 0
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
        elif k in ("add", "rewrite", "movedto"):
            out.append(red_block(nb))
        else:  # edit: only the added words are red
            n += 1
            frag = bd.run_latexdiff(bd.old_ref_rewrite(old[s["i"]], new_labels), nb, WORK / ("ld%03d" % n))
            out.append(project(strip_deletions(math_switches(frag)), nb))
        pos = at + len(nb)
    out.append(new_text[pos:])          # the references are copied unchanged
    note = ("% Copy of main_document.tex in which added or modified text is red, as requested\n"
            "% by the journal. Generated by revision_diff/make_colored.py; do not edit by hand.\n")
    doc = "".join(out)

    # check: removing the colour gives back main_document.tex character by character
    if uncolor(doc) != new_text:
        raise SystemExit("check failed: without the colour the file differs from main_document.tex")
    print("check: without the colour, the file equals main_document.tex character by character",
          file=sys.stderr)

    OUT_TEX.write_text(note + doc, encoding="utf-8")
    WORK.mkdir(exist_ok=True)
    shutil.copy(OUT_TEX, WORK / "colored.tex")
    shutil.copy(bd.NEW_DIR / "interact.cls", WORK / "interact.cls")
    for _ in range(3):
        subprocess.run(["pdflatex", "-interaction=nonstopmode", "colored.tex"], cwd=WORK,
                       capture_output=True)
    log = (WORK / "colored.log").read_text(encoding="utf-8", errors="replace")
    errors = [l for l in log.split("\n") if l.startswith("!")]
    shutil.copy(WORK / "colored.pdf", OUT_PDF)
    print("written:", OUT_TEX.name, "and", OUT_PDF.name)
    print("LaTeX errors:", len(errors))
    for e in errors[:10]:
        print("  ", e)
    print("undefined references:", sorted(set(re.findall(r"Reference `([^']*)'", log))))


if __name__ == "__main__":
    main()
