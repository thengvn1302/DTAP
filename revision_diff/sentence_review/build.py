#!/usr/bin/env python3
"""Build the sentence review of DTAP Finally v2/main_document.tex.

Run extract.py first (sentences.json). Writes sentence_review.md and sentence_review.pdf:
one row per sentence, three columns (sentence | issue? | keep / how to fix)."""
import json, re, shutil, subprocess
from pathlib import Path
from verdicts import V, GLOBAL

HERE = Path(__file__).resolve().parent
S = json.load(open(HERE / "sentences.json", encoding="utf-8"))
NAMES = {"A": "mơ hồ", "B": "tối nghĩa", "C": "thiếu chặt chẽ", "D": "liên kết",
         "E": "câu dài/nặng", "F": "thừa/lan man"}
LEVEL = {1: "phải sửa", 2: "nên sửa", 3: "tùy chọn"}

# attach verdicts
verdict = {}
for prefix, code, lvl, fix in V:
    hits = [x["id"] for x in S if x["text"].startswith(prefix)]
    assert len(hits) == 1, (prefix, hits)
    verdict[hits[0]] = (code, lvl, fix)

# ---------------------------------------------------------------- helpers
def md_math(s):
    s = s.replace("\\R", "\\mathbb{R}").replace("\\cvx", "\\mathrm{cvx}").replace("\\ps", "\\mathrm{ps}")
    s = re.sub(r"\\norm\{([^{}]*)\}", r"\\|\1\\|", s)
    s = re.sub(r"\\abs\{([^{}]*)\}", r"|\1|", s)
    s = re.sub(r"\\inner\{([^{}]*)\}\{([^{}]*)\}", r"\\langle \1,\2\\rangle", s)
    return s.replace("|", "\\|") if False else s

def md_cell(s):
    return md_math(s.replace("\\%", "%")).replace("|", "\\vert ").replace("\n", " ")

def tex_text(s):
    out = []
    for p in re.split(r"(\$[^$]*\$)", s):
        if p.startswith("$") and p.endswith("$") and len(p) > 1:
            out.append(p); continue
        p = p.replace("\\", "\\textbackslash{}")
        for a, b in (("&", "\\&"), ("%", "\\%"), ("#", "\\#"), ("_", "\\_"), ("{", "\\{"),
                     ("}", "\\}"), ("^", "\\textasciicircum{}"), ("~", "\\textasciitilde{}")):
            p = p.replace(a, b)
        p = p.replace("\\textbackslash\\{\\}", "\\textbackslash{}")
        p = p.replace("\\textasciicircum\\{\\}", "\\textasciicircum{}").replace("\\textasciitilde\\{\\}", "\\textasciitilde{}")
        out.append(p)
    return "".join(out)

# ---------------------------------------------------------------- statistics
n = len(S)
flag = {1: 0, 2: 0, 3: 0}
for c, l, _ in verdict.values():
    flag[l] += 1
by_code = {k: sum(1 for c, _, _ in verdict.values() if k in c) for k in NAMES}
long_units = sum(1 for x in S if x["words"] > 30)
split_long = sum(1 for c, l, _ in verdict.values() if "E" in c and l <= 2)

CRIT = [
 ("A", "Mơ hồ (đọc ra hai nghĩa)", "Đại từ hay chủ ngữ không rõ; phạm vi lượng từ không rõ; bổ ngữ treo; câu dễ đọc nhầm cấu trúc."),
 ("B", "Tối nghĩa (một nghĩa nhưng phải đoán)", "Thuật ngữ, ký hiệu dùng trước khi định nghĩa; biệt ngữ, ẩn dụ; chồng danh từ; nhắc tới quy trình hay tên gọi chưa giới thiệu."),
 ("C", "Thiếu chặt chẽ", "Khẳng định rộng hơn điều đã chứng minh; thiếu giả thiết hay lượng từ; một ký hiệu hai nghĩa; một khái niệm nhiều tên."),
 ("D", "Liên kết", "Câu hoặc đoạn không nối với phần trước; từ nối sai logic; một ý lặp ở nhiều nơi; nội dung đặt sai chỗ."),
 ("E", "Câu dài hoặc nặng", "Trên 30 từ, hoặc từ 3 mệnh đề trở lên, hoặc nhiều phủ định chồng nhau; hoặc chuỗi câu quá ngắn rời rạc."),
 ("F", "Thừa / lan man", "Phép thử xóa: bỏ câu mà không mất thông tin thì câu thừa; câu lệch mục đích của đoạn, lặp điều đã nói, hoặc rào đón."),
]
INTRO_MD = f"""# Rà soát từng câu — `DTAP Finally v2/main_document.tex`

Mục tiêu: bài dễ đọc, văn phong phù hợp một bài báo toán tối ưu, mỗi câu chặt chẽ, tường minh, ngắn gọn. **Chưa sửa gì trong bài**; bảng này chỉ ghi kết quả rà soát.

## Tiêu chí

Một câu đạt yêu cầu khi người đọc chỉ hiểu được **một nghĩa**, hiểu được **mà không phải đoán**, nội dung **đúng như toán học đã chứng minh**, câu **nối được** với câu trước và sau, và **không có chữ thừa**. Mỗi lỗi được gán một hoặc nhiều mã:

| Mã | Loại | Dấu hiệu |
|---|---|---|
""" + "".join(f"| **{c}** | {t} | {d} |\n" for c, t, d in CRIT) + f"""
**Súc tích** nghĩa là mỗi câu nói một ý cần thiết, chính xác, bằng ít chữ nhất mà người đọc vẫn không phải đoán. Nén quá mức thành biệt ngữ là lỗi B, không phải súc tích.

Mức độ: **[1] phải sửa** (sai hoặc có thể làm phản biện nghi ngờ kết quả), **[2] nên sửa** (gây khó hiểu), **[3] tùy chọn** (văn phong).

## Kết quả tổng quát

- Đã rà **{n} câu/đơn vị** (gồm tiêu đề, chú thích bảng, các bước của Thuật toán 1; không gồm phần thân bảng số liệu và danh mục tài liệu tham khảo).
- **{n - len(verdict)} câu không cần sửa.**
- **{len(verdict)} câu có vướng lỗi:** {flag[1]} câu mức [1], {flag[2]} câu mức [2], {flag[3]} câu mức [3].
- Theo loại (một câu có thể có nhiều mã): """ + ", ".join(f"{k} {NAMES[k]}: {by_code[k]}" for k in NAMES) + f""".
- Câu trên 30 từ: {long_units}; trong đó {split_long} câu được đề nghị tách (mức [2]). Các câu dài còn lại là danh sách tham số hoặc chứa công thức, có thể giữ.
- Phần chứng minh (Mục 3.6–3.9) đạt yêu cầu: các bước đều có lý do, lượng từ rõ, không có câu thừa.
- Hai câu cần lưu ý nhất: câu về công thức (8) "whose maximizers…" (mức [1], đọc ra nghĩa sai) và câu Introduction "the proof uses this weight only to…" (mức [2], chưa chính xác; câu này đang được letter R1.1 trích nguyên văn).

## Vấn đề xuyên suốt cả bài

| Mã | Mức | Vấn đề và cách sửa |
|---|---|---|
""" + "".join(f"| {c} | [{l}] | {t} |\n" for c, l, t in GLOBAL) + """
## Bảng rà soát từng câu

Cột 1 là câu nguyên văn (số trong ngoặc vuông là thứ tự câu; [công thức (n)] là công thức hiển thị). Cột 2 ghi có lỗi hay không, kèm mã và mức. Cột 3 ghi "Giữ nguyên" hoặc cách sửa cụ thể.

"""

def build_md():
    out = [INTRO_MD]
    sec = None
    for x in S:
        if x["sec"] == "Tiêu đề":
            out.append(f"\n### {x['text']}\n\n| Câu | Có lỗi không? | Không cần sửa / Cách sửa |\n|---|---|---|\n")
            if x["id"] in verdict:
                c, l, f = verdict[x["id"]]
                out.append(f"| [{x['id']}] **(tiêu đề)** {md_cell(x['text'])} | **Có** — {c} [{l}] | {md_cell(f)} |\n")
            continue
        if sec is None and x["sec"] == "Abstract" and not out[-1].startswith("\n### Abstract"):
            out.append("\n### Abstract và từ khóa\n\n| Câu | Có lỗi không? | Không cần sửa / Cách sửa |\n|---|---|---|\n")
            sec = "Abstract"
        if x["id"] in verdict:
            c, l, f = verdict[x["id"]]
            names = ", ".join(NAMES[ch] for ch in c)
            out.append(f"| [{x['id']}] {md_cell(x['text'])} | **Có** — {c} [{l}] ({names}, {LEVEL[l]}) | {md_cell(f)} |\n")
        else:
            out.append(f"| [{x['id']}] {md_cell(x['text'])} | Không | Giữ nguyên |\n")
    (HERE / "sentence_review.md").write_text("".join(out), encoding="utf-8")

def build_pdf():
    src = (HERE.parents[1] / "DTAP Finally v2" / "main_document.tex").read_text(encoding="utf-8")
    macros = "\n".join(l for l in src.split("\n") if l.startswith(("\\newcommand{\\R}", "\\newcommand{\\N}",
             "\\newcommand{\\norm}", "\\newcommand{\\abs}", "\\newcommand{\\inner}", "\\DeclareMathOperator",
             "\\newcommand{\\cvx}", "\\newcommand{\\ps}", "\\newcommand{\\dtap}")))
    md = (HERE / "sentence_review.md").read_text(encoding="utf-8")
    head_md = md[:md.index("## Bảng rà soát từng câu")]
    def para(t):  # very small markdown -> latex for the header part
        t = tex_text(t)
        t = re.sub(r"\*\*(.+?)\*\*", r"\\textbf{\1}", t)
        t = re.sub(r"`([^`]*)`", r"\\texttt{\1}", t)
        return t
    L = [r"""\documentclass[10pt]{article}
\usepackage[a4paper,landscape,margin=1.3cm]{geometry}
\usepackage{fontspec}
\setmainfont{DejaVu Serif}[Scale=0.92]
\usepackage{amsmath,amssymb}
\usepackage{xcolor,colortbl,longtable,array,booktabs}
\setlength{\parindent}{0pt}\setlength{\parskip}{4pt}
\definecolor{bad}{HTML}{FDECEA}\definecolor{hd}{HTML}{E6E9EF}
""", macros, r"""
\begin{document}
{\Large\bfseries Rà soát từng câu --- \texttt{DTAP Finally v2/main\_document.tex}}\par
"""]
    for block in head_md.split("\n\n")[1:]:
        b = block.strip()
        if not b: continue
        if b.startswith("## "):
            L.append("\\subsection*{" + para(b[3:]) + "}\n"); continue
        if b.startswith("|"):
            rows = [r for r in b.split("\n") if r.startswith("|") and not r.startswith("|---")]
            ncol = len(rows[0].strip("|").split("|"))
            spec = {3: "p{0.06\\linewidth}p{0.22\\linewidth}p{0.66\\linewidth}"}[ncol]
            L.append("\\begin{longtable}{" + spec + "}\\toprule\n")
            for k, r in enumerate(rows):
                cells = [para(c.strip()) for c in r.strip().strip("|").split("|")]
                L.append(" & ".join(cells) + "\\\\" + ("\\midrule\n" if k == 0 else "\n"))
            L.append("\\bottomrule\\end{longtable}\n"); continue
        if b.startswith("- "):
            L.append("\\begin{itemize}\n" + "".join("\\item " + para(i[2:]) + "\n" for i in b.split("\n") if i.startswith("- ")) + "\\end{itemize}\n"); continue
        L.append(para(b) + "\n\n")
    L.append(r"""\subsection*{Bảng rà soát từng câu}
Cột 1: câu nguyên văn (số trong ngoặc vuông là thứ tự câu; [công thức (n)] là công thức hiển thị). Cột 2: có lỗi hay không, mã và mức. Cột 3: ``Giữ nguyên'' hoặc cách sửa cụ thể. Hàng tô hồng là câu có lỗi.

{\small
\begin{longtable}{p{0.47\linewidth}p{0.12\linewidth}p{0.36\linewidth}}
\toprule \textbf{Câu} & \textbf{Có lỗi không?} & \textbf{Không cần sửa / Cách sửa}\\\midrule\endhead
\bottomrule\endfoot
""")
    for x in S:
        txt = x["text"]
        cell1 = ("\\textbf{" + txt + "}") if x["sec"] == "Tiêu đề" else txt
        cell1 = "{\\color{gray}[" + str(x["id"]) + "]} " + cell1
        if x["id"] in verdict:
            c, l, f = verdict[x["id"]]
            L.append("\\rowcolor{bad}" + cell1 + " & \\textbf{Có} --- " + c + " [" + str(l) + "] & " + tex_text(f) + "\\\\\n")
        else:
            L.append(cell1 + " & Không & Giữ nguyên\\\\\n")
    L.append("\\end{longtable}}\n\\end{document}\n")
    work = HERE / "build"
    if work.exists(): shutil.rmtree(work)
    work.mkdir()
    (work / "r.tex").write_text("".join(L), encoding="utf-8")
    for _ in range(3):
        subprocess.run(["lualatex", "-interaction=nonstopmode", "r.tex"], cwd=work, capture_output=True)
    log = (work / "r.log").read_text(errors="replace")
    errs = [l for l in log.split("\n") if l.startswith("!")]
    miss = sorted(set(re.findall(r"Missing character: There is no (.) ", log)))
    print("LaTeX errors:", len(errs), errs[:3], "missing glyphs:", miss)
    shutil.copy(work / "r.pdf", HERE / "sentence_review.pdf")
    if not errs: shutil.rmtree(work)

build_md()
build_pdf()
print(f"{n} units, {len(verdict)} flagged: {flag}; codes {by_code}; >30 words {long_units}, split {split_long}")
