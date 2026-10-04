# Model setup during installation

A normal installation in an interactive terminal offers a short wizard. It asks whether to configure now or later, confirms your harness, and asks for the exact model IDs available to you. Then choose a model for each alias, a cost profile and optionally individual role overrides. Review the summary before saving. Choosing the same model for every alias is supported; `0` keeps your current harness model.

| Alias | Intended tasks |
|---|---|
| `economical` | Bounded language, file and mechanical checks |
| `balanced` | Writing, literature, source verification and coordination |
| `frontier` | Complex methodology and unresolved scientific disputes |

The wizard does not rank models, estimate prices or verify account access. Enter model IDs exposed by your actual harness. An optional local inventory file can supply the list; it is not live discovery. The offline installer makes no provider/network calls and changes no client settings. It does not activate an API, request credentials or implement model routing.

## Guided installation

Use the usual command with your actual skill destination:

```bash
python3 scripts/install.py --dest /path/to/project/.agents/skills --profile full
```

In a terminal it offers model setup. For Claude Code, OpenCode or Copilot choose their documented destination as in the [installation guide](INSTALLATION.md). Choosing **later** saves a deferred configuration; Galileo offers configuration when a substantive workflow needs it. A small text edit does not require model setup. EOF, cancellation or rejecting the final summary stops installation before any skill is copied.

Save an optional inventory as JSON (these IDs are placeholders, not recommendations):

```json
{
  "harness": "other",
  "models": ["example/small", "example/general", "example/strong"]
}
```

Allowed harness values: `codex`, `claude-code`, `opencode`, `copilot`, `other`. Supply the inventory in a terminal:

```bash
python3 scripts/install.py --dest /path/to/project/.agents/skills --available-models /path/to/models.json
```

The wizard confirms the inventory's harness. A mismatch stops setup rather than applying another harness's model IDs. There is no automatic scraping of account settings or execution of a client CLI.

## Unattended installation and previews

```bash
# No questions; defer model configuration.
python3 scripts/install.py --dest /path/to/project/.agents/skills --non-interactive

# Import explicit preferences without questions.
python3 scripts/install.py --dest /path/to/project/.agents/skills --non-interactive --model-settings /path/to/my-model-settings.json

# Validate package, collision checks and a preferences file without writing or prompting.
python3 scripts/install.py --dest /path/to/project/.agents/skills --dry-run --model-settings /path/to/my-model-settings.json
```

Without a terminal the installer does not prompt: it imports supplied settings or saves a deferred configuration. `--available-models` requires interactive setup for a real installation; use `--model-settings` for automation. A dry run never prompts and does not prove that selected models can run.

[Example preferences](../examples/model-settings.json) show the complete schema; replace placeholder IDs before use. `provider_model_mapping` requires all three aliases. Every selected ID, including role overrides, must appear in `available_models`. Null keeps the current model. The supplied inventory is advisory and must be checked again at runtime. Unknown fields and role IDs are rejected.

`economy` reduces repeated passes and scopes costly work; `balanced` uses the standard role policy; `quality` applies more intensive methods/conflict review. Scientific evidence checks remain required in every profile. Stronger or more expensive models are not a correctness guarantee.

## Where preferences live

The installer writes `galileo-models.json` next to the installed skill folders, for example `/path/to/project/.agents/skills/galileo-models.json`. This mutable local file is separate from each skill's payload provenance. Do not commit personal inventories or settings to the public package. The package's `.gitignore` excludes `galileo-models.json` and its replacement backups.

All original workflow entry points read the same preferences, including direct invocation. Current user instructions and explicit project choices take precedence; unspecified null fields in a project template do not erase installation selections. Existing active projects retain their recorded choices on resume. Root-session changes and independent model assignments remain subject to actual host capabilities. Requested and observed models are recorded separately.

The only unavailable-model policy is `ask`: disclose the limitation and obtain a fallback choice, reusing a prior explicitly authorized choice when applicable. No silent provider substitution or paid API activation follows from an alias.

## Reconfigure without reinstalling skills

From the package checkout, configure an existing installation:

```bash
python3 scripts/install.py --dest /path/to/project/.agents/skills --configure-models --replace-model-settings
```

For an unattended change, add `--non-interactive --model-settings /path/to/my-model-settings.json`. On a legacy installation with no preferences file, omit `--replace-model-settings`. Existing preferences are preserved unless replacement is explicitly requested; replacement keeps a backup and copies no skills.

The installed helper also works without the package checkout and infers its own skill directory:

```bash
python3 /path/to/project/.agents/skills/galileo/scripts/model_settings.py --replace

# Or import a reviewed configuration without a terminal.
python3 /path/to/project/.agents/skills/galileo/scripts/model_settings.py --settings-file /path/to/my-model-settings.json --replace
```

Run that helper from the installed skill, or supply `--dest` explicitly when invoking it from the source checkout. Its `--dry-run` previews without asking questions or writing. Configuration changes neither modify client settings nor update an active project's explicit model choices automatically.

During guided reconfiguration, Enter reuses the previous inventory, alias mappings and cost profile. Existing role overrides are retained when compatible with the chosen inventory; the summary identifies removals if their models are absent. In the advanced role menu, prefix a role ID with `-` to remove its override. Choosing **later** keeps the existing configuration.
