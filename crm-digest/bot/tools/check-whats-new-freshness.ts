import { prompt } from "@grok/agent-sdk";
import { defineTool } from "@grok/agent-sdk/tools";
import * as z from "zod/v4";
import {
  WHAT_NEW_PAGE,
  loadDigestIssues,
  loadYearLists,
  monthName,
  newestMonthWithNotes,
  parseMonthNo,
} from "../lib/zoho-feeds.js";

function monthsBehind(
  newestYear: number,
  newestMonth: number,
  asOfYear: number,
  asOfMonth: number,
): number {
  return asOfYear * 12 + asOfMonth - (newestYear * 12 + newestMonth);
}

export default defineTool({
  description: prompt`
    Check whether Zoho CRM What's New looks updated enough to design the
    monthly Digest. Flags stale or thin content relative to the design day
    (about the 10th; Digest sends on the 20th). Call this on every Digest run.
  `,
  effect: "read",
  inputSchema: z.object({
    asOf: z
      .string()
      .regex(/^\d{4}-\d{2}-\d{2}$/)
      .optional()
      .describe("ISO date YYYY-MM-DD to evaluate against (default: today UTC)."),
    maxMonthsBehind: z
      .number()
      .int()
      .min(0)
      .max(6)
      .optional()
      .describe(
        "Flag stale when newest What's New month is this many months behind asOf (default 1).",
      ),
    minNotesInNewestMonth: z
      .number()
      .int()
      .min(1)
      .max(20)
      .optional()
      .describe("Flag thin when newest month has fewer notes than this (default 1)."),
  }),
  async execute({
    asOf,
    maxMonthsBehind = 1,
    minNotesInNewestMonth = 1,
  }) {
    const asOfDate = asOf ? new Date(`${asOf}T12:00:00.000Z`) : new Date();
    if (Number.isNaN(asOfDate.getTime())) {
      throw new Error(`Invalid asOf date: ${asOf}`);
    }
    const asOfYear = asOfDate.getUTCFullYear();
    const asOfMonth = asOfDate.getUTCMonth() + 1;
    const asOfDay = asOfDate.getUTCDate();

    // Design kickoff is ~10th; send is 20th. Issue month = calendar month of send.
    const issueMonth = asOfMonth;
    const issueYear = asOfYear;
    const designDay = 10;
    const sendDay = 20;
    const daysUntilDesign = designDay - asOfDay;
    const daysUntilSend = sendDay - asOfDay;

    const yearLists = await loadYearLists();
    const newest = newestMonthWithNotes(yearLists);
    const digests = await loadDigestIssues();
    const latestDigest = digests.length
      ? [...digests].sort((a, b) => {
          const ay = Number(a.year) * 12 + Number(a.month);
          const by = Number(b.year) * 12 + Number(b.month);
          return by - ay;
        })[0]
      : null;

    const flags: Array<{
      severity: "blocker" | "warning";
      code: string;
      message: string;
    }> = [];

    if (!newest) {
      flags.push({
        severity: "blocker",
        code: "whats_new_empty",
        message:
          "What's New feed returned no release notes. Do not treat the Digest as ready for design.",
      });
    } else {
      const behind = monthsBehind(
        Number(newest.year),
        newest.monthNo,
        asOfYear,
        asOfMonth,
      );
      if (behind > maxMonthsBehind) {
        flags.push({
          severity: "blocker",
          code: "whats_new_stale",
          message: `What's New content is not updated: newest month with notes is ${monthName(newest.monthNo)} ${newest.year} (${behind} month(s) behind ${monthName(asOfMonth)} ${asOfYear}). Flag for the CRM content owners before design locks.`,
        });
      } else if (behind === maxMonthsBehind && asOfDay >= designDay) {
        flags.push({
          severity: "warning",
          code: "whats_new_lagging_on_design_day",
          message: `On/after design day (${designDay}), newest What's New month is still ${monthName(newest.monthNo)} ${newest.year}. Confirm mid-month updates are published.`,
        });
      }
      if (newest.count < minNotesInNewestMonth) {
        flags.push({
          severity: "warning",
          code: "whats_new_thin",
          message: `Newest What's New month (${monthName(newest.monthNo)} ${newest.year}) has only ${newest.count} note(s).`,
        });
      }
    }

    if (latestDigest) {
      const digestMonth = parseMonthNo(latestDigest.month);
      const digestYear = Number(latestDigest.year);
      const digestBehind = monthsBehind(
        digestYear,
        digestMonth,
        issueYear,
        issueMonth,
      );
      if (digestBehind >= 2 && asOfDay >= designDay) {
        flags.push({
          severity: "warning",
          code: "digest_archive_lag",
          message: `Latest published Digest on the archive is ${latestDigest.issueName} (${monthName(digestMonth)} ${digestYear}). Expect a new issue for ${monthName(issueMonth)} ${issueYear}.`,
        });
      }
    }

    const stale = flags.some((f) => f.severity === "blocker");

    return {
      sourcePage: WHAT_NEW_PAGE,
      asOf: asOfDate.toISOString().slice(0, 10),
      cadence: {
        designDay,
        sendDay,
        issueMonth,
        issueYear,
        issueLabel: `${monthName(issueMonth)} ${issueYear}`,
        daysUntilDesign,
        daysUntilSend,
      },
      newestWhatsNew: newest
        ? {
            year: newest.year,
            monthNo: newest.monthNo,
            month: monthName(newest.monthNo),
            noteCount: newest.count,
          }
        : null,
      latestDigest: latestDigest
        ? {
            issueName: latestDigest.issueName,
            title: latestDigest.title,
            month: latestDigest.month,
            year: latestDigest.year,
            readmoreLink: latestDigest.readmoreLink ?? null,
          }
        : null,
      stale,
      readyForDesign: !stale,
      flags,
      summary: stale
        ? "BLOCKER: What's New content does not look updated enough for Digest design."
        : flags.length
          ? "What's New looks usable, with warnings to review."
          : "What's New looks updated enough for Digest design.",
    };
  },
});
