#!/usr/bin/env python3
"""Copy SOP screenshots into show/images with slide-oriented names, plus CRM capture frames."""

from pathlib import Path
from shutil import copy2

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent
FLOW = ROOT.parent / "process-flow"
IMG = ROOT / "images"

SOP = {
    "05-sop-brands-campuses.png": "03-brands-campuses-stages.png",
    "11-sop-forms-inbound.png": "08-enquiry-forms-inbound-phone.png",
    "13-sop-campus-visit.png": "07-campus-visit-email-whatsapp.png",
    "18-sop-portal-telephony.png": "04-lead-quality-telephony-portal.png",
    "21-sop-reports.png": "05-lead-mgmt-usecases-reports.png",
    "21b-sop-payments-booking.png": "11-qa-payments-forms-booking.png",
}

CRM_FRAMES = [
    ("07-crm-two-campus.png", "Scene 1 · CRM capture", "Leads search  9876543210", "Two Anita Sharma leads on one list\nAarav JP Nagar Enquiry  ·  Diya BTM App Initiated"),
    ("08-crm-sibling.png", "Scene 2 · CRM capture", "Leads search  Reddy", "Kavya Reddy  ·  Sibling Enquiry = true"),
    ("08b-crm-intercampus.png", "Scene 2 · CRM capture", "Leads search  Iyer", "Meera Iyer  ·  Intercampus Enq = true"),
    ("11-crm-nair.png", "Scene 3 · CRM capture", "Leads search  Nair", "Form Status Abandoned  ·  24h reminder task"),
    ("13-crm-menon.png", "Scene 4 · CRM capture", "Leads search  Menon", "Visit Scheduled  ·  18 Sep 2026 10:00  ·  event + tasks"),
    ("13b-crm-das.png", "Scene 4 · CRM capture", "Leads search  Das", "Visit Missed  ·  Visit Status = Missed"),
    ("14-crm-mehta.png", "Scene 5 · CRM capture", "Leads search  Mehta", "Accepted  ·  Founder Decision = Accept"),
    ("16-crm-workflows.png", "Scene 7 · CRM capture", "Setup → Workflow Rules → Ekya", "Six Ekya rules. Do not open EdNova."),
]


def _font(size, bold=False):
    candidates = [
        "/usr/share/fonts/truetype/inter/Inter-Bold.ttf" if bold else "/usr/share/fonts/truetype/inter/Inter-Regular.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    ]
    for path in candidates:
        if Path(path).exists():
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()


def frame(path, kicker, cue, body):
    w, h = 1600, 900
    im = Image.new("RGB", (w, h), (243, 245, 248))
    d = ImageDraw.Draw(im)
    d.rectangle([0, 0, 18, h], fill=(11, 31, 58))
    d.rectangle([18, 0, w, 10], fill=(196, 41, 46))
    d.rectangle([80, 140, w - 80, h - 100], outline=(196, 41, 46), width=3)
    d.rectangle([80, 140, w - 80, h - 100], fill=(255, 255, 255))
    d.text((80, 48), kicker.upper(), fill=(196, 41, 46), font=_font(28, True))
    d.text((100, 200), "Drop live CRM screenshot here", fill=(11, 31, 58), font=_font(42, True))
    d.text((100, 280), cue, fill=(31, 122, 110), font=_font(32, True))
    y = 380
    for line in body.split("\n"):
        d.text((100, y), line, fill=(74, 85, 104), font=_font(28))
        y += 48
    d.text((80, h - 70), "Capture in Cooper and Co CRM before the call. Do not use a mock UI.", fill=(107, 118, 136), font=_font(22))
    im.save(path, "PNG")


def main():
    IMG.mkdir(exist_ok=True)
    for dest, src in SOP.items():
        copy2(FLOW / src, IMG / dest)
        print("copied", dest)
    for name, kicker, cue, body in CRM_FRAMES:
        frame(IMG / name, kicker, cue, body)
        print("frame", name)


if __name__ == "__main__":
    main()
