#!/usr/bin/env bash
# Render a mermaid (.mmd) diagram to SVG (light theme, white background) then to PDF.
# Usage: ./render-mermaid.sh <file.mmd>
set -euo pipefail

in="${1:?Usage: render-mermaid.sh <file.mmd>}"
base="${in%.*}"

mmdc --input "$in" --output "$base.svg" --theme default --backgroundColor white
rsvg-convert -f pdf -o "$base.pdf" "$base.svg"

echo "Wrote $base.svg and $base.pdf"
