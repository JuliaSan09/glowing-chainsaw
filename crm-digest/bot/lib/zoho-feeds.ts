/** Public Zoho CRM feed helpers shared by server tools. */

export const RELEASE_NOTES_URL =
  "https://www.zohowebstatic.com/sites/zweb/images/crm/json/crm-release-notes.json";

export const DIGEST_ARCHIVE_URL =
  "https://www.zohowebstatic.com/sites/zweb/json/crm/newsletter-details.json";

export const WHAT_NEW_PAGE =
  "https://www.zoho.com/crm/whats-new/release-notes.html";

export const DIGEST_ARCHIVE_PAGE =
  "https://www.zoho.com/crm/resources/digest.html";

export type ReleaseNoteItem = {
  releaseNote_id?: string;
  Title: string;
  Description: string;
  Ecosystem?: string;
  LabelClass?: string;
  DC?: string[];
  Function?: string;
  Edition?: string[];
  read_moreTxt?: string;
  Readmore_link?: string;
  ThumbImge?: string;
  VideoUrl?: string;
  id?: string;
};

export type MonthList = {
  monthNo: number | string;
  DetailsList: ReleaseNoteItem[];
};

export type YearList = {
  yearName: string;
  monthLists: MonthList[];
};

export type DigestIssue = {
  issueName: string;
  description: string;
  title: string;
  readmoreTxt?: string;
  readmoreLink?: string;
  month: string;
  year: string;
};

const MONTH_NAMES = [
  "January",
  "February",
  "March",
  "April",
  "May",
  "June",
  "July",
  "August",
  "September",
  "October",
  "November",
  "December",
] as const;

export function monthName(monthNo: number): string {
  return MONTH_NAMES[monthNo - 1] ?? `Month ${monthNo}`;
}

export function parseMonthNo(value: number | string): number {
  const n = typeof value === "number" ? value : Number(value);
  if (!Number.isFinite(n) || n < 1 || n > 12) {
    throw new Error(`Invalid monthNo: ${value}`);
  }
  return n;
}

export async function fetchJson<T>(url: string): Promise<T> {
  const res = await fetch(url, {
    headers: {
      Accept: "application/json",
      "User-Agent": "crm-digest-agent/1.0",
    },
  });
  if (!res.ok) {
    throw new Error(`Fetch failed ${res.status} for ${url}`);
  }
  return (await res.json()) as T;
}

export async function loadYearLists(): Promise<YearList[]> {
  const data = await fetchJson<{
    release_notes: Array<{ yearLists: YearList[] }>;
  }>(RELEASE_NOTES_URL);
  const lists = data.release_notes?.[0]?.yearLists;
  if (!lists?.length) {
    throw new Error("release_notes.yearLists missing or empty");
  }
  return lists;
}

export async function loadDigestIssues(): Promise<DigestIssue[]> {
  const data = await fetchJson<{ BulletinList: DigestIssue[] }>(
    DIGEST_ARCHIVE_URL,
  );
  return data.BulletinList ?? [];
}

export function flattenNotes(
  yearLists: YearList[],
  opts: { year?: string; monthNo?: number; limit?: number } = {},
): Array<ReleaseNoteItem & { year: string; monthNo: number }> {
  const out: Array<ReleaseNoteItem & { year: string; monthNo: number }> = [];
  for (const year of yearLists) {
    if (opts.year && year.yearName !== opts.year) continue;
    for (const month of year.monthLists) {
      const monthNo = parseMonthNo(month.monthNo);
      if (opts.monthNo != null && monthNo !== opts.monthNo) continue;
      for (const note of month.DetailsList ?? []) {
        out.push({ ...note, year: year.yearName, monthNo });
      }
    }
  }
  // Newest year/month first as listed; keep stable order within month.
  out.sort((a, b) => {
    const y = Number(b.year) - Number(a.year);
    if (y !== 0) return y;
    return b.monthNo - a.monthNo;
  });
  return opts.limit != null ? out.slice(0, opts.limit) : out;
}

export function newestMonthWithNotes(
  yearLists: YearList[],
): { year: string; monthNo: number; count: number } | null {
  for (const year of yearLists) {
    const months = [...year.monthLists].sort(
      (a, b) => parseMonthNo(b.monthNo) - parseMonthNo(a.monthNo),
    );
    for (const month of months) {
      const count = month.DetailsList?.length ?? 0;
      if (count > 0) {
        return {
          year: year.yearName,
          monthNo: parseMonthNo(month.monthNo),
          count,
        };
      }
    }
  }
  return null;
}
