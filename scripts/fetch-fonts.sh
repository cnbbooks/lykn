#!/usr/bin/env bash
# ============================================================================
# fetch-fonts.sh — download the EPUB fonts from Google Fonts' open-source repo
#
# Usage (from the book root):
#   ./scripts/fetch-fonts.sh
#
# Downloads into theme/fonts/, which mdbook-epub will package into the EPUB.
# Safe to re-run: skips files that already exist.
#
# All three families are SIL Open Font License 1.1 — free to embed
# in both HTML and EPUB distributions.
# ============================================================================

set -euo pipefail

FONT_DIR="theme/fonts"
mkdir -p "$FONT_DIR"

# Google's fonts repo uses raw.githubusercontent.com for direct file access.
GF_RAW="https://raw.githubusercontent.com/google/fonts/main"

# Plex Mono lives in the IBM repo rather than Google's.
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
fetch "$GF_RAW/ofl/redhatdisplay/RedHatDisplay%5Bwght%5D.ttf"        "RedHatDisplay-VariableFont_wght.ttf"
fetch "$GF_RAW/ofl/redhatdisplay/RedHatDisplay-Italic%5Bwght%5D.ttf" "RedHatDisplay-Italic-VariableFont_wght.ttf"

echo "==> Literata (ofl/literata)"
fetch "$GF_RAW/ofl/literata/Literata%5Bopsz,wght%5D.ttf"        "Literata-VariableFont_opsz,wght.ttf"
fetch "$GF_RAW/ofl/literata/Literata-Italic%5Bopsz,wght%5D.ttf" "Literata-Italic-VariableFont_opsz,wght.ttf"

echo "==> IBM Plex Mono (IBM/plex)"
fetch "$PLEX_RAW/IBMPlexMono-Regular.ttf"  "IBMPlexMono-Regular.ttf"
fetch "$PLEX_RAW/IBMPlexMono-Italic.ttf"   "IBMPlexMono-Italic.ttf"
fetch "$PLEX_RAW/IBMPlexMono-Medium.ttf"   "IBMPlexMono-Medium.ttf"
fetch "$PLEX_RAW/IBMPlexMono-SemiBold.ttf" "IBMPlexMono-SemiBold.ttf"

echo ""
echo "Done. Fonts in $FONT_DIR/"
ls -lh "$FONT_DIR"
