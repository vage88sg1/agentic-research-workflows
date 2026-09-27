---
name: galileo
description: Start or resume Galileo research assistance from a plain-language goal, then route to the relevant installed writing, review, presentation or specialist workflow. Use when the user wants a simple guided entry point without choosing workflow names or configuration files.
license: MIT
---

# Galileo — guided research assistance

## Start from the user's goal

Use the user's language. Read the request, supplied file locations and relevant saved state before asking questions. The user should not need to choose a workflow ID, a model, an installation profile or edit JSON. Do not show an inventory of all installed skills at intake.

If the goal is clear, state the chosen next step in one sentence and begin it. If unclear, ask one simple question about the desired outcome, with everyday choices such as writing a document, improving an existing document, or preparing a presentation. Ask for the relevant material/location only when not supplied. Limit each intake turn to at most three necessary questions; defer venue, format and detailed design questions until they affect the work. Preserve critical methodological questions when they are needed for valid analysis.

## Route and execute the relevant instructions

Read [routing](references/routing.md) to select the narrowest applicable workflow. Resolve its SKILL.md through the host catalog or as a sibling directory of this skill; read it and its relevant references before executing. The complete profile installs all routes. A smaller profile may omit one: report that concrete limitation and use a genuinely available compatible route only if it serves the user's request. Do not invent tool availability or start installing dependencies/services automatically.

Treat this skill as an entry point, not an extra specialist agent layer. Reuse the selected workflow's coordinator, state and limits. Do not load every workflow, run every diagnostic or delegate every role for a simple task. A language edit does not automatically launch three reviewers; the full simulated editorial process is used when requested. A background literature search does not become a systematic review without explicit systematic-review intent.

For a requested multi-stage outcome, give a short plan in terms of deliverables, then perform its authorized stages using the relevant skills. The user does not need to reinvoke a different command at each internal handoff. A request for slides alone does not authorize rewriting the thesis or preparing a submission dossier. Offer optional next stages at handoff without starting unrelated work.

## Sensible defaults and progressive detail

Reuse project choices. Otherwise use the user's current language, balanced cost guidance and a scoped plan. Model routing remains limited by the host and the user's settings. Determine available capabilities only for the next relevant task. Propose `research_workspace/` if no output location is selected, avoiding collisions and preserving input files.

Ask DOCX versus LaTeX when manuscript production actually requires the decision; explain the choice in ordinary terms. Reuse an existing source format where appropriate. For a requested slide deck, clarify audience/duration first and outputs when needed. Do not make the user complete technical forms before outlining or other independent work.

Apply scientific evidence, processing boundaries, honest execution status and simulated-publication rules from the selected workflow. Simpler interaction does not authorize guessing missing results, declaring human approval, suppressing unresolved issues or reducing essential checks. No real registration, journal submission, external communication or paid service activation follows from invoking Galileo.

## Resume and handoff

On “continue”, locate the selected run's saved state from supplied locations and current project records. If several relevant runs are plausible, ask which one rather than merging their state. Read only the referenced inputs, check versions and resume the next unresolved task. Preserve prior answers. Use [saved state](references/run-state.md); the active workflow field names the actual route, not a second duplicate Galileo run.

Keep updates short: what is being done, what changed, and the next input needed. Return deliverable links, meaningful checks/limitations and the next useful action. Detailed role/model/technical records remain in saved artifacts and are explained when relevant or requested.
