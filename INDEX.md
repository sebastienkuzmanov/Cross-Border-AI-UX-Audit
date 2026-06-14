# Cross-Border AI UX Audit — Project Bundle / 项目合集

Everything from this project, in one folder. / 本项目的全部产出，集中在一个文件夹内。

## What's inside / 文件夹内容

```
Cross-Border-AI-UX-Audit/
├── INDEX.md                          ← you are here / 你在这里
├── cross-border-ai-ux-audit.skill    ← the installable skill / 可安装的技能包
├── skill-source/
│   └── cross-border-ai-ux-audit/     ← full source = the GitHub repo / 完整源码（即 GitHub 仓库）
├── examples/                         ← what the skill produces / 技能产出示例
│   ├── example_report.html           ← bilingual report (open in a browser, toggle EN/中文)
│   ├── example_report.pdf            ← PDF version / PDF 版
│   ├── example_backlog.csv           ← priority backlog / 优先级待办
│   └── example_backlog_jira.csv      ← Jira import format / Jira 导入格式
└── docs/
    ├── competitive-review.md         ← research: similar skills + upgrade roadmap / 竞品研究与升级路线
    └── how-to-build-a-similar-skill.md ← guide to building a skill like this / 如何构建同类技能
```

## How to use each part / 各部分用法

**EN**
- **Install the skill:** use `cross-border-ai-ux-audit.skill` — upload it in Claude.ai (Settings → Capabilities), or for other agents see `skill-source/cross-border-ai-ux-audit/INSTALL.md`.
- **Read / edit / publish the source:** open `skill-source/cross-border-ai-ux-audit/`. Its `README.md` (bilingual) explains everything; `INSTALL.md` covers Claude Code, Codex, Gemini CLI, Qwen Code, Doubao, MiniMax, and more.
- **See what it produces:** open `examples/example_report.html` in a browser and use the EN / 中文 toggle.
- **Publish to GitHub:** the folder under `skill-source/` is push-ready. From a terminal:
  ```bash
  cd skill-source/cross-border-ai-ux-audit
  git init && git add . && git commit -m "Initial commit: Cross-Border AI UX Audit skill v1.0.0"
  git branch -M main
  git remote add origin https://github.com/<your-username>/cross-border-ai-ux-audit.git
  git push -u origin main
  ```
  (Create the empty repo on github.com first, without a README/license.) Remember to fill the `<YOUR NAME OR STUDIO>` placeholder in `LICENSE.txt`.

**中文**
- **安装技能：** 使用 `cross-border-ai-ux-audit.skill`——在 Claude.ai（设置 → Capabilities）上传；其他代理见 `skill-source/cross-border-ai-ux-audit/INSTALL.md`。
- **阅读 / 修改 / 发布源码：** 打开 `skill-source/cross-border-ai-ux-audit/`。其中 `README.md`（中英双语）讲解全部内容；`INSTALL.md` 覆盖 Claude Code、Codex、Gemini CLI、Qwen Code、豆包、MiniMax 等。
- **查看产出效果：** 用浏览器打开 `examples/example_report.html`，使用 EN / 中文 切换。
- **发布到 GitHub：** `skill-source/` 下的文件夹已可直接推送。终端命令见上方英文代码块；发布前请先在 github.com 创建空仓库（不要勾选 README/license），并填好 `LICENSE.txt` 中的 `<YOUR NAME OR STUDIO>` 占位符。

---
*Note: the `.skill` and the `skill-source/` folder contain the same skill — one is packaged for installing, the other is the open folder for reading, editing, and pushing to GitHub. / 说明：`.skill` 与 `skill-source/` 为同一技能——前者为安装用打包文件，后者为便于阅读、修改与推送 GitHub 的展开文件夹。*
