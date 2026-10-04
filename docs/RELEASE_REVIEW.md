# Release preparation review

## Changes from the private prototype

- English entry points named research-drafting/research-review; output language, field, design, institution, venue and processing boundary come from intake.
- No country-specific access service, clinical cohort, personal filesystem path, original conversations or project-specific documents in the release.
- The workflow skills are self-contained with relative references, and the installer installs the scientific skills alongside them.
- Configurable roles, review count, limits, provider/model mapping and cost profiles; model recommendations are not asserted benchmarks or fixed-price guarantees.
- Explicit distinctions between instructions and execution engine, installed and discovered, context separation and access enforcement, AI inspection and human verification, simulation and actual review/submission.
- Pinned upstream content, full license notice, version inventory, file hashes and non-overwriting offline installation.
- Watermark removal and unrelated experimental services are excluded: they are outside scientific drafting/review scope.

## Validation boundary

Installer behavior, package links, skill structure and provenance are checked locally and in the supplied CI workflow. The synthetic behavioral protocol is not a completed empirical evaluation. No live dataset, paid service, real journal submission or external manuscript transfer is used in release preparation. Host discovery/parallelism and scientific performance must be checked in each deployment.

Local release checks passed: five installer tests (dry-run, full installation, collision preservation, tampered-content rejection and copy-failure rollback), package/provenance/link validation, and the Codex skill-creator structural validator for both original entry points. No CI run is implied by these local results.

## Format and presentation extension (2026-09-27)

Added conditional DOCX/LaTeX typesetting, a scientific presentation workflow with PPTX/PDF and PDF-only Beamer routes, and two MIT upstream support skills found online. Four original entry points and nine upstream skills are now available. Separate core/docx/latex/slides/full installation profiles preserve non-overwrite behavior.

LaTeX source provenance and license differ from K-Dense and are recorded per skill; the installer copies the correct license. Six installer tests pass, including conditional-profile exclusion and distinct license/source preservation. Both new original skills passed the skill-creator structural validator; package validation and whitespace checks passed. No end-to-end document or deck production is claimed by these packaging checks.

## Optional literature integrations (2026-09-27)

Added independent MCP configuration examples for PubMed/Europe PMC, OpenAlex, Crossref and experimental Zotero. Source commits and top-level npm versions are pinned; transitive dependencies are explicitly not locked. npm registry metadata confirmed all three selected versions and Node 24+ requirements. No adapter source is redistributed. No global client configuration or private library was accessed or modified.

Codex entries remain disabled and optional, with retrieval-tool allowlists; JSON client fragments require host-specific permission setup. Startup indexing risk in Zotero is documented and the probe refuses an existing semantic startup config. Drafting/review instructions include source routing, budget tracking and query/access records. The connection diagnostic only initializes and lists tools.

Twelve tests passed under bundled Python 3.11+, along with offline catalog, package provenance/link and whitespace checks. The system Python lacked tomllib, so the complete suite was rerun with the bundled runtime. MCP protocol tests use local fake servers, including paginated tool discovery, missing tools, malformed output, server error and timeout. No live server connection, upstream API search, full-text access or client permission enforcement is claimed.

## Final package review (2026-09-27)

Reviewed the installer, profile inventory, workflow entry points and references, README instructions/diagrams, MCP examples/diagnostic and validation coverage.

### Findings corrected

- **Untracked vendor payloads:** checking listed hashes alone allowed extra files to be copied. Installation and package validation now reject a vendor inventory that differs from provenance. A regression test adds an unexpected executable file and confirms rejection before destination writes.
- **Installed artifact traceability:** installed manifests identified upstream revisions but did not hash the installed payload. They now include SHA-256 values for copied files and retained license, excluding the manifest itself. This records file identity, not cryptographic authorship/authenticity.
- **Resume and handoff ambiguity:** all four workflows now ship a self-contained saved-state contract. Review and presentation runs must preserve drafting state, record actual checks and invalidate dependent checks after input changes. Starter state and issue-ledger templates are available in examples.
- **Stale support-skill wording:** references now describe profile-selected support skills rather than assuming a fixed seven-skill installation.

### Checks completed

Fourteen automated tests passed, including the two new installation regressions; vendor provenance, local links, MCP configuration, whitespace and the four original skill structural checks passed. Full tests used bundled Python with tomllib; the skill structural validator used the system Python with PyYAML. No dependency installation was needed.

### Remaining validation work

| Priority | Remaining check | Evidence needed before claiming completion |
|---|---|---|
| Before calling the workflows operationally validated | Run the synthetic protocol through drafting and simulated review in a supported host | Saved artifacts, actual agent/context/model records, expected issues detected, correction verification and stop behavior |
| Before claiming verified format production | Produce and inspect DOCX/PDF, LaTeX/PDF and PPTX/PDF samples | Real builds, rendered pages/slides, editability and cross-format checks |
| Before claiming working literature access | Connect each selected adapter and perform a small public search/identifier lookup | Runtime/version, actual response status, client allowlist check and access limitations; Zotero requires separate startup inspection |
| Before recommending a cost-optimal mapping | Compare economy/balanced/quality on the same synthetic task | Defects caught/missed, actual usage/cost where available and time; model names alone are insufficient |

The package is suitable for documented experimental use. Packaging checks are not evidence of end-to-end scientific performance. Remaining items are explicit validation gaps, not features to silently mark as complete. Real journal submission remains outside the project's intended scope.

## Lifecycle extensions (2026-09-27)

Implemented all proposed feature areas: environment preflight, evidence mapping, dependency-based change impact, explicit reproducibility packaging, thesis-to-article conversion, defense rehearsal, local submission dossier preparation and a separate systematic-review workflow.

The package now contains nine original entry points and nine unchanged upstream skills. Research project is included in every profile; publishing, defense and systematic profiles are added. Support scripts and templates ship inside the skill, so they work after installation without relying on repository-relative paths. Main/Italian documentation, installation counts and separate workflow diagrams were updated.

### Concrete validation

- 27 automated tests passed. New cases cover claim-evidence record gaps, graph integrity, indirect impact and missing files, path/symlink rejection, allowlisted bundle copying, restricted/credential paths, hash mismatch, failed-copy cleanup, no execution by preflight/packaging, and portable execution after profile installation.
- The bundled synthetic example was actually analyzed and packaged, then its recorded analysis was rerun from the package. The regenerated result matched the original bytes (four artificial values, arithmetic mean 7.0). This is a software example, not research data or scientific performance evidence.
- All nine original skill structures passed the skill-creator validator. Package/local-link/vendor-provenance and whitespace checks passed.
- An independent agent executed the new thesis-to-article skill on a synthetic cross-sectional summary. Its artifacts retained 80 recruited versus 60 completers and the supplied correlation, identified the inconsistent abstract denominator, replaced unsupported causal wording with association, and left missing methods/scoring/declarations unresolved. It produced an outline, provisional draft, conversion map, word counts, issues and resumable state in an isolated temporary workspace. This was one sequential-role execution by a separate evaluator, not independent scientific peer review. The exercise prompted an explicit “corrected” transformation category in the skill.

### Boundaries that remain

Preflight cannot infer host capabilities from PATH alone. The evidence script checks structure and recorded status; semantic claim support needs actual source assessment. Impact tracking requires registered dependencies. Packaging does not itself execute research code or establish lawful disclosure/independent reproduction. Systematic-review decisions, extraction, appraisal and flow counts must come from work actually performed; the included templates do not execute a review.

Complete host trials of defense interaction, submission preparation and systematic review, full scientific datasets, real DOCX/LaTeX/PPTX/PDF production, external MCP searches and model-cost comparisons remain unperformed. The new bounded tests narrow earlier validation gaps without closing those broader ones. No submission, registration, personal data processing or live external service activation was performed.

## Guided entry point and simpler onboarding (2026-09-27)

Added Galileo as the recommended everyday entry point. It routes a plain-language goal to the relevant installed specialist instructions, reuses their coordinator/state, asks only the next necessary questions and does not run all workflows by default. Scoped edits remain scoped; simulated editorial review and systematic review require their corresponding intent. Authorized multi-stage requests can proceed across internal handoffs without requiring repeated invocations.

The README and Italian guide now focus on getting started, example requests and resuming. The detailed workflow descriptions and nine specialist diagrams moved to WORKFLOW_GUIDE.md. Direct specialist entry points remain available; this change does not hide entries in clients that list every skill.

All installation profiles include the Galileo entry point. Full installation contains 19 directories: Galileo, nine specialist workflows and nine upstream support skills. Existing installations are not silently overwritten. Twenty-seven automated tests, package/link checks, whitespace checks and the new skill structural validator passed. These checks verify packaging and integrity; no separate behavioral routing benchmark or cross-client UI trial is claimed.

## Scope-sensitive usability corrections

Three synthetic first-turn scenarios and three fresh-context repetitions were completed. Initial thesis planning kept three necessary questions while reducing work artifacts from five to a planning note and compact state. A bounded language edit and Markdown slide-content request asked zero questions and each delivered one work artifact after the corrections. Counts exclude evaluation transcripts/logs and input copies. Source numbers and scientific qualifications were compared against the synthetic material; slides had six sections and an estimated eight-minute plan.

Galileo, drafting and presentation guidance now explicitly scope administrative records and export setup to the requested work. The slide exercises also exposed automatic insertion of an unverified support-library academic citation. A primary-record verification/omission rule was added. Its extra independent retest failed to start due to a host usage limit, so only structural checking is claimed for that final rule.

See [usability exercises and limits](USABILITY_TESTS.md) for the cases, counts and evaluation boundary. These are agent simulations, not real-user usability or performance benchmarks.

## Proactive, extensible MCP recommendations (2026-09-27)

Galileo now offers relevant literature connections when a task benefits from them and equivalent tools are unavailable. Drafting, review, systematic-review and presentation entry points share an installed recommendation reference. Choices carry across handoffs/resume; supplied-source editing and formatting do not trigger unrelated setup. The bundled catalog is a starting point: other task-relevant MCPs can be discovered from current primary documentation, with linked recommendations and explicit unbundled-candidate status.

Recommendations do not install or activate services. Selected setup uses the actual harness, preserves existing configuration and records real discovery/test status. Public server pins/catalog and MCP configuration examples are unchanged.

Nine installer tests, package/link/provenance validation, offline MCP configuration checks, the Galileo skill structural validator and whitespace checks passed. A temporary full installation confirmed that the shared reference and specialist links survive copying. These are packaging checks; proactive recommendation behavior, external-server discovery and live connections have not been independently exercised in this update.

## Slide design and institutional identity (2026-09-27)

The presentation workflow now includes visual-direction selection, a common style specification and representative rendered slides before full-deck expansion. Samples belong to the requested storyboard/count and require real supplied evidence; methods/concept slides substitute when results are absent. Optional preferences do not require an approval stop unless requested. Content-only work and bounded edits retain their simpler paths.

Group/university/department/consortium identity can use supplied assets/templates or verified official guidelines: logo variants/proportions/clear space, palette, fonts/substitutions, placement and co-branding are tracked and reviewed. Scientific chart semantics and readability take precedence over decorative palette reuse. An available host presentation/pptx skill is optional; external proprietary skills are not redistributed or installed. Vendor payloads and profile counts are unchanged.

Nine installer tests, package/link/provenance and whitespace checks, and the presentation skill structural validator passed. A temporary slides-profile installation confirmed the new design reference survives copying. The workflow diagram, role responsibilities, QA and saved-state guidance were aligned. No new rendered deck, institutional-brand compliance trial or independent behavioral evaluation was performed for this update.

## Evidence, literature, terminology and staged drafting (2026-09-27)

Added shared delivery guidance for essential input sufficiency, active targeted literature-gap searches, disciplinary terminology, reader usefulness and revision-specific QA. Missing project facts require focused questions and answers; public literature is consulted for external knowledge and cannot establish project methods/results. Central unsupported claims, invented facts/references and unresolved substantive contradictions block final readiness. Required independent review remains pending if unavailable; a review/cost limit cannot produce automatic acceptance.

Full manuscripts/theses now default to an agreed outline and section-by-section development, with interactive chapter checkpoints or autonomous progression according to the user’s choice. Each section checks facts, literature and dependencies before drafting, then evidence, terminology and communication before expansion. Abstract/conclusions are finalized after their underlying findings; whole-document and final-render review remain necessary. Bounded edits retain their simpler path. These are agent instructions, not a new executable enforcement engine or a guarantee of scientific correctness.

### Checks performed

- The existing 27 automated tests passed during this update. Package/local-link/vendor-provenance checks, all ten original skill structural validators and whitespace checks passed after the instruction changes. Upstream skill payloads remain unchanged.
- Fresh installations in all eight profiles retained the exact shared quality reference and valid installed-file hashes. Profile counts and the non-overwriting installer behavior are unchanged.
- A separate evaluator completed three synthetic bounded cases: thesis intake asked three focused project questions without inventing implementation/results; technical editing preserved identifiers and the limitation while correcting terminology; changed-version handoff verified the old review hash and left required independent final review pending. These cases exercised an earlier revision in this update, before the final literature/staged-drafting additions; they are not claimed as a fresh repetition of all final wording.
- One additional fresh exercise used the updated source instructions: an Italian introduction with chapter checkpoints and no supplied background bibliography. The evaluator actually searched public technical sources, consulted two Spring reference pages and an original technical design essay, wrote a supported provisional introduction/outline and asked three continuation questions. It stopped before the next chapter, recorded consulted passages/access limits and hashes of the instruction files used. It did not invent an implementation or present source inspection as human verification.

These four cases used one separate evaluator with sequential workflow roles; they are bounded behavioral exercises, not independent scientific peer review, a cost benchmark, a full-thesis rerun or compatibility certification across harnesses. The final case used web search, not a live MCP adapter. No private research material is included in the public validation report. Full rendered-document/deck trials under the new gates and broader host/cost comparisons remain unperformed.

## Objective fulfillment, bibliography coverage and delivery records (2026-09-27)

Full drafting and substantive review now map objectives to sections, attributed contribution, permitted evidence and verification. Section purpose/minimum explanation, supported central examples, a fresh-reader pass through the existing domain reviewer, appropriate bibliography source types and citation/reference checks in both directions complement claim-level accuracy. Changes to objectives, title or contribution reopen affected sections. Scope and source limits cannot silently turn a completed-work thesis into a reconstruction or proposal. Bounded edits retain their simpler path; no citation quota or extra mandatory reviewer is introduced.

Tracked final handoffs distinguish operational completion from content, bibliography, review and production readiness. The new offline `delivery` command checks selected file hashes, active check revisions, required checks, recorded independence when required and current output coverage. It preserves inputs and cannot renew a historical review by updating its checksum. It establishes record consistency only, not scientific validity, genuine reviewer independence or human approval. Assistants maintain the register from actual work rather than asking users to fill another form.

### Checks performed

- All 38 automated tests passed, including 11 new delivery tests for valid/stale records, pending readiness, missing or non-passing checks, required independence, superseded history, output coverage, unsafe paths and installed-script behavior.
- Package/local-link/vendor-provenance checks, all ten original skill structural validators and whitespace checks passed. All eight fresh profile installations retained exact shared quality/completeness references and the delivery script, with valid installed-file hashes. Upstream support payloads are unchanged.
- A separate evaluator completed two bounded synthetic exercises using the updated shared guidance. A technical thesis completion assessment identified missing implemented rules, author attribution, UI flow, evaluation evidence and bibliography integration; it prepared three focused questions and left thesis readiness pending instead of inventing answers or changing scope. With network access excluded, source consultation/search remained explicitly unperformed.
- In the second exercise, the evaluator actually ran the delivery command: exit 2 flagged a historical review/current manuscript mismatch, required independent review pending and uncovered current output. The current registered output hash already matched; the old review hash and all original input bytes were preserved.

These are packaging and bounded behavioral checks, not a full scientific peer review, rendered thesis/deck trial, human usability study or compatibility certification. The separate evaluator used sequential roles in one context. Its discovered Python was 3.9.6, below the documented 3.10+ minimum; the selected read-only command worked there, but broader 3.9 compatibility is not claimed. Automated checks used the bundled runtime. No private thesis or patient material appears in this public validation report.

## Native Office skill integration (2026-10-04)

Added the MIT `documents` skill from Magnus Hedemark's agent-skills, pinned at `9b34a87ee729f109019ac604681e5796349ea1b2`. Its tracked skill payload and license are retained unchanged, with per-file hashes. Full installation now contains 20 directories; docx/slides/publishing/defense also include this support skill. Core/latex/systematic counts are unchanged.

Original routing now selects available licensed Word/Excel/PowerPoint skills before the portable fallback. New guidance requires native editable/updateable structures when supported, separates creation/preservation from refresh/calculation and export, and records real capability limits. Word source-manager/add-in fields, spreadsheet calculation and native PowerPoint object checks supplement scientific review. User-selected static output remains supported. Existing documents are not changed by installing instructions.

Local validation: 40 project tests and 16 upstream document-validator tests passed, including installed four-format CLI execution, retained upstream license/revision, and refusing an existing host-owned documents skill. Package provenance/local-link and whitespace checks passed; the five changed original skills passed the skill-creator structural validator. These tests establish packaging and bounded validator behavior. No live Word TOC/citation update, Excel formula recalculation, PowerPoint master/object editing, real Office render or cross-client end-to-end execution is claimed for this change.

The upstream validator has important scope limits: optional unavailable rendering or unsupported inputs can accompany exit zero; Office `pages` counts generated PDF files; some PDF raster checks cover page 1. Its XML checks do not establish schema/relationship correctness or native behavior. Galileo's integration explicitly reads per-file outcomes and keeps full functional/visual QA separate; upstream code is not silently relabeled as a stronger validator.
