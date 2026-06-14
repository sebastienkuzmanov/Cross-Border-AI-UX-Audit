# Cross-Border AI UX Audit / 跨境 AI 用户体验审计

![version](https://img.shields.io/badge/version-1.0.0-blue) ![license](https://img.shields.io/badge/license-MIT-green) ![dimensions](https://img.shields.io/badge/dimensions-9-orange) ![bilingual](https://img.shields.io/badge/report-EN%20%2B%20%E4%B8%AD%E6%96%87-teal) ![agent skill](https://img.shields.io/badge/agent%20skill-open%20standard-purple)

An **Agent Skill** that audits whether an AI product's user experience is **ready for a specific target market** — not merely translated — and turns the gaps into a prioritized, client-ready **bilingual (English + 中文)** report: a deterministic market-fit score, before/after copy rewrites, an implementation backlog, and expert-review flags.

一个 **Agent Skill**：审计某个 AI 产品的用户体验是否真正**为特定目标市场做好了准备**（而不只是被翻译过），并把差距转化为一份可直接交付客户的**中英双语**报告：确定性的市场契合度评分、改写前后对照、实施待办清单，以及需专家复核的标记。

> **EN —** A product is not ready for a new market merely because its interface has been translated. It is ready when target-market users can **understand it, trust it, control it, recover from its failures, and see why it is relevant to them.**
>
> **中文 —** 产品并不会仅因为界面被翻译就为新市场做好了准备。只有当目标市场的用户能够**理解它、信任它、掌控它、在它出错时能恢复，并且看得出它与自己相关**时，它才算就绪。

**Read in:** [English](#-english) · [中文](#-中文)　|　**Install across tools:** [`INSTALL.md`](INSTALL.md)

---

# 🇬🇧 English

## What it is
A cross-border AI UX audit checks whether people in a **specific market** can understand, trust, control, and adopt an AI product as it exists today. The unit of analysis is a **market corridor** — `source market → target market → audience → product category → business goal → the materials reviewed` — not a generic language. The same product going *China → Russia/CIS B2B* needs different positioning, proof, and trust explanations than *China → English-speaking self-serve SaaS*.

It is a **decision-support tool**, not a translation review, legal/compliance opinion, security test, or market-fit guarantee. Compliance-sensitive items are **flagged for qualified experts**, not answered.

## What you get
Every audit produces a complete, client-ready package:

- 📊 **A market-fit score (0–100)** — computed by a deterministic weighted rubric (not guessed), with a readiness band, a confidence level, and a per-dimension breakdown across nine dimensions.
- 🔍 **Structured findings** — each with the evidence, the problem, why it matters for that market, a recommendation, a **before/after rewrite in the target-market language**, a market note, and a **cited standard** (e.g. NIST AI RMF, WCAG, MQM).
- ✅ **A prioritized backlog** — every fix tagged P1/P2/P3 × work area (UX / Copy / Localization / Trust / Agent Design / Compliance) × estimated impact.
- ⚠️ **Expert-review flags** — privacy, data-transfer, regulated-sector, and accessibility-conformance items routed to qualified experts.
- 📄 **A designed bilingual HTML report** with an **EN / 中文 toggle** and standards-citation chips, plus a **PDF**, a backlog **CSV**, and **Jira / Linear** exports.
- 💬 **A short chat summary** — overall readiness, the top 3 risks, the score, and links to every file.

## The nine dimensions
Findings are organized across nine dimensions, each grounded in a named external standard:

| # | Dimension | Asks | Grounded in |
|---|---|---|---|
| 1 | Language naturalness | Does it read native to the category, not translated? | MQM / MQM-Chat |
| 2 | Cultural fit | Do framing, examples, and promises fit the market? | Playbook |
| 3 | Trust & privacy | Is there enough to trust it before sharing data? | NIST AI RMF · ISO 42001 |
| 4 | AI expectation-setting | Are capability, limits, and control communicated? | NIST AI RMF |
| 5 | UX clarity | Do users know where they are and how to recover? | Nielsen · Norman |
| 6 | Conversion | Are there credible, low-friction next steps? | Nielsen / playbook |
| 7 | Agent & chatbot behavior | Is conversational AI bounded and accountable? | NIST AI RMF · OWASP LLM |
| 8 | **Accessibility** | Can everyone perceive and operate it (and is it legal)? | WCAG 2.1 AA · EN 301 549 · ADA |
| 9 | Market-entry risk | What could block launch beyond one screen? | Playbook |

## How it works (the steps)
1. **Intake & corridor** — the skill asks a short question set and defines the decision the audit must support and the market corridor.
2. **Evidence** — you paste materials (landing copy, onboarding, chatbot/agent transcripts, pricing, trust copy) or give URLs; with URLs it **captures live screenshots + text** so findings cite real evidence.
3. **Evaluate** — it reviews the product across the nine dimensions against an editable **target-market playbook** and the named standards.
4. **Findings** — it writes evidence-grounded findings with before/after rewrites and standards citations.
5. **Critic pass** — a built-in self-review checks every finding for evidence, honest severity, and no overreach.
6. **Score** — a deterministic script computes the market-fit score (with a corridor weight profile and caps for unresolved Critical issues).
7. **Prioritize & flag** — it builds the P1/P2/P3 backlog and flags expert-review items.
8. **Report** — it renders the bilingual HTML/PDF report, exports the backlog (CSV / Jira / Linear), and gives a chat summary. Re-run later and `compare_audits.py` shows the deltas.

## How to use it
1. **Install** it for your tool (one line — see [`INSTALL.md`](INSTALL.md)).
2. **Ask** for an audit, e.g.:
   - "Is our AI agent ready to launch in the US self-serve SaaS market?"
   - "Audit our chatbot's onboarding for the China inbound market."
   - "Why is our localized landing page converting badly in Russia/CIS?"
   - "Check our AI app for accessibility and market fit before the EU launch."
3. **Answer the intake** questions (decision, source → target market, audience, product type, business goal, the materials you can share, report languages). Paste your copy, or share URLs for live capture.
4. **Receive the report** — open the HTML, toggle EN / 中文, hand the PDF to the client, import the backlog into Jira/Linear, and send the flagged items to the right experts.

**Worked example.** Input: a China-origin AI agent's landing copy ("The AI agent handles the entire workflow for you"), onboarding, and pricing page, targeting English-global self-serve buyers. Output: a 56/100 report flagging the absolute-autonomy claim (High, NIST AI RMF), a missing trust panel at upload (High), a contrast/labels accessibility failure (High, WCAG 2.1 AA), buzzword-dense hero copy (MQM), and vague CTAs — each with a target-language rewrite, a P1–P3 backlog, and privacy + accessibility expert-review flags. (See the example report in the releases / `assets/`.)

## Built-in market playbooks
Russian/CIS · Balkan/EU · English-speaking global · China inbound · LATAM · MENA/Gulf. Playbooks are **working hypotheses, not cultural absolutes** — each carries provenance, a version stamp, and segmentation guidance, and the skill never stereotypes a region as uniform.

## Scope & safety — what it is NOT
Not a translation review, grammar check, legal/compliance opinion, security/penetration test, model benchmark, or a guarantee of market fit. It **flags** privacy, data-transfer, regulated-sector, and accessibility-conformance items for qualified local experts. The score is a heuristic summary for comparing iterations — **prioritize the findings over the number**. AI-assisted output **must be reviewed by a qualified operator** before client delivery.

## Install · run · develop
- **Install** (Claude Code / Codex CLI / Gemini CLI / Qwen Code / Cursor / Claude.ai / Doubao · MiniMax · others): see [`INSTALL.md`](INSTALL.md).
- **Run the scripts** (plain Python 3):
  ```bash
  python3 scripts/capture_evidence.py --url https://site/pricing -o evidence/   # optional live evidence
  python3 scripts/score_audit.py audit.json --in-place --profile eu_eaa          # deterministic score
  python3 scripts/render_html_report.py audit.json -o report.html                # bilingual HTML
  python3 scripts/export_issue_tracker.py audit.json --format jira -o jira.csv    # or linear / csv
  python3 scripts/compare_audits.py before.json after.json                        # re-audit loop
  ```
  Optional dependency (PDF + live capture only): `python3 -m pip install playwright && python3 -m playwright install chromium`.
- **Develop**: `python3 evals/test_score_audit.py` and `python3 evals/check_golden.py`. See `CONTRIBUTING.md` and `CHANGELOG.md`.

---

# 🇨🇳 中文

## 这是什么
跨境 AI 用户体验审计，用来检验**特定市场**的用户能否理解、信任、掌控并采用一个 AI 产品的当前形态。分析的基本单位是**市场走廊（market corridor）**——`来源市场 → 目标市场 → 受众 → 产品品类 → 业务目标 → 所审材料`——而不是笼统的“某种语言”。同一个产品走 *中国 → 俄罗斯/独联体 B2B* 与走 *中国 → 英语全球自助 SaaS*，所需的定位、佐证与信任说明完全不同。

它是一个**决策支持工具**，并非翻译审校、法律/合规意见、安全测试或市场契合度保证。涉及合规敏感的事项会被**标记给合格专家**，而不是由它下结论。

## 你会得到什么（交付物）
每次审计都会产出一套可直接交付客户的完整成果：

- 📊 **市场契合度评分（0–100）**——由确定性加权规则计算（而非臆测），含就绪区间、置信度，以及九个维度的逐项明细。
- 🔍 **结构化发现**——每条含原文/证据、问题、为何对该市场重要、建议、**以目标市场语言给出的改写前后对照**、市场说明，以及**所引用的标准**（如 NIST AI RMF、WCAG、MQM）。
- ✅ **优先级待办清单**——每项修复标注 P1/P2/P3 × 工作领域（体验 / 文案 / 本地化 / 信任 / 智能体设计 / 合规）× 预估影响。
- ⚠️ **需专家复核的标记**——隐私、数据跨境、受监管领域、无障碍合规等事项转交合格专家。
- 📄 **经设计的中英双语 HTML 报告**，带 **EN / 中文 切换**与标准引用标签，并附 **PDF**、待办 **CSV**，以及 **Jira / Linear** 导出。
- 💬 **简短对话摘要**——总体就绪度、三大风险、评分，以及所有文件的链接。

## 九个评估维度
发现按九个维度组织，每个维度都以具名外部标准为依据：

| # | 维度 | 关注 | 依据标准 |
|---|---|---|---|
| 1 | 语言自然度 | 读起来是否地道，而非翻译腔？ | MQM / MQM-Chat |
| 2 | 文化契合度 | 框架、示例与承诺是否契合市场？ | playbook |
| 3 | 信任与隐私 | 共享数据前是否有足够信任依据？ | NIST AI RMF · ISO 42001 |
| 4 | AI 预期设定 | 是否说清能力、边界与控制权？ | NIST AI RMF |
| 5 | 体验清晰度 | 用户是否知道身处何处、如何恢复？ | Nielsen · Norman |
| 6 | 转化 | 是否有可信、低摩擦的下一步？ | Nielsen / playbook |
| 7 | 智能体/对话行为 | 对话式 AI 是否有界、可问责？ | NIST AI RMF · OWASP LLM |
| 8 | **无障碍** | 所有人是否都能感知与操作（且合法）？ | WCAG 2.1 AA · EN 301 549 · ADA |
| 9 | 市场进入风险 | 单屏之外还有什么会阻碍上线？ | playbook |

## 工作流程（步骤）
1. **Intake 与走廊**——技能先问一组简短问题，明确审计要支持的决策与市场走廊。
2. **证据**——你粘贴材料（落地文案、引导流程、对话/智能体记录、定价、信任文案）或给出 URL；提供 URL 时会**实时采集页面截图与文本**，让发现有真实证据支撑。
3. **评估**——对照可编辑的**目标市场 playbook**与具名标准，从九个维度审视产品。
4. **撰写发现**——产出有证据支撑、带改写前后对照与标准引用的发现。
5. **批判性复核（critic pass）**——内置自检逐条核验证据、严重度是否如实、有无越界结论。
6. **评分**——由确定性脚本计算市场契合度评分（含走廊权重档，对未解决的严重项封顶）。
7. **排优先级与标记**——生成 P1/P2/P3 待办，并标记需专家复核项。
8. **生成报告**——渲染中英双语 HTML/PDF 报告，导出待办（CSV / Jira / Linear），并给出对话摘要。日后复审可用 `compare_audits.py` 查看前后差异。

## 如何使用
1. **安装**到你所用的工具（一行命令——见 [`INSTALL.md`](INSTALL.md)）。
2. **发起审计**，例如：
   - “我们的 AI 智能体适合在美国自助 SaaS 市场上线吗？”
   - “审计我们对话产品在中国入站市场的引导流程。”
   - “为什么我们在俄罗斯/独联体的本地化落地页转化很差？”
   - “在欧盟上线前，检查我们 AI 应用的无障碍与市场契合度。”
3. **回答 intake 问题**（决策、来源 → 目标市场、受众、产品类型、业务目标、可提供的材料、报告语言）。粘贴文案，或提供 URL 以便实时采集。
4. **获取报告**——打开 HTML、在 EN / 中文 间切换、把 PDF 交给客户、把待办导入 Jira/Linear，并将标记项交给相应专家。

**示例。** 输入：一个源自中国的 AI 智能体的落地文案（“The AI agent handles the entire workflow for you”）、引导流程与定价页，目标为英语全球自助买家。输出：一份 56/100 的报告，标记出绝对自主性表述（High，NIST AI RMF）、上传环节缺少信任面板（High）、对比度/标签的无障碍失败（High，WCAG 2.1 AA）、堆砌流行词的首屏文案（MQM）以及含糊的行动按钮——每条都附目标语言改写、P1–P3 待办，以及隐私与无障碍的专家复核标记。（示例报告见 releases / `assets/`。）

## 内置市场 playbook
俄罗斯/独联体 · 巴尔干/欧盟 · 英语全球 · 中国入站 · 拉美（LATAM）· 中东/海湾（MENA）。playbook 是**待验证的工作假设，并非文化定论**——每条带来源、版本标记与细分指引，技能绝不会把一个多元地区当作铁板一块。

## 适用范围与安全——它不做什么
不是翻译审校、语法检查、法律/合规意见、安全/渗透测试、模型基准，也不是市场契合度保证。它会把隐私、数据跨境、受监管领域与无障碍合规事项**标记**给合格的本地专家。评分只是用于比较迭代的启发式概览——**请以发现项为准，而非分数本身**。AI 辅助产出在交付客户前**必须经合格操作者复核**。

## 安装 · 运行 · 开发
- **安装**（Claude Code / Codex CLI / Gemini CLI / Qwen Code / Cursor / Claude.ai / 豆包 · MiniMax · 其他）：见 [`INSTALL.md`](INSTALL.md)。
- **运行脚本**（纯 Python 3）：见上方英文代码块（评分、渲染、导出、实时采集、版本对比）。仅 PDF 与实时采集需要可选依赖 Playwright，其余仅用标准库。
- **开发**：`python3 evals/test_score_audit.py` 与 `python3 evals/check_golden.py`；参见 `CONTRIBUTING.md` 与 `CHANGELOG.md`。

---

## Repository structure / 仓库结构
```
cross-border-ai-ux-audit/
├── SKILL.md                         # orchestrator the agent loads / 技能主文件
├── INSTALL.md                       # cross-runtime install (EN + 中文) / 跨运行时安装
├── README.md · LICENSE.txt · CHANGELOG.md · CONTRIBUTING.md
├── AGENTS.md · GEMINI.md · gemini-extension.json   # adapters for Codex/Qwen/Gemini / 适配文件
├── references/                      # detail, loaded on demand / 按需加载的细节
│   ├── intake_and_corridor.md · audit_dimensions.md · framework_crosswalk.md
│   ├── market_playbooks.md · evidence_and_inputs.md · scoring_severity_priority.md
│   ├── calibration_and_review.md · finding_and_report_schema.md
│   └── report_design_and_output.md · limitations_and_safety.md
├── scripts/                         # deterministic tools (plain Python 3) / 确定性工具
│   ├── score_audit.py · mqm_language_score.py · capture_evidence.py
│   ├── export_backlog_csv.py · export_issue_tracker.py · compare_audits.py
│   ├── render_markdown_report.py · render_html_report.py · html_to_pdf.py
│   └── bundle_for_system_prompt.py  # for models without a skills CLI / 无技能 CLI 的模型
├── assets/                          # sample_audit.json + rendered template / 示例与模板
└── evals/                           # tests + fixtures (not shipped in the .skill) / 测试
```

---

*Built to the Agent Skills open standard (`agentskills.io`): a `SKILL.md` orchestrator plus on-demand `references/`, deterministic `scripts/`, `assets/`, and dev `evals/`. Review and customize the playbooks, weights, and tone vocabulary for your studio before production use. / 遵循 Agent Skills 开放标准构建；投入生产前请按你的团队定制 playbook、权重与措辞。*
