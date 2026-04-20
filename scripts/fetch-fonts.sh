#!/usr/bin/env bash
# ============================================================================
# fetch-fonts.sh — download the EPUB fonts from their upstream repos
#
# Usage (from the book root):
#   ./scripts/fetch-fonts.sh
#
# Downloads into theme/fonts/, which mdbook-epub packages into the EPUB.
# Safe to re-run: skips files that already exist.
#
# NB: filenames are chosen to AVOID commas. Google Fonts publishes variable
# fonts with names like 'Literata[opsz,wght].ttf', but commas in EPUB filenames
# get URL-encoded inconsistently — the packaged file has a literal comma but
# the CSS reference ends up URL-encoded, which means Calibre (and strict EPUB
# readers) can't resolve them. We strip the axis list from the filename.
#
# All three families are SIL Open Font License 1.1 — free to embed
# in both HTML and EPUB distributions.
# ============================================================================

set -euo pipefail

FONT_DIR="theme/fonts"
mkdir -p "$FONT_DIR"

GF_RAW="https://raw.githubusercontent.com/google/fonts/main"
PLEX_RAW="https://raw.githubusercontent.com/IBM/plex/master/packages/plex-mono/fonts/complete/ttf"

fetch() {
  local url="$1"
  local dest="$FONT_DIR/$2"
  if [[ -f "$dest" ]]; then
    echo "  [skip] $2 (already present)"
    return 0
  fi
  echo "  [get]  $2"
  curl -sSfL -o "$dest" "$url"
}

echo "==> Red Hat Display (ofl/redhatdisplay)"
fetch "$GF_RAW/ofl/redhatdisplay/RedHatDisplay%5Bwght%5D.ttf"        "RedHatDisplay-Variable.ttf"
fetch "$GF_RAW/ofl/redhatdisplay/RedHatDisplay-Italic%5Bwght%5D.ttf" "RedHatDisplay-Italic-Variable.ttf"

echo "==> Literata (ofl/literata)"
fetch "$GF_RAW/ofl/literata/Literata%5Bopsz,wght%5D.ttf"        "Literata-Variable.ttf"
fetch "$GF_RAW/ofl/literata/Literata-Italic%5Bopsz,wght%5D.ttf" "Literata-Italic-Variable.ttf"

echo "==> IBM Plex Mono (IBM/plex)"
fetch "$PLEX_RAW/IBMPlexMono-Regular.ttf"  "IBMPlexMono-Regular.ttf"
fetch "$PLEX_RAW/IBMPlexMono-Italic.ttf"   "IBMPlexMono-Italic.ttf"
fetch "$PLEX_RAW/IBMPlexMono-Medium.ttf"   "IBMPlexMono-Medium.ttf"
fetch "$PLEX_RAW/IBMPlexMono-SemiBold.ttf" "IBMPlexMono-SemiBold.ttf"

echo ""
echo "Done. Fonts in $FONT_DIR/"
ls -lh "$FONT_DIR"
