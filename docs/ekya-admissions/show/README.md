# Copy into Zoho Show Zia (this is the easy path)

Open **[COPY-INTO-ZIA.md](COPY-INTO-ZIA.md)** — or open **[copy-into-zia.html](copy-into-zia.html)** in a browser for a Copy button plus the pictures.

Zia’s **Describe your presentation idea** box is text only (2,500 characters). It cannot hold JPEGs. The prompt names every image file. After Generate, drop the JPEGs onto the `[IMG]` slides.

## 1. Settings

| Setting | Choose |
| --- | --- |
| Slide Limit | Largest (not Small) |
| Content Tone | Professional |
| Visual Style | Content with Placeholders |
| Theme | Basic or Executive |

## 2. Paste this (2,497 / 2,500)

Select all in [zia-generate-prompt.txt](zia-generate-prompt.txt) and paste into the box. Then **Generate Presentation**.

Do not paste Python. Do not paste this README.

## 3. Insert images

Download [Ekya-CMR-Admissions-Screenshots.zip](Ekya-CMR-Admissions-Screenshots.zip). Map and pictures: [COPY-INTO-ZIA.md](COPY-INTO-ZIA.md) · [SCREENSHOTS.md](SCREENSHOTS.md).

Do not insert from the GitHub file preview.

## Already-built PPTX (optional)

If you would rather skip Zia, import [Ekya-CMR-Admissions-Demo.pptx](Ekya-CMR-Admissions-Demo.pptx). SOP stills are already embedded. Rebuild with `python3 build_presentation.py` (see below).

There is no Show API on this evaluation org. Native format after import is `.zslides`.

## Import a PPTX into Zoho Show

1. Open [show.zoho.com](https://show.zoho.com) or [show.zoho.in](https://show.zoho.in) with the same Zoho account you use for CRM.
2. Use **Import** (or **Open** → **Import file**).
3. Choose `Ekya-CMR-Admissions-Demo.pptx`.
4. Save as **Ekya CMR Admissions Demo**.
5. Turn on **Presenter view**.

From WorkDrive: upload the PPTX, then **Open with Zoho Show**.

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
| 6 | | SOP screenshot — brands and stages | `05-sop-brands-campuses.jpg` |
| 7 | | Ekya Lead Stage path | — |
| 8 | 1:30 | Scene 1 — Same phone, two campuses | Leads → `9876543210` |
| 9 | | CRM still — two campuses | `07-crm-two-campus.jpg` |
| 10 | 4:00 | Scene 2 — Sibling and intercampus | `Reddy` then `Iyer` |
| 11 | 6:00 | Scene 3 — Three intake channels | Joseph → Banerjee → Nair |
| 12 | | SOP screenshot — forms and inbound phone | `11-sop-forms-inbound.jpg` |
| 13 | 9:00 | Scene 4 — Visit booked and missed | `Menon` then `Das` |
| 14 | | SOP screenshot — campus visit flow | `13-sop-campus-visit.jpg` |
| 15 | 12:00 | Scene 5 — Submit → HOS → waitlist or accept | Khan → Rao → Patel → Mehta |
| 16 | 16:00 | Scene 6 — PU is not K-12 | `Gowda` + Deals |
| 17 | 17:30 | Scene 7 — Six workflows | Setup → Workflow Rules → Ekya |
| 18 | 19:00 | Scene 8 — In this org / go-live | — |
| 19 | | SOP screenshot — portal and telephony | `18-sop-portal-telephony.jpg` |
| 20 | | Questions | Leave up |
| 21 | appendix | Search cheat sheet | Presenter only |
| 22 | appendix | SOP screenshot — reports | `21-sop-reports.jpg` |

Zia’s 22-slide prompt matches the `[IMG]` rows above. The imported PPTX keeps the original 22-slide live-demo order (cue slides, not a still on every scene). 12-minute cut: skip sibling/intercampus and PU; on Scene 3 open Nair only.

Talk tracks, what not to edit, and recovery: [../DEMO-SCRIPT.md](../DEMO-SCRIPT.md)

## Rebuild the PPTX from SOP screenshots

```bash
cd docs/ekya-admissions/show
pip install -r requirements.txt
python3 build_presentation.py
```
