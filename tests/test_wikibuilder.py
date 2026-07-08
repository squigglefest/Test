"""Tests for wikibuilder. Run with: python -m pytest  (or python -m unittest)."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from wikibuilder import build, render, slugify  # noqa: E402


class SlugifyTests(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(slugify("Getting Started"), "getting-started")

    def test_punctuation_and_case(self):
        self.assertEqual(slugify("What's New?!"), "whats-new")

    def test_empty_falls_back(self):
        self.assertEqual(slugify("   "), "untitled")


class MarkdownTests(unittest.TestCase):
    def test_heading_and_title(self):
        doc = render("# Hello World\n\nsome text")
        self.assertEqual(doc.title, "Hello World")
        self.assertIn('<h1 id="hello-world">Hello World</h1>', doc.html)

    def test_inline_formatting(self):
        doc = render("This is **bold** and *italic* and `code`.")
        self.assertIn("<strong>bold</strong>", doc.html)
        self.assertIn("<em>italic</em>", doc.html)
        self.assertIn("<code>code</code>", doc.html)

    def test_code_block_is_escaped(self):
        doc = render("```python\nprint('<hi>')\n```")
        self.assertIn("<pre><code", doc.html)
        self.assertIn("&lt;hi&gt;", doc.html)
        # Content inside a code fence must not be turned into tags.
        self.assertNotIn("<hi>", doc.html)

    def test_lists(self):
        doc = render("- a\n- b\n- c")
        self.assertIn("<ul><li>a</li><li>b</li><li>c</li></ul>", doc.html)
        doc2 = render("1. one\n2. two")
        self.assertIn("<ol><li>one</li><li>two</li></ol>", doc2.html)

    def test_wiki_link_plain(self):
        doc = render("See [[Getting Started]].")
        self.assertIn('href="getting-started.html"', doc.html)
        self.assertEqual(doc.wiki_links, [("Getting Started", "getting-started")])

    def test_wiki_link_with_label(self):
        doc = render("See [[getting-started|the guide]].")
        self.assertIn(">the guide</a>", doc.html)
        self.assertEqual(doc.wiki_links[0][1], "getting-started")

    def test_external_link_opens_new_tab(self):
        doc = render("[site](https://example.com)")
        self.assertIn('target="_blank"', doc.html)

    def test_html_is_escaped(self):
        doc = render("A <script>alert(1)</script> tag")
        self.assertNotIn("<script>", doc.html)
        self.assertIn("&lt;script&gt;", doc.html)

    def test_search_text_strips_markup(self):
        doc = render("# Title\n\nHello **world**")
        self.assertIn("Hello world", doc.text)
        self.assertNotIn("<", doc.text)


class BuildTests(unittest.TestCase):
    def _write(self, root: Path, name: str, text: str) -> None:
        (root / name).write_text(text, encoding="utf-8")

    def test_build_produces_pages_and_backlinks(self):
        import tempfile

        with tempfile.TemporaryDirectory() as tmp:
            content = Path(tmp) / "content"
            content.mkdir()
            out = Path(tmp) / "site"
            self._write(content, "index.md", "# Home\n\nGo to [[Guide]].")
            self._write(content, "guide.md", "# Guide\n\nBack [[Home]].")

            result = build(content, out, site_name="Test Wiki")

            self.assertTrue((out / "index.html").exists())
            self.assertTrue((out / "guide.html").exists())
            self.assertEqual(result.broken_links, [])

            index_html = (out / "index.html").read_text(encoding="utf-8")
            self.assertIn("Test Wiki", index_html)
            self.assertIn('href="guide.html"', index_html)
            # Backlink from guide -> home should appear on the home page.
            self.assertIn("Linked from", index_html)

    def test_broken_link_is_reported(self):
        import tempfile

        with tempfile.TemporaryDirectory() as tmp:
            content = Path(tmp) / "content"
            content.mkdir()
            out = Path(tmp) / "site"
            self._write(content, "index.md", "# Home\n\nSee [[Nonexistent]].")

            result = build(content, out)
            self.assertEqual(len(result.broken_links), 1)
            self.assertEqual(result.broken_links[0][1], "nonexistent")
            html = (out / "index.html").read_text(encoding="utf-8")
            self.assertIn("wikilink broken", html)

    def test_assets_are_copied(self):
        import tempfile

        with tempfile.TemporaryDirectory() as tmp:
            content = Path(tmp) / "content"
            content.mkdir()
            out = Path(tmp) / "site"
            self._write(content, "index.md", "# Home")
            (content / "logo.png").write_bytes(b"\x89PNG fake")

            build(content, out)
            self.assertTrue((out / "logo.png").exists())


if __name__ == "__main__":
    unittest.main()
