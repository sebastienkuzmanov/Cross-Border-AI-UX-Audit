# Intake & Market Corridor

Read this first for any new audit. It covers the decision framing (Step 1), the market corridor (Step 2), the compact intake question set (Step 3), when an audit is most valuable, and evidence-collection guidance.

## Step 1 — Define the decision

Every audit must begin with a concrete business decision. Without one, the audit becomes a long list of observations with no implementation value. Pin one of these (or an equivalent):

- Is the product ready for a pilot in the target market?
- Which issues must be fixed before launch?
- Why is localized conversion weak despite traffic?
- What should be rewritten **before** translating the full product?
- Which trust and AI-boundary issues could block enterprise adoption?

Record the decision verbatim; it drives prioritization later (a finding only matters insofar as it affects this decision).

## Step 2 — Define the market corridor

The unit of analysis is a **market corridor**, never a generic language. A corridor connects:

- **Source market** — where the product originates (e.g., China, Russia/CIS, Balkan/EU, English-speaking global, Other).
- **Target market** — where it's entering (e.g., Russian/CIS, Balkan/EU, English-speaking global, China inbound, Other).
- **Target audience** — the specific buyer/user (e.g., B2B technical buyer, self-serve prosumer, enterprise procurement, educators).
- **Product category** — chatbot, agent, AI SaaS, AI education app, AI productivity tool, voice AI, multimodal, other.
- **Business goal** — e.g., self-serve trial conversion vs. enterprise pilot readiness (these demand different audits).
- **Materials / flows under review** — the concrete artifacts supplied.

Then select or create the matching playbook (see `market_playbooks.md`). The same product in a China→Russia/CIS B2B corridor needs different positioning, proof, interaction patterns, trust explanations, and language than the same product in a China→English-speaking self-serve SaaS corridor.

## Step 3 — Intake questions (ask before auditing)

Ask this compact set first. Do not start the audit until the user answers or explicitly says to proceed with assumptions.

Full set:
1. **Decision** — What business decision should this audit support (pilot-ready, pre-launch fixes, weak conversion, pre-translation rewrite, enterprise trust)?
2. **Corridor** — Source market → target market? Who exactly is the target audience and in what scenario do they use the product?
3. **Product** — What type of AI product is it, and what does the AI actually do (input → AI processing → output / action)?
4. **Business goal** — Self-serve conversion, enterprise pilot, retention, something else?
5. **Materials** — Which materials can you share (landing copy, onboarding flow, chatbot transcript, agent prompt+response, app-store listing, pricing page, trust/safety copy, screenshots/notes, other)?
6. **Known concerns** — Any trust, privacy, conversion, or AI-behavior problems you already suspect?
7. **Languages** — Report in English + 中文 (default), or restrict to one?

Quick version (paste-and-fill):
```
1. Decision:
2. Corridor (source -> target):
3. Target audience / scenario:
4. Product type + what the AI does:
5. Business goal:
6. Materials attached:
7. Report languages (default: EN + 中文):
```

If the user says "just proceed," infer carefully and write **every** inference into the report's evidence/limitations section as an explicit assumption.

## When an audit is most valuable (engagement moments)

- Before entering a new market; before an enterprise pilot; before translating the full product.
- After weak conversion in a localized market; after users express trust/privacy concerns.
- When an AI agent's role or autonomy is unclear; before a major onboarding redesign; before launching a new chatbot/agent workflow.
- After local user research, to translate findings into implementation tasks.

## Evidence collection guidance

Gather the highest-value materials first and **record what was reviewed and what was not available** — the report must state its evidence base and avoid conclusions that exceed it. See `evidence_and_inputs.md` for supported material types and the three evidence levels. The quality and breadth of evidence directly bound the quality of the audit.
