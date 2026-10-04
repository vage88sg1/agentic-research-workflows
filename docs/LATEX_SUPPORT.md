# Native LaTeX support

Galileo's LaTeX route uses the format's maintainable structures when relevant: contents and figure/table lists, counters, labels and cross-references, native math/tables, template-compatible citations and generated bibliography. Requested glossaries/indexes are produced with their actual backends. Beamer receives the same source/build checks plus scientific slide review. A command in the source is not a finished feature; final values must be built and checked.

## Skills and activation

- **academic-writing-latex**, already bundled under MIT: writing and TeX syntax guidance. User language, field, institutional style and engine override its English/engineering/IEEE defaults.
- **latex-safe-build**, added under MIT: [isolated local builds and diagnostics](https://github.com/molanocortes/latex-safe-build/tree/d6cd2314676c44a56e58c8f892082ef00a6a8371), pinned at `d6cd2314676c44a56e58c8f892082ef00a6a8371`, copyright 2026 Juan Sebastian Molano. Its [license](../vendor/latex-safe-build/LICENSE) and exact runtime/reference/test payload are retained with hashes. It does not supply LaTeX, write scientific content or guarantee updateability.
- **Available host LaTeX skills/compiler:** selected when adequate for the actual task. A supported built-in standalone editor/compiler remains preferred; no duplicate TeX installation is required.

The latex/slides/defense/full profiles include latex-safe-build. It is loaded only for a compatible local LaTeX build, including selected Beamer output. PPTX production does not activate it. The full profile contains 21 skill folders. Existing installations need deliberate reconciliation or a fresh destination; the installer never overwrites another skill of the same name or installs libraries/TeX engines.

## What the workflow checks

| Feature | Expected result |
|---|---|
| Contents, lists and numbering | Generated from actual sections/captions/counters, with correct final page/figure/table numbers |
| Cross-references | Resolved labels and correct destinations; no duplicated/undefined targets hidden by an old PDF |
| Bibliography | Verified source metadata, matching citation commands and a compatible backend that actually builds the final references |
| Math, tables and figures | Faithful editable source and readable rendering, with preserved units, uncertainty and attribution |
| Indexes, glossaries and acronyms | Added only when relevant; required processor runs and printed entries are checked |
| PDF and source package | Current final source, assets/styles/bibliography and build instructions agree with the inspected PDF |

Galileo identifies the template, entry point, engine, fonts and backends before compilation. It reads current diagnostics, checks required reruns and validates relevant automatic changes on a disposable sample/copy for a full production route. It then rebuilds and visually inspects the actual final artifact. Missing compilation or unsupported essential features remain pending rather than being reported as passed. Scientific evidence and citation support remain separate checks.

## Tool limits

The bundled wrapper is optional POSIX guidance/tooling, not a universal safe execution guarantee. It needs existing latexmk/rsync and a compatible engine/backend. At its pinned revision it can enable shell escape automatically, reads build settings, reuses scratch paths, excludes `.bbl`, overwrites its input-directory PDF and can return success with unresolved references. Its page-count helper uses heuristic boundaries and has an optional pypdf dependency. Galileo checks these limits before use, prefers the supported native compiler where applicable, and uses a different compatible route if the wrapper would lose required sources or exceed authorized operations. See the [precise integration instructions](../skills/galileo/references/latex-capabilities.md#optional-latex-safe-build-use-within-its-limits).

Linting, compilation, rendered-output inspection, scientific review and human approval are distinct. Package tests do not establish live TeX compilation or venue compliance. No automatic Zotero/MCP dependency, fixed bibliography style, watermark operation or external image service is added by this integration.

## Example

```text
Use Galileo to format this checked thesis as LaTeX and PDF using the supplied
university template. Preserve its engine and bibliography style. Use automatic
contents, captions and references, build the bibliography from verified metadata,
and verify the final logs, cross-references and rendered pages.
```

Existing Word files are not converted unless requested. Existing LaTeX artifacts require a requested revision/build to adopt these checks; installing instructions does not alter their contents.
