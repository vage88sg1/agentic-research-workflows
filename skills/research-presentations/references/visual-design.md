# Visual design for scientific decks

Read this when producing a rendered deck or revising its visual design. A text-only outline or notes request does not require themes, sample-slide exports or design records. For a bounded edit to an existing deck, reuse its style and check affected slides rather than redesigning the full presentation.

## Choose or reuse a direction

Inspect a supplied PPTX/POTX, Beamer theme, reference slide or institutional style before proposing alternatives. Preserve required logos, layout and branding only from authorized supplied assets; do not fabricate affiliations. Reuse the existing choice on resume.

Without a prescribed template, propose two or three directions appropriate to the audience and recommend one. Examples:

- Academic minimal: neutral background, restrained accent, generous space for evidence.
- Conference visual: stronger message hierarchy and diagrams, preserving the detail needed to interpret results.
- Institution-aligned: the user's authorized palette, fonts and template adapted for projection.

Explain differences in ordinary language. This is a preference choice, not an installation/configuration form. Keep questions within the intake limit. If the user has not required design approval, proceed with the stated recommendation as a provisional default while offering the opportunity to change it. If approval is explicitly required, wait for it before expanding the deck; independent storyboard/evidence work can continue.

## Research-group and university identity

Support the user's research-group, department, university or consortium identity without making them configure technical fields. Reuse supplied logos, brand guidelines, palette/font specifications, sample slides and PPTX/POTX or Beamer templates. A brand-book PDF or screenshot can guide styling but is not an editable slide master. Ask only for the group/institution or material location if it is missing and relevant; reuse answers already given.

If the user wants institutional branding but has no assets, use available browsing to locate the institution's official brand guidelines and logo downloads. Verify the actual institution/group and asset source; follow documented usage terms and preserve source URLs or supplied asset provenance. A third-party search image is not a verified official logo. If official assets or use conditions cannot be established, leave the logo unresolved and continue with a clearly provisional neutral style rather than fabricate an emblem or imply endorsement. Do not require an extra approval if the user has already supplied authorized assets or requested this styling.

Prefer vector logos where the output tool supports them, otherwise an adequate-resolution transparent raster. Preserve proportions, prescribed variants, clear space and minimum sizes. Do not recolor, crop, distort or redraw a logo to match the deck unless the actual guidelines permit it. Match light/dark background variants and inspect their actual rendered clarity. Placement should be consistent and leave room for evidence, captions and source attribution; do not put a large logo on every slide merely because it is available.

Apply official colors to branding and accents while maintaining readable text and charts. Keep data-category colors consistent; brand colors are not automatically a sufficient accessible scientific palette. If required brand colors cannot serve as readable text or distinguish chart categories, use permitted neutral/secondary colors and redundant labels/markers, recording any necessary deviation. Use supplied/licensed fonts only when available; otherwise choose a compatible fallback, disclose substitutions and recheck layout. Do not silently download/install fonts or assume font embedding is permitted.

For multiple affiliations, preserve the user's specified hierarchy and official co-branding rules, with appropriately balanced size and spacing. Distinguish research affiliation, funding acknowledgments and sponsor/support logos; do not infer sponsorship or partner relationships from a logo. Use group-specific identity over generic university styling when supplied and allowed by the institution's requirements. Resolve only material conflicts with the user before final branding.

Keep a compact branding record in existing deck state/build records: institution/group names as supplied, logo/template/brand-guide sources and versions where known, approved variants/palette, font availability/substitutions, placement/co-branding decisions and remaining questions. Samples should demonstrate the actual header/footer, logo placement and chart treatment before full expansion. Final review checks identity and brand compliance separately from scientific claim validity.

## Define one common style

Keep a compact style specification in existing deck records or build-source constants, rather than creating a new administrative file for every small task. Include:

- Aspect ratio and safe margins; alignment/grid and spacing shared across slides.
- Background, text, accent and chart colors; stable mappings for scientific groups/variables. Check contrast and distinguish categories through labels/shapes as well as color.
- Title/body/caption fonts and sizes suited to the actual language, available fonts and presentation distance. Use a coherent hierarchy, not an arbitrary small-text fallback to fit content.
- Recurring layouts: opening, section transition when useful, methods/diagram, main result with interpretation, limitations and closing. Adapt these to the storyboard instead of forcing extra slides.
- Figure/table styles, axes/units/uncertainty, caption/source placement and notes conventions.

Use available scientific-slides guidance conditionally: `references/slide_design_principles.md`, `assets/powerpoint_design_guide.md` and `references/visual_review_workflow.md`; use scientific-visualization for data figures. Resolve them through the installed catalog or sibling skill directory. Their example paths/tools are not proof of availability. This workflow's editable-output, evidence and optional-service boundaries still apply.

## Check two representative slides before expansion

Choose slides from the actual storyboard: normally one introducing the question and one containing real results. If results are absent, use methods or a conceptual slide instead. The samples remain ordinary slides in the requested deck, not two additional deliverables. For a very short deck, check the available slides rather than forcing a two-slide sample. For an existing-deck revision, use representative affected slides.

Create samples in the selected canonical format using real supplied content and editable objects where requested. Render them with the intended engine, inspect at presentation size and in an overview, and verify central numbers, uncertainty, units and references against the evidence. Check hierarchy, density, alignment, contrast, font/glyph substitution, logo variants/proportions/clear space, co-branding and legibility of charts/citations. If rendering is unavailable, retain supported source and mark visual checking pending; never describe source-only inspection as rendered verification.

Show previews or links when supported and invite targeted feedback. Distinguish a designer's provisional choice, actual visual/scientific checks and any explicit user approval. Correct sample issues before applying the shared style to the full deck. Do not block independent content work on an optional aesthetic preference. Sample checks do not replace final inspection of every slide and reconciliation of PPTX/PDF.

## Apply consistently and revise only what changed

Apply the style through template/master layouts or shared build constants where the production tool supports them. Keep chart category colors stable across slides and avoid decorative effects that obscure evidence. Split or simplify overloaded content while preserving scientific qualifiers; do not shrink essential labels beyond readability or hide uncertainty to achieve a cleaner layout. Use native text/tables/charts when requested and available.

Record the chosen direction, actual template/source, style version, representative slide IDs and performed checks in existing presentation state. Style/font changes invalidate affected render checks; evidence/data changes also return to scientific verification. Continue within the existing three-round/two-without-progress limits rather than creating a second unbounded aesthetic review loop.

## Optional host PowerPoint skill

Prefer a relevant presentation or `pptx` skill already supplied by the harness for template preservation, editing and technical checks, following its actual tool/dependency instructions. The external [Anthropic pptx skill](https://github.com/anthropics/skills/blob/main/skills/pptx/SKILL.md) is one possible capability and has [separate proprietary terms](https://github.com/anthropics/skills/blob/main/skills/pptx/LICENSE.txt). It is not copied or installed by Galileo. Use an available licensed host capability; otherwise retain the documented PPTX/Beamer fallback with honest build/QA status. Do not assume that a skill written for one host has its dependencies installed in another, or that a technical check establishes visual/scientific quality.
