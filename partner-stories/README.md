# Partner story pipeline

Pulls case studies from the public Find a Partner directory, keeps the ones that can be read, and prepares a Zoho customers-page draft for CRM, Desk, and Campaigns.

The stories live in the `PartnerStories` Data Store table in the `PartnerStories` Catalyst project. `catalyst/story-table.json` is the table definition, and `src/export_catalyst_csv.py` builds the file that loads it. Files belong in the Stratus bucket `partner-story-files`. Do not use File Store. It sunsets on 31 October 2026.

Nothing here publishes a page or contacts a customer.

## Run

From this directory:

```bash
python3 src/test_stories.py
python3 src/index_profiles.py
python3 src/build_stories.py
python3 src/download_sources.py
```

`index_profiles.py` asks for one profile about every two seconds. A faster pace gets the directory to refuse further calls for several minutes. The script waits that out and continues. It is safe to stop and run again.

`download_sources.py` fetches Zoho-hosted files for stories that are in scope, or whose product is not on the record yet. It skips social-only links and products outside CRM, Desk, and Campaigns.

## What a row means

`ready` is a CRM, Desk, Campaigns, or CRM Plus story with a file or a page. CRM Plus is flagged because the draft has to name the products in the bundle.

`needs_product` is a file or page with no product id. The text decides whether it is rewritten.

`held` is a social-only link, a story with no link, or a product outside the three.

Drafts follow `.cursor/skills/zoho-crm-case-study/SKILL.md` on the case-study skill branch, plus the Partner engagement section in `docs/partner-case-studies/republishing-partner-case-studies.md`. A number or a quote is copied from the source. It is not written in for the customer.

`catalog/stories.jsonl` is the index from the first full run (26 October 2026). Descriptions and testimonials are left out of that file because a few of them contained an email address or a phone number.

## First run

1,348 partners, 2,319 stories, no failed profile calls.

| Status | Stories |
| --- | --- |
| Text saved, ready to draft | 889 |
| Held, product outside CRM, Desk, and Campaigns | 1,227 |
| Held, only a social link | 84 |
| Held, page did not open | 50 |
| Held, file had no text layer | 33 |
| Held, page had no readable text | 27 |
| Held, site blocked the request | 6 |
| Held, login wall | 2 |
| Held, no link | 1 |

Of the 889 with text, 626 are Zoho-hosted files and 263 are web pages. The proof draft is `examples/junxion.md`. The rest are not rewritten yet. A person still edits every draft before it goes to a partner.

## Drafts

`drafts/<story_id>.md` holds one draft per story. The exporter marks any story with a draft file as `drafted` and puts the text in the `draft` column. `data/` is not committed, so source text has to be downloaded again before a story is drafted.

Batch 1 is seven drafts: Junxion (`examples/junxion.md`, copied here) and six more, chosen from CRM stories with enough source text and from different partners. None has a customer quote in the source that passes the quote test, except AndersonDodson. Each draft ends with a Flags list for the editor.

The catalog has 2,300 distinct stories after removing 19 duplicate rows. 875 have text. 7 are drafted, 868 are not.
