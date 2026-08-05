---
FRONT MATTER
---
Working headline: Under the Hood: How the VR MCP Server Actually Works
Alternate headlines:
  - "The Plumbing Behind 'Just Ask': A Technical Walkthrough of the VR MCP Server"
  - "What Happens Between the Question and the Published Post"

Dek: A plain-language walkthrough of the protocol, permissions, and request path behind the VR MCP server — for the broker who wants receipts, or their tech person.

Hook (verbatim as it appears in body): For the broker who wants receipts (or their tech person). This one gets technical on purpose.

Top image concept: [HERO: A cutaway "blueprint" illustration in newsprint-editorial collage style — a house rendered as architectural line art, with a cross-section revealing a small control room inside where a switchboard operator (labeled "MCP server") sits between a rotary phone labeled "Claude / ChatGPT" and a wall of levers labeled "Publish," "Edit Listing," "Update Price." Technical annotations in the margins like a patent diagram.]

Internal links used (3–6):
  - `/what-is-mcp` — anchor: "plain-English guide to MCP"
  - `/mcp-vs-zapier` — anchor: "why that's different from a Zapier workflow"
  - `/auth-security` — anchor: "how permissions and credentials are handled"
  - `/connect-claude` — anchor: "connecting Claude to your site"
  - `/howto-blog-post` — anchor: "asking your website to publish a post"
  - `/use-cases` — anchor: "the full list of things you can ask for"

External sources list:
  - Anthropic, "Introducing the Model Context Protocol" (Nov 2024) — https://www.anthropic.com/news/model-context-protocol
  - Model Context Protocol specification, "Architecture" overview — https://modelcontextprotocol.io/docs/learn/architecture
  - Model Context Protocol specification, "Tools" concept page — https://modelcontextprotocol.io/docs/concepts/tools
  - Model Context Protocol specification, "Transports" (JSON-RPC 2.0 base protocol) — https://modelcontextprotocol.io/docs/concepts/transports
  - [NEEDS SOURCE: any independent benchmark or count of "how many MCP servers exist" or similar ecosystem-size stat — omitted from body until sourced]

CTA placement: Final section, single paragraph, after "What This Means for You."
CTA type: Mid — "see a demo"
---

# Under the Hood: How the VR MCP Server Actually Works

For the broker who wants receipts (or their tech person). This one gets technical on purpose.

Every other article in this series keeps things at street level: you ask, the website does the thing. That's true, and it's the right way to think about it day to day. But some of you — or the person you call when the website breaks — want to know what's actually happening in between the asking and the doing. This article is for that person.

We're going to use real terms here: tools, resources, prompts, JSON-RPC. If you've read the [plain-English guide to MCP](/what-is-mcp), you already have the metaphor — an assistant with keys to the building, rather than a vending machine of fixed recipes. This article opens the building up and shows you the wiring.

## Jump to:
- [The short version](#the-short-version)
- [What MCP actually standardizes](#what-mcp-actually-standardizes)
- [The three building blocks: tools, resources, prompts](#the-three-building-blocks-tools-resources-prompts)
- [A request, start to finish](#a-request-start-to-finish)
- [What the VR server actually exposes](#what-the-vr-server-actually-exposes)
- [Where permissions fit in](#where-permissions-fit-in)
- [What This Means for You](#what-this-means-for-you)

<!-- SERIES_TOC: Your Website, On Speaking Terms -->

## The short version

The Model Context Protocol (MCP) is an open standard, published by Anthropic, that defines how an AI assistant talks to an external system — a database, an app, a website's back end — in a structured, predictable way (Anthropic, "Introducing the Model Context Protocol," Nov 2024, https://www.anthropic.com/news/model-context-protocol). The VR MCP server is our implementation of that standard, built specifically for real estate agent websites.

When you type a request to Claude or ChatGPT and your site responds, three things are happening: the assistant is interpreting your words, the protocol is carrying a structured message back and forth, and the VR server is the thing on the other end that actually knows how to edit a listing or publish a post. MCP is the wiring. The VR server is the appliance plugged into it.

## What MCP actually standardizes

Before MCP, if a company wanted an AI assistant to control their software, they built a custom integration — one-off code that only worked with one assistant, maintained forever by whoever built it. MCP replaces that with a shared protocol, so any MCP-compatible assistant can talk to any MCP server without custom glue code (Anthropic, "Introducing the Model Context Protocol," https://www.anthropic.com/news/model-context-protocol).

Under the hood, MCP runs on JSON-RPC 2.0 — a lightweight, decades-old messaging format for asking a remote system to run a specific function and get a structured answer back, rather than a paragraph of prose (MCP specification, "Transports," https://modelcontextprotocol.io/docs/concepts/transports). Think of it as the difference between mailing a letter in free-form prose and filling out a form with labeled fields — the form is slower to write but impossible to misread on the other end.

That structure is the whole point. It's also the detail that separates this from [a Zapier workflow](/mcp-vs-zapier): Zapier connects fixed triggers to fixed actions that a human wired together in advance. MCP lets the assistant discover what's possible and decide, in the moment, which structured action fits what you asked for.

## The three building blocks: tools, resources, prompts

MCP servers expose functionality to an assistant in three main shapes (MCP specification, "Tools," https://modelcontextprotocol.io/docs/concepts/tools):

**Tools** are actions the assistant can take — publish a post, update a listing price, upload a photo. Each tool has a name, a plain-language description, and a defined set of inputs it expects. When the assistant decides a tool fits your request, it calls that tool with the right inputs and gets a structured result back.

**Resources** are things the assistant can read — the current text of a listing, a list of recent blog posts, your site's category list. Resources give the assistant context before it acts, the way you'd skim a file before editing it.

**Prompts** are pre-written instruction templates the server can offer the assistant for common jobs — for example, a template that walks through the right structure for [a new listing blog post](/howto-blog-post), so the assistant doesn't have to reinvent that structure from scratch every time.

Put together: resources are what the assistant can see, tools are what it can do, and prompts are shortcuts for doing common things well.

## A request, start to finish

Here's a concrete run-through. Diane, a broker in Sarasota, tells Claude: "Change the price on the Bayshore listing to $649,000 and note it's now show-anytime."

1. **Interpretation.** Claude reads Diane's request and checks what tools the connected server has told it are available. It sees a tool called something like `update_listing`, with a description explaining it edits price and showing-status fields on an existing listing.

2. **Discovery.** If Claude isn't sure which listing "Bayshore" refers to, it may first call a resource or a search tool to look it up — the same way you'd search before you edit.

3. **The call.** Claude sends a structured JSON-RPC request to the VR MCP server: essentially, "call `update_listing`, with these arguments: listing ID, new price, new showing note."

4. **Execution.** The VR server receives that call, checks that the request is well-formed and that Diane's connection has permission to edit listings (more on that below), and then does the actual database update on VR's side.

5. **The response.** The server sends back a structured result — success, plus the updated listing fields — or a structured error if something went wrong (wrong ID, missing permission, invalid price format).

6. **The report.** Claude translates that structured result back into plain English for Diane: "Done — Bayshore is now listed at $649,000 and marked show-anytime."

Every step in the middle is protocol. The only two places anything resembling free-form language shows up are the start (Diane's sentence) and the end (Claude's confirmation). Everything in between is a form filled out correctly.

## What the VR server actually exposes

Concretely, the VR MCP server exposes tools that map to the things agents actually do on their site: creating and editing blog posts, creating and editing listings, managing media, and reading back current content and site structure so the assistant has accurate context before it acts. [The fuller list of what you can ask for](/use-cases) covers each one in plain language; this article is just showing you that behind each of those, there's a defined tool with defined inputs — not a black box guessing at your intent.

That mapping matters for a specific reason: it means the assistant can only do things the server explicitly exposes. It cannot improvise a database query or reach into parts of the site nobody built a tool for. The boundary of "what the AI can touch" is drawn by the tool list, not by what the assistant feels like trying.

## Where permissions fit in

None of this works without an identity check. Every call to the VR server carries credentials tied to a specific user connection — the same way [connecting Claude to your site](/connect-claude) involves a one-time authorization step, not a shared master password. The server checks those credentials before running any tool, and drafts stay drafts — unpublished — until a human explicitly approves publication. [How permissions and credentials are handled](/auth-security) covers that layer in full; the short version is that the protocol carries the request, but authorization decides whether the server acts on it.

## What This Means for You

You don't need to know JSON-RPC to use this. Diane didn't write a single line of code — she typed a sentence. But if you're the kind of broker who wants to know there's a defined, auditable path between "I asked" and "it happened" — rather than a vague AI doing vague things to your listings — now you've seen it. Structured calls, defined tools, permission checks, and a human approval step before anything goes live.

If you'd rather see this in motion than read about it, [see a demo](#) of the VR MCP server working against a live site — watch the request happen and the result come back in real time.

---

**Previous:** [#3 — "Isn't This Just Zapier?" — No, and Here's the Difference](/mcp-vs-zapier)
**Next:** [#5 — How to Publish a Blog Post by Asking for One](/howto-blog-post)
