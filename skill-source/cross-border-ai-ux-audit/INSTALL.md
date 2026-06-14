# Install & Compatibility / 安装与兼容性

This skill is written to the **Agent Skills open standard** (`agentskills.io`): a `SKILL.md` with standard frontmatter plus on-demand `references/`, `scripts/`, and `assets/`. Well-formed skills are **portable across compatible agents without modification** — only the install directory differs.

本技能遵循 **Agent Skills 开放标准**（`agentskills.io`）：一个带标准 frontmatter 的 `SKILL.md`，外加按需加载的 `references/`、`scripts/`、`assets/`。规范的技能在各兼容代理之间**无需修改即可移植**，仅安装目录不同。

---

## 1. Native SKILL.md agents (drop-in) / 原生支持 SKILL.md 的代理（直接放入）

Place the whole `cross-border-ai-ux-audit/` folder in the agent's skills directory, then start a new session and ask it to run an audit. The agent activates the skill by matching your prompt against the `description`.

把整个 `cross-border-ai-ux-audit/` 文件夹放入对应代理的技能目录，开新会话并请求做一次审计即可；代理会根据你的提问匹配 `description` 自动激活。

| Agent / 代理 | Personal path / 个人 | Project path / 项目 | Notes / 说明 |
|---|---|---|---|
| **Claude Code** | `~/.claude/skills/` | `.claude/skills/` | Also: upload the `.skill` in Claude.ai Settings → Capabilities. |
| **Codex CLI** (OpenAI) | `~/.codex/skills/` | `.codex/skills/` | Enable skills in Codex settings; optional `openai.yaml` metadata is ignored elsewhere. |
| **Gemini CLI** (Google) | `~/.gemini/skills/` | `.gemini/skills/` | Optional `gemini-extension.json` (included) registers it as an extension. |
| **Qwen Code** (Alibaba / 通义千问) | `~/.qwen/skills/` | `.qwen/skills/` | Browse/invoke with the `/skills` command. |
| **Cursor** | — | `.cursor/skills/` | Manual invocation (no auto-discovery). |
| **GitHub Copilot / Cline / Windsurf / Goose / Roo Code …** | per tool | per tool | Same SKILL.md; see each tool's skills path. |

Example (Qwen Code, personal) / 示例（Qwen Code，个人）:
```bash
mkdir -p ~/.qwen/skills && cp -r cross-border-ai-ux-audit ~/.qwen/skills/
# Codex:  cp -r cross-border-ai-ux-audit ~/.codex/skills/
# Gemini: cp -r cross-border-ai-ux-audit ~/.gemini/skills/
# Claude Code: cp -r cross-border-ai-ux-audit ~/.claude/skills/
```
The `SKILL.md` is identical for all of them — no edits needed. / 各代理使用同一个 `SKILL.md`，无需改动。

---

## 2. Models without a native skills CLI — Doubao, MiniMax, GLM, Kimi, etc. / 没有原生技能 CLI 的模型——豆包、MiniMax、GLM、Kimi 等

These are **models**, not skill-hosting agents, so there is no `~/.doubao/skills/` style directory. Use one of three paths:

它们是**模型**而非技能宿主代理，没有 `~/.doubao/skills/` 之类的目录。可用以下三种方式之一：

**A. A skills-compatible host with your model's API key / 用支持技能的宿主 + 你的模型 Key.**
Run a SKILL.md-compatible agent host (e.g. OpenClaw, Orkas, or any agent that supports skills and BYO keys) and configure it to use Doubao / MiniMax / Qwen / GLM / Kimi as the backing model. The skill loads exactly as in section 1.
运行一个兼容 SKILL.md 的代理宿主（如 OpenClaw、Orkas 或任何支持技能且可自带 Key 的代理），将其后端模型设为豆包 / MiniMax / 通义 / GLM / Kimi，技能加载方式同第 1 节。

**B. AgentSkills → MCP bridge (for function-calling models) / 技能转 MCP 桥（适用于支持函数调用的模型）.**
Any model with tool/function calling (Doubao, MiniMax, Qwen, GLM…) can use skills by exposing them through an AgentSkills MCP server and passing those tools to the model. The model then discovers and loads this skill like any tool.
任何支持工具/函数调用的模型（豆包、MiniMax、通义、GLM……）都可通过 AgentSkills MCP 服务暴露技能，并将这些工具传给模型；模型即可像调用工具一样发现并加载本技能。

**C. Universal system-prompt mode (works with any chat or API) / 通用系统提示模式（任意对话或 API 均可）.**
Use `scripts/bundle_for_system_prompt.py` to concatenate `SKILL.md` + the references into a single portable prompt, paste it as the **system/developer prompt** of Doubao / MiniMax / Qwen / any model, then give it the product materials. The model follows the methodology and emits the audit **JSON**; you run the rendering/scoring scripts yourself (see section 3).
用 `scripts/bundle_for_system_prompt.py` 把 `SKILL.md` 与 references 合并为一个可移植的提示，作为豆包 / MiniMax / 通义等模型的**系统/开发者提示**粘贴，再提供产品材料。模型按方法论输出审计 **JSON**，渲染/评分脚本由你自行运行（见第 3 节）。
```bash
python3 scripts/bundle_for_system_prompt.py -o system_prompt_bundle.md
# then paste system_prompt_bundle.md as the model's system prompt
```

---

## 3. Code execution & the scripts / 代码执行与脚本

The `scripts/` (deterministic scoring, MQM, renderers, exports, live capture, compare) are **plain Python 3** — runtime-agnostic. They run wherever Python runs.

`scripts/` 中的脚本（确定性评分、MQM、渲染、导出、实时采集、版本对比）均为**纯 Python 3**，与运行时无关，凡能运行 Python 处即可使用。

- Agents that can execute code (Claude Code, Codex, Gemini CLI, Qwen Code, etc.) run them directly.
- For chat-only / no-code-execution use (e.g. a plain Doubao or MiniMax chat), the model still produces the audit **JSON**; run the scripts on your own machine to score and render:
  ```bash
  python3 scripts/score_audit.py audit.json --in-place
  python3 scripts/render_html_report.py audit.json -o report.html
  ```
- Optional dependency (PDF + live capture only): `python3 -m pip install playwright && python3 -m playwright install chromium`. Everything else uses the Python standard library.

能执行代码的代理直接运行脚本；纯对话场景下，模型仍产出审计 **JSON**，你在本机运行脚本评分与渲染。仅 PDF 与实时采集需要可选依赖 Playwright，其余仅用 Python 标准库。

---

## 4. Notes on portability / 可移植性说明
- The **instructions are in English** (best cross-model triggering); the skill **outputs bilingual EN + 中文** reports, which Chinese models handle natively.
- Frontmatter sticks to widely-supported keys (`name`, `description`, `license`, `metadata`); tools ignore keys they don't use.
- Tool-specific extras are optional and harmless elsewhere: `gemini-extension.json` (Gemini), `AGENTS.md` (read by Codex and Qwen Code), `GEMINI.md` (Gemini context). They point to `SKILL.md`; they don't change behavior on agents that ignore them.
- 指令为英文（跨模型触发最佳）；技能**输出中英双语**报告，中文模型可原生处理。frontmatter 仅用广泛支持的键；各工具会忽略用不到的键。`gemini-extension.json`、`AGENTS.md`、`GEMINI.md` 为可选适配文件，对不识别它们的代理无害。
