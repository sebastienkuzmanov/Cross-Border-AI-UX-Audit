---
name: cross-border-ai-ux-audit
description: Audit whether an AI product's user experience is ready for a specific target market (a market corridor), not just translated. Scores nine dimensions (language naturalness, cultural fit, trust/privacy, AI expectation-setting, UX clarity, conversion, agent/chatbot behavior, accessibility, market-entry risk) against an editable market playbook, then produces a prioritized bilingual (English + Chinese) report with a deterministic market-fit score, before/after copy rewrites, an implementation backlog, and expert-review flags. Use whenever someone wants to know if an AI product is ready for a new country or language market; asks for a localization, transcreation, market-fit, or market-readiness review; wants to audit a chatbot, agent, SaaS, app, or voice/multimodal AI product for a target market; mentions cross-border or go-to-market UX; asks why localized conversion is weak; or wants product copy made trust-ready for a market. Trigger even when phrased as a localization review or make this ready for a market.

license: See LICENSE.txt
metadata:
  version: 1.0.0
---

# Cross-Border AI UX Audit

## Goal

Evaluate the **conceptual market-readiness** of an AI product's experience for a specific market corridor, and convert the gaps into concrete rewrites, UX changes, trust improvements, agent-behavior changes, expert-review flags, and an ordered implementation backlog.

The guiding question is always:

> *Can people in the target market understand, trust, control, and adopt this AI product as it exists today?*

A product is **not** ready for a new market merely because its interface has been translated. It is ready when target-market users can understand it, trust it, control it, recover from its failures, and see why it is relevant to them.

This skill is a **decision-support and implementation-planning tool**. It does not produce legal, compliance, security, or regulatory opinions — it flags those for qualified local experts.

## Use And Avoid

Use this skill for:
- Market-readiness / market-fit reviews of AI products entering or adapting between countries, languages, and business cultures.
- Localization or transcreation reviews that need **product-level** guidance, not only translated strings.
- Auditing a chatbot, agent, AI SaaS, AI education app, AI productivity tool, voice AI, or multimodal AI product for a target market.
- Diagnosing weak localized conversion, abandoned onboarding, or low trust in a target market.
- Trust / privacy / AI-boundary readiness checks before a launch or enterprise pilot.
- Before/after rewrites of product copy (landing pages, onboarding, CTAs, trust panels, agent prompts) for a specific market.

Do **not** use this skill for:
- Literal translation review, grammar-only proofreading, or copyediting in isolation.
- Legal opinions, regulatory certification, or patent/compliance judgments.
- Security penetration testing or vulnerability assessment.
- Model benchmarking or technical accuracy/quality evaluation of the model itself.
- A substitute for local user research, or a guarantee of compliance or product-market fit.

## Core Workflow

1. **Define the decision.** Establish the business decision the audit must support (pilot-ready? what to fix before launch? why is conversion weak?). Without a defined decision the audit becomes an unprioritized list of observations.
2. **Define the market corridor.** Record source market, target market, target audience, product type, and business goal. Select the matching target-market playbook.
3. **Run intake.** Ask the compact intake question set before doing anything else. Do not start auditing until the user answers or explicitly says to proceed with assumptions (which are then logged).
4. **Collect and inventory evidence.** Gather the highest-value product materials. Record what was reviewed and what was *not* available, and the evidence level (1 copy / 2 flow / 3 behavior). When URLs are available, use `scripts/capture_evidence.py` to capture screenshots + extracted text so findings cite real Level-2 evidence (fall back to text if tooling is unavailable, and say so).
5. **Evaluate across the nine dimensions** (now including **accessibility**) against general AI-UX principles, the target-market playbook, the business goal, and the target audience. Ground each finding in a named standard — see `references/framework_crosswalk.md`.
6. **Write structured findings** using the finding schema (evidence → problem → why it matters → recommendation → rewrite → target-market note), each with a category, severity, confidence, and `standard_refs` citing the relevant standard(s).
7. **Run the critic pass** (`references/calibration_and_review.md`): re-check every finding for evidence-grounding, evidence-level honesty, correct severity, cited standards, truthful rewrites, and non-stereotyping — correct the audit before scoring.
8. **Compute the market-fit score** with the deterministic rubric (`scripts/score_audit.py`, with the corridor weight profile) — never invent the number. For the language dimension, anchor it with `scripts/mqm_language_score.py`.
9. **Build the prioritized backlog** (P1/P2/P3 × work area × estimated impact).
10. **Flag expert-review items** (legal, compliance, privacy, security, regulated/sensitive sectors, and accessibility conformance).
11. **Render the client-ready report** as bilingual HTML, convert to PDF when tooling exists, and export the backlog (CSV, plus Jira/Linear via `scripts/export_issue_tracker.py`). Provide a short chat summary with file paths.
12. **State limitations and recommend the re-audit loop** (use `scripts/compare_audits.py` to diff against a prior version).

## Internal Modules

Treat these as internal modules of one skill, not separate skills:

- Decision & Corridor Definition Module
- Intake Module
- Evidence Inventory & Live-Capture Module
- Dimension Evaluation Module (×9, including accessibility)
- Playbook Application Module
- Framework Cross-Walk Module (cite named standards)
- Finding Authoring Module
- Calibration / Critic-Pass Module
- Deterministic Scoring Module
- Prioritization / Backlog Module
- Expert-Review Escalation Module
- Bilingual Report Generation Module

## Reference Loading

Load only the references needed for the current step:

- `references/intake_and_corridor.md` — the decision framing, market-corridor definition, the compact intake question set, engagement moments, and evidence-collection guidance. **Read this first for any new audit.**
- `references/audit_dimensions.md` — the nine audit dimensions (including accessibility): what each evaluates, its typical problem, and its typical recommendation. Read when evaluating materials and writing findings.
- `references/framework_crosswalk.md` — maps each dimension to named external standards (Nielsen/Norman, NIST AI RMF, ISO 42001, MQM/MQM-Chat, WCAG/EN 301 549, OWASP LLM as a boundary flag). Read when writing findings, and add `standard_refs` to each.
- `references/market_playbooks.md` — the editable target-market playbooks (Russian/CIS, Balkan/EU, English-speaking global, China inbound, LATAM, MENA/Gulf), accessibility-by-corridor, governance, provenance/versioning, and the optional competitor-reference step. Read after the corridor is set.
- `references/evidence_and_inputs.md` — supported material types, the three evidence levels, and the live evidence-capture mode. Read during evidence inventory.
- `references/scoring_severity_priority.md` — severity/priority definitions, the deterministic weighted rubric (nine weights, corridor profiles, score bands, Critical cap, evidence-completeness handling), and the MQM language sub-score. Read when scoring and prioritizing.
- `references/calibration_and_review.md` — the mandatory critic pass, per-dimension scoring anchors with calibration examples, and the MQM-style inter-rater method. **Read before scoring any client-facing audit.**
- `references/finding_and_report_schema.md` — the canonical audit JSON schema (nine dimensions, `standard_refs`, `evidence_ref`, `weight_profile`), the finding/backlog fields, the deliverables list, and the report section order. Read when authoring findings and assembling the report data.
- `references/report_design_and_output.md` — the bilingual output contract, visual design system, standards-citation chips, and export formats. Read when rendering the report.
- `references/limitations_and_safety.md` — what the audit must never claim, the controlled tone vocabulary, expert-review escalation (including accessibility conformance), the standards-are-grounding-not-compliance rule, and limitations to disclose. **Read before delivering any report.**

Use scripts when helpful (see each script's `--help`):

- `scripts/score_audit.py` — compute the deterministic weighted market-fit score, band, and dimension breakdown from per-dimension scores, with the unresolved-Critical cap, evidence-completeness handling, and a selectable corridor weight profile (`--profile`, `--list-profiles`).
- `scripts/mqm_language_score.py` — compute an MQM-style error-density sub-score for the language dimension from a labeled error list (MQM / MQM-Chat typology + severity).
- `scripts/capture_evidence.py` — capture live page evidence (full-page screenshots + extracted text + a manifest) via Playwright/Chromium, with a documented fallback to text evidence.
- `scripts/export_backlog_csv.py` — export the priority backlog to CSV (priority, area, impact, task, linked issue).
- `scripts/export_issue_tracker.py` — export the backlog to Jira or Linear CSV (or JSON), with priority mapping.
- `scripts/compare_audits.py` — diff two audit JSON versions (overall + per-dimension deltas, resolved/new/changed findings) for the re-audit loop.
- `scripts/render_markdown_report.py` — render the audit JSON into a bilingual Markdown report.
- `scripts/render_html_report.py` — render the audit JSON into a designed bilingual static HTML report with an EN / 中文 language toggle and standards-citation chips.
- `scripts/html_to_pdf.py` — convert the HTML report to PDF via Playwright/Chromium when available, with a documented fallback to delivering the HTML.
- `scripts/bundle_for_system_prompt.py` — concatenate SKILL.md + references into one pasteable system prompt, for using the skill with models that have no native skills CLI (Doubao, MiniMax, GLM, Kimi, etc.). See `INSTALL.md`.

Use `assets/html_report_template.html` as the visual reference when adjusting layout manually, and `assets/sample_audit.json` as a schema-complete example input.

## Execution Rules

**Ask intake first.** When invoked with only a rough description, ask the compact question set in `references/intake_and_corridor.md`. Do not audit until the user answers or explicitly says "proceed with assumptions." If proceeding on assumptions, write every assumption into the report's evidence/limitations section.

**Anchor to a market corridor, not a language.** The unit of analysis connects source market → target market → audience → product category → business goal → the specific materials reviewed. "Russian" or "Chinese" alone is not a corridor. The same product entering a China-origin → Russia/CIS B2B corridor needs different positioning, proof, and trust explanations than a China-origin → English-speaking self-serve SaaS corridor.

**Apply the target-market playbook, never one generic idea of "good UX."** Playbooks are working hypotheses, not cultural absolutes — never stereotype a diverse region as uniform, and say when a rule is an assumption that needs local validation.

**Evaluate the whole experience around the AI, not just model output.** Cover discovery, trust decision, capability understanding, data provision, result review, error correction, escalation, and the buy/continue decision.

**Write evidence-grounded findings only.** Every important finding must point to an observed element (pasted copy, a described flow, a prompt/response sample, or a captured `evidence_ref`). If a dimension can't be assessed from the supplied evidence, mark it **unknown** rather than inventing detail. Do not exceed the evidence level (don't draw Level-3 behavior conclusions from Level-1 copy alone).

**Ground findings in named standards.** Per `references/framework_crosswalk.md`, add `standard_refs` to each finding (Nielsen/Norman, NIST AI RMF, ISO 42001, MQM/MQM-Chat, WCAG/EN 301 549). Citing a standard means the finding is grounded in it — never that the product is certified or compliant. Add an expert-review flag for any compliance/legal item (accessibility, privacy, regulated sectors).

**Run the critic pass before scoring.** Per `references/calibration_and_review.md`, do a second pass over the audit (evidence-grounding, evidence-level honesty, severity, cited standards, truthful rewrites, non-stereotyping, score sanity) and correct it before computing the number.

**Score by the deterministic rubric, not by feel.** Produce per-dimension scores (0–100) with brief justifications anchored to the calibration examples, then run `scripts/score_audit.py` (with the corridor weight profile) to compute the overall score, band, and Critical cap. Never hand-write the final number. Put the most important decisions and actions first; do not bury the client in low-value observations.

**Separate severity from priority.** Severity = the consequence of the issue. Priority = when to act, given the planned launch scope. A High-severity issue in an out-of-scope flow may be P2; a Medium-severity issue on the main conversion path may be P1.

**Escalate, don't opine.** Flag privacy, data-transfer, regulated-sector, claims, and market-entry-obligation concerns for qualified local legal/compliance/privacy/security/domain experts. The audit names the concern and prepares a note; it does not give the legal opinion.

**Keep the tone analytical and non-accusatory.** Use the controlled vocabulary in `references/limitations_and_safety.md` (conceptual risk, market-fit gap, limited differentiation, unclear AI boundary) and avoid loaded terms.

## Output Style

Use terms such as: *market-readiness, market-fit gap, conceptual risk, trust threshold, AI boundary, scoped capability, control surface, evidence-grounded, limited local proof, requires expert review.*

Avoid terms such as: *non-compliant, illegal, certified, guaranteed, will pass legal review, fully autonomous (as praise), worthless, culturally backwards.*

Always distinguish facts, evidence-backed findings, inferences, and uncertainties. If evidence coverage is thin, say so. Never claim a product is compliant, certified, or guaranteed to succeed.

## Final Report

Deliverables (bilingual English + 中文 by default):
- a designed static **HTML** report file with an EN / 中文 toggle and standards-citation chips;
- a **PDF** version of that HTML when browser/PDF tooling is available;
- a **CSV** export of the priority backlog (and **Jira/Linear** export via `scripts/export_issue_tracker.py` when requested);
- a short **chat summary** with overall readiness, the top 3 risks, the score (with the weight profile used), and paths to all files.

Report title: **Cross-Border AI UX Audit** (跨境 AI 用户体验审计). Required sections, in order:
1. Executive summary
2. Market corridor & evidence reviewed
3. Market-fit score (with how it should and should not be read)
4. Top risks
5. Findings by dimension (structured issue register)
6. Before / after rewrites
7. Priority backlog
8. Expert-review flags
9. Recommended next steps & re-audit loop
10. Limitations

Keep the visual style precise, editorial, and evidence-heavy — a polished market-readiness report, more refined than a plain academic PDF. Keep the tone practical and non-accusatory throughout.
