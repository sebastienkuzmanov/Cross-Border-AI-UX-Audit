# Framework Cross-Walk

This reference grounds the audit's dimensions in **named, external standards** so findings can cite an authority instead of resting on a bespoke methodology. When writing a finding, add the relevant standard references to the issue's `standard_refs` array (they render as citation chips in the report). This is the single highest-leverage credibility lever for the skill.

**Important:** citing a standard means "this finding is grounded in the named framework's concept," **not** that the audit certifies compliance. Compliance conclusions are always escalated to qualified experts (see `limitations_and_safety.md`).

## Dimension → standard map

| Dimension | Primary standards to cite | Example `standard_refs` entries |
|---|---|---|
| `ux_clarity` | Nielsen's 10 usability heuristics; Norman's principles (discoverability, affordances, signifiers, feedback, mapping, constraints, conceptual models) | `"Nielsen #1: Visibility of system status"`, `"Norman: Affordances"` |
| `trust_and_privacy` | NIST AI RMF trustworthiness characteristics (Privacy-Enhanced, Secure & Resilient, Accountable & Transparent); ISO/IEC 42001 (AI management system: data governance, transparency) | `"NIST AI RMF: Privacy-Enhanced"`, `"ISO 42001: data governance"` |
| `ai_expectation_setting` | NIST AI RMF (Valid & Reliable, Explainable & Interpretable, Accountable & Transparent); ISO/IEC 42001 (impact assessment, human oversight) | `"NIST AI RMF: Explainable & Interpretable"` |
| `agent_chatbot_behavior` | NIST AI RMF (Safe, Accountable & Transparent); OWASP LLM Top 10 (Excessive Agency) — cite as a *boundary flag*, not a security test | `"NIST AI RMF: Safe"`, `"OWASP LLM: Excessive Agency (flag)"` |
| `language_naturalness` | MQM (Multidimensional Quality Metrics) error typology + severity; MQM-Chat for conversational surfaces | `"MQM: Terminology"`, `"MQM-Chat: buzzword/loanword"` |
| `accessibility` | WCAG 2.1 AA success criteria; EN 301 549 (EU harmonized standard); ADA / Section 508 (US) | `"WCAG 2.1 AA: 1.4.3 Contrast"`, `"EN 301 549"` |
| `cultural_fit` | No single formal standard; ground in the target-market playbook and Hofstede-style dimensions only as hypotheses, never as cultural absolutes | `"Playbook: english_global"` |
| `conversion` | No formal standard; cite the playbook and, where a usability cause applies, the relevant Nielsen heuristic | `"Nielsen #2: Match between system and the real world"` |
| `market_entry_risk` | No formal standard; ground in the playbook and escalate regulated/legal items | `"Playbook governance"` |

## The standards, in brief

### Nielsen's 10 usability heuristics (for `ux_clarity`, sometimes `conversion`)
Visibility of system status; match between system and the real world; user control and freedom; consistency and standards; error prevention; recognition rather than recall; flexibility and efficiency of use; aesthetic and minimalist design; help users recognize, diagnose, and recover from errors; help and documentation. Norman's principles complement these for intuitiveness (discoverability, affordances, signifiers, feedback, mapping, constraints, conceptual models).

### NIST AI RMF 1.0 trustworthiness characteristics (for the AI-specific dimensions)
The seven characteristics: **Valid & Reliable, Safe, Secure & Resilient, Accountable & Transparent, Explainable & Interpretable, Privacy-Enhanced, Fair (with harmful bias managed).** The RMF's four functions (Govern, Map, Measure, Manage) describe the lifecycle; for an audit, cite the *characteristic* a finding implicates. Generative-AI specifics live in NIST AI 600-1.

### ISO/IEC 42001 (AI management system)
Use for governance-flavored trust/AI findings: data governance, impact assessment, transparency & explainability, human oversight, and regulatory alignment (e.g. EU AI Act, GDPR). Cite the theme, not a clause number, unless certain.

### MQM and MQM-Chat (for `language_naturalness`)
MQM is the field-standard analytic typology for translation/localization quality (EU QTLaunchPad origin; used as the gold standard in WMT shared tasks; heading toward ISO standardization). It pairs a hierarchical **error typology** with **severity** (minor / major / critical) and a **scoring model**. Common top-level error categories to cite: **Terminology, Accuracy/Mistranslation, Fluency (grammar, spelling, register), Style/awkward, Locale convention, Audience appropriateness.** For chatbot/agent surfaces, **MQM-Chat (2025)** adds conversational categories: **ambiguity/disambiguation, buzzword/loanword issues, dialogue inconsistency.** LLM-automated MQM (AutoMQM, GEMBA-MQM) is precedent that an LLM applying this typology with severity is a validated pattern. Use `scripts/mqm_language_score.py` to turn a labeled error list into an MQM-style error-density sub-score for the language dimension.

### WCAG 2.1 AA / EN 301 549 / ADA (for `accessibility`)
WCAG organizes criteria under four **POUR** principles — Perceivable, Operable, Understandable, Robust — at conformance levels A / AA / AAA. **AA is the operative bar.** In the EU, **EN 301 549** is the harmonized standard (currently incorporating WCAG 2.1 AA; v4.x will move to WCAG 2.2), and conformance supports the **European Accessibility Act (enforceable 28 June 2025)**, which applies to any business serving EU consumers. In the US, ADA / Section 508 apply. Cite the specific success criterion when known (e.g. 1.4.3 Contrast, 4.1.2 Name/Role/Value, 2.1.1 Keyboard, 1.1.1 Non-text Content). Automated checks catch only ~30-40% of barriers, so accessibility findings should usually carry an expert-review flag for a full conformance audit.

### OWASP LLM Top 10 (boundary flags only)
The audit is **not** a security test. But when agent behavior touches a security-relevant boundary (e.g. an assistant that will act on untrusted input → Excessive Agency / Prompt Injection), cite it as a *flag* and route to security review. Do not attempt exploitation or a security verdict.

## How to apply in a finding
1. Identify the dimension.
2. Pick the most specific standard concept the evidence implicates.
3. Add 1-3 `standard_refs` entries (specific criterion > general principle).
4. If the standard is a compliance/legal one (WCAG/EN 301 549/ISO/AI Act), also add an `expert_review_flags` entry — the audit grounds the finding; it does not certify.
