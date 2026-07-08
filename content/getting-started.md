# Getting Started

Building a wiki takes three steps.

## 1. Write some pages

Create a `content/` directory and drop in Markdown files. Each file becomes a
page. The file called `index.md` becomes the landing page.

```
content/
├── index.md
├── getting-started.md
└── syntax.md
```

## 2. Build the site

Run the builder against your content directory:

```bash
python -m wikibuilder build content -o site -n "My Wiki"
```

This writes a fully self-contained static site into `site/`.

## 3. Preview it

Serve it locally to click around:

```bash
python -m wikibuilder serve content -n "My Wiki"
```

Then open <http://localhost:8000>.

That's it — deploy the `site/` folder to any static host (GitHub Pages,
Netlify, an S3 bucket, or a plain web server).

See [[Syntax]] for what you can put in a page, or head back to the [[Welcome]]
page.
