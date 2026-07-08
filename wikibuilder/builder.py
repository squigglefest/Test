"""Build a browsable static wiki from a directory of Markdown files."""

from __future__ import annotations

import html
import json
import re
import shutil
from dataclasses import dataclass, field
from pathlib import Path

from . import theme
from .markdown import Document, slugify

MARKDOWN_SUFFIXES = {".md", ".markdown"}


@dataclass
class Page:
    slug: str
    title: str
    source_path: Path
    document: Document
    url: str = ""
    backlinks: list[tuple[str, str]] = field(default_factory=list)  # (title, url)


@dataclass
class BuildResult:
    pages: list[Page]
    broken_links: list[tuple[str, str]]  # (source page slug, missing target slug)
    output_dir: Path


def _title_from_source(path: Path, doc: Document) -> str:
    if doc.title:
        return doc.title
    # Fall back to the file name, turned into Title Case.
    stem = path.stem.replace("-", " ").replace("_", " ").strip()
    return stem[:1].upper() + stem[1:] if stem else "Untitled"


def _collect_sources(content_dir: Path) -> list[Path]:
    return sorted(
        p
        for p in content_dir.rglob("*")
        if p.is_file() and p.suffix.lower() in MARKDOWN_SUFFIXES
    )


def build(content_dir: Path, output_dir: Path, site_name: str = "Wiki") -> BuildResult:
    """Render every Markdown file under *content_dir* into *output_dir*."""
    from .markdown import Parser

    content_dir = Path(content_dir)
    output_dir = Path(output_dir)
    if not content_dir.is_dir():
        raise FileNotFoundError(f"content directory not found: {content_dir}")

    parser = Parser()
    pages: list[Page] = []
    by_slug: dict[str, Page] = {}

    for source in _collect_sources(content_dir):
        text = source.read_text(encoding="utf-8")
        doc = parser.parse(text)
        title = _title_from_source(source, doc)
        # index.md keeps its slug so it becomes the landing page.
        slug = "index" if source.stem.lower() == "index" else slugify(title)
        # Guard against collisions.
        base, n = slug, 2
        while slug in by_slug:
            slug = f"{base}-{n}"
            n += 1
        page = Page(slug=slug, title=title, source_path=source, document=doc, url=f"{slug}.html")
        pages.append(page)
        by_slug[slug] = page

    # Build a resolver that maps both a page's own slug and the slug of its
    # title to the page. This lets `[[Home]]` find index.md even though its
    # file slug is forced to "index". A page's own slug always wins.
    resolve: dict[str, Page] = {}
    for page in pages:
        resolve.setdefault(slugify(page.title), page)
    for page in pages:  # own slugs take precedence over title aliases
        resolve[page.slug] = page

    # Resolve backlinks and detect broken wiki links.
    broken: list[tuple[str, str]] = []
    for page in pages:
        for label, target_slug in page.document.wiki_links:
            target = resolve.get(target_slug)
            if target is None:
                broken.append((page.slug, target_slug))
            elif target is not page:
                if (page.title, page.url) not in target.backlinks:
                    target.backlinks.append((page.title, page.url))

    # Sort nav: index first, then alphabetical by title.
    nav_pages = sorted(pages, key=lambda p: (p.slug != "index", p.title.lower()))

    # Build the search index.
    index = [
        {"title": p.title, "url": p.url, "text": p.document.text[:2000]}
        for p in pages
    ]
    index_json = json.dumps(index, ensure_ascii=False)

    output_dir.mkdir(parents=True, exist_ok=True)

    for page in pages:
        nav_html = _render_nav(nav_pages, active_slug=page.slug)
        body = _finalize_body(page, resolve)
        footer = f"Built with wikibuilder · {len(pages)} pages"
        page_html = theme.page(
            title=page.title,
            site_name=site_name,
            body=body,
            nav_html=nav_html,
            active_url=page.url,
            index_json=index_json,
            footer=footer,
        )
        (output_dir / page.url).write_text(page_html, encoding="utf-8")

    # Copy any non-Markdown assets (images, etc.) alongside the pages,
    # preserving relative layout.
    for asset in content_dir.rglob("*"):
        if asset.is_file() and asset.suffix.lower() not in MARKDOWN_SUFFIXES:
            dest = output_dir / asset.relative_to(content_dir)
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(asset, dest)

    return BuildResult(pages=pages, broken_links=broken, output_dir=output_dir)


def _render_nav(nav_pages: list[Page], active_slug: str) -> str:
    items = []
    for p in nav_pages:
        cls = ' class="active"' if p.slug == active_slug else ""
        items.append(f'<li><a href="{p.url}"{cls}>{html.escape(p.title)}</a></li>')
    return "".join(items)


_WIKILINK_TAG = re.compile(r'<a class="wikilink" href="([^"]+)\.html">')


def _finalize_body(page: Page, resolve: dict[str, "Page"]) -> str:
    body = page.document.html

    # Rewrite each wiki link to its resolved target URL, or mark it broken.
    def mark(match: re.Match) -> str:
        slug = match.group(1)
        target = resolve.get(slug)
        if target is not None:
            return f'<a class="wikilink" href="{target.url}">'
        return f'<a class="wikilink broken" title="Missing page: {html.escape(slug)}" href="{slug}.html">'

    body = _WIKILINK_TAG.sub(mark, body)

    if page.backlinks:
        links = "".join(
            f'<li><a href="{url}">{html.escape(title)}</a></li>'
            for title, url in sorted(page.backlinks)
        )
        body += (
            '<div class="backlinks"><h3>Linked from</h3>'
            f"<ul>{links}</ul></div>"
        )
    return body
