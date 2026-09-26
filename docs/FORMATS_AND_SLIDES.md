# Manuscript formats and scientific slides

## Installation versus activation

| Profile | Original entry points | Upstream support | Total skill folders |
|---|---|---|---|
| core | Project support, drafting, review | Seven core scientific skills | 10 |
| docx | Core entry points plus typesetting | Seven core scientific skills | 11 |
| latex | Core entry points plus typesetting | Core plus academic-writing-latex | 12 |
| slides | Core entry points plus presentations | Core plus scientific-slides | 12 |
| publishing | DOCX entry points plus thesis-to-article and submission | Seven core scientific skills | 13 |
| defense | Slides entry points plus defense rehearsal | Core plus scientific-slides | 13 |
| systematic | Core entry points plus systematic review | Seven core scientific skills | 11 |
| full | All nine entry points | All nine upstream skills | 18 |

Full installation does not activate every skill on every task. Set `manuscript_format` to docx or latex; leave it null until intake resolves the choice. Presentation outputs default to PPTX plus PDF and are independent of manuscript format. A Word thesis can produce Beamer slides; a LaTeX paper can produce editable PowerPoint.

## Online skill selection

- [HS0n4 academic-writing-latex](https://github.com/HS0n4/academic-writing-latex-skills): MIT; equations, floats, bibliography and cross-reference guidance. Its English/engineering/IEEE assumptions are overridden by user/venue requirements, and syntax must match the engine.
- [K-Dense scientific-slides](https://github.com/K-Dense-AI/scientific-agent-skills/tree/49c6e97775eaa18ba791bebe23162a70ae601c18/skills/scientific-slides): MIT; talk structure, timing, design, Beamer templates and visual review. External generative services are optional and inactive by default. Real user identity and verified charts are preserved.

Sources, revisions, licenses and hashes are pinned in vendor/provenance.json. No popularity or empirical superiority claim is made. Original research-typesetting and research-presentations route these skills to actual tools. Restricted redistribution licenses excluded other document skills from this public bundle.

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

Scientific manuscript review precedes format QA; meaning changes return to review. Presentations: evidence map/storyboard → draft → export/render → distinct science and visual review → correction → reconciled files. Default three rounds, two without progress stop unresolved.

Package tests validate installation, routing and provenance. End-to-end DOCX, LaTeX, PPTX and PDF production has not been tested on every host; use the synthetic evaluation protocol with your actual runtime.
