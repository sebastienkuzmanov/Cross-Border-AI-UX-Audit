#!/usr/bin/env python3
"""
capture_evidence.py - Live evidence capture for the Cross-Border AI UX Audit.

Removes the skill's biggest honesty limit (text-only evidence) by capturing what a
target-market page actually renders: a full-page screenshot plus extracted visible
text, for each supplied URL or local HTML file. The captured artifacts let findings
cite real Level-2/3 evidence (interaction, states, visuals) instead of inferring
from pasted copy. The model can then analyze the screenshots multimodally.

Best-effort: if Playwright/Chromium is unavailable, or a page fails, the script
records the failure in the manifest and continues, so the audit can fall back to
text evidence and state clearly what was and was not captured.

Setup (once):
  python -m pip install playwright
  python -m playwright install chromium

Usage:
  python capture_evidence.py --url https://example.com/pricing --url https://example.com/ -o evidence/
  python capture_evidence.py --url file:///abs/path/page.html -o evidence/
  python capture_evidence.py --urls-file urls.txt -o evidence/

Output: <out>/manifest.json + <out>/<slug>.png + <out>/<slug>.txt per page.
Note: live URLs require outbound network access in your environment.
"""
import argparse
import json
import os
import re
import sys
from datetime import datetime, timezone


def slugify(url):
    s = re.sub(r"^https?://", "", url)
    s = re.sub(r"[^a-zA-Z0-9]+", "-", s).strip("-").lower()
    return (s or "page")[:80]


def capture(urls, out_dir, full_page=True, timeout_ms=30000):
    os.makedirs(out_dir, exist_ok=True)
    manifest = {
        "captured_at": datetime.now(timezone.utc).isoformat(),
        "tool": "playwright/chromium",
        "pages": [],
        "available": True,
    }

    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        manifest["available"] = False
        manifest["error"] = ("Playwright not installed. Run: python -m pip install playwright "
                             "&& python -m playwright install chromium. "
                             "Falling back to text evidence.")
        _write_manifest(manifest, out_dir)
        print(manifest["error"], file=sys.stderr)
        return manifest, False

    ok_any = False
    with sync_playwright() as p:
        try:
            browser = p.chromium.launch()
        except Exception as exc:  # noqa: BLE001
            manifest["available"] = False
            manifest["error"] = f"Could not launch Chromium: {exc}. Falling back to text evidence."
            _write_manifest(manifest, out_dir)
            print(manifest["error"], file=sys.stderr)
            return manifest, False

        page = browser.new_page(viewport={"width": 1280, "height": 900}, device_scale_factor=2)
        for url in urls:
            slug = slugify(url)
            entry = {"url": url, "slug": slug}
            try:
                page.goto(url, wait_until="networkidle", timeout=timeout_ms)
                png_path = os.path.join(out_dir, f"{slug}.png")
                txt_path = os.path.join(out_dir, f"{slug}.txt")
                page.screenshot(path=png_path, full_page=full_page)
                text = page.inner_text("body")
                with open(txt_path, "w", encoding="utf-8") as f:
                    f.write(text)
                entry.update({
                    "screenshot": os.path.basename(png_path),
                    "text_file": os.path.basename(txt_path),
                    "title": page.title(),
                    "text_chars": len(text),
                    "status": "ok",
                })
                ok_any = True
            except Exception as exc:  # noqa: BLE001
                entry.update({"status": "failed", "error": str(exc)})
                print(f"Capture failed for {url}: {exc}", file=sys.stderr)
            manifest["pages"].append(entry)
        browser.close()

    _write_manifest(manifest, out_dir)
    return manifest, ok_any


def _write_manifest(manifest, out_dir):
    with open(os.path.join(out_dir, "manifest.json"), "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)


def main():
    ap = argparse.ArgumentParser(description="Capture live page evidence (best-effort).")
    ap.add_argument("--url", action="append", default=[], help="A URL or file:// path (repeatable).")
    ap.add_argument("--urls-file", help="Text file with one URL per line.")
    ap.add_argument("-o", "--output", default="evidence", help="Output directory.")
    ap.add_argument("--no-full-page", action="store_true", help="Capture viewport only.")
    args = ap.parse_args()

    urls = list(args.url)
    if args.urls_file:
        with open(args.urls_file, "r", encoding="utf-8") as f:
            urls += [ln.strip() for ln in f if ln.strip() and not ln.startswith("#")]
    if not urls:
        ap.error("Provide at least one --url or --urls-file")

    manifest, ok_any = capture(urls, args.output, full_page=not args.no_full_page)
    n_ok = sum(1 for p in manifest["pages"] if p.get("status") == "ok")
    print(f"Captured {n_ok}/{len(urls)} page(s) to {args.output}/ "
          f"(manifest.json). Available: {manifest['available']}")
    # Non-zero exit only if nothing captured AND tooling missing, so callers can fall back.
    sys.exit(0 if (ok_any or manifest["available"]) else 1)


if __name__ == "__main__":
    main()
