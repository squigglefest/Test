# The Keys to Your Website — Series Style Brief (shared by every article)

## Project
Educational blog series on the Virtual Results (VR) MCP server, published on the VR real estate site as an edu-sales funnel. National-magazine accessible (People-level readability), professionally polished, peer-reviewed quality bar.

## Positioning / sales thesis (must thread through every article)
Every product marketed as a "real estate MCP server" today (Bright Data, Apify/Redfin, BatchData, agentic-ops) is a data-extraction tool — it scrapes listings and property records INTO an AI. Nobody is publishing about an MCP server that lets an AI operate the agent's OWN website. And nobody explains MCP to real estate professionals in plain language — existing content is developer documentation. This series owns both gaps.

The industry is at war over who controls listing data (Zillow v. Compass/MRED antitrust suit, Clear Cooperation's unraveling, private listing networks, feed cutoffs). The one distribution channel an agent fully owns is their website. This series teaches agents that their website can now be operated by asking — and Virtual Results is the company that makes that true.

## Terminology (use consistently)
- First reference in the article: "MCP server (Model Context Protocol — think of it as your website's AI connection)". Use the exact phrase "MCP server" at least once in the article, for SEO.
- After first reference, prefer: "the integration," "your website's AI connection," "the connection."
- Never use unexplained jargon — no "tools/resources/prompts," no "JSON-RPC" — outside the technical article (#4).
- Metaphor of record: an assistant with keys to the building (vs. Zapier's vending machine of fixed recipes). Reuse it. The series name is "Your Website, On Speaking Terms" — it plays off the idea that the website now listens and responds, so lean into that in headers/intros where natural, without forcing it into every paragraph.

## Voice
People-magazine accessible, professionally polished. Short paragraphs. Concrete scenarios with named fictional agents (e.g., "Maria has a price change at 9 pm…"). NO hype words (revolutionary, game-changer, groundbreaking, cutting-edge, seamless). Explain every acronym on first use. Reading level ~10th grade for Tier A articles.

## Sourcing rules (strict)
- Real-estate industry claims: cite trade press of record — Inman, HousingWire, The Real Deal — or primary documents (court filings, NAR policy pages). Include the link (or a clearly marked [SOURCE: description + what to link]) next to the claim.
- Technical MCP claims: cite Anthropic's MCP documentation / modelcontextprotocol.io.
- If other vendors publish in this space (Bright Data, Apify, etc.), link to them and differentiate honestly: they pull data in; we let you operate what you own. Confidence, not FUD.
- NO unsourced statistics. NO invented quotes. Every external claim needs a link/citation or it must be cut. If you cannot verify a stat with real knowledge, mark it [NEEDS SOURCE: claim] instead of inventing one — do not fabricate.

## The controversy (background context — especially for #13, referenced elsewhere)
Cover honestly, both sides: Zillow's Listing Access Standards, Compass private exclusives/"private listing networks" (PLNs), the Zillow v. MRED + Compass antitrust suit (filed May 2026, N.D. Ill.), a Chicago-area feed cutoff affecting roughly 43,000 listings, Clear Cooperation Policy's unraveling, consolidation (Compass–Anywhere, Rocket–Redfin). Editorial stance: neutral and defensible — control of distribution is genuinely contested right now, so investing in the channel you fully own (your website) is the prudent move regardless of how the legal fights resolve. Do not take a side on who's "right" in the litigation.

## Media placeholders (brackets only — no production yet)
Insert production-ready, specific bracket placeholders: [HERO: …] [GRAPHIC: …] [ANIMATION: …] [VIDEO: …] [SCREENSHOT: …]. Each describes concept, purpose, and key elements in 1–3 sentences. Visual style of record: newsprint-editorial collage look. Example of good specificity:
[GRAPHIC: side-by-side "recipes vs. toolbox" — Zapier as a vending machine dispensing fixed cards; MCP as an open toolbox an assistant picks from. Newsprint-collage style.]

## Structural requirements every article must deliver
1. **Front matter block** at the top:
   - Working headline + 2 alternate headlines
   - Dek (1 sentence)
   - Hook (first 2 sentences, verbatim as they'll appear in the body)
   - Top image concept: [HERO: …]
   - 3–6 internal links used (list the target slugs from the roster below + anchor text)
   - External sources list (all citations used, as a bullet list of description + link or [NEEDS SOURCE])
   - CTA placement (which paragraph/section) and CTA type (soft: "read the series" / mid: "see a demo" / hard: "talk to us")
2. **In-article jump-link TOC** (H2 anchors) near the top, after the hook.
3. **Series TOC mention**: include a placeholder comment `<!-- SERIES_TOC: Your Website, On Speaking Terms -->` where the reusable series nav component will render (this gets built once and injected into every article later — don't hand-write the list of all 15 articles yourself).
4. **Body** in full Markdown, with H2/H3 structure, short paragraphs, at least one concrete named-agent scenario.
5. **Contextual internal links**: minimum 3, maximum 6, linking first mention of a concept covered elsewhere in the series to that article's slug (e.g., mentions of authentication/security → link to `/auth-security`; "unlike Zapier" asides → link to `/mcp-vs-zapier`). Use markdown link syntax with the slug as a relative link, e.g. `[authentication](/auth-security)`.
6. **Exactly one CTA** at the end — no CTA stacking. Match funnel stage:
   - Awareness (soft: "read the series") — articles #1–3
   - Consideration (mid: "see a demo") — articles #4–12
   - Decision (hard: "talk to us") — articles #13–15
7. **Prev/next footer links** using the roster order below (use slug + working headline; if prev/next isn't in this batch, still name it — it will resolve once all articles are drafted).

## Full roster (for TOC, prev/next, and cross-links — order is the series TOC order)
1. `overview` — Your Real Estate Website Can Take Instructions Now (awareness)
2. `what-is-mcp` — What Is an MCP Server? A Plain-English Guide for Real Estate Pros (awareness)
3. `mcp-vs-zapier` — "Isn't This Just Zapier?" — No, and Here's the Difference (awareness)
4. `technical` — Under the Hood: How the VR MCP Server Actually Works (consideration)
5. `howto-blog-post` — How to Publish a Blog Post by Asking for One (consideration)
6. `howto-listing` — How to Create or Edit a Listing by Asking (consideration)
7. `connect-claude` — Connect Claude to Your Website in 10 Minutes (consideration)
8. `connect-chatgpt-codex` — Connect ChatGPT and Codex to Your Website (consideration)
9. `connect-cli` — For Power Users: Connecting from the Command Line (consideration)
10. `connect-gui` — No Terminal Required: GUI Ways to Connect (consideration)
11. `team-rollout` — Getting Your Whole Team Connected (consideration)
12. `auth-security` — Who Holds the Keys? Authentication and Security, Explained (consideration)
13. `listing-data-wars` — The Listing Data Wars: Why Owning Your Website Matters More Than Ever (decision)
14. `use-cases` — Beyond Blog Posts: 12 Things You Can Ask Your Website to Do (consideration)
15. `buyers-guide` — Questions to Ask Before Adding AI to Your Website (decision)

## CTA copy for decision-stage articles (13, 15)
Use "talk to us" as the hard CTA — do not name pricing. Example: "Ready to see what your website could do if you could just ask? [Talk to Virtual Results](#) about connecting your site."

## Deliverable format
Output ONLY the final Markdown file content (front matter block + TOC + body + footer), nothing else — no meta-commentary before or after.
