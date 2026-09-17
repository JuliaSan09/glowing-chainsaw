# Zoho Show deck — import and present

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

| Slide | When | Show title | CRM |
| ---: | --- | --- | --- |
| 1 | 0:00 | Title | — |
| 2 | | Presenting order | — |
| 3 | | Before we click | — |
| 4 | 0:00 | Scene 0 — Four brands, one CRM | Accounts → Ekya \| CMR Group |
| 5 | | Brands and campuses | Stay on Accounts |
| 6 | | Ekya Lead Stage path | — |
| 7 | 1:30 | Scene 1 — Same phone, two campuses | Leads → `9876543210` |
| 8 | 4:00 | Scene 2 — Sibling and intercampus | `Reddy` then `Iyer` |
| 9 | 6:00 | Scene 3 — Three intake channels | Joseph → Banerjee → Nair |
| 10 | 9:00 | Scene 4 — Visit booked and missed | `Menon` then `Das` |
| 11 | 12:00 | Scene 5 — Submit → HOS → waitlist or accept | Khan → Rao → Patel → Mehta |
| 12 | 16:00 | Scene 6 — PU is not K-12 | `Gowda` + Deals |
| 13 | 17:30 | Scene 7 — Six workflows | Setup → Workflow Rules → Ekya |
| 14 | 19:00 | Scene 8 — In this org / go-live | — |
| 15 | | Questions | Leave up |
| 16 | appendix | Search cheat sheet | Presenter only |
| 17 | appendix | 12-minute cut | Presenter only |

12-minute cut: skip slides 8 and 12. On slide 9, open Nair only.

Talk tracks, what not to edit, and recovery: [../DEMO-SCRIPT.md](../DEMO-SCRIPT.md)
