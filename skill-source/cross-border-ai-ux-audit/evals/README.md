# Evals

Lightweight checks for the Cross-Border AI UX Audit skill. These live in the repo for development and CI; they are **excluded from the packaged `.skill`** (the packager drops the root `evals/` directory), so they don't ship to end users or consume skill context.

## What's here
- `test_score_audit.py` — unit tests for the deterministic scorer: weight sums, weighted average, unresolved-Critical caps (59 / 39), null-dimension renormalization, band boundaries, evidence-completeness → confidence, score clamping, and the corridor weight profiles.
- `check_golden.py` — re-scores `golden/gold_audit.json` and confirms the scorer reproduces `golden/expectations.json`, plus schema-shape checks (nine dimensions, issues, expert-review flags) and that every issue cites a standard.
- `golden/` — a gold, expert-shaped audit fixture and its expected outputs. Update it deliberately and re-verify when you change weights, anchors, or the schema.
- `triggering_tests.md` — prompts the skill should / should not fire on, with what to verify when it triggers.

## Run
```bash
# from the repo root
python evals/test_score_audit.py     # scorer unit tests
python evals/check_golden.py         # golden regression check
# or, if you use pytest:
pytest evals/test_score_audit.py
```

## When you change the skill
- Changing **weights, profiles, or calibration anchors** → re-run `check_golden.py`; update `golden/expectations.json` only with a recorded reason (note it in `CHANGELOG.md`).
- Changing the **schema** → update `golden/gold_audit.json`, the renderers, and `references/finding_and_report_schema.md` together.
- Changing the **description** → re-walk `triggering_tests.md` to confirm triggering didn't regress.
