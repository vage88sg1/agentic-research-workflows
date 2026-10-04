---
name: latex-safe-build
description: Compile LaTeX documents in an isolated scratch copy so a build can never corrupt the source tree, then report unresolved references and the page counts that actually matter (text pages, not just PDF pages). Use this skill whenever compiling or building any LaTeX document (latexmk, pdflatex, xelatex, lualatex, biber), whenever a build fails with corrupted .aux/.bcf files, "File ended while scanning", or phantom undefined-reference storms, whenever more than one session, agent, or person might touch the same LaTeX tree, or when asked how long a thesis, report, or paper is in pages. Even a plain "compile my thesis" or "rebuild the PDF" should go through this skill. Not for writing or editing LaTeX content itself (equations, wording, structure); it governs builds and build diagnostics only.
---

# latex-safe-build

Build LaTeX documents without ever running the compiler inside the working tree.

## Why builds are isolated

`latexmk` writes dozens of intermediates (`.aux`, `.bcf`, `.toc`, `.fls`, ...) into
the directory it runs in. If anything touches that directory during the build (an
editor saving a chapter, another agent session, a file sync tool, a second build),
the intermediates end up half-written, and the failures look like source bugs:
`File ended while scanning use of ...`, biber crashing on a malformed `.bcf`,
sudden storms of undefined references, a PDF assembled from a stale table of
contents. So: **snapshot the tree to a scratch location, build there, copy only
the finished PDF back.** The working tree stays byte-identical except for the
output, edits made mid-build cannot corrupt anything, and the build is
deterministic with respect to the moment the snapshot was taken. The full failure
analysis lives in `references/concurrency.md`; read it when you need to explain to
a user *why* their in-tree build produced garbage.

## How to build

Use the bundled script. Zero configuration for a standard project:

```bash
scripts/safe-build.sh [source-dir] [main-tex] [engine-flag]
```

All three arguments are optional. The script auto-detects:

- **the root file**: from `.latexmkrc` (`@default_files`), or by scanning root
  `.tex` files for `\documentclass` + `\begin{document}` (preferring `main.tex`,
  `thesis.tex`, `report.tex`, `paper.tex` when several qualify);
- **the engine**: TeXShop/TeXstudio magic comments first, then `fontspec` /
  `polyglossia` / `unicode-math` usage (XeLaTeX, or LuaLaTeX when `luacode` /
  `directlua` appears), else pdflatex;
- **shell-escape**: enabled automatically when `minted` or `svg` is used;
- **the bibliography backend**: left to latexmk, which picks biber or bibtex from
  the document itself.

Every run starts by printing a banner with the resolved source dir, main file,
engine (and *why* it was chosen), build dir, and output path. Read that banner
every time. A build wrapper that silently builds the wrong tree, or the wrong root
file, is worse than no wrapper, because "BUILD OK" then certifies an artifact
nobody meant to build. If the banner disagrees with what the user intended, stop
and fix the invocation, not the document.

When auto-detection cannot know something (unusual boundaries, forced
shell-escape, extra latexmk flags), put a `.latex-safe-build.conf` in the project
root; the keys are documented at the top of the script. Detection failures are
loud by design: no root file found, or several plausible ones, is an error
naming the candidates, never a silent guess.

On failure the script prints a short triage (the actual TeX error block, biber
errors, and hints), not the whole log; the full log path is printed with it.
Interpret triage lines with `references/troubleshooting.md`.

## Page counts: report the number that matters

A PDF page count and a document length are different numbers. Universities and
journals count **text pages** (typically first chapter through conclusion), while
the PDF total includes title, table of contents, bibliography and appendices. A
130-page PDF can be a 70-page document, and reporting the wrong number to a user
with a page limit is a serious error, so report both:

```bash
scripts/text_pages.py <pdf>                # tries common boundary headings
scripts/text_pages.py <pdf> --start "1 Introduction" --end "References"
```

With no flags it tries common English and German boundary headings and names the
markers it matched. When it cannot find boundaries it says so and reports only
the total; never present a guessed text count as fact. Pin the boundaries per
project with `TEXT_START` / `TEXT_END` in `.latex-safe-build.conf`.

## Rules of engagement for the agent

- **Do not run `latexmk`, `pdflatex`, `xelatex`, or `lualatex` directly in a
  working tree** that anyone else might touch, even for a "quick check". Use the
  script. The one exception: a throwaway single-file snippet in a directory
  nothing else uses.
- **If the user asks you to build in-tree**, do not silently comply or silently
  refuse: explain the corruption risk in one sentence (half-written `.aux`/`.bcf`
  when edits land mid-build) and offer the isolated build, which produces the
  same PDF in the same place.
- **If the project has its own Makefile or build script** that compiles in-tree,
  do not fight it or rewrite it unasked. Offer to route it through the isolated
  build; the drop-in pattern is in `references/concurrency.md`.
- **Never "fix" a broken build by deleting `.aux`/`.bcf` files inside the working
  tree.** That treats the symptom in the wrong place; a fresh isolated build gets
  the same effect without destroying state other tools may hold open.
- **Before any manual rebuild after a crash**, confirm no stale `latexmk` is
  still alive (`pgrep -fl latexmk`). The script refuses to start when one is; do
  not work around that refusal, it exists because overlapping builds corrupt each
  other's intermediates.
- **Quote the banner in your report to the user** (source, main, engine, output),
  so a wrong-tree build is caught by a human immediately.

## Float and layout problems

If figures drift far from their references, a section renders as a bare heading,
or a lone figure strands itself on its own page, read
`references/float-governance.md`: a proven preamble block that makes float
placement deterministic, plus targeted fixes for both orphan patterns. Apply it
when diagnosing layout complaints, not preemptively on healthy documents.

## Scope boundaries

This skill governs building and diagnosing LaTeX projects. It does not write or
restructure LaTeX content, choose document classes, or manage bibliography
databases beyond reporting unresolved citations. For content questions, answer
normally without this skill.
