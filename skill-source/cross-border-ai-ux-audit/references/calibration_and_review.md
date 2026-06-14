# Calibration & Review (Critic Pass)

This reference raises the reliability of the audit's judgments and scores. It covers (1) a mandatory critic pass before the report renders, (2) per-dimension scoring anchors with calibration examples, and (3) an inter-rater method borrowed from MQM. Single-rater LLM judgment is the default failure mode this addresses.

## 1. The critic pass (run before scoring and rendering)

After drafting findings and per-dimension scores, do a **second pass** over the audit object and correct it before computing the score or rendering. Check each finding against this checklist:

- **Evidence-grounded?** Does the finding point to a specific observed element (`original_text` or a captured `evidence_ref`)? If not, delete it or mark the dimension `unknown`.
- **Within the evidence level?** No Level-3 behavior claims from Level-1 copy. Downgrade overreaching claims to "flag to verify with live testing."
- **Severity honest?** Re-check against the severity table; don't inflate. A finding in an out-of-scope flow may still be lower priority.
- **Standard cited where applicable?** Add `standard_refs` per `framework_crosswalk.md`; add an `expert_review_flags` entry for any compliance/legal item.
- **Rewrite truthful?** Does `rewritten_version` stay true to what the product actually does, in the target-market language?
- **Non-stereotyping?** Is any cultural claim framed as a playbook hypothesis, not a fact about a people?
- **Score sanity:** do the per-dimension scores match the findings (a dimension with a Critical issue should not score 80)? Set `unresolved_critical_count` correctly so the cap fires.

Then run `scripts/score_audit.py` to compute `overall` / `band` / `confidence`. Note the critic pass in the report's process if asked, and never skip it for client-facing audits.

Optionally, run the critic pass as a fresh read ("review these findings for evidence-grounding and overreach, list what to cut or downgrade") to approximate a second annotator.

## 2. Per-dimension scoring anchors (0-100)

Use these anchors for every dimension score; they make scores comparable across audits and raters.

- **90-100** — native-quality on this dimension for the corridor; only targeted polish remains.
- **75-89** — solid, a few important fixes.
- **60-74** — usable but with clear gaps a local buyer would notice.
- **40-59** — significant rework needed before launch.
- **0-39** — fundamental problems on this dimension.
- **null / unknown** — insufficient evidence to score; exclude and note in limitations.

### Calibration examples (illustrative anchors)
- `trust_and_privacy` = 45: data is requested at upload with no panel explaining use/storage/training/retention; company identity present but no DPA or provider disclosure. (Major gap at the key decision point → low-middle.)
- `ai_expectation_setting` = 40: "handles the entire workflow" with no scope, no review queue, no fallback. (Absolute autonomy claim, no control surface → low.)
- `language_naturalness` = 72: mostly natural, but buzzword-dense hero copy and one awkward calque; MQM error-density moderate. (Good base, targeted rewrites.)
- `accessibility` = 52: visible contrast failures and unlabeled icon controls on a key page; rest untested. (Known AA failures on a primary surface → below bar.)

Maintain a small set of **expert-reviewed gold audits** (see `evals/golden/`) and re-check new scores against them; when you change the weights or anchors, record the change and re-verify the gold set.

## 3. Inter-rater method (from MQM)

MQM scores each segment with **2-3 annotators** and averages. Emulate this when stakes are high:
- Score each dimension twice (the critic pass can serve as the second read), and if the two scores differ by more than ~10 points, reconcile by re-examining the evidence and writing why.
- Record disagreement as part of `confidence` — wide spread or thin evidence → lower confidence, regardless of the number.
- For the language dimension specifically, use `scripts/mqm_language_score.py` so the number derives from a labeled error list rather than a gestalt impression.

## 4. Evidence-completeness vs. confidence

`evidence_completeness` (0-100) reflects how much of the corridor's relevant material was actually reviewed. It sets `confidence` (low < 50, medium 50-79, high >= 80) and **never silently moves the score**. When evidence is thin, prefer reporting the findings over the number, and say so in the executive summary.
