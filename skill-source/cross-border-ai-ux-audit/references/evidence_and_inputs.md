# Evidence & Inputs

The quality of the audit is bounded by the quality and breadth of evidence supplied. Always record what was reviewed and what was not available, and never draw conclusions that exceed the evidence level.

## Project context (collect for every audit)
Client/company name; product name; product type; source market; target market; target audience; business goal. The business goal distinguishes, e.g., a self-serve trial-conversion audit from an enterprise pilot-readiness audit.

## Supported material types
Core (well supported by a text-driven audit):
- landing page copy
- onboarding flow (described step by step)
- chatbot conversation transcript
- agent prompt and response
- app store listing
- pricing page
- trust and safety copy
- screenshot notes (text descriptions of screens)
- other supporting material

A more mature audit can also use: live product access; interface screenshots; screen recordings; information architecture; help-center/support content; sales decks/demo scripts; privacy and data-use disclosures; error and empty states; refusal/escalation examples; analytics/funnel data; user research; support tickets; model-evaluation results; competitor/category references.

## The three evidence levels

| Level | Evidence | What it supports |
| --- | --- | --- |
| **1 — Copy review** | Pasted text, scripts, prompt/response samples | Language, claims, clarity, trust copy, rewrite recommendations |
| **2 — Flow review** | Screenshots, screen recordings, step-by-step flows | Interaction design, onboarding, navigation, control, recovery, conversion |
| **3 — Behavior review** | Live product, test accounts, analytics, user research, model evaluations | Actual AI behavior, failure handling, adoption barriers, deeper market-readiness conclusions |

## Rules
- **State the evidence level** reached for the audit (and per dimension where it varies). Text-driven audits are typically Level 1 plus text-described Level 2.
- **Do not exceed the evidence.** Don't assert Level-3 behavior conclusions (e.g., "the agent fails to escalate") from Level-1 copy alone; instead note it as a flagged risk to verify with live testing.
- **Record gaps.** List materials that were requested but unavailable; thin coverage must be disclosed in the report's limitations.
- **Uploaded files are not auto-extracted.** If a material is referenced but its content wasn't provided as text/described, treat it as not-reviewed and say so.

## Live evidence capture (raising the evidence level)
Text-only evidence is the skill's biggest honesty limit. When you have URLs (or local HTML), use `scripts/capture_evidence.py` to capture, for each page, a full-page **screenshot** plus **extracted visible text**, written to an evidence folder with a `manifest.json`. Then analyze the screenshots multimodally so findings can cite **real Level-2 evidence** (rendered states, layout, contrast, controls) instead of inferring from pasted copy.

- Record the captured artifact on each grounded finding via `evidence_ref` (e.g. `"pricing.png"`), and point `meta.evidence_capture.manifest` at the manifest.
- Best-effort: if the browser tooling is unavailable or a page fails, the manifest records it and the audit falls back to text evidence — **state clearly** what was and was not captured, and don't raise the evidence level for un-captured surfaces.
- Live URLs require outbound network access; local `file://` inputs always work. Accessibility findings especially benefit from a real screenshot (contrast, labels, focus).
