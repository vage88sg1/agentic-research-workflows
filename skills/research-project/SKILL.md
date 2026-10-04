---
name: research-project
description: Inspect project capabilities, maintain a claim-evidence dependency map, identify artifacts affected by changed inputs, check final delivery records, and assemble an explicitly selected reproducibility package. Use for cross-workflow project checks and traceability; not for certifying scientific validity.
license: MIT
---

# Research project support

For role/model selection, follow [installed model preferences](../galileo/references/model-settings.md). Reuse explicit project choices and the shared installation mapping; distinguish requested models from actual host execution. Bounded edits need no model-setup interview.

Use this support workflow for preflight, evidence mapping, change impact, final delivery-record checks or reproducibility packaging. Ask which operation is needed only if it cannot be inferred. Read [tool usage and schemas](references/project-tools.md) before running the bundled Python CLI. It uses the standard library, requires Python 3.10+, and remains available after skill installation.

## Check the actual environment

Run `scripts/research_tools.py preflight` from this skill's directory. Binary discovery does not establish working tools or supported versions. Supplement the report with capabilities actually exposed by the host: independent contexts, selected models, browsing/MCP, native document/slide renderers and LaTeX compiler. Do not run every route or install runtimes at intake. Check only the requested route with a small authorized example, record actual result/diagnostics and use native tools when available. For Office deliverables, apply the relevant [native feature and functional checks](../galileo/references/office-capabilities.md); tool presence, successful export and native feature behavior are separate capabilities. For LaTeX/Beamer, distinguish the [compiler, bibliography/index backends and inspected PDF](../galileo/references/latex-capabilities.md); a discovered TeX binary does not establish template/package compatibility. Classify each capability as discovered, tested, unavailable or not tested; report fallback sequential roles/source-only production honestly.

## Build and assess the evidence map

Use `assets/research-map.json` as a schema example, not as scientific evidence. Give sources, claims and artifacts stable unique IDs. Record original source identifiers, consulted material/access level, local content hashes when applicable, locators, supporting/contradicting/context relations, verifier and check date. For a result source, record its executed analysis provenance. A checksum identifies bytes; it does not establish authenticity, source quality or correct interpretation.

Run the `evidence` check to detect structural gaps, pending checks and metadata-only support. Then have an evidence verifier inspect the consulted passage/result against the actual claim's population, design, direction, magnitude and uncertainty. Record rationale and conflicting evidence. The script does not infer semantic entailment or verify the stated human identity. Do not mark human_verified without an actual identified human check; use ai_checked for assistant assessment. Check corrections/retractions as relevant through current authorized sources.

## Propagate changes

Keep `depends_on` IDs for tables, figures, manuscript sections and slides, plus claim-to-source links. Use `impact` with the project root; it compares recorded local hashes and accepts explicit changed IDs for remote/new versions. The report includes indirect dependents, even when their current file bytes have not yet changed. Missing/unsafe files also require recheck. Only tracked dependencies can be discovered.

Copy impacted IDs into the issue/state records as requiring recheck, rerun affected analysis when authorized, then verify dependent claims/artifacts. Preserve prior maps and source files. Rebaseline hashes only after corrected content and checks are recorded; merely updating a checksum is not a correction. Impact reporting never silently rewrites state, evidence or a manuscript.

## Check a final delivery record

Run `delivery` with the selected state snapshot and project root after reading its format in [tool usage](references/project-tools.md#delivery-record-check). It compares current output/check hashes, checks referenced required review records and distinguishes recorded readiness from operational completion. It does not update hashes, repair state, render files, execute analysis or establish scientific validity. Resolve affected checks before rebaselining; preserve historical snapshots and keep one clearly identified current register. The assistant maintains this record for tracked final work, not another configuration task for the user.

## Assemble reproducibility materials

Use `assets/reproducibility-manifest.json` to select individual files with author-reviewed public/synthetic sharing classification and expected hashes. Include code, environment/dependency records, README commands, figure-generation inputs and license/access information appropriate to scope. Exclude restricted data, secrets and licensed full texts not authorized for redistribution. Supply access instructions and limitations for excluded inputs; a package with unavailable inputs is not independently reproducible merely because code is present.

Run `bundle` into a new destination. It copies only listed files and records their hashes; reproduction commands are documented, never executed by the packager. Inspect the assembled payload before any separately authorized sharing. To claim computational reproduction, actually rerun the recorded commands in the agreed environment and compare outputs using justified exact/numerical tolerances. Keep packaging, analysis execution and independent reproduction as separate statuses.

## Roles and delivery

A coordinator maintains records, an economical metadata assistant can populate IDs, a balanced evidence verifier checks claim support, and an execution specialist handles real runs. Use stronger reasoning for a specific unresolved methodological risk. Save reports, unresolved issues and [run state](references/run-state.md). Return a concise capability/evidence/change/delivery/bundle summary and the next actionable gap, not a global scientific approval.
