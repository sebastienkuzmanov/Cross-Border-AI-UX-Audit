# Cross-Border AI UX Audit — Competitive Research & Upgrade Report

*Prepared June 14, 2026. Method: web research across the Claude/Agent-Skills ecosystem (official Anthropic repo + community marketplaces), the closest comparable audit skills on GitHub, and the established methodologies your skill implicitly draws on (UX heuristics, AI-governance frameworks, localization-quality standards, and accessibility law). Sources listed at the end.*

---

## 1. Executive summary

**Verdict: your skill occupies a niche that nothing else currently fills, but its methodology is "self-authored" where the strongest competitor is "standards-grounded." Closing that one gap — plus adding live evidence capture and an accessibility dimension — would move it from a strong indie skill to a defensible, professional-grade product.**

Three findings drove this conclusion:

1. **No direct competitor exists.** Across Anthropic's official catalog (~17–25 skills) and the major community marketplaces, there is **no** cross-border / market-readiness / localization-aware AI-UX audit skill. The adjacent skills are either generic UX audits, generic AI-governance audits, or general website audits. Your combination — *AI-product-specific dimensions + market corridors + editable market playbooks + a deterministic market-fit score + bilingual EN/中文 output* — is unique in the set I found.

2. **The bar to beat is `mastepanoski/claude-skills`.** It is the most professionally packaged comparable (31★, 23 commits, versioned, multi-platform, indexed on skills.sh). Its edge is **credibility through named standards** — Nielsen, WCAG, NIST AI RMF, ISO 42001, OWASP LLM. That is precisely the dimension where your skill is weakest.

3. **Your scoring, bilingual output, and report design are genuinely ahead of the field.** No comparable produces a deterministic, capped, weight-renormalized score; none produces true bilingual reports with target-market-language rewrites; and most default to the "AI-slop" cream/serif/terracotta report look that yours deliberately avoids.

---

## 2. The comparable landscape

### Ecosystem context
The agent-skills ecosystem grew from one registry in late 2025 to roughly eight marketplaces by Q2 2026 (skills.sh, SkillsMP, MCP Market, Agensi, ClaudeSkills.info, LobeHub, etc.). Anthropic's official `anthropics/skills` repo holds ~17–25 demonstration skills (documents, creative/design, dev/technical, enterprise comms) — **none** in localization, UX audit, or market readiness. So you are not competing with an Anthropic first-party skill.

### The four closest skills

| Skill | Stars / maturity | What it is | Overlap with yours | Key difference |
|---|---|---|---|---|
| **mastepanoski/claude-skills** | 31★, 23 commits, MIT, versioned, multi-platform | An 11-skill **suite**: a UX-evaluation set (Nielsen, WCAG, Don Norman, IxDF, cognitive walkthrough, UI review) + an AI-governance/security set (NIST AI RMF, ISO 42001, OWASP LLM Top 10, OWASP AI Testing, AIAS) | UX audit + AI trust/risk evaluation; severity ratings; structured reports | **Standards-grounded and generic.** No market corridors, no localization, no market-fit score, no bilingual output. Separate single-purpose skills rather than one workflow. |
| **appariciojunior/website-audit-skill** | 9★, solo | One structured website **content + UX audit** that crawls every page; output is a severity-tagged MD report with a priority action plan | Intake-first; conversion + UX + copy review; severity tiers; **touches localization** (PT-BR vs PT-PT, US vs UK dialect) | **Not AI-specific.** No corridor/playbook, no score, no bilingual output, no AI-trust/agent dimensions, no expert escalation. But it *crawls live pages* (you don't). |
| **daymade/claude-code-skills → `product-analysis`** | active marketplace | Evidence-driven product audit using parallel agents; covers UX/API/architecture + **competitive benchmark**; quantified findings; a `references/analysis_dimensions.md` | Dimensions file + quantified findings + priority recommendations + UX audit framing | **General product audit**, not cross-border or AI-trust-specific. But it adds *competitive benchmarking* and *live crawling*, which you lack. |
| **yoyothesheep/claude-skills** | active | AEO/SEO site-audit skills with an audit→fix→audit loop and IA/UX recommendations | Site audit; UX recommendations; iterative loop | SEO/AEO focus; tangential to market-readiness. |

**Structural note:** the two closest *output-structure* matches (website-audit-skill, product-analysis) both **crawl live pages**, and the closest *AI-methodology* match (mastepanoski) is **standards-grounded**. Your skill is, in effect, more sophisticated than each on its own axis but is missing the specific strength that each competitor leads with.

---

## 3. Feature-by-feature comparison

| Capability | **Yours** | mastepanoski | website-audit | product-analysis |
|---|---|---|---|---|
| AI-product-specific dimensions (trust, AI expectation, agent behavior) | ✅ 8 dimensions | ⚠️ via separate AI-governance skills | ❌ | ❌ |
| Cross-border / market-corridor unit of analysis | ✅ | ❌ | ❌ (dialect only) | ❌ |
| Editable market playbooks + anti-stereotype governance | ✅ 4 corridors | ❌ | ❌ | ❌ |
| Deterministic, weighted, capped market-fit score | ✅ | ❌ (qualitative severity) | ❌ | ⚠️ "quantified findings" |
| Bilingual EN + 中文 report w/ language toggle | ✅ | ❌ | ❌ | ❌ |
| Target-market-language before/after rewrites | ✅ | ❌ | ⚠️ corrected text, source-lang | ❌ |
| Severity **and** priority separation | ✅ | ⚠️ severity only | ⚠️ 3 tiers | ✅ |
| Expert-review escalation (legal/privacy/security) | ✅ | ⚠️ implied by governance skills | ❌ | ❌ |
| Grounding in **named external standards** | ❌ **gap** | ✅ Nielsen/WCAG/NIST/ISO/OWASP | ❌ | ⚠️ partial |
| Live page / screenshot evidence capture | ❌ **gap** | ⚠️ from URL/screenshot input | ✅ crawls pages | ✅ crawls + benchmarks |
| Accessibility (WCAG/EN 301 549) dimension | ❌ **gap** | ✅ dedicated skill | ⚠️ basic (alt text) | ❌ |
| Competitive / category benchmarking | ❌ | ❌ | ❌ | ✅ |
| Eval / regression-test harness | ❌ **gap** | ⚠️ DEVELOPMENT.md + iteration | ❌ | ❌ |
| Repo polish (CHANGELOG, CONTRIBUTING, badges, skills.sh) | ❌ **gap** | ✅ | ❌ | ⚠️ |
| Single coherent end-to-end workflow | ✅ | ❌ (scattered skills) | ✅ | ✅ |

---

## 4. Strengths of your skill (validated against the field)

1. **Unique, defensible niche.** It is the only skill found that treats an AI product's readiness for a *specific market corridor* as the unit of analysis. The corridor concept (source → target → audience → category → goal → materials) is something none of the comparables have, and it is the right abstraction for this problem.

2. **The scoring is the most rigorous in the category.** A weighted rubric that renormalizes over scored dimensions, caps the total on unresolved Critical issues (59 / 39), and routes evidence-completeness to a confidence label rather than silently moving the number — no comparable does anything close. Most have no score at all; the ones that "quantify" don't expose their model. This is a real, demonstrable advantage.

3. **True bilingual output is rare and hard.** Competitors at best *flag* dialect issues in one language; yours produces the full report in EN **and** 中文 with a toggle, and writes the actual rewrite copy in the target market's language. For a cross-border tool this is the headline feature, and it's unmatched in the set.

4. **Playbooks as an explicit, governed context layer.** Treating market expectations as editable, versionable *working hypotheses* with anti-stereotype guidance is more thoughtful than the generic "good UX" baseline the other skills apply, and it directly addresses the biggest failure mode of cross-border advice.

5. **Operational maturity.** Severity-vs-priority separation, a structured finding schema (evidence → problem → why → recommendation → rewrite → note), expert-review escalation, and a controlled non-accusatory vocabulary are consultant-grade touches the hobby skills lack.

6. **Clean engineering and non-default design.** The "model emits one JSON object, scripts score and render" split is reproducible and testable. And the report's deliberately non-AI-default aesthetic (cool paper, system sans, teal, functional severity colors) is itself a differentiator — even Anthropic's own brand-guidelines skill ships the cream/orange look you avoided.

7. **One coherent workflow** (intake → evidence → 8 dimensions → score → backlog → report) versus the scattered single-purpose skills users otherwise have to chain together.

---

## 5. Weaknesses & gaps (sharpened by the comparison)

1. **Methodology isn't cross-walked to named standards — the single biggest credibility gap.** Your eight dimensions are sensible but read as "invented." `mastepanoski` cites Nielsen's 10 heuristics, WCAG 2.1/2.2, NIST AI RMF (Govern/Map/Measure/Manage + 7 trustworthiness characteristics), ISO 42001, and OWASP LLM Top 10 — which instantly answers the enterprise buyer's question "says who?". Right now your findings can't point to an external authority.

2. **Evidence is text-only; there's no live capture.** Your own spec lists this as the MVP's top limitation, and the comparison makes it sting: `website-audit-skill` and `product-analysis` both crawl rendered pages, so they can evaluate real states, flows, and visuals. Your Level-2/3 conclusions are currently inferred from pasted text, which limits how far findings can honestly go.

3. **No accessibility dimension — now a legal exposure, not just a quality gap.** "UX readiness" without accessibility is incomplete, and for any corridor touching EU consumers it's now a compliance issue: the **European Accessibility Act became enforceable on 28 June 2025**, applies to non-EU companies selling into the EU, uses EN 301 549 (WCAG 2.1 AA) as the technical standard, carries per-violation fines (roughly €10k–€300k depending on member state), and automated tools catch only ~30–40% of barriers. Your Balkan/EU corridor in particular should not ship without this.

4. **Scoring weights are uncalibrated.** You flag this honestly, but there's no calibration set, no per-dimension anchored examples, and no inter-rater methodology. The gold standard to emulate is **MQM** (below), which pairs an explicit typology with multi-annotator scoring.

5. **No eval / regression harness.** The official `skill-creator` supports evals, benchmarking, and variance analysis; `mastepanoski` shows 23 commits of iteration plus a DEVELOPMENT.md. Your scripts were tested once but have no triggering tests, no golden outputs, and no unit tests around the scorer's edge cases.

6. **The "language" dimension isn't grounded in localization QA.** It's the most translation-adjacent dimension, yet it doesn't reference the field's standard. **MQM (Multidimensional Quality Metrics)** — an EU-origin framework now heading toward ISO standardization, used as the gold standard in WMT shared tasks — provides an error typology (Core ~39 types) plus severity and a scoring model, and there is a **2025 MQM-Chat** variant with categories tailored to conversational AI (ambiguity/disambiguation, buzzword/loanword issues, dialogue inconsistency). LLM-automated MQM (AutoMQM, GEMBA-MQM) is precedent that an LLM applying a structured typology with severity is a validated pattern — exactly what your skill does.

7. **Playbooks are broad and few.** Four regional generalizations, no country/industry/audience segmentation, no source provenance, no version stamps. You note the stereotype risk; the structural fix is granularity + provenance + versioning.

8. **No competitive / category benchmarking.** `product-analysis` compares against competitors; cross-border buyers care about *local category norms*, which your product-internal audit doesn't yet capture.

9. **Single-rater LLM judgment.** There's no second-pass/critic and no self-consistency check beyond the evidence-completeness label. MQM uses 2–3 annotators per segment; a critic pass would raise reliability.

10. **Repo & distribution maturity.** No CHANGELOG, CONTRIBUTING, issue/PR templates, version badge, demo report in the README, skills.sh indexing, one-line install, or plugin packaging. `mastepanoski` models the bar, and this directly affects discoverability and trust.

---

## 6. Upgrade roadmap

Ordered by leverage. P1 = highest impact for the effort; do these first.

### P1 — Credibility & correctness (mostly documentation; very high ROI)

- **Add a "framework cross-walk" reference.** Map each dimension to a named standard and *cite it in findings*:
  - `ux_clarity` → Nielsen's 10 heuristics + Norman's principles
  - `trust_and_privacy` + `ai_expectation_setting` + `agent_chatbot_behavior` → NIST AI RMF's 7 trustworthiness characteristics (valid & reliable, safe, secure & resilient, accountable & transparent, explainable & interpretable, privacy-enhanced, fair) and ISO 42001 themes
  - `language_naturalness` → MQM / MQM-Chat typology
  - new accessibility dimension → WCAG 2.1 AA / EN 301 549
  This is the cheapest change with the biggest credibility payoff. A finding that reads "per NIST AI RMF (Explainable & Interpretable), the agent gives no confidence or provenance…" is far more defensible than an unattributed one.

- **Add an Accessibility dimension (the 9th).** Grounded in WCAG 2.1 AA / EN 301 549, with an **EAA legal-flag** escalation for any EU-facing corridor. Re-normalize the scoring weights to include it, and add accessibility rules to the Balkan/EU (and any EU-touching) playbook.

- **Ground `language_naturalness` in MQM.** Adopt a compact MQM-derived error typology plus MQM severity levels; for chatbot/agent surfaces, use the MQM-Chat categories. Optionally compute an MQM-style error-density sub-score for the language dimension so that one dimension has a defensible, literature-backed number.

### P2 — Evidence & rigor

- **Add a live evidence-capture mode.** You already ship Playwright for PDF export — reuse it (or Claude's Browser Use) to capture rendered pages, key states, and screenshots, then do multimodal analysis so Level-2/3 findings are grounded in what the UI actually does. Record the captured evidence reference on each finding.

- **Build a calibration set + a critic pass.** Create a handful of expert-scored example audits with per-dimension anchored scores; document an inter-rater method (mirroring MQM's multi-annotator averaging); and add a second-pass "review findings for evidence-grounding and overreach, and re-check the score" step before the report renders.

- **Add an `evals/` suite** using the official skill-creator eval framework: triggering tests (does it fire on "make this ready for Germany" but not on unrelated prompts?), golden audit outputs for a couple of fixtures, and unit tests that pin the scorer's edge cases (Critical caps, null renormalization, band boundaries) you already verified manually.

### P3 — Depth & distribution

- **Deepen the playbooks.** Segment by country / industry / audience, add source provenance and version stamps to each rule, and expand beyond four corridors. Add a "local category norms / competitor reference" comparison step so the audit can say how the product reads *against local peers*, not just against itself.

- **Add audit-version comparison.** A script that diffs two audit JSONs and shows score and finding deltas — this operationalizes the re-audit loop your spec already recommends and turns the score's main legitimate use (tracking iterations) into a feature.

- **Polish the repo for GitHub & discoverability.** Add CHANGELOG, CONTRIBUTING, `.github/` issue & PR templates, a version badge, and an embedded sample report (HTML/PDF) in the README; index on skills.sh; and package as a Claude Code plugin with a one-line install. Optionally offer a modular split (core audit + optional dimension add-ons) the way `mastepanoski` ships a suite — while keeping the single end-to-end workflow as the default.

- **Add issue-tracker export** (Jira / Linear) alongside the existing CSV backlog, so the backlog lands where teams actually work.

---

## 7. Quick wins vs. strategic bets

**Quick wins (a day or less each, mostly writing):**
- Framework cross-walk reference + citing standards in findings.
- Accessibility dimension + EAA escalation flag.
- Scorer unit tests + a triggering eval.
- Repo polish (CHANGELOG, CONTRIBUTING, badges, demo report in README).

**Strategic bets (worth scoping deliberately):**
- Live evidence capture / multimodal analysis (removes the biggest honesty limit).
- MQM-grounded language scoring + calibration set + critic pass (raises reliability and defensibility together).
- Playbook depth with provenance and the local-category benchmark (where the long-term moat is).

**The single highest-leverage move:** the **framework cross-walk + accessibility dimension**. It's mostly documentation, it directly closes the one axis where your strongest competitor beats you, and it converts an enterprise buyer's "says who?" into "per NIST AI RMF / WCAG / MQM." Everything else compounds on top of that credibility.

---

## 8. Sources

Ecosystem & official catalog
- Awesome Claude Skills directory — https://awesomeclaude.ai/awesome-claude-skills
- AI agent skills marketplaces overview (2026) — https://www.agensi.io/learn/best-ai-agent-skills-marketplaces-2026
- Anthropic official skills repo — https://github.com/anthropics/skills
- Anthropic official skills walkthrough (17 skills) — https://claudecn.com/en/blog/claude-official-skills-walkthrough/

Comparable skills
- mastepanoski/claude-skills (UX + AI governance suite) — https://github.com/mastepanoski/claude-skills
- appariciojunior/website-audit-skill — https://github.com/appariciojunior/website-audit-skill
- daymade/claude-code-skills (product-analysis) — https://github.com/daymade/claude-code-skills
- yoyothesheep/claude-skills (AEO/SEO audit) — https://github.com/yoyothesheep/claude-skills

Methodology grounding
- NIST AI RMF (via mastepanoski skill description: Govern/Map/Measure/Manage + 7 trustworthiness characteristics) — https://github.com/mastepanoski/claude-skills
- MQM framework overview — https://www.emergentmind.com/topics/multidimensional-quality-metrics-mqm
- MQM scoring models & statistical quality control (10th-anniversary paper) — https://arxiv.org/pdf/2405.16969
- MQM-Chat (conversational variant, COLING 2025) — https://aclanthology.org/2025.coling-main.221/

Accessibility law (for the EU corridor)
- European Accessibility Act enforceable 28 June 2025; EN 301 549 / WCAG 2.1 AA — https://www.levelaccess.com/blog/eu-accessibility-requirements-and-eaa-compliance/
- EN 301 549 standard detail and penalties — https://userway.org/compliance/en/
- EAA enforcement & scope (applies to non-EU sellers; automated tools catch 30–40%) — https://www.accessibility.works/european-accessibility-act/
