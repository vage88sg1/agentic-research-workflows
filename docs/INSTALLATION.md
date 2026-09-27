# Installation and host compatibility

Run `python3 scripts/install.py --dest PATH --profile full --dry-run` before installing. The destination is a host-supported directory containing skill folders. Existing names block the entire installation; choose a fresh directory or manually reconcile versions. No silent updates or overwrite option.

The installer verifies vendor hashes, stages the full set and rolls back directories it created if copying fails. It is intended for a single installer process; do not run competing installers against the same destination. It does not download dependencies or execute third-party scripts. Libraries/services needed for individual tasks are documented in their SKILL.md and are optional until needed.

## Codex

For normal use select **Galileo** in the supported skill menu and describe your goal. `$galileo` is the explicit alternative. It routes to the installed specialist skills and reuses saved state. Direct specialist entry points remain available for advanced use.

For project scope choose `/path/to/project/.agents/skills`. For a different scope consult current host documentation rather than assuming paths are interchangeable. Refresh discovery/start a new session. Desktop enabled skills can appear in the slash menu; CLI `/skills` selects a skill. `$research-drafting` and `$research-review` are explicit invocation examples. UI display names are Research drafting and Research review. Arbitrary slash aliases are not registered by this installer.

## Claude Code, OpenCode and GitHub Copilot

Choose the project directory documented by your harness:

| Harness | Example destination | Invocation |
|---|---|---|
| Claude Code | `/path/to/project/.claude/skills` | `/galileo` followed by the request |
| OpenCode | `/path/to/project/.opencode/skills` | Ask the agent to load and use the Galileo skill |
| GitHub Copilot, in a skill-capable mode | `/path/to/project/.github/skills` | Ask the agent to use the Galileo skill |

For example, from the package checkout:

```bash
python3 scripts/install.py --dest "/path/to/project/.claude/skills" --profile full --dry-run
```

Review the plan, then run the same command without `--dry-run`. Open the target research project in the client and refresh skill discovery or start a new session.

Sources: [Claude Code skills and commands](https://code.claude.com/docs/en/skills), [OpenCode skill discovery](https://opencode.ai/docs/skills/), [GitHub Copilot agent skills](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills). These document format and discovery support; complete Galileo runs on these harnesses have not yet been verified.

## Other clients

If your client supports the SKILL.md format, point `--dest` to its supported skill location. Extra Codex UI metadata may be ignored. Use `--profile core|docx|latex|slides|publishing|defense|systematic|full` to choose installed capabilities; full includes nineteen directories. All profiles preserve non-overwrite behavior. The workflows themselves are portable Markdown instructions, but model settings, independent contexts, tool identifiers and menus are not universal. No claim is made of end-to-end testing in other clients. Installing skills does not add native harness agent definitions. Separate agents require explicit delegation support and host permission; otherwise the roles are performed sequentially with that limitation disclosed. Model recommendations must be mapped to the models available in the host, and MCP settings must be configured for that host separately.

If skills are unsupported, provide the entry point, its references and relevant vendor guidance as instructions. The workflow must report unavailable parallelism, computation, browsing and model routing instead of simulating successful tool execution.

## Installed versus operational

Copied files are not proof of client discovery or operational tools. Record these separately: installed, discovered, dependencies available, tools executed, output verified. Scientific-writing and peer-review audit CLIs require Python 3.11+ according to the bundled snapshot; optional statistical/plotting/search tools have additional requirements. The installer itself needs Python 3.10+ standard library.

There is no model/API key requirement for installation. Authorize any cloud processing independently of installation. Do not expose credentials or confidential materials in commits, logs, reports or public issues.

Sources: [Codex desktop slash commands](https://learn.chatgpt.com/docs/reference/slash-commands), [Codex CLI slash commands](https://learn.chatgpt.com/docs/cli/slash-commands). Consult your host's current documentation for changes.

For users of the first published version: this release adds files and changes the original entry points. Install into a fresh supported skill location or explicitly reconcile existing versions after backup. Do not overwrite modified skills to bypass the collision check. Format selection activates only the relevant installed guidance.

## Optional literature MCP module

MCP examples are kept outside skill installation. Configure selected servers separately using the [literature integration guide](LITERATURE_INTEGRATIONS.md). The installer does not copy or merge client settings, install server runtimes or enable services.

The installer rejects vendor files absent from its provenance inventory, including generated caches; use a clean source checkout. Each installed skill records SHA-256 hashes of its payload and retained license in `bundle-provenance.json` (the manifest excludes itself). This detects later file changes; it is not a signature or authenticity guarantee.

All profiles include galileo and research-project and its portable standard-library scripts. The publishing profile adds thesis-to-article and submission preparation; defense adds oral rehearsal; systematic adds the dedicated evidence-synthesis workflow. New profiles still require a fresh destination or deliberate reconciliation with existing installations.
