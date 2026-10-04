# Manuscript formats and scientific slides

## Installation versus activation

| Profile | Original entry points | Upstream support | Total skill folders |
|---|---|---|---|
| core | Project support, drafting, review, AI provenance | Seven core scientific skills | 12 |
| docx | Core entry points plus typesetting | Core scientific skills plus documents | 14 |
| latex | Core entry points plus typesetting | Core plus academic-writing-latex and latex-safe-build | 15 |
| slides | Core entry points plus presentations | Core plus scientific-slides, documents and latex-safe-build | 16 |
| publishing | DOCX entry points plus thesis-to-article and submission | Core scientific skills plus documents | 16 |
| defense | Slides entry points plus defense rehearsal | Core plus scientific-slides, documents and latex-safe-build | 17 |
| systematic | Core entry points plus systematic review | Seven core scientific skills | 13 |
| full | Galileo and ten specialist workflows | All eleven upstream skills | 22 |

Every profile includes the Galileo guided entry point, project support and AI provenance. Full installation does not activate every skill on every task. Set `manuscript_format` to docx or latex; leave it null until intake resolves the choice. Presentation outputs default to PPTX plus PDF and are independent of manuscript format. A Word thesis can produce Beamer slides; a LaTeX paper can produce editable PowerPoint.

## Online skill selection

- [HS0n4 academic-writing-latex](https://github.com/HS0n4/academic-writing-latex-skills): MIT; equations, floats, bibliography and cross-reference guidance. Its English/engineering/IEEE assumptions are overridden by user/venue requirements, and syntax must match the engine.
- [K-Dense scientific-slides](https://github.com/K-Dense-AI/scientific-agent-skills/tree/49c6e97775eaa18ba791bebe23162a70ae601c18/skills/scientific-slides): MIT; talk structure, timing, design, Beamer templates and visual review. External generative services are optional and inactive by default. Real user identity and verified charts are preserved.

- [Magnus Hedemark documents](https://github.com/magnus919/agent-skills/tree/9b34a87ee729f109019ac604681e5796349ea1b2/documents): MIT; portable Word/Excel/PowerPoint/PDF guidance and basic package validation. Galileo adds native-feature requirements and stricter delivery checks; the upstream tool is not a Word field evaluator or scientific reviewer.

- [latex-safe-build](https://github.com/molanocortes/latex-safe-build/tree/d6cd2314676c44a56e58c8f892082ef00a6a8371): MIT; optional isolated POSIX local builds and diagnostic/page-count support. Galileo preserves native compiler preference and checks the wrapper’s actual limits before use; it is not a universal compiler or scientific validator.

Sources, revisions, licenses and hashes are pinned in vendor/provenance.json. No popularity or empirical superiority claim is made. Original research-typesetting and research-presentations route these skills to actual tools. Restricted redistribution licenses excluded other document skills from this public bundle.

## Native LaTeX functionality

LaTeX manuscript/Beamer production uses automatic contents, counters, labels/cross-references and template-compatible BibTeX or biblatex/Biber. Indexes/glossaries are activated only when needed and actually built. See [LaTeX support](LATEX_SUPPORT.md) for routing, source portability, wrapper limitations and final-version verification. The latex/slides/defense/full profiles include latex-safe-build; it is loaded only for a compatible local compile route.

## Office functionality

The `documents` skill adds MIT guidance, templates and structural tooling for DOCX, XLSX, PPTX and PDF. It is included in full/docx/slides/publishing/defense; other profiles reuse available host skills or report the missing route. Read [Office support](OFFICE_SUPPORT.md) for native features, capability limits and functional verification. Generation libraries and Office applications are not installed with the skill.

## Slide styling and representative previews

Rendered-deck production includes a design stage. Galileo reuses your supplied template or proposes two or three visual directions, recommends one and defines a common palette, typography, margins, layouts and scientific color mappings. It then builds two representative storyboard slides—normally introduction and results—and checks their actual renders before expanding the deck. A methods/concept slide replaces results if verified results are unavailable. Samples remain within the requested slide count; they do not replace final full-deck QA.

Research-group, department, university and consortium branding is supported: supply logos, color/font specifications, a brand-book PDF or an existing PPTX/POTX/Beamer template. If you name the institution and ask for branding without assets, Galileo can look for official guidelines/downloads using available browsing. It preserves logo proportions/variants and co-branding rules, records asset sources and font substitutions, and keeps scientific charts readable. Missing official assets remain unresolved rather than being invented. A brand-book PDF guides style but is not an editable slide template.

Optional preferences do not halt reversible production unless you request approval first. Text-only outlines and notes skip theme/sample-export setup; scoped deck edits preserve the existing style. Style decisions and actual checks are kept in existing presentation records. See [visual design instructions](../skills/research-presentations/references/visual-design.md).

A relevant presentation or `pptx` skill already available in your harness can support template editing and technical checks. The [Anthropic pptx skill](https://github.com/anthropics/skills/blob/main/skills/pptx/SKILL.md) has [separate proprietary terms](https://github.com/anthropics/skills/blob/main/skills/pptx/LICENSE.txt) and is not redistributed or installed by this MIT bundle. Galileo works with available licensed host capabilities or the documented local fallback; no extra styling skill is required by the installer.

## Capabilities and dependencies

| Output | Preferred route | Local fallback if needed | Limits to record |
|---|---|---|---|
| DOCX | Host document skill/tool | python-docx or template converter | Fields, native equations, tracked changes and rendering |
| LaTeX/PDF | Built-in standalone source editor/compiler if supported | Existing TeX engine, bibliography backend/packages | Multi-file support, fonts, references and visual QA |
| PPTX | Host presentation skill/tool | PptxGenJS and Node.js | Native math, editability and template/feature support |
| PDF from PPTX/DOCX | Host or office renderer | Existing PowerPoint/LibreOffice-compatible exporter | Fonts, animation flattening, notes and version agreement |
| PDF slides from Beamer | Built-in compiler if supported | Existing TeX toolchain | Frames versus overlay pages; no automatic editable PPTX |

Installation does not install these runtimes, office tools, fonts or TeX distributions. Follow actual host instructions; do not redistribute proprietary tools. When an exporter or renderer is unavailable, preserve source and mark missing build/QA instead of claiming completed artifacts.

## Verification

Scientific manuscript review precedes format QA; meaning changes return to review. Presentations: evidence map/storyboard → visual direction and shared style → representative rendered slides → full draft → export/render → distinct science and visual review → correction → reconciled files. Default three rounds, two without progress stop unresolved.

Package tests validate installation, routing and provenance. End-to-end DOCX, LaTeX, PPTX and PDF production has not been tested on every host; use the synthetic evaluation protocol with your actual runtime.
