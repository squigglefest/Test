# About

**wikibuilder** is a tiny, open-source static wiki generator. It exists to make
a personal or team knowledge base as easy as writing Markdown files in a folder.

## Design goals

- **Zero dependencies.** It runs on a stock Python install. Nothing to
  `pip install`, nothing to keep updated.
- **Self-contained output.** Each generated page inlines its own CSS and
  search index, so the `site/` folder works from any static host — or even
  straight off your filesystem.
- **Wiki-first.** `[[wiki links]]`, backlinks, and search are built in rather
  than bolted on.

## What it is not

It is deliberately *not* a full CMS. There's no database, no accounts, and no
live editing — you edit Markdown and rebuild. If you need collaborative,
in-browser editing, a hosted wiki engine will serve you better.

## License

Released under the [MIT license](https://opensource.org/license/mit). Use it,
fork it, ship it.

Back to the [[Welcome]] page.
