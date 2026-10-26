#!/usr/bin/env python3
"""Turn saved partner profiles into one row per case study."""

import hashlib
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from links import is_social, story_urls
from products import classify_products

ROOT = Path(__file__).resolve().parents[1]
PROFILES = ROOT / "data" / "profiles.jsonl"
STORIES = ROOT / "data" / "stories.jsonl"


def old_cases(raw):
    if isinstance(raw, list):
        return raw
    if isinstance(raw, str) and raw.strip().startswith("["):
        try:
            parsed = json.loads(raw)
        except json.JSONDecodeError:
            return []
        return parsed if isinstance(parsed, list) else []
    return []


def story_id(*parts):
    digest = hashlib.sha1("\n".join(str(part) for part in parts).encode("utf-8")).hexdigest()
    return digest[:16]


def source_kind(primary, urls):
    if str(primary).startswith("zoho-file:"):
        return "zoho_file"
    http_urls = [url for url in urls if url.startswith("http")]
    if http_urls and all(is_social(url) for url in http_urls):
        return "social"
    if any(url.startswith("http") for url in urls) or str(primary).startswith("http"):
        return "web"
    return "none"


def hold_for(kind, scope):
    if kind == "social":
        return "held", "only a social link"
    if kind == "none":
        return "held", "no file or page link"
    if scope == "out_of_scope":
        return "held", "product is outside CRM, Desk, and Campaigns"
    if scope == "unknown":
        return "needs_product", ""
    return "ready", ""


def load_profiles():
    best = {}
    if not PROFILES.exists():
        return []
    for line in PROFILES.read_text(errors="replace").splitlines():
        if not line.strip():
            continue
        try:
            record = json.loads(line)
        except json.JSONDecodeError:
            continue
        pid = record.get("encryptedpid")
        if not pid:
            continue
        if record.get("ok") or pid not in best:
            best[pid] = record
    return [record for record in best.values() if record.get("ok")]


def rows_for(profile):
    company = profile.get("companyname") or ""
    website = profile.get("website") or ""
    pid = profile.get("encryptedpid") or ""
    rows = []
    for study in profile.get("new_case_studies") or []:
        if not isinstance(study, dict):
            continue
        primary, urls = story_urls(study)
        products = classify_products(study.get("zoho_product"))
        kind = source_kind(primary, urls)
        status, reason = hold_for(kind, products["scope"])
        flags = []
        if products["bundle"]:
            flags.append("bundle named, products inside it are not")
        rows.append({
            "story_id": story_id(pid, study.get("customer_name"), primary, "new"),
            "partner_id": pid,
            "partner": company,
            "website": website,
            "customer": study.get("customer_name") or "",
            "country": study.get("customer_country") or "",
            "industry": study.get("customer_industry") or "",
            "source": "new_case_studies",
            "source_kind": kind,
            "primary": primary,
            "urls": urls,
            "file_id": primary.split(":", 1)[1] if str(primary).startswith("zoho-file:") else "",
            "description": str(study.get("casestudy_description") or "")[:2000],
            "testimonial": str(study.get("testimonial_link") or "")[:2000],
            "product_ids": products["ids"],
            "product_names": products["names"],
            "scope": products["scope"],
            "status": status,
            "hold_reason": reason,
            "flags": flags,
        })
    for study in old_cases(profile.get("case_studies")):
        if not isinstance(study, dict):
            continue
        file_id = str(study.get("fileid") or study.get("fileId") or "")
        primary = "zoho-file:" + file_id if file_id.isdigit() else ""
        products = classify_products("")
        status, reason = hold_for("zoho_file" if primary else "none", "unknown")
        rows.append({
            "story_id": story_id(pid, study.get("casestudytitle"), file_id, "old"),
            "partner_id": pid,
            "partner": company,
            "website": website,
            "customer": study.get("casestudytitle") or study.get("filename") or "",
            "country": "",
            "industry": "",
            "source": "case_studies",
            "source_kind": "zoho_file" if primary else "none",
            "primary": primary,
            "urls": [],
            "file_id": file_id if file_id.isdigit() else "",
            "description": study.get("filename") or "",
            "testimonial": "",
            "product_ids": [],
            "product_names": [],
            "scope": "unknown",
            "status": status,
            "hold_reason": reason,
            "flags": ["product not on the old case-study record"],
        })
    return rows


def main():
    profiles = load_profiles()
    stories = []
    for profile in profiles:
        stories.extend(rows_for(profile))
    STORIES.parent.mkdir(parents=True, exist_ok=True)
    with STORIES.open("w") as handle:
        for story in stories:
            handle.write(json.dumps(story, ensure_ascii=True) + "\n")
    from collections import Counter
    print(f"profiles={len(profiles)} stories={len(stories)}")
    print("status", Counter(story["status"] for story in stories))
    print("scope", Counter(story["scope"] for story in stories))
    print("kind", Counter(story["source_kind"] for story in stories))
    ready = [story for story in stories if story["status"] == "ready"]
    print("ready", len(ready), "files", sum(1 for story in ready if story["source_kind"] == "zoho_file"))


if __name__ == "__main__":
    main()
