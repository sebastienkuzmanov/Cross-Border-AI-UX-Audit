# AGENTS.md

This directory is an **Agent Skill**: **Cross-Border AI UX Audit** (跨境 AI 用户体验审计).

If you are an agent working in this directory (e.g. Codex CLI, Qwen Code, or any agent that reads AGENTS.md), treat **`SKILL.md`** as the authoritative instructions and follow it. Load files under `references/` on demand, and use the deterministic helpers in `scripts/` (plain Python 3) rather than computing scores or rendering reports by hand.

**What this skill does:** audits whether an AI product's UX is ready for a specific target market (a "market corridor"), not merely translated. It scores nine standards-grounded dimensions, produces a deterministic market-fit score, before/after rewrites, a prioritized backlog, and expert-review flags, and renders a bilingual (English + 中文) report.

**Start here:** read `SKILL.md` → run intake → follow the Core Workflow. See `INSTALL.md` for cross-runtime setup. Do not give legal/compliance/security verdicts; escalate those to expert review.
