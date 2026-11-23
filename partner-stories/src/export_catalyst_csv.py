"""Export the story catalog to a CSV that matches the PartnerStories Data Store table.

Usage: python3 export_catalyst_csv.py [catalog.jsonl] [out.csv]
Load with: catalyst ds:import out.csv --table PartnerStories
"""

import csv
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
DEFAULT_CATALOG = HERE.parent / "catalog" / "stories.jsonl"
DEFAULT_OUT = HERE.parent / "catalyst" / "partner_stories_import.csv"

COLUMNS = [
    "story_id", "partner", "partner_id", "customer", "country", "industry",
    "product_names", "scope", "status", "hold_reason", "source_kind",
    "primary_link", "file_id", "stratus_key", "flags", "draft",
]


def row_for(record: dict) -> dict:
    return {
        "story_id": record.get("story_id", ""),
        "partner": record.get("partner", ""),
        "partner_id": record.get("partner_id", ""),
        "customer": record.get("customer", ""),
        "country": record.get("country", ""),
        "industry": record.get("industry", ""),
        "product_names": ", ".join(record.get("product_names") or []),
        "scope": record.get("scope", ""),
        "status": record.get("status", ""),
        "hold_reason": record.get("hold_reason", ""),
        "source_kind": record.get("source_kind", ""),
        "primary_link": record.get("primary", ""),
        "file_id": str(record.get("file_id") or ""),
        "stratus_key": "",
        "flags": ", ".join(record.get("flags") or []),
        "draft": "",
    }


def main() -> None:
    catalog = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_CATALOG
    out = Path(sys.argv[2]) if len(sys.argv) > 2 else DEFAULT_OUT
    out.parent.mkdir(parents=True, exist_ok=True)
    count = 0
    with catalog.open(encoding="utf-8") as src, out.open("w", newline="", encoding="utf-8") as dst:
        writer = csv.DictWriter(dst, fieldnames=COLUMNS)
        writer.writeheader()
        for line in src:
            if not line.strip():
                continue
            writer.writerow(row_for(json.loads(line)))
            count += 1
    print(f"wrote {count} rows to {out}")


if __name__ == "__main__":
    main()
