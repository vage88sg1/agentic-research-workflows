# Installation and host compatibility

Run `python3 scripts/install.py --dest PATH --dry-run` before installing. The destination is a host-supported directory containing skill folders. Existing names block the entire installation; choose a fresh directory or manually reconcile versions. No silent updates or overwrite option.

The installer verifies vendor hashes, stages the full set and rolls back directories it created if copying fails. It is intended for a single installer process; do not run competing installers against the same destination. It does not download dependencies or execute third-party scripts. Libraries/services needed for individual tasks are documented in their SKILL.md and are optional until needed.

## Codex

For project scope choose `/path/to/project/.agents/skills`. For a different scope consult current host documentation rather than assuming paths are interchangeable. Refresh discovery/start a new session. Desktop enabled skills can appear in the slash menu; CLI `/skills` selects a skill. `$research-drafting` and `$research-review` are explicit invocation examples. UI display names are Research drafting and Research review. Arbitrary slash aliases are not registered by this installer.

## Other clients

If your client supports the SKILL.md format, point `--dest` to its supported skill location. Extra Codex UI metadata may be ignored. The workflows themselves are portable Markdown instructions, but model settings, independent contexts, tool identifiers and menus are not universal. No claim is made of end-to-end testing in other clients.

If skills are unsupported, provide the entry point, its references and relevant vendor guidance as instructions. The workflow must report unavailable parallelism, computation, browsing and model routing instead of simulating successful tool execution.

## Installed versus operational

Copied files are not proof of client discovery or operational tools. Record these separately: installed, discovered, dependencies available, tools executed, output verified. Scientific-writing and peer-review audit CLIs require Python 3.11+ according to the bundled snapshot; optional statistical/plotting/search tools have additional requirements. The installer itself needs Python 3.10+ standard library.

There is no model/API key requirement for installation. Authorize any cloud processing independently of installation. Do not expose credentials or confidential materials in commits, logs, reports or public issues.

Sources: [Codex desktop slash commands](https://learn.chatgpt.com/docs/reference/slash-commands), [Codex CLI slash commands](https://learn.chatgpt.com/docs/cli/slash-commands). Consult your host's current documentation for changes.
