"""HTML shell, stylesheet, and client-side search for the generated wiki.

Everything is inlined into each page so the output is a fully self-contained
static site with no external asset dependencies.
"""

from __future__ import annotations

import html

STYLESHEET = """
:root {
  --bg: #ffffff; --fg: #1f2328; --muted: #656d76; --border: #d0d7de;
  --link: #0969da; --sidebar-bg: #f6f8fa; --code-bg: #f6f8fa; --accent: #0969da;
  --sidebar-w: 17rem;
}
@media (prefers-color-scheme: dark) {
  :root {
    --bg: #0d1117; --fg: #e6edf3; --muted: #8b949e; --border: #30363d;
    --link: #4493f8; --sidebar-bg: #161b22; --code-bg: #161b22; --accent: #4493f8;
  }
}
* { box-sizing: border-box; }
body {
  margin: 0; background: var(--bg); color: var(--fg);
  font: 16px/1.6 -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
}
a { color: var(--link); text-decoration: none; }
a:hover { text-decoration: underline; }
.layout { display: flex; min-height: 100vh; }
.sidebar {
  width: var(--sidebar-w); flex: 0 0 var(--sidebar-w); background: var(--sidebar-bg);
  border-right: 1px solid var(--border); padding: 1.25rem 1rem; overflow-y: auto;
  position: sticky; top: 0; height: 100vh;
}
.sidebar h1 { font-size: 1.1rem; margin: 0 0 1rem; }
.sidebar h1 a { color: var(--fg); }
.search-box {
  width: 100%; padding: .5rem .65rem; margin-bottom: 1rem; border-radius: 6px;
  border: 1px solid var(--border); background: var(--bg); color: var(--fg); font-size: .9rem;
}
.nav { list-style: none; margin: 0; padding: 0; }
.nav li { margin: .15rem 0; }
.nav a { display: block; padding: .3rem .5rem; border-radius: 6px; color: var(--fg); font-size: .92rem; }
.nav a:hover { background: rgba(127,127,127,.12); text-decoration: none; }
.nav a.active { background: var(--accent); color: #fff; }
.nav a.active:hover { background: var(--accent); }
#search-results { list-style: none; margin: 0 0 1rem; padding: 0; }
#search-results li { margin: .3rem 0; }
#search-results .snippet { color: var(--muted); font-size: .8rem; display: block; }
.content { flex: 1 1 auto; max-width: 52rem; padding: 2.5rem 3rem; min-width: 0; }
.content h1, .content h2, .content h3 { line-height: 1.25; margin-top: 1.75rem; }
.content h1 { font-size: 2rem; border-bottom: 1px solid var(--border); padding-bottom: .3rem; }
.content h2 { font-size: 1.5rem; border-bottom: 1px solid var(--border); padding-bottom: .3rem; }
.content img { max-width: 100%; }
.content pre {
  background: var(--code-bg); border: 1px solid var(--border); border-radius: 6px;
  padding: 1rem; overflow-x: auto; font-size: .875rem;
}
.content code {
  background: var(--code-bg); border-radius: 4px; padding: .15em .35em;
  font-size: .875em; font-family: ui-monospace, SFMono-Regular, Menlo, monospace;
}
.content pre code { background: none; padding: 0; }
.content blockquote {
  margin: 1rem 0; padding: .25rem 1rem; color: var(--muted);
  border-left: .25rem solid var(--border);
}
.content table { border-collapse: collapse; }
.content a.wikilink.broken { color: #cf222e; border-bottom: 1px dotted #cf222e; }
.footer { margin-top: 3rem; padding-top: 1rem; border-top: 1px solid var(--border);
  color: var(--muted); font-size: .85rem; }
.backlinks { margin-top: 2.5rem; padding-top: 1rem; border-top: 1px solid var(--border); }
.backlinks h3 { margin: 0 0 .5rem; font-size: .95rem; color: var(--muted); }
.menu-toggle { display: none; }
@media (max-width: 800px) {
  .layout { flex-direction: column; }
  .sidebar { width: 100%; height: auto; position: static; border-right: none;
    border-bottom: 1px solid var(--border); }
  .content { padding: 1.5rem 1.25rem; }
}
"""

SEARCH_JS = """
(function () {
  var index = window.__WIKI_INDEX__ || [];
  var box = document.getElementById('search');
  var results = document.getElementById('search-results');
  var nav = document.getElementById('nav');
  if (!box || !results) return;
  function esc(s){ return s.replace(/[&<>]/g, function(c){
    return {'&':'&amp;','<':'&lt;','>':'&gt;'}[c]; }); }
  box.addEventListener('input', function () {
    var q = box.value.trim().toLowerCase();
    if (!q) { results.innerHTML = ''; if (nav) nav.style.display = ''; return; }
    if (nav) nav.style.display = 'none';
    var hits = [];
    for (var i = 0; i < index.length; i++) {
      var p = index[i];
      var hay = (p.title + ' ' + p.text).toLowerCase();
      var pos = hay.indexOf(q);
      if (pos === -1) continue;
      var score = (p.title.toLowerCase().indexOf(q) !== -1) ? 0 : 1;
      var start = Math.max(0, pos - 30);
      var snip = p.text.substr(start, 90);
      hits.push({ p: p, score: score, snip: snip });
    }
    hits.sort(function (a, b) { return a.score - b.score; });
    if (!hits.length) { results.innerHTML = '<li class="snippet">No matches.</li>'; return; }
    results.innerHTML = hits.slice(0, 20).map(function (h) {
      return '<li><a href="' + h.p.url + '">' + esc(h.p.title) + '</a>' +
        '<span class="snippet">' + esc(h.snip) + '…</span></li>';
    }).join('');
  });
})();
"""


def page(
    *,
    title: str,
    site_name: str,
    body: str,
    nav_html: str,
    active_url: str,
    index_json: str,
    footer: str,
) -> str:
    """Assemble a complete HTML page."""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)} · {html.escape(site_name)}</title>
<style>{STYLESHEET}</style>
</head>
<body>
<div class="layout">
<aside class="sidebar">
  <h1><a href="index.html">{html.escape(site_name)}</a></h1>
  <input id="search" class="search-box" type="search" placeholder="Search…" autocomplete="off">
  <ul id="search-results"></ul>
  <ul id="nav" class="nav">{nav_html}</ul>
</aside>
<main class="content">
{body}
<div class="footer">{footer}</div>
</main>
</div>
<script>window.__WIKI_INDEX__ = {index_json};</script>
<script>{SEARCH_JS}</script>
</body>
</html>
"""
