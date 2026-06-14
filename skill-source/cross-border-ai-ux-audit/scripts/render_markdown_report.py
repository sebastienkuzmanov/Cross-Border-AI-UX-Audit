#!/usr/bin/env python3
"""
render_markdown_report.py — Render the canonical audit JSON into a bilingual
(English + 中文) Markdown report.

Usage:
  python render_markdown_report.py audit.json -o report.md
  python render_markdown_report.py audit.json            # prints to stdout
"""
import argparse
import json
import sys

DIM_LABELS = {
    "language_naturalness": ("Language Naturalness", "语言自然度"),
    "cultural_fit": ("Cultural Fit", "文化契合度"),
    "trust_and_privacy": ("Trust & Privacy", "信任与隐私"),
    "ai_expectation_setting": ("AI Expectation-Setting", "AI 预期设定"),
    "ux_clarity": ("UX Clarity", "体验清晰度"),
    "accessibility": ("Accessibility", "无障碍可达性"),
    "conversion": ("Conversion", "转化"),
    "agent_chatbot_behavior": ("Agent & Chatbot Behavior", "智能体/对话行为"),
    "market_entry_risk": ("Market-Entry Risk", "市场进入风险"),
}


def langs_in(meta):
    return meta.get("report_languages", ["en", "zh"])


def bi(field, langs, sep="  \n"):
    """Render a {en, zh} field (or plain string) for the active languages."""
    if field is None:
        return ""
    if isinstance(field, str):
        return field
    parts = []
    if "en" in langs and field.get("en"):
        parts.append(field["en"])
    if "zh" in langs and field.get("zh"):
        zh = field["zh"]
        parts.append(zh if ("en" not in langs) else f"中文：{zh}")
    return sep.join(parts)


def render(audit):
    meta = audit.get("meta", {})
    langs = langs_in(meta)
    L = []

    title = "Cross-Border AI UX Audit"
    if "zh" in langs:
        title += " / 跨境 AI 用户体验审计"
    L.append(f"# {title}\n")

    corridor = f"{meta.get('source_market','?')} → {meta.get('target_market','?')}"
    L.append(f"**Corridor:** {corridor}  ")
    if meta.get("target_audience"):
        L.append(f"**Audience:** {meta['target_audience']}  ")
    if meta.get("product"):
        L.append(f"**Product:** {meta['product']} ({meta.get('product_type','')})  ")
    if meta.get("business_goal"):
        L.append(f"**Business goal:** {meta['business_goal']}  ")
    if meta.get("playbook"):
        L.append(f"**Playbook:** {meta['playbook']}  ")
    L.append(f"**Audit date / version:** {meta.get('audit_date','')} · v{meta.get('audit_version',1)}\n")

    # 1. Executive summary
    L.append("## 1. Executive Summary / 概要")
    L.append(bi(audit.get("executive_summary"), langs) + "\n")

    # 2. Corridor & evidence
    L.append("## 2. Market Corridor & Evidence Reviewed / 市场走廊与证据")
    rev = ", ".join(meta.get("evidence_reviewed", [])) or "—"
    na = ", ".join(meta.get("evidence_not_available", [])) or "—"
    L.append(f"- **Evidence reviewed:** {rev}")
    L.append(f"- **Not available:** {na}")
    L.append(f"- **Evidence level:** {meta.get('evidence_level','?')}")
    if meta.get("assumptions"):
        L.append(f"- **Assumptions:** {'; '.join(meta['assumptions'])}")
    L.append("")

    # 3. Market-fit score
    mfs = audit.get("market_fit_score", {})
    L.append("## 3. Market-Fit Score / 市场契合度评分")
    L.append(f"**{mfs.get('overall','?')} / 100** — {mfs.get('band','')}  ")
    L.append(f"Confidence: {mfs.get('confidence','?')} · "
             f"Evidence completeness: {mfs.get('evidence_completeness','?')} · "
             f"Unresolved Critical: {mfs.get('unresolved_critical_count',0)}\n")
    ds = mfs.get("dimension_scores", {})
    if ds:
        L.append("| Dimension | Score |")
        L.append("| --- | --- |")
        for k, (en, zh) in DIM_LABELS.items():
            v = ds.get(k)
            label = f"{en} / {zh}" if "zh" in langs else en
            L.append(f"| {label} | {'—' if v is None else v} |")
        L.append("")
    if mfs.get("score_explanation"):
        L.append(bi(mfs.get("score_explanation"), langs) + "\n")
    L.append("> The score is a heuristic summary for comparing iterations of the same "
             "product and corridor. It is **not** a certification, a legal/compliance "
             "rating, or a guarantee of market fit. Prioritize the findings over the number.\n")

    # 4. Top risks
    L.append("## 4. Top Risks / 主要风险")
    for i, r in enumerate(audit.get("top_risks", []), 1):
        L.append(f"{i}. {bi(r, langs, sep=' — ')}")
    L.append("")

    # 5. Findings by dimension
    L.append("## 5. Findings by Dimension / 分维度发现")
    for issue in audit.get("issues", []):
        cat = issue.get("category", "")
        en, zh = DIM_LABELS.get(cat, (cat, cat))
        cat_label = f"{en} / {zh}" if "zh" in langs else en
        L.append(f"### [{issue.get('severity','')}] {cat_label} — {issue.get('id','')}")
        if issue.get("original_text"):
            L.append(f"> **Evidence:** {issue['original_text']}")
        L.append(f"- **Problem:** {bi(issue.get('problem'), langs)}")
        L.append(f"- **Why it matters:** {bi(issue.get('why_it_matters'), langs)}")
        L.append(f"- **Recommendation:** {bi(issue.get('recommendation'), langs)}")
        if issue.get("rewritten_version"):
            rl = issue.get("rewritten_version_language", "")
            L.append(f"- **Rewrite ({rl}):** {issue['rewritten_version']}")
        if issue.get("target_market_note"):
            L.append(f"- **Target-market note:** {bi(issue.get('target_market_note'), langs)}")
        if issue.get("standard_refs"):
            L.append(f"- **Standards:** {', '.join(issue['standard_refs'])}")
        grounding = issue.get('evidence_grounding', '—')
        if issue.get('evidence_ref'):
            grounding += f" (captured: {issue['evidence_ref']})"
        L.append(f"- _Evidence grounding: {grounding} · "
                 f"confidence: {issue.get('confidence','—')}_\n")

    # 6. Before / after
    rewrites = [i for i in audit.get("issues", []) if i.get("rewritten_version")]
    if rewrites:
        L.append("## 6. Before / After Rewrites / 改写前后对照")
        for issue in rewrites:
            L.append(f"**{issue.get('id','')}**")
            L.append(f"- Before: {issue.get('original_text','')}")
            L.append(f"- After: {issue.get('rewritten_version','')}\n")

    # 7. Priority backlog
    L.append("## 7. Priority Backlog / 优先级待办")
    bl = audit.get("backlog", [])
    if bl:
        L.append("| Priority | Area | Impact | Task | Issue |")
        L.append("| --- | --- | --- | --- | --- |")
        for it in bl:
            L.append(f"| {it.get('priority','')} | {it.get('area','')} | "
                     f"{it.get('estimated_impact','')} | {bi(it.get('task'), langs, sep=' / ')} | "
                     f"{it.get('linked_issue_id','')} |")
    L.append("")

    # 8. Expert-review flags
    flags = audit.get("expert_review_flags", [])
    if flags:
        L.append("## 8. Expert-Review Flags / 需专家复核")
        for fl in flags:
            L.append(f"- **{fl.get('area','')}:** {bi(fl.get('reason'), langs)}")
        L.append("")

    # 9. Next steps
    L.append("## 9. Recommended Next Steps & Re-Audit Loop / 下一步与复审循环")
    for i, s in enumerate(audit.get("next_steps", []), 1):
        L.append(f"{i}. {bi(s, langs, sep=' — ')}")
    L.append("")

    # 10. Limitations
    L.append("## 10. Limitations / 局限性")
    L.append(bi(audit.get("limitations"), langs) + "\n")

    return "\n".join(L)


def main():
    ap = argparse.ArgumentParser(description="Render audit JSON to bilingual Markdown.")
    ap.add_argument("path", help="Path to audit JSON.")
    ap.add_argument("-o", "--output", help="Output .md path (default: stdout).")
    args = ap.parse_args()

    with open(args.path, "r", encoding="utf-8") as f:
        audit = json.load(f)

    md = render(audit)
    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(md)
        print(f"Wrote Markdown report to {args.output}")
    else:
        sys.stdout.write(md)


if __name__ == "__main__":
    main()
