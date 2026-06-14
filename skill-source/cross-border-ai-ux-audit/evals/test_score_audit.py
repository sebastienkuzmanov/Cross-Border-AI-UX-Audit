#!/usr/bin/env python3
"""
Unit tests for scripts/score_audit.py.

Run directly:   python evals/test_score_audit.py
Or with pytest: pytest evals/test_score_audit.py

These pin the scorer's contract: weight sums, weighted average, the unresolved-Critical
caps, null-dimension renormalization, band boundaries, evidence-completeness -> confidence,
and the corridor weight profiles.
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))
import score_audit as s  # noqa: E402

FULL_90 = {d: 90 for d in s.DIMENSIONS}


def approx(a, b, tol=1):
    return abs(a - b) <= tol


def test_profiles_sum_to_one():
    for name, w in s.PROFILES.items():
        assert approx(sum(w.values()), 1.0, 0.0001), f"{name} weights must sum to 1.0"
        assert len(w) == 9, f"{name} must have nine dimensions"


def test_all_equal_scores_returns_that_value():
    r = s.compute({d: 70 for d in s.DIMENSIONS}, 0, 80)
    assert r["overall"] == 70
    assert r["band"] == "Usable base, but material market-fit gaps remain"


def test_one_critical_caps_at_59():
    r = s.compute(FULL_90, unresolved_critical_count=1, evidence_completeness=90)
    assert r["overall"] == 59
    assert "59" in (r["cap_applied"] or "")


def test_two_criticals_cap_at_39():
    r = s.compute(FULL_90, unresolved_critical_count=2, evidence_completeness=90)
    assert r["overall"] == 39
    assert "39" in (r["cap_applied"] or "")


def test_cap_not_applied_when_base_already_below_cap():
    r = s.compute({d: 30 for d in s.DIMENSIONS}, unresolved_critical_count=1)
    assert r["overall"] == 30
    assert r["cap_applied"] is None


def test_null_dimensions_renormalize():
    scores = {d: None for d in s.DIMENSIONS}
    scores["trust_and_privacy"] = 50
    scores["ai_expectation_setting"] = 50
    r = s.compute(scores, 0, 40)
    assert r["overall"] == 50
    assert set(r["scored_dimensions"].keys()) == {"trust_and_privacy", "ai_expectation_setting"}
    assert len(r["skipped_dimensions"]) == 7


def test_confidence_thresholds():
    assert s.compute(FULL_90, 0, 49)["confidence"] == "low"
    assert s.compute(FULL_90, 0, 50)["confidence"] == "medium"
    assert s.compute(FULL_90, 0, 79)["confidence"] == "medium"
    assert s.compute(FULL_90, 0, 80)["confidence"] == "high"
    assert s.compute(FULL_90, 0, None)["confidence"] == "unknown"


def test_band_boundaries():
    assert s.band_for(90) == "Strong readiness; targeted improvements remain"
    assert s.band_for(75) == "Generally ready with important fixes"
    assert s.band_for(74) == "Usable base, but material market-fit gaps remain"
    assert s.band_for(59) == "Significant adaptation required before launch"
    assert s.band_for(39) == "Fundamental trust, clarity, or market-fit problems"
    assert s.band_for(0) == "Fundamental trust, clarity, or market-fit problems"


def test_scores_clamped_to_0_100():
    r = s.compute({d: 150 for d in s.DIMENSIONS}, 0, 100)
    assert r["overall"] == 100
    r2 = s.compute({d: -20 for d in s.DIMENSIONS}, 0, 100)
    assert r2["overall"] == 0


def test_eu_profile_weights_accessibility_higher():
    assert s.PROFILES["eu_eaa"]["accessibility"] > s.PROFILES["default"]["accessibility"]
    # With accessibility low and others high, eu_eaa should score <= default.
    scores = {d: 90 for d in s.DIMENSIONS}
    scores["accessibility"] = 20
    default = s.compute(scores, 0, 90, profile="default")["overall"]
    eu = s.compute(scores, 0, 90, profile="eu_eaa")["overall"]
    assert eu <= default


def test_no_scorable_dimensions_raises():
    try:
        s.compute({d: None for d in s.DIMENSIONS}, 0, 50)
    except ValueError:
        return
    raise AssertionError("expected ValueError when no dimensions are scorable")


def _run_all():
    tests = [v for k, v in sorted(globals().items()) if k.startswith("test_") and callable(v)]
    passed = 0
    for t in tests:
        t()
        passed += 1
        print(f"  PASS {t.__name__}")
    print(f"\n{passed}/{len(tests)} scorer tests passed.")


if __name__ == "__main__":
    _run_all()
