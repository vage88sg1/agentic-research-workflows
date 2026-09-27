# Scientific presentation export and QA

## PPTX plus PDF

Prefer available native presentation tooling and follow its documented APIs. For a portable local alternative, [PptxGenJS](https://gitbrent.github.io/PptxGenJS/) supports PPTX text, tables, shapes, images and charts. Use current documentation and installed versions; this package does not bundle or install that library.

Keep content text editable; use native tables/data charts for requested editable evidence. Preserve source data, plotting code, vector figures and equation source. Unsupported native math, animation, comments or accessibility metadata must be disclosed, not claimed functional from appearance alone.

Save PPTX, export that same revision through a real office renderer to PDF, and rasterize/render the PDF for inspection. PowerPoint/LibreOffice or a host exporter may render differently; log the engine and inspect substituted fonts. PDF is static: decide how animations/builds flatten, and compare slide count/order, central text, numbers, captions and figures. Notes may be absent from slide-only PDF: deliver a separate notes document if requested.

Example only after confirming tools are available:

```bash
soffice --headless --convert-to pdf --outdir rendered presentation.pptx
```

[LibreOffice parameters](https://help.libreoffice.org/latest/en-US/text/shared/guide/start_parameters.html) document conversion. Use an isolated build directory and protect existing outputs. Do not assume conversion succeeded from exit code alone: check the output, page count and rendered content.

## PDF-first Beamer

Use scientific-slides/references/beamer_guide.md only for this route. Choose theme, aspect ratio, engine and fonts appropriate to the language and event. Built-in LaTeX source editor/compiler is preferred for supported standalone documents when available; multi-file projects may need an existing toolchain. Beamer overlays can generate multiple PDF pages per frame: agree on audience-facing versus handout export and count both honestly.

Deliver .tex/assets and the PDF actually compiled. There is no automatic editable PPTX guarantee from Beamer/PDF conversion. If both PPTX and PDF are required, use PPTX as the canonical deck or explicitly agree on separately authored versions with content reconciliation.

## Representative and final rendering

Follow [visual design](visual-design.md) to render representative slides before full-deck expansion. Use the intended final renderer and inspect actual font/layout behavior; if the engine or fonts change, recheck affected slides. Reuse sample slides within the requested slide count. Their checks do not substitute for inspecting every final slide or reconciling exported formats.

## Visual and scientific checklist

- Inspect every rendered page/slide and a full-deck overview; no clipping, collisions, missing glyphs or cropped uncertainty.
- Verify labels, units, n, intervals and sources against the evidence record; simple visual appeal is not validation.
- Check shared palette, stable scientific color mappings, typography, margins, recurring layouts and template consistency. Verify supplied/official logo identity, variant, proportions, clear space, placement, co-branding and font substitutions against the recorded guidelines.
- Test distance readability, contrast and redundant encodings rather than blindly applying a fixed font size or color ratio.
- Check the detail required for each message: dense table labels and full-size screenshots may fit yet remain unreadable to the audience. Use a faithful crop, annotation, conceptual view or backup placement without changing the source meaning or agreed slide count.
- Keep source attribution on relevant slides/notes and a readable bibliography as appropriate; visible disclosures remain visible.
- Reconcile final PPTX/PDF versions and note animation/overlay behavior. Do not claim PowerPoint inspection unless it actually occurred there.
- Record generated, rendered, visually inspected, scientifically checked and human-approved separately.

If rendering is unavailable, leave visual review pending; if export is unavailable, deliver source/build instructions and mark missing output. Neither source code nor an image-only deck is a verified editable PPTX.

## Checks covering the delivered deck

Follow [revision-specific closure](../../galileo/references/quality-gates.md#3-close-checks-against-the-delivered-revision). For each scientific or visual check record the PPTX/PDF revision/hash, reviewer/tool and context, actual slide coverage, render size or inspection method and evidence locator. Compare exports against their final editable source. After changes recheck affected slides, notes, page order and fonts; an earlier report only remains applicable to documented unchanged material. If a distinct reviewer cannot complete the final pass, identify the coordinator fallback and leave required independent review pending. Do not convert export success or a contact-sheet inspection alone into a claim of scientific or presentation readiness.
