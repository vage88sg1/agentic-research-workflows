# Saved state and workflow handoff

Read this when creating a run, resuming one or handing artifacts to another workflow. Save `workflow_state.json` inside the selected run directory; separate review/presentation runs must not overwrite drafting state. Existing compatible state may be extended instead of replaced. This is an assistant-maintained convention, not a scheduler or executable schema.

Record:

- `schema_version`: 1; `run_id`: a locally unique label; `workflow`: the actual skill name.
- `phase` and `status`: active, awaiting_input, blocked or complete; blocked is a local workflow status, not a host goal status.
- `updated_at`: actual UTC time; `language`; relative paths to project configuration and evidence/issue records.
- `inputs`: path, version/hash where material, and the authorized processing boundary.
- `outputs`: path, version/hash, actual build status and actual check status. Separate source created, compilation/export completed, visual QA completed and human approval.
- `execution`: actual models, settings, tools and whether role contexts were independent, sequential or unavailable. Unknown telemetry remains null, not an estimate presented as measured usage.
- `round`, `max_rounds` and `no_progress_rounds` where a bounded revision loop applies.
- `open_issues`, `pending_user_input`, `completed_checks` and one concrete `next_action`.

For each issue preserve ID, artifact/version/location, observation/evidence, severity, owner, requested correction, status and verification evidence/by. Scientific authors do not self-close review issues. A completed workflow may still hand off explicitly accepted limitations; unresolved blocking issues preclude a verified final status.

On resume, read only relevant state and records, check that referenced inputs still exist and compare versions before reusing prior checks. A changed result invalidates dependent claims, tables, figures and slides. Preserve the previous state/version when changing scope; never replay completed external actions merely because a chat was interrupted. Record missing evidence and continue only independent work.

At handoff identify the source run, exact manuscript/results version, supporting evidence, unresolved issues and checks still required. Start the receiving workflow in its own run directory or deliberately extend an existing compatible run. Save state before stopping for missing information, budget or round limits. Do not label a build, human approval or review as completed merely to make the next workflow proceed.
