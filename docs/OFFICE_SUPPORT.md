# Native Office support

Galileo uses the selected application's editable features when supported and appropriate to the task. It checks capabilities before producing the file, keeps existing templates/managers where compatible, and records static fallbacks. This applies across Word, Excel and PowerPoint; it is not limited to bibliographies or contents pages.

| Format | Preferred behavior |
|---|---|
| Word / DOCX | Heading and list styles, automatic contents/lists, captions and cross-references, pagination fields, native tables/equations/notes, supported linked citations and bibliography; real comments/revisions when requested |
| Excel / XLSX | Typed data, appropriate tables/filters/validation, maintainable formulas and recalculated results, chart-to-data links, scientific scoring and missing-data fidelity |
| PowerPoint / PPTX | Template masters/layouts/themes, editable text/tables/charts/diagrams where required, speaker notes and preserved object relationships |
| PDF export | Export from the same final editable artifact, then inspect pages/slides and reconcile content, references, pagination and fonts |

Only relevant features are applied. Observed data and fixed analysis outputs may remain values; an original scientific figure may remain an image. A requested static/flattened artifact is a valid scope. Native features do not establish scientific correctness.

## Skills used

Galileo first looks for a suitable licensed skill already available in the harness: documents/Word, spreadsheets/Excel, presentations/PowerPoint. Names and dependencies differ by provider. The selected skill is loaded at the actual production/editing step, not for a prose-only request.

For a portable fallback, the package includes [Magnus Hedemark's `documents` skill](https://github.com/magnus919/agent-skills/tree/9b34a87ee729f109019ac604681e5796349ea1b2/documents), pinned at `9b34a87ee729f109019ac604681e5796349ea1b2`, under its [MIT license](../vendor/documents/LICENSE.md). It provides DOCX/XLSX/PPTX/PDF references, templates, fixtures and a basic structural/render checker. Galileo's additional [Office capability instructions](../skills/galileo/references/office-capabilities.md) govern native features and scientific delivery checks. Upstream files are copied unchanged; provenance records their hashes. This is a third-party support skill, not an Office application or a claim of superiority.

It is included in `full`, `docx`, `slides`, `publishing` and `defense`. Existing installations need a deliberate reconciled update or a fresh destination; the installer does not overwrite another `documents` skill. Other profiles can use host skills and need not install Office support for an unrelated task. Installation supplies no Office licenses, applications, libraries or add-ins.

The [Anthropic document skills](https://github.com/anthropics/skills) are another host-dependent option with [separate restricted terms](https://github.com/anthropics/skills/blob/main/skills/docx/LICENSE.txt); this MIT package does not copy or install them. Available licensed host implementations can still be selected under their applicable instructions. Office skills found online are assessed for actual scope, licensing, dependencies and behavior before inclusion; popularity is not validation.

## What verification means

Galileo separates creation, preservation, refresh/calculation, export and functional verification. A generated Word field may not have been evaluated; a saved Excel formula may lack a calculated result. A bibliography metadata connector is not a Word citation add-in. Native Word sources or an existing supported reference manager are used when available; static bibliographies are explicitly identified and retain machine-readable metadata.

Required dynamic behavior is checked on a disposable representative sample/copy, then the actual final artifact is refreshed and inspected with a capable tool. In tracked runs, each relevant feature is recorded as structurally present, functionally verified, not tested or unsupported. Unsupported essential functionality keeps the relevant readiness check pending. A basic ZIP check, a converter result or an update-on-open flag alone cannot close it.

The bundled validator checks container signatures, selected required parts and selected XML. It does not verify all relationships or native features. Read each per-file result; skipped or unavailable checks are unperformed even when the exit code is zero. Its Office `pages` value counts generated PDF files, and PDF raster checking may cover only page 1. Full final page/slide inspection remains separate. See the [precise usage limits](../skills/galileo/references/office-capabilities.md#basic-validator-bounded-use).

## Example requests

```text
Use Galileo to format this thesis as Word and PDF using the university template.
Use native Word structures where supported, including the table of contents,
captions and internal references. Preserve the existing Zotero integration.
Verify what can actually be updated and report any static fallback.
```

```text
Use Galileo to create an Excel scoring workbook from the supplied questionnaire
rules, preserving missing data. Keep calculations editable, verify recalculated
results, and prepare editable PowerPoint slides from the checked findings.
```

These instructions change future production and requested revisions. Installing a skill does not retroactively repair existing DOCX/PPTX/XLSX files.
