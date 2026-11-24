#!/usr/bin/env python3
"""Pull every Find a Partner profile at a pace the directory accepts.

Saves a slim record: company, website, and case studies. Contact emails and
phone numbers on the profile are not stored.
"""

import json
import re
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
PROFILES = DATA / "profiles.jsonl"
LISTING = DATA / "toppartners.js"
LOG = DATA / "index.log"

LIST_URL = "https://store.zoho.com/partnerlisting/toppartners?callback=getAllDetails"
PROFILE_URL = "https://store.zoho.com/partnerlisting/partnerid?id={pid}&callback=getPartnerDetails"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
    "Accept": "*/*",
    "Referer": "https://www.zoho.com/partners/find-partner-profile.html",
}
PAUSE_SECONDS = 2.2


def log(message):
    DATA.mkdir(parents=True, exist_ok=True)
    line = message.rstrip() + "\n"
    with LOG.open("a") as handle:
        handle.write(line)
    print(line, end="", flush=True)


def fetch_text(url):
    request = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(request, timeout=40) as response:
        return response.read().decode("utf-8", "replace")


def load_listing():
    if not LISTING.exists() or LISTING.stat().st_size < 1000:
        log("downloading partner list")
        LISTING.write_text(fetch_text(LIST_URL))
    raw = LISTING.read_text(errors="replace")
    match = re.search(r"getAllDetails\((.*)\)\s*;?\s*$", raw, re.S)
    if not match:
        raise SystemExit("partner list was not JSONP")
    return json.loads(match.group(1))


def done_ids():
    found = set()
    if not PROFILES.exists():
        return found
    for line in PROFILES.read_text(errors="replace").splitlines():
        if not line.strip():
            continue
        try:
            record = json.loads(line)
        except json.JSONDecodeError:
            continue
        if record.get("ok") and record.get("encryptedpid"):
            found.add(record["encryptedpid"])
    return found


def slim(partner, profile):
    studies = profile.get("new_case_studies")
    if not isinstance(studies, list):
        studies = []
    return {
        "ok": True,
        "encryptedpid": partner.get("encryptedpid"),
        "companyname": profile.get("companyname") or partner.get("companyname"),
        "website": profile.get("website") or partner.get("website") or "",
        "tier": profile.get("tier") or partner.get("tier") or "",
        "country": partner.get("country") or [],
        "new_case_studies": studies,
        "case_studies": profile.get("case_studies") or "",
    }


def fetch_profile(pid):
    body = fetch_text(PROFILE_URL.format(pid=pid))
    match = re.search(r"getPartnerDetails\((.*)\)\s*;?\s*$", body, re.S)
    if not match:
        raise RuntimeError("profile response was not JSONP")
    return json.loads(match.group(1))


def main():
    partners = load_listing()
    finished = done_ids()
    todo = [partner for partner in partners if partner.get("encryptedpid") not in finished]
    log(f"partners={len(partners)} already={len(finished)} todo={len(todo)}")
    ok = 0
    errors = 0
    with PROFILES.open("a") as handle:
        for index, partner in enumerate(todo, 1):
            pid = partner["encryptedpid"]
            record = None
            for attempt in range(6):
                try:
                    record = slim(partner, fetch_profile(pid))
                    ok += 1
                    break
                except Exception as error:
                    message = str(error)
                    if any(code in message for code in ("400", "403", "429")):
                        wait = 60 * (8 + attempt * 4)
                        log(f"throttle at {index}/{len(todo)} {partner.get('companyname')} wait {wait}s")
                        time.sleep(wait)
                        continue
                    if attempt < 2:
                        time.sleep(3)
                        continue
                    record = {
                        "ok": False,
                        "encryptedpid": pid,
                        "companyname": partner.get("companyname"),
                        "website": partner.get("website") or "",
                        "error": message,
                    }
                    errors += 1
                    break
            if record is None:
                record = {
                    "ok": False,
                    "encryptedpid": pid,
                    "companyname": partner.get("companyname"),
                    "error": "exhausted",
                }
                errors += 1
            handle.write(json.dumps(record, ensure_ascii=True) + "\n")
            handle.flush()
            if index % 25 == 0 or index == len(todo):
                log(f"progress {index}/{len(todo)} ok={ok} errors={errors}")
            time.sleep(PAUSE_SECONDS)
    log("INDEX_DONE")


if __name__ == "__main__":
    main()
