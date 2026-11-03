import { prompt } from "@grok/agent-sdk";
import { defineTool } from "@grok/agent-sdk/tools";
import * as z from "zod/v4";
import {
  WHAT_NEW_PAGE,
  flattenNotes,
  loadYearLists,
  monthName,
  parseMonthNo,
} from "../lib/zoho-feeds.js";

export default defineTool({
  description: prompt`
    Fetch Zoho CRM What's New release notes from the public JSON feed.
    Use before ideation or drafting a Digest. Filter by year and/or month,
    or ask for the most recent N notes across months.
  `,
  effect: "read",
  inputSchema: z.object({
    year: z
      .string()
      .regex(/^\d{4}$/)
      .optional()
      .describe("Calendar year, e.g. 2026. Omit for all years."),
    monthNo: z
      .number()
      .int()
      .min(1)
      .max(12)
      .optional()
      .describe("Month number 1–12. Omit for all months in the year filter."),
    limit: z
      .number()
      .int()
      .min(1)
      .max(80)
      .optional()
      .describe("Max notes to return (default 40)."),
    includeDescription: z
      .boolean()
      .optional()
      .describe("Include full Description text (default true)."),
  }),
  async execute({
    year,
    monthNo,
    limit = 40,
    includeDescription = true,
  }) {
    const yearLists = await loadYearLists();
    const notes = flattenNotes(yearLists, { year, monthNo, limit }).map(
      (n) => ({
        id: n.id ?? n.releaseNote_id ?? null,
        year: n.year,
        monthNo: n.monthNo,
        month: monthName(n.monthNo),
        title: n.Title,
        description: includeDescription ? n.Description : undefined,
        ecosystem: n.Ecosystem ?? n.LabelClass ?? null,
        function: n.Function ?? null,
        edition: n.Edition ?? [],
        dc: n.DC ?? [],
        readMoreUrl: n.Readmore_link ?? null,
      }),
    );

    const monthsTouched = [
      ...new Set(notes.map((n) => `${n.year}-${n.monthNo}`)),
    ];

    return {
      sourcePage: WHAT_NEW_PAGE,
      filter: {
        year: year ?? null,
        monthNo: monthNo ?? null,
        monthLabel: monthNo != null ? monthName(parseMonthNo(monthNo)) : null,
        limit,
      },
      count: notes.length,
      monthsTouched,
      notes,
    };
  },
});
