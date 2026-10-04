# Inspection routes and interpretation

Choose only routes relevant to the supplied files. The package installs instructions, not a proprietary text verifier, C2PA binary, Office renderer or forensic laboratory. A tool name in this table is not proof it is installed or operational. Prefer authorized local inspection; check the current tool documentation and version before executing. Network access, external manifest resolution and web uploads are separate from local file reading.

| Material | Useful inspection | What it cannot establish |
|---|---|---|
| TXT/Markdown/TeX/BibTeX | Actual text, source comments, explicit AI-use statements and any identified formatting/control characters | Provider-specific statistical watermark absence or human authorship |
| DOCX | Core/custom properties, comments/revisions where relevant, header/footer objects and rendered pages; preserve citation/TOC fields | Absence of a watermark in paragraph word choices; completeness of inspection from a ZIP scan alone |
| PPTX/XLSX | Core/custom properties, relevant editable objects/assets/notes and actual renders; preserve charts/formulas | Authorship or watermark state of every embedded asset from outer metadata alone |
| PDF | Document information/XMP, signatures, watermark/page objects with actual page renders | Valid provenance from a creator field; signature preservation after rewriting |
| Images/SVG/audio/video | Supported C2PA validator and an authorized scheme-specific verifier when available; source/asset inspection | Universal AI-free certification or a conclusion about surrounding manuscript text |

Use available licensed document/presentation/PDF tools for native inspection and narrowly scoped editing. Some Office/PDF tools omit custom properties, revisions or embedded assets; name the coverage. Do not parse archives by extracting arbitrary member paths into the workspace, run macros or execute document code. A format conversion can destroy native structures and signatures: it is not a neutral cleanup.

[C2PA Tool](https://github.com/contentauth/c2patool) is an optional open-source inspector for supported media manifests. Follow its current read/validation documentation and retain returned diagnostics; reading a manifest alone does not validate trust or all assertions. Do not invent signing keys or auto-install it during an inspection request. Read the [C2PA explainer](https://spec.c2pa.org/specifications/specifications/2.2/explainer/Explainer.html) to distinguish provenance, integrity and factual truth. Credential absence does not demonstrate authenticity or human creation. Embedded document assets need their own supported-file checks.

For actual local C2PA checks and the opt-in official OpenAI media API adapter, read [verification.md](verification.md). Preserve its JSON outputs and explicit untested scope in the project audit.

## Provider-specific verification snapshot

Primary sources checked 2026-10-04; recheck before using a live service or making an availability claim.

- [Anthropic text watermark documentation](https://www.anthropic.com/news/claude-text-watermark): describes statistical word-choice marking, not hidden characters; its detection API is in private preview for eligible organizations. Do not assume a public key/API or that the result distinguishes generation from heavy editing. Supported-file credentials are separate from text marking.
- [OpenAI provenance update](https://openai.com/index/advancing-content-provenance/): describes supported image/audio provenance verification. Do not reinterpret it as a general manuscript-text detector. Negative results are not proof that AI was uninvolved.
- [OpenAI's retired text classifier](https://openai.com/index/new-ai-classifier-for-indicating-ai-written-text/): historical example of classifier limitations, not an available tool to invoke. Generic AI classifiers and provider-key watermark checks are different methods.

Optional generic classifiers (examples, not bundled integrations or accuracy endorsements):

- [Turnitin AI Writing Report](https://guides.turnitin.com/hc/en-us/articles/22774058814093-Using-the-AI-Writing-Report): verify institutional access, qualifying text and supported language. Its documented language list at this check does not include Italian. Its AI-writing percentage is separate from text similarity; its own guidance requires further human assessment rather than a sole adverse-decision basis.
- [Pangram model card](https://www.pangram.com/research/model-card/pangram-4): check the current model, language and text-length coverage and exact output semantics. Italian is listed for this version; the vendor describes confidence as not a calibrated probability. Vendor results do not establish performance on this user's thesis. External processing still needs authorization.

Do not extrapolate one provider's deployed marks to every model/version or all AI writing tools. Do not infer EU compliance or a legal removal right from a detector result. For a particular institution/journal and jurisdiction consult current official requirements; report unresolved scope rather than asserting a universal legal mandate.

## Compact audit and cleanup record

For a small task, a concise response plus original/derivative links may suffice. For a tracked audit record:

- Requested scope, authorized processing/cleanup, exact file names and source/derivative hashes.
- One finding per scheme or metadata/visible-mark check: location, actual tool/version/command or consulted source, observed result, SIGNAL PRESENT/NOT FOUND IN THIS CHECK/INVALID/UNKNOWN/NOT TESTED/UNAVAILABLE as appropriate, and coverage limits. These labels are observations, not a universal verdict.
- Original metadata/credential evidence retained privately when needed, requested fields/objects changed, and any credential/signature loss or invalidation on the derivative.
- Source-content/native-feature and rendered-output comparisons, checker/context/version, unresolved items and relevant disclosure policy/source/date.

Only claim removal of the specifically inspected, authorized mark/property after a successful before/after check. Removing ordinary metadata does not imply a statistical watermark was changed. Preserve copyright/attribution and truthful required disclosure; don't state that the work was human-only on the basis of this audit.
