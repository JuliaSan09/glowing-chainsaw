"""How a Find a Partner case study decides its clickable link."""

import re

URL_RE = re.compile(r"https?://[^\s\"'<>)\]]+", re.I)
SOCIAL_SUFFIXES = (
    "facebook.com",
    "fb.com",
    "fb.watch",
    "instagram.com",
    "linkedin.com",
    "twitter.com",
    "x.com",
    "youtube.com",
    "youtu.be",
    "tiktok.com",
    "vm.tiktok.com",
    "t.me",
    "telegram.me",
    "wa.me",
    "whatsapp.com",
    "threads.net",
    "pinterest.com",
    "reddit.com",
    "vimeo.com",
)


def clean_url(url):
    return url.strip().rstrip(".,;")


def host_of(url):
    match = re.match(r"https?://([^/]+)", url, re.I)
    if not match:
        return ""
    host = match.group(1).lower().split(":")[0]
    if host.startswith("www."):
        host = host[4:]
    return host


def is_social(url):
    host = host_of(url)
    return any(host == suffix or host.endswith("." + suffix) for suffix in SOCIAL_SUFFIXES)


def is_file_id(value):
    text = str(value).strip()
    return text.isdigit() and len(text) >= 5


def urls_in(value):
    if value is None:
        return []
    text = str(value).strip()
    if not text or text in ("-", "-1", "None", "null"):
        return []
    return [clean_url(url) for url in URL_RE.findall(text)]


def resolve_token(value):
    if value is None:
        return None
    text = str(value).strip()
    if not text or text in ("-", "None", "null", "-1"):
        return None
    if text.lower().startswith("http"):
        return clean_url(text)
    if is_file_id(text):
        return "zoho-file:" + text
    return None


def primary_link(case_link, testimonial_link):
    """Same choice the partner profile page makes when a story is clicked."""
    case_text = "" if case_link is None else str(case_link).strip()
    if case_text == "-1":
        return resolve_token(testimonial_link)
    resolved = resolve_token(case_link)
    if resolved:
        return resolved
    return resolve_token(testimonial_link)


def story_urls(record):
    primary = primary_link(record.get("casestudy_link"), record.get("testimonial_link"))
    found = []
    if isinstance(primary, str) and primary.startswith("http"):
        found.append(primary)
    for field in ("casestudy_link", "testimonial_link", "casestudy_description"):
        found.extend(urls_in(record.get(field)))
    unique = []
    seen = set()
    for url in found:
        if url not in seen:
            seen.add(url)
            unique.append(url)
    return primary or "", unique
