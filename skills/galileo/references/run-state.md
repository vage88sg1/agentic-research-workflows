# Saved state and workflow handoff

Read this when creating a run, resuming one or handing artifacts to another workflow. Save `workflow_state.json` inside the selected run directory; separate review/presentation runs must not overwrite drafting state. Existing compatible state may be extended instead of replaced. This is an assistant-maintained convention, not a scheduler or executable schema.

Record:

- `schema_version`: 1; `run_id`: a locally unique label; `workflow`: the actual skill name.
- `phase` and `status`: active, awaiting_input, blocked or complete; blocked is a local workflow status, not a host goal status.
- `updated_at`: actual UTC time; `language`; relative paths to project configuration and evidence/issue records.
- `inputs`: path, version/hash where material, and the authorized processing boundary.
- `outputs`: path, version/hash, actual build status and actual check status. Separate source created, compilation/export completed, visual QA completed and human approval.
- `execution`: actual models, settings, tools and whether role contexts were independent, sequential or unavailable. Unknown telemetry remains null, not an estimate presented as measured usage.
- Optional `literature_connections`: offered/selected/declined/deferred integrations, bundled versus external-candidate status, upstream URL/revision where relevant, reason, authorized scope and actual connection/check status; preserve choices across handoffs.
- `round`, `max_rounds` and `no_progress_rounds` where a bounded revision loop applies.
- `open_issues`, `pending_user_input`, `completed_checks` and one concrete `next_action`.
- For substantive drafting, a compact evidence-sufficiency summary in existing notes/state: intended product, essential available facts, gaps classified as missing/ambiguous/uninspected/present-but-excluded, affected claims and next action. Reuse any terminology list when relevant; bounded edits need no new records.
- Each material `completed_checks` entry identifies check kind/status, artifact path and version/hash, source/export linkage where relevant, reviewer/tool and actual independent/sequential/self-review context, inspection scope/method and evidence locator. Keep evidence/content, terminology/editorial and visual checks distinguishable; unknown or pending checks are not passes.

For each issue preserve ID, artifact/version/location, observation/evidence, severity, owner, requested correction, status and verification evidence/by. Scientific authors do not self-close review issues. A completed workflow may still hand off explicitly accepted limitations; unresolved blocking issues preclude a verified final status.

On resume, read only relevant state and records, check that referenced inputs still exist and compare versions before reusing prior checks. A changed result invalidates dependent claims, tables, figures and slides. Content, layout or renderer changes also invalidate affected review/export checks. Reuse checks only for documented unchanged material; recheck downstream pagination, references, notes and exports. If a distinct final reviewer is unavailable, record any coordinator fallback and leave required independent review pending rather than applying an earlier pass to the changed revision. Preserve the previous state/version when changing scope; never replay completed external actions merely because a chat was interrupted. Record missing evidence and continue only independent work.

At handoff identify the source run, exact manuscript/results version, supporting evidence, unresolved issues and checks still required. Start the receiving workflow in its own run directory or deliberately extend an existing compatible run. Save state before stopping for missing information, budget or round limits. Do not label a build, human approval or review as completed merely to make the next workflow proceed.

For a staged manuscript/thesis, reuse existing notes/state to identify the agreed outline, checkpoint/autonomous preference, current section, section checks and pending factual/literature questions. A section pass does not replace whole-document or final-revision review.
