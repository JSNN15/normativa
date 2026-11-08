#!/usr/bin/env bash
# Descarga los 19 pliegos RIC desde sec.cl y extrae su texto (requiere curl y pdftotext de poppler).
set -euo pipefail
cd "$(dirname "$0")"
mkdir -p raw txt out
while read -r u; do
  f="raw/$(basename "$u" | python3 -c 'import sys,urllib.parse;print(urllib.parse.unquote(sys.stdin.read().strip()))')"
  [ -f "$f" ] || curl -sfL -A 'Mozilla/5.0' -o "$f" "$u"
  pdftotext -layout "$f" "txt/$(basename "$f" .pdf).txt"
done < raw/urls.txt
echo "Listo: $(ls txt | wc -l) pliegos en txt/"
