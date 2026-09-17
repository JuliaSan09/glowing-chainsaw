#!/usr/bin/env python3
"""Build the Ekya / CMR admissions demo deck for Zoho Show (import as PPTX)."""

from pathlib import Path

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN
from pptx.oxml.ns import qn
from pptx.util import Inches, Pt
from lxml import etree

NAVY = RGBColor(0x0B, 0x1F, 0x3A)
NAVY2 = RGBColor(0x14, 0x32, 0x58)
RED = RGBColor(0xC4, 0x29, 0x2E)
GOLD = RGBColor(0xC4, 0x8A, 0x2B)
SLATE = RGBColor(0x4A, 0x55, 0x68)
MUTED = RGBColor(0x6B, 0x76, 0x88)
LIGHT = RGBColor(0xF3, 0xF5, 0xF8)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
INK = RGBColor(0x1B, 0x24, 0x33)
TEAL = RGBColor(0x1F, 0x7A, 0x6E)

W = Inches(13.333)
H = Inches(7.5)
OUT = Path(__file__).with_name("Ekya-CMR-Admissions-Demo.pptx")


def _set_run(run, size, color, bold=False, italic=False, font_name="Calibri"):
    run.font.size = Pt(size)
    run.font.color.rgb = color
    run.font.bold = bold
    run.font.italic = italic
    run.font.name = font_name
    rPr = run._r.get_or_add_rPr()
    ea = rPr.find(qn("a:ea"))
    if ea is None:
        ea = etree.SubElement(rPr, qn("a:ea"))
    ea.set("typeface", font_name)


def add_text(tf, text, size, color, bold=False, italic=False, align=PP_ALIGN.LEFT, space_after=6):
    p = tf.paragraphs[0] if not tf.paragraphs[0].text else tf.add_paragraph()
    p.alignment = align
    p.space_after = Pt(space_after)
    run = p.add_run()
    run.text = text
    _set_run(run, size, color, bold, italic)
    return p


def box(slide, l, t, w, h, fill=None, line=None):
    sh = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, l, t, w, h)
    sh.shadow.inherit = False
    sh.fill.solid()
    sh.fill.fore_color.rgb = fill or WHITE
    if line is None:
        sh.line.fill.background()
    else:
        sh.line.color.rgb = line
    return sh


def tb(slide, l, t, w, h):
    return slide.shapes.add_textbox(l, t, w, h)


def set_notes(slide, text):
    notes = slide.notes_slide.notes_text_frame
    notes.text = text


def footer(slide, scene, cue=None, dark=False):
    color = RGBColor(0xB8, 0xC4, 0xD4) if dark else MUTED
    t = tb(slide, Inches(0.55), Inches(7.12), Inches(9.2), Inches(0.28))
    tf = t.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    run = p.add_run()
    run.text = f"Ekya / CMR admissions  ·  {scene}"
    _set_run(run, 11, color)
    if cue:
        t2 = tb(slide, Inches(7.4), Inches(7.12), Inches(5.4), Inches(0.28))
        tf2 = t2.text_frame
        tf2.word_wrap = True
        p2 = tf2.paragraphs[0]
        p2.alignment = PP_ALIGN.RIGHT
        run2 = p2.add_run()
        run2.text = cue
        _set_run(run2, 11, RED if not dark else GOLD, bold=True)


def rail(slide):
    box(slide, Inches(0), Inches(0), Inches(0.14), H, NAVY)
    box(slide, Inches(0.14), Inches(0), W - Inches(0.14), Inches(0.08), RED)


def kicker(slide, text, y=Inches(0.28)):
    t = tb(slide, Inches(0.55), y, Inches(12.2), Inches(0.32))
    tf = t.text_frame
    p = tf.paragraphs[0]
    run = p.add_run()
    run.text = text.upper()
    _set_run(run, 12, RED, bold=True)
    # letter-spacing approximation: already uppercase


def title_block(slide, title, subtitle=None, y=Inches(0.55)):
    t = tb(slide, Inches(0.55), y, Inches(12.2), Inches(0.7))
    tf = t.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    run = p.add_run()
    run.text = title
    _set_run(run, 28, NAVY, bold=True)
    if subtitle:
        t2 = tb(slide, Inches(0.55), y + Inches(0.62), Inches(12.2), Inches(0.4))
        tf2 = t2.text_frame
        tf2.word_wrap = True
        p2 = tf2.paragraphs[0]
        run2 = p2.add_run()
        run2.text = subtitle
        _set_run(run2, 16, SLATE)


def bullets(slide, items, l, t, w, h, size=16, color=INK):
    shape = tb(slide, l, t, w, h)
    tf = shape.text_frame
    tf.word_wrap = True
    for i, item in enumerate(items):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.level = 0
        p.space_after = Pt(10)
        pPr = p._p.get_or_add_pPr()
        buFont = etree.SubElement(pPr, qn("a:buFont"))
        buFont.set("typeface", "Calibri")
        buChar = etree.SubElement(pPr, qn("a:buChar"))
        buChar.set("char", "•")
        run = p.add_run()
        run.text = item
        _set_run(run, size, color)
    return shape


def cue_card(slide, label, body, l, t, w, h):
    sh = box(slide, l, t, w, h, LIGHT)
    t1 = tb(slide, l + Inches(0.22), t + Inches(0.12), w - Inches(0.4), Inches(0.28))
    tf = t1.text_frame
    p = tf.paragraphs[0]
    run = p.add_run()
    run.text = label.upper()
    _set_run(run, 11, RED, bold=True)
    t2 = tb(slide, l + Inches(0.22), t + Inches(0.4), w - Inches(0.4), h - Inches(0.5))
    tf2 = t2.text_frame
    tf2.word_wrap = True
    p2 = tf2.paragraphs[0]
    run2 = p2.add_run()
    run2.text = body
    _set_run(run2, 15, NAVY, bold=True)


def new_prs():
    prs = Presentation()
    prs.slide_width = W
    prs.slide_height = H
    return prs


def blank(prs):
    layout = prs.slide_layouts[6]  # blank
    return prs.slides.add_slide(layout)


def add_title_slide(prs):
    s = blank(prs)
    box(s, Inches(0), Inches(0), W, H, NAVY)
    box(s, Inches(0), Inches(0), Inches(0.18), H, RED)
    box(s, Inches(0), Inches(6.85), W, Inches(0.65), NAVY2)
    t = tb(s, Inches(0.7), Inches(1.7), Inches(11.8), Inches(0.4))
    p = t.text_frame.paragraphs[0]
    run = p.add_run()
    run.text = "ZOHO CRM  ·  ADMISSIONS EVALUATION"
    _set_run(run, 14, GOLD, bold=True)
    t = tb(s, Inches(0.7), Inches(2.2), Inches(11.8), Inches(1.6))
    tf = t.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    run = p.add_run()
    run.text = "Connected admissions across\nfour brands and every campus"
    _set_run(run, 36, WHITE, bold=True)
    t = tb(s, Inches(0.7), Inches(4.15), Inches(11.8), Inches(0.9))
    tf = t.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    run = p.add_run()
    run.text = "Ekya Schools  ·  Ekya Nava  ·  CMR NPS  ·  CMR NPUC"
    _set_run(run, 18, RGBColor(0xD5, 0xDE, 0xEA))
    t = tb(s, Inches(0.7), Inches(6.98), Inches(11.8), Inches(0.35))
    p = t.text_frame.paragraphs[0]
    run = p.add_run()
    run.text = "Demo presentation  ·  20 minutes  ·  Follow with live CRM  ·  Cooper and Co org60040760589"
    _set_run(run, 13, RGBColor(0xB8, 0xC4, 0xD4))
    set_notes(
        s,
        "Open this deck in Zoho Show. Keep CRM in a second window.\n"
        "Say: This is one CRM for the group. We will walk four brands, from first enquiry to founder accept.\n"
        "Then: I will cue each scene here, then we click the live record.",
    )


def add_agenda(prs):
    s = blank(prs)
    rail(s)
    kicker(s, "Presenting order")
    title_block(s, "Nine scenes. Same order as the live CRM demo.")
    rows = [
        ("00:00", "0", "Four brands, one CRM", "Accounts → Ekya | CMR Group"),
        ("01:30", "1", "Same phone, two campuses", "Leads → 9876543210"),
        ("04:00", "2", "Sibling and intercampus", "Reddy, then Iyer"),
        ("06:00", "3", "Phone, database, abandoned form", "Joseph → Banerjee → Nair"),
        ("09:00", "4", "Campus visit booked and missed", "Menon, then Das"),
        ("12:00", "5", "Submit → HOS → waitlist or accept", "Khan → Rao → Patel → Mehta"),
        ("16:00", "6", "PU is a different journey", "Gowda + Deals"),
        ("17:30", "7", "What is already automated", "Setup → Ekya workflows"),
        ("19:00", "8", "Close and go-live", "Questions"),
    ]
    y0 = Inches(1.45)
    header = ["Time", "Scene", "On this slide", "Then open in CRM"]
    widths = [Inches(1.2), Inches(0.9), Inches(4.6), Inches(5.1)]
    x0 = Inches(0.55)
    # header bar
    box(s, x0, y0, Inches(12.2), Inches(0.38), NAVY)
    x = x0 + Inches(0.15)
    for htxt, w in zip(header, widths):
        t = tb(s, x, y0 + Inches(0.05), w, Inches(0.3))
        p = t.text_frame.paragraphs[0]
        run = p.add_run()
        run.text = htxt
        _set_run(run, 12, WHITE, bold=True)
        x += w
    for i, (time, scene, title, crm) in enumerate(rows):
        y = y0 + Inches(0.38) + Inches(i * 0.52)
        fill = LIGHT if i % 2 == 0 else WHITE
        box(s, x0, y, Inches(12.2), Inches(0.52), fill)
        vals = [time, scene, title, crm]
        x = x0 + Inches(0.15)
        for j, (val, w) in enumerate(zip(vals, widths)):
            t = tb(s, x, y + Inches(0.1), w, Inches(0.32))
            p = t.text_frame.paragraphs[0]
            run = p.add_run()
            run.text = val
            _set_run(run, 14, NAVY if j == 2 else SLATE, bold=(j == 2))
            x += w
    footer(s, "Agenda")
    set_notes(
        s,
        "Say: We stay in this order. I show a cue slide, then we click CRM. "
        "Use Ekya Lead Stage, not Admission Stage. We will not edit the showcase records.",
    )


def add_ground_rules(prs):
    s = blank(prs)
    rail(s)
    kicker(s, "Before we click")
    title_block(s, "How to watch this demo")
    cards = [
        ("Look at", "Ekya Lead Stage, Brand, Campus, App Type, Form Status, Visit Status, Founder Decision."),
        ("Ignore", "Admission Stage. That picklist belongs to an older process in this org."),
        ("Do not edit", "Sharma, Menon, Das, Rao, Patel, or Mehta while the customer is watching."),
        ("Parking lot", "Parent portal, live WhatsApp, VOIP/IVR, payments, Bookings, Campaigns, Forms OTP."),
    ]
    for i, (h, body) in enumerate(cards):
        col = i % 2
        row = i // 2
        l = Inches(0.55) + Inches(col * 6.25)
        t = Inches(1.55) + Inches(row * 2.35)
        box(s, l, t, Inches(5.95), Inches(2.15), LIGHT)
        box(s, l, t, Inches(0.12), Inches(2.15), RED if i != 1 else GOLD)
        tt = tb(s, l + Inches(0.4), t + Inches(0.28), Inches(5.3), Inches(0.4))
        p = tt.text_frame.paragraphs[0]
        run = p.add_run()
        run.text = h
        _set_run(run, 18, NAVY, bold=True)
        bb = tb(s, l + Inches(0.4), t + Inches(0.8), Inches(5.3), Inches(1.1))
        tf = bb.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        run = p.add_run()
        run.text = body
        _set_run(run, 16, SLATE)
    footer(s, "Ground rules")
    set_notes(
        s,
        "Say this once. Then hide Setup until Scene 7. CRM tabs already open: Leads, Accounts, Deals, Workflows.",
    )


def add_scene0(prs):
    s = blank(prs)
    rail(s)
    kicker(s, "Scene 0  ·  0:00–1:30")
    title_block(s, "Four brands. One CRM.")
    bullets(
        s,
        [
            "The group account holds Ekya Schools, Ekya Nava, CMR NPS, CMR NPUC, and Ekya Vana Early Years.",
            "Campuses sit under the brand. Early Years and future campuses add as accounts, not new modules.",
            "K-12 and PU are different admissions processes. Brand, Campus, Grade, and App Type split the journey.",
            "Campus accounts are locations. They are not finance legal entities.",
        ],
        Inches(0.55),
        Inches(1.55),
        Inches(7.4),
        Inches(4.6),
        18,
    )
    cue_card(
        s,
        "Open in CRM",
        "Accounts → Ekya | CMR Group\nExpand brand and campus children.\nID 902823000002022001",
        Inches(8.15),
        Inches(1.55),
        Inches(4.6),
        Inches(4.4),
    )
    footer(s, "Scene 0", "CRM · Accounts")
    set_notes(
        s,
        "SAY: This is one CRM for the group. Ekya Schools, Nava, CMR NPS, and CMR PU College are brands. "
        "Campuses sit under the brand. Early Years and future campuses can be added here without a new module.\n\n"
        "K-12 and PU are not the same admissions process. Every enquiry carries Brand, Campus, Grade, and App Type "
        "so the journey, the owner, and the dashboard can split.\n\n"
        "DO NOT open finance / Books.",
    )


def add_campus_map(prs):
    s = blank(prs)
    rail(s)
    kicker(s, "Scene 0  ·  still on Accounts")
    title_block(s, "Brands and campuses in this org")
    rows = [
        ("Ekya Schools", "JP Nagar, BTM Layout, ITPL, Byrathi, NICE Road", "K-12"),
        ("CMR National Public School", "HRBR Layout", "K-12"),
        ("Ekya Nava", "Panathur", "K-12"),
        ("CMR National PU College", "HRBR, BTM, ITPL, Byrathi, NICE Road", "PU"),
        ("Ekya Vana Early Years", "Campus X, Y, Z (placeholders)", "K-12"),
    ]
    y0 = Inches(1.5)
    box(s, Inches(0.55), y0, Inches(12.2), Inches(0.42), NAVY)
    for x, txt, w in (
        (Inches(0.7), "Brand", Inches(4.0)),
        (Inches(4.8), "Campuses", Inches(5.6)),
        (Inches(10.6), "App type", Inches(1.9)),
    ):
        t = tb(s, x, y0 + Inches(0.06), w, Inches(0.3))
        p = t.text_frame.paragraphs[0]
        run = p.add_run()
        run.text = txt
        _set_run(run, 13, WHITE, bold=True)
    for i, (brand, campuses, app) in enumerate(rows):
        y = y0 + Inches(0.42) + Inches(i * 0.78)
        box(s, Inches(0.55), y, Inches(12.2), Inches(0.78), LIGHT if i % 2 == 0 else WHITE)
        t = tb(s, Inches(0.7), y + Inches(0.2), Inches(4.0), Inches(0.42))
        p = t.text_frame.paragraphs[0]
        run = p.add_run()
        run.text = brand
        _set_run(run, 16, NAVY, bold=True)
        t = tb(s, Inches(4.8), y + Inches(0.2), Inches(5.6), Inches(0.42))
        p = t.text_frame.paragraphs[0]
        run = p.add_run()
        run.text = campuses
        _set_run(run, 15, SLATE)
        t = tb(s, Inches(10.6), y + Inches(0.2), Inches(1.9), Inches(0.42))
        p = t.text_frame.paragraphs[0]
        run = p.add_run()
        run.text = app
        _set_run(run, 16, TEAL if app == "PU" else NAVY, bold=True)
    footer(s, "Scene 0", "CRM · stay on Accounts")
    set_notes(
        s,
        "Point at brand accounts and a couple of campuses. Mention Maya and Indravadhan as campus owners. "
        "Do not invent Books legal-entity names.",
    )


def add_journey(prs):
    s = blank(prs)
    rail(s)
    kicker(s, "The path we will walk")
    title_block(s, "Ekya Lead Stage — not Admission Stage")
    stages = [
        "Enquiry",
        "App\nInitiated",
        "Visit\nScheduled",
        "Visit\nMissed",
        "App\nSubmitted",
        "HOS\nReview",
        "Founder\nReview",
        "Accepted\n/ Waitlist",
    ]
    n = len(stages)
    total_w = Inches(12.2)
    gap = Inches(0.12)
    card_w = int((total_w - gap * (n - 1)) / n)
    y = Inches(1.7)
    x = Inches(0.55)
    for i, name in enumerate(stages):
        fill = RED if i in (0, 7) else NAVY
        box(s, x, y, card_w, Inches(1.55), fill)
        t = tb(s, x + Inches(0.06), y + Inches(0.28), card_w - Inches(0.12), Inches(1.1))
        tf = t.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.alignment = PP_ALIGN.CENTER
        run = p.add_run()
        run.text = name
        _set_run(run, 13, WHITE, bold=True)
        if i < n - 1:
            t2 = tb(s, x + card_w - Inches(0.05), y + Inches(0.55), Inches(0.22), Inches(0.35))
            p = t2.text_frame.paragraphs[0]
            run = p.add_run()
            run.text = "›"
            _set_run(run, 18, GOLD, bold=True)
        x += card_w + gap
    bullets(
        s,
        [
            "Review and Readiness Session also exist on the picklist. We will not linger there today.",
            "Disqualified and Junk are outcomes, same as Accept and Waitlist.",
            "Each live record you open is already sitting on one of these stages.",
        ],
        Inches(0.55),
        Inches(3.6),
        Inches(12.2),
        Inches(2.6),
        18,
    )
    footer(s, "Journey")
    set_notes(
        s,
        "Say: Everything we open next is a parent on this path. Keep your eye on Ekya Lead Stage.",
    )


def add_scene1(prs):
    s = blank(prs)
    rail(s)
    kicker(s, "Scene 1  ·  1:30–4:00")
    title_block(s, "One mobile number. Two campuses.")
    # two cards
    box(s, Inches(0.55), Inches(1.55), Inches(5.95), Inches(3.55), LIGHT)
    box(s, Inches(6.8), Inches(1.55), Inches(5.95), Inches(3.55), LIGHT)
    left = [
        ("Parent / student", "Anita Sharma / Aarav Sharma"),
        ("Campus", "Ekya JP Nagar"),
        ("Stage", "Enquiry"),
        ("Form", "Not started"),
        ("Search", "9876543210"),
    ]
    right = [
        ("Parent / student", "Anita Sharma / Diya Sharma"),
        ("Campus", "Ekya BTM Layout"),
        ("Stage", "App Initiated"),
        ("Form", "Started"),
        ("Search", "same number"),
    ]
    for col, title, rows in (
        (Inches(0.55), "Lead 1", left),
        (Inches(6.8), "Lead 2", right),
    ):
        t = tb(s, col + Inches(0.3), Inches(1.7), Inches(5.3), Inches(0.4))
        p = t.text_frame.paragraphs[0]
        run = p.add_run()
        run.text = title
        _set_run(run, 14, RED, bold=True)
        for i, (k, v) in enumerate(rows):
            y = Inches(2.15) + Inches(i * 0.52)
            t = tb(s, col + Inches(0.3), y, Inches(1.8), Inches(0.4))
            p = t.text_frame.paragraphs[0]
            run = p.add_run()
            run.text = k
            _set_run(run, 14, MUTED)
            t = tb(s, col + Inches(2.1), y, Inches(3.5), Inches(0.4))
            p = t.text_frame.paragraphs[0]
            run = p.add_run()
            run.text = v
            _set_run(run, 16, NAVY, bold=True)
    t = tb(s, Inches(0.55), Inches(5.3), Inches(12.2), Inches(1.4))
    tf = t.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    run = p.add_run()
    run.text = "If you unique-lock mobile, this family breaks. Each campus keeps its own nurture path."
    _set_run(run, 18, SLATE)
    footer(s, "Scene 1", "CRM · Leads · 9876543210")
    set_notes(
        s,
        "SAY: Anita used one mobile number for two campuses. We did not treat that as a duplicate. "
        "JP Nagar is still an enquiry for Aarav. BTM has already started Diya’s application. "
        "Each campus nurtures its own record.\n\n"
        "If asked whether they can apply twice from the same number: Yes. That was an explicit requirement.\n\n"
        "POINT AT: Brand, Campus, Grade, Student Name, How Heard, OTP Verified, Ekya Lead Stage, Phone.",
    )


def add_scene2(prs):
    s = blank(prs)
    rail(s)
    kicker(s, "Scene 2  ·  4:00–6:00")
    title_block(s, "Sibling and intercampus are flags, not duplicates.")
    box(s, Inches(0.55), Inches(1.55), Inches(5.95), Inches(4.4), LIGHT)
    box(s, Inches(6.8), Inches(1.55), Inches(5.95), Inches(4.4), LIGHT)
    t = tb(s, Inches(0.85), Inches(1.75), Inches(5.4), Inches(0.4))
    p = t.text_frame.paragraphs[0]
    run = p.add_run()
    run.text = "SIBLING"
    _set_run(run, 13, RED, bold=True)
    bullets(
        s,
        [
            "Kavya Reddy / Vihaan Reddy",
            "CMRNPS HRBR · LKG · Enquiry",
            "Sibling Enquiry = true",
            "Search: Reddy",
        ],
        Inches(0.85),
        Inches(2.25),
        Inches(5.3),
        Inches(3.3),
        17,
    )
    t = tb(s, Inches(7.1), Inches(1.75), Inches(5.4), Inches(0.4))
    p = t.text_frame.paragraphs[0]
    run = p.add_run()
    run.text = "INTERCAMPUS"
    _set_run(run, 13, RED, bold=True)
    bullets(
        s,
        [
            "Meera Iyer / Ananya Iyer",
            "Nava Panathur · Grade 5 · Enquiry",
            "Intercampus Enq = true",
            "Previous school: Ekya JP Nagar",
            "Search: Iyer",
        ],
        Inches(7.1),
        Inches(2.25),
        Inches(5.3),
        Inches(3.3),
        17,
    )
    footer(s, "Scene 2", "CRM · Leads · Reddy then Iyer")
    set_notes(
        s,
        "SAY: Sibling and intercampus are flags on the lead, not a second product. "
        "Counsellors see why a second file exists instead of merging the family by accident.\n\n"
        "Meera is moving a child from JP Nagar to Nava Panathur. The previous school is on the record.",
    )


def add_scene3(prs):
    s = blank(prs)
    rail(s)
    kicker(s, "Scene 3  ·  6:00–9:00")
    title_block(s, "Three ways an enquiry lands.")
    cards = [
        ("Inbound phone", "Maria Joseph / Leo Joseph", "How Heard = Inbound Phone\nHotline 080-46809096\nCall Count 1 · BTM · Enquiry\nSearch: Joseph"),
        ("Database upload", "Amit Banerjee / Riya Banerjee", "How Heard = Database Upload\nStage Enquiry · form empty\nNo current-year workflow until the parent acts\nSearch: Banerjee"),
        ("Abandoned form", "Suresh Nair / Nila Nair", "App Initiated · Form Abandoned\nMeta Ads · UKG\nTask: 24h incomplete application\nSearch: Nair"),
    ]
    for i, (h, who, body) in enumerate(cards):
        l = Inches(0.55) + Inches(i * 4.15)
        box(s, l, Inches(1.5), Inches(3.95), Inches(4.85), LIGHT)
        box(s, l, Inches(1.5), Inches(3.95), Inches(0.1), RED)
        t = tb(s, l + Inches(0.22), Inches(1.75), Inches(3.5), Inches(0.35))
        p = t.text_frame.paragraphs[0]
        run = p.add_run()
        run.text = f"3.{chr(97 + i)}  {h}"
        _set_run(run, 14, RED, bold=True)
        t = tb(s, l + Inches(0.22), Inches(2.2), Inches(3.5), Inches(0.7))
        tf = t.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        run = p.add_run()
        run.text = who
        _set_run(run, 16, NAVY, bold=True)
        t = tb(s, l + Inches(0.22), Inches(3.0), Inches(3.5), Inches(3.0))
        tf = t.text_frame
        tf.word_wrap = True
        for j, line in enumerate(body.split("\n")):
            p = tf.paragraphs[0] if j == 0 else tf.add_paragraph()
            p.space_after = Pt(8)
            run = p.add_run()
            run.text = line
            _set_run(run, 15, SLATE)
    footer(s, "Scene 3", "CRM · Joseph → Banerjee → Nair")
    set_notes(
        s,
        "Stay tight: one sentence per record, land on Nair.\n\n"
        "PHONE: Four published hotlines. After VOIP, IVR maps campus. Activity belongs on this lead.\n\n"
        "DATABASE: Last year’s list can live in CRM for nurture. It should not fire this year’s incoming-lead workflow until the parent acts.\n\n"
        "NAIR: She started the form from a paid campaign and did not submit. 24-hour task. "
        "Honest limit: Zoho Forms does not natively push abandoned as a CRM stage.\n\n"
        "Open the 24h incomplete application reminder task on Nair.",
    )


def add_scene4(prs):
    s = blank(prs)
    rail(s)
    kicker(s, "Scene 4  ·  9:00–12:00")
    title_block(s, "Book the visit. Recover the miss.")
    box(s, Inches(0.55), Inches(1.5), Inches(6.05), Inches(4.85), LIGHT)
    box(s, Inches(6.8), Inches(1.5), Inches(5.95), Inches(4.85), LIGHT)
    t = tb(s, Inches(0.85), Inches(1.7), Inches(5.5), Inches(0.35))
    p = t.text_frame.paragraphs[0]
    run = p.add_run()
    run.text = "BOOKED"
    _set_run(run, 13, TEAL, bold=True)
    bullets(
        s,
        [
            "Priya Menon / Arjun Menon · Byrathi",
            "Stage Visit Scheduled · Status Booked",
            "18 Sep 2026  10:00–10:30 IST",
            "Event on the lead",
            "Tasks: day-before, and 30-min with reschedule",
            "Search: Menon",
        ],
        Inches(0.85),
        Inches(2.2),
        Inches(5.5),
        Inches(3.8),
        16,
    )
    t = tb(s, Inches(7.1), Inches(1.7), Inches(5.5), Inches(0.35))
    p = t.text_frame.paragraphs[0]
    run = p.add_run()
    run.text = "MISSED"
    _set_run(run, 13, RED, bold=True)
    bullets(
        s,
        [
            "Rohit Das / Ishaan Das · NICE Road",
            "Stage Visit Missed · Status Missed",
            "Visit date 10 Sep 2026",
            "Missed-visit event + nurture task",
            "Setting Visit Status to Missed fires the workflow",
            "Search: Das",
        ],
        Inches(7.1),
        Inches(2.2),
        Inches(5.5),
        Inches(3.8),
        16,
    )
    footer(s, "Scene 4", "CRM · Menon then Das")
    set_notes(
        s,
        "SAY BOOKED: Parent gets a link, sees about two weeks of availability, picks a 30-minute slot. "
        "Confirmation to admissions and the parent. Day before, workflow marks Reminder Sent. "
        "Thirty minutes before, reminder with reschedule. Bookings can sit on top later.\n\n"
        "SAY MISSED: If they miss without rescheduling, stage moves to Visit Missed and nurture starts. "
        "You do not rely on someone dragging a Kanban card.",
    )


def add_scene5(prs):
    s = blank(prs)
    rail(s)
    kicker(s, "Scene 5  ·  12:00–16:00")
    title_block(s, "Submit. HOS comments. Waitlist or accept.")
    rows = [
        ("Farah Khan / Zara Khan", "App Submitted", "CMRNPS HRBR  ·  form submitted, visit attended", "Khan"),
        ("Lakshmi Rao / Aditi Rao", "HOS Review", "Founder Decision Pending  ·  HOS comments on the record", "Rao"),
        ("Neha Patel / Kabir Patel", "Waitlist", "Founder Decision Waitlist  ·  Grade 1 capacity at JP Nagar", "Patel"),
        ("Sanjay Mehta / Aanya Mehta", "Accepted", "Founder Decision Accept  ·  workflow moved the stage", "Mehta"),
    ]
    y = Inches(1.5)
    for i, (who, stage, note, search) in enumerate(rows):
        box(s, Inches(0.55), y, Inches(12.2), Inches(1.15), LIGHT if i % 2 == 0 else WHITE)
        t = tb(s, Inches(0.75), y + Inches(0.18), Inches(0.5), Inches(0.7))
        p = t.text_frame.paragraphs[0]
        run = p.add_run()
        run.text = str(i + 1)
        _set_run(run, 22, RED, bold=True)
        t = tb(s, Inches(1.3), y + Inches(0.14), Inches(5.3), Inches(0.4))
        p = t.text_frame.paragraphs[0]
        run = p.add_run()
        run.text = who
        _set_run(run, 18, NAVY, bold=True)
        t = tb(s, Inches(1.3), y + Inches(0.58), Inches(7.5), Inches(0.4))
        p = t.text_frame.paragraphs[0]
        run = p.add_run()
        run.text = note
        _set_run(run, 14, SLATE)
        t = tb(s, Inches(8.9), y + Inches(0.22), Inches(2.4), Inches(0.7))
        p = t.text_frame.paragraphs[0]
        p.alignment = PP_ALIGN.RIGHT
        run = p.add_run()
        run.text = stage
        _set_run(run, 16, TEAL if stage == "Accepted" else NAVY, bold=True)
        t = tb(s, Inches(11.3), y + Inches(0.35), Inches(1.2), Inches(0.4))
        p = t.text_frame.paragraphs[0]
        run = p.add_run()
        run.text = search
        _set_run(run, 13, MUTED)
        y += Inches(1.2)
    footer(s, "Scene 5", "CRM · Khan → Rao → Patel → Mehta")
    set_notes(
        s,
        "Tell this as one file moving forward. Do not linger.\n\n"
        "KHAN: Application is in. Visit happened. Optional: open deal K-12 Application - Zara Khan.\n"
        "RAO: Head of School writes on the same record. Founder sees the comment. No side email thread.\n"
        "PATEL: Accept and Waitlist are first-class outcomes. Capacity is a founder decision, not a lost lead.\n"
        "MEHTA: When the founder sets Accept, a workflow moves Ekya Lead Stage to Accepted.\n\n"
        "DO NOT change Founder Decision on Rao or Patel during the demo.",
    )


def add_scene6(prs):
    s = blank(prs)
    rail(s)
    kicker(s, "Scene 6  ·  16:00–17:30")
    title_block(s, "PU is not the Grade 1 pipeline.")
    box(s, Inches(0.55), Inches(1.55), Inches(6.05), Inches(4.4), LIGHT)
    box(s, Inches(6.8), Inches(1.55), Inches(5.95), Inches(4.4), LIGHT)
    t = tb(s, Inches(0.85), Inches(1.75), Inches(5.5), Inches(0.35))
    p = t.text_frame.paragraphs[0]
    run = p.add_run()
    run.text = "K-12 DEAL"
    _set_run(run, 13, RED, bold=True)
    bullets(
        s,
        [
            "Zara Khan · CMRNPS HRBR",
            "App Type K-12 · Grade 6",
            "Deal: K-12 Application - Zara Khan",
            "Standard Deal Stage stays Qualification",
            "Admissions status lives on Ekya stages",
        ],
        Inches(0.85),
        Inches(2.25),
        Inches(5.5),
        Inches(3.4),
        17,
    )
    t = tb(s, Inches(7.1), Inches(1.75), Inches(5.5), Inches(0.35))
    p = t.text_frame.paragraphs[0]
    run = p.add_run()
    run.text = "PU DEAL"
    _set_run(run, 13, TEAL, bold=True)
    bullets(
        s,
        [
            "Ramesh Gowda / Kiran Gowda",
            "Brand CMRNPUC · NPUC HRBR",
            "App Type PU · PUC 1 · App Initiated",
            "Deal: PU Application - Kiran Gowda",
            "Search: Gowda",
        ],
        Inches(7.1),
        Inches(2.25),
        Inches(5.5),
        Inches(3.4),
        17,
    )
    footer(s, "Scene 6", "CRM · Gowda + Deals")
    set_notes(
        s,
        "SAY: Same CRM, different journey. PU and K-12 dashboards can be two views on App Type. "
        "You do not run PUC 1 through the Grade 1 school pipeline.",
    )


def add_scene7(prs):
    s = blank(prs)
    rail(s)
    kicker(s, "Scene 7  ·  17:30–19:00")
    title_block(s, "Six Ekya workflows. The spine of what you just saw.")
    rows = [
        ("Ekya Set Stage Enquiry", "New branded lead starts at Enquiry"),
        ("Ekya Form Started Stage", "Nair / Diya Sharma → App Initiated"),
        ("Ekya Form Submitted Stage", "Khan / Mehta → App Submitted"),
        ("Ekya Visit Day Before", "Menon reminder the day before 18 Sep"),
        ("Ekya Visit Missed Stage", "Das when Visit Status = Missed"),
        ("Ekya Founder Accept Stage", "Mehta when Founder Decision = Accept"),
    ]
    y = Inches(1.48)
    for i, (name, meaning) in enumerate(rows):
        box(s, Inches(0.55), y, Inches(12.2), Inches(0.78), LIGHT if i % 2 == 0 else WHITE)
        t = tb(s, Inches(0.75), y + Inches(0.2), Inches(0.5), Inches(0.4))
        p = t.text_frame.paragraphs[0]
        run = p.add_run()
        run.text = f"{i + 1:02d}"
        _set_run(run, 16, RED, bold=True)
        t = tb(s, Inches(1.4), y + Inches(0.2), Inches(5.5), Inches(0.4))
        p = t.text_frame.paragraphs[0]
        run = p.add_run()
        run.text = name
        _set_run(run, 16, NAVY, bold=True)
        t = tb(s, Inches(7.1), y + Inches(0.2), Inches(5.4), Inches(0.4))
        p = t.text_frame.paragraphs[0]
        run = p.add_run()
        run.text = meaning
        _set_run(run, 15, SLATE)
        y += Inches(0.8)
    footer(s, "Scene 7", "CRM · Setup → Workflow Rules → Ekya")
    set_notes(
        s,
        "SAY: These six rules are the spine. Email, WhatsApp, Bookings, and telephony plug into the same fields. "
        "We did not overwrite the existing EdNova process in this org.\n\n"
        "DO NOT open or edit EdNova follow -up update.",
    )


def add_scene8(prs):
    s = blank(prs)
    rail(s)
    kicker(s, "Scene 8  ·  19:00–20:00")
    title_block(s, "In this org today. Go-live next.")
    box(s, Inches(0.55), Inches(1.5), Inches(6.05), Inches(4.85), LIGHT)
    box(s, Inches(6.8), Inches(1.5), Inches(5.95), Inches(4.85), LIGHT)
    t = tb(s, Inches(0.85), Inches(1.7), Inches(5.5), Inches(0.4))
    p = t.text_frame.paragraphs[0]
    run = p.add_run()
    run.text = "YOU JUST CLICKED"
    _set_run(run, 13, TEAL, bold=True)
    bullets(
        s,
        [
            "Brand, campus, grade, channel on every lead",
            "Same phone, two campus journeys",
            "Sibling and intercampus flags",
            "Visit booked and missed nurture",
            "HOS comments and founder accept / waitlist",
            "K-12 and PU as parallel pipelines",
        ],
        Inches(0.85),
        Inches(2.2),
        Inches(5.5),
        Inches(3.8),
        16,
    )
    t = tb(s, Inches(7.1), Inches(1.7), Inches(5.5), Inches(0.4))
    p = t.text_frame.paragraphs[0]
    run = p.add_run()
    run.text = "TO GO LIVE"
    _set_run(run, 13, RED, bold=True)
    bullets(
        s,
        [
            "Forms with OTP",
            "Parent portal for documents and edit",
            "Bookings or Google Calendar",
            "Campaigns and WhatsApp by grade",
            "Marketplace telephony on four hotlines",
            "Payment with campus-specific bank details",
            "Books: one org under Zoho One; other legal entities standalone",
        ],
        Inches(7.1),
        Inches(2.2),
        Inches(5.5),
        Inches(3.8),
        15,
    )
    footer(s, "Scene 8")
    set_notes(
        s,
        "SAY: You asked for one place that knows the brand, the campus, the grade, the channel, the visit, "
        "and the founder decision. That is what you just clicked through.\n\n"
        "To go live: Forms with OTP, parent portal, Bookings or Google Calendar, Campaigns and WhatsApp by grade, "
        "marketplace telephony, payment with campus-specific bank details. One Books org can sit under Zoho One; "
        "other legal entities need their own Books. We did not invent entity names because those packs were empty.\n\n"
        "Questions I can answer from this org: two applications on one phone, sibling vs intercampus, "
        "K-12 vs PU, missed-visit nurture, HOS to founder.\n\nSTOP. Take questions.",
    )


def add_questions(prs):
    s = blank(prs)
    box(s, Inches(0), Inches(0), W, H, NAVY)
    box(s, Inches(0), Inches(0), Inches(0.18), H, RED)
    t = tb(s, Inches(0.7), Inches(2.6), Inches(12), Inches(1.2))
    tf = t.text_frame
    p = tf.paragraphs[0]
    run = p.add_run()
    run.text = "Questions from this org"
    _set_run(run, 36, WHITE, bold=True)
    t = tb(s, Inches(0.7), Inches(4.0), Inches(12), Inches(1.4))
    tf = t.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    run = p.add_run()
    run.text = "Two applications on one phone  ·  Sibling vs intercampus\nK-12 vs PU  ·  Missed-visit nurture  ·  HOS to founder"
    _set_run(run, 20, RGBColor(0xD5, 0xDE, 0xEA))
    set_notes(s, "Leave this up. Do not improvise edits on showcase leads.")


def add_cheatsheet(prs):
    s = blank(prs)
    rail(s)
    kicker(s, "Presenter appendix")
    title_block(s, "Search cheat sheet")
    rows = [
        ("Two campuses, same phone", "9876543210"),
        ("Sibling", "Reddy"),
        ("Intercampus", "Iyer"),
        ("Abandoned form", "Nair"),
        ("Visit booked", "Menon"),
        ("Visit missed", "Das"),
        ("App submitted", "Khan"),
        ("HOS → founder", "Rao"),
        ("Waitlist", "Patel"),
        ("Accepted", "Mehta"),
        ("PU vs K-12", "Gowda"),
        ("Database upload", "Banerjee"),
        ("Inbound hotline", "Joseph"),
    ]
    left, right = rows[:7], rows[7:]
    for col, data in ((Inches(0.55), left), (Inches(6.85), right)):
        for i, (want, term) in enumerate(data):
            y = Inches(1.5) + Inches(i * 0.7)
            box(s, col, y, Inches(5.9), Inches(0.62), LIGHT if i % 2 == 0 else WHITE)
            t = tb(s, col + Inches(0.2), y + Inches(0.14), Inches(3.6), Inches(0.35))
            p = t.text_frame.paragraphs[0]
            run = p.add_run()
            run.text = want
            _set_run(run, 15, SLATE)
            t = tb(s, col + Inches(3.7), y + Inches(0.14), Inches(2.0), Inches(0.35))
            p = t.text_frame.paragraphs[0]
            p.alignment = PP_ALIGN.RIGHT
            run = p.add_run()
            run.text = term
            _set_run(run, 16, NAVY, bold=True)
    footer(s, "Appendix", "Leads search")
    set_notes(s, "Keep this slide in presenter view or printed. Not for the customer unless they ask.")


def add_short_cut(prs):
    s = blank(prs)
    rail(s)
    kicker(s, "Presenter appendix")
    title_block(s, "12-minute cut — skip Scene 2 and Scene 6")
    rows = [
        ("00:00", "Accounts tree", "Scene 0"),
        ("01:00", "9876543210 two campuses", "Scene 1"),
        ("03:00", "Nair abandoned form + 24h task", "Scene 3c only"),
        ("05:00", "Menon booked, Das missed", "Scene 4"),
        ("08:00", "Khan → Rao → Patel → Mehta", "Scene 5"),
        ("11:00", "Workflow list + close", "Scenes 7–8"),
    ]
    y = Inches(1.5)
    for i, (time, what, scene) in enumerate(rows):
        box(s, Inches(0.55), y, Inches(12.2), Inches(0.78), LIGHT if i % 2 == 0 else WHITE)
        t = tb(s, Inches(0.8), y + Inches(0.2), Inches(1.6), Inches(0.4))
        p = t.text_frame.paragraphs[0]
        run = p.add_run()
        run.text = time
        _set_run(run, 16, RED, bold=True)
        t = tb(s, Inches(2.6), y + Inches(0.2), Inches(6.5), Inches(0.4))
        p = t.text_frame.paragraphs[0]
        run = p.add_run()
        run.text = what
        _set_run(run, 18, NAVY, bold=True)
        t = tb(s, Inches(9.4), y + Inches(0.2), Inches(3.0), Inches(0.4))
        p = t.text_frame.paragraphs[0]
        run = p.add_run()
        run.text = scene
        _set_run(run, 15, SLATE)
        y += Inches(0.82)
    footer(s, "Appendix")
    set_notes(s, "If time is short: drop sibling/intercampus and PU. In Scene 3 show only Nair.")


def main():
    prs = new_prs()
    add_title_slide(prs)
    add_agenda(prs)
    add_ground_rules(prs)
    add_scene0(prs)
    add_campus_map(prs)
    add_journey(prs)
    add_scene1(prs)
    add_scene2(prs)
    add_scene3(prs)
    add_scene4(prs)
    add_scene5(prs)
    add_scene6(prs)
    add_scene7(prs)
    add_scene8(prs)
    add_questions(prs)
    add_cheatsheet(prs)
    add_short_cut(prs)
    prs.save(OUT)
    print(f"Wrote {OUT} ({len(prs.slides)} slides)")


if __name__ == "__main__":
    main()
