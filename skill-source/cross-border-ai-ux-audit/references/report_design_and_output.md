# Report Design & Output

This reference defines the bilingual output contract, the visual design system for the HTML/PDF report, and the export formats. The default renderers (`render_html_report.py`, `render_markdown_report.py`) already implement this; read this when adjusting layout or producing the report manually.

## Bilingual output contract (EN + 中文)

- **Default:** every analytical text field is produced in **both English and Chinese** (`{en, zh}`). The HTML report shows an **EN / 中文 toggle** that switches all `.lang-en` / `.lang-zh` content; the Markdown report renders both languages per field (English first, then 中文).
- **Rewrites (`rewritten_version`)** are written in the **target market's language** by default, because that copy is the actual implementable deliverable. Record `rewritten_version_language`. For a China-inbound corridor the rewrite is in Chinese; for an English-global corridor it is in English; for Russian/CIS or Balkan/EU, in the appropriate local language (note script/variant).
- **Evidence (`original_text`)** is shown verbatim in its original language; never translate the evidence inside the evidence field (a translation may be added as a labeled aside if helpful).
- If the user restricts languages (e.g., "English only"), honor it: set `meta.report_languages` accordingly and the renderers emit a single-language report.

## Visual design system

Direction: a **market-readiness dossier** — precise, editorial, evidence-heavy; more refined than a plain academic PDF, calmer than a marketing deck. The severity scale carries the only strong color; everything else stays disciplined.

Tokens (already encoded in the template):
- **Palette:** ink `#16202C` (text/headers), paper `#FBFAF7` (background), corridor accent `#2F6F6A` (deep teal, used sparingly for the score arc, links, section markers), hairline `#E2DDD3`.
- **Severity colors (functional, not decorative):** Critical `#B23A3A`, High `#C2722B`, Medium `#3E6E8E`, Low `#7C8579`.
- **Type:** a strong humanist/grotesk sans for headings and data, a readable serif or sans for body; clear type scale; generous leading for the body, tighter tracking for labels/eyebrows. (System-font stacks are used so the report renders without web-font fetches.)
- **Structure:** numbered section eyebrows are appropriate here because the report *is* an ordered sequence. Severity badges, a corridor line (source → target), and a before→after paired block are the signature elements.
- **Quality floor:** responsive down to mobile, visible keyboard focus on the toggle, `prefers-reduced-motion` respected, prints cleanly to PDF (page breaks avoided inside issue cards).

## Report structure (rendered)
Header: title **Cross-Border AI UX Audit / 跨境 AI 用户体验审计**, the corridor line (source → target · audience · product type), audit date/version, and the EN / 中文 toggle.
Then the ten sections in order (see `finding_and_report_schema.md`): executive summary; corridor & evidence; market-fit score (with a clear "how to read / not read" caption); top risks; findings by dimension as severity-coded cards (each showing evidence → problem → why it matters → recommendation → rewrite → target-market note); before/after rewrites; the priority backlog as a table; expert-review flags; next steps & re-audit loop; limitations.

## Export formats
- **HTML** — the primary, designed report (self-contained, no external fetches).
- **PDF** — via `scripts/html_to_pdf.py` (Playwright/Chromium). If the conversion fails or tooling is absent, **still deliver the HTML** and state the PDF was blocked and why.
- **CSV** — the priority backlog via `scripts/export_backlog_csv.py`.
- **Markdown** — via `scripts/render_markdown_report.py`, for easy copy/paste.
- **Chat summary** — overall readiness, top 3 risks, the score (with caveat), and the file paths.

Recommended output paths:
```
reports/cross_border_ai_ux_audit_<slug>_<YYYYMMDD>.html
reports/cross_border_ai_ux_audit_<slug>_<YYYYMMDD>.pdf
reports/cross_border_ai_ux_audit_<slug>_<YYYYMMDD>_backlog.csv
reports/cross_border_ai_ux_audit_<slug>_<YYYYMMDD>.md
```

## Standards citations & accessibility in the report
- Findings may carry `standard_refs` (e.g. NIST AI RMF, MQM, WCAG criteria); the HTML renderer shows them as small citation **chips** under each issue and the Markdown renderer as a **Standards:** line. This is the visible payoff of the framework cross-walk — keep them specific.
- The report includes the ninth dimension, **Accessibility / 无障碍可达性**, in the score bars and as severity-coded findings; accessibility findings should also appear in the Expert-Review Flags section.
- Findings grounded in captured evidence show the captured artifact reference (e.g. `pricing.png`) next to the evidence grounding.
- New export scripts: `export_issue_tracker.py` (Jira / Linear CSV) alongside `export_backlog_csv.py`, and `compare_audits.py` to diff two audit versions for the re-audit loop.
