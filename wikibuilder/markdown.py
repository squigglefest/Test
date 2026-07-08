"""A small, dependency-free Markdown-to-HTML converter.

This is intentionally compact rather than CommonMark-complete. It covers the
subset a wiki needs: headings, paragraphs, bold/italic, inline & fenced code,
lists, blockquotes, links, images, horizontal rules, and ``[[wiki links]]``.

The wiki-link syntax is the one wiki-specific extension:

    [[Page Title]]            -> link to the page whose title is "Page Title"
    [[slug|Displayed text]]   -> link to page "slug", showing "Displayed text"

Wiki links are emitted as ``<a class="wikilink" href="SLUG.html">``. The
builder rewrites/validates these afterwards, so the parser only needs to
produce a slug and a label.
"""

from __future__ import annotations

import html
import re
from dataclasses import dataclass, field
from typing import Callable


def slugify(text: str) -> str:
    """Turn a heading or title into a URL-safe slug."""
    text = text.strip().lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    return text.strip("-") or "untitled"


@dataclass
class Document:
    """The result of rendering one Markdown file."""

    html: str
    title: str
    # (label, slug) for every wiki link encountered, so the builder can
    # report broken links.
    wiki_links: list[tuple[str, str]] = field(default_factory=list)
    # Plain text with markup stripped, for the search index.
    text: str = ""


# --- inline parsing --------------------------------------------------------

_INLINE_CODE = re.compile(r"`([^`]+)`")
_IMAGE = re.compile(r"!\[([^\]]*)\]\(([^)\s]+)(?:\s+\"([^\"]*)\")?\)")
_LINK = re.compile(r"\[([^\]]+)\]\(([^)\s]+)(?:\s+\"([^\"]*)\")?\)")
_WIKILINK = re.compile(r"\[\[([^\]]+)\]\]")
_BOLD = re.compile(r"\*\*([^*]+)\*\*|__([^_]+)__")
_ITALIC = re.compile(r"(?<!\*)\*(?!\*)([^*]+)\*(?!\*)|(?<!_)_(?!_)([^_]+)_(?!_)")


class _InlineRenderer:
    """Renders inline spans, protecting code spans from further formatting."""

    def __init__(self, on_wikilink: Callable[[str, str], None]):
        self._on_wikilink = on_wikilink

    def render(self, text: str) -> str:
        # Protect inline code first so its contents are never reformatted.
        placeholders: list[str] = []

        def stash(match: re.Match) -> str:
            placeholders.append("<code>" + html.escape(match.group(1)) + "</code>")
            return f"\x00{len(placeholders) - 1}\x00"

        text = _INLINE_CODE.sub(stash, text)
        text = html.escape(text, quote=False)

        text = _IMAGE.sub(self._image, text)
        text = _WIKILINK.sub(self._wikilink, text)
        text = _LINK.sub(self._link, text)
        text = _BOLD.sub(lambda m: f"<strong>{m.group(1) or m.group(2)}</strong>", text)
        text = _ITALIC.sub(
            lambda m: f"<em>{m.group(1) if m.group(1) is not None else m.group(2)}</em>",
            text,
        )

        # Restore code spans.
        def unstash(match: re.Match) -> str:
            return placeholders[int(match.group(1))]

        return re.sub(r"\x00(\d+)\x00", unstash, text)

    def _image(self, match: re.Match) -> str:
        alt, src, title = match.group(1), match.group(2), match.group(3)
        title_attr = f' title="{html.escape(title, quote=True)}"' if title else ""
        return f'<img src="{html.escape(src, quote=True)}" alt="{html.escape(alt, quote=True)}"{title_attr}>'

    def _link(self, match: re.Match) -> str:
        label, href, title = match.group(1), match.group(2), match.group(3)
        title_attr = f' title="{html.escape(title, quote=True)}"' if title else ""
        external = href.startswith(("http://", "https://", "//"))
        rel = ' rel="noopener noreferrer" target="_blank"' if external else ""
        return f'<a href="{html.escape(href, quote=True)}"{title_attr}{rel}>{label}</a>'

    def _wikilink(self, match: re.Match) -> str:
        inner = match.group(1)
        if "|" in inner:
            target, label = inner.split("|", 1)
        else:
            target = label = inner
        slug = slugify(target)
        self._on_wikilink(label.strip(), slug)
        return f'<a class="wikilink" href="{slug}.html">{label.strip()}</a>'


# --- block parsing ---------------------------------------------------------

_HEADING = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")
_FENCE = re.compile(r"^(```|~~~)\s*([\w+-]*)\s*$")
_HR = re.compile(r"^ {0,3}([-*_])( *\1){2,} *$")
_UL = re.compile(r"^\s*[-*+]\s+(.*)$")
_OL = re.compile(r"^\s*\d+[.)]\s+(.*)$")
_QUOTE = re.compile(r"^ {0,3}>\s?(.*)$")


class Parser:
    def __init__(self) -> None:
        self._wiki_links: list[tuple[str, str]] = []
        self._inline = _InlineRenderer(self._record_wikilink)

    def _record_wikilink(self, label: str, slug: str) -> None:
        self._wiki_links.append((label, slug))

    def parse(self, source: str) -> Document:
        self._wiki_links = []
        lines = source.replace("\r\n", "\n").replace("\r", "\n").split("\n")
        out: list[str] = []
        title = ""
        i = 0
        n = len(lines)

        while i < n:
            line = lines[i]

            # Fenced code block.
            fence = _FENCE.match(line)
            if fence:
                marker, lang = fence.group(1), fence.group(2)
                body: list[str] = []
                i += 1
                while i < n and lines[i].strip() != marker:
                    body.append(lines[i])
                    i += 1
                i += 1  # consume closing fence (or EOF)
                cls = f' class="language-{lang}"' if lang else ""
                code = html.escape("\n".join(body))
                out.append(f"<pre><code{cls}>{code}</code></pre>")
                continue

            # Blank line.
            if not line.strip():
                i += 1
                continue

            # Heading.
            heading = _HEADING.match(line)
            if heading:
                level = len(heading.group(1))
                text = heading.group(2).strip()
                if not title and level == 1:
                    title = _strip_inline(text)
                anchor = slugify(text)
                out.append(
                    f'<h{level} id="{anchor}">{self._inline.render(text)}</h{level}>'
                )
                i += 1
                continue

            # Horizontal rule.
            if _HR.match(line):
                out.append("<hr>")
                i += 1
                continue

            # Blockquote.
            if _QUOTE.match(line):
                quoted: list[str] = []
                while i < n and _QUOTE.match(lines[i]):
                    quoted.append(_QUOTE.match(lines[i]).group(1))
                    i += 1
                inner = self._inline.render(" ".join(quoted))
                out.append(f"<blockquote><p>{inner}</p></blockquote>")
                continue

            # Lists.
            if _UL.match(line) or _OL.match(line):
                ordered = bool(_OL.match(line))
                pattern = _OL if ordered else _UL
                items: list[str] = []
                while i < n and pattern.match(lines[i]):
                    items.append(pattern.match(lines[i]).group(1))
                    i += 1
                tag = "ol" if ordered else "ul"
                rendered = "".join(
                    f"<li>{self._inline.render(item)}</li>" for item in items
                )
                out.append(f"<{tag}>{rendered}</{tag}>")
                continue

            # Paragraph: gather consecutive non-blank, non-block lines.
            para: list[str] = []
            while i < n and lines[i].strip() and not _is_block_start(lines[i]):
                para.append(lines[i].strip())
                i += 1
            out.append(f"<p>{self._inline.render(' '.join(para))}</p>")

        rendered = "\n".join(out)
        return Document(
            html=rendered,
            title=title,
            wiki_links=list(self._wiki_links),
            text=_html_to_text(rendered),
        )


def _is_block_start(line: str) -> bool:
    return bool(
        _HEADING.match(line)
        or _FENCE.match(line)
        or _HR.match(line)
        or _UL.match(line)
        or _OL.match(line)
        or _QUOTE.match(line)
    )


_TAG = re.compile(r"<[^>]+>")


def _strip_inline(text: str) -> str:
    text = _WIKILINK.sub(lambda m: m.group(1).split("|")[-1], text)
    text = _LINK.sub(lambda m: m.group(1), text)
    text = re.sub(r"[*_`#]", "", text)
    return text.strip()


def _html_to_text(rendered: str) -> str:
    text = _TAG.sub(" ", rendered)
    text = html.unescape(text)
    return re.sub(r"\s+", " ", text).strip()


def render(source: str) -> Document:
    """Convenience: render a Markdown string to a :class:`Document`."""
    return Parser().parse(source)
