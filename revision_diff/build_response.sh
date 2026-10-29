#!/usr/bin/env bash
# Build response_letter_draft.pdf. The revised manuscript is compiled first so that the
# letter can read its section, table, equation and page numbers (package xr).
set -euo pipefail
cd "$(dirname "$0")"
mkdir -p newref
cp "../DTAP Finally/main_document.tex" newref/new.tex
cp "../DTAP Finally/interact.cls" newref/
(cd newref && for i in 1 2; do pdflatex -interaction=nonstopmode new.tex >/dev/null; done)
for i in 1 2; do lualatex -interaction=nonstopmode response_letter_draft.tex >/dev/null || true; done
grep -E "^!|undefined" response_letter_draft.log || echo "response_letter_draft.pdf: no errors, no undefined references"
