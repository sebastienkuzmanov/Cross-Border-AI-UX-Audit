## What this changes
Brief summary.

## Type
- [ ] New/updated dimension or playbook
- [ ] Scoring / rubric / profile
- [ ] Script (renderer, export, capture, compare)
- [ ] Reference docs
- [ ] Evals / fixtures
- [ ] Other

## Checklist
- [ ] `python evals/test_score_audit.py` passes
- [ ] `python evals/check_golden.py` passes
- [ ] Schema changes propagated to sample, renderers, schema reference, and golden fixture
- [ ] Weight/anchor changes recorded in `CHANGELOG.md` (and `golden/expectations.json` updated)
- [ ] `description` still < 1024 chars, no angle brackets; triggering re-checked if changed
- [ ] `quick_validate.py` reports the skill valid
- [ ] No stereotyping; compliance items escalate to expert review; standards cited where applicable
