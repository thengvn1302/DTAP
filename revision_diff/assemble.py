"""Second stage of build_diff.py: write the marked-up LaTeX source and compile it."""
import json
import re
import shutil
import subprocess
from pathlib import Path

import build_diff as bd

DIFF_PREAMBLE = r"""
% ---------------------------------------------------------------- change mark-up
\usepackage{fontspec}
\usepackage{luacolor,lua-ul,marginnote}
\usepackage[luatex,leftbars]{changebar}
\cbcolor{orange}
\setlength{\changebarwidth}{1.6pt}
\setlength{\changebarsep}{6mm}
\setlength{\marginparwidth}{2.5cm}
\setlength{\marginparsep}{3mm}
\LuaULSetHighLightColor{yellow!55}
\definecolor{DIFdelcolor}{rgb}{0.85,0,0}
\definecolor{DIFtagcolor}{rgb}{1,0.88,0.70}
\makeatletter
% word-level mark-up produced by latexdiff
\newcommand{\DIFadd}[1]{\highLight{#1}}
\newcommand{\DIFdel}[1]{{\color{DIFdelcolor}\strikeThrough[DIFdelcolor]{#1}}}
\newcommand{\DIFaddFL}[1]{\DIFadd{#1}}
\newcommand{\DIFdelFL}[1]{\DIFdel{#1}}
\newcommand{\DIFaddbegin}{}\newcommand{\DIFaddend}{}
\newcommand{\DIFdelbegin}{}\newcommand{\DIFdelend}{}
\newcommand{\DIFmodbegin}{}\newcommand{\DIFmodend}{}
\newcommand{\DIFaddbeginFL}{}\newcommand{\DIFaddendFL}{}
\newcommand{\DIFdelbeginFL}{}\newcommand{\DIFdelendFL}{}
\newcommand{\DIFaddmath}{\@highLight}
\newcommand{\DIFdelmath}{\color{DIFdelcolor}\@strikeThrough[DIFdelcolor]}
% whole added / deleted blocks
\newcommand{\DIFaddblockbegin}{\par\begingroup\@highLight}
\newcommand{\DIFaddblockend}{\par\endgroup}
\newcommand{\DIFdelblockbegin}{\par\begingroup\color{DIFdelcolor}\@strikeThrough[DIFdelcolor]}
\newcommand{\DIFdelblockend}{\par\endgroup}
\newsavebox{\DIFfloatbox}
\newcommand{\DIFaddfloatbegin}{\begin{lrbox}{\DIFfloatbox}\begin{minipage}{\dimexpr\linewidth-2\fboxsep\relax}\LuaULResetUnderline*}
\newcommand{\DIFaddfloatend}{\end{minipage}\end{lrbox}\colorbox{yellow!30}{\usebox{\DIFfloatbox}}}
\newcommand{\DIFdelfloatbegin}{\par\noindent\begin{lrbox}{\DIFfloatbox}\begin{minipage}{\dimexpr\linewidth-2\fboxsep-2\fboxrule\relax}\LuaULResetUnderline*\color{DIFdelcolor}}
\newcommand{\DIFdelfloatend}{\end{minipage}\end{lrbox}\fcolorbox{DIFdelcolor}{white}{\usebox{\DIFfloatbox}}\par}
% margin tag: number, reviewer comments, extra note
\newcommand{\DIFtag}[3]{\marginnote{\raggedright\fontsize{6.5}{7.5}\selectfont\sffamily
  \colorbox{DIFtagcolor}{\textbf{C#1}}\ifx\relax#2\relax\else\ #2\fi
  \ifx\relax#3\relax\else\\#3\fi}\label{chg:#1}}
\newcommand{\DIFtagagain}[2]{\marginnote{\raggedright\fontsize{6.5}{7.5}\selectfont\sffamily
  \colorbox{DIFtagcolor}{\textbf{C#1}}\ifx\relax#2\relax\else\\#2\fi}}
% pieces of deleted old text
\newcommand{\DIFoldheading}[3]{\par\medskip\noindent{\bfseries[\,Mục cũ\ifx\relax#2\relax\else\ #2\fi\,]\ #3}\par\smallskip}
\newcommand{\DIFoldcaption}[3]{\par\noindent{\small\bfseries #1 cũ\ifx\relax#2\relax\else\ #2\fi.}\ {\small #3}\par\smallskip}
\newcommand{\DIFoldthm}[3]{\par\smallskip\noindent{\bfseries #1\ifx\relax#2\relax\else\ #2\fi}\ifx\relax#3\relax\else\ (#3)\fi.\ }
\newcommand{\DIFoldthmend}{\par\smallskip}
\newcommand{\DIFoldproof}{\par\noindent\textit{Proof.}\ }
\newcommand{\DIFoldproofend}{\par}
\newcommand{\DIFoldfootnote}[1]{\ [Chú thích cũ: #1]}
\newcommand{\DIFmovedfrom}[2]{\par\smallskip\noindent{\color{DIFdelcolor}\small\itshape
  [\,Đoạn này của bản cũ#2 đã được chuyển sang vị trí mới --- xem C#1, tr.~\pageref{chg:#1}\,]}%
  \par\smallskip}
\makeatother
\providecommand{\doi}[1]{doi: #1}
"""


def old_label_table(build):
    """Compile the old manuscript once and read its label numbers and pages."""
    work = build / "oldref"
    work.mkdir(parents=True, exist_ok=True)
    for f in bd.OLD_DIR.iterdir():
        if f.suffix in (".png", ".cls", ".pdf", ".eps", ".jpg"):
            shutil.copy(f, work / f.name)
    shutil.copy(bd.OLD_TEX, work / "old.tex")
    for _ in range(2):
        subprocess.run(["pdflatex", "-interaction=nonstopmode", "old.tex"], cwd=work,
                       capture_output=True)
    labels = {}
    for line in (work / "old.aux").read_text(encoding="utf-8", errors="replace").split("\n"):
        m = re.match(r"\\newlabel\{([^}]*)\}\{\{(.*?)\}\{(.*?)\}", line)
        if m:
            labels[m.group(1)] = (m.group(2), m.group(3))
    return labels


def tabular_spec(block):
    m = re.search(r"\\begin\{(tabular|longtable)\}(.*)", block)
    return m.group(2).strip() if m else None


def is_float(block):
    return bool(bd.FLOAT_RE.search(block))


def convert_longtable(text):
    """Turn a deleted longtable into caption + tabular (no repeated heads)."""
    m = re.search(r"\\begin\{DIFoldlongtable\}(\{(?:[^{}]|\{[^{}]*\})*\})(.*?)\\end\{DIFoldlongtable\}",
                  text, re.S)
    if not m:
        return text
    spec, content = m.group(1), m.group(2)
    cap = re.search(r"(\\DIFoldcaption\{[^}]*\}\{[^}]*\}\{(?:[^{}]|\{[^{}]*\})*\})\s*\\\\", content, re.S)
    caption = cap.group(1) if cap else ""
    head = content[cap.end():content.index("\\endfirsthead")] if cap else ""
    rows = content[content.index("\\endlastfoot") + len("\\endlastfoot"):]
    # a deleted longtable becomes a float, so that LaTeX can move it to a page where it fits
    new = "\\begin{table}[htbp]\\footnotesize\n%s\n\\begin{tabular}%s\n%s\n%s\n\\bottomrule\n\\end{tabular}\n\\end{table}\n" % (
        caption, spec, head.strip(), rows.strip())
    return text[:m.start()] + new + text[m.end():]


def float_switch(block, switch):
    """Floats reset colour and attributes, so the mark-up is repeated inside them."""
    return re.sub(r"(\\begin\{(?:table|figure)\}(?:\[[^\]]*\])?)", lambda m: m.group(1) + switch, block)


def deleted_float_box(block):
    """Frame deleted floats and tables in red (strike-through is unreliable in tables)."""
    block = re.sub(r"(\\begin\{(table|figure)\}(?:\[[^\]]*\])?)", r"\1\\DIFdelfloatbegin", block)
    block = re.sub(r"(\\end\{(?:table|figure)\})", r"\\DIFdelfloatend\1", block)
    if "\\DIFdelfloatbegin" not in block and "\\begin{tabular}" in block:
        block = "\\DIFdelfloatbegin\n" + block + "\n\\DIFdelfloatend"
    return block


def added_float_box(block):
    """Put the whole body of an added float on a light yellow background."""
    block = re.sub(r"(\\begin\{(table|figure)\}(?:\[[^\]]*\])?)", r"\1\\DIFaddfloatbegin", block)
    return re.sub(r"(\\end\{(?:table|figure)\})", r"\\DIFaddfloatend\1", block)


def matching_brace(text, start):
    """Index of the brace closing the one at text[start]."""
    depth, k = 0, start
    while k < len(text):
        c = text[k]
        if c == "\\":
            k += 2
            continue
        if c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
            if depth == 0:
                return k
        k += 1
    raise ValueError("unbalanced")


def math_switches(frag):
    """\\begin{env}\\DIFadd{body}\\end{env} -> \\begin{env}\\DIFaddmath body\\end{env}.

    latexdiff wraps whole displayed equations in one argument, which breaks
    alignment environments (split, align) whose cells contain &.
    """
    pat = re.compile(r"\\begin\{([A-Za-z*]+)\}\\DIF(add|del)(FL)?\{")
    out, pos = [], 0
    for m in pat.finditer(frag):
        if m.start() < pos:
            continue
        close = matching_brace(frag, m.end() - 1)
        tail = frag[close + 1:]
        endtag = "\\end{%s}" % m.group(1)
        if not tail.startswith(endtag):
            continue
        out.append(frag[pos:m.start()])
        out.append("\\begin{%s}\\DIF%smath %s%s" % (m.group(1), m.group(2), frag[m.end():close], endtag))
        pos = close + 1 + len(endtag)
    out.append(frag[pos:])
    return "".join(out)


class Renderer:
    def __init__(self, old_labels, new_labels, notes, work):
        self.old_labels = old_labels
        self.old_numbers = {k: v[0] for k, v in old_labels.items()}
        self.new_labels = new_labels
        self.notes = notes
        self.work = work
        self.tagged = set()
        self.n_latexdiff = 0

    # ---- pieces
    def refs(self, cid):
        n = self.notes.get(str(cid), {})
        return ", ".join(n.get("refs", [])) or "?"

    def tag(self, cid, extra=""):
        if cid in self.tagged:
            return "\\DIFtagagain{%d}{%s}" % (cid, extra)
        self.tagged.add(cid)
        return "\\DIFtag{%d}{%s}{%s}" % (cid, self.refs(cid), extra)

    def old_prepare(self, block):
        block = bd.old_ref_rewrite(block, self.new_labels)
        return block

    def neutralize(self, block):
        # captions carry the old float number
        def cap_repl(m, env, num):
            return "\\DIFoldcaption{%s}{%s}{" % (env, num)
        fl = re.search(r"\\begin\{(table|figure|longtable)\}", block)
        if fl:
            env = "Hình" if fl.group(1) == "figure" else "Bảng"
            labs = bd.LABEL_RE.findall(block)
            num = next((self.old_numbers[l] for l in labs if l in self.old_numbers), "")
            block = block.replace("\\caption{", "\\DIFoldcaption{%s}{%s}{" % (env, num))
            block = block.replace("width=\\textwidth", "width=0.6\\textwidth")
        # theorem-like environments: keep the old number
        def thm(m):
            env, opt, lab = m.group(1), (m.group(2) or "")[1:-1], m.group(3)
            num = self.old_numbers.get(lab, "") if lab else ""
            return "\\DIFoldthm{%s}{%s}{%s}" % (env.capitalize(), num, opt)
        block = re.sub(r"\\begin\{(%s)\}(\[[^\]]*\])?(?:\\label\{([^}]*)\})?" % "|".join(bd.THEOREM_ENVS),
                       thm, block)
        for env in bd.THEOREM_ENVS:
            block = block.replace("\\end{%s}" % env, "\\DIFoldthmend")
        block = bd.neutralize_old(block, self.old_numbers)
        block = block.replace("\\DIFoldcaption{", "\\DIFoldcaption{")
        return convert_longtable(block)

    def del_block(self, block):
        body = deleted_float_box(self.neutralize(self.old_prepare(block)))
        return "\\DIFdelblockbegin\n%s\n\\DIFdelblockend" % body

    def add_block(self, block):
        return "\\DIFaddblockbegin\n%s\n\\DIFaddblockend" % added_float_box(block)

    def word_diff(self, oblock, nblock):
        self.n_latexdiff += 1
        frag = bd.run_latexdiff(self.old_prepare(oblock), nblock, self.work / ("ld%03d" % self.n_latexdiff))
        return math_switches(frag)


    def wrap_cb(self, body, float_block):
        if float_block:
            return body
        return "\\cbstart\n%s\n\\cbend" % body

    def inject_tag(self, rendered, tag, float_block):
        """Place the margin tag inside floats, after headings, or at the start.

        A tag placed before a float or a heading would end up on the previous line or
        page, so it goes inside the float or right after the heading instead.
        """
        m = re.search(r"\\begin\{(table|figure|algorithm)\}(\[[^\]]*\])?", rendered)
        if m and (float_block or m.group(1) == "algorithm"):
            return rendered[:m.end()] + tag + rendered[m.end():]
        h = re.match(r"\s*(?:\\DIF(?:add|del)blockbegin\s*)?\\(section|subsection|subsubsection|DIFoldheading)\*?\{",
                     rendered)
        if h:
            end = matching_brace(rendered, h.end() - 1)
            if h.group(1) == "DIFoldheading":      # three arguments
                for _ in range(2):
                    end = matching_brace(rendered, end + 1)
            lab = re.match(r"\s*\\label\{[^}]*\}", rendered[end + 1:])
            if lab:
                end += lab.end()
            return rendered[:end + 1] + tag + "%\n" + rendered[end + 1:]
        return tag + "%\n" + rendered

    # ---- one segment
    def render(self, s, old, new):
        k, cid = s["kind"], s.get("cid")
        if k == "same":
            return new[s["j"]]
        ob = old[s["i"]] if s["i"] is not None else None
        nb = new[s["j"]] if s["j"] is not None else None
        if k == "movedfrom":
            where = s.get("sec_old", "")
            sec = self.old_section_number(ob, s)
            return "\\DIFmovedfrom{%d}{%s}" % (cid, (" (mục cũ %s)" % sec) if sec else "")
        flt = is_float(ob or "") or is_float(nb or "")
        extra = ""
        if k == "movedto":
            sec = self.old_section_number(ob, s)
            extra = "chuyển từ mục cũ %s" % sec if sec else "chuyển từ chỗ khác"
        if k in ("edit", "movedto"):
            word_level = bd.similarity(ob, nb) >= bd.WORD_LEVEL_MIN
            if flt and tabular_spec(ob) != tabular_spec(nb):
                word_level = False
            body = self.word_diff(ob, nb) if word_level else (self.del_block(ob) + "\n" + self.add_block(nb))
        elif k == "rewrite":
            body = self.del_block(ob) + "\n" + self.add_block(nb)
        elif k == "del":
            body = self.del_block(ob)
        elif k == "add":
            body = self.add_block(nb)
        else:
            raise ValueError(k)
        body = self.inject_tag(body, self.tag(cid, extra), flt)
        return self.wrap_cb(body, flt)

    def old_section_number(self, ob, s):
        return s.get("old_secnum", "")


def old_section_numbers(old, segs, old_numbers):
    """Remember, for each old block, the number of its enclosing old (sub)section."""
    cur = ""
    by_i = {}
    for i, b in enumerate(old):
        h = bd.heading_of(b)
        if h:
            lab = bd.LABEL_RE.search(b)
            if lab and lab.group(1) in old_numbers:
                cur = old_numbers[lab.group(1)]
        by_i[i] = cur
    for s in segs:
        if s["i"] is not None:
            s["old_secnum"] = by_i.get(s["i"], "")


def new_section_labels(new, segs):
    cur = ""
    by_j = {}
    for j, b in enumerate(new):
        if bd.heading_of(b):
            lab = bd.LABEL_RE.search(b)
            cur = lab.group(1) if lab else ""
        by_j[j] = cur
    last = ""
    for s in segs:
        if s["j"] is not None and s["kind"] != "movedfrom":
            last = by_j.get(s["j"], "")
        s["new_seclabel"] = last


# --------------------------------------------------------------------------- bibliography
def parse_bib(bib):
    parts = re.split(r"(?m)^(?=\\bibitem)", bib)
    header, items = parts[0], {}
    order = []
    for p in parts[1:]:
        first, _, rest = p.partition("\n")
        m = bd.BIBITEM_RE.match(first)
        key = m.group(2)
        items[key] = (first, rest.strip())
        order.append(key)
    return header, items, order


def bib_sort_key(first):
    m = re.match(r"\\bibitem\[([^\]]*)\]", first)
    lab = m.group(1) if m else first
    lab = re.sub(r"\\['`^\"~]|[{}\\]", "", lab)
    return lab.lower()


def render_bib(old_bib, new_bib, r, cid_base):
    oh, oi, _ = parse_bib(old_bib)
    nh, ni, _ = parse_bib(new_bib)
    keys = sorted(set(oi) | set(ni), key=lambda k: bib_sort_key((ni.get(k) or oi.get(k))[0]))
    cid_del, cid_add, cid_fmt = cid_base + 1, cid_base + 2, cid_base + 3
    out, stats = [nh.strip()], {"del": [], "add": [], "fmt": []}
    for k in keys:
        if k in oi and k in ni:
            (of, ob), (nf, nb) = oi[k], ni[k]
            if bd.norm(ob) == bd.norm(nb):
                out.append(nf + "\n" + nb)
            else:
                stats["fmt"].append(k)
                out.append(nf + r.tag(cid_fmt) + "\n" + r.word_diff(ob, nb))
        elif k in oi:
            stats["del"].append(k)
            of, ob = oi[k]
            out.append(of + r.tag(cid_del) + "\n{\\color{DIFdelcolor}\\strikeThrough[DIFdelcolor]{" +
                       ob.replace("\n", " ") + "}}")
        else:
            stats["add"].append(k)
            nf, nb = ni[k]
            out.append(nf + r.tag(cid_add) + "\n\\highLight{" + nb.replace("\n", " ") + "}")
    return "\\begin{thebibliography}{99}\n" + "\n\n".join(out) + "\n\\end{thebibliography}\n", stats


# --------------------------------------------------------------------------- front matter
KIND_VI = {"edit": "Sửa", "rewrite": "Viết lại", "del": "Xóa", "add": "Thêm",
           "movedto": "Chuyển", "movedfrom": "Chuyển"}


def tex_escape(s):
    return (s.replace("\\", "\\textbackslash{}").replace("&", "\\&").replace("%", "\\%")
             .replace("#", "\\#").replace("_", "\\_").replace("$", "\\$"))


def front_matter(rows, review, notes, n_pages_hint):
    L = []
    L.append(r"\pagenumbering{roman}")
    L.append(r"\begin{center}{\Large\bfseries Bản đối chiếu thay đổi}\\[4pt]"
             r"{\large Bản nộp lần đầu (DTAP\_submission) $\rightarrow$ Bản sửa theo phản biện (DTAP Finally)}\end{center}")
    L.append(r"\section*{Cách đọc tài liệu này}")
    L.append(r"""\begin{itemize}[leftmargin=1.5em,itemsep=2pt]
\item \DIFadd{Nền vàng} = nội dung \textbf{mới thêm} trong bản sửa.
\item \DIFdel{Chữ đỏ gạch ngang} = nội dung của bản nộp lần đầu \textbf{đã bị xóa}.
\item Vạch dọc màu cam ở lề trái đánh dấu vùng có thay đổi; ô màu cam ở lề phải (ví dụ \colorbox{DIFtagcolor}{\sffamily\scriptsize\textbf{C12}} {\sffamily\scriptsize m5}) là \textbf{mã thay đổi} kèm \textbf{ý kiến phản biện} liên quan. Tra mã ở Bảng~A.
\item Bảng/hình \textbf{mới} nằm trong \colorbox{yellow!30}{khung nền vàng}; bảng/hình \textbf{cũ đã bị xóa hoặc thay} nằm trong \fcolorbox{DIFdelcolor}{white}{\color{DIFdelcolor}khung viền đỏ, chữ đỏ} (không gạch ngang để dễ đọc số liệu), có nhãn ``Bảng cũ $n$'' theo số của bản cũ.
\item Đoạn sửa ít được đánh dấu \emph{từng từ}. Đoạn viết lại gần như toàn bộ được hiển thị \emph{nguyên đoạn cũ} (đỏ gạch) rồi \emph{nguyên đoạn mới} (vàng) để dễ đọc.
\item Đoạn \textbf{di chuyển} chỉ hiện một lần, tại vị trí mới, và được so với bản cũ của chính nó; ở vị trí cũ chỉ còn một dòng đỏ nghiêng chỉ sang mã mới.
\item Ký hiệu ý kiến: \textbf{R1.1--R1.5} = 5 ý kiến chính của \textbf{Reviewer 1} (nằm trong email của Editor, xem \texttt{reviewer1\_comments.txt}); \textbf{M1--M4} = ý kiến chính (Major), \textbf{m1--m20} = ý kiến phụ (Minor) và \textbf{G} = nhận xét chung của \textbf{Reviewer 2} (file đính kèm \texttt{referee\_report.pdf}); \textbf{TG} = tác giả tự sửa, không do phản biện yêu cầu (vẫn phải nêu trong response letter).
\item Số mục, số công thức, số bảng trong phần thân theo \textbf{bản mới}. Trong phần bị xóa, số trong ngoặc như ``Mục cũ 2.2'', ``Bảng cũ 5'' là số của \textbf{bản cũ}. Số trích dẫn [n] trong file này được đánh lại vì danh mục tài liệu gộp cả tài liệu cũ đã xóa.
\end{itemize}""")
    # Table A: inventory
    L.append(r"\section*{Bảng A. Danh sách mọi thay đổi}")
    L.append(r"{\footnotesize\setlength{\tabcolsep}{3pt}\renewcommand{\arraystretch}{1.15}")
    L.append(r"\begin{longtable}{@{}>{\raggedright\arraybackslash}p{0.9cm}>{\raggedright\arraybackslash}p{0.7cm}"
             r">{\raggedright\arraybackslash}p{2.1cm}>{\raggedright\arraybackslash}p{1.25cm}"
             r">{\raggedright\arraybackslash}p{7.3cm}>{\raggedright\arraybackslash}p{1.6cm}@{}}")
    L.append(r"\toprule Mã & Tr. & Vị trí & Loại & Nội dung thay đổi & Ý kiến \\ \midrule \endfirsthead")
    L.append(r"\toprule Mã & Tr. & Vị trí & Loại & Nội dung thay đổi & Ý kiến \\ \midrule \endhead")
    L.append(r"\midrule \multicolumn{6}{r}{\emph{tiếp trang sau}}\\ \endfoot \bottomrule \endlastfoot")
    for r in rows:
        n = notes.get(str(r["cid"]), {})
        desc = n.get("vi", r"\textcolor{red}{(chưa mô tả)}")
        refs = ", ".join(n.get("refs", [])) or r"\textcolor{red}{?}"
        where = []
        if r.get("new_seclabel"):
            where.append(r"mới §\ref{%s}" % r["new_seclabel"])
        if r.get("old_secnum"):
            where.append(r"cũ §%s" % r["old_secnum"])
        if r.get("where"):
            where = [r["where"]]
        L.append(r"C%d & \pageref{chg:%d} & %s & %s & %s & %s \\" % (
            r["cid"], r["cid"], "; ".join(where) or "--", r["kind_vi"], desc, refs))
    L.append(r"\end{longtable}}")
    # Table B: reverse map
    inv = {}
    for r in rows:
        for ref in notes.get(str(r["cid"]), {}).get("refs", []):
            inv.setdefault(ref, []).append(r["cid"])
    L.append(r"\section*{Bảng B. Đối chiếu ngược: ý kiến phản biện $\rightarrow$ thay đổi}")
    L.append(r"Dùng bảng này khi viết response letter: mỗi ý kiến phải có ít nhất một thay đổi hoặc một lời giải thích.")
    L.append(r"{\footnotesize\setlength{\tabcolsep}{3pt}\renewcommand{\arraystretch}{1.15}")
    L.append(r"\begin{longtable}{@{}>{\raggedright\arraybackslash}p{0.9cm}>{\raggedright\arraybackslash}p{7.6cm}"
             r">{\raggedright\arraybackslash}p{5.3cm}@{}}")
    L.append(r"\toprule Ý kiến & Nội dung (tóm tắt) & Thay đổi liên quan \\ \midrule \endfirsthead")
    L.append(r"\toprule Ý kiến & Nội dung (tóm tắt) & Thay đổi liên quan \\ \midrule \endhead")
    L.append(r"\bottomrule \endlastfoot")
    for c in review:
        ids = inv.get(c["id"], [])
        txt = ", ".join(r"C%d\,(tr.\,\pageref{chg:%d})" % (i, i) for i in ids) if ids else \
            r"\textcolor{red}{\textbf{Chưa có thay đổi nào}} " + tex_escape(c.get("none", ""))
        L.append(r"%s & %s & %s \\" % (c["id"], c["vi"], txt))
    L.append(r"\end{longtable}}")
    # longtable steps the table counter even without a caption
    L.append(r"\clearpage\pagenumbering{arabic}\setcounter{table}{0}")
    return "\n".join(L)


# --------------------------------------------------------------------------- driver
def assemble(old_text, new_text, old, new, segs, ncid, oldparts, newparts):
    build = bd.BUILD
    if build.exists():
        shutil.rmtree(build)
    build.mkdir(parents=True)
    for d in (bd.OLD_DIR, bd.NEW_DIR):
        for f in d.iterdir():
            if f.suffix in (".png", ".cls", ".eps", ".jpg"):
                shutil.copy(f, build / f.name)
    old_labels = old_label_table(build)
    with open(build / "oldlabels.tex", "w", encoding="utf-8") as fh:
        for k, (num, page) in old_labels.items():
            fh.write("\\newlabel{old:%s}{{%s}{%s}}\n" % (k, num, page))
    new_labels = set(bd.LABEL_RE.findall(new_text))
    notes = json.loads(bd.NOTES.read_text(encoding="utf-8")) if bd.NOTES.exists() else {}
    review = json.loads(bd.REVIEW.read_text(encoding="utf-8")) if bd.REVIEW.exists() else []
    old_section_numbers(old, segs, {k: v[0] for k, v in old_labels.items()})
    new_section_labels(new, segs)

    r = Renderer(old_labels, new_labels, notes, build / "frag")
    body = [r.render(s, old, new) for s in segs]
    (old_pre, old_bib), (new_pre, new_bib) = oldparts, newparts
    bib, bibstats = render_bib(old_bib, new_bib, r, ncid)

    # inventory rows in id order
    rows, seen = [], {}
    for s in segs:
        if s["kind"] == "same":
            continue
        cid = s["cid"]
        if cid in seen:
            if s["kind"] != "movedfrom":
                seen[cid]["kinds"].add(s["kind"])
            continue
        row = {"cid": cid, "kinds": {s["kind"]}, "new_seclabel": s.get("new_seclabel", ""),
               "old_secnum": s.get("old_secnum", "")}
        seen[cid] = row
        rows.append(row)
    for row in rows:
        ks = row["kinds"]
        if "movedto" in ks or "movedfrom" in ks:
            row["kind_vi"] = "Chuyển + sửa"
        else:
            row["kind_vi"] = " + ".join(KIND_VI[k] for k in ("rewrite", "edit", "del", "add") if k in ks)
        if ks == {"add"}:
            row["old_secnum"] = ""
        if ks == {"del"}:
            row["new_seclabel"] = ""
    rows.sort(key=lambda x: x["cid"])
    for off, (name, vi) in enumerate((("del", "Xóa"), ("add", "Thêm"), ("fmt", "Sửa"))):
        if bibstats[name]:
            rows.append({"cid": ncid + 1 + off, "kind_vi": vi, "where": "Tài liệu tham khảo"})

    missing = [row["cid"] for row in rows if str(row["cid"]) not in notes]
    preamble = new_pre + DIFF_PREAMBLE + "\\AtBeginDocument{\\input{oldlabels.tex}}\n"
    doc = (preamble + "\\begin{document}\n" + front_matter(rows, review, notes, 0) + "\n" +
           "\n\n".join(body) + "\n\n" + bib + "\n\\end{document}\n")
    (build / "diff.tex").write_text(doc, encoding="utf-8")
    for _ in range(3):
        res = subprocess.run(["lualatex", "-interaction=nonstopmode", "diff.tex"], cwd=build,
                             capture_output=True, text=True, errors="replace", timeout=900)
    log = (build / "diff.log").read_text(encoding="utf-8", errors="replace")
    errors = [l for l in log.split("\n") if l.startswith("!")]
    shutil.copy(build / "diff.pdf", bd.OUT_PDF)
    print("latexdiff fragments:", r.n_latexdiff)
    print("bibliography: removed %d, added %d, reformatted %d" % tuple(len(bibstats[k]) for k in ("del", "add", "fmt")))
    print("removed refs:", ", ".join(bibstats["del"]))
    print("added refs:", ", ".join(bibstats["add"]))
    print("changes without a note:", missing if missing else "none")
    print("LaTeX errors:", len(errors))
    for e in errors[:20]:
        print("  ", e)
    undefined = sorted(set(re.findall(r"Reference `([^']*)' on page", log)))
    print("undefined references:", undefined)
    print("undefined citations:", sorted(set(re.findall(r"Citation `([^']*)'", log))))
