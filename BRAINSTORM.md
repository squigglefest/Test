# MCP Server — Brainstorm

> Scratchpad of ideas for building an MCP (Model Context Protocol) server.
> Nothing here is locked in — it's a starting point to react to.

## 1. What is this server for?

The first decision. An MCP server exposes **tools**, **resources**, and/or
**prompts** to an AI client (Claude Desktop, Claude Code, etc.). Pick the
problem it solves before picking the tech.

Candidate purposes (pick one to start, keep it small):
- **Personal knowledge / notes** — search & read your own docs/notes.
- **Internal API wrapper** — expose an existing service (CRM, DB, ticketing)
  as clean tools so the model can act on it.
- **Dev/ops helper** — query logs, trigger deploys, check CI, read dashboards.
- **Data access** — read-only queries against a database or warehouse.
- **Domain glue** — stitch together 2–3 SaaS tools you use daily.

## 2. Capabilities to expose

| Type | What it is | Good first candidates |
|------|-----------|------------------------|
| **Tools** | Actions the model can call (functions) | `search`, `get_item`, `create_x` |
| **Resources** | Readable content addressed by URI | files, records, config |
| **Prompts** | Reusable prompt templates | "summarize this ticket", "draft reply" |

Start with **2–3 read-only tools**. Add write/mutating tools only once the
read path feels good — mistakes there are reversible.

## 3. Tech choices

- **Language/SDK**: TypeScript (`@modelcontextprotocol/sdk`) or Python
  (`mcp` package). Pick whichever your target API client is already in.
- **Transport**:
  - **stdio** — simplest, great for local tools launched by the client.
  - **HTTP / streamable HTTP** — for remote/hosted servers, multiple clients.
- **Hosting** (if remote): Cloudflare Workers, Vercel, a small container, or
  just run locally over stdio to start.

## 4. Auth & safety (don't skip)

- How does the server authenticate to the upstream system? (API key, OAuth)
- Where do secrets live? (env vars / secret store — never in the repo)
- Which tools mutate state? Mark them clearly; consider a dry-run/confirm step.
- Scope down: least-privilege tokens, read-only where possible to start.

## 5. Minimal first milestone (MVP)

1. Scaffold a server with the SDK.
2. One tool: `ping` / `echo` to prove the wiring.
3. One real read-only tool against your chosen data source.
4. Connect it to Claude Desktop/Code and call it end-to-end.
5. Then iterate: more tools, error handling, auth.

## 6. Open questions for you

- What's the **one problem** this server should solve first?
- What system(s) does it need to talk to?
- Local-only (stdio) or hosted/remote (HTTP)?
- TypeScript or Python?
- Any tools that should be **write-capable**, or read-only for now?

## 7. Notes / parking lot

_(Add freeform thoughts here as they come.)_
-
-
