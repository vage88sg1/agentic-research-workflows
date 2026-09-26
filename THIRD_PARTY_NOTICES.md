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
