# Office capabilities and functional QA

Read only the selected format below when producing or editing an Office artifact. This reference supplements the active scientific workflow; content evidence, terminology and review requirements still apply. A request for prose or a slide outline does not require Office tooling.

## Select the available skill and tool

Inspect the actual host catalog and relevant task tools. Prefer a suitable licensed host skill for documents/Word/DOCX, spreadsheets/Excel/XLSX or presentations/PowerPoint/PPTX; names vary by host. Read its instructions before use. Reuse an existing capable route instead of installing a duplicate. The bundled `documents` skill is MIT fallback guidance with per-format references, templates and a basic validator. Resolve it as a sibling or through the catalog. Do not assume a generic `documents` name refers to the bundled implementation if another provider supplies that name; identify the actual source.

For the requested features, distinguish **creation**, **preservation**, **refresh/calculation**, **render/export** and **functional verification**. A library may write fields but not evaluate them, or preserve formulas without calculating results. A citation metadata/search connector does not supply a Word citation add-in. Native application automation depends on operating system and exposed authorized tools; Windows COM is not a macOS or Linux fallback. Do not install Office, a plug-in, or a service merely because a skill mentions it.

Use the institution's template and the user's format choice. Prefer native, editable and updateable structures when supported and applicable. Do not substitute manually maintained text or images silently. For a real limitation, record the feature, attempted/available route, fallback and consequence in existing build/QA records. An intentionally static export or user-selected flattened document remains valid for that scope. If dynamic behavior is essential and unavailable, deliver a provisional source with that requirement pending; ask only for a decision that materially changes the deliverable.

## Word / DOCX

| Needed behavior | Preferred representation | What to verify |
|---|---|---|
| Navigation and consistent headings | Heading paragraph styles / template outline levels | Actual style/outline assignments and hierarchy; visual bold text alone is insufficient |
| Numbered headings or lists | Native numbering definitions linked to relevant paragraph styles | Numbering continues/restarts as intended when items move; do not type every number |
| Table of contents / figure or table lists | Actual `TOC` field with appropriate heading/caption selection | Field instructions and populated results; refresh after pagination changes; entries/links resolve |
| Captions and internal references | `SEQ` captions, stable bookmarks and `REF` / `PAGEREF` or equivalent application objects | Targets exist, field values update, numbers/links agree; fixed strings are not dynamic references |
| Pagination and section layout | `PAGE` / `NUMPAGES` as needed, section settings and headers/footers | Front matter/body numbering and orientation; avoid whitespace for positioning |
| Citations and bibliography | Existing supported Zotero/EndNote integration or Word sources with real `CITATION` / `BIBLIOGRAPHY` fields | Source records, citation identifiers and bibliography remain linked; chosen style and claim support are correct |
| Tables, equations and footnotes | Native tables, supported Office math and footnote/endnote objects | Editability, table headers, equation glyphs and note placement; retain formula source for a declared image fallback |
| Review and accessibility | Real comments/tracked revisions when requested, document language, descriptive links and appropriate alternative text | Review objects are present and preserved, reading order/metadata appropriate; colored text alone is not tracked changes |

Apply only relevant features. A short letter does not require a TOC, numbered chapters or citations. Figure images may legitimately remain images; their captions, attribution and references should remain maintainable.

Choose citation tooling from actual availability and style support; preserve an existing supported manager rather than converting it unnecessarily. Word's source manager is a possible route, not a universal scientific citation style engine. BibTeX/RIS/CSL metadata or static bibliography paragraphs alone do not establish live Word integration. Do not forge add-in field payloads or claim an add-in can refresh a document without checking its supported integration. Keep verified source metadata exportable, with stable IDs. If only static bibliography is feasible, label it **static**, preserve machine-readable references and document the update limitation. Never sacrifice verified locators or source meaning merely to fit a manager.

Inspect the actual saved DOCX, not just generation code. Check field instructions (including complex fields whose instructions span runs), numbering/styles, source records or supported manager payload, relationships and bookmark targets relevant to the task. Structural presence is only the first check. Use a capable authorized application/renderer to refresh fields, save, export and inspect the final revision. An update-on-open flag, cached result, successful export or ZIP validation does not prove field refresh. Some renderers do not evaluate Word bibliography/add-in fields; record this per feature.

For a long document/template route, test needed dynamic behavior on a disposable copy or representative sample: add/move a heading or caption, refresh, and check resulting TOC/number/reference changes. When live citations are required, test a source/citation change with the chosen manager. Preserve the authoritative deliverable during this test. Record **structurally present**, **functionally verified**, **not tested** or **unsupported** per relevant feature; do not claim general Word compatibility from one test. Restore/rebuild the intended content, refresh the actual final source and derive the requested PDF from it. Inspect final TOC page numbers, bibliography, captions and references after layout changes. If refresh cannot be run, distinguish pending refresh from confirmed values; provide concise instructions appropriate to the user's application.

## Excel / XLSX

Use an available spreadsheet skill or bundled `documents` Excel guidance for requested extraction, scoring, results or calculation workbooks. Preserve raw inputs and the scoring/analysis specification; do not introduce an XLSX deliverable into a prose-only request.

- Preserve cell types, dates, units, missing-data semantics and identifiers. Do not turn missingness into zero or identifiers into numbers. Use native tables/filters, appropriate validation, number formats, named ranges and freeze panes where useful; avoid decorative merged cells inside analysis tables.
- Use formulas for calculations expected to remain editable; verified observed data and fixed analysis outputs can be values. Map formulas to the scoring/analysis rules, including reversed items, missing-item thresholds and denominator choices. Recalculate through a capable engine, inspect resulting errors and compare representative outputs with independently computed expected results. Writing formulas or a recalculation flag is not calculation; cached results can be missing/stale. Do not invent caches to imitate execution.
- Prefer native charts linked to actual ranges when editable charts are required and the chart type can truthfully represent the result. Keep uncertainty and labels correct; a specialized scientific figure may remain a source-backed image with an explicit editability limit. Check workbook dependencies, external links, hidden data and print/export scope as relevant. Preserve macros/advanced objects only with a compatible route; disclose potential loss before a destructive round trip.

An Excel workbook is an authoring/delivery format, not evidence that statistical analysis is valid. Scientific and computation checks remain separate.

## PowerPoint / PPTX

Use an available presentation skill or bundled `documents` PowerPoint guidance together with research-presentations/scientific-slides for a scientific talk. Reuse appropriate masters, layouts, placeholders, theme colors/fonts and native objects from a supplied template. Preserve slide size, notes, branding and object relationships. Use native text, real tables/charts and editable diagram shapes when supported and required; do not flatten an entire slide merely to reproduce its appearance. Original scientific images can remain images, with sources and legible annotations.

Check actual editable objects, master/layout relationships, chart data, notes, links and reading order. Preserve or declare lost animations, media, equations or embedded objects when converting. Confirm slide order/count, font substitutions and PDF agreement from the final deck. Render and visually inspect all final slides at the intended presentation size; an editable deck or a successful converter pass alone does not establish readable slides. Scientific verification remains distinct.

## Basic validator: bounded use

After reading the bundled skill, the installed command from its `documents/` directory is:

```bash
python3 scripts/validate-documents.py --json manuscript.docx results.xlsx talk.pptx
```

Add `--render-check` only when the available route is appropriate. Review **each file's** format, status, checks and render result; exit zero or an aggregate `ok` may include skipped unsupported files or unavailable rendering. Treat skipped/unavailable operations as unperformed, not passed. The upstream Office render report's `pages` counts generated PDF files, not document pages. Its PDF raster check covers page 1 for some engines. Neither is a substitute for final whole-document/deck inspection. The script does not prove OOXML schema conformance, relationships, native feature behavior, formula calculation, citation correctness, accessibility compliance or scientific validity. Do not run an unsafe round trip just to obtain a green result.

## Delivery and sources

For a tracked run, keep the selected skill/tool/version, relevant native feature statuses, static fallbacks, actual refresh/calculation/export commands and final artifact hashes in the existing records. Pending functional checks stay pending. Apply the active workflow's final-version delivery gates; do not add a new configuration form or promise absolute quality.

Primary references (consult current product/platform support when needed): [Microsoft Word field updates](https://support.microsoft.com/en-us/word/update-fields), [Word bibliography objects and source XML](https://learn.microsoft.com/en-us/office/vba/word/concepts/working-with-word/working-with-bibliographies), [Word citations](https://support.microsoft.com/en-us/word/add-citations-in-a-word-document), [Zotero word-processor integration](https://www.zotero.org/support/word_processor_integration), [python-docx](https://python-docx.readthedocs.io/en/latest/), [openpyxl formula limits](https://openpyxl.readthedocs.io/en/stable/simple_formulae.html), [python-pptx](https://python-pptx.readthedocs.io/en/latest/).
