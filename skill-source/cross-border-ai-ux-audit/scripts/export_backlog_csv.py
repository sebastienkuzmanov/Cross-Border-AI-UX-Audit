#!/usr/bin/env python3
"""
export_backlog_csv.py — Export the Cross-Border AI UX Audit priority backlog to CSV.

Reads the canonical audit JSON (or a bare list of backlog items) and writes a CSV
sorted by priority (P1, P2, P3) then estimated impact (High, Medium, Low).

Usage:
  python export_backlog_csv.py audit.json -o backlog.csv
  python export_backlog_csv.py audit.json            # writes <input>_backlog.csv
"""
import argparse
import csv
import json
import os
import sys

PRIORITY_ORDER = {"P1": 0, "P2": 1, "P3": 2}
IMPACT_ORDER = {"High": 0, "Medium": 1, "Low": 2}


def pick_lang(field, lang="en"):
    """Backlog task may be a bilingual dict or a plain string."""
    if isinstance(field, dict):
        return field.get(lang) or field.get("en") or field.get("zh") or ""
    return field or ""


def get_backlog(data):
    if isinstance(data, list):
        return data
    if isinstance(data, dict):
        return data.get("backlog", [])
    return []


def main():
    ap = argparse.ArgumentParser(description="Export audit backlog to CSV.")
    ap.add_argument("path", help="Path to audit JSON.")
    ap.add_argument("-o", "--output", help="Output CSV path.")
    ap.add_argument("--lang", default="en", choices=["en", "zh"],
                    help="Language for the task text (default: en).")
    args = ap.parse_args()

    with open(args.path, "r", encoding="utf-8") as f:
        data = json.load(f)

    backlog = get_backlog(data)
    if not backlog:
        print("No backlog items found.", file=sys.stderr)

    backlog = sorted(
        backlog,
        key=lambda it: (
            PRIORITY_ORDER.get(it.get("priority", "P3"), 3),
            IMPACT_ORDER.get(it.get("estimated_impact", "Low"), 3),
        ),
    )

    out = args.output
    if not out:
        base = os.path.splitext(args.path)[0]
        out = f"{base}_backlog.csv"

    with open(out, "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Priority", "Area", "Estimated impact", "Task", "Linked issue"])
        for it in backlog:
            writer.writerow([
                it.get("priority", ""),
                it.get("area", ""),
                it.get("estimated_impact", ""),
                pick_lang(it.get("task"), args.lang),
                it.get("linked_issue_id", ""),
            ])

    print(f"Wrote {len(backlog)} backlog rows to {out}")


if __name__ == "__main__":
    main()
