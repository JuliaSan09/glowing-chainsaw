import { defineEval } from "@grok/agent-sdk/evals";

export default defineEval({
  tags: ["smoke"],
  description:
    "Freshness tool runs and the conductor is asked to start the Digest pipeline.",
  async test(t) {
    await t.send(
      'Check whether Zoho CRM What\'s New is updated enough for Digest design. Call check-whats-new-freshness and summarize the flags. Do not draft the full newsletter yet.',
    );
    t.succeeded();
    t.calledTool("check-whats-new-freshness");
  },
});
