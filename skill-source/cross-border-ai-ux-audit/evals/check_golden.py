#!/usr/bin/env python3
"""
Golden regression check: re-score the gold audit and confirm the scorer still
reproduces the expected overall / band / confidence, and that the schema shape
(nine dimensions, issues, expert-review flags) is intact.

Run:  python evals/check_golden.py
"""
import json
import os
import sys

HERE = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(HERE, "..", "scripts"))
import score_audit as s  # noqa: E402


def main():
    audit = json.load(open(os.path.join(HERE, "golden", "gold_audit.json"), encoding="utf-8"))
    exp = json.load(open(os.path.join(HERE, "golden", "expectations.json"), encoding="utf-8"))

    mfs = audit["market_fit_score"]
    profile = audit.get("meta", {}).get("weight_profile", "default")
    r = s.compute(mfs["dimension_scores"], mfs.get("unresolved_critical_count", 0),
                  mfs.get("evidence_completeness"), profile=profile)

    checks = {
        "overall": (r["overall"], exp["overall"]),
        "band": (r["band"], exp["band"]),
        "confidence": (r["confidence"], exp["confidence"]),
        "weight_profile": (r["weight_profile"], exp["weight_profile"]),
        "dimension_count": (len(mfs["dimension_scores"]), exp["dimension_count"]),
        "issue_count": (len(audit["issues"]), exp["issue_count"]),
        "expert_review_flags": (len(audit["expert_review_flags"]), exp["expert_review_flags"]),
    }

    failed = []
    for name, (got, want) in checks.items():
        status = "PASS" if got == want else "FAIL"
        if got != want:
            failed.append(name)
        print(f"  {status} {name}: got {got!r}, expected {want!r}")

    # Every issue should cite at least one standard (framework cross-walk).
    missing_refs = [i["id"] for i in audit["issues"] if not i.get("standard_refs")]
    if missing_refs:
        failed.append("standard_refs")
        print(f"  FAIL standard_refs: issues without standard_refs: {missing_refs}")
    else:
        print("  PASS standard_refs: every issue cites a standard")

    if failed:
        print(f"\nGOLDEN CHECK FAILED: {', '.join(failed)}")
        sys.exit(1)
    print("\nGolden check passed.")


if __name__ == "__main__":
    main()
