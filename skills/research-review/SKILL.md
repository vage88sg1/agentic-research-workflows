---
name: research-review
description: Review or resume a research manuscript or thesis through a simulated editorial process with independent anonymous reviewers, reasoned decisions, point-by-point author responses, corrections and bounded rereview. For simulation and internal quality improvement, not actual journal acceptance or submission.
license: MIT
---

# Research review

Read [agent contracts](references/agent-contracts.md) and [skill integration](references/skill-integration.md). Match language, discipline, design, document and venue. An author's internal simulation is not an assigned journal review; do not invent reviewer identities, qualifications, publisher permissions or real editorial outcomes.

## Intake and freeze

Locate the manuscript and available supplements specified by the user. If missing, ask for their location. Resolve scope, target venue if any, authorized processing and saved state. For third-party confidential material resolve ownership/permission and controlling policy before substantive review. Authorization to review is not permission to disclose to another service.

Create a versioned run under the selected output directory with author-facing, editor-only and individual reviewer areas. Hash/freeze inputs; record what is actually available. Directory separation does not impose access isolation: report what the host really enforces.

Verify the target journal's current scope, article type, anonymity, formatting and tool policies from official sources. If unspecified, use an explicitly generic simulated profile. Institutional thesis assessment and journal review differ; neither is replaced by this simulation.

## Technical check and editorial assessment

The editorial secretary checks files, declarations, format and anonymity against the chosen profile. Separate title-page and blinded materials when required while retaining scientific details needed for assessment. The simulated editor records return for correction, clarification, desk rejection or referral to review with reasons.

## Independent review

Default to three reviewers with complementary expertise, adapting specialties to the actual discipline: domain/clinical relevance; methods/statistics; measurement or another technical specialty. Use fresh contexts with the same frozen manuscript and permitted supplements. Do not include author drafting history, identities under an anonymous process, other reports at first pass or a desired verdict. Reviewer roles never modify the master.

Use peer-review and scientific-critical-thinking, plus relevant statistical, citation or measurement guidance. Distinguish missing reporting from demonstrated error and reporting completeness from study validity. A local checklist cannot establish merit. Sequential reviewers in the same context are not independent; state this fallback explicitly.

Each report includes neutral summary, strengths, major/minor issues, unavailable material and competence limits. Each comment carries ID, location/version, observation, evidence/criterion, consequence, proportionate requested action and verification method. Request additional work only when necessary for a central claim; consider clarification, sensitivity analysis, narrower conclusions or limitations instead.

Use [evidence sufficiency and reader-focused review](../galileo/references/quality-gates.md) to distinguish absent, uninspected and deliberately excluded evidence and to assess fitness for the actual document type. Keep scientific/content issues separate from editorial/visual issues; a reconstructed analysis is not automatically equivalent to a thesis about completed work. Do not demand unavailable results from a proposal or treat a proposed test as a performed result.

Apply [objective and chapter completeness](../galileo/references/content-completeness.md): reviewers assess substantive answers, attributed contributions, missing explanations and appropriate bibliography coverage, not only the correctness of existing sentences. The domain reviewer includes a fresh-reader assessment; the evidence specialist checks source type, exact support and citation/bibliography integration. Existing roles suffice.

Assess disciplinary terminology separately from grammar. Preserve exact names and customary English technical vocabulary in other-language manuscripts when that matches field/user convention; an accepted local equivalent is not inherently wrong. Distinguish stylistic awkwardness from a translation that changes meaning, and route the latter to the relevant domain/technical reviewer. Do not add another mandatory peer reviewer solely for copyediting.

Check whether material literature gaps were actually researched and central references support their specific claims. Use targeted authorized primary-source searches for external background; request missing project facts from the author. Invented facts/citations, unsupported central conclusions and unresolved methods/results contradictions are blocking findings. A longer reference list or a successful metadata check does not resolve missing claim support. Keep readiness pending when essential search/full-text verification is unavailable.

Separate comments to authors from confidential notes to the editor. Ordinary scientific criticism belongs in the author report. Reserved notes may address conflicts, competence, process or observable integrity concerns; avoid speculative accusations. Recommendations are advisory and simulated; the editor determines the simulated outcome.

When this step needs external literature, identifier checks or an authorized reference library, follow [literature connection recommendations](../galileo/references/literature-connections.md). Offer relevant MCP connections if equivalent tools are unavailable; reuse the coordinator's recorded choice. Do not propose setup for a task fully supported by supplied sources.

## Decision and correction loop

The editor synthesizes reasons rather than majority voting. Record simulated accept/minor revision/major revision/reject, required versus optional changes, disagreements and unresolved validity limits. Maintain issues with IDs, severity, ownership, evidence and verification status.

The author team produces a clean revision, change comparison and point-by-point response. For each ID provide change/location or evidence-based disagreement. Change underlying records/results before prose and rerun affected outputs/audits. Do not alter hypotheses, exclusions or scoring to manufacture favorable findings.

Original reviewers or a distinct verifier confirm corrections; authors do not self-close scientific issues. Major revision returns to relevant reviewers; minor may be checked by the editor according to the profile. New comments require evidence, not shifting preferences. Escalate substantive disagreements to the accountable user.

Default cap: three complete rounds; stop after two rounds without substantive progress, blocking evidence gaps, rejection or acceptance. User configuration may change these operational limits. Hitting the cap leaves revision required or rejection; never auto-accept. Save a resumable state and continue only independent work when information is missing.

Apply [revision-specific closure](../galileo/references/quality-gates.md#3-close-checks-against-the-delivered-revision): reviewer checks identify the inspected artifact version/hash, scope and context. Changes reopen affected checks. If a distinct verifier is unavailable, preserve the required review as pending and disclose any coordinator fallback; author self-review cannot close scientific reviewer issues or produce simulated acceptance.

## Production and handoff

Simulated acceptance requires resolution of validity-blocking/major issues and sufficient evidenced consistency; distinguish AI checks from human verification still pending. Actual submission readiness requires responsible human approval and genuine declarations.

For selected DOCX or LaTeX production use research-typesetting when installed, with real build/render verification and conditional LaTeX guidance. Optional copyediting/proofs occur after simulated acceptance; substantive changes return to the editor. All dossier, decisions and production artifacts carry SIMULATION — NOT SUBMITTED — NOT PUBLISHED. Do not invent DOI, indexing, journal logo, signatures or real acceptance. Never upload to a journal or contact others through this workflow.

Deliver reviewer reports, decision rationale, issue ledger, response, clean revision/change comparison, actual check log, limits and run state. Rejection remains a valid final simulation outcome.

## Saved state and continuation

When starting, resuming or handing off a run, follow [saved state and handoff](references/run-state.md). Save the current phase, artifact versions, actual checks, open issues and next action in the run directory.

## Optional project support

Use research-project when installed for a requested capability check, evidence-map audit, dependency-impact report or reproducibility package. All installation profiles include it. Read only the relevant operation's guidance; support scripts check records and bytes, not scientific meaning. Record affected artifacts in saved state and reverify them after substantive changes.
