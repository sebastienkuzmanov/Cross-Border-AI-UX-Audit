# How to Build a Skill Like the AI Product Similarity Checker

A blueprint based on a teardown of `YiLight0/AI-product-similarity-checker`.

The value of that repo isn't the "AI idea plagiarism check" domain — it's that it's a **complete, well-architected skill** that uses every layer of the skill format the way it's meant to be used. This report breaks down how it's built, names the design patterns worth copying, and gives you a step-by-step plan plus a fill-in-the-blank template to build one like it for *your* idea.

---

## 1. The pattern this skill is an instance of

Strip away the domain and the skill is really a pipeline:

> **intake → structured extraction → search the world → normalize evidence → score against a rubric → classify into a known pattern → render a designed report**

This "research-and-produce-a-report" shape applies to a huge range of ideas: a competitive-landscape checker, a grant/RFP fit analyzer, a security-posture reviewer, a "is this clinical claim supported" checker, a name/brand availability auditor, a literature gap-finder, and so on. If your idea is "take a fuzzy input, go gather evidence, judge it consistently, and hand back a polished document," this is the exact skeleton to copy.

---

## 2. Architecture at a glance (copy this layout)

```
your-skill/
├── SKILL.md            ← the ONLY file always loaded. Acts as the orchestrator/index.
├── references/         ← detailed docs, loaded on demand (the "how" of each step)
│   ├── intake_questions_and_scope.md
│   ├── <domain>_dna_schema.md
│   ├── search_query_patterns.md
│   ├── source_extraction_schema.md
│   ├── similarity_rubric.md          (your scoring rules)
│   ├── pattern_taxonomy.md           (known categories to classify into)
│   ├── report_template.md
│   ├── report_design.md              (visual/HTML spec)
│   └── limitations_and_safety.md     (tone + what NOT to say)
├── scripts/            ← deterministic code, run without loading into context
│   ├── score.py                      (turn dimension scores → weighted total)
│   ├── merge_sources.py              (dedupe evidence)
│   ├── render_html_report.py
│   ├── render_markdown_report.py
│   └── html_to_pdf.py
├── assets/             ← files used IN the output (templates, not instructions)
│   ├── report_template.html
│   └── sample_report.md
└── README.md           ← human-facing: what it is, install, how to trigger
```

**The single most important idea here is progressive disclosure.** Three loading levels:

1. **Frontmatter (name + description)** — always in context. ~50–100 words. This is the *only* thing the agent reads to decide whether to use your skill at all.
2. **SKILL.md body** — loaded when the skill triggers. Keep it lean (~150 lines here). It's an **index**, not an encyclopedia: it defines the workflow and *points to* the reference files.
3. **references/ + scripts/ + assets/** — pulled in only when a given step needs them. Unlimited size, because they're not always loaded. Scripts can even run without their code entering context.

This is why the main file can stay short while the skill stays deep. Don't dump everything into SKILL.md — route to references.

---

## 3. Anatomy of the main `SKILL.md` (section by section)

This skill's main file is ~150 lines and is organized into these sections. Use the same spine.

### Frontmatter — `name` + `description`
The description is the entire triggering mechanism. Theirs (paraphrased structure) does two things well:
- **States capability with every synonym:** "Analyze an AI product, AI application, AI agent, AI tool, AI hardware, or AI startup idea... generate a Turnitin-like conceptual similarity report."
- **Lists explicit trigger situations:** "Use this skill when the user asks whether an AI product idea has been done before, whether it is original, whether a hackathon AI idea is common, or wants prior-art / novelty / similarity checking."

Why it works: skills tend to *under*-trigger, so the description is deliberately "pushy" — it enumerates phrasings a real user would type, not just one canonical keyword. Copy this habit: write the description as a list of the actual sentences your user would say.

### `Goal`
2–3 sentences on what the skill evaluates and produces — plus, critically, the **boundary**: "Do not make legal judgments. Do not accuse any person or team of plagiarism." Stating what the skill is *not* up front shapes every later decision.

### `Use And Avoid`
Two bullet lists: "Use this for X" and "Do NOT use for Y" (non-AI ideas, code plagiarism, essay checking, patent law). This sharpens triggering precision — it stops the skill firing on adjacent-but-wrong requests. Very cheap to add, very effective.

### `Core Workflow`
A numbered 12-step pipeline — the spine of the whole skill. This is the table of contents for everything that follows. Keep it a clean ordered list (intake → extract → scan-depth → queries → search → extract evidence → merge → score → classify → render → suggest → state limits).

### `Internal Modules`
Names the conceptual sub-components (DNA extraction, query expansion, each search channel, scoring, report generation) and explicitly says **"treat these as internal modules, not separate skills."** This keeps one cohesive skill instead of fragmenting into many, while still giving the model named mental building blocks.

### `Reference Loading`
The orchestration heart. It maps each need to a specific file: *"Load only the references needed for the current task"*, then a bullet per reference file describing exactly when to read it, followed by a list of the scripts and when to run each. This is what lets the body stay short — it delegates detail downward.

### `Execution Rules`
The detailed behavioral contract, in imperative voice **with reasoning**. E.g. "Score by conceptual dimensions, then apply differentiation discounts. Names and branding matter less than AI capability and AI workflow, but obvious product-defining differences matter a lot" — followed by a concrete example. Note the style: it explains *why* a rule exists rather than barking standalone MUSTs. Models follow reasoning better than bare commands.

### `Output Style`
A prescribed vocabulary: a "use these terms" list (conceptual similarity, prior-art overlap, limited differentiation, unclear novelty) and an "avoid these terms" list (plagiarized, stolen, fraud, worthless). For any skill where tone/liability matters, this is a powerful, simple control.

### `Final Report`
The exact deliverable spec: the output formats (designed HTML + PDF when tooling exists + a short chat summary with file paths), the title, and the required sections in order. Pinning the output structure is what makes results consistent across runs.

---

## 4. What goes in `references/` and why

References hold the heavy detail you don't want bloating the main file. Each is loaded only when its step runs. The teardown's references map cleanly onto the pipeline:

| Reference file | Holds |
| --- | --- |
| `intake_questions_and_scope.md` | the pre-search questions + the scan-depth profiles (theirs: 简洁/详细/深度 → ~10/30/100 cases) |
| `<domain>_dna_schema.md` | the structured fields you extract from the user's input (see §6) |
| `search_query_patterns.md` | query categories, multilingual variants, platform-specific query shapes |
| `source_extraction_schema.md` | the normalized shape every piece of evidence must take |
| `similarity_rubric.md` | dimension **weights**, score bands, and the discount rules |
| `pattern_taxonomy.md` | the known categories to classify inputs into |
| `report_template.md` | the required final structure |
| `report_design.md` | the visual system for the HTML/PDF |
| `limitations_and_safety.md` | tone constraints and disclaimers |

**Rule of thumb:** anything that's a *schema, a rubric, a long list, or a template* belongs in a reference file, not in SKILL.md. If a reference grows past ~300 lines, give it its own table of contents.

---

## 5. What goes in `scripts/` and why

Scripts are for work that should be **deterministic and identical every run** — things you don't want the model improvising token-by-token. The teardown bundles five, and they map to exactly the steps where consistency matters:

- `score.py` — takes per-dimension scores as JSON, applies the fixed weights, returns the weighted total + risk band. (Doing weighted math in code, not in the model's head, means the same inputs always give the same number.)
- `merge_sources.py` — dedupes evidence by URL, falls back to title+platform similarity, merges matched dimensions, keeps the higher-quality summary, sorts by score.
- `render_html_report.py` / `render_markdown_report.py` — turn one structured JSON blob into the final document. The model produces *data*; the script produces *presentation*.
- `html_to_pdf.py` — converts HTML → PDF via a headless browser, with a documented fallback ("if PDF fails, still deliver the HTML and say why").

**Design principle worth stealing:** make the model's job to produce a single well-specified **JSON object**, and let scripts handle scoring and rendering. This separates judgment (model) from computation and formatting (code), which makes the whole skill more reliable and testable. Notice the repo even documents a minimal example of that JSON in its README — define your data contract explicitly.

Always give scripts a graceful fallback and state dependencies (theirs needs Playwright + Chromium for PDF).

---

## 6. The transferable design patterns (the real gold)

These are domain-independent. Lift them directly.

1. **Intake before action.** The skill refuses to start searching until it has asked a compact set of clarifying questions (or the user says "proceed with assumptions," in which case every guess is logged in an `assumptions` field). This single rule prevents the agent from charging off in the wrong direction. Bake an intake gate into almost any analysis skill.

2. **Structured extraction ("DNA").** Before doing the work, the skill converts a fuzzy idea into a fixed JSON schema (~17 fields: problem, target user, workflow, output, novelty claim, assumptions, etc.). Everything downstream operates on this clean structure instead of on free text. Define your own equivalent schema for whatever you're analyzing.

3. **A weighted rubric, not a vibe.** Scoring is split into named dimensions with explicit weights (workflow .18, capability .16, ...) and score bands (Low/Medium/High/Very High). Plus a smart wrinkle: **differentiation discounts** so superficial overlap (both use an LLM) doesn't inflate the score when product-defining details differ. A transparent rubric makes outputs defensible and consistent.

4. **Classify into a known taxonomy.** Rather than judging in a vacuum, it sorts the input into common "families" (AI companion, AI tutor, AI wrapper-for-X...). Having a catalog of known patterns turns vague judgment into recognition. Build the equivalent catalog for your domain.

5. **Controlled vocabulary for tone + liability.** The explicit "use these words / never these words" lists keep the skill analytical and non-accusatory. Any skill touching sensitive judgments (legal, medical, financial, reputational) benefits from this.

6. **Dual-format, graceful deliverable.** Primary output is a *designed* HTML report; PDF is generated when tooling exists, otherwise it degrades cleanly and explains the gap; plus a short chat summary with file paths. Specify your output formats and their fallbacks.

---

## 7. Step-by-step plan to build your own

1. **Write the one-line job + boundary.** "This skill takes ___, does ___, and produces ___. It does NOT do ___." Get this crisp before anything else.
2. **Draft the frontmatter `description`** as a list of the real sentences your user would type to invoke it. Make it slightly pushy. This is your highest-leverage 80 words.
3. **Write the `Core Workflow`** as a numbered pipeline. This becomes your skill's spine and your reference-file checklist.
4. **Design your extraction schema** (your "DNA"): the fixed JSON fields you'll pull from the user's input. Put it in `references/<domain>_dna_schema.md`.
5. **Write the intake questions** and an scope/depth profile, in `references/intake_questions_and_scope.md`. Add the rule: don't proceed past intake without answers or explicit permission.
6. **Define your rubric** — dimensions, weights, bands, and any discount rules — in `references/similarity_rubric.md` (rename to fit). Decide what's judgment vs. computation.
7. **Build the scripts** for the deterministic parts (scoring math, dedupe, rendering, format conversion). Make the model emit one JSON object; scripts consume it. Give each script a fallback.
8. **Write the report template + design spec** (`references/report_template.md`, `references/report_design.md`, `assets/*.html`). Pin the section order.
9. **Add `limitations_and_safety.md`** with your tone vocabulary and disclaimers, and reference it from an `Output Style` section in SKILL.md.
10. **Assemble SKILL.md** as the index: Goal → Use/Avoid → Core Workflow → (Internal Modules) → Reference Loading (map each file to when to load it) → Execution Rules (imperative + reasoning) → Output Style → Final Report.
11. **Write a README** for humans: what it is, who it's for, install path, and 3–5 example trigger phrases.
12. **Test on 3 realistic prompts.** Check two things separately: does it *trigger* (fix the description if not), and is the *output* good (fix the body/references if not). Iterate. Then expand the test set.

---

## 8. Starter template (fill in the blanks)

`SKILL.md`:

```markdown
---
name: your-skill-name
description: <One sentence on what it analyzes, naming every synonym for the input.> Use this skill when the user asks <phrasing 1>, <phrasing 2>, <phrasing 3>, or wants <the noun your skill produces>.
---

# Your Skill Name

## Goal
<2–3 sentences: what it evaluates and produces.> Do not <the boundary / what it must never claim>.

## Use And Avoid
Use this skill for:
- <case 1>
- <case 2>
Do not use this skill for:
- <adjacent-but-wrong case 1>
- <adjacent-but-wrong case 2>

## Core Workflow
1. Ask intake questions before <acting>.
2. Extract <your DNA schema> from the user's input.
3. <select depth / scope>.
4. <gather evidence / data>.
5. <normalize / merge>.
6. Score against the rubric.
7. Classify into a known pattern.
8. Render the report; convert to PDF when tooling exists.
9. Give concrete recommendations.
10. State limitations.

## Reference Loading
Load only what the current step needs:
- `references/intake_questions_and_scope.md`: pre-action questions + scope profiles.
- `references/<domain>_dna_schema.md`: extraction fields and confidence rules.
- `references/rubric.md`: dimension weights, bands, discount rules.
- `references/pattern_taxonomy.md`: known categories.
- `references/report_template.md`: required report structure.
- `references/limitations_and_safety.md`: tone constraints.

Use scripts when helpful:
- `scripts/score.py`: weighted total + risk band from dimension scores.
- `scripts/merge.py`: dedupe and merge evidence.
- `scripts/render_html_report.py`: JSON analysis → designed HTML.
- `scripts/html_to_pdf.py`: HTML → PDF, with fallback to HTML.

## Execution Rules
<Imperative rules, each with a short "why." Cover: intake gate, extraction,
how much evidence per depth level, source preferences, scoring + discounts,
marking unknowns as unknown rather than inventing them.>

## Output Style
Use terms such as: <neutral vocabulary>.
Avoid terms such as: <loaded vocabulary>.
Always separate facts, evidence-backed findings, inferences, and uncertainties.

## Final Report
Deliverables: a designed HTML report, a PDF when tooling exists, and a short
chat summary with file paths. The report includes, in order:
- executive summary
- <extracted DNA>
- <method / scope>
- <closest matches / evidence>
- <score breakdown>
- <pattern analysis>
- <recommendations>
- limitations
```

---

## 9. Pitfalls and notes

- **Keep SKILL.md lean.** The moment you're tempted to paste a long schema or rubric into it, move that to a reference file and link it. The body is an index.
- **Over-triggering is as bad as under-triggering.** The `Use And Avoid` lists exist precisely to stop the skill firing on near-miss requests. Don't skip them.
- **Separate judgment from computation.** Let the model produce structured JSON; let scripts do math and rendering. This is what makes the output reproducible and testable.
- **Specify fallbacks.** Every external dependency (a browser for PDF, a search backend) should have a "if unavailable, do this instead and say so" rule.
- **Where it runs.** This particular repo targets Codex skills (it installs into a `.codex/skills/` directory). Custom skills in the Claude ecosystem can be created in Claude Code, uploaded via the Claude API, or added in Claude.ai settings — same SKILL.md format, different install path. Build the folder once; install it wherever you need it.
- **Third-party-skill caution.** This repo looks clean, but as a general habit, only run skills (especially their scripts) from sources you trust or have audited — a skill's scripts execute with whatever access the agent has.

---

### Bottom line
Copy the *shape*, not the domain: a lean orchestrator `SKILL.md` that routes to `references/` for detail and `scripts/` for deterministic work; an intake gate; a structured extraction schema; a transparent weighted rubric; a known-pattern taxonomy; a controlled tone vocabulary; and a pinned, graceful report format. Fill those slots with your idea and you'll have a skill at the same level of polish.
