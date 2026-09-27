# Agent contracts and cost profiles

Use roles appropriate to the question; do not start every role on every turn. Default concurrency is coordinator plus three specialists, bounded by the host. No third-party service or paid API is activated automatically.

| Role | Inputs and accountable output | Balanced default |
|---|---|---|
| Author coordinator | Intake, objective/contribution map, section plan, state and master integration; no editorial verdict | Balanced model, medium reasoning |
| Evidence specialist | Search log, topic/claim coverage, appropriate source types, citation/bibliography reconciliation and exact support; no invented full-text verification | Balanced, medium |
| Measurement/data specialist | Verified manuals, data dictionary, scoring, missingness and transformations | Balanced, high |
| Author methodologist | Estimand, executable plan, diagnostics, effects/intervals and limitations | Balanced, high; escalate complex central risks |
| Scientific writer | Evidence-linked prose and declarations actually supplied | Balanced, medium; high for complex interpretation |
| Figure specialist | Executed outputs, reproducible visualizations and rendered/export checks | Balanced, medium; omit if unnecessary |
| Source/consistency verifier | Claim support, identifiers, repeated numbers and dependencies | Balanced, medium; deterministic checks in code |
| Reviewer 1: domain | Independent contextual review, objective fulfillment, missing explanations and fresh-reader understanding; bounded interpretation | Balanced, high |
| Reviewer 2: methods/statistics | Independent validity, dependence, missingness, multiplicity and uncertainty review | Frontier, high in balanced/quality profiles |
| Reviewer 3: measurement/technical | Instrument validity or domain-specific technical risks | Balanced, high; escalate unresolved central risks |
| Editorial secretary | File completeness, anonymity, format requirements and current delivery-register/hash checks | Economical, medium; no merit judgment |
| Simulated handling editor | Reasoned synthesis, required changes and simulated decision | Balanced, high; frontier for substantive conflict |
| Copyeditor and terminology editor | Grammar/style and a separate discipline-specific terminology pass; preserve customary English terms, exact identifiers and the shared term list. Substantive or uncertain meaning changes return to domain/content review | Economical, medium for bounded checks; balanced for unresolved domain ambiguity |

## Cost profiles

- **Economy:** balanced models for substantive roles including methods review; economical models for bounded clerical work. Escalate central validity questions. Preserve reviewer separation, evidence checks and honest limits; reduce repeated passes/context instead of dropping validation.
- **Balanced (default):** table above, with one frontier methods/statistics reviewer in the first full round. Subsequent reviews focus on changed dependencies.
- **Quality:** frontier methodological planning and substantive editorial conflict assessment; balanced for writing/evidence, economical for clerical tasks. Higher expense is not a correctness guarantee.

Model examples for hosts exposing them: GPT-6 Luna = economical; GPT-6 Sol = balanced; GPT-6 Astra = frontier. Availability and reasoning settings must be checked in the host. Other providers/local models may be mapped to capability tiers after a synthetic task evaluation. No provider is required; no clinical expertise certification is implied.

Use the least costly configuration that passes the relevant task checks. Start scoped work at moderate reasoning; use high for substantive review, stronger settings only after a specific unresolved failure. Do not duplicate whole conversations or every skill in each context. Preserve reports and recheck only affected dependencies after revisions, with full manuscript available for coherence.

Escalation requires a concrete central uncertainty, disagreement or failed targeted attempt. State the question and evidence before retrying. Log actual model, settings, calls and cost/tokens if the host exposes them; estimates remain estimates. Apply a user-specified budget, saving state before exceeding it. Without usage telemetry do not promise a hard metered ceiling.

API charges differ from subscription quotas. Never silently switch to a billed API. Prices, cache eligibility, tools and reasoning tokens affect task cost and change over time: check [official model selection](https://developers.openai.com/api/docs/guides/model-selection) and [pricing](https://developers.openai.com/api/docs/pricing) for OpenAI, or the chosen provider's equivalent.

## Delegation contract

Each assignment specifies goal, allowed inputs/version, applicable skill, output, evidence standard, competence limits and recipient. Use new reviewer contexts without drafting history or other reports at first pass. Prompt-based separation is not enforced file access separation. Record fallback sequential role simulation honestly.

The root model remains the user's configured model unless the host allows an authorized change. When the user invokes this agentic workflow, use subagents only within their request and host permissions. Do not create new user-owned chats, contact people or assume external service authorization. Never claim an override worked without observing it.
