# Third-party notices

The eight K-Dense directories under `vendor/` are exact copies from [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills), commit `49c6e97775eaa18ba791bebe23162a70ae601c18`, retrieved 2026-09-26 for the core seven and 2026-09-27 for scientific-slides from the same pinned revision. These are third-party instructions and optional tools, not skills maintained by OpenAI or the author of this package.

Each selected K-Dense SKILL.md declares MIT licensing. The original copyright and permission notice are retained in [vendor/LICENSE.md](vendor/LICENSE.md). `vendor/provenance.json` records hashes for all shipped upstream files. No upstream content has been modified. Original workflow integration rules are documented separately and may intentionally decline optional services or instructions outside the user's scope.

| Skill | Upstream declared version |
|---|---|
| scientific-writing | 2.1 |
| citation-management | 2.1 |
| scientific-critical-thinking | 1.3 |
| statistical-analysis | 1.2 |
| literature-review | 1.8 |
| scientific-visualization | 1.2 |
| peer-review | 2.2 |
| scientific-slides | 1.8 |

Preserve the upstream license when redistributing these files. The offline installer copies notices into each installed skill. External papers, manuals and publisher policies referenced by the skills retain their own rights; they are not made MIT-licensed by a link.

The bundled collection includes scholarly attribution guidance. When citing its contribution to research, verify the current primary bibliographic record rather than treating an embedded citation as already verified. This repository records software provenance without claiming verification of every cited research source.

## Additional LaTeX guidance

[academic-writing-latex](https://github.com/HS0n4/academic-writing-latex-skills) is an exact copy of SKILL.md and LICENSE from commit `d981a7c3057f1387f980b12a64d213fab5f2db6e`, retrieved 2026-09-27. It does not declare a numbered version. Its own [MIT license](vendor/academic-writing-latex/LICENSE), copyright 2026 HSOn04, is retained and copied by the installer. Per-skill repositories/commits/licenses are recorded in provenance.json; the top-level source record describes the K-Dense snapshot only.

The original workflow routes override field/language/citation defaults and automatic external generation as documented, without modifying upstream files. The additional guidance does not supply a compiler. The bundled scientific-slides tools include optional third-party generative API calls: no such route is started by installation or the default presentation workflow.

Restricted-license PPTX/DOCX skills are not redistributed. Original typesetting/presentation instructions use host-available licensed tools or publicly documented libraries, without copying those restricted instructions or code into this repository.

## Office document support

The `vendor/documents` directory contains the tracked `documents/` payload from [Magnus Hedemark's agent-skills](https://github.com/magnus919/agent-skills/tree/9b34a87ee729f109019ac604681e5796349ea1b2/documents), commit `9b34a87ee729f109019ac604681e5796349ea1b2`, retrieved 2026-10-04. Its MIT license, copyright 2026 Magnus Hedemark, is retained as [vendor/documents/LICENSE.md](vendor/documents/LICENSE.md). Upstream instructions, references, templates, fixtures, tests and validation script are copied unchanged; caches and unrelated repository skills are excluded. The installer retains the license and records payload hashes. The validation script declares version 1.0.0; the skill does not declare a release version.

Galileo adds original integration guidance in [Office capabilities](skills/galileo/references/office-capabilities.md): prefer an adequate licensed host skill, preserve scientific meaning and use actual native structures when supported. The upstream validator establishes limited container sanity and optional conversion/raster success, not native feature behavior, complete XML/schema validity, calculated formulas, scientific validity or complete visual QA. Linked sibling skills mentioned upstream are optional and are not installed or executed automatically. Upstream portability claims are not an end-to-end Galileo host test.

## Additional LaTeX build support

`vendor/latex-safe-build` contains the unmodified runtime, references, README/WHY, tests/fixtures and [MIT license](vendor/latex-safe-build/LICENSE) from [molanocortes/latex-safe-build](https://github.com/molanocortes/latex-safe-build), commit `d6cd2314676c44a56e58c8f892082ef00a6a8371`, retrieved 2026-10-04; copyright 2026 Juan Sebastian Molano. Its repository CI and dotfiles are excluded. Per-file hashes and the retained license are recorded in provenance; no release version is declared upstream. Original integration guidance in [LaTeX capabilities](skills/galileo/references/latex-capabilities.md) bounds when the wrapper may be used and preserves the native compiler preference. Upstream assertions of never corrupting a source tree, deterministic float placement or general institution page-count rules are not guarantees made by Galileo.

Installation does not execute tests/builds, activate shell escape, install TeX or download packages. The full upstream build test suite requires external tools and includes shell-escape fixtures. Functional/native output verification, source stability, final artifact inspection and scientific review remain separate from packaging or wrapper exit codes.

## Referenced optional MCP adapters

Configuration examples reference cyanheads/pubmed-mcp-server, cyanheads/openalex-mcp-server and cyanheads/crossref-mcp-server (Apache-2.0), plus peterdresslar/zotero-mcp (MIT). Revisions, executable references and license identifiers are recorded in `integrations/literature/servers.json`. Their server code and dependency trees are not vendored or covered by Galileo's original MIT license. Installing/running these optional adapters obtains third-party packages under their own licenses; consult the linked pinned repositories and dependency notices.
