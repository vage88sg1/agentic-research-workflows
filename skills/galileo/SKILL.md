---
name: galileo
description: Start or resume Galileo research assistance from a plain-language goal, then route to the relevant installed writing, review, presentation or specialist workflow. Use when the user wants a simple guided entry point without choosing workflow names or configuration files.
license: MIT
---

# Galileo — guided research assistance

## Start from the user's goal

Use the user's language. Read the request, supplied file locations and relevant saved state before asking questions. The user should not need to choose a workflow ID, a model, an installation profile or edit JSON. Do not show an inventory of all installed skills at intake.

If the goal is clear, state the chosen next step in one sentence and begin it. If unclear, ask one simple question about the desired outcome, with everyday choices such as writing a document, improving an existing document, or preparing a presentation. Ask for the relevant material/location only when not supplied. Limit each intake turn to at most three necessary questions; defer venue, format and detailed design questions until they affect the work. Preserve critical methodological questions when they are needed for valid analysis.

## Match the amount of process to the request

For a one-off language edit, a short outline or content-only slide notes, deliver the requested artifact and a brief explanation directly when the supplied information is sufficient. Do not create a new project configuration, issue ledger, comparison file or saved-state file merely to complete a small task. Preserve the original and check the affected scientific meaning. If the user requests a comparison/resume record, or the work belongs to an existing tracked project, provide/update the relevant records without duplicating them.

For an actual new research project, a first useful planning note plus compact resumable state is enough to start. Create additional evidence/analysis/configuration records when real work populates them; avoid empty scaffolding. Important missing facts can still block dependent claims or analyses. Do not ask about formats, visual themes or tools that are irrelevant to the requested deliverable.

## Route and execute the relevant instructions

Read [routing](references/routing.md) to select the narrowest applicable workflow. Resolve its SKILL.md through the host catalog or as a sibling directory of this skill; read it and its relevant references before executing. The complete profile installs all routes. A smaller profile may omit one: report that concrete limitation and use a genuinely available compatible route only if it serves the user's request. Do not invent tool availability or start installing dependencies/services automatically.

Treat this skill as an entry point, not an extra specialist agent layer. Reuse the selected workflow's coordinator, state and limits. Do not load every workflow, run every diagnostic or delegate every role for a simple task. A language edit does not automatically launch three reviewers; the full simulated editorial process is used when requested. A background literature search does not become a systematic review without explicit systematic-review intent.

For a requested multi-stage outcome, give a short plan in terms of deliverables, then perform its authorized stages using the relevant skills. The user does not need to reinvoke a different command at each internal handoff. A request for slides alone does not authorize rewriting the thesis or preparing a submission dossier. Offer optional next stages at handoff without starting unrelated work.

## Sensible defaults and progressive detail

Reuse project choices. Otherwise use the user's current language, balanced cost guidance and a scoped plan. Model routing remains limited by the host and the user's settings. Determine available capabilities only for the next relevant task. Propose `research_workspace/` if no output location is selected, avoiding collisions and preserving input files.

Ask DOCX versus LaTeX when manuscript production actually requires the decision; explain the choice in ordinary terms. Reuse an existing source format where appropriate. For a requested slide deck, clarify audience/duration first and outputs when needed. Do not make the user complete technical forms before outlining or other independent work.

Apply scientific evidence, processing boundaries, honest execution status and simulated-publication rules from the selected workflow. Simpler interaction does not authorize guessing missing results, declaring human approval, suppressing unresolved issues or reducing essential checks. No real registration, journal submission, external communication or paid service activation follows from invoking Galileo.

## Offer useful MCP connections

When the next step needs new literature, bibliographic verification, reuse of a reference library or another concrete research-tool connection, read [MCP connection recommendations](references/literature-connections.md). Proactively offer the smallest useful set of MCP integrations if equivalent tools are not already available. Explain the benefit and give a simple choice to set them up or continue with available sources; keep independent work moving. Respect earlier choices and avoid repeating declined proposals. A scoped language edit, supplied-source slide outline or formatting task does not need an MCP setup pitch. The bundled catalog is not exclusive: if it does not meet the task or the user asks for alternatives, use available catalog/web discovery to assess other relevant MCPs from current primary sources. Present them as candidates with source links and limits, not as bundled/tested integrations. Follow the reference for selection, actual capability status and host-specific setup boundaries.

## Resume and handoff

On “continue”, locate the selected run's saved state from supplied locations and current project records. If several relevant runs are plausible, ask which one rather than merging their state. Read only the referenced inputs, check versions and resume the next unresolved task. Preserve prior answers. For resumable project work, use [saved state](references/run-state.md); the active workflow field names the actual route, not a second duplicate Galileo run.

Keep updates short: what is being done, what changed, and the next input needed. Return deliverable links, meaningful checks/limitations and the next useful action. Mention missing capabilities or checks only when they affect the requested result; do not report unrequested exports as missing deliverables. Detailed role/model/technical records, when needed, remain in project artifacts and are explained when relevant or requested.
