import { prompt } from "@grok/agent-sdk";
import { defineTool } from "@grok/agent-sdk/tools";
import * as z from "zod/v4";
import {
  DIGEST_ARCHIVE_PAGE,
  loadDigestIssues,
  monthName,
  parseMonthNo,
} from "../lib/zoho-feeds.js";

export default defineTool({
  description: prompt`
    List recent Zoho CRM Digest issues from the public archive metadata.
    Use for issue numbering, tone reference links, and knowing the last shipped month.
  `,
  effect: "read",
  inputSchema: z.object({
    limit: z
      .number()
      .int()
      .min(1)
      .max(24)
      .optional()
      .describe("How many recent issues to return (default 6)."),
  }),
  async execute({ limit = 6 }) {
    const issues = await loadDigestIssues();
    const sorted = [...issues].sort((a, b) => {
      const ay = Number(a.year) * 12 + Number(a.month);
      const by = Number(b.year) * 12 + Number(b.month);
      return by - ay;
    });
    const items = sorted.slice(0, limit).map((issue) => {
      const monthNo = parseMonthNo(issue.month);
      return {
        issueName: issue.issueName,
        title: issue.title,
        description: issue.description,
        monthNo,
        month: monthName(monthNo),
        year: issue.year,
        readmoreLink: issue.readmoreLink ?? null,
      };
    });
    return {
      sourcePage: DIGEST_ARCHIVE_PAGE,
      count: items.length,
      latestIssueNumber: items[0]?.issueName ?? null,
      issues: items,
    };
  },
});
