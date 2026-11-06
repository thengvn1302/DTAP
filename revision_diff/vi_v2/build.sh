#!/usr/bin/env bash
# Build the Vietnamese review translations (not for submission). Needs lualatex.
set -euo pipefail
cd "$(dirname "$0")"
cat parts/0*.tex > main_document_vi.tex
cp "../../DTAP Finally v2/interact.cls" .
for i in 1 2 3; do lualatex -interaction=nonstopmode main_document_vi.tex >/dev/null || true; done
for i in 1 2; do lualatex -interaction=nonstopmode response_letter_vi.tex >/dev/null || true; done
grep -E "^!" main_document_vi.log response_letter_vi.log || echo "no LaTeX errors"
rm -f *.aux *.log *.out interact.cls
