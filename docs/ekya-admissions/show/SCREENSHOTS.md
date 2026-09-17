# Screenshots for the Zoho Show deck

**Copy into Zia:** [COPY-INTO-ZIA.md](COPY-INTO-ZIA.md) — prompt plus every JPEG shown next to the slide it belongs on.

Zia **Generate** cannot attach images. After the deck is built, click a placeholder → **Insert image** and pick a **.jpg** from the zip (not the GitHub file preview).

**Download this:** [Ekya-CMR-Admissions-Screenshots.zip](Ekya-CMR-Admissions-Screenshots.zip)  
Unzip, then insert into Show. GitHub’s file viewer often shows “failing to load” on these binaries even when the files are fine.

SOP stills are RGB JPEGs (Show-safe). CRM frames are labeled placeholders — capture live CRM and replace them. Do not invent a CRM UI.

## After Zia generates — drop these files

Folder: `docs/ekya-admissions/show/images/` (also inside the zip)

| Generated slide (demo order) | Insert this file | Kind |
| --- | --- | --- |
| Scene 0 brands / campuses | `05-sop-brands-campuses.jpg` | SOP (ready) |
| Scene 1 two campuses | `07-crm-two-campus.jpg` | Replace with live CRM capture |
| Scene 2 sibling | `08-crm-sibling.jpg` | Replace with live CRM capture |
| Scene 2 intercampus | `08b-crm-intercampus.jpg` | Replace with live CRM capture |
| Scene 3 forms / phone | `11-sop-forms-inbound.jpg` | SOP (ready) |
| Scene 3 Nair | `11-crm-nair.jpg` | Replace with live CRM capture |
| Scene 4 visit flow | `13-sop-campus-visit.jpg` | SOP (ready) |
| Scene 4 Menon / Das | `13-crm-menon.jpg` then `13b-crm-das.jpg` | Replace with live CRM capture |
| Scene 5 accept | `14-crm-mehta.jpg` | Replace with live CRM capture |
| Scene 7 workflows | `16-crm-workflows.jpg` | Replace with live CRM capture |
| Scene 8 portal / telephony | `18-sop-portal-telephony.jpg` | SOP (ready) |
| Reports (if asked) | `21-sop-reports.jpg` | SOP (ready) |

## CRM captures (10 minutes, before the call)

Stay signed in as ACP Pradhyuman. Use **Ekya Lead Stage**. Save as **JPEG**.

| File to replace | Search | What must be visible |
| --- | --- | --- |
| `07-crm-two-campus.jpg` | `9876543210` | Both Sharma leads on the **list** |
| `08-crm-sibling.jpg` | `Reddy` | Sibling Enquiry = true |
| `08b-crm-intercampus.jpg` | `Iyer` | Intercampus Enq = true |
| `11-crm-nair.jpg` | `Nair` | Form Status Abandoned + 24h task |
| `13-crm-menon.jpg` | `Menon` | Visit Scheduled, 18 Sep 2026 10:00, related event |
| `13b-crm-das.jpg` | `Das` | Visit Missed |
| `14-crm-mehta.jpg` | `Mehta` | Accepted, Founder Decision Accept |
| `16-crm-workflows.jpg` | Setup → Workflow Rules | Names starting with **Ekya** only |

Do not screenshot EdNova **Admission Stage**.

## In the imported PPTX

SOP JPEGs are already embedded. Import `Ekya-CMR-Admissions-Demo.pptx` if Show rejected the earlier PNG-based file.
