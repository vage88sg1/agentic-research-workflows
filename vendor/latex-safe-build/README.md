# latex-safe-build

[![CI](https://github.com/molanocortes/latex-safe-build/actions/workflows/ci.yml/badge.svg)](https://github.com/molanocortes/latex-safe-build/actions/workflows/ci.yml)

An [Agent Skill](https://code.claude.com/docs/en/skills) plus two standalone
scripts that compile LaTeX in an isolated scratch copy, so a build can never
corrupt the document it is building.

## The problem

`latexmk` writes its intermediates (`.aux`, `.bcf`, `.toc`, ...) into the tree it
runs in. The moment anything else touches that tree during a build (an editor
saving a chapter, an AI agent session, a file sync tool, a second build), the
intermediates end up half-written and you get failures that look like source
bugs: `File ended while scanning use of ...`, biber crashing on a malformed
`.bcf`, undefined references that were fine an hour ago, a PDF assembled from a
stale table of contents.

This workflow came out of a large master's thesis written with multiple AI agent
sessions editing the tree concurrently. In-tree builds corrupted state
repeatedly; isolated builds eliminated the failure class, and the document
shipped from exactly this setup. The longer story is in [WHY.md](WHY.md), the
failure analysis in [references/concurrency.md](references/concurrency.md).

## What it does

Every build behavior below is enforced by a test in [tests/](tests/); the
letters refer to the fixtures in `tests/fixtures/`. The one exception is the
float-governance reference, which is documentation, not code.

- **Builds in isolation.** `scripts/safe-build.sh` rsyncs the project to a
  scratch directory, runs `latexmk -halt-on-error` there, and copies only the
  finished PDF back. The working tree never contains a build artifact
  (every test asserts this; test *g* mutates a source file mid-build and checks
  that the tree stays pristine and the mutation does not reach the PDF).
- **Zero configuration.** Auto-detects the root file (test *a*), the engine
  (XeLaTeX for fontspec, test *c*), shell-escape (minted, test *d*), and handles
  multi-file `\include` trees with figures in subdirectories (test *e*).
  Everything auto-detection cannot know goes in an optional
  `.latex-safe-build.conf` (keys documented at the top of the script; test *h*).
- **Says what it resolved.** Every run prints a banner with the resolved source
  dir, main file, engine and why it was chosen, and output path, so a
  wrong-tree or wrong-file build is visible immediately.
- **Refuses to race.** It detects an already-running `latexmk` on the same
  document and stops (exit 2) instead of corrupting the build (test *i*).
- **Reports unresolved references.** After every successful build it prints a
  filtered list of undefined or multiply defined labels and citations, with
  rerun and font noise stripped, so real problems are not buried (test *a*).
- **Triages failures.** On error you get the actual TeX error block and a
  hint, not a 2000-line log dump (test *f*); the full log path is printed
  alongside. The pattern table is in
  [references/troubleshooting.md](references/troubleshooting.md).
- **Reports the page count that matters.** `scripts/text_pages.py` prints both
  the PDF total and the text pages (first chapter through conclusion, the
  number page limits are checked against; test *b*). When it cannot find the
  boundaries it says so instead of guessing.
- **Documents float fixes.** [references/float-governance.md](references/float-governance.md)
  carries a preamble block, proven in long use, for deterministic float
  placement, plus fixes for bare-heading sections and orphaned figure pages.

## Install

As a personal [Claude Code](https://code.claude.com/docs/en/skills) skill:

```bash
git clone https://github.com/molanocortes/latex-safe-build ~/.claude/skills/latex-safe-build
```

Or copy the folder into a project's `.claude/skills/` to share it with that
repo. The skill format is an open standard, so any agent that reads `SKILL.md`
can use it.

Requirements: a TeX distribution with `latexmk`; `rsync`; optionally `python3`
with `pypdf` for the page-count report (`pip install pypdf`).

## Use it standalone

The scripts need no AI agent:

```bash
scripts/safe-build.sh                     # current dir, all auto-detected
scripts/safe-build.sh ~/thesis            # explicit project root
scripts/safe-build.sh ~/thesis main.tex -xelatex   # everything explicit
scripts/text_pages.py ~/thesis/main.pdf --start "1 Introduction" --end "References"
```

Exit codes of `safe-build.sh`, for Makefile and CI wiring: `0` build succeeded,
`1` build or setup error (triage printed), `2` refused because another latexmk
for the same document is already running (safe to retry after it finishes).

Run the test suite (needs a full-ish TeX installation). Each fixture builds a real
document and asserts one behaviour, including the two that matter most: *g* mutates
a source file mid-build and checks the mutation never reaches the PDF, and *i*
starts a second build of the same document and checks it is refused rather than
allowed to race.

```console
$ tests/run_tests.sh
PASS: a-article
PASS: b-report-biber
PASS: c-fontspec
PASS: d-minted
PASS: e-multifile
PASS: f-broken
PASS: g-concurrency
PASS: h-config
PASS: i-race-guard

9 passed, 0 failed, 0 skipped
```

## Limitations

- Engines: pdflatex, XeLaTeX, LuaLaTeX via latexmk. No ConTeXt, no plain
  TeX, no custom multi-pass toolchains beyond what latexmk orchestrates.
- Platforms: developed and tested on macOS (MacTeX) and Linux (TeX Live, in
  CI). Windows is untested; the scripts are POSIX shell and would need WSL.
- Text-page detection is heuristic (common English and German headings) and
  falls back to "not determined" rather than a guess. Pin exact boundaries per
  project with `TEXT_START`/`TEXT_END` in the config file.
- Assets referenced outside the project root (absolute or `../` paths) are
  not copied into the isolated build; the script warns about them before
  building.
- Root-file auto-detection expects filenames without spaces; pass the file
  explicitly otherwise.
- The race guard matches on the latexmk process name, so two projects whose
  root files share a name can trigger a false refusal; wait or pass a distinct
  root filename.
- This is not a LaTeX tutor: it builds and diagnoses; it does not write content.

## License

MIT
