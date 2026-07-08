# Syntax

wikibuilder understands a practical subset of Markdown plus one extension for
linking between pages.

## Text formatting

You can write **bold**, *italic*, and `inline code`. Combine them freely.

> Blockquotes are supported too — handy for callouts and citations.

## Headings

Use `#` through `######` for headings. Every heading gets an `id`, so you can
deep-link to a section.

## Lists

Unordered:

- First item
- Second item
- Third item

Ordered:

1. Step one
2. Step two
3. Step three

## Code blocks

Fenced code blocks keep their language hint:

```python
def greet(name):
    return f"Hello, {name}!"
```

## Links

Regular [external links](https://example.com) open in a new tab. Internal
**wiki links** use double brackets:

- `[[Getting Started]]` links to the page titled "Getting Started".
- `[[getting-started|the setup guide]]` links to the same page but shows custom
  text: [[getting-started|the setup guide]].

Every page automatically lists which other pages link to it under **Linked
from**. Try it — this page is referenced from [[Welcome]] and
[[Getting Started]].
