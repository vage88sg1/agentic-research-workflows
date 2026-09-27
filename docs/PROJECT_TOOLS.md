# Project checks and a runnable synthetic example

Research project supplies five offline Python commands: `preflight`, `evidence`, `impact`, `delivery` and `bundle`. They complement the agent workflows with file/record checks, not semantic fact-checking or automatic scientific approval. The [installed skill guide](../skills/research-project/references/project-tools.md) describes schemas, exit codes and limits.

Run these examples from the repository root. After installation, use the corresponding script inside the installed research-project directory instead.

```bash
python3 skills/research-project/scripts/research_tools.py preflight
python3 skills/research-project/scripts/research_tools.py evidence --map examples/synthetic-project/research-map.json
python3 skills/research-project/scripts/research_tools.py impact --map examples/synthetic-project/research-map.json --root examples/synthetic-project --changed data
```

The supplied [synthetic project](../examples/synthetic-project) contains four artificial values, a standard-library analysis, its result, a short manuscript/slide source and a complete dependency map. It has no empirical or clinical meaning. The impact example should identify the analysis, result, claim, manuscript and slides as requiring recheck. It does not mutate them or their state.

For a bundle choose a fresh destination whose parent already exists:

```bash
python3 skills/research-project/scripts/research_tools.py bundle --manifest examples/synthetic-project/reproducibility-manifest.json --root examples/synthetic-project --dest /tmp/galileo-synthetic-bundle
```

The directory will contain only explicitly listed files under `payload/`, plus recorded environment/commands and hashes. Existing destinations are refused. For this specific inspected synthetic example, execute its recorded analysis in the payload directory:

```bash
cd /tmp/galileo-synthetic-bundle/payload
python3 analyze.py
```

The resulting `results.json` should contain `n: 4` and `mean: 7.0`. The packager itself never runs that command. Compare generated results with the original result to distinguish successful packaging from a completed reproduction. This example uses no third-party libraries and does not test a real research analysis, document render or MCP service.

For your own project, copy and fill the [research-map template](../skills/research-project/assets/research-map.json) and [reproducibility manifest](../skills/research-project/assets/reproducibility-manifest.json). Empty templates are intentionally incomplete. Use actual hashes, explicitly permitted files, dependency/environment records and truthful verification status. Do not put tokens or private material in manifests, commands or supposedly public files.

Evidence and delivery check exit 2 means review items exist; exit 1 means malformed input or I/O failure. A successful structural check cannot determine whether a source really supports a claim. The AI/human evidence verifier must inspect the material and record its reasoning. Impact tracking only covers registered dependencies. Preflight finds executable names but cannot infer native host capabilities or validate a server connection.

## Check final delivery records

For a tracked final handoff, ask the assistant to maintain one current output register and record checks actually performed against those revisions. The [delivery schema](../skills/research-project/references/project-tools.md#delivery-record-check) distinguishes content, bibliography, review and production readiness from operational completion. The assistant can normalize compatible existing records into a snapshot; users do not need to complete another configuration form.

```bash
python3 skills/research-project/scripts/research_tools.py delivery --state /path/to/project/delivery-state.json --root /path/to/project
```

This read-only command compares selected output bytes with their registered hashes and active check records. It reports stale or absent reviews, pending readiness and missing recorded independence when required. Updating a hash alone cannot renew an old review. Historical checks can remain but cannot close a current requirement. A clear report establishes record consistency only: source support, completeness, genuine reviewer independence, rendered layout and human approval still require their respective assessments.
