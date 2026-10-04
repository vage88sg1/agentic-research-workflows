---
name: research-drafting
description: Draft or resume an evidence-traceable research paper, thesis, dissertation, or report using progressive intake, specialist roles, measurement checks, reproducible analysis and internal review. Use for scientific drafting workflows; do not perform journal submission.
license: MIT
---

# Research drafting

For role/model selection, follow [installed model preferences](../galileo/references/model-settings.md). Reuse explicit project choices and the shared installation mapping; distinguish requested models from actual host execution. Bounded edits need no model-setup interview.

For a full drafting project, read [agent contracts](references/agent-contracts.md) and [skill integration](references/skill-integration.md). For a bounded edit, start with the scoped path below and load further guidance only if a substantive issue requires it. Use the user's language, discipline, institution and venue requirements; do not assume a particular country, field, study design or dataset. This workflow can be invoked through a host's skill/slash picker, explicitly by name, or as plain instructions.

## Scoped editing path

When the user supplies text and asks only for style, clarity or a bounded revision, edit that text directly. Preserve requested structure, numbers, units, qualifiers, citations and meaning; compare against the original. Do not start full study intake, bibliography discovery, model selection or simulated review. Ask a targeted question only if an ambiguity prevents a faithful edit. Flag an observed scientific inconsistency rather than silently changing the underlying result.

Preserve exact technical identifiers and the discipline's established terminology, including customary English terms in other-language prose. Do not replace them with improvised translations; accepted local equivalents and the user's convention guide the choice. For a scoped edit, check this directly without creating a glossary or extra role.

Return the requested corrected file (or text in chat) with a brief account of meaningful edits. Keep the original intact. Do not create new configuration, state, issue or diff files for a one-off task unless requested or needed to update an existing tracked run. The full-project output/state sections below apply to resumable research projects, not mandatory scaffolding for every edit.

## Intake and continuation

Inspect only relevant authorized inputs. Locate the user's selected output directory and saved `workflow_state.json`; otherwise propose `research_workspace/`. Never silently overwrite inputs or an existing run. Record effective tools/models and missing information. Resume from state rather than repeating completed work.

Ask up to three focused questions at a time, starting with research question, document type, stage and available materials. Then resolve design, analysis unit, sample, groups/overlap, repeated measurements, instruments/versions/manuals, outcomes, covariates and missingness as relevant. Resolve writing language, manuscript format (DOCX or LaTeX), requested PDF, institutional/venue requirements, existing protocol/analysis plan and processing boundary. Reuse documented answers; do not ask every possible question when irrelevant.

Continue independent outlining or public-source searches while awaiting answers. Block only dependent scoring, analysis or factual drafting. Distinguish unavailable results from incomplete prose; never make up a plausible study. A plan written after results were examined is not a preregistration.

For full projects, use [evidence sufficiency](../galileo/references/quality-gates.md#1-decide-what-the-materials-can-support) before factual drafting and revisit it before production. Identify the intended product and its essential information, including the author's contribution for a thesis about completed work. Classify gaps as missing, ambiguous, uninspected or present-but-excluded; ask targeted questions and wait for answers before dependent factual drafting. Honor intentional source restrictions without silently substituting a reconstruction for the requested thesis. Unresolved essentials block final readiness; retain a provisional draft and resolve the gaps rather than completing methods/results with plausible text or blanket caveats.

Use [objective, section and bibliography completeness](../galileo/references/content-completeness.md) for full projects. Keep the objective/contribution map in existing notes; assess substantive answers, not heading or citation counts. Reconsider the outline and dependent sections after changes to title, objectives or attributed contribution.

## Delegation and evidence

When the user requests an agentic workflow and the host permits it, delegate roles from the contracts. Use targeted inputs and separate outputs; the coordinator integrates the master. Without delegation, state that roles are sequential in one context. Do not open new user-owned chats or purchase services as an implicit side effect.

Read relevant installed bundled skills before applying them. Use literature-review for scope, search/selection/extraction and thematic synthesis; citation-management for metadata and bibliography; scientific-critical-thinking for bias, alternatives and bounded inference. A narrative background is not a systematic review. Record queries, dates, coverage limits, full-text availability and selection decisions proportionate to the review type.

Actively check literature coverage of the outline and resolve material external-knowledge gaps through [targeted source searches](../galileo/references/quality-gates.md#resolve-literature-gaps-actively) with available authorized tools. Read and verify claim support, not only citation metadata; preserve search/access records. For actual project methods or results, request the author/source instead of treating published work as a substitute. Search unavailable or essential sources inaccessible means dependent claims stay unverified and final readiness pending; do not invent bibliography or ask the user for general references that available tools can find.

Maintain source and claim records with IDs, exact support/locator, material actually consulted and verification status. Distinguish metadata validity, AI inspection and completed human verification. Search snippets and fluent summaries are not verification. Check corrections/retractions when relevant; never invent bibliographic identifiers or attribute checks to humans who did not perform them.

When this step needs external literature, identifier checks or an authorized reference library, follow [literature connection recommendations](../galileo/references/literature-connections.md). Offer relevant MCP connections if equivalent tools are unavailable; reuse the coordinator's recorded choice. Do not propose setup for a task fully supported by supplied sources.

## Measurement, analysis and figures

Verify measurement rules from the actual instrument/manual: language/version, population, reverse coding, scale range, subscales, missing-item rules and thresholds. Screening scores do not establish diagnoses; reliability alone does not establish validity. Preserve originals and transformation/exclusion records.

Use statistical-analysis with critical assessment: define the question/estimand, design, dependence, missingness, precision, multiplicity and confounding before selecting methods. Do not choose tests mechanically from one normality p-value, claim effects exist from p-values, or claim equivalence from nonsignificance. Distinguish planned and exploratory work; do not try tests until significance appears.

Execute analysis only with authorized inputs and tools. Save code, commands, environment, seeds, outputs and deviations. Without execution mark reproduction NOT PERFORMED. Use scientific-visualization only for justified, provenance-bound displays; specify units, denominators, n, uncertainty and missingness. Quantitative figures derive from executed data, not generative images.

## Draft and internal audit

Apply scientific-writing: evidence-linked outline first, then venue/design-appropriate prose. Prefer methods/results before final discussion, abstract and title when suitable; do not force IMRAD onto every document. Keep unsupported facts and declarations in an unresolved register rather than plausible boilerplate.

### Section-by-section development

Prefer a staged draft for full manuscripts and theses rather than producing the entire text in one pass. Agree an evidence-linked outline and a proportionate length plan; reuse requirements and prior answers. Propose starting with a provisional introduction/context when useful, then domain foundations, methods or implementation, actual results/evaluation, discussion and conclusions in the document’s appropriate order. The writing order need not match the reading order: defer definitive abstract, conclusions and introduction claims about findings until the underlying sections are checked. Never force an empirical structure onto an implementation thesis.

Ask once whether the user prefers checkpoints after each chapter/major section or autonomous progression through the agreed plan; honor the answer and whole-draft requests. Checkpoint mode delivers the current section with focused questions and waits for feedback before the next dependent section. Autonomous mode proceeds after section checks without repeated permission requests; essential factual gaps still require answers. If the preference is not yet available, prepare the outline and first source-supported section only, not the whole manuscript. Small edits keep their scoped path.

Before each section, check its purpose, dependencies, available project facts and literature coverage; search resolvable external-knowledge gaps and ask about missing project facts before writing dependent claims. Draft that section, then check exact claim support, methods/results consistency, terminology, reader usefulness and relevant figures/citations. Correct blocking findings before propagating claims into subsequent sections. Record section status and unresolved questions in existing project notes/state; do not create a mandatory file per section. Reopen affected earlier sections when new information changes their support. Section passes do not replace independent central evidence review or final whole-document consistency and rendered-output QA.

Before expanding each major section, apply its purpose and minimum explanation from the shared completeness reference. Include a supported operational example when useful; label synthetic examples and retrospective design analysis honestly. Audit bibliography coverage by topic/claim and source type, then reconcile in-text citations and bibliography in both directions. Use the domain reviewer for a reader-focused assessment of missing explanations, without another default agent.

Reconcile repeated numbers, units, populations, time points, methods, results, tables and figures. Select reporting guidance from the actual design and verify official/current documents. Coverage checks do not certify methodological validity or compliance. Use bundled CLIs only after reading their schema/help and verifying dependencies; record actual execution and limitations.

Run internal source/consistency and methodological checks with distinct verification where possible. Correct affected records before prose and regenerate dependent outputs. Preserve author decisions and unresolved issues. No automatic human approval, real submission-ready certification, external disclosure or submission.

Then run the separate [reader-focused review](../galileo/references/quality-gates.md#2-separate-evidence-review-from-usefulness-to-the-reader): reconcile document type, title and conclusions; introduce domain terms; remove unnecessary repetition and move production commentary to provenance unless it is the subject. Keep author-reported historical results, actually reproduced results and proposed checks distinct. Version-ambiguous assets do not establish one historical release. Follow [revision-specific closure](../galileo/references/quality-gates.md#3-close-checks-against-the-delivered-revision) for tracked outputs; a review of an earlier draft is not a pass for changed content.

Include a terminology pass distinct from grammar: use a compact shared term list for recurring/ambiguous vocabulary, preserve standard names and code identifiers, and reconcile manuscript, figures and slides. The copyeditor may perform this scoped pass; unresolved meaning changes go to the domain reviewer rather than a fluent but unverified translation. No extra agent is required for an ordinary language edit.

For full scientific final delivery, unresolved central evidence, methods/results contradictions, unverified central citations or major terminology/visual errors block readiness. Use a reviewer distinct from the writer for central evidence/method checks when supported; record that check as pending when unavailable. Apply the final-readiness conditions in the shared reference, with no automatic pass at a round, time or cost limit. A finished file or provisional draft is not automatically a verified final manuscript.

## Conditional format production

After the scientific draft is checked, use the installed research-typesetting skill for the selected manuscript format, or compatible host tools with explicit limitations. Load academic-writing-latex only for LaTeX. Do not activate a compiler or generate both authoring formats unasked. Preserve verified content and inspect the final rendered artifact.

## Outputs

As a full project develops, save relevant project configuration, study summary, source/claim records, bibliography, measurement records, actual analysis code/output, draft, issues and state. Initial planning can start with a useful study note and compact state; create further records when there is substantive content to save, rather than empty ledgers. Report missing inputs, checks performed, limits and next action. Offer research-review as a separate invocation rather than starting simulated editorial review unasked.

## Saved state and continuation

When starting, resuming or handing off a run, follow [saved state and handoff](references/run-state.md). Save the current phase, artifact versions, actual checks, open issues and next action in the run directory.

## Optional project support

Use research-project when installed for a requested capability check, evidence-map audit, dependency-impact report or reproducibility package. All installation profiles include it. Read only the relevant operation's guidance; support scripts check records and bytes, not scientific meaning. Record affected artifacts in saved state and reverify them after substantive changes.
