# Project CLI and record formats

Run with Python 3.10+ from this skill directory; installed copies include the script and templates. Resolve file paths from the working directory explicitly. Output is JSON; redirect to a new report path if persistence is desired. The tools neither contact services nor execute code from a manifest.

```bash
python3 scripts/research_tools.py preflight
python3 scripts/research_tools.py delivery --state /path/to/project/delivery-state.json --root /path/to/project
python3 scripts/research_tools.py evidence --map /path/to/project/research-map.json
python3 scripts/research_tools.py impact --map /path/to/project/research-map.json --root /path/to/project --changed source-1
python3 scripts/research_tools.py bundle --manifest /path/to/project/reproducibility-manifest.json --root /path/to/project --dest /path/to/new-bundle
```

`--changed` can repeat and is optional; impact always checks local file hashes. A project root bounds file access; absolute/traversal/symlink paths are rejected. Bundles require a new output directory with an existing parent and refuse overwrites. No recursive inclusion of directories is supported. Classification as public/synthetic must reflect actual authorization, not the desire to include a file. Inspect content for confidential data and credentials before packaging; filename exclusions are not a secret scanner. A bundle must not contain confidential commands, dependency URLs or environment values either.

Exit codes: 0 = command completed; 1 = input, schema or I/O error; 2 = a structurally valid evidence map or delivery record has issues to assess. Zero never means scientific validity. The impact report does not change map hashes or state and can complete successfully while reporting affected outputs. Preflight records PATH discovery only and reports host capabilities as not verified.

## Research map, schema version 1

Top level: `schema_version`, `sources`, `claims`, `artifacts`. All three collections are lists; IDs are unique across collections. Every optional `depends_on` list references existing IDs; cycles and dangling references are rejected. Any node with a local `path` needs its baseline `sha256`. Paths use project-relative POSIX notation. For remote changes use explicit changed IDs; no remote content is fetched by the script.

Source fields: `id`, `access` (metadata, abstract, full_text or executed_result), optional `identifier`, `path`, `sha256`, `depends_on` and provenance notes. An executed_result is a recorded result, not a guarantee the script reran its analysis. Record associated code/input IDs as dependencies.

Claim fields: `id`, `text`, `evidence` and optional `depends_on`. Each evidence entry contains `source_id`, `relation` (supports, contradicts, context), `verification` (pending, ai_checked, human_verified), `locator`, `verified_by`, `checked_at` and optional assessment rationale. A checked entry needs a nonempty locator/verifier/date; the script cannot authenticate them or establish that the source entails the claim. Metadata and abstract-only access generate review items. Contradictory evidence is preserved and flagged rather than silently discarded.

Artifact fields: `id`, `path`, `sha256`, `depends_on` and optional version/type. Include separate nodes for affected manuscript sections/figures/slides when useful. Dependencies express provenance: a figure depends on results, not the other way around. Unrecorded dependencies cannot be detected.

## Reproducibility manifest, schema version 1

Top level: `schema_version`, nonempty `files`, nonempty `environment`, nonempty `reproduction_commands`, `excluded_inputs` (possibly empty), and `license_or_terms`. Each file has `path`, `sha256` and `sharing` (public or synthetic). Sensitive/restricted data stay out of the payload; `excluded_inputs` should explain their access conditions and resulting limits. Document dependencies using supplied lockfiles and actual runtime versions where available; do not call an approximate environment a lockfile.

The resulting directory contains `payload/` with selected relative paths, `bundle-manifest.json`, and `REPRODUCE.md`. Commands are recorded for execution from `payload/`, never automatically run. The generated execution status is NOT_EXECUTED_BY_PACKAGER regardless of claims in the input manifest. Hash validation catches changed bytes before/during copying. It does not provide an authenticity signature, a clinical-data anonymization assessment or independent reproduction.

## Delivery record check

```bash
python3 scripts/research_tools.py delivery --state /path/to/project/workflow_state.json --root /path/to/project
```

Use for a tracked final-delivery snapshot maintained by the assistant. It is not a new user intake form or required for a bounded edit. The assistant may normalize the existing state into a separate versioned snapshot when its earlier check format differs; preserve the original and reference the current snapshot. Do not populate fictitious completed checks just to fit the format.

The schema uses `schema_version: 1`, nonempty `outputs` (each `path`, `sha256`), `completed_checks`, optional `required_checks` (check IDs), and `readiness`. Operational `status: complete` is informational; it cannot satisfy a missing check. Paths are project-relative and bounded by `--root`; no files are modified.

`readiness` contains `content`, `bibliography`, `review` and `production`. Each is an object with `status` (checked, pending, blocked, not_required), a nonempty `rationale`, and `check_ids` for checked assessments. Use not_required only for an actually inapplicable operation and explain why. For a required independent review, set `readiness.review.requires_independent: true`; self/sequential/tool contexts do not close it. Human approval stays separately recorded and is never inferred or authenticated by this command.

Each active `completed_checks` entry has a unique `id`, `status: performed`, `result: pass`, nonempty `reviewer`, `scope`, `evidence` locator and `context` (independent, sequential, self, tool). `artifacts` is a nonempty list of the inspected output `path`/`sha256` pairs. Performing a check is not passing it. Pending/failed/needed checks remain open. Historical/superseded entries can remain in the record but cannot fulfill a required or referenced check. Every current selected output needs coverage by a current passed check. Declare whole-page versus overview/render or section scope honestly; the script cannot judge whether that scope was scientifically sufficient.

The command compares current files with registered output and active-check hashes. It reports stale/missing/unsafe files, changed-version passes, unrecorded/pending readiness, missing required checks and uncovered outputs. Exit 2 means recorded issues need attention; exit 1 means malformed input/I/O failure. Exit 0 and `record_consistent: true` establish record consistency only. They do not assess objective fulfillment, bibliography coverage, authenticity, reviewer identity, actual independent contexts, visual quality or scientific merit. Claimed semantic judgments still require actual source/reader review.

Example check, only after the described work really occurred:

```json
{
  "id": "content-review-v2",
  "status": "performed",
  "result": "pass",
  "reviewer": "actual reviewer or tool identifier",
  "context": "independent",
  "scope": "specified sections/pages and evidence assessed",
  "evidence": "review-report.md, relevant finding locators",
  "artifacts": [{"path": "manuscript.md", "sha256": "record the actual 64-character hash"}]
}
```

A hash update alone does not resolve a scientific issue. After a substantive change, reopen affected assessments, perform the necessary checks, preserve their reports and then update the current register. The CLI neither repairs records nor executes recorded analysis commands.
