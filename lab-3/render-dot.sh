#!/usr/bin/env bash
# Render a Graphviz (.dot / .gv) diagram to SVG (white background) then to PDF.
# Usage: ./render-dot.sh <file.dot>
set -euo pipefail

in="${1:?Usage: render-dot.sh <file.dot>}"
base="${in%.*}"

dot -Tsvg -Gbgcolor=white -o "$base.svg" "$in"
rsvg-convert -f pdf -o "$base.pdf" "$base.svg"

echo "Wrote $base.svg and $base.pdf"