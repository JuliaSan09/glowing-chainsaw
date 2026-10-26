# Republishing partner case studies

Process specification

## Table of contents

1. Introduction
2. Objectives
3. Requirements
3.1 Republished story
3.1.1 Purpose
3.1.2 Scope
3.1.3 Fields required
3.1.4 Data source
3.1.5 Data usage / flow
3.2 Permission record
3.2.1 Purpose
3.2.2 Scope
3.2.3 Fields required
3.2.4 Data source
3.2.5 Data usage / flow
4. Cross-record data mapping
4.1 Partner section to republished story
5. Conclusion

## 1. Introduction

Partners have already published case studies on their own sites and shared them with us. This work puts those stories on Zoho's customers page, in Zoho's format.

This document specifies the two records that work needs: the republished story, and the permission record that has to exist before that story goes live. It also specifies how a partner's text maps onto our page, and how the work runs from the first partner through the Find a Partner list and the partner-led webinars.

## 2. Objectives

- Publish the story in our format, in the present tense.
- The customer's quote names the Zoho product and the outcome. The partner's name is added to that quote when it is required.
- The partner stays in the story, in Partner engagement.
- The partner talks to the customer. Customer marketing does not. Partner account managers stay on the thread with us.
- Nothing goes live without the partner's approval of the draft and the customer's permission for Zoho's website.
- One process, so a conversation with a partner is not a fresh negotiation.
- Partner Store points stay as they are. An approved study is worth 10 points, up to 5 studies. This page does not add or remove points.
- Later, a new story arrives in this format, with the consent form already filled in.

## 3. Requirements

### 3.1 Republished story

#### 3.1.1 Purpose

The customers-page record of one customer. It is the story we publish.

#### 3.1.2 Scope

In scope:

- Stories already published on the partner's website and shared with us, or submitted to Partner Store.
- Products: CRM, Desk, and Campaigns.
- One partner at a time. An agreed set, sent in batches of five, six, or seven.
- Seven in a batch when the person quoted is still there and the facts are current. Five when we need new quotes.
- One revision after the partner reviews. Then we publish or we hold.

Out of scope:

- Customer marketing contacting the customer.
- A new customer with no story yet. They are introduced to the marketer who already writes original stories with partners. That work stays as it is.
- A second submission to Partner Store. An approved study cannot be resubmitted.
- Changing tier points.
- Holding a story until the page template can show the partner's name, logo, and link.
- Holding a story so it can debut in a webinar.

#### 3.1.3 Fields required

| Field name | Type | Description |
| --- | --- | --- |
| Title | Text | The customer, what changed, the product, and the partner's name. The partner's name is not in the title today. |
| Customer quote | Long text | Product and outcome. Partner's name only when required. |
| The company | Long text | Who the customer is. |
| The challenge | Long text | The problem, as it is now. |
| The solution | Long text | What the product does now. |
| Benefits and ROI | Long text | Outcomes. A number only if the partner says it is still true. |
| Partner engagement | Long text | How the partner came in, and the partner's quote. |
| Industry | Text | Side column. |
| Employees | Text | Side column. |
| Type of business | Text | Side column. |
| Customer logo | Image | Side column. Needs the customer's permission. |
| Partner logo | Image | Side column. Not on the page yet. Collected with the story. |
| Partner link | URL | Nofollow. Not on the page yet. Collected with the story. |

The nofollow link lets the reader visit. Zoho does not pass search credit. It is not a line telling the reader to hire the partner. The call to action at the end of the partner's own case study does not come onto our page.

#### 3.1.4 Data source

- The partner's published page, or the text submitted to Partner Store.
- The checklist in 3.1.5, returned by the partner.
- A first draft from the rewrite tool, read by a person before it is sent. If the tool is not ready, we draft by hand. The tool does not email the partner and does not file permission. It does not add a number the source does not contain.
- The tool flags a quote that would fail the test below, a stale fact, a product outside CRM, Desk, and Campaigns, a bundle that does not name the products, a missing partner quote, or a story whose only partner credit is a call to action. A flag is not quietly edited away.

#### 3.1.5 Data usage / flow

A quote passes when a Zoho product is named and an outcome is named. The partner's name may be in it when that is required. It fails when the partner is the only subject, or when the sentence is praise with no product and no outcome. We do not invent an outcome.

These lines were written for the test. They are not from a customer. Do not publish them.

Does not pass:

- "Our partner understood our business and changed how we work." No product. No outcome.
- "Zoho has been great." No product. No outcome.

Passes:

- "Zoho CRM is where the pipeline sits. Follow-ups go out without someone having to remember."
- "A ticket in Zoho Desk is on the same customer we already have in CRM."

The name on the quote has to be a person who will stand by it. If they have left, the old sentence does not get a new name. The partner gets a new sentence from someone who is there, and can refresh their own page at the same time. We do not refresh it for them.

1. Draft.
2. Send one batch. Each story goes with the checklist below.
3. The partner comes back with the quote, the customer's permission, and the corrections.
4. We revise once. If the second draft is still wrong, we stop and talk.
5. Publish when the quote passes, the partner has approved the revision, and the permission record is filled. Otherwise hold it, with the reason in one line to the partner. A held story does not block the rest and is not part of the next batch's count.
6. Send the next batch when the reviews on this one are back. The next batch can be drafted while we wait. It is not sent early.

Checklist. One per story. The partner returns it.

- Title on their site, and the URL
- Person to quote: name, role, still at the company
- If that person has left: the new person's name and role
- The quote
- What in the old story is no longer true
- Products, if it was sold as a bundle
- Partner name for the title, logo file for the side column, and the site address for the nofollow link
- Consent: the form submitted, or the email attached
- Anything that must not be published

### 3.2 Permission record

#### 3.2.1 Purpose

The row that proves we may publish this story on Zoho's website. No row, no publish.

#### 3.2.2 Scope

In scope:

- The customer's name, company name, and the products in the story. A bundle is named as the products in it.
- Logo and images, when we use them.
- The form first. An email from the customer if they will not fill the form in.

Out of scope:

- Treating permission for the partner's website as permission for ours.
- A phone call the partner describes to us.
- "The partner says the form was filled in," with nothing we can point at.

#### 3.2.3 Fields required

| Field name | Type | Description |
| --- | --- | --- |
| Partner | Lookup | The partner this story belongs to |
| Their title | Text | Title on the partner's site |
| Their URL | URL | Where the story is published now |
| Our working title | Text | Title we are writing |
| Customer name | Text | As it will appear |
| Company | Text | As it will appear |
| Products named in the consent | Text | CRM, Desk, Campaigns, as applicable |
| Form or email | Picklist | Which proof we have |
| Date | Date | When the proof arrived |
| Where the proof is | URL / file | The submission, or the forwarded email |
| Our URL | URL | Filled when the page is live |
| Status | Picklist | Draft / With the partner / Revising / Cleared / Published / Held |
| Hold reason | Text | One line, when status is Held |

#### 3.2.4 Data source

Permission for the partner's website is not permission for Zoho's website. Partner Store also asks for consent before submission and reuse: https://www.zoho.com/store/partner/help/partner-company-manage-case-studies.html

The Zoho form does not attach itself to the case study. Until it does, this link goes out with every batch: https://consent.zohocorp.com/#Consents

Gopal is checking the backend and will say how a submission gets tied to a story.

The form is the first ask. If the customer will not fill it in, the partner sends the email below. The customer replies. The partner forwards that reply. We do not send the email.

Subject: Permission to publish your story on Zoho's website

We are working with Zoho on a version of the story that is already on our website. Their version is rewritten for their site. It needs your permission, separate from the permission you gave us.

Reply to this email with a yes or a no.

A yes covers:

- your name, [name]
- [company]
- [Zoho CRM, Zoho Desk, Zoho Campaigns — only the ones in the story]
- your logo, and any photo we already use, on that page

If you would rather use the form, it is here: https://consent.zohocorp.com/#Consents

We ask for the form first. This email is for when you do not want to fill the form in.

#### 3.2.5 Data usage / flow

Open the row before the first draft goes to the partner. The words of the story can be finished before permission arrives. The page cannot go live before the row is filled.

When a form submission starts attaching to the story on its own, this sheet is what gets attached. It is not thrown away first.

## 4. Cross-record data mapping

| From | To | Purpose |
| --- | --- | --- |
| Partner's published story, or Partner Store text | Republished story | The source we rewrite |
| Partner checklist | Republished story | Quote, corrections, name, logo, link |
| Consent form or customer email | Permission record | Proof we may publish |
| Permission record | Republished story | The gate. No row, no publish |
| Republished story | Partner LinkedIn post | After the page is live. Uses Partner engagement and the partner quote. A story in review is not posted |
| Republished story | Partner-led webinar | A use case the partner can present. Dates in section 5 are tentative |

### 4.1 Partner section → republished story

The partner's case study is the source. These fields are what we keep. The call to action at the end of the partner's study does not move.

| Partner's section | Our field | Purpose |
| --- | --- | --- |
| Title card | Title | Outcome, product, and the partner's name |
| Overview and executive summary | The company | Who the customer is |
| Problem | The challenge | The problem now |
| Evaluation, proposed solution, implementation | The solution | What the product does now. How the partner did the work moves to Partner engagement |
| Results | Benefits and ROI | Outcomes still true |
| Partner quote, and how they were brought in | Partner engagement | The partner's place in the story |
| Closing customer quote | Customer quote | Only if it passes the test in 3.1.5 |

## 5. Conclusion

Short term: one partner at a time, on the batch in 3.1.5, for CRM, Desk, and Campaigns. Bring the partner account managers in before the first batch and keep them on the thread. Agree promotion with that account team before a page is live. The first partner is also how we check the rewrite tool. We do not wait for the tool. No date on the wider list until that first batch shows how long a quote and a permission take.

Long term: the same process for Find a Partner. Checked on 23 October 2026, that directory has 1,347 consulting partners and 2,319 story records. 1,039 of those stories are already a Zoho file. A story that is both in a partner's agreed set and on Find a Partner is done once.

A script could not open every external link on that check:

- 79 story pages on 23 partner sites blocked automated access. A person in a browser may still get through. Four of those partners returned a rate limit.
- 7 stories, from 6 partners, sit behind a login.
- 84 stories, under 28 directory names, are only a social link. Another 101 social links sit next to a Zoho file or a normal page, so those stories are not in the 84.
- 20 stories are on a third-party host that refused the request.
- 3 stories are on a site that is not the partner's own, and that site blocked the request.

Those links are not dropped. The partner supplies the text.

The products stay CRM, Desk, and Campaigns unless we add one later. Once a partner's existing stories are republished, the next story is written in this format and the customer fills the consent form before we draft. Whether partners hear that after the full list, or when their own stories are done, is still open.

The partner-led CRM webinars run alongside this. A published story with a filled permission record can be the use case the partner presents. Dates below are tentative. The Tuesday and Thursday slot, 8:30 PM IST, is tentative too.

| Segment | Tentative date | Topic |
| --- | --- | --- |
| Foundations | Tue 1 Sep 2026 | Lead capture done right: web, social and email into CRM |
| Foundations | Thu 3 Sep 2026 | One place for every customer: data model, dedupe and the single view |
| Foundations | Tue 8 Sep 2026 | Build your sales pipeline: stages, deals and visibility |
| Foundations | Thu 10 Sep 2026 | Never miss a follow-up: tasks, reminders and cadences |
| Foundations | Tue 15 Sep 2026 | Email inside CRM: templates, Outlook and Gmail sync |
| Foundations | Thu 17 Sep 2026 | Reports leadership checks every morning: dashboards and KPIs |
| Foundations | Tue 22 Sep 2026 | From lead to won: the full sales journey walkthrough |
| Foundations | Thu 24 Sep 2026 | Make it yours: custom modules, fields and layouts |
| Zia | Tue 29 Sep 2026 | Meet Zia: your AI assistant inside Zoho CRM |
| Automation | Thu 1 Oct 2026 | Workflow automation 101: rules, triggers and alerts |
| Automation | Tue 6 Oct 2026 | Blueprint: put your process on rails |
| Zia Agents | Thu 8 Oct 2026 | Your first Zia Agent: a lead-qualifying agent, built live |
| Zia Agents | Tue 13 Oct 2026 | The follow-up agent: Zia that nurtures and books meetings |
| Zia Agents | Thu 15 Oct 2026 | Zia deal intelligence: win probability and next best action |
| Zia Agents | Tue 20 Oct 2026 | CPQ and the Zia quote agent: instant, accurate quotes |
| Zia Agents | Thu 22 Oct 2026 | 100+ ready-made agents: the Zia Agent Store tour |
| Zia Agents | Tue 27 Oct 2026 | Build your own: a custom agent in Zia Agent Studio, no code |
| Omnichannel | Thu 29 Oct 2026 | WhatsApp and telephony in CRM |
| Cross-Zoho | Tue 3 Nov 2026 | CRM and Zoho Books: quotes, invoices and orders in sync |
| Cross-Zoho | Thu 5 Nov 2026 | CRM and Campaigns: nurture drips and newsletters that convert |
| Cross-Zoho | Tue 10 Nov 2026 | CRM and Desk: support tickets meet customer context |
| Zia Agents | Thu 12 Nov 2026 | Zia across CRM and Desk: an AI support-triage agent |
| Integrations | Tue 17 Nov 2026 | Integrations that matter: Outlook, QuickBooks and Zoho Flow |
| Cross-Zoho | Thu 19 Nov 2026 | Zoho One and CRM Plus: the connected suite |
| Migration | Tue 24 Nov 2026 | Move to Zoho CRM: from spreadsheets, HubSpot and Salesforce |
| Analytics | Thu 26 Nov 2026 | Analytics deep-dive with Zia. This date is US Thanksgiving, so it may move. |
| Vertical | Tue 1 Dec 2026 | Zoho CRM for Insurance |
| Vertical | Thu 3 Dec 2026 | Zoho CRM for Real Estate |
| Capstone | Tue 8 Dec 2026 | Your AI-powered CRM in 2026: the full Zia agent stack |
| Wrap | Thu 10 Dec 2026 | CRM adoption clinic: live org teardown and Q&A |
