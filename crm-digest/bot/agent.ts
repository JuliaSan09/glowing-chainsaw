import { defineAgent } from "@grok/agent-sdk";

export default defineAgent({
  name: "crm-digest",
  description:
    "Multi-agent Zoho CRM Digest newsletter conductor: ideation, drafting, and editing from What's New.",
  model: {
    id: "grok-4.7",
    params: [
      { id: "reasoning_effort", value: "high" },
      { id: "fast", value: "true" },
    ],
  },
  hosting: {
    // Public Zoho marketing feeds used by server tools.
    egressDomains: [
      "www.zohowebstatic.com",
      "www.zoho.com",
      "zoho.com",
    ],
  },
});
