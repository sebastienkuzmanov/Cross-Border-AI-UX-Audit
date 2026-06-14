# Contributing

Thanks for helping improve the **cross-border-ai-ux-audit** skill.

## Ground rules
- Keep the skill a **decision-support tool**, not a legal/compliance/security authority. Anything that would assert compliance must be routed to expert review, not answered.
- **Don't stereotype.** Playbook rules are working hypotheses; label unvalidated ones and frame market guidance as context, never as facts about a people.
- Findings must stay **evidence-grounded** and cite a **named standard** (`references/framework_crosswalk.md`) where one applies.

## Repo layout
- `SKILL.md` — orchestrator (instructions in English; the skill outputs bilingual EN + 中文).
- `references/` — detail loaded on demand. Keep each focused.
- `scripts/` — deterministic tools. Keep them dependency-light; Playwright is optional and must fail gracefully.
- `assets/` — schema-complete `sample_audit.json` and the rendered template.
- `evals/` — tests and fixtures (excluded from the packaged `.skill`).

## Before opening a PR
1. Run the checks:
   ```bash
   python evals/test_score_audit.py
   python evals/check_golden.py
   ```
2. If you changed the **schema**, update `assets/sample_audit.json`, both renderers, `references/finding_and_report_schema.md`, and `evals/golden/`.
3. If you changed **weights, profiles, or calibration anchors**, re-run `check_golden.py`, update `evals/golden/expectations.json` with a recorded reason, and note it in `CHANGELOG.md`.
4. If you changed the **`description`**, validate it stays < 1024 characters with no angle brackets, and re-walk `evals/triggering_tests.md`.
5. Validate and package with the official skill-creator tools (`quick_validate.py`, `package_skill.py`).

## Adding a market playbook / corridor
Add a section to `references/market_playbooks.md` with `emphasize` / `watch for`, mark it a working hypothesis, include provenance and a version stamp, and add a corridor scoring profile in `scripts/score_audit.py` only after calibration.

## Style
Prose over bullets in references where it reads better; keep the controlled, non-accusatory vocabulary from `references/limitations_and_safety.md`.
