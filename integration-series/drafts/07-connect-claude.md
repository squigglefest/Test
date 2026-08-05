---
headline: "Connect Claude to Your Website in 10 Minutes"
alternates:
  - "Give Claude the Keys to Your Website"
  - "Three Steps to AI That Knows Your Listings"
dek: "Step-by-step, screenshots included, zero terminal."
hook: "Step-by-step, with screenshots at every stage — no terminal required. Your website already has an MCP server (Model Context Protocol — think of it as your website's AI connection) running. Claude just needs the key."
hero: "[HERO: screenshot of Claude chat window with a question about a new listing, and a response panel showing data from the agent's website. Split layout showing "your question" and "your website's answer." Newsprint-editorial style.]"
internal_links:
  - slug: "overview"
    anchor_text: "Your Real Estate Website Can Take Instructions Now"
  - slug: "what-is-mcp"
    anchor_text: "MCP server"
  - slug: "howto-listing"
    anchor_text: "how MCP works with your listings"
  - slug: "auth-security"
    anchor_text: "credentials safely"
external_sources:
  - "Anthropic Claude documentation: https://claude.ai/docs"
  - "[NEEDS SOURCE: VR MCP server authentication flows and API credential generation]"
  - "[NEEDS SOURCE: Claude.ai integration interface and connector setup steps]"
cta:
  type: "mid"
  stage: "consideration"
  placement: "final section before prev/next"
  copy: "Want to see this working with real listings? See a demo."
series_comment: "<!-- SERIES_TOC: Your Website, On Speaking Terms -->"
---

## In This Article

- [Why Connect Claude to Your Website?](#why)
- [What You'll Need](#requirements)
- [Step-by-Step: Connect in 10 Minutes](#steps)
  - [Step 1: Get Your VR API Key](#step-1)
  - [Step 2: Open Claude and Navigate to Integrations](#step-2)
  - [Step 3: Paste Your Key and Select Your Website](#step-3)
  - [Step 4: Test Your Connection](#step-4)
  - [Step 5: Try Your First Question](#step-5)
- [Troubleshooting: Quick Fixes](#troubleshooting)
- [Next Steps](#next)

<!-- SERIES_TOC: Your Website, On Speaking Terms -->

Step-by-step, with screenshots at every stage — no terminal required. Your website already has an MCP server (Model Context Protocol — think of it as your website's AI connection) running. Claude just needs the key.

This guide walks you through the most straightforward setup path. For context on why your website can now take AI instructions, read the [overview](/overview) of the series.

## Why Connect Claude to Your Website? {#why}

Right now, Claude is smart but it doesn't know your business. It can't tell you if a listing sold yesterday, pull your current inventory, or answer a question about your open house schedule. Connect Claude to your [MCP server](/what-is-mcp), and suddenly it has the keys to your website—it can read everything and answer questions about your specific business. You'll be able to ask Claude to help with tasks like [creating or editing listings](/howto-listing) without leaving the chat.

Imagine Sarah, an agent in Denver, gets a client call at 9 pm: "What was the sale price of that house on Maple Street?" Instead of digging through files, Sarah opens Claude, types the question, and gets the answer in three seconds. That's what this connection does.

## What You'll Need {#requirements}

Before you start, gather these three things:

1. **Your VR API Key** — a unique credential that tells Claude your website is real and authorized. We'll show you where to find this in the first step. (Want to know how [credentials are kept safe](/auth-security)? We cover that in a separate article.)
2. **A Claude account** — free or Pro, both work the same for this integration.
3. **About 10 minutes** and a quiet spot to follow along.

If you've already set up Claude before, this will feel familiar—it's the same pattern you'd use to connect any AI assistant to a tool.

## Step-by-Step: Connect in 10 Minutes {#steps}

Note: menu labels and exact click paths below reflect our best understanding of the current flow. Interfaces change, and we haven't verified every label against the live product — treat these as "here's roughly what to expect," and use the [SCREENSHOT] cues and general shape of each step as your guide if a label has shifted.

### Step 1: Log into Your Virtual Results Dashboard and Copy Your API Key {#step-1}

Go to your VR website's admin dashboard (the login link was in your onboarding email). Once logged in, look for something like a section labeled "Integrations" or "API Settings" in the left sidebar.

[SCREENSHOT: VR dashboard login page with sidebar highlighted, showing "Integrations" option in the menu]

You should see a box along the lines of "API Key for External AI Assistants." Look for a copy button next to it—this is your unique connection credential, and it's the only secret you need to share with Claude. Keep it handy for the next step.

[SCREENSHOT: Integrations settings page with API key box displayed, copy button highlighted with cursor hovering over it]

### Step 2: Open Claude and Navigate to Integrations {#step-2}

Open [Claude.ai](https://claude.ai) in your browser and sign in if you're not already. Look for your profile picture or name, typically in the bottom left corner of the sidebar, and open something like a "Settings" menu from there.

[SCREENSHOT: Claude chat interface with profile menu open in bottom left, showing "Settings" option highlighted]

From Settings, look for an option along the lines of "Integrations" or "Connected Tools." Claude's menu names shift from time to time, so if you don't see that exact wording, look for anything related to connecting outside tools or data sources.

[SCREENSHOT: Settings page with "Integrations" or "Connected Tools" menu item highlighted]

### Step 3: Find Virtual Results and Paste Your Key {#step-3}

You should see a list of available integrations. Scroll or search for "Virtual Results" or "VR MCP." When you find it, look for a button along the lines of "Connect."

[SCREENSHOT: Integrations list showing various tools; Virtual Results MCP option highlighted or visible in the list]

A dialog box should appear asking you to paste your API key. This is the credential you copied in Step 1. Paste it into the field for the API key and look for a button like "Authorize" or "Connect."

[SCREENSHOT: Dialog box with an input field labeled "API Key" and an "Authorize" button, with the key field ready for input]

Claude will verify your key and sync with your website automatically. You should see some kind of green checkmark or "Connected" message when it's done. Once that appears, Claude knows where your website is and has permission to read from it.

[SCREENSHOT: Success screen showing "Connected to Virtual Results" with a green checkmark, and a list of available data sources (e.g., "Listings," "Blog Posts," "Team Info")]

### Step 4: Test Your Connection {#step-4}

Go back to the Claude chat window (click "Back to Chat" or close the Settings panel). Start a new conversation and ask Claude a simple question about your website—something like "How many listings do I have right now?" or "What's my newest blog post?"

Claude will check your website through the connection you just set up. If everything's working, it'll come back with real data from your site—not generic text, but your actual listings, dates, and information.

[SCREENSHOT: Claude chat showing a user message "How many listings do I have right now?" and Claude responding with a real number pulled from the connected website]

### Step 5: You're Connected—Try Something Real {#step-5}

Now ask Claude something you'd actually use it for. Marcus, a commercial real estate agent, connected his site and immediately asked: "What properties have I listed in the downtown corridor in the last 30 days?" Claude pulled the data, filtered it, and had the answer ready in one message. That's the moment you'll know it's working.

Try asking Claude things like:
- "Who's the listing agent for 456 Oak Avenue?"
- "Can you write a description for my newest listing?"
- "What properties closed last week?"
- "Show me all open houses this weekend."

Each question shows Claude reaching into your website, reading real data, and answering based on what it finds.

## Troubleshooting: Quick Fixes {#troubleshooting}

**Claude says "Connection failed" or "Invalid key"**
Go back to your VR dashboard, make sure you copied the entire API key (it's usually a long string with no spaces at the end), and try pasting it again. If it still doesn't work, check that you're logged into the VR dashboard as an admin—some users can't generate new keys.

**Claude gives generic answers instead of website data**
The connection is probably live, but Claude doesn't have permission to read that specific data yet. This usually means a permission setting in your VR dashboard needs adjusting. Look for something like "Integrations" > "Permissions" and make sure external AI assistants have read access to at least "Listings" and "Blog Posts."

**I'm pasting the key but nothing happens**
Try refreshing the Claude website (Ctrl+R or Cmd+R) and returning to the Settings area where you found Integrations. Paste the key again. If that doesn't work, contact VR support with your API key in a secure message—they can diagnose it in seconds.

## What Comes Next {#next}

You now have Claude connected to your website—the foundation is built. The next articles in this series show you [how to connect other AI assistants](/connect-chatgpt-codex) if you prefer ChatGPT or Codex, and how to [set up team access safely](/team-rollout) so your whole office can ask questions without sharing passwords.

Want to see this working with real listings? **[See a demo](#).**

---

**← Previous:** [How to Create or Edit a Listing by Asking](/howto-listing)  
**Next →** [Connect ChatGPT and Codex to Your Website](/connect-chatgpt-codex)
