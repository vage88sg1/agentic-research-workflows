---
name: research-drafting
description: Draft or resume an evidence-traceable research paper, thesis, dissertation, or report using progressive intake, specialist roles, measurement checks, reproducible analysis and internal review. Use for scientific drafting workflows; do not perform journal submission.
license: MIT
---

# Research drafting

Read [agent contracts](references/agent-contracts.md) and [skill integration](references/skill-integration.md). Use the user's language, discipline, institution and venue requirements; do not assume a particular country, field, study design or dataset. This workflow can be invoked through a host's skill/slash picker, explicitly by name, or as plain instructions.

## Intake and continuation

Inspect only relevant authorized inputs. Locate the user's selected output directory and saved `workflow_state.json`; otherwise propose `research_workspace/`. Never silently overwrite inputs or an existing run. Record effective tools/models and missing information. Resume from state rather than repeating completed work.

Ask up to three focused questions at a time, starting with research question, document type, stage and available materials. Then resolve design, analysis unit, sample, groups/overlap, repeated measurements, instruments/versions/manuals, outcomes, covariates and missingness as relevant. Resolve writing language, manuscript format (DOCX or LaTeX), requested PDF, institutional/venue requirements, existing protocol/analysis plan and processing boundary. Reuse documented answers; do not ask every possible question when irrelevant.

Continue independent outlining or public-source searches while awaiting answers. Block only dependent scoring, analysis or factual drafting. Distinguish unavailable results from incomplete prose; never make up a plausible study. A plan written after results were examined is not a preregistration.

## Delegation and evidence

When the user requests an agentic workflow and the host permits it, delegate roles from the contracts. Use targeted inputs and separate outputs; the coordinator integrates the master. Without delegation, state that roles are sequential in one context. Do not open new user-owned chats or purchase services as an implicit side effect.

Read relevant installed bundled skills before applying them. Use literature-review for scope, search/selection/extraction and thematic synthesis; citation-management for metadata and bibliography; scientific-critical-thinking for bias, alternatives and bounded inference. A narrative background is not a systematic review. Record queries, dates, coverage limits, full-text availability and selection decisions proportionate to the review type.

Maintain source and claim records with IDs, exact support/locator, material actually consulted and verification status. Distinguish metadata validity, AI inspection and completed human verification. Search snippets and fluent summaries are not verification. Check corrections/retractions when relevant; never invent bibliographic identifiers or attribute checks to humans who did not perform them.

## Measurement, analysis and figures

Verify measurement rules from the actual instrument/manual: language/version, population, reverse coding, scale range, subscales, missing-item rules and thresholds. Screening scores do not establish diagnoses; reliability alone does not establish validity. Preserve originals and transformation/exclusion records.

Use statistical-analysis with critical assessment: define the question/estimand, design, dependence, missingness, precision, multiplicity and confounding before selecting methods. Do not choose tests mechanically from one normality p-value, claim effects exist from p-values, or claim equivalence from nonsignificance. Distinguish planned and exploratory work; do not try tests until significance appears.

Execute analysis only with authorized inputs and tools. Save code, commands, environment, seeds, outputs and deviations. Without execution mark reproduction NOT PERFORMED. Use scientific-visualization only for justified, provenance-bound displays; specify units, denominators, n, uncertainty and missingness. Quantitative figures derive from executed data, not generative images.

## Draft and internal audit

Apply scientific-writing: evidence-linked outline first, then venue/design-appropriate prose. Prefer methods/results before final discussion, abstract and title when suitable; do not force IMRAD onto every document. Keep unsupported facts and declarations in an unresolved register rather than plausible boilerplate.

Reconcile repeated numbers, units, populations, time points, methods, results, tables and figures. Select reporting guidance from the actual design and verify official/current documents. Coverage checks do not certify methodological validity or compliance. Use bundled CLIs only after reading their schema/help and verifying dependencies; record actual execution and limitations.

Run internal source/consistency and methodological checks with distinct verification where possible. Correct affected records before prose and regenerate dependent outputs. Preserve author decisions and unresolved issues. No automatic human approval, real submission-ready certification, external disclosure or submission.

## Conditional format production

After the scientific draft is checked, use the installed research-typesetting skill for the selected manuscript format, or compatible host tools with explicit limitations. Load academic-writing-latex only for LaTeX. Do not activate a compiler or generate both authoring formats unasked. Preserve verified content and inspect the final rendered artifact.

## Outputs

Save project configuration, study summary, source/claim records, bibliography, measurement records, analysis code/output where available, draft, issues and state. Report missing inputs, checks performed, limits and next action. Offer research-review as a separate invocation rather than starting simulated editorial review unasked.

## Saved state and continuation

When starting, resuming or handing off a run, follow [saved state and handoff](references/run-state.md). Save the current phase, artifact versions, actual checks, open issues and next action in the run directory.

## Optional project support

Use research-project when installed for a requested capability check, evidence-map audit, dependency-impact report or reproducibility package. All installation profiles include it. Read only the relevant operation's guidance; support scripts check records and bytes, not scientific meaning. Record affected artifacts in saved state and reverify them after substantive changes.
