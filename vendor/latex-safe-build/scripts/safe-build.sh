#!/bin/sh
# safe-build.sh -- compile a LaTeX tree in an isolated scratch copy so the
# build can never corrupt the working tree.
#
# Usage: safe-build.sh [source-dir] [main-tex] [engine-flag]
#   source-dir   LaTeX project root                (default: .)
#   main-tex     root .tex file                    (default: auto-detect)
#   engine-flag  -pdf | -xelatex | -lualatex       (default: auto-detect)
#
# Optional config file <source-dir>/.latex-safe-build.conf, KEY=VALUE lines:
#   MAIN=thesis.tex        root file (overrides auto-detect, not the CLI arg)
#   ENGINE=-xelatex        engine flag
#   SHELL_ESCAPE=1         force -shell-escape on (auto-detected otherwise)
#   EXTRA_ARGS=...         appended to the latexmk call
#   TEXT_START=...         first-text-page marker for the page-count report
#   TEXT_END=...           after-last-text-page marker
#
# Exit codes: 0 ok, 1 build/setup error, 2 refused (another build running)
set -eu

# ---------------------------------------------------------------- helpers --
die()  { printf 'error: %s\n' "$*" >&2; exit 1; }
# Read KEY=VALUE from the config file without executing it.
conf() { [ -f "$CONF" ] && sed -n "s/^[[:space:]]*$1=//p" "$CONF" | head -1 || true; }

# ------------------------------------------------------------ dependencies --
command -v latexmk >/dev/null 2>&1 \
  || PATH="/Library/TeX/texbin:/usr/local/texlive/bin:$PATH"   # MacTeX default
command -v latexmk >/dev/null 2>&1 \
  || die "latexmk not found. Install a TeX distribution (TeX Live / MacTeX)."
command -v rsync >/dev/null 2>&1 \
  || die "rsync not found. It ships with macOS and every major Linux distro."

# -------------------------------------------- capture args before any set -- --
ARG_SRC="${1:-.}"
ARG_MAIN="${2:-}"
ARG_ENGINE="${3:-}"

# ------------------------------------------------------------- source dir --
SRC=$(cd "$ARG_SRC" 2>/dev/null && pwd) || die "source dir '$ARG_SRC' not found"
CONF="$SRC/.latex-safe-build.conf"

# --------------------------------------------------------- main-tex detect --
MAIN="$ARG_MAIN"
MAIN_WHY="given"
[ -n "$MAIN" ] || { MAIN=$(conf MAIN); MAIN_WHY="config"; }
if [ -z "$MAIN" ] && [ -f "$SRC/.latexmkrc" ]; then
  MAIN=$(sed -n "s/.*@default_files[[:space:]]*=[[:space:]]*(*['\"]\([^'\"]*\)['\"].*/\1/p" \
         "$SRC/.latexmkrc" | head -1)
  MAIN_WHY=".latexmkrc"
fi
if [ -z "$MAIN" ]; then
  CANDIDATES=""
  for f in "$SRC"/*.tex; do
    [ -f "$f" ] || continue
    if grep -lq '\\documentclass' "$f" && grep -lq '\\begin{document}' "$f"; then
      CANDIDATES="$CANDIDATES ${f##*/}"
    fi
  done
  # shellcheck disable=SC2086  # word splitting is the point; no-space names only
  set -- $CANDIDATES
  case $# in
    0) die "no root .tex found in $SRC (need \\documentclass + \\begin{document})" ;;
    1) MAIN=$1 ;;
    *) for pref in main.tex thesis.tex report.tex paper.tex; do
         for c in "$@"; do [ "$c" = "$pref" ] && MAIN=$pref; done
       done
       [ -n "$MAIN" ] || die "several root files found ($CANDIDATES ); pass one: safe-build.sh $SRC <file.tex>" ;;
  esac
  MAIN_WHY="auto-detected"
fi
[ -f "$SRC/$MAIN" ] || die "$SRC/$MAIN not found"
BASE="${MAIN%.tex}"

# ----------------------------------------------------------- engine detect --
ENGINE="$ARG_ENGINE"
ENGINE_WHY="given"
[ -n "$ENGINE" ] || { ENGINE=$(conf ENGINE); ENGINE_WHY="config"; }
if [ -z "$ENGINE" ]; then
  # TeXShop/TeXstudio magic comment in the first lines of the root file.
  MAGIC=$(head -5 "$SRC/$MAIN" \
    | sed -n 's/^%[[:space:]]*!*[Tt][Ee][Xx][[:space:]]*\([Tt][Ss]-\)*program[[:space:]]*=[[:space:]]*\([a-zA-Z]*\).*/\2/p' \
    | head -1 | tr '[:upper:]' '[:lower:]')
  case "$MAGIC" in
    xelatex)  ENGINE="-xelatex";  ENGINE_WHY="magic comment" ;;
    lualatex) ENGINE="-lualatex"; ENGINE_WHY="magic comment" ;;
    pdflatex) ENGINE="-pdf";      ENGINE_WHY="magic comment" ;;
  esac
fi
if [ -z "$ENGINE" ]; then
  # fontspec and friends require a unicode engine.
  if grep -rqE --include='*.tex' --include='*.sty' \
       '\\usepackage(\[[^]]*\])?\{(fontspec|polyglossia|unicode-math)' "$SRC" 2>/dev/null; then
    if grep -rqE --include='*.tex' 'luacode|directlua' "$SRC" 2>/dev/null; then
      ENGINE="-lualatex"; ENGINE_WHY="luacode detected"
    else
      ENGINE="-xelatex"; ENGINE_WHY="fontspec detected"
    fi
  else
    ENGINE="-pdf"; ENGINE_WHY="default (pdflatex)"
  fi
fi

# ----------------------------------------------------- shell-escape detect --
EXTRAS=""
EXTRAS_WHY=""
if [ "$(conf SHELL_ESCAPE)" = "1" ]; then
  EXTRAS="-shell-escape"; EXTRAS_WHY="config"
elif grep -rqE --include='*.tex' --include='*.sty' --include='*.cls' \
       '\\usepackage(\[[^]]*\])?\{(minted|svg)\}' "$SRC" 2>/dev/null; then
  EXTRAS="-shell-escape"; EXTRAS_WHY="minted/svg detected"
fi
EXTRA_ARGS=$(conf EXTRA_ARGS)

# ------------------------------------------------- assets outside the tree --
if grep -rqE --include='*.tex' '\\(includegraphics|input|include)(\[[^]]*\])?\{(/|\.\./)' "$SRC" 2>/dev/null; then
  echo "warning: the document references files OUTSIDE $SRC (absolute or ../ paths)." >&2
  echo "warning: those are not copied into the isolated build and may fail to resolve." >&2
fi

# -------------------------------------------------------------- race guard --
if pgrep -f "latexmk.*$BASE" >/dev/null 2>&1; then
  echo "error: a latexmk for '$BASE' is already running (see: pgrep -fl latexmk)." >&2
  echo "error: overlapping builds corrupt intermediates; wait for it or kill it." >&2
  exit 2
fi

# ------------------------------------------------------------ scratch copy --
HASH=$(printf '%s' "$SRC" | cksum | cut -d' ' -f1)
SCRATCH="${TMPDIR:-/tmp}/latex-safe-build"
BLD="$SCRATCH/$(basename "$SRC")-$HASH"
LOG="$BLD.log"

cat <<BANNER
== latex-safe-build ==========================================
 source : $SRC
 main   : $MAIN ($MAIN_WHY)
 engine : $ENGINE ($ENGINE_WHY)${EXTRAS:+
 extras : $EXTRAS ($EXTRAS_WHY)}${EXTRA_ARGS:+
 args   : $EXTRA_ARGS (config)}
 build  : $BLD
 output : $SRC/$BASE.pdf
==============================================================
BANNER

rm -rf "$BLD"
mkdir -p "$BLD"
# Copy everything except regenerable artifacts. Never exclude *.pdf globally:
# vector figures are PDFs and they are content, not artifacts.
rsync -a \
  --exclude="/$BASE.pdf" \
  --exclude='*.aux' --exclude='*.bcf' --exclude='*.bbl' --exclude='*.blg' \
  --exclude='*.fdb_latexmk' --exclude='*.fls' --exclude='*.synctex.gz' \
  --exclude='*.toc' --exclude='*.lof' --exclude='*.lot' --exclude='*.out' \
  --exclude='*.run.xml' --exclude='.git' \
  "$SRC/" "$BLD/"

# ------------------------------------------------------------------- build --
cd "$BLD"
# shellcheck disable=SC2086  # ENGINE/EXTRAS are single flags by construction
if ! latexmk $ENGINE $EXTRAS $EXTRA_ARGS -interaction=nonstopmode \
       -halt-on-error -file-line-error "$MAIN" >"$LOG" 2>&1; then
  echo "BUILD FAILED. Triage (full log: $LOG):"
  echo "--------------------------------------------------------------"
  # First TeX error blocks. With -file-line-error, errors print as
  # 'file:line: message' instead of the classic '! message'; match both.
  grep -E -A2 '^(!|\./[^ :]+:[0-9]+:|[^ :]+\.tex:[0-9]+:)' "$BASE.log" 2>/dev/null | head -24
  # latexmk/biber problems that never reach the TeX log.
  grep -iE 'biber.*error|bibtex.*error|failed to find|shell escape' "$LOG" | head -6
  # Actionable hints for the two most common causes.
  if grep -q "not found" "$BASE.log" 2>/dev/null; then
    echo "hint: a 'File ... not found' above means a missing package (tlmgr install <name>) or a missing figure/input path."
  fi
  if grep -qi 'shell.escape' "$BASE.log" "$LOG" 2>/dev/null; then
    echo "hint: this document needs -shell-escape; set SHELL_ESCAPE=1 in .latex-safe-build.conf."
  fi
  exit 1
fi

cp "$BLD/$BASE.pdf" "$SRC/$BASE.pdf"
echo "BUILD OK -> $SRC/$BASE.pdf"

# ----------------------------------------------------------------- reports --
echo "--- unresolved references ---"
REFS=$(grep -iE "undefined|multiply defined" "$BLD/$BASE.log" 2>/dev/null \
  | grep -ivE "rerun|font|shape" | head -30 || true)
if [ -n "$REFS" ]; then printf '%s\n' "$REFS"; else echo "none"; fi

DIR=$(cd "$(dirname "$0")" && pwd)
if command -v python3 >/dev/null 2>&1 && [ -f "$DIR/text_pages.py" ]; then
  TS=$(conf TEXT_START); TE=$(conf TEXT_END)
  python3 "$DIR/text_pages.py" "$SRC/$BASE.pdf" \
    ${TS:+--start "$TS"} ${TE:+--end "$TE"} || true
fi
