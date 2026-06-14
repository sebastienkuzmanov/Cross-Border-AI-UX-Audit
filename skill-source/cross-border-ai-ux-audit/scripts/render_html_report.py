#!/usr/bin/env python3
"""
render_html_report.py — Render the canonical audit JSON into a designed, self-contained,
bilingual (English + 中文) static HTML report with an EN / 中文 language toggle.

No external fonts or assets are fetched; the file is portable and prints cleanly to PDF
(via scripts/html_to_pdf.py).

Usage:
  python render_html_report.py audit.json -o report.html
"""
import argparse
import html
import json

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
SEV_CLASS = {"Critical": "sev-crit", "High": "sev-high", "Medium": "sev-med", "Low": "sev-low"}


def e(s):
    return html.escape(str(s)) if s is not None else ""


def bi(field):
    """Return (en_html, zh_html) for a {en, zh} field or plain string."""
    if field is None:
        return ("", "")
    if isinstance(field, str):
        return (e(field), e(field))
    return (e(field.get("en", "")), e(field.get("zh", "")))


def span(field, extra_class=""):
    """Wrap a bilingual field in language spans so the toggle can switch them."""
    en, zh = bi(field)
    cls = (" " + extra_class) if extra_class else ""
    return (f'<span class="lang-en{cls}">{en}</span>'
            f'<span class="lang-zh{cls}">{zh}</span>')


def both(en_text, zh_text):
    return (f'<span class="lang-en">{e(en_text)}</span>'
            f'<span class="lang-zh">{e(zh_text)}</span>')


CSS = """
:root{
  --ink:#16202C; --paper:#FBFAF7; --accent:#2F6F6A; --hair:#E2DDD3; --muted:#5C6670;
  --crit:#B23A3A; --high:#C2722B; --med:#3E6E8E; --low:#7C8579;
}
*{box-sizing:border-box;}
html{-webkit-text-size-adjust:100%;}
body{
  margin:0; background:var(--paper); color:var(--ink);
  font-family:-apple-system,BlinkMacSystemFont,"Segoe UI","Helvetica Neue","PingFang SC","Microsoft YaHei",Arial,sans-serif;
  line-height:1.62; font-size:16px;
}
.wrap{max-width:880px; margin:0 auto; padding:48px 28px 96px;}
a{color:var(--accent);}
.eyebrow{font-size:12px; letter-spacing:.14em; text-transform:uppercase; color:var(--accent); font-weight:700;}
h1{font-size:31px; line-height:1.15; margin:.2em 0 .1em; letter-spacing:-.01em;}
h2{font-size:20px; margin:0; letter-spacing:-.005em;}
h3{font-size:16px; margin:0 0 .4em;}
.sub{color:var(--muted);}
.corridor{font-size:15px; color:var(--ink); margin:.3em 0 .2em; font-weight:600;}
.corridor .arrow{color:var(--accent); padding:0 .35em;}
.meta-line{color:var(--muted); font-size:13.5px; margin-top:.2em;}
header.report-head{border-bottom:2px solid var(--ink); padding-bottom:20px; margin-bottom:8px;
  display:flex; justify-content:space-between; align-items:flex-end; gap:20px; flex-wrap:wrap;}
section{padding:26px 0; border-bottom:1px solid var(--hair);}
.sec-head{display:flex; align-items:baseline; gap:12px; margin-bottom:12px;}
.sec-num{font-variant-numeric:tabular-nums; color:var(--accent); font-weight:700; font-size:14px; min-width:1.4em;}
p{margin:.5em 0;}
.callout{background:#fff; border:1px solid var(--hair); border-left:3px solid var(--accent);
  padding:12px 14px; border-radius:4px; font-size:14px; color:var(--muted);}
/* score */
.score-row{display:flex; gap:26px; align-items:center; flex-wrap:wrap;}
.score-badge{font-variant-numeric:tabular-nums; font-size:46px; font-weight:800; line-height:1; letter-spacing:-.02em;}
.score-badge small{font-size:18px; font-weight:600; color:var(--muted);}
.score-band{font-weight:700;}
.score-facts{color:var(--muted); font-size:13.5px;}
.dims{width:100%; margin-top:14px; display:grid; grid-template-columns:1fr; gap:7px;}
.dim{display:grid; grid-template-columns:200px 1fr 42px; gap:10px; align-items:center; font-size:14px;}
.dim .bar{height:8px; background:var(--hair); border-radius:99px; overflow:hidden;}
.dim .bar > i{display:block; height:100%; background:var(--accent); border-radius:99px;}
.dim .val{text-align:right; font-variant-numeric:tabular-nums; color:var(--muted);}
.dim .na > i{background:repeating-linear-gradient(45deg,var(--hair),var(--hair) 4px,#eee 4px,#eee 8px); width:100%;}
/* risks */
ol.risks{margin:0; padding-left:1.25em;} ol.risks li{margin:.3em 0;}
/* issue cards */
.issue{background:#fff; border:1px solid var(--hair); border-radius:7px; padding:16px 18px; margin:12px 0;
  page-break-inside:avoid; break-inside:avoid;}
.issue-top{display:flex; align-items:center; gap:10px; margin-bottom:8px; flex-wrap:wrap;}
.badge{font-size:11.5px; font-weight:700; letter-spacing:.04em; text-transform:uppercase;
  padding:3px 9px; border-radius:99px; color:#fff;}
.sev-crit{background:var(--crit);} .sev-high{background:var(--high);}
.sev-med{background:var(--med);} .sev-low{background:var(--low);}
.cat{font-weight:700;} .iid{color:var(--muted); font-size:13px; margin-left:auto; font-variant-numeric:tabular-nums;}
.evidence{background:#F6F3EC; border-radius:5px; padding:9px 12px; font-size:14px; margin:8px 0;
  border-left:3px solid var(--hair);}
.evidence .lbl{font-weight:700; color:var(--muted); font-size:11.5px; text-transform:uppercase; letter-spacing:.06em;}
.kv{margin:6px 0; font-size:14.5px;}
.kv b{color:var(--ink);}
.rewrite{display:grid; grid-template-columns:1fr 1fr; gap:10px; margin-top:10px;}
.rewrite .cell{border:1px solid var(--hair); border-radius:5px; padding:9px 11px; font-size:14px;}
.rewrite .before{background:#FBF1F1;} .rewrite .after{background:#EEF5F1;}
.rewrite .lbl{font-size:11px; font-weight:700; text-transform:uppercase; letter-spacing:.06em; color:var(--muted); display:block; margin-bottom:3px;}
.note{color:var(--muted); font-size:13px; margin-top:6px;}
.std{display:inline-block; font-size:11px; font-weight:600; background:#EEF2F1; color:var(--accent);
  border:1px solid #D8E3E1; border-radius:99px; padding:1px 8px; margin:0 4px 3px 0; white-space:nowrap;}
/* tables */
table{width:100%; border-collapse:collapse; font-size:14px; margin-top:8px;}
th,td{text-align:left; padding:8px 10px; border-bottom:1px solid var(--hair); vertical-align:top;}
th{font-size:12px; text-transform:uppercase; letter-spacing:.05em; color:var(--muted);}
td.p1{font-weight:700;}
.pill{font-size:11px; font-weight:700; padding:2px 7px; border-radius:99px; background:#EEE9DF; color:var(--ink);}
/* flags */
.flag{border:1px solid var(--hair); border-left:3px solid var(--high); background:#fff; border-radius:5px;
  padding:10px 13px; margin:8px 0; font-size:14px;}
.flag b{color:var(--high);}
/* toggle */
.toggle{display:inline-flex; border:1px solid var(--ink); border-radius:99px; overflow:hidden; font-size:13px;}
.toggle button{appearance:none; border:0; background:transparent; color:var(--ink); padding:6px 14px;
  cursor:pointer; font-weight:700; font-family:inherit;}
.toggle button[aria-pressed="true"]{background:var(--ink); color:var(--paper);}
.toggle button:focus-visible{outline:3px solid var(--accent); outline-offset:2px;}
/* language switching */
body[data-lang="en"] .lang-zh{display:none;}
body[data-lang="zh"] .lang-en{display:none;}
.lang-en,.lang-zh{} /* both shown if no data-lang (e.g. print of single-lang) */
@media (max-width:620px){
  .dim{grid-template-columns:130px 1fr 36px;}
  .rewrite{grid-template-columns:1fr;}
  h1{font-size:25px;}
}
@media print{
  body{background:#fff;} .toggle{display:none;} .wrap{padding:0;}
  section{border-bottom:1px solid #ddd;}
}
@media (prefers-reduced-motion:reduce){*{transition:none!important;animation:none!important;}}
"""

TOGGLE_JS = """
(function(){
  var body=document.body;
  var langs=(body.getAttribute('data-available')||'en,zh').split(',');
  function set(l){body.setAttribute('data-lang',l);
    document.querySelectorAll('.toggle button').forEach(function(b){
      b.setAttribute('aria-pressed', b.getAttribute('data-l')===l ? 'true':'false');});}
  document.querySelectorAll('.toggle button').forEach(function(b){
    b.addEventListener('click',function(){set(b.getAttribute('data-l'));});});
  set(langs[0]);
})();
"""


def dim_rows(mfs, langs):
    ds = mfs.get("dimension_scores", {})
    rows = []
    for key, (en, zh) in DIM_LABELS.items():
        v = ds.get(key)
        label = both(en, zh)
        if v is None:
            rows.append(f'<div class="dim"><div>{label}</div>'
                        f'<div class="bar na"><i></i></div><div class="val">n/a</div></div>')
        else:
            pct = max(0, min(100, float(v)))
            rows.append(f'<div class="dim"><div>{label}</div>'
                        f'<div class="bar"><i style="width:{pct:.0f}%"></i></div>'
                        f'<div class="val">{int(round(pct))}</div></div>')
    return "\n".join(rows)


def render(audit):
    meta = audit.get("meta", {})
    langs = meta.get("report_languages", ["en", "zh"])
    available = ",".join(langs)
    data_lang = langs[0]

    # Header
    corridor = (f'{e(meta.get("source_market","?"))}'
                f'<span class="arrow">→</span>{e(meta.get("target_market","?"))}')
    meta_bits = []
    if meta.get("target_audience"):
        meta_bits.append(e(meta["target_audience"]))
    if meta.get("product_type"):
        meta_bits.append(e(meta["product_type"]))
    if meta.get("playbook"):
        meta_bits.append("playbook: " + e(meta["playbook"]))
    meta_line = " · ".join(meta_bits)
    date_line = f'{e(meta.get("audit_date",""))} · v{e(meta.get("audit_version",1))}'

    toggle = ('<div class="toggle" role="group" aria-label="Language">'
              '<button data-l="en">EN</button>'
              '<button data-l="zh">中文</button></div>') if len(langs) > 1 else ""

    parts = []
    parts.append(f'''<header class="report-head">
  <div>
    <div class="eyebrow">{both("Market-Readiness Dossier","市场就绪报告")}</div>
    <h1>{both("Cross-Border AI UX Audit","跨境 AI 用户体验审计")}</h1>
    <div class="corridor">{corridor}</div>
    <div class="meta-line">{meta_line}</div>
    <div class="meta-line">{date_line}</div>
  </div>
  {toggle}
</header>''')

    def section(num, en_title, zh_title, inner):
        return (f'<section><div class="sec-head"><span class="sec-num">{num}</span>'
                f'<h2>{both(en_title, zh_title)}</h2></div>{inner}</section>')

    # 1. Executive summary
    parts.append(section("01", "Executive Summary", "概要",
                         f'<p>{span(audit.get("executive_summary"))}</p>'))

    # 2. Corridor & evidence
    rev = ", ".join(e(x) for x in meta.get("evidence_reviewed", [])) or "—"
    na = ", ".join(e(x) for x in meta.get("evidence_not_available", [])) or "—"
    ev_inner = (f'<p class="kv"><b>{both("Evidence reviewed","已审证据")}:</b> {rev}</p>'
                f'<p class="kv"><b>{both("Not available","缺失材料")}:</b> {na}</p>'
                f'<p class="kv"><b>{both("Evidence level","证据层级")}:</b> {e(meta.get("evidence_level","?"))}</p>')
    if meta.get("assumptions"):
        asm = "; ".join(e(a) for a in meta["assumptions"])
        ev_inner += f'<p class="kv"><b>{both("Assumptions","假设")}:</b> {asm}</p>'
    parts.append(section("02", "Market Corridor & Evidence", "市场走廊与证据", ev_inner))

    # 3. Score
    mfs = audit.get("market_fit_score", {})
    score_inner = f'''<div class="score-row">
  <div class="score-badge">{e(mfs.get("overall","?"))}<small>/100</small></div>
  <div>
    <div class="score-band">{e(mfs.get("band",""))}</div>
    <div class="score-facts">{both("Confidence","置信度")}: {e(mfs.get("confidence","?"))} ·
      {both("Evidence completeness","证据完整度")}: {e(mfs.get("evidence_completeness","?"))} ·
      {both("Unresolved Critical","未解决严重项")}: {e(mfs.get("unresolved_critical_count",0))}</div>
  </div>
  <div class="dims">{dim_rows(mfs, langs)}</div>
</div>'''
    if mfs.get("score_explanation"):
        score_inner += f'<p>{span(mfs.get("score_explanation"))}</p>'
    score_inner += ('<div class="callout">' + span({
        "en": "The score is a heuristic summary for comparing iterations of the same product "
              "and corridor. It is not a certification, a legal/compliance rating, or a guarantee "
              "of market fit. Prioritize the findings over the number.",
        "zh": "该评分用于比较同一产品在同一走廊下的多次审计迭代，是启发式概览，"
              "并非合规认证、法律评级或市场契合度保证。请以发现项为准，而非分数本身。",
    }) + '</div>')
    parts.append(section("03", "Market-Fit Score", "市场契合度评分", score_inner))

    # 4. Top risks
    risks = audit.get("top_risks", [])
    risk_items = "".join(f'<li>{span(r)}</li>' for r in risks) or "<li>—</li>"
    parts.append(section("04", "Top Risks", "主要风险", f'<ol class="risks">{risk_items}</ol>'))

    # 5. Findings
    issue_html = []
    for it in audit.get("issues", []):
        sev = it.get("severity", "")
        sev_cls = SEV_CLASS.get(sev, "sev-low")
        cat = it.get("category", "")
        en, zh = DIM_LABELS.get(cat, (cat, cat))
        card = [f'<div class="issue"><div class="issue-top">'
                f'<span class="badge {sev_cls}">{e(sev)}</span>'
                f'<span class="cat">{both(en, zh)}</span>'
                f'<span class="iid">{e(it.get("id",""))}</span></div>']
        if it.get("original_text"):
            card.append(f'<div class="evidence"><span class="lbl">{both("Evidence","原文/行为")}</span><br>'
                        f'{e(it["original_text"])}</div>')
        card.append(f'<p class="kv"><b>{both("Problem","问题")}:</b> {span(it.get("problem"))}</p>')
        card.append(f'<p class="kv"><b>{both("Why it matters","影响")}:</b> {span(it.get("why_it_matters"))}</p>')
        card.append(f'<p class="kv"><b>{both("Recommendation","建议")}:</b> {span(it.get("recommendation"))}</p>')
        if it.get("rewritten_version"):
            rl = it.get("rewritten_version_language", "")
            card.append(f'<div class="rewrite">'
                        f'<div class="cell before"><span class="lbl">{both("Before","改写前")}</span>{e(it.get("original_text",""))}</div>'
                        f'<div class="cell after"><span class="lbl">{both("After","改写后")} ({e(rl)})</span>{e(it["rewritten_version"])}</div>'
                        f'</div>')
        if it.get("target_market_note"):
            card.append(f'<p class="note"><b>{both("Target-market note","市场说明")}:</b> {span(it.get("target_market_note"))}</p>')
        if it.get("standard_refs"):
            chips = " ".join(f'<span class="std">{e(s)}</span>' for s in it["standard_refs"])
            card.append(f'<p class="note"><b>{both("Standards","对应标准")}:</b> {chips}</p>')
        grounding = e(it.get("evidence_grounding", "—"))
        if it.get("evidence_ref"):
            grounding += f' ({both("captured","已采集")}: {e(it["evidence_ref"])})'
        card.append(f'<p class="note">{both("Evidence grounding","证据来源")}: {grounding} · '
                    f'{both("confidence","置信度")}: {e(it.get("confidence","—"))}</p>')
        card.append('</div>')
        issue_html.append("".join(card))
    parts.append(section("05", "Findings by Dimension", "分维度发现", "".join(issue_html) or "<p>—</p>"))

    # 6. Before / after (only those with rewrites)
    rewrites = [i for i in audit.get("issues", []) if i.get("rewritten_version")]
    if rewrites:
        rw = []
        for it in rewrites:
            rw.append(f'<div class="rewrite">'
                      f'<div class="cell before"><span class="lbl">{both("Before","改写前")} · {e(it.get("id",""))}</span>{e(it.get("original_text",""))}</div>'
                      f'<div class="cell after"><span class="lbl">{both("After","改写后")}</span>{e(it.get("rewritten_version",""))}</div>'
                      f'</div>')
        parts.append(section("06", "Before / After Rewrites", "改写前后对照", "".join(rw)))

    # 7. Backlog
    bl = audit.get("backlog", [])
    rows = []
    for it in bl:
        p = e(it.get("priority", ""))
        pcls = ' class="p1"' if p == "P1" else ""
        rows.append(f'<tr><td{pcls}>{p}</td><td>{e(it.get("area",""))}</td>'
                    f'<td>{e(it.get("estimated_impact",""))}</td>'
                    f'<td>{span(it.get("task"))}</td><td>{e(it.get("linked_issue_id",""))}</td></tr>')
    backlog_tbl = (f'<table><thead><tr>'
                   f'<th>{both("Priority","优先级")}</th><th>{both("Area","领域")}</th>'
                   f'<th>{both("Impact","影响")}</th><th>{both("Task","任务")}</th>'
                   f'<th>{both("Issue","对应项")}</th></tr></thead><tbody>'
                   + ("".join(rows) or '<tr><td colspan="5">—</td></tr>') + '</tbody></table>')
    parts.append(section("07", "Priority Backlog", "优先级待办", backlog_tbl))

    # 8. Expert-review flags
    flags = audit.get("expert_review_flags", [])
    if flags:
        fl_html = "".join(f'<div class="flag"><b>{e(fl.get("area",""))}:</b> {span(fl.get("reason"))}</div>'
                          for fl in flags)
        parts.append(section("08", "Expert-Review Flags", "需专家复核", fl_html))

    # 9. Next steps
    steps = audit.get("next_steps", [])
    step_items = "".join(f'<li>{span(s)}</li>' for s in steps) or "<li>—</li>"
    parts.append(section("09", "Next Steps & Re-Audit Loop", "下一步与复审循环",
                         f'<ol class="risks">{step_items}</ol>'))

    # 10. Limitations
    parts.append(section("10", "Limitations", "局限性",
                         f'<p>{span(audit.get("limitations"))}</p>'))

    body = "\n".join(parts)
    return f'''<!DOCTYPE html>
<html lang="{data_lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Cross-Border AI UX Audit — {e(meta.get("product",""))}</title>
<style>{CSS}</style>
</head>
<body data-lang="{data_lang}" data-available="{available}">
<div class="wrap">
{body}
</div>
<script>{TOGGLE_JS}</script>
</body>
</html>'''


def main():
    ap = argparse.ArgumentParser(description="Render audit JSON to designed bilingual HTML.")
    ap.add_argument("path", help="Path to audit JSON.")
    ap.add_argument("-o", "--output", required=True, help="Output .html path.")
    args = ap.parse_args()

    with open(args.path, "r", encoding="utf-8") as f:
        audit = json.load(f)

    htmlout = render(audit)
    with open(args.output, "w", encoding="utf-8") as f:
        f.write(htmlout)
    print(f"Wrote HTML report to {args.output}")


if __name__ == "__main__":
    main()
