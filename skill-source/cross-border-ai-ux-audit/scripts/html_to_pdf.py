#!/usr/bin/env python3
"""
html_to_pdf.py — Convert the HTML audit report to PDF using Playwright/Chromium.

Per the skill's rules, PDF is best-effort: if Playwright/Chromium is unavailable or
the conversion fails, the HTML report is still the deliverable — this script exits
non-zero with a clear message so the caller can fall back to delivering the HTML.

Setup (once):
  python -m pip install playwright
  python -m playwright install chromium

Usage:
  python html_to_pdf.py report.html report.pdf
"""
import argparse
import os
import sys


def convert(html_path, pdf_path):
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("Playwright is not installed. Install with:\n"
              "  python -m pip install playwright\n"
              "  python -m playwright install chromium\n"
              "Falling back: deliver the HTML report instead.", file=sys.stderr)
        return False

    abs_html = os.path.abspath(html_path)
    url = "file://" + abs_html
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            page.goto(url, wait_until="networkidle")
            # Render with the report's print styles; toggle is hidden by @media print.
            page.pdf(
                path=pdf_path,
                format="A4",
                print_background=True,
                margin={"top": "16mm", "bottom": "16mm", "left": "14mm", "right": "14mm"},
            )
            browser.close()
        return True
    except Exception as exc:  # noqa: BLE001 - we want any failure to fall back cleanly
        print(f"PDF conversion failed: {exc}\n"
              "Falling back: deliver the HTML report instead.", file=sys.stderr)
        return False


def main():
    ap = argparse.ArgumentParser(description="Convert HTML report to PDF (best-effort).")
    ap.add_argument("html_path", help="Input HTML report path.")
    ap.add_argument("pdf_path", help="Output PDF path.")
    args = ap.parse_args()

    if not os.path.exists(args.html_path):
        print(f"Input not found: {args.html_path}", file=sys.stderr)
        sys.exit(2)

    ok = convert(args.html_path, args.pdf_path)
    if ok:
        print(f"Wrote PDF to {args.pdf_path}")
        sys.exit(0)
    else:
        # Non-zero exit signals the caller to fall back to HTML delivery.
        sys.exit(1)


if __name__ == "__main__":
    main()
