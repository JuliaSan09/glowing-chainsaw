import { defineAgent } from "@grok/agent-sdk";

export default defineAgent({
  description:
    "Draft the Zoho CRM Digest newsletter document from an approved ideation brief. Writes Digest-shaped markdown copy only; does not invent features or skip the brief.",
});
