#!/usr/bin/env python3
"""Fetch in-scope story pages that are ordinary web links, not Zoho files."""

import json
import re
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STORIES = ROOT / "data" / "stories.jsonl"
FILES = ROOT / "data" / "files"
TEXT = ROOT / "data" / "text"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/pdf;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
}


def load_stories():
    return [json.loads(line) for line in STORIES.read_text().splitlines() if line.strip()]


def save_stories(rows):
    with STORIES.open("w") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=True) + "\n")


def html_to_text(body):
    text = re.sub(r"(?is)<script.*?>.*?</script>|<style.*?>.*?</style>", " ", body)
    text = re.sub(r"(?s)<[^>]+>", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def fetch_page(story):
    url = story["primary"]
    request = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(request, timeout=25) as response:
        raw = response.read(150000)
        status = response.status
        final = response.geturl()
        content_type = response.headers.get("Content-Type", "")
    FILES.mkdir(parents=True, exist_ok=True)
    TEXT.mkdir(parents=True, exist_ok=True)
    path = FILES / f"{story['story_id']}.html"
    path.write_bytes(raw)
    text = html_to_text(raw.decode("utf-8", "replace"))
    text_path = TEXT / f"{story['story_id']}.txt"
    text_path.write_text(text)
    return {
        "http_status": status,
        "final_url": final,
        "content_type": content_type.split(";")[0][:80],
        "bytes": len(raw),
        "file": str(path.relative_to(ROOT)),
        "text_file": str(text_path.relative_to(ROOT)),
        "text_chars": len(text),
    }


def hold_reason(error, result):
    message = str(error or "")
    if "401" in message:
        return "login wall"
    if any(code in message for code in ("403", "429")):
        return "site blocked automated access"
    if result and result["text_chars"] < 80:
        return "page returned no readable text"
    return ""


def main():
    rows = load_stories()
    targets = [
        row for row in rows
        if row.get("status") == "ready"
        and row.get("source_kind") == "web"
        and str(row.get("primary", "")).startswith("http")
        and not row.get("downloaded")
    ]
    print(f"to_fetch={len(targets)}", flush=True)
    ok = failed = 0
    for index, story in enumerate(targets, 1):
        try:
            result = fetch_page(story)
            story.update(result)
            story["downloaded"] = True
            reason = hold_reason("", result)
            if reason:
                story["status"] = "held"
                story["hold_reason"] = reason
            else:
                story["status"] = "fetched"
            ok += 1
            print(f"{index}/{len(targets)} {story['partner'][:40]} chars={result['text_chars']}", flush=True)
        except Exception as error:
            story["download_error"] = str(error)[:300]
            story["status"] = "held"
            story["hold_reason"] = hold_reason(error, None) or "page could not be opened"
            failed += 1
            print(f"{index}/{len(targets)} FAIL {story['partner'][:40]} {error}", flush=True)
        if index % 15 == 0:
            save_stories(rows)
        time.sleep(0.8)
    save_stories(rows)
    print(f"PAGES_DONE ok={ok} failed={failed}", flush=True)


if __name__ == "__main__":
    main()
