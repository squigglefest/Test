"""wikibuilder — an open-source static wiki builder.

Turn a directory of Markdown files into a self-contained, browsable static
wiki with navigation, ``[[wiki links]]``, backlinks, and client-side search.
"""

from .builder import BuildResult, Page, build
from .markdown import Document, render, slugify

__version__ = "0.1.0"

__all__ = [
    "build",
    "render",
    "slugify",
    "BuildResult",
    "Page",
    "Document",
    "__version__",
]
