# Triggering Tests

Prompts the skill **should** fire on, and prompts it should **not**. Use these to check the `description` triggers correctly (and to catch regressions when the description changes). With the skill installed, run each prompt in a fresh session and confirm the skill does / does not activate.

## Should trigger (positive)
- "Is our AI agent ready to launch in the US self-serve SaaS market?"
- "Audit our chatbot's onboarding for the China inbound market."
- "Why is our localized landing page converting badly in Russia/CIS?"
- "Make this product copy trust-ready for EU buyers."
- "Run a cross-border AI UX audit on these materials."
- "Localization review of our pricing page for Brazil — is it market-ready?"
- "We're entering the Gulf market with our voice assistant; review the UX and trust."
- "Check our AI app for accessibility and market fit before the EU launch." (should also exercise the accessibility dimension + `eu_eaa` profile)
- "Transcreation + market-readiness review for our agent going from China to English-global."
- "We localized into German but enterprise pilots stall — what's wrong with the experience?"

## Should NOT trigger (negative)
- "Translate this paragraph into Spanish." (pure translation, no product/market readiness)
- "Fix the grammar in this email." (proofreading)
- "Write unit tests for this Python function." (unrelated)
- "Review my React component for bugs." (code review, not market UX)
- "Is this contract legally compliant in Germany?" (legal opinion — out of scope; the skill escalates, doesn't opine)
- "Run a penetration test on our API." (security testing — out of scope)
- "Benchmark our model's accuracy against GPT-4." (model evaluation — out of scope)

## Edge cases (judgment)
- "Improve our website copy." → may trigger only if a target market / cross-border intent is present; otherwise a general copy task. The skill should ask intake to establish the corridor.
- "Audit our website." → ambiguous; the skill should clarify whether this is a cross-border/market-readiness audit (this skill) vs. a generic site audit.

## What to check when it triggers
1. It asks the **intake** question set before auditing.
2. It anchors to a **market corridor**, not just a language.
3. Findings are **evidence-grounded**, cite **standards** (`standard_refs`), and include the **accessibility** dimension where relevant.
4. The **score** is computed by the script (with the right weight profile), not hand-written.
5. Compliance/legal/accessibility items are **escalated** to expert review.
6. The report is **bilingual** (EN + 中文) unless the user restricted languages.
