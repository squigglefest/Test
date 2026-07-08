# wikibuilder

An open-source, **zero-dependency** static wiki builder. Point it at a folder of
Markdown files and it produces a self-contained, browsable wiki — with
navigation, `[[wiki links]]`, automatic backlinks, and client-side full-text
search — that you can host anywhere.

No database. No accounts. No `pip install` of anything. Just Python 3.9+.

## Quick start

```bash
# Build the demo wiki that ships in ./content
python -m wikibuilder build content -o site -n "My Wiki"

# ...or build and preview it in one step
python -m wikibuilder serve content -n "My Wiki"
# then open http://localhost:8000
```

Deploy the generated `site/` directory to GitHub Pages, Netlify, S3, or any
plain web server.

## How it works

1. Every `*.md` / `*.markdown` file under your content directory becomes a page.
2. `index.md` becomes the landing page (`index.html`).
3. Non-Markdown files (images, downloads) are copied through as assets.

### Writing pages

Standard Markdown — headings, bold/italic, inline & fenced code, lists,
blockquotes, links, and images — plus one wiki extension:

| Syntax | Result |
|--------|--------|
| `[[Page Title]]` | Link to the page titled "Page Title" |
| `[[slug\|Displayed text]]` | Link to `slug`, showing custom text |

Links to pages that don't exist are rendered in red and reported at build time,
so broken links are easy to catch. Each page also shows a **Linked from**
section listing every page that links to it.

See the [`content/`](content/) folder for a worked example (it's the demo wiki).

## CLI

```
python -m wikibuilder build [CONTENT_DIR] [-o OUTPUT_DIR] [-n SITE_NAME]
python -m wikibuilder serve [CONTENT_DIR] [-o OUTPUT_DIR] [-n SITE_NAME] [-p PORT]
```

Defaults: content dir `./content`, output `./site`, name `Wiki`, port `8000`.

## Using it as a library

```python
from pathlib import Path
from wikibuilder import build

result = build(Path("content"), Path("site"), site_name="My Wiki")
print(f"{len(result.pages)} pages, {len(result.broken_links)} broken links")
```

## Development

```bash
python -m unittest discover -s tests   # run the test suite
```

## License

[MIT](LICENSE).
