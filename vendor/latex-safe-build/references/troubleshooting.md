# Log triage

`safe-build.sh` prints a short triage on failure instead of the raw log (the full
log path is printed alongside). This file maps triage lines to causes and fixes.

Note on error formats: the script builds with `-file-line-error`, so TeX errors
appear as `./chapter2.tex:41: Undefined control sequence` rather than the classic
`! Undefined control sequence`. Both mean the same thing; the file:line form
tells you where to look.

## Triage table

| Line contains | What it means | Fix |
|---|---|---|
| `File 'x.sty' not found` | Missing LaTeX package | `tlmgr install <pkg>` (TeX Live/MacTeX) or `apt install texlive-<collection>` |
| `File 'x.pdf' not found` / `File 'x' not found` (graphics) | Figure or input path wrong, or the file lives OUTSIDE the project dir (the script warns about `../` and absolute paths before building) | Fix the path, or move the asset into the tree |
| `Undefined control sequence` | Typo in a macro, or its package is not loaded | Check the named file:line |
| `shell escape` / `minted Error` | Document needs `-shell-escape` | The script auto-enables it for minted/svg; for other packages set `SHELL_ESCAPE=1` in `.latex-safe-build.conf` |
| `pygmentize` not found (minted) | minted needs Pygments installed | `pip install pygments` |
| `fontspec error` / `cannot be found` (a font) | Wrong engine, or the named font is not installed | The script selects XeLaTeX for fontspec automatically; check the font name against installed fonts |
| `biber ... error` / `.bcf could not be read` | Stale or malformed biber handoff | A fresh isolated build fixes stale state; if it persists, the `.bib` has a syntax error the biber log names |
| `Emergency stop` / `No pages of output` | A fatal error earlier in the log | Read the first error block in the triage, not the last line |
| `! LaTeX Error: Missing \begin{document}` | Stray text before `\begin{document}`, often a BOM or an editing accident in the preamble | Check the first lines of the root file |

## Failure patterns beyond single lines

**A storm of undefined references that were fine yesterday.** Usually stale
`.aux` state, not a source problem. latexmk reruns automatically, so a fresh
isolated build resolves it. Only if the fresh build still reports them are they
real; then the filtered list printed after `BUILD OK` is the actual to-do list.

**`File ended while scanning use of ...` on a file nobody edited.** An
intermediate was half-written when read: the signature of a build racing an
editor, a sync tool, or another build. Fresh isolated build; if it recurs, find
what is writing into the build directory (see `concurrency.md`). If the
truncated file is a `.tex` source, the source itself is damaged.

**Build hangs, or two builds interleave.** `pgrep -fl latexmk`. Two latexmk
processes on one document corrupt each other even in a scratch directory; the
script refuses to start when it detects one, so a hang usually means an earlier
run never exited. Kill it; the next run starts from a clean snapshot anyway.

**The PDF built but looks stale.** Confirm you are reading the PDF the script
copied back (project root, check the modification time), not an old artifact
elsewhere. The banner prints the exact output path.

**Page count changed unexpectedly.** Rebuild twice from clean snapshots before
blaming content; a stale `.toc`/`.lof` can shift front matter by a page. If the
difference is real, diff the two builds' `.toc` files to localize it.
