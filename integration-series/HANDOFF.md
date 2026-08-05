# Handoff: "Your Website, On Speaking Terms" Series

**Date:** August 5, 2026
**Status:** All 15 articles drafted and quality-gated. Publishing is blocked pending a live site connection.

---

## What's included

15 Markdown draft articles (`01-overview.md` through `15-buyers-guide.md`), plus the shared `style-brief.md` used to brief every drafting/review agent. Everything also lives in the repo `squigglefest/Test`, branch `claude/integration-series-orchestration-xsrrys`, as draft PR [#2](https://github.com/squigglefest/Test/pull/2).

## Series name

**"Your Website, On Speaking Terms"** — your call, replacing the placeholder "The Integration Series."

## Pipeline completed (per the original orchestration plan)

| Stage | Status |
|---|---|
| Brief | Done — shared style-brief.md covers positioning, terminology, voice, sourcing rules, controversy background, roster, structural requirements |
| Draft | Done — all 15 (Tier A on Sonnet, Tier B on Haiku, per the cost tiering in the plan) |
| Peer review | Done — every article reviewed by a separate agent against the rubric (accuracy, voice, reading level, link plan, jargon, singular CTA) |
| Fact-check | Done — article 13's 9 flagged claims verified via web search against Inman/HousingWire/The Real Deal/court records/NAR; other articles' unverifiable claims left as flagged `[NEEDS SOURCE]` rather than fabricated |
| Interlink audit | Done — hub-and-spoke `/overview` links added to every article's intro, contextual links kept to 3–6 per article, prev/next footer chain verified 1→15, no orphan slugs |
| Quality gate | Done — every article scored 1–10 ("would a national magazine run this?"); all 15 currently score ≥8 and are PUBLISH-ready |

## What still needs a human before anything goes live

1. **Article 12 (`auth-security`)** — 3 claims about VR's actual product behavior are flagged `[NEEDS SOURCE]` and need your team to confirm or correct:
   - The exact permission-scope tiers exposed at connection setup, and whether they're user-configurable
   - Whether revoked-key actions are visible in an audit trail
   - VR's specific key rotation/expiration policy
   You already reviewed this article and said it's fine as-is — flagging again here only because the underlying product claims are still unverified, not because the writing needs another pass.

2. **Article 13 (`listing-data-wars`)** — the lawsuit reference intentionally omits an exact court docket/case number (verified everything else: filing date, court, parties, the ~43,000-listing feed cutoff, Clear Cooperation status, and confirmed the Compass–Anywhere and Rocket–Redfin deals are already closed, not pending). You said to just leave the docket number out — done, nothing further needed here.

3. **Articles 7, 8, 10** (Claude/ChatGPT/GUI connection how-tos) — the step-by-step UI instructions (button labels, menu paths) were never verified against the live Claude.ai / ChatGPT / VR connection-tool interfaces. Language has been hedged ("look for something like...") rather than stated as fact, but before publish someone should actually walk through the real UI and correct/confirm the steps and screenshots.

4. **No media exists yet.** Every `[HERO: ...]` `[GRAPHIC: ...]` `[SCREENSHOT: ...]` `[ANIMATION: ...]` bracket is a placeholder describing what should be produced, in the newsprint-editorial collage style. None of it has been made.

5. **Publishing path is unresolved.** The plan calls for dogfooding — publishing via the VR MCP server itself, with the how-to screenshots coming from doing it for real. That requires either:
   - The NovaMira MCP connector (`virtualresults.com novamira mcp`) to be enabled for a Claude session — it's installed at the org level but was still showing `enabledInChat: false` as of this handoff, or
   - Using the already-connected "Virtual Results Website" tool against one of its 5 sites (`chatmls-kellernewyork.virtualresults.com`, `chatmls-agentinc.virtualresults.com`, `rtrsells.com`, `empowerhome-team.com`, `agentinc.com`) if one of those is actually the intended target — never confirmed.

## Open decisions still on record from the original plan

- Pricing in article 15's close: you said stay with "talk to us," not naming pricing. Done.
- Publish order once live: 1, 2, 3 first, then how-tos weekly, controversy (#13) + close (#15) last, per the original plan — not yet started.

## Files in this handoff

- `drafts/01-overview.md` through `drafts/15-buyers-guide.md`
- `style-brief.md`
- This document
