# Partner story pipeline

Pulls case studies from the public Find a Partner directory, keeps the ones that can be read, and prepares a Zoho customers-page draft for CRM, Desk, and Campaigns.

The Catalyst project was not connected from this environment, so the runner stores the same rows locally. `catalyst/story-table.json` is the Data Store table. Files belong in a Stratus bucket named `partner-story-files`. Do not use File Store. It sunsets on 31 October 2026.

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
