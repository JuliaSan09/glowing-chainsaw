#!/usr/bin/env python3
"""Turn extracted source text into a customers-page draft and a flag list.

Quotes and figures are copied from the source. A missing section is left out.
The draft is not published.
"""

import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

ROOT = Path(__file__).resolve().parents[1]
STORIES = ROOT / "data" / "stories.jsonl"
TEXT = ROOT / "data" / "text"
DRAFTS = ROOT / "data" / "drafts"

QUOTE_RE = re.compile(r"[\"“](.{20,400}?)[\"”]")
FIGURE_RE = re.compile(
    r"\b\d[\d,.]*(?:\s*%|\s*x\b|\s*(?:hours?|hrs?|days?|weeks?|months?|minutes?|mins?)\b)",
    re.I,
)
PRODUCT_WORDS = ("Zoho CRM", "Zoho Desk", "Zoho Campaigns", "Zoho One", "CRM Plus")


def quotes_in(text):
    found = []
    for match in QUOTE_RE.finditer(text):
        quote = re.sub(r"\s+", " ", match.group(1)).strip()
        if quote and quote not in found:
            found.append(quote)
    return found


def figures_in(text):
    found = []
    for match in FIGURE_RE.finditer(text):
        start = max(0, match.start() - 80)
        end = min(len(text), match.end() + 80)
        window = re.sub(r"\s+", " ", text[start:end]).strip()
        if window not in found:
            found.append(window)
    return found[:8]


def products_named(text):
    return [name for name in PRODUCT_WORDS if name.lower() in text.lower()]


def quote_flags(quote, partner):
    flags = []
    lowered = quote.lower()
    partner_name = (partner or "").split(",")[0].strip().lower()
    if partner_name and partner_name in lowered:
        flags.append("The quote names the partner.")
    if not any(word in lowered for word in ("zoho crm", "zoho desk", "zoho campaigns", "crm plus")):
        flags.append("The quote names no Zoho product.")
    outcome_words = ("save", "saved", "hour", "day", "week", "roi", "pipeline", "faster", "reduced", "increase", "%", "minute")
    if not any(word in lowered for word in outcome_words):
        flags.append("The quote has no outcome.")
    return flags


def build_draft(story, text):
    quotes = quotes_in(text)
    figures = figures_in(text)
    named = products_named(text)
    flags = list(story.get("flags") or [])
    if story.get("scope") == "unknown" and not any(item in named for item in ("Zoho CRM", "Zoho Desk", "Zoho Campaigns")):
        flags.append("The product is outside CRM, Desk, and Campaigns, or it is not named.")
    if not quotes:
        flags.append("There is no partner quote to move.")
    else:
        flags.extend(quote_flags(quotes[0], story.get("partner")))
    flags.append("We do not know if the person quoted is still there.")
    # Preserve order and drop duplicates.
    unique_flags = []
    for flag in flags:
        if flag not in unique_flags:
            unique_flags.append(flag)

    customer = story.get("customer") or "the customer"
    product = "Zoho CRM"
    if "Zoho Desk" in named and "Zoho CRM" not in named:
        product = "Zoho Desk"
    elif "Zoho Campaigns" in named and "Zoho CRM" not in named:
        product = "Zoho Campaigns"

    lines = [f"# {customer} runs its work in {product}", ""]
    if quotes:
        lines.append(f"\"{quotes[0]}\"")
        lines.append("")
        lines.append("Attribution is not in the source as a name, title, and company line yet.")
        lines.append("")
    if len(figures) >= 2:
        lines.append("## Key results:")
        for figure in figures[:4]:
            lines.append(f"- {figure}")
        lines.append("")
    lines.append("## The company")
    lines.append(f"{customer} is the customer named on the partner story from {story.get('partner') or 'the partner'}.")
    if story.get("industry") or story.get("country"):
        lines.append(f"Industry: {story.get('industry') or 'not stated'}. Country: {story.get('country') or 'not stated'}.")
    lines.append("")
    lines.append("## The challenge")
    lines.append("The source text is stored beside this draft. The previous system is included here only when the source names it.")
    lines.append("")
    lines.append("## The solution")
    if named:
        lines.append("Products named in the source: " + ", ".join(named) + ".")
    else:
        lines.append("The source does not name Zoho CRM, Zoho Desk, or Zoho Campaigns in a way this pass could point at.")
    lines.append("")
    lines.append("## Benefits and ROI")
    if figures:
        lines.append("Figures copied from the source, with the words around them:")
        for figure in figures:
            lines.append(f"- {figure}")
    else:
        lines.append("The source does not state a figure. None is added.")
    lines.append("")
    lines.append("## Partner engagement")
    lines.append(f"{story.get('partner') or 'The partner'} is the partner on the Find a Partner record for this story.")
    lines.append("")
    lines.append("## Flags")
    for flag in unique_flags:
        lines.append(f"- {flag}")
    lines.append("")
    lines.append(f"Source file: {story.get('text_file') or 'not saved'}")
    return "\n".join(lines).strip() + "\n", unique_flags


def main():
    story_id = sys.argv[1] if len(sys.argv) > 1 else ""
    rows = [json.loads(line) for line in STORIES.read_text().splitlines() if line.strip()]
    chosen = [row for row in rows if row.get("status") == "fetched" and row.get("text_chars", 0) >= 80]
    if story_id:
        chosen = [row for row in rows if row["story_id"] == story_id]
    if not chosen:
        raise SystemExit("no fetched story to draft")
    story = chosen[0]
    text = (TEXT / f"{story['story_id']}.txt").read_text(errors="replace")
    draft, flags = build_draft(story, text)
    DRAFTS.mkdir(parents=True, exist_ok=True)
    path = DRAFTS / f"{story['story_id']}.md"
    path.write_text(draft)
    story["status"] = "drafted"
    story["flags"] = flags
    story["draft_file"] = str(path.relative_to(ROOT))
    with STORIES.open("w") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=True) + "\n")
    print(path)
    print("flags", len(flags))


if __name__ == "__main__":
    main()
