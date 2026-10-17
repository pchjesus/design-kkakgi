#!/usr/bin/env python3
"""Verify the MUL. stable Pages entry, functionality and approved generated media."""
from pathlib import Path
import base64
import hashlib
import json
import re
import sys

root = Path(__file__).resolve().parents[1]
landing = (root / "index.html").read_text(encoding="utf-8")
site_path = root / "cases/mul-cup/latest/index.html"
site = site_path.read_text(encoding="utf-8")
manifest = json.loads((root / "cases/mul-cup/latest/release.json").read_text(encoding="utf-8"))

image_payloads = re.findall(r'data:image/webp;base64,([A-Za-z0-9+/=]+)', site)
img_tags = re.findall(r'<img\b[^>]*>', site, flags=re.I | re.S)
expected_hashes = manifest.get("image_sha256", [])
decoded_hashes = []
valid_webp = True
for encoded in image_payloads:
    try:
        payload = base64.b64decode(encoded, validate=True)
        decoded_hashes.append(hashlib.sha256(payload).hexdigest())
        valid_webp &= (
            len(payload) >= 12 and payload[:4] == b"RIFF"
            and payload[8:12] == b"WEBP"
        )
    except (ValueError, base64.binascii.Error):
        valid_webp = False

checks = {
    "landing_link_is_latest": 'href="./cases/mul-cup/latest/"' in landing,
    "manifest_points_to_latest": manifest.get("public_html") == "cases/mul-cup/latest/index.html",
    "html_matches_manifest": (
        f'name="mul-release" content="{manifest.get("html_release_tag", "")}"' in site
    ),
    "release_id_is_approved": manifest.get("release_id") == "E6-C5-HERO",
    "approved_media_scope": (
        manifest.get("image_policy") == "MUL-project-generated-images-approved-for-public-latest-only"
        and manifest.get("images_embedded_in_online") == 2
        and manifest.get("images_embedded_in_local_original") == 2
    ),
    "only_two_approved_images": (
        len(image_payloads) == len(img_tags) == 2
        and site.count("data:image") == 2
        and all("data:image/webp;base64," in tag for tag in img_tags)
    ),
    "webp_payload_valid": valid_webp,
    "generated_image_hashes_match": len(expected_hashes) == 2 and decoded_hashes == expected_hashes,
    "image_size_budget_2mb": site_path.stat().st_size <= 2_000_000,
    "hero_motion_present": "mul-hero-two-modes-controller" in site,
    "E6C5_details_present": "mul-e6c5-details-scale-refine" in site,
    "saved_state_contract_present": "mul-exp001-e1-" in site,
    "cart_preserved": ".add-cart" in site and ".cart-list" in site,
    "colors_preserved": ".turn-control" in site and ".reset-angle" in site,
    "faq_preserved": ".faq-items" in site,
    "reduced_motion_present": "prefers-reduced-motion" in site,
    "no_old_photo_omission_notice": 'data-github-image-omitted="true"' not in site,
}
for name, passed in checks.items():
    print(f'{"PASS" if passed else "FAIL"}: {name}')
if not all(checks.values()):
    sys.exit(1)
print(f'OK: {manifest["release_id"]}, two verified generated photos, stable Pages route.')
