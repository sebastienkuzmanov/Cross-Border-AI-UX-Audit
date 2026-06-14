# The Eight Audit Dimensions

Findings are organized across eight dimensions. For each material/flow, evaluate it against general AI-UX principles, the target-market playbook, the business goal, and the target audience. Every finding is tagged with exactly one dimension (its primary category).

The canonical dimension keys (used in the JSON schema and scoring) are:
`language_naturalness`, `cultural_fit`, `trust_and_privacy`, `ai_expectation_setting`, `ux_clarity`, `conversion`, `agent_chatbot_behavior`, `accessibility`, `market_entry_risk`.

Each dimension is grounded in named external standards — see `framework_crosswalk.md`, and add the relevant `standard_refs` to every finding so it cites an authority rather than a bespoke rubric.

---

## 1. Language Naturalness (`language_naturalness`)
Does the language feel **native to the product category and target audience**, not merely correct?

Evaluate: natural phrasing; terminology and category conventions; tone and formality; clarity and specificity; consistency; idioms and metaphors; borrowed vs. translated product terms; script and spelling conventions; whether copy sounds like a translated source-market product.

- **Typical problem:** "Our intelligent platform lets you go global instantly."
- **Why it matters:** Broad, translated AI-benefit language can make a credible product feel immature or untrustworthy.
- **Typical recommendation:** Name the workflow, input, output, user control, and limitation using target-market-native product language.

## 2. Cultural Fit (`cultural_fit`)
Do the product's framing, assumptions, examples, interactions, and promises fit the target market?

Evaluate: local business expectations; buyer motivation; decision-making style; support expectations; appropriate use of social proof; regional sensitivity; local scenarios; acceptable information density; whether a diverse region is treated as one uniform culture.

- **Typical problem:** "Go global instantly" minimizes the real adaptation effort experienced buyers expect.
- **Why it matters:** Mismatched framing reads as naïve to local buyers and erodes credibility.
- **Typical recommendation:** Position the product as making adaptation faster, clearer, and more controlled — not as eliminating local strategy.

## 3. Trust & Privacy (`trust_and_privacy`)
Do users get enough information to trust the product **before** sharing data or relying on AI output?

Evaluate: company identity and accountability; support/contact paths; data use; model-training policy; data storage and hosting; retention and deletion; third-party model providers; permissions and auditability; consent; data transfer; expert-review requirements for sensitive workflows.

- **Typical problem:** An upload flow says "Let AI optimize everything automatically," without explaining what happens to the uploaded content.
- **Why it matters:** AI raises the trust threshold; cross-border use raises it further (company, hosting, support, data handling, local relevance).
- **Typical recommendation:** Place a compact trust panel at the upload decision point covering data use, storage, training, retention, deletion, and review requirements.

## 4. AI Expectation-Setting (`ai_expectation_setting`)
Does the product accurately communicate AI capability, limitations, uncertainty, and control?

Evaluate: autonomy claims; accuracy/reliability claims; distinction between copilot, agent, automation, and analytics; human review; uncertainty/confidence; citations or evidence where relevant; failure modes; fallback paths; user responsibility.

- **Typical problem:** "The AI agent handles the entire workflow for you."
- **Why it matters:** Cross-border buyers are often especially cautious about delegating decisions to an unfamiliar AI provider; absolute autonomy claims create an expectation/behavior mismatch.
- **Typical recommendation:** Explain that the agent drafts, flags, routes, or prepares work, while users approve defined decisions and can intervene.

## 5. UX Clarity (`ux_clarity`)
Do users understand where they are, what to do, what will happen, and how to recover?

Evaluate: navigation; onboarding sequence; action labels; input requirements; expected outputs; time/effort expectations; error states; empty states; settings/control surfaces; progress/status; recovery paths.

- **Typical problem:** A call to action that says only "Start now."
- **Why it matters:** Unclear actions and missing recovery states stall onboarding and increase support burden.
- **Typical recommendation:** Use action-specific labels such as "Run market-fit audit" or "Generate localized review," and design explicit error/empty/recovery states.

## 6. Conversion (`conversion`)
Does the product give target-market users credible reasons and low-friction paths to take the next commercial action?

Evaluate: positioning; value proposition; audience segmentation; product proof; local examples/testimonials; pricing clarity; trial/demo expectations; calls to action; sales handoff; alignment between the user's risk and the requested commitment.

- **Typical problem:** "Contact us for more information."
- **Why it matters:** Generic CTAs and missing local proof waste strong traffic and depress conversion.
- **Typical recommendation:** Offer a concrete outcome — a diagnostic review, sample audit, scoped pilot, or implementation discussion.

## 7. Agent & Chatbot Behavior (`agent_chatbot_behavior`)
Does the conversational AI behave appropriately for the target market and use case?

Evaluate: role and scope; conversational tone; overclaiming; refusals; escalation; human handoff; clarification behavior; user correction; memory/personalization expectations; high-stakes boundaries; whether the assistant distinguishes product guidance from legal/professional advice.

- **Typical problem:** "I can answer anything about your market launch."
- **Why it matters:** Overclaiming and missing escalation paths create reputational and trust risk, especially with an unfamiliar provider.
- **Typical recommendation:** State the assistant's scope, identify sensitive areas, and offer to prepare a note for qualified expert review.

## 8. Accessibility (`accessibility`)
Can people with disabilities perceive, operate, and understand the experience — and does it meet the accessibility bar legally required in the target market?

Evaluate (against **WCAG 2.1 AA** / **EN 301 549** / **ADA / Section 508**, organized by the POUR principles): text and non-text contrast; text alternatives for images and icons; keyboard operability and focus order; visible focus; accessible names/roles/values for controls; form labels and error identification; headings and landmarks; motion and timing controls; language-of-page; and target sizes. Note script/RTL handling for the target market.

- **Typical problem:** Light-grey CTA text on white plus icon-only buttons with no labels (fails 1.4.3 Contrast and 4.1.2 Name/Role/Value).
- **Why it matters:** Beyond excluding users, accessibility is **legally required** in several corridors — the EU's European Accessibility Act has been enforceable since 28 June 2025 and applies to any business serving EU consumers (EN 301 549 / WCAG 2.1 AA), and the US ADA/Section 508 apply elsewhere. Automated tools catch only ~30-40% of barriers.
- **Typical recommendation:** Raise contrast to >=4.5:1, add accessible names to icon-only controls, ensure full keyboard operability, and run a WCAG 2.1 AA pass with assistive technology. **Always add an `expert_review_flags` entry** for a full conformance audit — the audit grounds the finding in WCAG; it does not certify compliance. Weight this dimension up for EU-facing corridors via the `eu_eaa` scoring profile.

## 9. Market-Entry Risk (`market_entry_risk`)
What could weaken or block a launch **beyond** a single screen or message?

Evaluate: unsupported universal-market claims; missing local deployment/support explanations; local ecosystem fit; script and language variants; sensitive sectors; data-transfer concerns; region-specific proof; credibility of the market-entry story; areas needing further local research or expert review.

- **Typical problem:** "Built for every market."
- **Why it matters:** Universal claims without local substance undermine the entire market-entry story.
- **Typical recommendation:** Name supported market corridors, configurations, proof, and limitations.
