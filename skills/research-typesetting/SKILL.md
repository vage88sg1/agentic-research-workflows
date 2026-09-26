---
name: research-typesetting
description: Format an evidence-checked research paper or thesis as DOCX or LaTeX with optional PDF output, verified templates, bibliography and cross-reference checks, compilation/rendering and visual inspection. Use after selecting the authoring format; not for inventing research content.
license: MIT
---

# Research typesetting

Ask or read the configured manuscript format: DOCX or LaTeX. Activate only the selected route. If not chosen, explain editable Word versus TeX source briefly and ask; continue evidence work that does not depend on format. Read [format routing](references/format-routing.md) for the chosen route.

Resolve authorized source material, template, language/script, paper size, bibliography style and intended output. Check current official venue/institution rules; never assume English, IEEE, A4 or a specific thesis structure. Formatting must preserve verified claims, numbers, uncertainty, citations and declarations.

## DOCX route

Use the host's document skill/tools when available and compatible with the request. Otherwise use a documented local DOCX tool such as python-docx or a template-based converter, recording its limitations. Create editable headings/styles, captions, tables and equations where supported. Do not rename another file to .docx or substitute screenshots for required editable evidence.

Do not load academic-writing-latex for a DOCX task. Produce the editable .docx; when PDF is requested, export the same final version through a real office/document renderer. Inspect rendered pages for clipping, pagination, figures/tables, field values and bibliography. If a renderer is unavailable, deliver source with visual QA NOT PERFORMED, not a claimed verified PDF.

## LaTeX route

Read academic-writing-latex if installed; use its TeX syntax/math/cross-reference guidance conditionally. Its English/engineering/IEEE defaults and stylistic absolutes do not override user/venue requirements. Unicode/font handling depends on the engine; do not copy its preamble blindly across pdfLaTeX, XeLaTeX and LuaLaTeX. Never treat embedded worked examples as verified evidence.

Choose the official template where required, preserve its class/style files and license, and identify engine and BibTeX/Biber backend from actual compatibility. Keep .tex, bibliography and required figures/styles in a reproducible source package with relative paths. Preserve a canonical evidence record so switching format does not silently change results.

In a host with a built-in standalone LaTeX editor/compiler, prefer it for supported documents: save/open the source, compile, inspect diagnostics and repair up to three times. Do not install a TeX distribution merely to duplicate the built-in compiler. For unsupported multi-file projects use an already available authorized local toolchain, documenting engine/backend/versions and commands; no shell escape or external upload without a concrete need and authorization.

Compilation success is required before declaring a PDF built. Check undefined references/citations, package conflicts, missing glyphs, overfull boxes and unreadable equations/figures; render and inspect final pages. If compilation is unavailable, retain source and report PDF NOT BUILT. A compiler pass does not prove venue compliance or scientific validity.

## Handoff

Return selected editable source, requested PDF if actually generated, bibliography/assets and concise build/QA status. Record build input hashes, actual tool/version and output version. Substantive content changes return to scientific review; simulated publication artifacts retain their simulation label. Do not create both formats unless requested or required.

## Saved state and continuation

When starting, resuming or handing off a run, follow [saved state and handoff](references/run-state.md). Save the current phase, artifact versions, actual checks, open issues and next action in the run directory.

## Optional project support

Use research-project when installed for a requested capability check, evidence-map audit, dependency-impact report or reproducibility package. All installation profiles include it. Read only the relevant operation's guidance; support scripts check records and bytes, not scientific meaning. Record affected artifacts in saved state and reverify them after substantive changes.
