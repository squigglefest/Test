"""Command-line interface for wikibuilder.

Usage:
    python -m wikibuilder build [CONTENT_DIR] [-o OUTPUT_DIR] [-n SITE_NAME]
    python -m wikibuilder serve [CONTENT_DIR] [-o OUTPUT_DIR] [-n NAME] [-p PORT]
"""

from __future__ import annotations

import argparse
import functools
import http.server
import socketserver
import sys
from pathlib import Path

from . import __version__, build


def _add_common(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        "content", nargs="?", default="content",
        help="directory containing Markdown files (default: ./content)",
    )
    parser.add_argument(
        "-o", "--output", default="site",
        help="output directory for the generated site (default: ./site)",
    )
    parser.add_argument(
        "-n", "--name", default="Wiki", help="site name shown in the header",
    )


def _do_build(content: str, output: str, name: str) -> int:
    result = build(Path(content), Path(output), site_name=name)
    print(f"Built {len(result.pages)} page(s) -> {result.output_dir}")
    if result.broken_links:
        print(f"\n{len(result.broken_links)} broken wiki link(s):", file=sys.stderr)
        for src, target in result.broken_links:
            print(f"  {src}.html -> [[{target}]] (missing)", file=sys.stderr)
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="wikibuilder",
        description="Build a static wiki from Markdown files.",
    )
    parser.add_argument("--version", action="version", version=f"wikibuilder {__version__}")
    sub = parser.add_subparsers(dest="command", required=True)

    build_p = sub.add_parser("build", help="build the wiki once")
    _add_common(build_p)

    serve_p = sub.add_parser("serve", help="build then serve locally")
    _add_common(serve_p)
    serve_p.add_argument("-p", "--port", type=int, default=8000, help="port (default: 8000)")

    args = parser.parse_args(argv)

    try:
        rc = _do_build(args.content, args.output, args.name)
    except FileNotFoundError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    if rc != 0 or args.command == "build":
        return rc

    # serve
    directory = str(Path(args.output).resolve())
    handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=directory)
    with socketserver.TCPServer(("", args.port), handler) as httpd:
        print(f"Serving {directory} at http://localhost:{args.port} (Ctrl+C to stop)")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nStopped.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
