---
name: zoho-crm-case-study
description: >-
  Write or revise a Zoho CRM customer case study in the style of the stories
  published at zoho.com/crm/customers. Use when drafting a case study, customer
  story, success story, use-case narrative, directory card, headline, pull
  quote, key-results block, or "features that helped" list for Zoho CRM.
---

# Write a Zoho CRM case study

Write the way the stories on [zoho.com/crm/customers](https://www.zoho.com/crm/customers/) are written. This file was taken from that directory (204 entries in October 2026: 135 written case studies, 69 video stories) and from the long-form pages behind them, including Brigade Plus, IDT, CIMCO, ESCO, MindNation, Way.com, Shiji, Valenta, FundsIndia, Selectra, and Revision Energy.

The customer is the subject. Zoho CRM is how they did the work. A number appears only when the customer stated it.

## What you produce

Most requests need both of these.

1. **Directory card.** The line on the customers index. One sentence, usually 8–16 words (the live set has a median of 12 and a 90th percentile of 16). Almost every card names Zoho.
2. **Story page.** The article at `/crm/customers/{slug}`.

Also return the sidebar facts and the directory filters when you have them. They are part of the published page, not optional metadata.

## Facts to collect before drafting

Stop and ask for anything on this list you cannot point to in the source notes. Do not fill the gap with a plausible number, quote, or product.

- Legal customer name, and the division that actually uses CRM if those differ (Brigade Plus inside Brigade Group, NRS inside IDT).
- One speaker: name, title, company. Confirm the spelling once and keep it.
- What the business sells, where, and since when.
- Scale the customer will put in public: employees, offices, customers, revenue, or growth. Omit any figure they will not approve.
- The system they left, by name: spreadsheets, Google Sheets, ACT!, Salesforce, Vtiger, SAP C4C, a homegrown tool, email.
- What broke: growth, regional silos, adoption, cost, no single pipeline, field teams with no mobile record.
- What they run in Zoho CRM now, in the order of a working day.
- Other Zoho apps and third-party tools that are actually connected.
- Results they will say out loud. A time comparison ("two weeks" to "a few minutes") counts. An invented percentage does not.
- Who implemented it: the customer's own team, Zoho, or a named partner, and how long it took.
- Industry, region, country, employee band, and B2B / B2C / D2C.
- Whether the piece is a public zoho.com story or an internal implementation brief.

## Choose the length from the material

| Shape | When | Length |
| --- | --- | --- |
| Short page | One speaker, one previous system, one change, at most two results | 350–700 words |
| Standard page | A company history, an evaluation or rollout, several capabilities, a result | 800–1,500 words |
| Flagship | Several products across a whole operating company, with quantified results | Up to about 2,600 words |
| Video page | The directory label is Videos | Headline, one quote, and a short Challenge / Solution / Results. Do not stretch it into a flagship. |
| Web summary of a PDF | The long narrative lives in a download | Short page plus Key results, and one line that points to the PDF |

Match length to how much happened. A 400-word story that has been padded to 1,500 reads as a different genre from the archive.

## Headline

Sentence case. No period at the end. Name Zoho CRM, or a specific feature when that feature is the story. Put either the customer or a measured outcome in the same line.

Use one of these shapes. They are the shapes on the live pages.

- `{Company} {verb} {outcome} with Zoho CRM`
  Brigade Plus transforms sales management and customer journeys with Zoho CRM.
- `{Who they are} {sees or achieves} {metric} {by or after} {implementing or using} Zoho CRM`
  Largest industrial refrigeration contractor in North America sees a 20% boost in sales upon employing Zoho CRM.
- `Zoho CRM {delivers or helps} {outcome} {to or at} {company}`
  Zoho CRM delivers 100% ROI to Singapore-based audiovisual company, ESCO.
- `How {company} {achieved} {one specific change} with Zoho CRM {Feature}`
  How the Streaming Network achieved automation without loopholes with Zoho CRM Blueprint.

Prefer the first shape for a named customer. Use the second when a single metric is the reason to read. Use the fourth when one feature did the work. The verb is concrete: transforms, achieves, uses, switches, finds, drives, runs, sees. Skip "leverages" and "unlocks".

The directory card is this headline, or a tighter version of it that still stands alone.

## Page structure

### Standard page

Use this for a new zoho.com story.

```
# Headline

"{Opening quote.}"
Full Name, Title, Company

## Key results:
- Label value
- Label value

## The company
## The challenge
### {Only if the evaluation or a second pain is its own scene}
## The solution
### {Outcome phrase}
### {Outcome phrase}
## Benefits and ROI
## Looking forward
```

Drop **Key results** when you do not have two figures. Drop **Looking forward** when the customer has not named a next step. Keep the remaining sections in this order.

### Short page

```
# Headline

"{Opening quote.}"
Full Name, Title, Company

{One paragraph on who they are, if the quote did not already say it.}

## Challenge
## Solution
## Results

## Would you recommend Zoho?
"{One sentence.}"
Full Name, Title, Company
```

Older pages use this shape (FundsIndia, Selectra, Revision Energy, Allergy Standards). Use it when the material is a single thread. The recommendation heading is optional and only appears when you have a recommendation quote that is different from the opening quote.

Pick one closer. A page has Benefits and ROI, or Results, or Before and after. It does not have all three.

## How each section is written

**Opening quote.** Sits under the headline, before any section. One to three sentences, spoken, with "I" or "we". It does one of these jobs: says what changed, gives a number, names why they chose Zoho, or recommends it. The attribution is its own line, `Full Name, Title, Company`, with no "says" on that line.

**Key results.** Two to four lines. The label is a noun phrase and the value is the figure, the way the live pages do it: `Adoption 100%`, `Payback period 6 months`, `Productivity increase 6X`, `Revenue increase 42%`, `Time saved on day to day sales activities 18hrs/week`. No sentence, no hedging word.

**The company.** One or two paragraphs. Founded year, place, what they sell, who buys it, and the scale numbers you are allowed to print. If a division is the CRM customer, say how it sits inside the parent. No product pitch in this section. IDT's page adds a one-sentence "in this case study we will" line. Leave that line out.

**The challenge.** Name the previous system. Then the moment it stopped working, tied to growth or to a job the team could not do. Then the requirement in operational language: one pipeline, assignment by region, a record management can trust, a mobile app for field teams. Two short paragraphs, or two H3s when the pains are distinct. Published H3s read like `Orchestrating the sales process` and `Assisting management`.

If they evaluated another product, that is its own short scene, usually an H3. State who compared what, any figure the customer gave, and the reason they chose Zoho. CIMCO's page does this with a Salesforce implementation quote of $1,000,000 against a Zoho implementation of $30,000, told as David Fauser's decision. Keep that restraint. The narrator does not score the other product.

Implementation can close the challenge or open the solution: how long it took, who configured it, and the customizations that matched the business (currencies, territories, approval rules, custom modules). ESCO's page says the CRM was customized and rolled out in a month after a Philippines trial. Way.com's page says the move from Vtiger took about four months. Use the real duration.

**The solution.** Follow the working day, not the product menu.

1. Where leads come from, and how they land in CRM.
2. How they are assigned.
3. The pipeline or Blueprint the team now follows.
4. The automation that removed a manual step.
5. What the manager sees in reports or dashboards.
6. The other Zoho app or third-party tool, named on both sides of the integration.

Every feature shares a sentence with the job it does. "Workflow rules assign web leads to the regional owner and create the follow-up task" is a case-study sentence. "They use workflows, assignment rules, and Blueprint" is a feature list.

H3s are outcomes, not feature names: `Managing lead flow`, `Visibility into sales operations with customized reports`, `An enhanced end-to-end sales process`. Add an H3 when a section would otherwise run past about 150 words. Name the users and the volume: 150 sales executives, 370 users, 400,000 leads, used daily.

**Benefits and ROI.** Before and after on the same activity. Weeks to minutes, a spreadsheet to a dashboard, a portion of customers processed to a higher portion. Put the customer's figure in the same paragraph as the change. If you have no figure, describe the change in steps or time and do not invent one. Call the section `Benefits` when there is no payback or ROI figure.

**Looking forward.** One short paragraph, future tense, in the customer's plans: the next Zoho app, the next region, the next team. It is not a recap and it is not a call to action. The site already adds "Share your Zoho CRM success story" after the article.

**Would you recommend Zoho?** Only on a short page, and only with a fresh quote. One or two sentences. FundsIndia's closer is the speaker saying they vouch for Zoho to anyone who asks. Do not reprint the opening quote here. Several older pages do that. Do not.

## Quotes after the opening

Place a later quote at the end of the paragraph it proves. One quote in a section. Attribute a new speaker in full. After the first mention in the body, use the last name, and "says" is enough.

A usable quote is specific. These published lines show the grain, short enough to imitate:

- Function, in the speaker's metaphor: "Zoho CRM is essentially the brain of our company. It holds all of our memory." Aurian De Maupeou, Selectra.
- A non-specialist describing a real capability: "I'm not an IT person, but I can quite easily make whatever chart or graph that I want to help me understand or diagnose what's going on." David Fauser, CIMCO.

Write a quote only from words the person said. If the notes contain no quote, leave the quote out and say so, rather than composing one in their voice.

## Voice

- Third person. Past tense for the decision and the old system. Present tense for what the team does in CRM now.
- The customer, a team, or the named person is the grammatical subject. Zoho CRM arrives with "with", "using", or as a possessive: "Zoho CRM's reports gave management a daily view of the pipeline."
- Paragraphs of two to five sentences.
- Contractions inside quotes. Spell out contractions in the narration.
- No exclamation marks in the narration.
- No throat-clearing: "In this case study", "let's dive in", "it's worth noting".
- Adjectives attach to a fact. "Significant improvement" needs the number in that paragraph. If there is no number, describe the step that disappeared.
- One spelling system for the whole piece, taken from the customer's country. US: realize, organization. UK, Ireland, India, Australia, New Zealand: realise, organisation.
- A person is introduced once, with title. Keep accents and spelling identical after that. Published pages sometimes drift (Bajas / Bájàs). Do not.

## Product names

First body mention is `Zoho CRM`. After that, `Zoho CRM` or `the CRM`. `Zoho` alone means the company or the suite.

Use the published feature names when they are actually in the story: Blueprint, Zia, Workflow rules, Assignment rules, Canvas, Reports, Dashboards, SalesInbox, custom modules, predictive sales, the mobile app.

Name other apps in full: Zoho Desk, Zoho Analytics, Zoho Campaigns, Zoho Cliq, Zoho Creator, Zoho Projects, Zoho SalesIQ, Zoho Forms, Zoho Bookings, Zoho One. Older pages say Zoho Reports. Use Zoho Analytics unless you are quoting the customer.

**Features that helped** is a chip list of 4–8 features this customer uses. Short labels, as on the live pages: `Customization`, `Blueprint`, `Workflow automation`, `Reports & Analytics`, `Integrations`, `Mobile app`, `Zia`. List only features the solution section already described.

## Sidebar and directory filters

Sidebar, on the article:

- Industry type. This can be more specific than the directory bucket. Brigade's page says Interior design while the directory files the story under Real Estate.
- Employees. A band is fine: `Below 50`, `51-200 employees`, `201-500 employees`, `501-1000`, `1000-5000 employees`.
- Type of business. Plain words: `B2C`, `Privately held`, `Digital Marketing Agency`.

Directory filters, for the index entry:

- Label: `Case study` or `Videos`
- Industry, from the directory's industry list
- Region and country
- Employee band: `50 and below`, `51-200`, `201-500`, `Above 500`
- Business process: `B2B`, `B2C`, or `D2C`
- Link text: `Read More` for a story page. Use `Read full story` only when you are pointing at a long flagship.

## Public story or implementation brief

A public zoho.com story is the narrative above. It does not include license limits, seat math, fee tables, internal SOP codes, unreleased roadmap detail, or a requirements bullet list.

An implementation brief for evaluators can add a Requirements section and name fields, stages, and connected apps. Mark it as an internal brief at the top, and still open with the customer, the old system, and the change. Do not present the brief as the public case study. The Ekya admissions write-up in this repository is that second kind of document.

## Draft from this skeleton

Replace every brace. Delete a section you cannot fill. Do not leave a brace in the draft you return.

```
# {Headline}

"{Opening quote.}"
{Full Name}, {Title}, {Company}

## Key results:
- {Label} {value}

## The company
{Founded, where, what they sell, scale. One or two paragraphs.}

## The challenge
{Previous system, what broke, what they needed.}

### {Evaluation or second pain, or delete this heading}
{Who decided, what they compared, the reason Zoho won, how long implementation took.}

## The solution
{One paragraph of orientation: who uses CRM, and for which process.}

### {Outcome}
{Where work enters, who owns it, which feature does that job.}

### {Outcome}
{The next step in the same day: pipeline, automation, mobile, or a named integration.}

### {Outcome}
{What a manager can see now.}

## Benefits and ROI
{Before and after on the same activity. The customer's figure.}

## Looking forward
{The next team, region, or Zoho app they have named.}

Industry type {specific}
Employees {band}
Type of business {B2B, B2C, or plain description}
Features that helped us
{four to eight chips}
```

Directory card, on its own line under the page:

`{8–16 word card that names Zoho}`

## Check before you return the draft

- The headline is sentence case, names Zoho CRM or one feature, and can be read without the page.
- The card is one sentence, about 8–16 words, and still makes sense on the index.
- The first line under the headline is a real quote, then `Name, Title, Company`.
- Company, then challenge, then solution, then one closer, in that order.
- The previous system is named.
- Each Zoho feature appears in a sentence about the job it does.
- Every number traces to the source notes. Key results was removed if there were not two of them.
- No quote is repeated. No quote was written for the customer.
- One spelling system. One spelling of the speaker's name.
- The sidebar chips match capabilities the solution section already described.
- A public story contains no license math, SOP codes, or unapproved figures.
- Word count sits in the band the material earned.
