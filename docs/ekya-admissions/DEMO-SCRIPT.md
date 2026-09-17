# Ekya / CMR admissions — demo run-through script

**Audience:** admissions, marketing, campus heads  
**Org:** Cooper and Co · `org60040760589` · Asia/Kolkata · INR  
**Login:** ACP Pradhyuman (`julia.edwards+crm4e@zohotest.com`)  
**Length:** 20 minutes (12-minute cut at the end)  
**Story:** one CRM for four brands, from first enquiry to founder accept

Use **Ekya Lead Stage**. Ignore **Admission Stage** (that is the older EdNova picklist).

Related docs: [use case](USE-CASE.md) · [demo script](DEMO-SCRIPT.md) · [walkthrough](WALKTHROUGH.md) · [Zoho Show deck](show/README.md)

**Presenting:** open [Ekya-CMR-Admissions-Demo.pptx](show/Ekya-CMR-Admissions-Demo.pptx) in Zoho Show. Advance the matching slide, then click CRM. Speaker notes are the talk track.

---

## 15 minutes before

1. Import [Ekya-CMR-Admissions-Demo.pptx](show/Ekya-CMR-Admissions-Demo.pptx) into Zoho Show. Open Presenter view. See [show/README.md](show/README.md).
2. Sign in as ACP Pradhyuman. CRM in a second window; hide Setup until Scene 7.
3. Open four CRM tabs and leave them:
   - **Leads** (All Leads)
   - **Accounts** → `Ekya | CMR Group`
   - **Deals**
   - **Setup → Automation → Workflow Rules** (filter name contains `Ekya`)
4. On Leads, pin a filter or remember: **Brand Ekya is not empty**.
5. Do **not** create or edit the showcase leads below. If a stage looks wrong, stop and reset from the walkthrough before the call.
6. Parking lot for later: parent portal, live WhatsApp, VOIP/IVR, payment gateway, Zoho Bookings, Campaigns, Forms OTP. Those are designed, not live in this org.

### Search cheat sheet

| You want | Search in Leads |
| --- | --- |
| Two campuses, same phone | `9876543210` |
| Sibling | `Reddy` |
| Intercampus | `Iyer` |
| Abandoned form | `Nair` |
| Visit booked | `Menon` |
| Visit missed | `Das` |
| App submitted | `Khan` |
| HOS → founder | `Rao` |
| Waitlist | `Patel` |
| Accepted | `Mehta` |
| PU vs K-12 | `Gowda` |
| Database upload | `Banerjee` |
| Inbound hotline | `Joseph` |

---

## Run of show

Show slides 1–3 (title, order, ground rules) before CRM. Then one cue slide, then the live record. SOP screenshot slides sit immediately after the matching scene.

| Min | Scene | Show slide | Record to leave on screen |
| --- | ---: | ---: | --- |
| 0:00 | Open | 4–7 | Accounts tree |
| 1:30 | Same phone, two campuses | 8 | Anita Sharma pair |
| 4:00 | Sibling and intercampus | 9 | Reddy, then Iyer |
| 6:00 | Three intake channels | 10–11 | Joseph → Banerjee → Nair |
| 9:00 | Campus visit booked and missed | 12–13 | Menon, then Das |
| 12:00 | Submit → HOS → waitlist or accept | 14 | Khan → Rao → Patel → Mehta |
| 16:00 | PU is a different journey | 15 | Gowda + Deals |
| 17:30 | Workflows | 16 | Setup list |
| 19:00 | Close and next steps | 17–19 | Questions slide |

---

## Scene 0 — Four brands, one CRM (1.5 min)

**Click:** Accounts → **Ekya \| CMR Group** (`902823000002022001`). Expand related / parent-child accounts.

**Point at:** brand accounts (Ekya Schools, Ekya Nava, CMRNPS, CMRNPUC, Ekya Vana Early Years) and campus accounts under them (JP Nagar, BTM, ITPL, Byrathi, NICE Road, HRBR, Panathur, PU campuses, Vana X/Y/Z).

**Say:**

> This is one CRM for the group. Ekya Schools, Nava, CMR NPS, and CMR PU College are brands. Campuses sit under the brand. Early Years and future campuses can be added here without a new module.
>
> K-12 and PU are not the same admissions process. Every enquiry carries Brand, Campus, Grade, and App Type so the journey, the owner, and the dashboard can split.

**Do not:** open finance / Books. Campus accounts are locations, not legal entities.

---

## Scene 1 — Same mobile, two campuses (2.5 min)

**Click:** Leads → search `9876543210`. You should see two leads.

**Open first:** **Anita Sharma** / student **Aarav Sharma** · Ekya JP Nagar · Enquiry · `902823000002043006`

**Point at:** Brand Ekya, Campus Ekya, Grade Applied (Grade 1), Student Name, How Heard (Website), OTP Verified, Ekya Lead Stage = Enquiry. Phone and Mobile both `9876543210`.

**Open second (same search):** **Anita Sharma** / student **Diya Sharma** · Ekya BTM Layout · App Initiated · Form Status Started · `902823000002043007`

**Say:**

> Anita used one mobile number for two campuses. We did not treat that as a duplicate. JP Nagar is still an enquiry for Aarav. BTM has already started Diya’s application. Each campus nurtures its own record.
>
> If you unique-lock mobile, this family breaks.

**If asked “can they apply twice from the same number?”:** Yes. That was an explicit requirement.

---

## Scene 2 — Sibling and intercampus (2 min)

**Click:** search `Reddy`. Open **Kavya Reddy** / **Vihaan Reddy** · CMRNPS HRBR · `902823000002043008`

**Point at:** Sibling Enquiry = true, Brand CMRNPS, Grade LKG, stage Enquiry.

**Click:** search `Iyer`. Open **Meera Iyer** / **Ananya Iyer** · Nava Panathur · `902823000002043009`

**Point at:** Intercampus Enq = true, Previous School = Ekya Schools JP Nagar, Brand Ekya Nava.

**Say:**

> Sibling and intercampus are flags on the lead, not a second product. Counsellors see why a second file exists instead of merging the family by accident.
>
> Meera is moving a child from JP Nagar to Nava Panathur. The previous school is on the record so the new campus has context.

---

## Scene 3 — Phone, database, abandoned form (3 min)

Stay in Leads. Keep this tight: one sentence per record, then land on Nair.

### 3a Inbound phone

**Open:** **Maria Joseph** / **Leo Joseph** · `902823000002030009`

**Point at:** How Heard = Inbound Phone, Hotline Number = `080-46809096`, Call Count = 1, Campus = Ekya BTM Layout, stage Enquiry.

**Say:**

> Four published hotlines. After a VOIP provider is on the marketplace, IVR maps campus and the owner on this lead is who takes the call. Inbound and outbound activity belongs on this record, not in a shared inbox.

### 3b Prior-year database

**Open:** **Amit Banerjee** / **Riya Banerjee** · `902823000002030008`

**Point at:** How Heard = Database Upload, stage Enquiry, Form Status empty.

**Say:**

> Last year’s list can live in CRM for nurture. It should not fire this year’s incoming-lead workflow until the parent acts. When they do, this record becomes a live enquiry.

### 3c Application started, not finished

**Open:** **Suresh Nair** / **Nila Nair** · `902823000002043010`

**Point at:** Ekya Lead Stage = App Initiated, Form Status = Abandoned, How Heard = Meta Ads, Grade = UKG.

**Click:** Open Activities / Open Tasks → **24h incomplete application reminder - Nila Nair**

**Say:**

> She started the form from a paid campaign and did not submit. The counsellor gets a 24-hour task. In production, that is the email and WhatsApp chase by grade.
>
> One honest limit: Zoho Forms does not natively push “abandoned” as a CRM stage. We store Form Status here and chase from CRM once we know the form was started.

**Do not:** promise a native Forms-to-stage abandon webhook.

---

## Scene 4 — Campus visit booked and missed (3 min)

### 4a Booked

**Open:** **Priya Menon** / **Arjun Menon** · `902823000002043011`

**Point at:** Stage = Visit Scheduled, Visit Status = Booked, Visit Date = 18 Sep 2026 10:00 IST, Campus = Ekya Byrathi, Form Status = Started.

**Click:** Open Activities → event **Campus visit - Arjun Menon - Ekya Byrathi** (10:00–10:30). Then the tasks **Day-before campus visit reminder** and **30-min visit reminder with reschedule**.

**Say:**

> Parent gets a link, sees about two weeks of availability, picks a 30-minute slot in working hours. Confirmation goes to admissions and the parent. CRM holds the slot on the lead.
>
> Day before, a workflow marks Reminder Sent. Thirty minutes before, they get a reminder with reschedule. Bookings or Google Calendar can sit on top of this later; the data model is already here.

### 4b Missed

**Open:** **Rohit Das** / **Ishaan Das** · `902823000002043012`

**Point at:** Stage = Visit Missed, Visit Status = Missed, Visit Date = 10 Sep 2026.

**Click:** Open the missed-visit event and the task **Missed campus tour nurture**.

**Say:**

> If they miss without rescheduling, the stage moves to Visit Missed and nurture starts. Setting Visit Status to Missed is what fires that workflow. You do not rely on someone remembering to drag a Kanban card.

---

## Scene 5 — Submitted → HOS → waitlist or accept (4 min)

Tell this as one file moving forward. Do not linger.

### 5a Submitted

**Open:** **Farah Khan** / **Zara Khan** · CMRNPS HRBR · `902823000002043013`

**Point at:** Stage = App Submitted, Form Status = Submitted, Visit Status = Attended.

**Say:**

> Application is in. Visit happened. This is the point the file becomes an admissions case, not just an enquiry.

**Optional click:** Deals → **K-12 Application - Zara Khan - CMRNPS HRBR** (`902823000002021147`). Point at Brand, Campus, App Type, Student Name. Leave standard Deal Stage as Qualification; admissions status is **Ekya App Stage** / the lead stage.

### 5b HOS comments for the founder

**Open:** **Lakshmi Rao** / **Aditi Rao** · Nava Panathur · `902823000002043014`

**Point at:** Stage = HOS Review, Founder Decision = Pending, HOS Comments (recommend founder review).

**Say:**

> Head of School writes on the same record. Founder sees the comment, the campus, the grade, and later the documents. No side email thread.

### 5c Waitlist

**Open:** **Neha Patel** / **Kabir Patel** · JP Nagar · `902823000002043015`

**Point at:** Stage = Waitlist, Founder Decision = Waitlist, HOS comment about Grade 1 capacity.

**Say:**

> Accept and Waitlist are first-class outcomes. Capacity at a campus is a founder decision, not a lost lead.

### 5d Accepted

**Open:** **Sanjay Mehta** / **Aanya Mehta** · Ekya ITPL · `902823000002030010`

**Point at:** Stage = Accepted, Founder Decision = Accept, Form Submitted, Visit Attended, OTP Verified, HOS Comments.

**Say:**

> When the founder sets Accept, a workflow moves Ekya Lead Stage to Accepted. That is the happy path you will report as admitted.

**Do not:** change Founder Decision on Rao or Patel during the demo. Mehta is already the accept example.

---

## Scene 6 — PU is not K-12 (1.5 min)

**Open:** **Ramesh Gowda** / **Kiran Gowda** · `902823000002030007`

**Point at:** Brand = CMRNPUC, Campus = NPUC HRBR, App Type = **PU**, Grade = **PUC 1**, stage App Initiated.

**Click:** Deals → **PU Application - Kiran Gowda - NPUC HRBR** (`902823000002021148`) next to the K-12 deal for Zara Khan.

**Say:**

> Same CRM, different journey. PU and K-12 dashboards can be two views on App Type. You do not run PUC 1 through the Grade 1 school pipeline.

---

## Scene 7 — What is already automated (1.5 min)

**Click:** the Workflow Rules tab. Show only names starting with **Ekya**.

| Rule | What you just saw |
| --- | --- |
| Ekya Set Stage Enquiry | New branded lead starts at Enquiry |
| Ekya Form Started Stage | Nair / Diya Sharma → App Initiated |
| Ekya Form Submitted Stage | Khan / Mehta → App Submitted |
| Ekya Visit Day Before | Menon reminder the day before 18 Sep |
| Ekya Visit Missed Stage | Das when Visit Status = Missed |
| Ekya Founder Accept Stage | Mehta when Founder Decision = Accept |

**Say:**

> These six rules are the spine. Email, WhatsApp, Bookings, and telephony plug into the same fields. We did not overwrite the existing EdNova process in this org.

**Do not:** open or edit **EdNova follow -up update**.

---

## Scene 8 — Close (1 min)

Leave Mehta or the Accounts tree on screen.

**Say:**

> You asked for one place that knows the brand, the campus, the grade, the channel, the visit, and the founder decision. That is what you just clicked through.
>
> To go live: Forms with OTP, parent portal for documents and edit, Bookings or Google Calendar, Campaigns and WhatsApp by grade, marketplace telephony on the four hotlines, and payment with campus-specific bank details. One Books org can sit under Zoho One; other legal entities need their own Books. We did not invent entity names because those packs were empty.
>
> Questions I can answer from this org: two applications on one phone, sibling vs intercampus, K-12 vs PU, missed-visit nurture, HOS to founder.

**Stop.** Take questions. Use the parking lot for portal, WhatsApp, IVR, and fees.

---

## 12-minute cut

Drop Scenes 2 and 6 (Show slides 9 and 15). In Scene 3 show only **Nair**. Keep 0, 1, 4, 5, 7, 8.

| Min | Scene | Show slide |
| --- | --- | ---: |
| 0:00 | Accounts tree | 4–7 |
| 1:00 | `9876543210` two campuses | 8 |
| 3:00 | Nair abandoned form + 24h task | 10–11 |
| 5:00 | Menon booked visit, Das missed | 12–13 |
| 8:00 | Khan → Rao → Patel → Mehta | 14 |
| 11:00 | Workflow list + close | 16–19 |

---

## If something looks wrong

| Symptom | Likely cause | Fix after the call |
| --- | --- | --- |
| New lead with Brand Ekya is not Enquiry | Workflow inactive | Re-enable **Ekya Set Stage Enquiry** |
| Visit or HOS record jumped to App Initiated | Form Status set to Started | Set **Ekya Lead Stage** back; do not leave Form Status = Started on enquiry-only demos |
| Search `9876543210` returns one lead | Filter too narrow | Clear filters; search Phone or Mobile |
| You see Admission Stage, not Ekya Lead Stage | Wrong field on the layout | Add **Ekya Lead Stage** to the list view |

Do not improvise a live edit on Sharma, Menon, Das, Rao, Patel, or Mehta while the customer is watching.

---

## After the demo

- Zoho Show deck: [show/README.md](show/README.md)
- Use case write-up: [USE-CASE.md](USE-CASE.md)
- Record IDs and SOP screenshots: [WALKTHROUGH.md](WALKTHROUGH.md)
- CRM Case Study: **Ekya CMR Admissions Evaluation** (`902823000002022024`)
