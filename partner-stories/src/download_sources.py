#!/usr/bin/env python3
"""Download ready Zoho-hosted case-study files and save extracted text.

Web pages are a later pass. This pass only takes file ids the directory
already hosts, and only for stories marked ready or needs_product.
"""

import json
import re
import subprocess
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STORIES = ROOT / "data" / "stories.jsonl"
FILES = ROOT / "data" / "files"
TEXT = ROOT / "data" / "text"
FILE_URL = "https://store.zoho.com/FileDownloadPublic?fileId={file_id}"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
    "Accept": "*/*",
    "Referer": "https://www.zoho.com/partners/find-partner-profile.html",
}


def load_stories():
    rows = []
    for line in STORIES.read_text(errors="replace").splitlines():
        if line.strip():
            rows.append(json.loads(line))
    return rows


def save_stories(rows):
    with STORIES.open("w") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=True) + "\n")


def extension_for(content_type, body):
    content_type = (content_type or "").lower()
    if "pdf" in content_type or body[:4] == b"%PDF":
        return ".pdf"
    if "html" in content_type or body[:1] == b"<":
        return ".html"
    if "word" in content_type or body[:2] == b"PK":
        return ".docx"
    return ".bin"


def extract_text(path):
    if path.suffix == ".html":
        raw = path.read_text(errors="replace")
        text = re.sub(r"(?is)<script.*?>.*?</script>|<style.*?>.*?</style>", " ", raw)
        text = re.sub(r"(?s)<[^>]+>", " ", text)
        return re.sub(r"\s+", " ", text).strip()
    if path.suffix == ".pdf":
        result = subprocess.run(
            ["pdftotext", "-layout", str(path), "-"],
            capture_output=True,
            text=True,
            timeout=60,
        )
        if result.returncode == 0 and result.stdout.strip():
            return result.stdout
        return ""
    return ""


def download_one(story):
    FILES.mkdir(parents=True, exist_ok=True)
    TEXT.mkdir(parents=True, exist_ok=True)
    file_id = story["file_id"]
    request = urllib.request.Request(FILE_URL.format(file_id=file_id), headers=HEADERS)
    with urllib.request.urlopen(request, timeout=60) as response:
        body = response.read()
        content_type = response.headers.get("Content-Type", "")
        status = response.status
    suffix = extension_for(content_type, body)
    path = FILES / f"{story['story_id']}{suffix}"
    path.write_bytes(body)
    text = extract_text(path)
    text_path = TEXT / f"{story['story_id']}.txt"
    text_path.write_text(text)
    return {
        "http_status": status,
        "content_type": content_type.split(";")[0],
        "bytes": len(body),
        "file": str(path.relative_to(ROOT)),
        "text_file": str(text_path.relative_to(ROOT)),
        "text_chars": len(text.strip()),
    }


def main():
    rows = load_stories()
    targets = [
        row for row in rows
        if row.get("source_kind") == "zoho_file"
        and row.get("file_id")
        and row.get("status") in ("ready", "needs_product")
        and not row.get("downloaded")
    ]
    print(f"to_download={len(targets)}", flush=True)
    done = 0
    failed = 0
    for index, story in enumerate(targets, 1):
        try:
            result = download_one(story)
            story.update(result)
            story["downloaded"] = True
            if result["text_chars"] < 80:
                story["status"] = "held"
                story["hold_reason"] = "file has no text layer"
            else:
                story["status"] = "fetched"
            done += 1
            print(f"{index}/{len(targets)} {story['partner']} {result['bytes']} chars={result['text_chars']}", flush=True)
        except Exception as error:
            story["downloaded"] = False
            story["download_error"] = str(error)[:300]
            failed += 1
            print(f"{index}/{len(targets)} FAIL {story['partner']} {error}", flush=True)
            if any(code in str(error) for code in ("400", "403", "429")):
                print("throttle, sleeping 8 minutes", flush=True)
                save_stories(rows)
                time.sleep(480)
        if index % 10 == 0:
            save_stories(rows)
        time.sleep(1.2)
    save_stories(rows)
    print(f"DOWNLOAD_DONE ok={done} failed={failed}", flush=True)


if __name__ == "__main__":
    main()
