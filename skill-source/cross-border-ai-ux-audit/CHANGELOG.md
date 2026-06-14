# Changelog

All notable changes to the **cross-border-ai-ux-audit** skill are documented here.
This project follows [Semantic Versioning](https://semver.org/).

## [1.0.0] - 2026-06-14

First public release. Audits whether an AI product's UX is ready for a specific **market corridor**, not merely translated, and produces a prioritized, bilingual (EN + 中文) market-readiness report.

### Methodology
- **Nine audit dimensions**: language naturalness, cultural fit, trust & privacy, AI expectation-setting, UX clarity, conversion, agent/chatbot behavior, **accessibility**, and market-entry risk.
- **Framework cross-walk** (`references/framework_crosswalk.md`): every dimension is grounded in named external standards — Nielsen heuristics & Norman principles (UX), NIST AI RMF & ISO/IEC 42001 (trust/AI/agent), MQM & MQM-Chat (language), WCAG 2.1 AA / EN 301 549 / ADA (accessibility), with OWASP LLM Top 10 as a boundary flag. Findings cite standards via `standard_refs`.
- **Deterministic market-fit score** (`scripts/score_audit.py`): weighted rubric over the nine dimensions with weight renormalization, unresolved-Critical caps (59 / 39), evidence-completeness → confidence, and **corridor weight profiles** (`default`, `eu_eaa`).
- **MQM language sub-score** (`scripts/mqm_language_score.py`): error-density score from a labeled MQM/MQM-Chat error list.
- **Calibration & critic pass** (`references/calibration_and_review.md`): per-dimension anchors, calibration examples, an MQM-style inter-rater method, and a mandatory pre-scoring critic pass.

### Evidence
- **Live evidence capture** (`scripts/capture_evidence.py`): full-page screenshots + extracted text + a manifest via Playwright/Chromium, with a documented text fallback; findings reference captured artifacts via `evidence_ref`.
- Three evidence levels with explicit "don't exceed the evidence" guidance.

### Playbooks
- Six target-market playbooks: Russian/CIS, Balkan/EU, English-speaking global, China inbound, **LATAM**, **MENA/Gulf**.
- Accessibility-by-corridor, governance, provenance/versioning/segmentation, and an optional local category-norm / competitor-reference step.

### Reporting & exports
- Designed, bilingual, self-contained **HTML** report with an EN / 中文 toggle and standards-citation chips; **PDF** export (`scripts/html_to_pdf.py`) with HTML fallback; **Markdown** report.
- Backlog **CSV** export, plus **Jira / Linear** export (`scripts/export_issue_tracker.py`).
- **Audit-version diff** (`scripts/compare_audits.py`) for the re-audit loop.

### Compatibility
- **Cross-runtime by the Agent Skills open standard**: drop-in on Claude Code, Codex CLI, Gemini CLI, Qwen Code, Cursor, Copilot, and ~30 other agents (`INSTALL.md`).
- Adapter files for non-Claude hosts: `AGENTS.md` (Codex / Qwen Code), `GEMINI.md`, and an optional `gemini-extension.json`.
- `scripts/bundle_for_system_prompt.py` enables use with models lacking a native skills CLI (Doubao, MiniMax, GLM, Kimi…) via system-prompt mode or an AgentSkills→MCP bridge.

### Quality & safety
- Expert-review escalation for legal/privacy/security/regulated and **accessibility conformance** items; standards citations are grounding, not compliance opinions.
- Controlled, non-accusatory tone vocabulary; mandatory human review before client delivery.
- **Evals** (`evals/`): scorer unit tests, a golden regression check, and triggering tests (excluded from the packaged skill).
