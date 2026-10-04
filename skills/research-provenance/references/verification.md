# Executable verification and official test material

Use `scripts/verify_provenance.py` from this installed skill folder; Python 3.10+ and the standard library suffice. The helper inspects one file, hashes the tested bytes and creates JSON. It never edits originals, installs a detector or certifies human authorship. Reports may include private assertions and author metadata; retain them within the project's processing boundary.

## Local C2PA route

An existing trusted [C2PA Tool](https://github.com/contentauth/c2patool) is required; the integration was exercised with 0.28.1. Follow the [official read/trust options](https://github.com/contentauth/c2patool/blob/main/docs/usage.md). From the skill directory:

```bash
python3 scripts/verify_provenance.py c2pa figure.jpg --report figure.c2pa.audit.json
```

Use `--c2patool /absolute/path/to/c2patool` for a separately installed executable. A cached local trust list can be supplied with `--trust-anchors /absolute/path/to/trust.pem`; its hash is recorded. The helper passes explicit settings, excludes inherited C2PA configuration and inspects an isolated copy. Remote manifest/OCSP fetching is disabled and the SDK host allowlist is empty. Adjacent sidecars are not resolved. Use a compatible tool version and, for a strict offline boundary, the host's network sandbox as well; tool settings are not an operating-system network firewall. Older/unrecognized schemas remain UNKNOWN instead of being inferred valid. The raw validator state, diagnostics and trust policy remain available in the report. `Valid` and `Trusted` are distinct; neither asserts that the work is true or AI-free.

The [C2PA public test files](https://spec.c2pa.org/public-testfiles/) provide validator interoperability/conformance cases, including positive and negative assets where available. Read each case's format/version/README and compare actual diagnostics with that expected case. Test roots belong to test environments, not production trust policies. These fixtures test credentials, not authorship classifiers. The collection has its own CC BY-SA license and is not redistributed in Galileo's MIT payload. Passing selected cases does not make Galileo a C2PA-certified product.

## Official OpenAI media route

The [official API guide](https://developers.openai.com/api/docs/guides/content-provenance) and [response reference](https://developers.openai.com/api/reference/resources/content_provenance_checks/methods/create) define the integration. The optional [browser verifier](https://openai.com/verify/) is an alternative; do not upload research assets without authorization.

```bash
# Plan only: no credentials read, no network request.
python3 scripts/verify_provenance.py openai-media figure.png --dry-run

# Only after authorization to upload this file and configure an eligible account.
# Set OPENAI_API_KEY securely through the host; never paste it into the report.
python3 scripts/verify_provenance.py openai-media figure.png --allow-upload --report figure.openai.audit.json
```

This route checks supported images/audio only, with a 50-MiB limit and decoded audio at most 60 seconds. PCM WAV duration is checked locally; other audio relies on server validation. The API is not eligible for Zero Data Retention. Requests use the fixed official endpoint, one file, no redirects and no automatic retries. Missing credentials/access, unsupported formats, transport failures and rate limits produce unavailable/unknown checks rather than negative detections.

Read each `results` entry separately. `c2pa.outcome` concerns OpenAI AI-generation credentials; `validation_state` also describes non-OpenAI or invalid credentials. SynthID detection is separate. A negative signal does not exclude AI involvement. The report retains bounded official results while redacting the configured credential. No SDK subscription or live account is installed by Galileo.

## Text and generic classifiers

[Anthropic's official announcement](https://www.anthropic.com/news/claude-text-watermark) describes restricted private-preview access for text-watermark verification. Galileo does not invent an API endpoint/schema: obtain legitimate access and current documentation before adding a compatible adapter, or record UNAVAILABLE. A generic writing classifier is not this provider-key verification. Inspectors cannot use the media routes above to verify the word choices of a DOCX/PDF manuscript.

## Exit codes and rechecking

Exit 0 means a completed supported check, including a negative finding; it is not an AI-free pass. Exit 2 means unavailable, not tested, unknown, invalid, or a local input/output error. Read the JSON status and each scheme's fields. `--report` refuses existing paths before executing a verifier; select a new report per revision. Dry-run reports remain NOT TESTED. If editing was authorized, compare originals and derivatives with the same compatible checks and record any credential loss/invalidity; never seek a score that hides AI assistance.

Package tests mock the remote API and exercise failure/scope boundaries. The release review separately records the actual local tool and selected official fixtures exercised. No public universal benchmark certifies a thesis's human authorship.
