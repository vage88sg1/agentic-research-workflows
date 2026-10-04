---
name: research-typesetting
description: Format an evidence-checked research paper or thesis as DOCX or LaTeX with optional PDF output, verified templates, bibliography and cross-reference checks, compilation/rendering and visual inspection. Use after selecting the authoring format; not for inventing research content.
license: MIT
---

# Research typesetting

For role/model selection, follow [installed model preferences](../galileo/references/model-settings.md). Reuse explicit project choices and the shared installation mapping; distinguish requested models from actual host execution. Bounded edits need no model-setup interview.

Ask or read the configured manuscript format: DOCX or LaTeX. Activate only the selected route. If not chosen, explain editable Word versus TeX source briefly and ask; continue evidence work that does not depend on format. Read [format routing](references/format-routing.md) for the chosen route.

Resolve authorized source material, template, language/script, paper size, bibliography style and intended output. Check current official venue/institution rules; never assume English, IEEE, A4 or a specific thesis structure. Formatting must preserve verified claims, numbers, uncertainty, citations and declarations.

Apply the relevant [editorial/visual checks and revision-specific closure](../galileo/references/quality-gates.md#2-separate-evidence-review-from-usefulness-to-the-reader). Inspect isolated short continuations before chapter breaks, avoidable figure/table gaps, detail readability and final index numbers, as well as clipping. Resolve page size/template from supplied or verified requirements; otherwise state the provisional choice without claiming compliance. A justified figure-only or institutional blank page is not automatically a defect. Preserve content rather than compressing text to hide layout problems.

## DOCX route

Use the host's document skill/tools when available and compatible with the request. Otherwise use a documented local DOCX tool such as python-docx or a template-based converter, recording its limitations. Read [Office capabilities and functional QA](../galileo/references/office-capabilities.md) before DOCX production. Prefer actual native structures: heading/list styles, automatic contents/lists, caption and cross-reference fields, native tables/equations and supported reference-manager citations. Use an available licensed host document skill first; the bundled `documents` skill is portable fallback guidance and structural tooling. Do not silently recreate supported dynamic structures as manually maintained text. Do not rename another file to .docx or substitute screenshots for required editable evidence.

Do not load academic-writing-latex for a DOCX task. Produce the editable .docx; when PDF is requested, export the same final version through a real office/document renderer. Inspect rendered pages for clipping, pagination, figures/tables, field values and bibliography. If a renderer is unavailable, deliver source with visual QA NOT PERFORMED, not a claimed verified PDF.

## LaTeX route

Read [LaTeX capabilities and build QA](../galileo/references/latex-capabilities.md) for native structures and the actual compilation route. Prefer a suitable available LaTeX skill; `academic-writing-latex` supplies writing guidance and `latex-safe-build` supplies optional external build/diagnostic guidance. Load the latter only for a compatible local build after the reference checks, not as a replacement for a supported built-in compiler. Read academic-writing-latex if installed; use its TeX syntax/math/cross-reference guidance conditionally. Its English/engineering/IEEE defaults and stylistic absolutes do not override user/venue requirements. Unicode/font handling depends on the engine; do not copy its preamble blindly across pdfLaTeX, XeLaTeX and LuaLaTeX. Never treat embedded worked examples as verified evidence.

Choose the official template where required, preserve its class/style files and license, and identify engine and BibTeX/Biber backend from actual compatibility. Keep .tex, bibliography and required figures/styles in a reproducible source package with relative paths. Preserve a canonical evidence record so switching format does not silently change results.

In a host with a built-in standalone LaTeX editor/compiler, prefer it for supported documents: save/open the source, compile, inspect diagnostics and repair up to three times. Do not install a TeX distribution merely to duplicate the built-in compiler. For unsupported multi-file projects use an already available authorized local toolchain, documenting engine/backend/versions and commands; no shell escape or external upload without a concrete need and authorization.

Compilation success is required before declaring a PDF built. Check undefined references/citations, package conflicts, missing glyphs, overfull boxes and unreadable equations/figures; render and inspect final pages. If compilation is unavailable, retain source and report PDF NOT BUILT. A compiler pass does not prove venue compliance or scientific validity.

## Handoff

Return selected editable source, requested PDF if actually generated, bibliography/assets and concise build/QA status. Record build input hashes, actual tool/version and output version. Substantive content changes return to scientific review; simulated publication artifacts retain their simulation label. Do not create both formats unless requested or required.

Link each final check to the actual artifact revision/hash and inspection scope. Export and inspect the requested PDF from that editable revision. Invalidate affected checks after content/layout/renderer changes; keep required independent review pending if only coordinator self-review was possible, with that fallback explicit. Separate successful generation from verified usability and human approval.

Reconcile citations with bibliography in both directions and preserve source metadata/versions; source or topic coverage gaps return to evidence/content review rather than being hidden by formatting. For tracked final outputs, use the shared delivery-register guidance to distinguish produced files from content, bibliography, required-review and production readiness.

## Saved state and continuation

When starting, resuming or handing off a run, follow [saved state and handoff](references/run-state.md). Save the current phase, artifact versions, actual checks, open issues and next action in the run directory.

## Optional project support

Use research-project when installed for a requested capability check, evidence-map audit, dependency-impact report or reproducibility package. All installation profiles include it. Read only the relevant operation's guidance; support scripts check records and bytes, not scientific meaning. Record affected artifacts in saved state and reverify them after substantive changes.
