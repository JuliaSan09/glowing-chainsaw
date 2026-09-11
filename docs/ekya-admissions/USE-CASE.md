# A Multi-Brand School Group Uses Zoho CRM for Connected Admissions Across Campuses and Channels

## Use Case

A Bengaluru school group runs admissions across four operating brands: Ekya Schools, Ekya Nava, CMR National Public School (CMRNPS), and CMR National PU College (CMRNPUC). Campuses include JP Nagar, BTM Layout, ITPL, Byrathi, NICE Road, HRBR Layout, and Panathur, with Early Years programmes under several of the brands. The group is also planning further campuses, including Ekya Vana Early Years.

Parents reach the group through website forms, paid campaigns (Meta, Google, LinkedIn), social media, walk-ins, education fairs and expos, inbound hotlines, and historical database uploads. The same family may enquire for more than one child, more than one campus, or both a K-12 school and a PU college. K-12 and PU admissions follow different processes and need different pipelines, communications, and reports.

Admissions teams need a single place to capture the enquiry, book a campus visit or virtual interaction, chase incomplete applications, record every call and message, and take the file from Head of School review to founder accept or waitlist. Marketing needs to see which channel produced the enquiry. Campus heads need to see their own pipeline without mixing another brand’s data.

The group wanted Zoho CRM to be that admissions system of record, with Forms, Bookings, Campaigns, SalesIQ, telephony, a parent portal, and accounting connected around it.

## Requirements

- Configure four brands and their campuses in one CRM, including Early Years and future brands, without collapsing K-12 and PU into a single journey.
- Capture enquiries from webforms, landing pages, paid ads, social, walk-ins, expos, inbound phone, and bulk database upload, with source, medium, and campaign on the lead.
- Collect enquiry fields for campus, student name, grade, parent name, email, previous school, and how the parent heard about the school. Offer a thank-you path to book a campus tour or start an application.
- Allow the same mobile number to open two applications or two campus enquiries, and support sibling and intercampus applications as first-class use cases rather than duplicates.
- Run automated, grade-aware email and WhatsApp journeys by stage and sub-stage, including 24-hour reminders when an application is started but not submitted.
- Let parents book a campus visit or virtual slot (two-week window, 30-minute working-hour slots), send confirmations and reminders, and re-nurture missed visits.
- Route inbound calls from four hotlines by IVR to campus owners, round-robin a central team where needed, and record inbound and outbound calls on the lead.
- Give counsellors tasks, follow-up reminders, missed-call reminders, and a full activity history (message sent, email sent, opened or read).
- Provide a parent-facing admission portal for application forms, photo and document upload, sibling and intercampus applications, and the ability to recall and edit an application. Use OTP verification for email and mobile on the enquiry form.
- Support Head of School comments for the founder, with accept and waitlist outcomes and a way to view uploaded documents.
- Collect application fees through a payment gateway, with campus-specific fee structures and bank details.
- Separate K-12 and CMRNPUC dashboards and produce stage, source, campus, grade, TAT, call, and disqualified/junk reports.
- Keep prior-year databases in CRM for nurture without firing the current-year incoming-lead workflow until the parent takes action.
- Connect accounting so each legal entity can invoice and reconcile correctly. One Books organisation can sit under Zoho One; remaining entities need standalone Books subscriptions. Warehouses and bins apply only when storage locations belong to the same legal entity.

### Features used

Custom fields Workflows Webforms Bookings Campaigns SalesIQ Telephony Customer portal Dashboards Zoho Books

### Differentiating brands, campuses, and K-12 versus PU journeys

Zoho CRM holds the group as an account hierarchy: a group account, a brand account for each of Ekya Schools, Ekya Nava, CMRNPS, CMRNPUC, and Ekya Vana Early Years, and a campus account under the relevant brand.

Each enquiry carries Brand, Campus, Grade Applied, and App Type (K-12 or PU). Those fields drive assignment, communication, and reporting. PU applications follow a separate pipeline from K-12 school admissions, so a PUC 1 enquiry at CMRNPUC HRBR is not forced through the school visit and readiness-session path used for Grade 1 at Ekya JP Nagar.

Campus ownership is split across admissions users so follow-up and reporting can be read by campus. Future brands and placeholder campuses can be added as accounts and picklist values without redesigning the modules.

### Capturing every enquiry into one admissions record

The parent is stored as the lead. The student’s name, previous school, grade, and how the family heard about the school sit on the same record. Lead source values cover website, Meta ads, LinkedIn, Google ads, walk-in, inbound phone, social media, education fair, expo, referral, and database upload.

Webforms and landing pages create leads directly in CRM. There is no limit on the number of forms used across pages. Paid campaign sources such as Meta, LinkedIn, and Google Ads can be captured automatically; unique sources are added as picklist values when they appear.

Bulk upload is used for prior-year repositories. Those records sit in Leads (or a related module) for nurture. They do not inherit the current-year incoming-lead workflow until the parent takes an action, at which point the record is treated as a live enquiry and staged accordingly.

OTP verification for email and mobile is designed on Zoho Forms. CRM stores an OTP Verified flag so counsellors can see whether the enquiry was confirmed.

### Handling sibling, intercampus, and same-phone applications

Duplicate rules do not block a second lead on the same mobile number. A parent can start two applications, or enquire for two campuses, and each campus keeps its own record and nurture path.

Sibling Enquiry and Intercampus Enquiry flags, plus an application-type field, tell counsellors why a second record exists and how to connect the family without merging the journeys.

### Moving leads through an admissions stage model

Admissions uses a dedicated stage field so the journey is independent of any other sales process already in the org. The path is:

Enquiry → Application Initiated → Visit Scheduled / Visit Missed → Application Submitted → Review → Readiness Session → HOS Review → Founder Review → Accepted, Waitlist, Disqualified, or Junk.

Workflows set Enquiry when a branded lead is created, move the record to Application Initiated when a form is started, and to Application Submitted when the form is submitted. A 24-hour reminder task is created when the application is started but not completed.

Abandoned-form stage update from Zoho Forms is not native. Counsellors still see Form Status (Started, Submitted, Abandoned) on the CRM record, and partners can approximate the 24-hour chase with workflows after a form event is captured. The stage does not change on abandon unless that event reaches CRM.

Sub-stages remain available as free text so campus teams can record local status without exploding the main picklist.

### Booking campus visits and recovering missed slots

Parents receive a booking link by email or WhatsApp. The booking surface shows about two weeks of availability. Choosing a date opens 30-minute slots inside working hours. Confirmation goes to the admissions calendar and the parent.

CRM stores Visit Date and Visit Status (Not Booked, Booked, Reminder Sent, Attended, Missed, Rescheduled) and creates a 30-minute event on the lead. A workflow marks Reminder Sent the day before a booked visit. Tasks cover the day-before reminder, a 30-minute-before reminder with a reschedule option, and nurture if the parent misses the slot without rescheduling. Missed visits move the lead to Visit Missed.

Zoho Bookings can replace the event-and-task pattern as a full booking product, with Google Calendar connected if the group wants two-way busy/free on counsellor calendars.

### Keeping parents engaged with email and WhatsApp

Email and WhatsApp templates can include video, images, PDFs, and dynamic links. Workflows send stage- and grade-based messages. Campaigns send bulk email and WhatsApp to lists built from stage, sub-stage, campus, and grade.

Activity history on the lead records messages and emails sent, and read or open receipts where the channel provides them. SalesIQ can host a website or WhatsApp bot; that bot is a separate subscription from CRM.

Consumable limits follow the licensed edition: mass email inside CRM on Ultimate is 2000 per day; paid editions calculate CRM email as confirmed users × 300. Zoho Campaigns licenses 5000 contacts per user, with email to those contacts on that model.

### Routing inbound calls and recording activity on the lead

Four published hotlines feed the process: 080-46809096, 080 4709 1586, 080 6945 7788, and 080 4709 5123. After a VOIP provider is chosen from the CRM marketplace, IVR can route by department or campus, with round-robin to a central team and campus owner mapped from the IVR choice.

The enquiry owner is the user who receives or places calls for that lead. Call count and hotline number are stored on the record. Inbound and outbound calls are written to the lead’s activity history. TAT reminders can be emailed when first-response targets are missed.

### Reviewing applications with HOS and founder decisions

Once the application is submitted and the visit is attended, the deal represents the application moving toward admission. Head of School comments are captured on the record and shared with the founder. Founder Decision is Pending, Accept, or Waitlist. Setting Accept moves the lead to Accepted.

The designed portal experience adds document viewing and Accept / Waitlist actions for the founder. In CRM, HOS Comments and Founder Decision already support that conversation before the portal is live.

### Giving parents a portal to apply, upload, and track

Zoho Forms captures the enquiry and the fuller application. After the enquiry, the parent’s email can be invited to a CRM portal to see selected fields such as current stage. The portal is intended to hold application fields, photo and supporting-document upload, sibling and intercampus applications, and recall/edit of an in-progress form.

Thank-you pages on the enquiry form offer two next steps: book a campus tour, or start the application. Those links write back into Visit Status and Form Status so the counsellor sees what the parent did next.

### Collecting application fees across campuses

Application fees are collected through a payment gateway from the CRM marketplace. Gateway cost follows the publisher of that integration. Fee structure and bank details differ by campus, so the implementation maps payment settlement per campus rather than a single group account.

Zoho Books is used where the group wants accounting in the Zoho stack. One Books organisation can sit under Zoho One. Remaining legal entities need standalone Books subscriptions. Campuses in CRM are operational locations; they are not automatically finance entities. Legal-entity names, GST, and bank packs are configured when those details are provided. Warehouses and bins are used only if storage locations belong to the same legal entity.

### Reporting from enquiry to admission

Because every lead is tagged with brand, campus, grade, app type, source, owner, and stage, the group can build separate K-12 and CMRNPUC dashboards from the same org.

The reporting set requested by admissions includes:

- Stage-wise timeline at 24 hours, 3, 7, 15, and 28 days
- Call time and weekly targets; inbound and outbound status (dialled, answered) by user
- Leads not engaged at 3, 7, and 10+ days
- Campus / grade / source admitted; campus / grade enquiry-to-admission
- TAT call reports; leads unattended for two years; workflow reports to users
- Activity reports for calls scheduled, overdue, and completed, grouped as answered / not answered, and RNR / blocked / bounced
- Outcome reports with time buckets L7D, WoW, L30D, MoM, and breakouts by campus, grade, channel, and sales owner
- Efficiency measures such as time to first contact, follow-up on time, campus visits scheduled, applications submitted, funnel drop-off, time to process, and percentage admitted
- Disqualified and junk rates by the same time and campus/grade/source cuts

## Results

Admissions, marketing, and campus teams work from one CRM-led process instead of separate spreadsheets, inboxes, and campus lists.

Enquiries from forms, campaigns, walk-ins, fairs, phone, and historical databases land as structured leads with brand, campus, grade, and source. The same phone number can support two campus journeys. Sibling and intercampus intent is visible on the record. K-12 and PU stay on separate pipelines.

Counsellors see the stage, form status, visit status, tasks, and activity history for each family. Workflows start the journey on create, chase incomplete applications, remind before a campus visit, and move missed visits and founder accepts without a manual stage edit. HOS comments and founder accept or waitlist sit on the same file the counsellor has been nurturing.

When Forms, Bookings, Campaigns, SalesIQ, telephony, the parent portal, and payment gateways are connected in production, the same data model already distinguishes campuses, grades, and legal-entity accounting needs. Reporting can be split by K-12 versus PU and by campus without a second CRM.

*Please note that the solution described here is developed for a real admissions evaluation. Brand and campus names are those used in the customer’s SOP (EKYA/01/26-27). A public Zoho.com version would anonymise identifying details.*

---

Demo org, sample records, and SOP screenshots: [WALKTHROUGH.md](WALKTHROUGH.md)  
Live click-through: [DEMO-SCRIPT.md](DEMO-SCRIPT.md)
