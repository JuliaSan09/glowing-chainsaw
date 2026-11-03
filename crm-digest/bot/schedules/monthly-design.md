---
cron: "0 4 10 * *"
---

It is Digest design day (around the 10th; Zoho CRM Digest sends on the 20th).

Run the full multi-agent CRM Digest pipeline for this calendar month's issue:

1. check-whats-new-freshness
2. fetch-release-notes for the current year (recent months)
3. list-past-digests
4. ideation → drafter → editor

Return the full output package (status, freshness, issue meta, final draft, editor findings, sources).

If What's New is not updated, keep status blocked-pending-whats-new and lead with blocker flags so content owners can act before design lock.
