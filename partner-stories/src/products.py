"""Zoho service ids used on Find a Partner case studies."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SERVICES_PATH = ROOT / "catalyst" / "zoho-service-ids.json"

# Stories we rewrite name these products. CRM Plus is the bundle that contains them.
IN_SCOPE_IDS = {"2": "CRM", "4501": "Desk", "4701": "Campaigns"}
CRM_PLUS_IDS = {"180000": "CRM Plus", "240000": "CRM Plus", "970000": "CRM Plus"}


def load_services():
    if not SERVICES_PATH.exists():
        return {}
    return json.loads(SERVICES_PATH.read_text())


def parse_product_ids(raw):
    if raw is None:
        return []
    if isinstance(raw, list):
        return [str(item).strip() for item in raw if str(item).strip()]
    if isinstance(raw, (int, float)):
        return [str(int(raw))]
    text = str(raw).strip()
    if not text or text in ("[]", "null", "-", "None"):
        return []
    try:
        parsed = json.loads(text)
    except json.JSONDecodeError:
        parsed = None
    if isinstance(parsed, list):
        return [str(item).strip() for item in parsed if str(item).strip()]
    return [part.strip() for part in text.split(",") if part.strip()]


def classify_products(raw):
    """Return scope, names, and whether a bundle still needs its products named."""
    services = load_services()
    ids = parse_product_ids(raw)
    names = [services.get(item, item) for item in ids]
    in_scope = [IN_SCOPE_IDS[item] for item in ids if item in IN_SCOPE_IDS]
    bundle = [CRM_PLUS_IDS[item] for item in ids if item in CRM_PLUS_IDS]
    if in_scope or bundle:
        scope = "in_scope"
    elif not ids:
        scope = "unknown"
    else:
        scope = "out_of_scope"
    return {
        "ids": ids,
        "names": names,
        "scope": scope,
        "in_scope_products": in_scope,
        "bundle": bool(bundle) and not in_scope,
    }
