# Finding & Report Schema

This reference defines the **canonical audit JSON object** that every script consumes, the structured finding fields, the backlog fields, the deliverables, and the report section order. The pattern is: **the model produces one well-formed JSON object; the scripts score and render it.** Keep the model's job to judgment and authoring; let scripts handle math, CSV, and presentation.

A schema-complete example lives in `assets/sample_audit.json`.

## Structured finding fields (Step 5)
Each finding separates evidence, diagnosis, consequence, and action:
- **category** — one of the eight dimension keys.
- **severity** — Critical / High / Medium / Low.
- **original_text** — the evidence (pasted text or observed behavior), kept as-is.
- **problem** — what is wrong or risky.
- **why_it_matters** — the target-market and business consequence.
- **recommendation** — the action to take.
- **rewritten_version** — an implementable example where relevant, in the **target market's language** by default.
- **target_market_note** — the market-specific rationale (often tied to the playbook).
- plus **id**, **evidence_grounding** (which material it came from), and **confidence** (high/medium/low).

## Backlog fields (Step 6)
- **task** — the implementation task.
- **priority** — P1 / P2 / P3.
- **area** — UX / Copy / Localization / Trust / Agent Design / Compliance.
- **estimated_impact** — High / Medium / Low.
- **linked_issue_id** — the finding it resolves.

## Canonical audit JSON schema

Bilingual text fields use `{ "en": "...", "zh": "..." }`. The `original_text` and `rewritten_version` are single strings (evidence is kept verbatim; rewrites are in the target-market language, with the language recorded).

```json
{
  "meta": {
    "client": "",
    "product": "",
    "product_type": "AI agent",
    "source_market": "China",
    "target_market": "English-speaking global",
    "target_audience": "",
    "business_goal": "",
    "launch_decision": "",
    "playbook": "english_global",
    "weight_profile": "default",
    "evidence_reviewed": ["landing page copy", "onboarding flow"],
    "evidence_not_available": ["live product", "analytics"],
    "evidence_level": "1",
    "evidence_capture": { "manifest": "evidence/manifest.json", "pages_captured": 0 },
    "assumptions": [],
    "report_languages": ["en", "zh"],
    "audit_version": 1,
    "audit_date": "2026-06-14"
  },
  "executive_summary": { "en": "", "zh": "" },
  "market_fit_score": {
    "overall": 0,
    "band": "",
    "dimension_scores": {
      "language_naturalness": 0,
      "cultural_fit": 0,
      "trust_and_privacy": 0,
      "ai_expectation_setting": 0,
      "ux_clarity": 0,
      "accessibility": 0,
      "conversion": 0,
      "agent_chatbot_behavior": 0,
      "market_entry_risk": 0
    },
    "evidence_completeness": 0,
    "unresolved_critical_count": 0,
    "confidence": "medium",
    "score_explanation": { "en": "", "zh": "" }
  },
  "top_risks": [
    { "en": "", "zh": "" }
  ],
  "issues": [
    {
      "id": "ISSUE-1",
      "category": "ai_expectation_setting",
      "severity": "High",
      "original_text": "",
      "problem": { "en": "", "zh": "" },
      "why_it_matters": { "en": "", "zh": "" },
      "recommendation": { "en": "", "zh": "" },
      "rewritten_version": "",
      "rewritten_version_language": "en",
      "target_market_note": { "en": "", "zh": "" },
      "standard_refs": ["NIST AI RMF: Explainable & Interpretable"],
      "evidence_grounding": "landing page copy",
      "evidence_ref": "",
      "confidence": "high"
    }
  ],
  "backlog": [
    {
      "task": { "en": "", "zh": "" },
      "priority": "P1",
      "area": "Agent Design",
      "estimated_impact": "High",
      "linked_issue_id": "ISSUE-1"
    }
  ],
  "expert_review_flags": [
    { "area": "Privacy / data transfer", "reason": { "en": "", "zh": "" } }
  ],
  "next_steps": [
    { "en": "", "zh": "" }
  ],
  "limitations": { "en": "", "zh": "" }
}
```

Notes:
- `dimension_scores` may set a dimension to `null` when there is insufficient evidence; the scorer excludes nulls and renormalizes weights.
- `overall`, `band`, and `confidence` should be (re)computed by `scripts/score_audit.py` from `dimension_scores`, `unresolved_critical_count`, and `evidence_completeness` — do not hand-write `overall`.
- Keep `original_text` verbatim; never paraphrase the evidence inside the evidence field.

## Deliverables (Section 11)
A complete audit produces: executive summary; market-fit score (with interpretation caveats); top risks; a structured issue register; before/after examples; a priority backlog; recommended next steps; and clearly stated limitations.

## Report section order
1. Executive summary
2. Market corridor & evidence reviewed
3. Market-fit score (how to read / not read it)
4. Top risks
5. Findings by dimension (structured issue register)
6. Before / after rewrites
7. Priority backlog
8. Expert-review flags
9. Recommended next steps & re-audit loop
10. Limitations

## Field notes (current schema)
- `dimension_scores` now spans **nine** dimensions (adds `accessibility`); any may be `null` (excluded from scoring, weights renormalize).
- `meta.weight_profile` selects the scoring weight profile (`default` or `eu_eaa`); the scorer also accepts `--profile`. The chosen profile is echoed in `market_fit_score.weight_profile`.
- Each issue may carry `standard_refs` (a list of standard citations per `framework_crosswalk.md`) and `evidence_ref` (a captured-evidence artifact name, e.g. `"pricing.png"`).
- `meta.evidence_capture` points at the `manifest.json` produced by `scripts/capture_evidence.py` and records how many pages were captured live.
- Re-audit loop: keep prior audit JSONs and diff them with `scripts/compare_audits.py` to track score and finding deltas across versions (`meta.audit_version`).
- Issue-tracker export: `scripts/export_issue_tracker.py` turns `backlog` into Jira or Linear CSV (priority mapped P1→Highest/Urgent, etc.).
