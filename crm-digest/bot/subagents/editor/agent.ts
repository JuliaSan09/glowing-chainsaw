import { defineAgent } from "@grok/agent-sdk";

export default defineAgent({
  description:
    "Edit and cross-check a Zoho CRM Digest draft against What's New evidence and Digest format: fix claims, tone, gaps, links, and freshness flags. Returns the final draft plus blockers/nits.",
});
