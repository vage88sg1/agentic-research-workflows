# LaTeX capabilities and build QA

Read for the selected LaTeX manuscript or Beamer production route, not for Word or a content-only outline. Keep the active scientific workflow's evidence, terminology and review requirements. Use an adequate licensed LaTeX skill already available in the host. The bundled `academic-writing-latex` supplies writing/syntax guidance; optional `latex-safe-build` supplies a local build wrapper and diagnostics, not content generation or a TeX distribution. Read only the relevant support references.

## Preserve the selected template and content

Resolve the actual entry point, document class, local styles, language, fonts, engine and bibliography/index backends from the supplied template/build instructions. Preserve official files and licenses, and work on a copy. Multiple plausible roots require inspection or a focused question; a filename alone is not authoritative. For a generic document without prescribed format, choose and state a suitable provisional class; do not claim institutional/venue compliance. Template-specific missing files and project facts cannot be invented. General background gaps go to authorized primary-source searches.

Keep one canonical checked content/evidence record. Preserve stable citation keys, source locators, labels and custom macros where appropriate. Converting from Markdown or DOCX can flatten references, notes, math or bibliography; inspect the result rather than treating conversion success as equivalence. LaTeX content must use its intended constructs, not manually maintained printed numbers or screenshot text. Embedded support-skill examples are not research evidence.

## Native structures when relevant

| Requirement | Preferred LaTeX representation | Verification |
|---|---|---|
| Contents and figure/table lists | Structural headings and `\tableofcontents`, `\listoffigures`, `\listoftables` or class equivalents | Generated entries and page numbers agree with final headings/captions; required reruns completed |
| Numbered headings, captions, equations and lists | Class counters/environments; `\caption`, equation/align and appropriate list environments | Counter behavior, hierarchy and printed labels remain correct after insertion/reordering |
| Internal references | Stable `\label` with `\ref`, `\eqref` or compatible `\autoref`/`\cref`; `\pageref` when needed | No undefined/duplicate labels; exact target and numbering correct; float labels capture the caption counter |
| Bibliography and citations | Verified `.bib` with template-supported BibTeX/natbib or biblatex and its selected backend; matching citation commands | Backend actually runs, all required keys resolve, printed metadata/style supports each citation and matches the source record |
| Subject index, glossary and acronyms | Template-compatible index/glossary/acronym commands and required backend | Entries are used/printed correctly; makeindex/xindy/makeglossaries or the selected alternative actually runs when needed |
| Math, quantities and tables | Native math/table commands, suitable existing packages such as amsmath/booktabs/siunitx where compatible | Editable source, meaning, units, alignment, symbols and render readability preserved |
| Navigation and page structure | Class sections/front matter/appendices, compatible hyperlink/bookmark/page-style tools | Labels, outline destinations, pagination and links agree with the rendered PDF |
| Beamer | Theme/layout/frame structures, notes and overlays/handout choices as requested | Scientific meaning preserved; distinguish frame count from exported overlay pages and notes |

Activate only needed features. A short letter needs no glossary or figure list. Do not add packages indiscriminately or change template package ordering to match a support skill. `hyperref`, `cleveref`, glossary tools and fonts have class/engine/language dependencies; use the template's supported equivalent. Do not mix incompatible bibliography systems. Biblatex may use different backends; identify the actual configured one rather than assuming every `.bib` means BibTeX. Index/glossary commands alone do not produce finished indexes.

Use native citation commands and source metadata by default. Preserve a venue-required supplied `.bbl` or an explicitly selected static `thebibliography` route when appropriate, identifying its update/source limitations. Verified source metadata should remain exportable when available. Do not automatically replace a required bibliography style or invent missing sources to make compilation green. Actual claim support and bibliography coverage remain scientific checks, separate from key resolution.

## Compile with a real compatible route

Prefer a supported built-in standalone LaTeX editor/compiler: save/open the source, compile, inspect diagnostics and repair within its limits. Check actual multi-file, bibliography/backend and package support; do not infer it from a minimal successful snippet. Do not install TeX or a plugin merely to duplicate the native compiler. For unsupported projects use an available authorized local toolchain with the selected engine and required backends, or deliver source with PDF NOT BUILT and pending QA.

For a local build, use an isolated task-owned work/build directory, stable inputs and bounded execution. Inspect applicable configuration/build commands before running them. Record the source version/hashes, engine/backend/tool versions and actual commands/diagnostics. Prefer compatible latexmk orchestration where available; otherwise execute the chosen engine/bibliography/index sequence and required reruns until references settle within the repair budget. Repeating the wrong engine is not a repair. Do not disable errors or remove unresolved citations to claim success. Preserve required source assets and generated files the selected venue legitimately needs.

A successful process exit is not sufficient: identify a **new PDF from this source revision**, inspect final `.log` plus applicable `.blg`/backend diagnostics and generated bibliography/contents, and verify resolved values in the rendered output. Inspect undefined citations/references, duplicate labels/destinations, rerun requests, missing glyphs/files/fonts and layout issues. Classify material warnings by consequence; an overfull box can clip evidence, while some harmless template warnings can be documented. ChkTeX, if available and useful, is lint rather than compilation, scientific validation or PDF visual QA. Never edit prose merely to silence a false positive.

For a full/template route, test required automatic structures on a disposable representative sample/copy: insert/move a heading or caption, rebuild and check corresponding number, contents/list/reference changes. For bibliography changes, confirm the new citation is rendered and the bibliography is rebuilt using verified test metadata. Test only relevant behavior and preserve the intended final content. Rebuild the actual final source after edits, inspect all final pages and retain correct figure/table positioning and legible detail. A source command, cached `.aux`/`.bbl`, old PDF, lint result or compile flag is not proof of functional updateability.

## Optional latex-safe-build: use within its limits

Read its installed SKILL.md and relevant references only for a compatible **POSIX local build** with existing latexmk/rsync and the required engine/backend. It is not a substitute for the supported native compiler or a Windows-native implementation. An absolute script path, explicit inspected entry point and engine should be used; the wrapper changes working directory internally. Invoke it on a task-owned project work copy and use a separate temporary root per run. Confirm the printed source/root/engine/build/output match the intended project before accepting its result.

Inspect source and config before use. At the pinned revision the wrapper automatically enables shell escape for minted/svg or its config, passes configured extra arguments and can load latexmk configuration. A scratch directory is not a security sandbox and does not authorize arbitrary external commands. Do not invoke this automatic route when its options exceed the authorized task; use a compatible inspected compiler command without shell escape or keep the needed capability pending. A concrete justified external-command requirement must be authorized, not inferred from package presence.

Other limits change the decision to use the wrapper:

- It copies a source tree with rsync, which is not an atomic snapshot of actively edited inputs. Stabilize/verify the input version. Its scratch path is reused for a given source and its process check is not an atomic lock; serialize builds, use distinct work copies/temp roots and do not kill other users' processes to bypass a refusal.
- It excludes `.bbl` and other presumed generated files, so it is unsuitable unchanged for a project whose supplied `.bbl` is an essential source with no regenerable database. Preserve that source through another compatible route rather than deleting/replacing it.
- It copies the finished PDF back to its input directory, potentially replacing an earlier output. Build in a new task-owned work copy or preserve the previous artifact. Inspect the actual final source/output hashes; a banner or BUILD OK is not scientific/production readiness.
- Undefined references can accompany exit zero; its filtered/truncated diagnostic list is not the full log and can omit other material warnings. Inspect complete current logs/backend outputs and keep unresolved essentials open.
- `text_pages.py` is optional and can exit zero without pypdf or reliable boundaries. Its default markers can match a contents entry or prose. Confirm actual body boundaries and the institution's counting rule before using its count. Do not assume all venues exclude front matter/references/appendices or report a guessed body length as fact.
- Its float-governance preamble is a possible targeted fix, not proof of deterministic placement or a universal template rule. Diagnose rendered pages before changing float settings; a legitimate figure page is not automatically a defect.

Do not execute the upstream full test suite automatically: it requires a real TeX installation and includes shell-escape fixtures. Installation only copies instructions and scripts. Read script usage and dependency requirements before any selected operation.

## Handoff and sources

Return requested TeX source, verified bibliography and required assets/styles with relative paths and usable build instructions, plus the PDF only if actually built. Keep final logs, relevant source hashes, feature statuses (**verified**, **not tested**, **unsupported**), actual inspection coverage and unresolved limitations in existing records. Venue-specific packaging may require `.bbl`/other files; establish that from actual rules rather than a universal cleanup list. Do not claim PDF/A, PDF/UA or complete reproducibility from package options alone. Scientific review and human approval remain separate.

Primary references: [LaTeX Project documentation](https://www.latex-project.org/help/documentation/), [latexmk](https://ctan.org/pkg/latexmk), [biblatex](https://ctan.org/pkg/biblatex), [Biber](https://ctan.org/pkg/biber), [hyperref](https://ctan.org/pkg/hyperref), [cleveref](https://ctan.org/pkg/cleveref), [glossaries](https://ctan.org/pkg/glossaries), [ChkTeX](https://ctan.org/pkg/chktex), and [pinned latex-safe-build](https://github.com/molanocortes/latex-safe-build/tree/d6cd2314676c44a56e58c8f892082ef00a6a8371).
