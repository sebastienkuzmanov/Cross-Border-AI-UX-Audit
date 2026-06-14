# Cross-Border AI UX Audit / 跨境 AI 用户体验审计

![version](https://img.shields.io/badge/version-1.0.0-blue) ![license](https://img.shields.io/badge/license-MIT-green) ![dimensions](https://img.shields.io/badge/dimensions-9-orange) ![bilingual](https://img.shields.io/badge/report-EN%20%2B%20%E4%B8%AD%E6%96%87-teal) ![agent skill](https://img.shields.io/badge/agent%20skill-open%20standard-purple)

An **Agent Skill** that audits whether an AI product's user experience is **ready for a specific target market** — not merely translated — and turns the gaps into a prioritized, client-ready **bilingual (English + 中文)** report: a deterministic market-fit score, before/after copy rewrites, an implementation backlog, and expert-review flags.

一个 **Agent Skill**：审计某个 AI 产品的用户体验是否真正**为特定目标市场做好了准备**（而不只是被翻译过），并把差距转化为一份可直接交付客户的**中英双语**报告：确定性的市场契合度评分、改写前后对照、实施待办清单，以及需专家复核的标记。

> **EN —** A product is not ready for a new market merely because its interface has been translated. It is ready when target-market users can **understand it, trust it, control it, recover from its failures, and see why it is relevant to them.**
>
> **中文 —** 产品并不会仅因为界面被翻译就为新市场做好了准备。只有当目标市场的用户能够**理解它、信任它、掌控它、在它出错时能恢复，并且看得出它与自己相关**时，它才算就绪。

---

## What's inside this repo / 仓库内容

```
Cross-Border-AI-UX-Audit/
├── README.md                          ← you are here / 你在这里
├── INDEX.md                           ← short bundle map / 简要导览
├── cross-border-ai-ux-audit.skill     ← the installable skill / 可安装的技能包
├── skill-source/
│   └── cross-border-ai-ux-audit/      ← full source + detailed README / 完整源码与详细说明
├── examples/                          ← what the skill produces / 技能产出示例
│   ├── example_report.html            ← bilingual report (open in a browser, toggle EN/中文)
│   ├── example_report.pdf             ← PDF version / PDF 版
│   ├── example_backlog.csv            ← priority backlog / 优先级待办
│   └── example_backlog_jira.csv       ← Jira import format / Jira 导入格式
└── docs/
    ├── competitive-review.md          ← research: similar skills + upgrade roadmap / 竞品研究与升级路线
    └── how-to-build-a-similar-skill.md ← guide to building a skill like this / 如何构建同类技能
```

> The `.skill` file and the `skill-source/` folder contain the **same skill** — one is packaged for installing, the other is the open folder for reading, editing, and contributing. / `.skill` 与 `skill-source/` 为同一技能——前者用于安装，后者便于阅读、修改与贡献。

## Quick start / 快速开始

**1. Install the skill / 安装技能**
- **Claude.ai:** upload `cross-border-ai-ux-audit.skill` (Settings → Capabilities).
- **Other tools** (Claude Code · Codex CLI · Gemini CLI · Qwen Code · Cursor · 豆包 · MiniMax · …): see [`skill-source/cross-border-ai-ux-audit/INSTALL.md`](skill-source/cross-border-ai-ux-audit/INSTALL.md).

**2. Ask for an audit / 发起审计**, e.g.:
- "Is our AI agent ready to launch in the US self-serve SaaS market?"
- "Why is our localized landing page converting badly in Russia/CIS?"
- "Check our AI app for accessibility and market fit before the EU launch."

**3. See what it produces / 查看产出**
Open [`examples/example_report.html`](examples/example_report.html) in a browser and use the **EN / 中文** toggle.

## What you get / 交付物

- 📊 **A market-fit score (0–100)** from a deterministic weighted rubric, with a readiness band, confidence level, and a per-dimension breakdown across **nine dimensions**.
- 🔍 **Structured findings** — evidence, the problem, why it matters for that market, a recommendation, a **before/after rewrite in the target-market language**, and a **cited standard** (NIST AI RMF, WCAG, MQM, …).
- ✅ **A prioritized backlog** — every fix tagged P1/P2/P3 × work area × estimated impact, with CSV / Jira / Linear exports.
- ⚠️ **Expert-review flags** — privacy, data-transfer, regulated-sector, and accessibility-conformance items routed to qualified experts.
- 📄 **A designed bilingual HTML + PDF report** with an EN / 中文 toggle and standards-citation chips.

## The nine dimensions / 九个评估维度

| # | Dimension / 维度 | Grounded in / 依据 |
|---|---|---|
| 1 | Language naturalness / 语言自然度 | MQM / MQM-Chat |
| 2 | Cultural fit / 文化契合度 | Playbook |
| 3 | Trust & privacy / 信任与隐私 | NIST AI RMF · ISO 42001 |
| 4 | AI expectation-setting / AI 预期设定 | NIST AI RMF |
| 5 | UX clarity / 体验清晰度 | Nielsen · Norman |
| 6 | Conversion / 转化 | Nielsen / playbook |
| 7 | Agent & chatbot behavior / 智能体行为 | NIST AI RMF · OWASP LLM |
| 8 | Accessibility / 无障碍 | WCAG 2.1 AA · EN 301 549 · ADA |
| 9 | Market-entry risk / 市场进入风险 | Playbook |

## Scope & safety — what it is NOT / 适用范围与安全

It is a **decision-support tool**, not a translation review, grammar check, legal/compliance opinion, security/penetration test, model benchmark, or a guarantee of market fit. Compliance-sensitive items (privacy, data transfer, regulated sectors, accessibility conformance) are **flagged for qualified experts**, not answered. The score is a heuristic for comparing iterations — **prioritize the findings over the number**. AI-assisted output **must be reviewed by a qualified operator** before client delivery.

它是**决策支持工具**，并非翻译审校、语法检查、法律/合规意见、安全/渗透测试、模型基准或市场契合度保证。合规敏感事项会被**标记给合格专家**，而非由它下结论。评分仅用于比较迭代——**请以发现项为准，而非分数本身**；AI 辅助产出在交付客户前**必须经合格操作者复核**。

## Full documentation / 完整文档

The complete, bilingual project documentation — architecture, scoring rubric, market playbooks, scripts, and contribution guide — lives in the skill source:

完整的中英双语文档（架构、评分规则、市场 playbook、脚本与贡献指南）见技能源码：

➡️ **[`skill-source/cross-border-ai-ux-audit/README.md`](skill-source/cross-border-ai-ux-audit/README.md)**

## License / 许可

Released under the MIT License — see [`skill-source/cross-border-ai-ux-audit/LICENSE.txt`](skill-source/cross-border-ai-ux-audit/LICENSE.txt).

---

*Built to the Agent Skills open standard (`agentskills.io`): a `SKILL.md` orchestrator plus on-demand `references/`, deterministic `scripts/`, `assets/`, and dev `evals/`. Review and customize the playbooks, weights, and tone vocabulary for your studio before production use. / 遵循 Agent Skills 开放标准构建；投入生产前请按你的团队定制 playbook、权重与措辞。*
