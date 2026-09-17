# Zoho Show deck — import and present

## Generate with Zia AI (this screen)

Paste [zia-generate-prompt.txt](zia-generate-prompt.txt) into **Describe your presentation idea** (2,446 / 2,500 characters).

| Setting | Use |
| --- | --- |
| Slide Limit | Largest option available (not Small — Small will collapse the 16-slide order) |
| Content Tone | Professional |
| Visual Style | Content with Placeholders |
| Theme | Basic or Executive |

Then **Generate Presentation**. After it builds, keep the slide order. Drop screenshots onto placeholders using [SCREENSHOTS.md](SCREENSHOTS.md) — SOP images are ready; CRM stills must be captured live.

File: [Ekya-CMR-Admissions-Demo.pptx](Ekya-CMR-Admissions-Demo.pptx)

17 widescreen slides in the **same order as the live CRM demo**. Speaker notes on every slide are the talk track. Regenerating: `python3 docs/ekya-admissions/show/build_presentation.py`

There is no Show API on this evaluation org. Import the PPTX into Zoho Show (native `.zslides`).

## Import into Zoho Show

1. Open [show.zoho.com](https://show.zoho.com) or [show.zoho.in](https://show.zoho.in) with the same Zoho account you use for CRM.
2. **Blank presentation** is not required. Use **Import** (or **Open** → **Import file**).
3. Choose `Ekya-CMR-Admissions-Demo.pptx`.
4. Save the converted file as **Ekya CMR Admissions Demo**.
5. Turn on **Presenter view** so speaker notes stay on your screen. The customer sees the slide only.

From WorkDrive: upload the PPTX, then **Open with Zoho Show**. WorkDrive can also **Convert to Zoho format**.

## How to present (Show + CRM)

Use two windows. Show is the cue. CRM is the proof.

| Window | Role |
| --- | --- |
| Zoho Show | Advance one slide, read the CRM cue in the footer, glance at notes |
| Zoho CRM | Search and open the record named on the slide |

Do not stay on a slide while they could be looking at the live lead. Advance Show, then switch.

## Slide order (matches the 20-minute script)

| Slide | When | Show title | CRM / image |
| ---: | --- | --- | --- |
| 1 | 0:00 | Title | — |
| 2 | | Presenting order | — |
| 3 | | Before we click | — |
| 4 | 0:00 | Scene 0 — Four brands, one CRM | Accounts → Ekya \| CMR Group |
| 5 | | Brands and campuses | Stay on Accounts |
| 6 | | SOP screenshot — brands and stages | `05-sop-brands-campuses.png` |
| 7 | | Ekya Lead Stage path | — |
| 8 | 1:30 | Scene 1 — Same phone, two campuses | Leads → `9876543210` |
| 9 | 4:00 | Scene 2 — Sibling and intercampus | `Reddy` then `Iyer` |
| 10 | 6:00 | Scene 3 — Three intake channels | Joseph → Banerjee → Nair |
| 11 | | SOP screenshot — forms and inbound phone | `11-sop-forms-inbound.png` |
| 12 | 9:00 | Scene 4 — Visit booked and missed | `Menon` then `Das` |
| 13 | | SOP screenshot — campus visit flow | `13-sop-campus-visit.png` |
| 14 | 12:00 | Scene 5 — Submit → HOS → waitlist or accept | Khan → Rao → Patel → Mehta |
| 15 | 16:00 | Scene 6 — PU is not K-12 | `Gowda` + Deals |
| 16 | 17:30 | Scene 7 — Six workflows | Setup → Workflow Rules → Ekya |
| 17 | 19:00 | Scene 8 — In this org / go-live | — |
| 18 | | SOP screenshot — portal and telephony | `18-sop-portal-telephony.png` |
| 19 | | Questions | Leave up |
| 20 | appendix | Search cheat sheet | Presenter only |
| 21 | appendix | 12-minute cut | Presenter only |
| 22 | appendix | SOP screenshot — reports | Presenter only |

Screenshots: [SCREENSHOTS.md](SCREENSHOTS.md). 12-minute cut: skip slides 9 and 15. On slide 10, open Nair only.

Talk tracks, what not to edit, and recovery: [../DEMO-SCRIPT.md](../DEMO-SCRIPT.md)
