---
name: research-presentations
description: Build and revise evidence-grounded scientific conference, seminar or thesis-defense slides with specialist roles, speaker notes, timing and visual QA, delivering editable PPTX and PDF or selected PDF-only Beamer output. Use for scientific presentations, not journal submissions.
license: MIT
---

# Scientific presentation workflow

For deck production, read [roles and revision](references/presentation-agents.md) and [export and QA](references/export-and-qa.md). For a content-only request, start with the scoped path below; read export guidance only when export is requested. Load scientific-slides or other support guidance only when needed for the requested structure, design, citation or figure task; an adequately specified content-only outline need not load a full production toolkit. Read only relevant references. This package does not supply a PPTX renderer or generative service; check actual host production capabilities when a rendered deck is requested.

## Content-only path

If the user requests an outline, slide text or speaker notes in Markdown, produce that content directly from the supplied material when audience, duration and scope are sufficient. Follow the requested slide count and include message, notes, source attribution and estimated timing as appropriate. Preserve scientific qualifiers, denominators and evidence limits. Ask only a question that materially blocks this content task; do not require a theme, aspect ratio, presenter identity, renderer or output format already specified.

Do not run export/render setup, create unrequested PPTX/PDF, or report those files as missing. State timing as estimated rather than measured. Deliver the requested content file and a concise explanation. New state/technical ledgers are unnecessary for a one-off content task unless requested; update relevant records if this is part of an existing tracked run. The full deck's production and visual checks apply when that production stage is requested, not to a content-only handoff.

## Progressive intake

Ask up to three focused questions at a time: audience/talk type, duration including Q&A, source material and language. Then resolve requested total slide count, template/branding, aspect ratio, accessibility needs, presenter identity supplied by the user, speaker notes and export choice. Default request for PPTX and PDF means both outputs from one final deck. For PDF-only, ask whether editable PPTX source or Beamer .tex is preferred if it matters. Resume saved presentation state and preserve original inputs.

Use only authorized evidence. Do not infer missing results, fabricate speakers/institutions or assume a thesis has been published. A real research talk about unpublished work is not automatically a simulated publication: apply the simulation label only to simulated results/decisions/dossiers, labeling illustrative data explicitly.

When this step needs external literature, identifier checks or an authorized reference library, follow [literature connection recommendations](../galileo/references/literature-connections.md). Offer relevant MCP connections if equivalent tools are unavailable; reuse the coordinator's recorded choice. Do not propose setup for a task fully supported by supplied sources.

## Attribution without unverified bibliography

Retain applicable software/skill license notices in the project distribution. Do not automatically insert a paper title, DOI or arXiv identifier found in a support skill into a user's slide content or references. Verify a primary bibliographic record before adding such a citation when it is actually appropriate to the talk. If verification is unavailable, omit the academic reference from the deliverable and retain any necessary software credit separately in project provenance. Labeling a citation “unverified” does not make it suitable to insert automatically. Scientific references should support the talk's claims, not advertise the tooling used to prepare it.

## Plan and evidence map

Build a storyboard with slide ID, purpose, message, supporting claim/source/result IDs, visual, notes and time allocation. Adapt to conference, seminar, defense or journal club; do not force one slide-per-minute or a fixed number of references. Match the requested slide count including cover/closing unless clarified otherwise. Decide the minimum scientific context needed to understand the findings.

Keep uncertainty, limitations, units, n, denominators and comparison basis when shortening manuscript content. Use supplied verified sources; search additional public background only when needed and log it. Reviewer criticism is not new scientific evidence. Summarize disagreements fairly.

Use [evidence sufficiency and reader-focused review](../galileo/references/quality-gates.md) for full decks. Check whether the audience has enough context to understand domain objects before detailed methods or results. A source-grounded example or conceptual view can explain dense evidence; use backup detail or faithful crops/annotations when the audience cannot read the needed labels. Missing outcomes remain missing, and assets with uncertain versions remain labeled as such. Content-only requests use only the relevant scope checks, without production records.

Reuse the manuscript's established terminology or resolve the relevant terms from authorized domain sources. Preserve standard English technical terms when customary in the discipline, even in another-language talk, and keep API/component/instrument names exact. Explain unfamiliar terms for the audience without renaming them; check headings, captions and speaker notes as well as slide bodies. A grammar pass alone is not a terminology check.

## Visual design and representative slides

For a rendered deck, read [visual design](references/visual-design.md). Support research-group, department, university and consortium identity: reuse supplied logos, brand guidelines, colors/fonts and templates, or verify official asset sources when the user requests branding without supplying them. Preserve logo proportions and documented usage, distinguish affiliation from sponsorship, and record font substitutions or unresolved assets. Reuse the supplied template or established project style. Otherwise propose two or three suitable visual directions in plain language and recommend one; use that recommendation as a provisional default when the choice is optional. Define a compact common style before production: palette and scientific color meanings, fonts, margins, recurring layouts and figure/citation treatment.

Build and render two representative slides from the storyboard, normally an introduction and a results slide, then check both visually and scientifically before expanding the deck. If no verified result is available, use a methods or conceptual slide; do not invent data to demonstrate a layout. Invite feedback without requiring a new approval for routine reversible design work, unless the user has requested approval first. These samples are part of the requested slide count. Preserve content-only and scoped-edit paths; they do not require this full production stage.

## Specialist production

Delegate scoped roles when authorized/supported, following the role reference and host concurrency. A science verifier checks central claims independently from the writer. A visual reviewer sees actual rendered slides, not only source code. Without separate contexts/rendering, report those limits.

Use editable native text/tables/charts when required and available. Keep original figures or regenerate from verified data with scientifically equivalent labels/scales; simplification must not hide inconvenient observations or uncertainty. Equations may be vector images if native math is unavailable, with editable formula source retained and the limitation stated.

Upstream scientific-slides proposes OpenRouter/Nano Banana generation and a default author name. This workflow does not activate those routes or use that author default. Use real user-supplied identity or unresolved fields. No mandatory generative/decorative images; never use generated imagery to recreate quantitative results. An image-only PDF is not an editable PPTX. Native charts are required when requested, not screenshots disguised as chart objects.

## Export, render, review, correct

Prefer host-native presentation tools under their applicable instructions. If a presentation or `pptx` skill is already available in the host, use it for actual PowerPoint/template operations; do not assume its dependencies or redistribute it as part of this MIT bundle. Otherwise use a documented local PPTX generator and actual renderer. Export final PPTX and derive PDF from that version when both are requested. Beamer is a separate PDF-first route; it does not yield editable PowerPoint automatically. Use a built-in compiler for supported standalone .tex files when available; no unnecessary TeX installation.

Render every final slide and inspect at presentation size and in an overview/contact sheet. Check overflow/overlap, font substitution, equation glyphs, citations, chart readability, accessibility, scientific fidelity, notes and total timing. Check PPTX/PDF count/order/content agreement, including animation/overlay flattening choices. Basic structural ZIP checks are not visual verification.

Loop writer/designer corrections → distinct scientific and visual checks → coordinator decision. Default maximum three rounds, stop after two without substantive progress or missing essential capability/evidence. Keep issues open honestly; do not label files presentation-ready without the relevant checks. Changing scientific content invalidates dependent figures/notes and returns to the science verifier.

At final handoff follow [revision-specific closure](../galileo/references/quality-gates.md#3-close-checks-against-the-delivered-revision): record artifact revision/hash, reviewer context, inspected slides/render size and outstanding issues for each check. Recheck downstream notes and exports after corrections. If a distinct reviewer becomes unavailable, identify coordinator self-review and keep required independent review pending rather than carrying an earlier pass to the changed deck.

## Delivery

Deliver requested PPTX/PDF if generated, editable source/build assets as appropriate, notes and timing plan if requested. Preserve references, attribution and figure licenses. Record state with sources/version, actual models/tools, review round, build outputs and pending issues. If conversion or compilation is unavailable, deliver supported source only and mark missing PDF/PPTX explicitly. No external sharing or journal submission.

## Saved state and continuation

When starting, resuming or handing off a run, follow [saved state and handoff](references/run-state.md). Save the current phase, artifact versions, actual checks, open issues and next action in the run directory.

## Optional project support

Use research-project when installed for a requested capability check, evidence-map audit, dependency-impact report or reproducibility package. All installation profiles include it. Read only the relevant operation's guidance; support scripts check records and bytes, not scientific meaning. Record affected artifacts in saved state and reverify them after substantive changes.
