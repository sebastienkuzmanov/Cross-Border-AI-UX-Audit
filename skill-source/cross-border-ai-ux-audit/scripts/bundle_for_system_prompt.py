#!/usr/bin/env python3
"""
bundle_for_system_prompt.py - Concatenate SKILL.md + references into one portable
prompt, for using this skill with models that have no native skills CLI
(e.g. Doubao, MiniMax, GLM, Kimi, or any chat/API endpoint).

Paste the output as the model's SYSTEM / developer prompt, then provide the product
materials. The model follows the methodology and emits the audit JSON; you run the
scoring/rendering scripts yourself (they are plain Python 3).

Usage:
  python bundle_for_system_prompt.py -o system_prompt_bundle.md
  python bundle_for_system_prompt.py --core -o system_prompt_core.md   # SKILL.md + key refs only
  python bundle_for_system_prompt.py --list

Note: bundling every reference makes a large prompt. Chinese long-context models
(Qwen/Doubao/MiniMax/GLM) handle it, but use --core for tighter context budgets.
"""
import argparse
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
REF_DIR = os.path.join(ROOT, "references")

# A sensible "core" subset for tighter context budgets.
CORE_REFS = [
    "intake_and_corridor.md",
    "audit_dimensions.md",
    "framework_crosswalk.md",
    "scoring_severity_priority.md",
    "finding_and_report_schema.md",
    "limitations_and_safety.md",
]

HEADER = """# SYSTEM PROMPT — Cross-Border AI UX Audit (跨境 AI 用户体验审计)

You are operating as the Cross-Border AI UX Audit skill. Follow the orchestrator
(SKILL.md) below and the bundled references. Produce findings as a single audit JSON
object matching the schema in `finding_and_report_schema.md`; the user will run the
deterministic scoring and rendering scripts separately. Output reports bilingually
(English + 中文). Do not give legal/compliance/security verdicts — escalate them.
Run intake before auditing. Below are SKILL.md and the reference files, concatenated.

---
"""


def read(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def list_refs():
    return sorted(f for f in os.listdir(REF_DIR) if f.endswith(".md"))


def build(core=False):
    parts = [HEADER, "\n\n# ===== SKILL.md =====\n\n", read(os.path.join(ROOT, "SKILL.md"))]
    refs = CORE_REFS if core else list_refs()
    for name in refs:
        path = os.path.join(REF_DIR, name)
        if os.path.exists(path):
            parts.append(f"\n\n# ===== references/{name} =====\n\n")
            parts.append(read(path))
    return "".join(parts)


def main():
    ap = argparse.ArgumentParser(description="Bundle SKILL.md + references into one prompt.")
    ap.add_argument("-o", "--output", help="Output .md path (default: stdout).")
    ap.add_argument("--core", action="store_true", help="Bundle only the core reference subset.")
    ap.add_argument("--list", action="store_true", help="List available reference files and exit.")
    args = ap.parse_args()

    if args.list:
        print("All references:", ", ".join(list_refs()))
        print("Core subset:   ", ", ".join(CORE_REFS))
        return

    bundle = build(core=args.core)
    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(bundle)
        kb = len(bundle.encode("utf-8")) / 1024
        print(f"Wrote {args.output} ({kb:.1f} KB, ~{len(bundle)//4} tokens est.). "
              f"Paste it as the model's system prompt.")
    else:
        sys.stdout.write(bundle)


if __name__ == "__main__":
    main()
