#!/usr/bin/env python3
"""Static publishing guard for the public, image-free MUL. Pages preview."""
from pathlib import Path
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
landing = (ROOT / "index.html").read_text(encoding="utf-8")
site_file = ROOT / "cases/mul-cup/latest/index.html"
manifest_file = ROOT / "cases/mul-cup/latest/release.json"
site = site_file.read_text(encoding="utf-8")
manifest = json.loads(manifest_file.read_text(encoding="utf-8"))

checks = {
    "landing_link_is_latest": 'href="./cases/mul-cup/latest/"' in landing,
    "manifest_points_to_latest": manifest.get("public_html") == "cases/mul-cup/latest/index.html",
    "html_matches_manifest": (
        f'name="mul-release" content="{manifest.get("html_release_tag", "")}"' in site
    ),
    "no_embedded_image_payload": "data:image" not in site and "base64," not in site,
    "images_explicitly_omitted": (
        len(re.findall(r'<img\\b[^>]*\\bdata-github-image-omitted="true"', site))
        == manifest.get("images_embedded_in_local_original")
    ),
    "user_facing_media_notice": "GitHub 공개 미리보기" in site,
    "hero_motion_present": "mul-hero-two-modes-controller" in site,
    "E6C5_details_present": "mul-e6c5-details-scale-refine" in site,
    "saved_state_contract_present": "mul-exp001-e1-" in site,
    "cart_preserved": ".add-cart" in site and ".cart-list" in site,
    "colors_preserved": ".turn-control" in site and ".reset-angle" in site,
    "faq_preserved": ".faq-items" in site,
    "reduced_motion_present": "prefers-reduced-motion" in site,
}
for name, valid in checks.items():
    print(f'{"PASS" if valid else "FAIL"}: {name}')
if not all(checks.values()):
    sys.exit(1)
print(f'OK: latest route and {manifest["release_id"]} release manifest agree.')
