# Market Playbooks

A playbook is the **context layer** used to evaluate the product against a target market's expectations. It prevents the audit from applying one generic definition of "good UX" to every market. Select the playbook that matches the corridor's target market; if none fits, create a working playbook for the corridor and label it provisional.

Each playbook contains editable rules for: tone; trust expectations; privacy expectations; AI-claim sensitivity; UX preferences; localization warnings; common mistakes; and recommended copy style. **Playbooks are working hypotheses, not cultural truths** — see Governance at the end.

---

## Russian / CIS (`russian_cis`)
Emphasize:
- direct, specific, technically credible language;
- proof of reliability, ownership, and support;
- early security, deployment, and data-handling detail;
- measured AI claims (skepticism toward hype);
- visible settings, limits, and control surfaces;
- consistency in formal/informal address;
- concrete verbs and explicit workflow descriptions.

Watch for: vague benefit language; hidden or late privacy/security info; overstated autonomy; missing ownership/support proof.

## Balkan / EU (`balkan_eu`)
Emphasize:
- professional, human, locally respectful language;
- transparency, local relevance, and accessible support;
- GDPR-adjacent privacy expectations;
- **accessibility as a legal baseline** — WCAG 2.1 AA / EN 301 549 under the European Accessibility Act (enforceable 2025-06-28); use the `eu_eaa` scoring profile and flag conformance for expert review;
- human oversight in sensitive use cases;
- visible pricing and low-friction contact;
- language and script differences **within** the region;
- avoidance of political, national, or regional assumptions.

Watch for: treating the region as uniform; privacy hand-waving; political/national insensitivity; opaque pricing.

## English-Speaking Global (`english_global`)
Emphasize:
- concise, outcome-led language;
- visible product evidence;
- security, integrations, use cases, and credible proof;
- explicit model-training, retention, and provider handling;
- clear distinctions between AI capability types (copilot vs. agent vs. automation vs. analytics);
- confidence, citations, or reasoning where relevant;
- transparent pricing and strong onboarding examples;
- workflow-first rather than AI-first positioning.

Watch for: AI-first hype over workflow value; missing provider/retention disclosure; capability-type confusion; weak proof.

## China Inbound (`china_inbound`)
Emphasize:
- practical, credible, partnership-oriented positioning;
- business value, implementation detail, and local support;
- deployment, hosting, model-provider, and data-localization explanations;
- productivity and workflow-efficiency framing;
- rapid contact and implementation-discussion paths;
- category language aligned with Chinese AI and SaaS conventions;
- local scenarios, ecosystem fit, and enterprise trust detail.

Watch for: foreign-sounding category terms; missing localization/hosting story; slow or unclear contact path; weak enterprise trust signals.

---

## Latin America / LATAM (`latam`)
*Working hypothesis — validate per country (e.g. Mexico, Brazil, Argentina, Colombia) and segment; Brazil is Portuguese, most of the region is Spanish with strong national variants.*
Emphasize:
- warm, relationship-oriented but professional language; avoid stiff machine-translated register;
- correct national variant and script conventions (PT-BR vs PT-PT; regional Spanish vocabulary);
- local payment, pricing, and billing realities; mobile-first experiences;
- WhatsApp/contact-channel expectations and responsive human support;
- trust signals adapted to local buyers; clear data-handling given LGPD (Brazil) and similar laws;
- concrete local examples over global/US-centric proof.

Watch for: treating LATAM as one market; European Portuguese/Spanish used for the Americas; US-only proof and payment assumptions; ignoring LGPD-style obligations (flag for expert review).

## Middle East & Gulf / MENA (`mena_gulf`)
*Working hypothesis — validate per market (e.g. UAE, KSA, Egypt) and segment; Arabic is RTL with significant dialect/register variation; English is common in Gulf B2B.*
Emphasize:
- right-to-left (RTL) layout correctness and bidirectional text handling;
- Modern Standard Arabic for formal product copy, with attention to local register;
- partnership-oriented, relationship-led B2B positioning; local presence and support signals;
- data-localization and hosting expectations; sensitivity to local norms and content;
- clear, credible enterprise trust and implementation paths.

Watch for: broken RTL/mirroring; machine-translated Arabic; cultural insensitivity; assuming a single "Arab market"; missing data-residency story (flag for expert review).

## Playbook Governance

Playbooks should **not** be treated as permanent cultural truths. They are working hypotheses and operating guidance that should be:
- reviewed by local practitioners;
- updated with user research and sales evidence;
- segmented by country, audience, industry, and product category;
- versioned over time; and
- checked for stereotypes or overgeneralization.

When applying a playbook in a finding, attribute the rationale to the playbook and, where the rule is an untested assumption, say so and recommend local validation. Never present a playbook rule as an absolute fact about a people or nation.

### Provenance, versioning & segmentation (required for production use)
Each playbook rule should carry, where possible:
- **Provenance** — what the rule is based on (local practitioner input, user research, sales evidence, or "assumption pending validation"). Label unvalidated rules explicitly.
- **Version & date** — stamp the playbook (e.g. `english_global v1.2, 2026-06`) so audits can be compared on a consistent context layer; record changes in `CHANGELOG.md`.
- **Segmentation** — refine by country, industry, audience, and product category. "Russian/CIS" or "LATAM" is a starting region, not a single market; split when evidence justifies (e.g. enterprise vs self-serve, fintech vs edtech).

### Accessibility by corridor
Treat WCAG 2.1 AA as the floor everywhere. It is a **legal** baseline for EU-facing corridors (EN 301 549 / EAA) and US corridors (ADA / Section 508) — use the `eu_eaa` weight profile for EU consumers and always flag conformance for expert review. For RTL markets (MENA/Gulf), include RTL/bidi correctness in accessibility checks.

### Local category-norm / competitor reference (optional evidence step)
Cross-border buyers judge a product against **local peers**, not only against itself. When materials allow, add a light competitor/category reference: name 1-3 local category norms (how comparable products in the target market position, price, explain trust, and handle AI claims) and note where the product diverges. Keep it evidence-based and avoid naming competitors disparagingly; frame divergences as risks or opportunities, not verdicts.
