#!/usr/bin/env python3
"""
export_issue_tracker.py - Export the Cross-Border AI UX Audit backlog to issue trackers.

Lands the backlog where teams actually work. Produces:
  - Jira CSV   (Summary, Issue Type, Priority, Labels, Description)  -> Jira CSV importer
  - Linear CSV (Title, Description, Priority, Labels, Status)        -> Linear CSV import
  - generic JSON

Priority mapping: P1 -> Highest/Urgent, P2 -> High, P3 -> Medium.

Usage:
  python export_issue_tracker.py audit.json --format jira   -o backlog_jira.csv
  python export_issue_tracker.py audit.json --format linear -o backlog_linear.csv
  python export_issue_tracker.py audit.json --format json   -o backlog.json
"""
import argparse
import csv
import json

JIRA_PRIORITY = {"P1": "Highest", "P2": "High", "P3": "Medium"}
LINEAR_PRIORITY = {"P1": "Urgent", "P2": "High", "P3": "Medium"}
PRIORITY_ORDER = {"P1": 0, "P2": 1, "P3": 2}
IMPACT_ORDER = {"High": 0, "Medium": 1, "Low": 2}


def pick(field, lang="en"):
    if isinstance(field, dict):
        return field.get(lang) or field.get("en") or field.get("zh") or ""
    return field or ""


def issue_lookup(audit):
    return {i.get("id"): i for i in audit.get("issues", []) if i.get("id")}


def build_rows(audit, lang="en"):
    issues = issue_lookup(audit)
    rows = []
    for it in audit.get("backlog", []):
        linked = it.get("linked_issue_id", "")
        src = issues.get(linked, {})
        task = pick(it.get("task"), lang)
        desc_parts = []
        if src.get("category"):
            desc_parts.append(f"Dimension: {src['category']}")
        if src.get("severity"):
            desc_parts.append(f"Severity: {src['severity']}")
        if src.get("problem"):
            desc_parts.append("Problem: " + pick(src.get("problem"), lang))
        if src.get("recommendation"):
            desc_parts.append("Recommendation: " + pick(src.get("recommendation"), lang))
        if src.get("standard_refs"):
            desc_parts.append("Standards: " + "; ".join(src["standard_refs"]))
        if linked:
            desc_parts.append(f"Audit issue: {linked}")
        rows.append({
            "task": task,
            "priority": it.get("priority", "P3"),
            "area": it.get("area", ""),
            "impact": it.get("estimated_impact", ""),
            "linked_issue_id": linked,
            "description": "\n".join(desc_parts),
        })
    rows.sort(key=lambda r: (PRIORITY_ORDER.get(r["priority"], 3),
                             IMPACT_ORDER.get(r["impact"], 3)))
    return rows


def write_jira(rows, out):
    with open(out, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f)
        w.writerow(["Summary", "Issue Type", "Priority", "Labels", "Description"])
        for r in rows:
            labels = " ".join(x for x in [r["area"].replace(" ", "-"),
                                          f"impact-{r['impact']}", "cross-border-ux"] if x)
            w.writerow([r["task"], "Task", JIRA_PRIORITY.get(r["priority"], "Medium"),
                        labels, r["description"]])


def write_linear(rows, out):
    with open(out, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f)
        w.writerow(["Title", "Description", "Priority", "Labels", "Status"])
        for r in rows:
            labels = ",".join(x for x in [r["area"], f"impact:{r['impact']}", "cross-border-ux"] if x)
            w.writerow([r["task"], r["description"], LINEAR_PRIORITY.get(r["priority"], "Medium"),
                        labels, "Backlog"])


def write_json(rows, out):
    with open(out, "w", encoding="utf-8") as f:
        json.dump(rows, f, ensure_ascii=False, indent=2)


def main():
    ap = argparse.ArgumentParser(description="Export audit backlog to issue trackers.")
    ap.add_argument("path", help="Path to audit JSON.")
    ap.add_argument("--format", choices=["jira", "linear", "json"], required=True)
    ap.add_argument("-o", "--output", required=True, help="Output file path.")
    ap.add_argument("--lang", default="en", choices=["en", "zh"])
    args = ap.parse_args()

    with open(args.path, "r", encoding="utf-8") as f:
        audit = json.load(f)

    rows = build_rows(audit, args.lang)
    {"jira": write_jira, "linear": write_linear, "json": write_json}[args.format](rows, args.output)
    print(f"Wrote {len(rows)} {args.format} item(s) to {args.output}")


if __name__ == "__main__":
    main()
