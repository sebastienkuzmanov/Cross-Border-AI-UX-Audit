# Limitations & Safety

Read before delivering any report. This covers what the audit must never claim, the controlled tone vocabulary, expert-review escalation, client-data handling, and the limitations to disclose.

## The audit must not present legal advice
The audit can **flag** concerns related to privacy, data transfer, regulated sectors, claims, or market-entry obligations — and must direct those items to qualified local **legal, compliance, privacy, security, or domain experts**. It does not give the legal/compliance opinion, certify compliance, or guarantee anything.

A cross-border AI UX audit is **not**: a literal translation review; grammar-only proofreading; a legal opinion or regulatory certification; a security penetration test; a model benchmark or technical-accuracy evaluation; a replacement for local user research; proof of compliance in any jurisdiction; or a guarantee of product-market fit.

## Controlled tone vocabulary
Keep the tone analytical, practical, and non-accusatory. Always separate facts, evidence-backed findings, inferences, and uncertainties.

Use terms such as: *market-readiness, market-fit gap, conceptual risk, trust threshold, AI boundary, scoped capability, control surface, evidence-grounded, limited local proof, unclear novelty/positioning, requires expert review, working hypothesis.*

Avoid terms such as: *non-compliant, illegal, certified, guaranteed, will pass legal/audit, fully autonomous (used as praise), fraud, worthless, no originality, culturally backwards,* or any phrase that asserts a legal/compliance conclusion or stereotypes a people or nation.

Never claim a product is compliant, certified, or guaranteed to succeed, and never claim an idea/positioning is globally original just because no counterexample was found.

## Expert-review escalation
Route to qualified experts (and add to `expert_review_flags`) any item touching: personal/sensitive data handling and transfer; model-training on customer data; retention/deletion obligations; regulated sectors (health, finance, children, biometrics, etc.); consent and data-residency; or claims with legal exposure. Name the concern and prepare a note; do not resolve it inside the audit.

## Client-data handling (operating guidance)
Before collecting client materials, the operating team should define: what data is accepted; where it is stored; which model provider receives it; whether it is used for model training; retention period; deletion process; access controls; data-residency/transfer considerations; and incident response. Do not paste confidential client materials into systems that don't meet these requirements.

## Human review is mandatory before client delivery
AI-assisted output must be reviewed by a qualified operator for: factual grounding; product truth; market-specific accuracy; cultural overgeneralization; unsafe or inappropriate recommendations; unsupported legal/compliance conclusions; rewrite quality; and priority alignment. Remove generic or unsupported findings; verify each issue is grounded in evidence; correct target-market assumptions; edit rewrites for product truth and tone.

## Limitations to disclose in every report
State clearly that:
- the audit is primarily **text-driven**; uploaded file contents and live interfaces are **not** automatically extracted/crawled unless their content was supplied;
- the market-fit score is a **heuristic summary**, useful for comparison across iterations, not a certification or statistically validated measure — even with the deterministic rubric, the per-dimension scores are expert judgments;
- default playbooks are **broad regional starting points**, not country-, industry-, or audience-specific research, and are working hypotheses to validate locally;
- the quality of findings depends on the supplied materials and the reviewer's judgment;
- high-similarity / high-severity items and any score near a band boundary warrant human re-check;
- the audit does **not** replace local user testing, legal review, security review, or model evaluation.

## Weak-audit warning signs (avoid these)
Generic localization advice; grammar-only focus; many findings without evidence; treating a region as culturally uniform; "add trust" without specifying where/how; rewriting copy without understanding product truth; using the score as the main conclusion; making legal/compliance claims; ignoring agent behavior and failure states; or delivering a report without an implementation backlog.

## Accessibility is a legal baseline, not only a quality dimension
The `accessibility` dimension is grounded in WCAG 2.1 AA. For EU-facing corridors, conformance is **legally required** under EN 301 549 and the European Accessibility Act (enforceable 28 June 2025, applying to any business serving EU consumers); US corridors fall under ADA / Section 508. The audit **grounds** accessibility findings in the relevant success criteria but does **not** certify compliance — always add an `expert_review_flags` entry for a full conformance audit by a qualified specialist, and use the `eu_eaa` scoring profile for EU consumers. Automated checks catch only ~30-40% of barriers.

## Standards citations are grounding, not compliance opinions
Findings cross-walk to named standards (NIST AI RMF, ISO 42001, MQM/MQM-Chat, WCAG/EN 301 549, Nielsen/Norman) via each issue's `standard_refs`. This signals the basis of a finding; it is **not** a statement that the product conforms to, is certified against, or passes any standard. Keep the controlled vocabulary and route all compliance/legal conclusions to qualified experts.

## Run the critic pass before delivery
For any client-facing audit, run the critic pass in `calibration_and_review.md` before scoring and rendering: verify every finding is evidence-grounded and within its evidence level, severities are honest, standards are cited, rewrites are truthful, and no cultural claim is stated as fact. This second pass is the main guard against single-rater overreach.
