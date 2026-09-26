# Project CLI and record formats

Run with Python 3.10+ from this skill directory; installed copies include the script and templates. Resolve file paths from the working directory explicitly. Output is JSON; redirect to a new report path if persistence is desired. The tools neither contact services nor execute code from a manifest.

```bash
python3 scripts/research_tools.py preflight
python3 scripts/research_tools.py evidence --map /path/to/project/research-map.json
python3 scripts/research_tools.py impact --map /path/to/project/research-map.json --root /path/to/project --changed source-1
python3 scripts/research_tools.py bundle --manifest /path/to/project/reproducibility-manifest.json --root /path/to/project --dest /path/to/new-bundle
```

`--changed` can repeat and is optional; impact always checks local file hashes. A project root bounds file access; absolute/traversal/symlink paths are rejected. Bundles require a new output directory with an existing parent and refuse overwrites. No recursive inclusion of directories is supported. Classification as public/synthetic must reflect actual authorization, not the desire to include a file. Inspect content for confidential data and credentials before packaging; filename exclusions are not a secret scanner. A bundle must not contain confidential commands, dependency URLs or environment values either.

Exit codes: 0 = command completed; 1 = input, schema or I/O error; 2 = a structurally valid evidence map has issues to assess. Zero never means scientific validity. The impact report does not change map hashes or state and can complete successfully while reporting affected outputs. Preflight records PATH discovery only and reports host capabilities as not verified.

## Research map, schema version 1

Top level: `schema_version`, `sources`, `claims`, `artifacts`. All three collections are lists; IDs are unique across collections. Every optional `depends_on` list references existing IDs; cycles and dangling references are rejected. Any node with a local `path` needs its baseline `sha256`. Paths use project-relative POSIX notation. For remote changes use explicit changed IDs; no remote content is fetched by the script.

Source fields: `id`, `access` (metadata, abstract, full_text or executed_result), optional `identifier`, `path`, `sha256`, `depends_on` and provenance notes. An executed_result is a recorded result, not a guarantee the script reran its analysis. Record associated code/input IDs as dependencies.

Claim fields: `id`, `text`, `evidence` and optional `depends_on`. Each evidence entry contains `source_id`, `relation` (supports, contradicts, context), `verification` (pending, ai_checked, human_verified), `locator`, `verified_by`, `checked_at` and optional assessment rationale. A checked entry needs a nonempty locator/verifier/date; the script cannot authenticate them or establish that the source entails the claim. Metadata and abstract-only access generate review items. Contradictory evidence is preserved and flagged rather than silently discarded.

Artifact fields: `id`, `path`, `sha256`, `depends_on` and optional version/type. Include separate nodes for affected manuscript sections/figures/slides when useful. Dependencies express provenance: a figure depends on results, not the other way around. Unrecorded dependencies cannot be detected.

## Reproducibility manifest, schema version 1

Top level: `schema_version`, nonempty `files`, nonempty `environment`, nonempty `reproduction_commands`, `excluded_inputs` (possibly empty), and `license_or_terms`. Each file has `path`, `sha256` and `sharing` (public or synthetic). Sensitive/restricted data stay out of the payload; `excluded_inputs` should explain their access conditions and resulting limits. Document dependencies using supplied lockfiles and actual runtime versions where available; do not call an approximate environment a lockfile.

The resulting directory contains `payload/` with selected relative paths, `bundle-manifest.json`, and `REPRODUCE.md`. Commands are recorded for execution from `payload/`, never automatically run. The generated execution status is NOT_EXECUTED_BY_PACKAGER regardless of claims in the input manifest. Hash validation catches changed bytes before/during copying. It does not provide an authenticity signature, a clinical-data anonymization assessment or independent reproduction.
