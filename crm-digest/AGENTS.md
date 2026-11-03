# crm-digest

Agent SDK project (`@grok/agent-sdk`) for the Zoho CRM Digest newsletter.
Root conductor plus subagents `ideation`, `drafter`, and `editor`.
The served agent's prompt is `bot/instructions.md`.

## Loop

```bash
npx --yes "@grok/agent-sdk@0.5.0" validate --dir .
npx --yes "@grok/agent-sdk@0.5.0" info --dir . --json
npx --yes "@grok/agent-sdk@0.5.0" run --dir . --message "..."
npx --yes "@grok/agent-sdk@0.5.0" eval --dir .
npm run check
```

Run the CLI under Node, never Bun.

## Layout

- `bot/instructions.md` is the always-on conductor prompt.
- `bot/tools/<name>.ts` is one tool per file. The filename is the tool name.
- `bot/subagents/<id>/` are ideation / drafter / editor roles (`description` required).
- `bot/schedules/monthly-design.md` fires on the 10th (UTC cron) for design day.
- `bot/lib/` is shared code. Never discovered.
- `evals/` is filesystem evals (`evals/evals.config.ts` required).
  Not `bot/evals/`. That path is ignored.

## Do not

- Grow host TypeScript for formatting, classification, or reply composition.
  That stays in instructions/skills. Host code owns auth, idempotency,
  evidence seeding, and side-effect gates.
- Add npm deps on a first cut. Stick to what `@grok/agent-sdk` already ships.
- Point `serve` at a parent folder during bring-up. It mounts every sibling.

## Pointers

- Package loop: `node_modules/@grok/agent-sdk/AGENTS.md`
- Skills: `node_modules/@grok/agent-sdk/skills/` (`create-agent`, `deploy`, `evals`, `hillclimb`, `debug`)
- Docs: `npx @grok/agent-sdk docs`
- LLM docs index: `node_modules/@grok/agent-sdk/dist/docs/llms.txt`
