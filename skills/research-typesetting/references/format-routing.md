# Conditional manuscript format routing

| Choice | Skills and tools | Deliverable | Verification |
|---|---|---|---|
| DOCX | scientific-writing, citation-management, available host document skill; local python-docx/template tools as fallback | Editable .docx, PDF only if requested and exported | Actual rendered pages, styles, field/citation values, tables/equations and pagination |
| LaTeX | scientific-writing, citation-management, academic-writing-latex; native compiler or existing compatible TeX toolchain | .tex/source package and compiled PDF when requested | Build diagnostics, cross-references/bibliography, glyphs and visual pages |

The additional academic-writing-latex skill is guidance, not a compiler or official venue template. Font encoding, language packages and citation commands must match the chosen engine/template. Its recommendation to bold best metric values is not automatic in scientific results. Evidence support and uncertainty matter more than a comparative highlight.

Preserve one authoritative content/evidence record across formats. Round-trip conversion can lose fields, equations, comments, cross-references or layout; compare the converted artifact instead of assuming equivalence. DOCX tracked changes, citation-manager fields and dynamic tables of contents are tool-specific; declare unsupported features rather than synthesizing them from plain text.

PDF is a rendered output, not an authoring format. A file can compile/export and still have missing references or visual defects. Do not claim PDF/UA, archival compliance or anonymization from a basic export. If both manuscript formats are requested, record which is canonical and verify each output independently.

Use a native editor where available. Otherwise check tools first; installations require a concrete task and authorization. Offline local examples, only after availability is established:

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
soffice --headless --convert-to pdf --outdir rendered manuscript.docx
```

The LaTeX example assumes a pdfLaTeX-compatible project; other engines need different flags. Office conversion may substitute fonts; inspect the result. Resolve installed paths and use isolated build/output directories without replacing existing deliverables.

Primary tool documentation: [python-docx](https://python-docx.readthedocs.io/en/latest/), [LibreOffice command-line parameters](https://help.libreoffice.org/latest/en-US/text/shared/guide/start_parameters.html). These dependencies are not bundled or installed automatically.
