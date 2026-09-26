# Release preparation review

## Changes from the private prototype

- English entry points named research-drafting/research-review; output language, field, design, institution, venue and processing boundary come from intake.
- No country-specific access service, clinical cohort, personal filesystem path, original conversations or project-specific documents in the release.
- The workflow skills are self-contained with relative references, and the installer installs the scientific skills alongside them.
- Configurable roles, review count, limits, provider/model mapping and cost profiles; model recommendations are not asserted benchmarks or fixed-price guarantees.
- Explicit distinctions between instructions and execution engine, installed and discovered, context separation and access enforcement, AI inspection and human verification, simulation and actual review/submission.
- Pinned upstream content, full license notice, version inventory, file hashes and non-overwriting offline installation.
- Watermark removal and unrelated experimental services are excluded: they are outside scientific drafting/review scope.

## Validation boundary

Installer behavior, package links, skill structure and provenance are checked locally and in the supplied CI workflow. The synthetic behavioral protocol is not a completed empirical evaluation. No live dataset, paid service, real journal submission or external manuscript transfer is used in release preparation. Host discovery/parallelism and scientific performance must be checked in each deployment.

Local release checks passed: five installer tests (dry-run, full installation, collision preservation, tampered-content rejection and copy-failure rollback), package/provenance/link validation, and the Codex skill-creator structural validator for both original entry points. No CI run is implied by these local results.

## Format and presentation extension (2026-09-27)

Added conditional DOCX/LaTeX typesetting, a scientific presentation workflow with PPTX/PDF and PDF-only Beamer routes, and two MIT upstream support skills found online. Four original entry points and nine upstream skills are now available. Separate core/docx/latex/slides/full installation profiles preserve non-overwrite behavior.

LaTeX source provenance and license differ from K-Dense and are recorded per skill; the installer copies the correct license. Six installer tests pass, including conditional-profile exclusion and distinct license/source preservation. Both new original skills passed the skill-creator structural validator; package validation and whitespace checks passed. No end-to-end document or deck production is claimed by these packaging checks.

## Optional literature integrations (2026-09-27)

Added independent MCP configuration examples for PubMed/Europe PMC, OpenAlex, Crossref and experimental Zotero. Source commits and top-level npm versions are pinned; transitive dependencies are explicitly not locked. npm registry metadata confirmed all three selected versions and Node 24+ requirements. No adapter source is redistributed. No global client configuration or private library was accessed or modified.

Codex entries remain disabled and optional, with retrieval-tool allowlists; JSON client fragments require host-specific permission setup. Startup indexing risk in Zotero is documented and the probe refuses an existing semantic startup config. Drafting/review instructions include source routing, budget tracking and query/access records. The connection diagnostic only initializes and lists tools.

Twelve tests passed under bundled Python 3.11+, along with offline catalog, package provenance/link and whitespace checks. The system Python lacked tomllib, so the complete suite was rerun with the bundled runtime. MCP protocol tests use local fake servers, including paginated tool discovery, missing tools, malformed output, server error and timeout. No live server connection, upstream API search, full-text access or client permission enforcement is claimed.
