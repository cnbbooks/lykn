#!/usr/bin/env python3
"""
mdbook-epub-image-paths — mdbook preprocessor that rewrites relative image
paths so they resolve correctly under mdbook-epub.

Background:
  mdbook-epub (v0.5.2, confirmed from source) resolves image paths as
  'root + src + path' rather than relative to the containing markdown file.
  This means '../../images/foo.png' from src/a/b/c.md resolves to
  root/images/foo.png (one level above src/), which doesn't exist.

  mdbook's HTML renderer correctly resolves the same reference as
  src/images/foo.png, so we can't just edit the source.

Fix:
  This preprocessor walks the book in memory, computes what each relative
  image path SHOULD resolve to from mdbook-epub's perspective, and rewrites
  the chapter content with a path that works. Source files are untouched.

  For chapter at src/a/b/c.md referencing '../../images/foo.png':
    mdbook HTML resolves: src/a/b/../../images/foo.png -> src/images/foo.png OK
    We need mdbook-epub to see: images/foo.png
    Because it does: src + images/foo.png -> src/images/foo.png OK

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
    Given a chapter's path (relative to src/, e.g. 'a/b/c.md') and a
    reference path from that chapter (e.g. '../../images/foo.png'),
    return the path form that mdbook-epub needs.

    Strategy: figure out what src-relative path this reference actually
    points to (same calculation mdbook's HTML renderer does), then return
    that src-relative path. mdbook-epub joins 'root + src + path', so a
    src-relative path resolves correctly.
    """
    # Use PurePosixPath for cross-platform consistency (book paths are posix).
    chapter_dir = PurePosixPath(chapter_path).parent

    # os.path.normpath handles ../ collapsing. We keep this as a string
    # operation because PurePosixPath doesn't collapse .. in the middle
    # of a path (it's lexical, not filesystem-aware, but it also doesn't
    # resolve up-navigation).
    joined = str(chapter_dir / ref_path) if str(chapter_dir) != '.' else ref_path
    normalized = os.path.normpath(joined).replace('\\', '/')

    # If normpath collapsed to something beginning with ../ it means the
    # reference escapes src/ entirely — that's a broken link, not something
    # we can fix. Return unchanged so the error surfaces meaningfully.
    if normalized.startswith('../'):
        return ref_path

    # Strip a leading "./" if present (cosmetic).
    if normalized.startswith('./'):
        normalized = normalized[2:]

    return normalized


def rewrite_content(chapter_path: str, content: str) -> str:
    """
    Rewrite all image references in the chapter content so paths are
    src-relative rather than file-relative.
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
    mdbook book JSON shape:
      { "sections": [ {"Chapter": {...}}, {"Separator": null}, ... ] }
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
    sections = book.get('sections', [])
    walk_items(sections)

    json.dump(book, sys.stdout)
    return 0


def run_supports_check(renderer: str) -> int:
    """
    mdbook asks 'supports <renderer>?' to decide whether to invoke us.
    We support only epub — HTML and other renderers don't need this fix
    (and running it on HTML would actively break things by rewriting paths
    that the HTML renderer depends on being file-relative).
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
