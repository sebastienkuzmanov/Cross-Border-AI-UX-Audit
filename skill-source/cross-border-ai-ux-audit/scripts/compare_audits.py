#!/usr/bin/env python3
"""
compare_audits.py - Diff two Cross-Border AI UX Audit JSON files (same product/corridor,
different iterations) and report what changed.

Operationalizes the re-audit loop: run an audit, fix P1 items, re-audit, then compare.
Shows the overall + per-dimension score deltas and the added / removed / changed findings.

Usage:
  python compare_audits.py before.json after.json
  python compare_audits.py before.json after.json --json   # machine-readable diff
"""
import argparse
import json

DIM_LABELS = {
    "trust_and_privacy": "Trust & Privacy",
    "ai_expectation_setting": "AI Expectation-Setting",
    "agent_chatbot_behavior": "Agent & Chatbot Behavior",
    "ux_clarity": "UX Clarity",
    "conversion": "Conversion",
    "cultural_fit": "Cultural Fit",
    "accessibility": "Accessibility",
    "language_naturalness": "Language Naturalness",
    "market_entry_risk": "Market-Entry Risk",
}


def load(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def issues_by_id(audit):
    return {i.get("id"): i for i in audit.get("issues", []) if i.get("id")}


def diff(before, after):
    b_mfs = before.get("market_fit_score", {})
    a_mfs = after.get("market_fit_score", {})
    b_overall = b_mfs.get("overall")
    a_overall = a_mfs.get("overall")

    dim_deltas = {}
    b_dims = b_mfs.get("dimension_scores", {})
    a_dims = a_mfs.get("dimension_scores", {})
    for dim in DIM_LABELS:
        bv, av = b_dims.get(dim), a_dims.get(dim)
        if bv is None and av is None:
            continue
        dim_deltas[dim] = {"before": bv, "after": av,
                           "delta": (av - bv) if (isinstance(bv, (int, float))
                                                  and isinstance(av, (int, float))) else None}

    b_iss, a_iss = issues_by_id(before), issues_by_id(after)
    resolved = sorted(set(b_iss) - set(a_iss))
    new = sorted(set(a_iss) - set(b_iss))
    changed = []
    for iid in sorted(set(b_iss) & set(a_iss)):
        bsv, asv = b_iss[iid].get("severity"), a_iss[iid].get("severity")
        if bsv != asv:
            changed.append({"id": iid, "severity_before": bsv, "severity_after": asv})

    return {
        "overall_before": b_overall,
        "overall_after": a_overall,
        "overall_delta": (a_overall - b_overall) if (isinstance(b_overall, (int, float))
                                                     and isinstance(a_overall, (int, float))) else None,
        "band_before": b_mfs.get("band"),
        "band_after": a_mfs.get("band"),
        "dimension_deltas": dim_deltas,
        "resolved_issue_ids": resolved,
        "new_issue_ids": new,
        "changed_severity": changed,
        "unresolved_critical_before": b_mfs.get("unresolved_critical_count"),
        "unresolved_critical_after": a_mfs.get("unresolved_critical_count"),
    }


def fmt_delta(d):
    if d is None:
        return "n/a"
    return f"+{d}" if d > 0 else (str(d) if d < 0 else "0")


def render_text(d, before_meta, after_meta):
    L = []
    prod = before_meta.get("product") or after_meta.get("product") or "product"
    L.append(f"Audit comparison - {prod}")
    L.append(f"  {before_meta.get('source_market','?')} -> {before_meta.get('target_market','?')}")
    L.append("")
    L.append(f"Overall: {d['overall_before']} -> {d['overall_after']}  ({fmt_delta(d['overall_delta'])})")
    L.append(f"  Band: {d['band_before']}  ->  {d['band_after']}")
    L.append(f"  Unresolved Critical: {d['unresolved_critical_before']} -> {d['unresolved_critical_after']}")
    L.append("")
    L.append("Dimension deltas:")
    for dim, v in d["dimension_deltas"].items():
        L.append(f"  {DIM_LABELS.get(dim, dim):<26} {str(v['before']):>4} -> {str(v['after']):>4}  ({fmt_delta(v['delta'])})")
    L.append("")
    L.append(f"Resolved since last audit ({len(d['resolved_issue_ids'])}): "
             + (", ".join(d['resolved_issue_ids']) or "none"))
    L.append(f"New findings ({len(d['new_issue_ids'])}): "
             + (", ".join(d['new_issue_ids']) or "none"))
    if d["changed_severity"]:
        L.append("Severity changes:")
        for c in d["changed_severity"]:
            L.append(f"  {c['id']}: {c['severity_before']} -> {c['severity_after']}")
    return "\n".join(L)


def main():
    ap = argparse.ArgumentParser(description="Diff two audit JSON files.")
    ap.add_argument("before", help="Earlier audit JSON.")
    ap.add_argument("after", help="Later audit JSON.")
    ap.add_argument("--json", action="store_true", help="Output machine-readable JSON.")
    args = ap.parse_args()

    before, after = load(args.before), load(args.after)
    d = diff(before, after)
    if args.json:
        print(json.dumps(d, ensure_ascii=False, indent=2))
    else:
        print(render_text(d, before.get("meta", {}), after.get("meta", {})))


if __name__ == "__main__":
    main()
