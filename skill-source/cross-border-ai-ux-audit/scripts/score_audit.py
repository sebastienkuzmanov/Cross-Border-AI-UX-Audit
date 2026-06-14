#!/usr/bin/env python3
"""
score_audit.py - Deterministic market-fit scorer for the Cross-Border AI UX Audit.

The model produces per-dimension scores (0-100) with justifications; this script
computes the overall score, band, and confidence so the number is reproducible
rather than LLM-guessed.

Nine dimensions are scored. Weights are a calibratable hypothesis, not a validated
constant (see references/scoring_severity_priority.md and calibration_and_review.md).
A corridor weight PROFILE may be selected (e.g. "eu_eaa" boosts accessibility for
EU-facing corridors, where EN 301 549 / WCAG 2.1 AA is legally required).

Inputs (JSON), either:
  - a full audit object with a "market_fit_score" block (and optional meta.weight_profile), or
  - a bare score block: {"dimension_scores": {...}, "unresolved_critical_count": N,
                         "evidence_completeness": M}

Usage:
  python score_audit.py audit.json
  python score_audit.py audit.json --profile eu_eaa
  python score_audit.py audit.json --in-place        # write overall/band/confidence back
  python score_audit.py --list-profiles
  cat score_block.json | python score_audit.py -

Logic:
  1. weighted base over scored dimensions (weights renormalized over non-null dims)
  2. cap at 59 if >=1 unresolved Critical, at 39 if >=2
  3. evidence_completeness sets confidence; it does not silently move the number
  4. band the (possibly capped) overall
"""
import argparse
import json
import sys

# Default weights across the nine dimensions (sum = 1.00). Trust and AI-expectation
# dominate because AI raises the trust threshold and cross-border raises it further;
# language correctness is necessary but not sufficient. Recalibrate against
# expert-reviewed examples and record the version used.
DEFAULT_WEIGHTS = {
    "trust_and_privacy": 0.16,
    "ai_expectation_setting": 0.15,
    "agent_chatbot_behavior": 0.12,
    "ux_clarity": 0.11,
    "conversion": 0.11,
    "cultural_fit": 0.10,
    "accessibility": 0.09,
    "language_naturalness": 0.09,
    "market_entry_risk": 0.07,
}

# Corridor / context weight profiles. "eu_eaa" raises accessibility and market-entry
# weight for any corridor that serves EU consumers (European Accessibility Act,
# enforceable 2025-06-28; EN 301 549 / WCAG 2.1 AA).
PROFILES = {
    "default": DEFAULT_WEIGHTS,
    "eu_eaa": {
        "trust_and_privacy": 0.15,
        "ai_expectation_setting": 0.14,
        "accessibility": 0.14,
        "agent_chatbot_behavior": 0.11,
        "ux_clarity": 0.10,
        "conversion": 0.10,
        "market_entry_risk": 0.09,
        "cultural_fit": 0.09,
        "language_naturalness": 0.08,
    },
}

DIMENSIONS = list(DEFAULT_WEIGHTS.keys())

BANDS = [
    (90, 100, "Strong readiness; targeted improvements remain"),
    (75, 89, "Generally ready with important fixes"),
    (60, 74, "Usable base, but material market-fit gaps remain"),
    (40, 59, "Significant adaptation required before launch"),
    (0, 39, "Fundamental trust, clarity, or market-fit problems"),
]

CRITICAL_CAP_ONE = 59
CRITICAL_CAP_TWO = 39


def band_for(score):
    for lo, hi, label in BANDS:
        if lo <= score <= hi:
            return label
    return "Out of range"


def confidence_for(evidence_completeness):
    if evidence_completeness is None:
        return "unknown"
    if evidence_completeness < 50:
        return "low"
    if evidence_completeness < 80:
        return "medium"
    return "high"


def compute(dimension_scores, unresolved_critical_count=0, evidence_completeness=None,
            weights=None, profile="default"):
    if weights is None:
        weights = PROFILES.get(profile, DEFAULT_WEIGHTS)

    # Keep only dimensions with a numeric score (exclude null / missing).
    scored = {}
    skipped = []
    for dim in weights:
        val = dimension_scores.get(dim)
        if val is None:
            skipped.append(dim)
            continue
        try:
            val = float(val)
        except (TypeError, ValueError):
            skipped.append(dim)
            continue
        val = max(0.0, min(100.0, val))
        scored[dim] = val

    if not scored:
        raise ValueError("No scorable dimensions provided.")

    # Renormalize weights across scored dimensions.
    total_weight = sum(weights[d] for d in scored)
    weighted_base = sum(weights[d] * scored[d] for d in scored) / total_weight

    overall = weighted_base
    cap_applied = None
    n_crit = int(unresolved_critical_count or 0)
    if n_crit >= 2 and overall > CRITICAL_CAP_TWO:
        overall = CRITICAL_CAP_TWO
        cap_applied = f"capped at {CRITICAL_CAP_TWO} (>=2 unresolved Critical issues)"
    elif n_crit >= 1 and overall > CRITICAL_CAP_ONE:
        overall = CRITICAL_CAP_ONE
        cap_applied = f"capped at {CRITICAL_CAP_ONE} (>=1 unresolved Critical issue)"

    overall = int(round(overall))

    return {
        "overall": overall,
        "band": band_for(overall),
        "confidence": confidence_for(evidence_completeness),
        "weight_profile": profile,
        "weighted_base": round(weighted_base, 1),
        "cap_applied": cap_applied,
        "unresolved_critical_count": n_crit,
        "evidence_completeness": evidence_completeness,
        "scored_dimensions": {d: round(scored[d], 1) for d in scored},
        "skipped_dimensions": skipped,
        "weights_used": {d: round(weights[d], 3) for d in scored},
    }


def extract_block(data):
    """Accept either a full audit object or a bare score block."""
    if isinstance(data, dict) and "market_fit_score" in data:
        return data["market_fit_score"], data
    return data, None


def main():
    ap = argparse.ArgumentParser(description="Deterministic market-fit scorer.")
    ap.add_argument("path", nargs="?", help="Path to audit JSON, or '-' for stdin.")
    ap.add_argument("--in-place", action="store_true",
                    help="Write overall/band/confidence/weight_profile back into the audit file.")
    ap.add_argument("--profile", default=None,
                    help=f"Weight profile to use. One of: {', '.join(PROFILES)}.")
    ap.add_argument("--list-profiles", action="store_true",
                    help="Print available weight profiles and exit.")
    args = ap.parse_args()

    if args.list_profiles:
        for name, w in PROFILES.items():
            print(f"{name}: " + ", ".join(f"{k}={v}" for k, v in w.items()))
        return

    if not args.path:
        ap.error("path is required (or use --list-profiles)")

    if args.path == "-":
        data = json.load(sys.stdin)
    else:
        with open(args.path, "r", encoding="utf-8") as f:
            data = json.load(f)

    block, full = extract_block(data)

    # Profile precedence: --profile flag > meta.weight_profile > "default".
    profile = args.profile
    if profile is None and full is not None:
        profile = full.get("meta", {}).get("weight_profile")
    if profile is None:
        profile = "default"
    if profile not in PROFILES:
        ap.error(f"Unknown profile '{profile}'. Available: {', '.join(PROFILES)}")

    dimension_scores = block.get("dimension_scores", {})
    result = compute(
        dimension_scores,
        block.get("unresolved_critical_count", 0),
        block.get("evidence_completeness"),
        profile=profile,
    )

    if args.in_place:
        if args.path == "-":
            ap.error("--in-place cannot be used with stdin")
        if full is None:
            ap.error("--in-place requires a full audit object containing 'market_fit_score'")
        full["market_fit_score"]["overall"] = result["overall"]
        full["market_fit_score"]["band"] = result["band"]
        full["market_fit_score"]["confidence"] = result["confidence"]
        full["market_fit_score"]["weight_profile"] = result["weight_profile"]
        with open(args.path, "w", encoding="utf-8") as f:
            json.dump(full, f, ensure_ascii=False, indent=2)
        print(f"Updated {args.path}: overall={result['overall']} "
              f"({result['band']}), confidence={result['confidence']}, "
              f"profile={result['weight_profile']}")
    else:
        print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
