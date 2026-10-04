#!/bin/sh
# Test gauntlet for latex-safe-build. Every fixture is a real miniature LaTeX
# project; every README claim is exercised here. Fixtures are copied to a temp
# workdir before each test, so the repo itself is never built in (practice what
# we preach).
set -u

HERE=$(cd "$(dirname "$0")" && pwd)
BUILD="$HERE/../scripts/safe-build.sh"
WORK="${TMPDIR:-/tmp}/latex-safe-build-tests"
PASS=0; FAIL=0; SKIP=0

pass() { PASS=$((PASS+1)); printf 'PASS: %s\n' "$1"; }
fail() { FAIL=$((FAIL+1)); printf 'FAIL: %s (%s)\n' "$1" "$2"; }
skip() { SKIP=$((SKIP+1)); printf 'SKIP: %s (%s)\n' "$1" "$2"; }

fresh() { # fresh <fixture> -> prints the temp workdir it copied it to
  rm -rf "${WORK:?}/$1"
  mkdir -p "$WORK"
  cp -R "$HERE/fixtures/$1" "$WORK/$1"
  printf '%s\n' "$WORK/$1"
}

pristine() { # succeeds when the tree holds no build artifacts
  find "$1" \( -name '*.aux' -o -name '*.toc' -o -name '*.log' -o -name '*.bcf' \
    -o -name '*.fls' -o -name '*.fdb_latexmk' -o -name '*.bbl' -o -name '*.out' \
    -o -name '*.blg' -o -name '*.synctex.gz' \) -print | grep -q . && return 1 || return 0
}

has() { printf '%s' "$2" | grep -qF "$1"; }

# --- (a) plain article: auto-detect, honest page-count fallback -------------
t_article() {
  d=$(fresh a-article)
  out=$("$BUILD" "$d" 2>&1); rc=$?
  [ $rc -eq 0 ]                                || { fail a-article "exit $rc"; return; }
  has "BUILD OK" "$out"                        || { fail a-article "no BUILD OK"; return; }
  has "main   : paper.tex (auto-detected)" "$out" || { fail a-article "main not auto-detected"; return; }
  has "engine : -pdf" "$out"                   || { fail a-article "engine not pdflatex"; return; }
  has "TEXT PAGES: not determined" "$out"      || { fail a-article "no honest page-count fallback"; return; }
  has "none" "$out"                            || { fail a-article "unresolved-ref report missing"; return; }
  [ -f "$d/paper.pdf" ]                        || { fail a-article "no PDF copied back"; return; }
  pristine "$d"                                || { fail a-article "artifacts leaked into tree"; return; }
  pass a-article
}

# --- (b) report + biber + appendix: text-page boundaries --------------------
t_report_biber() {
  d=$(fresh b-report-biber)
  out=$("$BUILD" "$d" 2>&1); rc=$?
  [ $rc -eq 0 ]                                || { fail b-report-biber "exit $rc"; return; }
  has "BUILD OK" "$out"                        || { fail b-report-biber "no BUILD OK"; return; }
  has "TEXT PAGES ('Chapter 1' -> before 'Bibliography'): 4" "$out" \
                                               || { fail b-report-biber "wrong text-page count"; return; }
  pristine "$d"                                || { fail b-report-biber "artifacts leaked"; return; }
  pass b-report-biber
}

# --- (c) fontspec: engine auto-detection ------------------------------------
t_fontspec() {
  d=$(fresh c-xelatex-fontspec)
  out=$("$BUILD" "$d" 2>&1); rc=$?
  [ $rc -eq 0 ]                                || { fail c-fontspec "exit $rc: $(printf '%s' "$out" | tail -3)"; return; }
  has "engine : -xelatex (fontspec detected)" "$out" \
                                               || { fail c-fontspec "xelatex not auto-selected"; return; }
  has "BUILD OK" "$out"                        || { fail c-fontspec "no BUILD OK"; return; }
  pristine "$d"                                || { fail c-fontspec "artifacts leaked"; return; }
  pass c-fontspec
}

# --- (d) minted: shell-escape auto-detection --------------------------------
t_minted() {
  command -v pygmentize >/dev/null 2>&1 || { skip d-minted "pygmentize not installed"; return; }
  d=$(fresh d-minted-shellescape)
  out=$("$BUILD" "$d" 2>&1); rc=$?
  [ $rc -eq 0 ]                                || { fail d-minted "exit $rc: $(printf '%s' "$out" | tail -3)"; return; }
  has "extras : -shell-escape (minted/svg detected)" "$out" \
                                               || { fail d-minted "shell-escape not auto-enabled"; return; }
  has "BUILD OK" "$out"                        || { fail d-minted "no BUILD OK"; return; }
  pristine "$d"                                || { fail d-minted "artifacts leaked"; return; }
  pass d-minted
}

# --- (e) multi-file include tree with figures in subdirs --------------------
t_multifile() {
  d=$(fresh e-multifile)
  out=$("$BUILD" "$d" 2>&1); rc=$?
  [ $rc -eq 0 ]                                || { fail e-multifile "exit $rc: $(printf '%s' "$out" | tail -3)"; return; }
  has "BUILD OK" "$out"                        || { fail e-multifile "no BUILD OK"; return; }
  [ -f "$d/main.pdf" ]                         || { fail e-multifile "no PDF"; return; }
  pristine "$d"                                || { fail e-multifile "artifacts leaked"; return; }
  pass e-multifile
}

# --- (f) broken project: log triage, not a log dump -------------------------
t_broken() {
  d=$(fresh f-broken)
  out=$("$BUILD" "$d" 2>&1); rc=$?
  [ $rc -ne 0 ]                                || { fail f-broken "broken project built?!"; return; }
  has "BUILD FAILED" "$out"                    || { fail f-broken "no BUILD FAILED banner"; return; }
  has "nosuchpackage123" "$out"                || { fail f-broken "actual error not surfaced"; return; }
  has "hint:" "$out"                           || { fail f-broken "no actionable hint"; return; }
  lines=$(printf '%s\n' "$out" | wc -l)
  [ "$lines" -lt 60 ]                          || { fail f-broken "triage dumped $lines lines"; return; }
  pristine "$d"                                || { fail f-broken "artifacts leaked"; return; }
  pass f-broken
}

# --- (g) concurrency: mutate the source mid-build ---------------------------
t_concurrency() {
  d=$(fresh g-concurrency)
  # Reproduce the scratch path the script will use, so we can time the mutation
  # to land after the snapshot (rsync) but during the compile. The script
  # canonicalizes the source path with cd/pwd (macOS TMPDIR has a trailing
  # slash), so canonicalize the same way before hashing.
  d=$(cd "$d" && pwd)
  hash=$(printf '%s' "$d" | cksum | cut -d' ' -f1)
  bld="${TMPDIR:-/tmp}/latex-safe-build/g-concurrency-$hash"
  rm -rf "$bld"
  outfile="$WORK/g-out.txt"
  "$BUILD" "$d" >"$outfile" 2>&1 &
  pid=$!
  i=0
  while [ ! -f "$bld/main.tex" ] && [ $i -lt 100 ]; do sleep 0.1; i=$((i+1)); done
  [ -f "$bld/main.tex" ] || { kill $pid 2>/dev/null; fail g-concurrency "snapshot never appeared"; return; }
  sleep 0.3
  # Mutate the WORKING copy mid-build, the way a concurrent editor would.
  awk '/\\chapter\{Two\}/ {print "MUTATIONXYZ text injected mid-build."} {print}' \
    "$d/main.tex" > "$d/main.tex.new" && mv "$d/main.tex.new" "$d/main.tex"
  wait $pid; rc=$?
  out=$(cat "$outfile")
  [ $rc -eq 0 ]                                || { fail g-concurrency "exit $rc: $(printf '%s' "$out" | tail -3)"; return; }
  has "BUILD OK" "$out"                        || { fail g-concurrency "no BUILD OK"; return; }
  pristine "$d"                                || { fail g-concurrency "artifacts leaked into mutated tree"; return; }
  if command -v python3 >/dev/null 2>&1 && python3 -c 'import pypdf' 2>/dev/null; then
    python3 - "$d/main.pdf" <<'PY' || { fail g-concurrency "mid-build mutation leaked into the PDF"; return; }
import sys
from pypdf import PdfReader
text = "".join((p.extract_text() or "") for p in PdfReader(sys.argv[1]).pages)
sys.exit(1 if "MUTATIONXYZ" in text else 0)
PY
  else
    printf 'note: pypdf unavailable, PDF-content determinism check skipped\n'
  fi
  pass g-concurrency
}

# --- (h) config file overrides auto-detection -------------------------------
t_config() {
  d=$(fresh a-article)
  printf 'ENGINE=-xelatex\n' > "$d/.latex-safe-build.conf"
  out=$("$BUILD" "$d" 2>&1); rc=$?
  [ $rc -eq 0 ]                                || { fail h-config "exit $rc: $(printf '%s' "$out" | tail -3)"; return; }
  has "engine : -xelatex (config)" "$out"      || { fail h-config "config engine not honored"; return; }
  # TEXT_START/TEXT_END from config must reach the page counter.
  d2=$(fresh b-report-biber)
  printf 'TEXT_START=Chapter 1\nTEXT_END=Appendix\n' > "$d2/.latex-safe-build.conf"
  out=$("$BUILD" "$d2" 2>&1); rc=$?
  [ $rc -eq 0 ]                                || { fail h-config "exit $rc (markers): $(printf '%s' "$out" | tail -3)"; return; }
  has "TEXT PAGES ('Chapter 1' -> before 'Appendix'): 5" "$out" \
                                               || { fail h-config "config text markers not honored"; return; }
  pass h-config
}

# --- (i) race guard: a second build must refuse, not corrupt ----------------
t_race_guard() {
  d=$(fresh g-concurrency)
  d=$(cd "$d" && pwd)
  hash=$(printf '%s' "$d" | cksum | cut -d' ' -f1)
  bld="${TMPDIR:-/tmp}/latex-safe-build/g-concurrency-$hash"
  rm -rf "$bld"
  outfile="$WORK/race-out.txt"
  "$BUILD" "$d" >"$outfile" 2>&1 &
  pid=$!
  i=0
  while [ ! -f "$bld/main.tex" ] && [ $i -lt 100 ]; do sleep 0.1; i=$((i+1)); done
  out2=$("$BUILD" "$d" 2>&1); rc2=$?
  wait $pid; rc1=$?
  [ $rc2 -eq 2 ]                               || { fail i-race-guard "second build exited $rc2, wanted 2"; return; }
  has "already running" "$out2"                || { fail i-race-guard "no refusal message"; return; }
  [ $rc1 -eq 0 ]                               || { fail i-race-guard "first build broke (exit $rc1)"; return; }
  pass i-race-guard
}

t_article
t_report_biber
t_fontspec
t_minted
t_multifile
t_broken
t_concurrency
t_config
t_race_guard

printf '\n%d passed, %d failed, %d skipped\n' "$PASS" "$FAIL" "$SKIP"
[ "$FAIL" -eq 0 ]
