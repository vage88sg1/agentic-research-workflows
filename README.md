# Galileo: Agentic Research Workflows

**Describe what you want to achieve. Galileo guides the research work.**

Write a thesis or paper, improve a manuscript, prepare slides, or rehearse your defense. Start with one entry point; Galileo selects the relevant workflow and asks for missing information as it becomes necessary. Work in your preferred language and AI coding assistant (harness). Galileo ships portable `SKILL.md` instructions and local tools; your harness supplies the model, agents and execution environment.

## Start here

After installation, ask your assistant to use the **Galileo** skill and describe your goal. Include the location of any materials you already have:

```text
Use the Galileo skill to help me write my thesis.
I have a study description and results in study_inputs/.
Write in English and guide me through the next step.
```

No workflow names, model selection or JSON configuration are needed for normal use. Explicit invocation depends on your harness:

| Harness | Project skill directory | How to start |
|---|---|---|
| Claude Code | `.claude/skills/` | `/galileo` followed by your request |
| Codex | `.agents/skills/` | `$galileo` followed by your request, or select Galileo in the supported skill menu |
| OpenCode | `.opencode/skills/` | Ask the agent to load the Galileo skill and follow your request |
| GitHub Copilot, in a skill-capable mode | `.github/skills/` | Ask the agent to use the Galileo skill and follow your request |
| Other skill-compatible harnesses | The directory documented by the harness | Use its skill menu, invocation syntax or an explicit natural-language request |

These are documented skill discovery paths, not a claim of end-to-end testing on every harness. See the [installation and compatibility guide](docs/INSTALLATION.md) for sources and execution limits. The installer copies skills; it does not create a universal slash command.

## What would you like to do?

| Start with this | Galileo helps you do |
|---|---|
| “Help me write my thesis.” | Clarify the question, organize evidence/results and develop a draft |
| “Improve this manuscript.” | Make scoped improvements; run simulated peer review when you request it |
| “Create a 12-minute talk from this paper.” | Plan and produce slides, notes and timing with scientific and visual checks |
| “Turn my thesis into an article.” | Select a focused scope and preserve a map back to the thesis |
| “Help me rehearse my defense.” | Ask questions, wait for your answers and provide feedback |
| “Prepare the files for this journal.” | Assemble a local submission dossier and identify missing declarations |
| “Help me plan a systematic review.” | Develop the protocol and documented search, screening and synthesis process |

You can request a sequence in one message, such as “Turn this thesis into an article, then create presentation slides.” Galileo handles the requested handoffs without requiring a new command at each step.

## What to expect

1. **A short conversation:** Galileo uses the material already supplied and asks only the next necessary questions.
2. **A clear next step:** it chooses the relevant specialist workflow and uses available tools.
3. **A reviewable result:** you receive files, meaningful checks and any unresolved issues.

For rendered presentations, Galileo supports research-group and university logos, colors, fonts and templates, or proposes suitable visual directions, defines a shared style and checks representative slides before completing the deck.

Small requests stay small: a language edit returns the corrected text, and a Markdown slide outline does not require export setup or new project records. Longer research projects keep resumable state.

```mermaid
flowchart LR
  A[Describe your goal] --> B[Galileo chooses the relevant workflow]
  B --> C[Work, check and correct]
  C --> D[Deliver files and save progress]
  D -->|Continue later| B
```

Format choices such as Word or LaTeX are discussed when they matter. Technical evidence records, model settings and dependency checks stay in the project records and are explained when useful. The default cost guidance is balanced; actual model use depends on your host.

To resume in the same project, invoke Galileo using your harness and say:

```text
Continue from the saved state in research_workspace/. Reuse my previous answers.
```

If more than one run could match, Galileo asks which one to continue.

## Install once

Requires Python 3.10+ for the offline installer. Clone the package:

```bash
git clone https://github.com/vage88sg1/agentic-research-workflows.git
cd agentic-research-workflows
```

Then install into your research project's skill directory. Choose **one** command matching your harness and replace `/path/to/research-project` with the actual path:

```bash
# Claude Code
python3 scripts/install.py --dest "/path/to/research-project/.claude/skills"

# Codex
python3 scripts/install.py --dest "/path/to/research-project/.agents/skills"

# OpenCode
python3 scripts/install.py --dest "/path/to/research-project/.opencode/skills"

# GitHub Copilot
python3 scripts/install.py --dest "/path/to/research-project/.github/skills"
```

Then open that research project in your assistant and refresh its skills or start a new session. The default complete installation includes Galileo and its specialist/support skills. Add `--dry-run` to preview the installation. Existing skill names are never overwritten; see the [installation guide](docs/INSTALLATION.md) for updates, other clients and smaller profiles.

The installer copies instructions and local tools. It does not install document renderers, activate MCP services or purchase API access. The assistant reports missing capabilities when they affect your task.

## Agentic execution and portability

The workflow instructions describe coordination, specialist roles and review loops. For separate agents, include a request such as:

```text
Use Galileo in agentic mode. Delegate the relevant roles to separate agents
where supported, and coordinate their reviews and corrections.
```

Independent agents require harness support and permission to delegate. Otherwise, the assistant follows the roles sequentially and discloses that limitation. Installing skills does not install native agent definitions or guarantee parallel execution.

Model examples are optional guidance, not a dependency on one provider. Use models available in your harness; actual model routing and costs depend on its capabilities. When literature work would benefit from an unavailable connection, Galileo proposes the relevant MCP integration and offers to help set it up or continue with available sources. It can also look for other task-relevant MCPs beyond the bundled catalog, using current upstream documentation and distinguishing candidates from bundled integrations. It reuses your choice on resume. MCP connections and document/export tools still require host-specific setup; a recommendation does not activate a service. Codex UI metadata can be ignored by other clients.

Package checks and synthetic workflow exercises are documented in the [release review](docs/RELEASE_REVIEW.md) and [usability report](docs/USABILITY_TESTS.md). Complete runs on Claude Code, OpenCode and GitHub Copilot have not yet been verified.

## Explore when needed

- [All nine specialist workflows, examples and diagrams](docs/WORKFLOW_GUIDE.md)
- [Word, LaTeX, PowerPoint and PDF](docs/FORMATS_AND_SLIDES.md)
- [Optional scientific literature connections](docs/LITERATURE_INTEGRATIONS.md)
- [Evidence tracking, change impact and reproducibility tools](docs/PROJECT_TOOLS.md)
- [Guida rapida in italiano](docs/README.it.md)

Galileo is an instruction package that works through your AI host. It keeps evidence and execution limits explicit; simulated peer review is labeled as such. It does not submit to journals or create real acceptance. Establish the authorized processing boundary before supplying confidential research material.

[Validation and remaining limitations](docs/RELEASE_REVIEW.md) · [Contributing](CONTRIBUTING.md) · [Security](SECURITY.md) · [Third-party notices](THIRD_PARTY_NOTICES.md) · [MIT license](LICENSE)
