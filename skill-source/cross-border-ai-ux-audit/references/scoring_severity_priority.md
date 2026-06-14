# Scoring, Severity & Priority

This reference defines severity, priority, and the **deterministic market-fit scoring rubric** implemented by `scripts/score_audit.py`. The score is never hand-written by the model: the model produces per-dimension scores (0–100) with brief justifications, and the script computes the overall number, band, and caps.

---

## Severity (the consequence of an issue)

| Severity | Meaning | Typical examples |
| --- | --- | --- |
| **Critical** | Likely to block launch, create serious trust/safety risk, or require immediate expert review | Missing sensitive-data disclosure at upload; dangerous agent behavior; severe misleading claim |
| **High** | Materially harms trust, comprehension, adoption, or conversion | Overstated autonomy; unclear data use; unnatural core positioning |
| **Medium** | Creates friction, weakens credibility, or reduces conversion but does not usually block use | Vague CTA; weak local proof; unclear secondary flow |
| **Low** | Improvement opportunity with limited immediate impact | Minor wording inconsistency; unsupported broad claim in a low-visibility area |

## Priority (when to act, given the planned launch scope)

| Priority | Meaning |
| --- | --- |
| **P1** | Resolve before launch, pilot, or major client review |
| **P2** | Resolve in the next product or localization cycle |
| **P3** | Improve when higher-impact risks are controlled |

**Severity ≠ priority.** A High-severity issue may be lower priority if its flow isn't part of the planned launch; a Medium-severity issue may become P1 if it sits on the main conversion path. Decide priority against the corridor's defined decision.

---

## Deterministic market-fit score (0–100)

The score is a **summary signal** for comparing audit iterations of the same product/corridor and for prioritization conversation. It is **not** a certification, a legal/compliance rating, a statistically validated measure, or a substitute for the issue-level findings. Always present it with that framing.

### Inputs
- `dimension_scores`: integer 0–100 for each of the eight dimensions, where higher = more market-ready on that dimension. Use the per-dimension anchors below. Unknown dimensions (insufficient evidence) are omitted/`null` and excluded from the weighted average (weights renormalize over scored dimensions).
- `unresolved_critical_count`: number of open Critical issues.
- `evidence_completeness`: 0–100 estimate of how complete the supplied evidence is for the corridor (see anchors).

### Dimension weights (default profile; calibratable hypothesis, not a validated constant)
```
trust_and_privacy        0.16
ai_expectation_setting   0.15
agent_chatbot_behavior   0.12
ux_clarity               0.11
conversion               0.11
cultural_fit             0.10
accessibility            0.09
language_naturalness     0.09
market_entry_risk        0.07   (sum = 1.00)
```
Rationale: AI raises the trust threshold and cross-border raises it further, so `trust_and_privacy` and `ai_expectation_setting` carry the most weight; translation correctness alone (`language_naturalness`) is necessary but not sufficient, so it is weighted modestly; `accessibility` is meaningful and legally weighty but corridor-dependent (boost it via a profile below). These weights are a documented starting point — recalibrate against expert-reviewed examples (`calibration_and_review.md`) and record the version used.

### Weight profiles (corridor-aware)
`scripts/score_audit.py` supports named weight profiles. Select with `--profile NAME`, or set `meta.weight_profile` in the audit. Available:
- **default** — the weights above; use for most corridors.
- **eu_eaa** — for any corridor that serves EU consumers. Raises `accessibility` to 0.14 and `market_entry_risk` to 0.09 (European Accessibility Act, enforceable 2025-06-28; EN 301 549 / WCAG 2.1 AA is legally required), reducing other weights proportionally so the sum stays 1.00.

Run `python scripts/score_audit.py --list-profiles` to print them. The profile used is recorded in the score block (`weight_profile`) and shown in the report. Add new corridor/industry profiles here and in the script as you calibrate them.

### Computation (implemented in the script)
1. **Weighted base** = sum(weightᵢ × scoreᵢ) over scored dimensions, with weights renormalized so they sum to 1 across the dimensions that have scores.
2. **Critical cap** (a high-severity safety/trust gate):
   - if `unresolved_critical_count` >= 1 → cap the overall at **59** (cannot read as "ready");
   - if `unresolved_critical_count` >= 2 → cap the overall at **39** (fundamental problems).
3. **Evidence-completeness handling**: do **not** silently inflate or deflate the number. Report `evidence_completeness` alongside the score and lower stated confidence when it is low (< 50 → confidence "low"; 50–79 → "medium"; >= 80 → "high"). When evidence is thin, prefer reporting the findings over the number.
4. **Band** the (possibly capped) overall:

| Score | Band / interpretation |
| --- | --- |
| 90–100 | Strong readiness; targeted improvements remain |
| 75–89 | Generally ready with important fixes |
| 60–74 | Usable base, but material market-fit gaps remain |
| 40–59 | Significant adaptation required before launch |
| 0–39 | Fundamental trust, clarity, or market-fit problems |

### Per-dimension scoring anchors (use as a guide for each 0–100 score)
- **90–100**: native-quality on this dimension for the corridor; only targeted polish remains.
- **75–89**: solid, with a few important fixes.
- **60–74**: usable but with clear gaps a local buyer would notice.
- **40–59**: significant rework needed before launch.
- **0–39**: fundamental problems on this dimension.
- **unknown**: insufficient evidence to score — omit and note in limitations.

### Future scoring enhancements (for a production rubric)
Define evidence-based anchors per dimension; calibrate against expert-reviewed examples; show dimension-level scores; cap on unresolved Criticals (done); account for evidence completeness (reported); and record changes between audit versions for trend comparison.

### Language dimension: MQM-derived sub-score
The `language_naturalness` score can be derived (not just guessed) with `scripts/mqm_language_score.py`, which turns a labeled MQM/MQM-Chat error list into an error-density score using MQM severity penalties (minor=1, major=5, critical=10) normalized per 100 words. See `framework_crosswalk.md` for the typology. Use the script's number to anchor the dimension score and cite the MQM error types in the finding's `standard_refs`.

### Calibration and the critic pass
Per-dimension scores are expert judgments even though the overall number is deterministic. Before scoring, run the **critic pass** and check scores against the **calibration examples** and gold audits in `calibration_and_review.md`. When you change weights, profiles, or anchors, re-verify the gold set and record the change in `CHANGELOG.md`.
