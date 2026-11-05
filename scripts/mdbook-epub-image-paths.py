#!/usr/bin/env python3
"""
EPUB-only image policy: reuse the small cover rather than linking to the
full-resolution web cover. Preserve other chapter-relative paths; the EPUB
renderer already resolves them relative to their source chapters. Source
files and HTML output stay untouched.

Configuration (in book.toml):

    [preprocessor.epub-image-paths]
    command = "python3 scripts/mdbook-epub-image-paths.py"
    renderers = ["epub"]            # only runs for EPUB builds

mdbook invokes this script twice per build:
  1. With argv: "supports" "<renderer-name>"  -> exit 0 if supported, 1 otherwise
  2. With no argv, JSON on stdin: [context, book] -> write modified book on stdout

See: https://rust-lang.github.io/mdBook/for_developers/preprocessors.html
"""

import json
import os
import re
import sys
from pathlib import PurePosixPath


# Markdown image: ![alt](path)  or  ![alt](path "title")
MD_IMAGE_RE = re.compile(
    r'(!\[[^\]]*\]\()'
    r'([^)\s#?]+?)'
    r'(\s+"[^"]*"|\s+\'[^\']*\')?'
    r'(\))'
)

# Reference-style link/image definition: [id]: url  or  [id]: url "title"
REF_DEF_RE = re.compile(
    r'(^\[[^\]]+\]:\s+)'
    r'([^\s#?]+?)'
    r'(\s+"[^"]*"|\s+\'[^\']*\')?'
    r'(\s*)$',
    re.MULTILINE,
)

# HTML img tag: <img ... src="path" ...>
HTML_IMG_RE = re.compile(
    r'(<img\s+[^>]*?src\s*=\s*["\'])'
    r'([^"\']+?)'
    r'(["\'])'
)


def is_rewritable(path: str) -> bool:
    """
    Return True if this path is a local file reference we should rewrite.
    Skip URLs, absolute paths, and fragment/protocol references.
    """
    if not path:
        return False
    if path.startswith(('http://', 'https://', '//')):
        return False
    if path.startswith(('mailto:', 'tel:', '#', 'data:', 'file:')):
        return False
    if path.startswith('/'):
        # Already an absolute-from-root path. mdbook-epub may or may not
        # handle these; leave alone. They work in HTML regardless.
        return False
    return True


def normalize_for_epub(chapter_path: str, ref_path: str) -> str:
    """
    Substitute only the book's large cover, preserving chapter relativity.
    """
    chapter_dir = PurePosixPath(chapter_path).parent
    joined = str(chapter_dir / ref_path) if str(chapter_dir) != '.' else ref_path
    normalized = os.path.normpath(joined).replace('\\', '/')
    if normalized == 'images/cover-large.png':
        return str(PurePosixPath(ref_path).with_name('cover.png'))
    return ref_path


def rewrite_content(chapter_path: str, content: str) -> str:
    """
    Apply the EPUB cover exception to inline, reference, and HTML images.
    """
    def rewrite_md(m):
        prefix, path, title, suffix = m.groups()
        if not is_rewritable(path):
            return m.group(0)
        new_path = normalize_for_epub(chapter_path, path)
        return f'{prefix}{new_path}{title or ""}{suffix}'

    def rewrite_ref(m):
        prefix, path, title, trailing = m.groups()
        if not is_rewritable(path):
            return m.group(0)
        new_path = normalize_for_epub(chapter_path, path)
        return f'{prefix}{new_path}{title or ""}{trailing}'

    def rewrite_html(m):
        prefix, path, suffix = m.groups()
        if not is_rewritable(path):
            return m.group(0)
        new_path = normalize_for_epub(chapter_path, path)
        return f'{prefix}{new_path}{suffix}'

    content = MD_IMAGE_RE.sub(rewrite_md, content)
    content = REF_DEF_RE.sub(rewrite_ref, content)
    content = HTML_IMG_RE.sub(rewrite_html, content)
    return content


def walk_items(sections: list) -> None:
    """
    Recursively walk a book's section list, rewriting each Chapter's content.
    mdbook 0.5 book JSON shape (older versions use "sections" instead):
      { "items": [ {"Chapter": {...}}, {"Separator": null}, ... ] }
    A Chapter has: name, content, path, sub_items, ...
    """
    for section in sections:
        if not isinstance(section, dict):
            continue
        chapter = section.get('Chapter')
        if chapter is None:
            continue

        path = chapter.get('path')
        content = chapter.get('content')
        if path and content:
            chapter['content'] = rewrite_content(path, content)

        # Recurse into nested chapters.
        sub_items = chapter.get('sub_items')
        if sub_items:
            walk_items(sub_items)


def run_preprocessor() -> int:
    """Read book JSON on stdin, write modified book JSON on stdout."""
    try:
        payload = json.load(sys.stdin)
    except json.JSONDecodeError as e:
        print(f'epub-image-paths: invalid JSON on stdin: {e}', file=sys.stderr)
        return 1

    # mdbook sends [context, book]
    if not isinstance(payload, list) or len(payload) != 2:
        print(f'epub-image-paths: expected [context, book] array', file=sys.stderr)
        return 1

    _context, book = payload
    # mdBook 0.5 uses items; older versions use sections.
    sections = book.get('items', book.get('sections', []))
    walk_items(sections)

    json.dump(book, sys.stdout)
    return 0


def run_supports_check(renderer: str) -> int:
    """
    mdbook asks 'supports <renderer>?' to decide whether to invoke us.
    Support only EPUB; HTML retains its link to the full-resolution cover.
    """
    supported = renderer == 'epub'
    # Log to stderr — mdbook prints preprocessor stderr to the user's
    # terminal, so this shows up in the build output without interfering
    # with the JSON protocol on stdout.
    print(
        f'epub-image-paths: supports({renderer!r}) -> {supported}',
        file=sys.stderr,
    )
    return 0 if supported else 1


def main() -> int:
    argv = sys.argv[1:]
    if len(argv) == 2 and argv[0] == 'supports':
        return run_supports_check(argv[1])
    if not argv:
        print('epub-image-paths: running preprocessor pass', file=sys.stderr)
        return run_preprocessor()

    print(f'epub-image-paths: unexpected arguments: {argv}', file=sys.stderr)
    return 1


if __name__ == '__main__':
    sys.exit(main())
