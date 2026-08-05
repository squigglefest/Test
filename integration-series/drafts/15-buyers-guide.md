---
FRONT MATTER
---

**Working headline:** Questions to Ask Before Adding AI to Your Website

**Alternate headlines:**
1. The Buyer's Guide to AI Website Integrations for Real Estate Agents
2. Before You Give an AI the Keys: A Checklist for Agents

**Dek:** A plain checklist for evaluating any AI-website integration — what to ask, why it matters, and how Virtual Results answers each one.

**Hook (verbatim, first 2 sentences of body):** Adding AI to your website means handing something a set of keys. Before you do that with any vendor — including us — here's the checklist worth going through first.

**Top image concept:** [HERO: A newsprint-editorial collage of a classic consumer "buyer's guide" checklist — clipboard with checkboxes, styled like a Consumer Reports spread, but the items are about AI and website keys instead of appliances.]

**Internal links used (3-6):**
- `/auth-security` — "Who Holds the Keys?" (authentication/revocable access)
- `/listing-data-wars` — the listing data wars context
- `/mcp-vs-zapier` — Zapier comparison for the lock-in question
- `/what-is-mcp` — plain-English MCP definition
- `/use-cases` — the 12 things you can ask your website to do
- `/technical` — under-the-hood architecture for the audit trail question

**External sources list:**
- Anthropic MCP documentation (modelcontextprotocol.io) — used for the definition of MCP and the description of scoped, revocable access as a protocol-level design goal.
- [NEEDS SOURCE: any specific vendor pricing-opacity complaint or industry survey on AI-tool vendor lock-in in real estate — none cited; the article deliberately avoids naming competitor practices without a source]

**CTA placement:** Final section, "Talk to Us." **CTA type:** Hard ("talk to us" — no pricing named).

---

# Questions to Ask Before Adding AI to Your Website

Adding AI to your website means handing something a set of keys. Before you do that with any vendor — including us — here's the checklist worth going through first.

By now you know the shape of the idea: an [MCP server (Model Context Protocol — think of it as your website's AI connection)](/what-is-mcp) lets [an AI assistant act on your site](/overview) instead of just answering questions about it. That's genuinely useful. It's also a new kind of access to grant, and not every implementation of it deserves your trust equally.

This article is not another pitch. It's the checklist we'd want if we were the one buying — followed by an honest account of how Virtual Results answers each question. Where the honest answer is "it depends" or "ask your specific vendor," we say so.

## In This Article

- [Why This Checklist Matters Now](#why-this-checklist-matters-now)
- [Question 1: Who Owns the Data?](#question-1-who-owns-the-data)
- [Question 2: Can Access Be Revoked, Instantly and Completely?](#question-2-can-access-be-revoked-instantly-and-completely)
- [Question 3: What Can the AI Actually Touch — and What's Off-Limits?](#question-3-what-can-the-ai-actually-touch--and-whats-off-limits)
- [Question 4: Is There an Audit Trail?](#question-4-is-there-an-audit-trail)
- [Question 5: Are You Locked In?](#question-5-are-you-locked-in)
- [Question 6: Is the Cost Transparent?](#question-6-is-the-cost-transparent)
- [Question 7: Does It Work With the AI Tools You Already Use?](#question-7-does-it-work-with-the-ai-tools-you-already-use)
- [Question 8: What Happens When It's Wrong?](#question-8-what-happens-when-its-wrong)
- [Putting It Together: A One-Page Checklist](#putting-it-together-a-one-page-checklist)
- [Talk to Us](#talk-to-us)

<!-- SERIES_TOC: Your Website, On Speaking Terms -->

## Why This Checklist Matters Now

The pressure to add AI to a real estate website is real, and so is the pressure to move fast. Meanwhile the broader fight over who controls listing distribution — the subject of [the listing data wars](/listing-data-wars) — has made agents more aware than ever that access and ownership are not the same thing. A feed can be cut off. A syndication partner can change terms. The one channel you fully control is your own website, and that's exactly why it's worth being careful about who gets to operate it.

An AI integration is, functionally, a new user account with some amount of authority over your site. You wouldn't hand a new employee the keys to your MLS login, your CRM, and your blog without asking a few questions first. The same standard should apply here — vendor by vendor, regardless of who's asking.

## Question 1: Who Owns the Data?

**Ask:** When the AI reads or writes content on my site, does the vendor retain a copy, a license to reuse it, or any claim on it?

This is the single most-skipped question in software procurement, and it matters more with AI tools because the entire premise is that the assistant is handling your content — listings, blog posts, client-facing pages — on your behalf.

**How VR answers it:** The content on your website is yours. The integration is a connection that lets an approved AI assistant read and write through your own site's existing systems — it isn't a pipe that copies your listings into a third-party database for the vendor's own use. If you disconnect the integration, your content stays exactly where it was: on your site, under your ownership.

## Question 2: Can Access Be Revoked, Instantly and Completely?

**Ask:** If I need to cut off an AI assistant's access right now — because an employee left, a device was lost, or I simply want to pause — can I do that myself, immediately, without calling support?

This is the practical test of whether "you're in control" is a real design decision or a slogan. We covered the mechanics of this in detail in [Who Holds the Keys?](/auth-security): every connection should be scoped, credentialed per person or per app, and revocable independently of every other connection.

**How VR answers it:** Yes. Each connection is tied to a specific credential, and revoking one doesn't touch the others. Maria's laptop losing its connection doesn't touch Devon's phone. You don't need a support ticket to pull a key back — that's the entire point of the "keys to the building" model over a single shared password.

**Scenario:** Priya manages a four-agent team. When one agent leaves the brokerage mid-listing-season, she revokes that agent's website connection the same afternoon — before the agent has even cleared out their desk — without touching anyone else's access or changing a shared password everyone would have had to update.

## Question 3: What Can the AI Actually Touch — and What's Off-Limits?

**Ask:** Does the assistant have a defined scope, or does it have the same access as an administrator? Can it touch billing, user accounts, or site-wide settings, or is it limited to content — listings, posts, pages?

A tool that can draft a blog post should not, by the same credential, be able to change your domain settings or add a new admin user. Scope is a security property, not a feature.

**How VR answers it:** The integration is built around specific, named capabilities — creating and editing listings, publishing blog content, updating specific fields — documented plainly in [Beyond Blog Posts: 12 Things You Can Ask Your Website to Do](/use-cases). It is not a blanket administrator account handed to a chatbot. Anything outside that defined set — server configuration, billing, user permissions — isn't something the AI connection touches at all.

## Question 4: Is There an Audit Trail?

**Ask:** If a listing changes overnight, can I see who — or what — made the change, and when?

If a vendor can't answer this cleanly, that's the answer. "The AI did it" is not an audit trail.

**How VR answers it:** Actions taken through the integration are attributable — tied to the credential that authorized them — and changes to listings and posts follow the same drafting and versioning your site already uses for human edits. The key point: every action gets logged to the audit trail, so there's a clear record and no mysteries.

**Scenario:** Devon wakes up to find a listing's price updated overnight. Before assuming an error, he checks the activity: it was Devon's own assistant, acting on the "reduce to $475,000" instruction he gave it at 11 p.m. before bed. Nothing mysterious — just a record.

## Question 5: Are You Locked In?

**Ask:** If I stop using this vendor, what happens to my content, my workflows, and my ability to switch? Is the AI integration a proprietary format I'd have to unwind, or does it sit on top of standards I could take elsewhere?

We addressed the mechanics of this distinction in ["Isn't This Just Zapier?"](/mcp-vs-zapier): a fixed-recipe automation tool ties your workflow to its specific triggers and actions. MCP is an open protocol — Anthropic publishes the specification at modelcontextprotocol.io — which means the connection method itself isn't a proprietary black box, even though any given vendor's implementation of it still deserves scrutiny.

**How VR answers it:** Your website's content lives in your website, in standard formats, whether or not the AI integration is active. Turning the connection off doesn't strand your listings or posts in a vendor-specific format. This is a real trade-off worth asking any vendor about directly, because "built on an open protocol" and "easy to leave" are related but not identical claims — ask them both.

## Question 6: Is the Cost Transparent?

**Ask:** What does this cost, what triggers a price change, and is there a plain-language answer to "what am I actually paying for"?

You don't need a number from us in this article to ask a vendor this question well. You need to know whether they'll give you a straight answer without a sales call, and whether the pricing model tracks something you understand (seats, sites, usage) rather than something opaque.

**How VR answers it:** We'll walk you through pricing plainly when you talk to us — no pricing games, no "call for a quote" theater dressed up as a discovery call. That's a conversation, not a paragraph in a blog post, because it depends on your site and your team.

## Question 7: Does It Work With the AI Tools You Already Use?

**Ask:** Am I locked into one AI assistant, or can I connect the tools my team already has?

If the only way to use the integration is through one specific chatbot, that's a second, quieter form of lock-in.

**How VR answers it:** The integration works with various AI assistants — Claude, ChatGPT, and others — because the connection method itself isn't locked to a single AI product. It's a connection your website exposes; which assistant you point at it is your call.

## Question 8: What Happens When It's Wrong?

**Ask:** AI assistants make mistakes. When one does — drafts a listing with a wrong detail, misreads an instruction — what's the blast radius, and how do I catch it?

This is less a technical question than a design philosophy question. The honest answer from any vendor should acknowledge that mistakes happen, not promise they won't.

**How VR answers it:** Content created or edited through the integration follows your site's normal draft-and-review path rather than publishing itself silently to the world. Scope (Question 3) limits how much damage a bad instruction can do, and the audit trail (Question 4) means you can see and fix it. We don't claim the AI won't be wrong. We've built the guardrails around the fact that it sometimes will be.

## Putting It Together: A One-Page Checklist

Print this, forward it, or hand it to whoever evaluates software at your brokerage — for us or for anyone else:

1. Do I retain full ownership of my content?
2. Can I revoke access instantly, per person or per device, without a support call?
3. Is the AI's access scoped to specific actions, not full administrative control?
4. Is there an audit trail showing who or what made each change?
5. Am I locked into a proprietary format, or built on an open standard I could carry elsewhere?
6. Is pricing explained in plain language, without pressure tactics?
7. Can I use the AI assistants my team already has, or only one specific product?
8. What's the process when the AI gets something wrong?

If a vendor can't answer these eight questions in plain language, that's worth noticing — regardless of how good the demo looks.

## Talk to Us

We wrote this checklist because we think it holds up, not because it's a trick question with only one right vendor. If it raises follow-up questions about your specific site, your team, or how the [MCP server](/what-is-mcp) connection actually works day to day, that's exactly the conversation worth having.

Ready to see what your website could do if you could just ask? [Talk to Virtual Results](#) about connecting your site.

---

**Previous:** [#14 — Beyond Blog Posts: 12 Things You Can Ask Your Website to Do](/use-cases)
**Next:** This is the final article in the series — [return to the series overview](/overview).
