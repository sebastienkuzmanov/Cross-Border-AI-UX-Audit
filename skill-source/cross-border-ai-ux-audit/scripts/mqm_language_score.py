#!/usr/bin/env python3
"""
mqm_language_score.py - MQM-style error-density score for the language_naturalness
dimension of a Cross-Border AI UX Audit.

Grounds the most translation-adjacent dimension in the field standard: MQM
(Multidimensional Quality Metrics), the EU-origin analytic translation-quality
framework used as the gold standard in WMT shared tasks, plus MQM-Chat (2025) for
conversational AI surfaces. See references/framework_crosswalk.md for the typology.

The MQM scoring model penalizes errors by severity, normalizes by text length, and
maps the penalty to a 0-100 quality score. This mirrors how AutoMQM / GEMBA-MQM use
an LLM to label errors with MQM types + severity; here the model supplies the error
list and this script computes the number deterministically.

Input JSON:
  {
    "word_count": 350,
    "errors": [
      {"type": "terminology", "severity": "major"},
      {"type": "mqm_chat:buzzword", "severity": "minor"},
      {"type": "fluency/grammar", "severity": "critical"}
    ]
  }

Usage:
  python mqm_language_score.py lang_errors.json
  cat lang_errors.json | python mqm_language_score.py -

Severity penalties follow common MQM practice (minor=1, major=5, critical=10);
override per error with an explicit "weight". The reference length normalizes the
penalty so scores are comparable across samples of different length.
"""
import argparse
import json
import sys

SEVERITY_PENALTY = {"neutral": 0, "minor": 1, "major": 5, "critical": 10}
REFERENCE_LENGTH = 100  # words; penalty is expressed per REFERENCE_LENGTH words


def compute(word_count, errors):
    wc = max(1, int(word_count or 0))
    total_penalty = 0.0
    by_severity = {"minor": 0, "major": 0, "critical": 0, "neutral": 0}
    by_type = {}
    for err in errors or []:
        sev = str(err.get("severity", "minor")).lower()
        weight = err.get("weight")
        pen = float(weight) if weight is not None else SEVERITY_PENALTY.get(sev, 1)
        total_penalty += pen
        by_severity[sev] = by_severity.get(sev, 0) + 1
        etype = err.get("type", "unspecified")
        by_type[etype] = by_type.get(etype, 0) + 1

    # MQM error density: penalty points per REFERENCE_LENGTH words.
    density = total_penalty / wc * REFERENCE_LENGTH
    # Map density to a 0-100 score. A density of 0 -> 100; each penalty point per
    # 100 words removes ~3 points, floored at 0. (Calibratable; document any change.)
    score = max(0, round(100 - density * 3))

    return {
        "language_naturalness_score": score,
        "mqm_error_density_per_100_words": round(density, 2),
        "total_penalty": round(total_penalty, 1),
        "word_count": wc,
        "error_count": len(errors or []),
        "errors_by_severity": by_severity,
        "errors_by_type": by_type,
        "note": "MQM-style heuristic; per-dimension judgment still required. "
                "Severity penalties minor=1/major=5/critical=10.",
    }


def main():
    ap = argparse.ArgumentParser(description="MQM-style language quality scorer.")
    ap.add_argument("path", help="Path to errors JSON, or '-' for stdin.")
    args = ap.parse_args()

    if args.path == "-":
        data = json.load(sys.stdin)
    else:
        with open(args.path, "r", encoding="utf-8") as f:
            data = json.load(f)

    result = compute(data.get("word_count"), data.get("errors", []))
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
