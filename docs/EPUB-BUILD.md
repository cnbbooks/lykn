# Lykn EPUB build — the complete setup

This is the consolidated guide — supersedes the earlier `EPUB-BUILD.md`
and `FIX-IMAGE-PATHS.md` drafts.

## The file layout you're targeting

```
lykn/                              ← book root
├── book.toml                      ← updated config
├── css/
│   ├── custom.css                 ← existing, unchanged
│   └── epub.css                   ← NEW, palette-matched
├── scripts/
│   ├── fetch-fonts.sh             ← NEW, font downloader
│   └── mdbook-epub-image-paths.py ← NEW, path-fix preprocessor
├── theme/
│   └── fonts/                     ← NEW, populated by fetch-fonts.sh
│       ├── RedHatDisplay-*.ttf
│       ├── Literata-*.ttf
│       └── IBMPlexMono-*.ttf
├── .github/workflows/
│   └── publish.yml                ← updated
└── src/
    └── … (unchanged)
```

## One-time setup

```bash
cd ~/lab/cnbb/lykn

# 1. Install the EPUB backend (cargo-binstall is faster if you have it)
cargo install mdbook-epub

# 2. Place the new files
#    - book.toml                               (replaces existing)
#    - css/epub.css                            (new)
#    - scripts/fetch-fonts.sh                  (new)
#    - scripts/mdbook-epub-image-paths.py      (new)
#    - .github/workflows/publish.yml           (replaces existing)
mkdir -p scripts
chmod +x scripts/fetch-fonts.sh
chmod +x scripts/mdbook-epub-image-paths.py

# 3. Fetch the fonts
./scripts/fetch-fonts.sh

# 4. Verify the preprocessor responds correctly
python3 scripts/mdbook-epub-image-paths.py supports epub && echo OK
python3 scripts/mdbook-epub-image-paths.py supports html || echo "correctly declines"
```

## Local build

```bash
mdbook build
# Output: book/epub/Lykn.epub (plus book/html/ as before)
```

`mdbook serve` and `mdbook watch` for local preview continue to work
unchanged — the preprocessor only runs when EPUB is being rendered,
and `mdbook serve` only renders HTML.

## How the preprocessor works

`scripts/mdbook-epub-image-paths.py` is an mdbook preprocessor
(per the [preprocessor spec](https://rust-lang.github.io/mdBook/for_developers/preprocessors.html))
that gets invoked only during EPUB builds via the `renderers = ["epub"]`
hint in `book.toml`.

It reads the whole book from stdin as JSON, rewrites relative image
paths in each chapter's content to be src-rooted rather than
file-relative, and emits the modified book on stdout. Your source
markdown files are never touched.

For a chapter at `src/part0/chapter0/0-opening.md` containing
`![](../../images/ch0.png)`:

- HTML renderer: resolves relative to the chapter file → `src/images/ch0.png` ✓
- EPUB renderer: joins `root + src + path` → `root/images/ch0.png` ✗

The preprocessor rewrites the reference to `images/ch0.png` in the
content stream going to EPUB only. Then:

- EPUB renderer: joins `root + src + path` → `root/src/images/ch0.png` ✓

## Verification checklist

Before shipping to a user, spot-check these. The single most common
failure mode for mdbook-epub is a silent half-built EPUB with missing
fonts or images — the backend logs warnings but doesn't fail the build.

```bash
# 1. Build completed without errors in stdout
mdbook build 2>&1 | grep -iE 'error|warn' | head

# 2. Fonts packaged (expect 8)
unzip -l book/epub/Lykn.epub | grep -iE '\.ttf$' | wc -l

# 3. Stylesheet packaged
unzip -l book/epub/Lykn.epub | grep -i epub.css

# 4. Chapter images packaged (38 ch*.png + 13 dssrt*.png)
unzip -l book/epub/Lykn.epub | grep -iE 'ch[0-9]+\.png|dssrt[0-9]+\.png' | wc -l

# 5. Cover
unzip -l book/epub/Lykn.epub | grep -i cover

# 6. Overall size (expect 15–40 MB with all your images)
ls -lh book/epub/Lykn.epub
```

## Reader testing

Open the `.epub` in each of these to spot rendering issues:

- **Apple Books** (macOS/iOS) — drop onto the app icon. Treat as reference.
- **Thorium Reader** (free, all platforms, best standards conformance).
- **Calibre viewer** — quick checks; more forgiving than real readers.
- **Kindle** — convert with Calibre to `.azw3`. Expect some font fallback
  on older Kindles; layout should still work.

## Troubleshooting

### "Asset was not found" errors still appear

First, verify the preprocessor actually ran:

```bash
RUST_LOG=debug mdbook build 2>&1 | grep -i 'epub-image-paths\|preprocessor'
```

You should see a line indicating the preprocessor was invoked. If not,
check that `[preprocessor.epub-image-paths]` is present in `book.toml`
and that the `command` path matches where you saved the script.

If the preprocessor did run but you still see the error, the path in
the error might reference a file that genuinely doesn't exist. Check:

```bash
# Extract the missing path from the error, then verify in src/
ls src/images/<filename-from-error>
```

### Fonts appear to be defaults in the rendered EPUB

Run the "Fonts packaged" check above. If the count is less than 8, a
path in `additional-resources` doesn't match a file in `theme/fonts/`.
Re-run `./scripts/fetch-fonts.sh` and verify all 8 files exist.

### Code blocks have funny quote characters

Check `curly-quotes = false` is still in `[output.epub]` in `book.toml`.
Some mdbook-epub versions have a bug where curly-quote processing
mangles content inside `<code>` blocks.

### Preprocessor rejects the mdbook version

If you see an error like "preprocessor doesn't support this version of
mdbook", it means mdbook shelled out to the preprocessor and got a
non-zero exit from the `supports` subcommand. The script only accepts
`epub` as a renderer; for any other renderer it exits with 1, which is
the correct behaviour (mdbook then skips us for that renderer). This
shouldn't produce a user-facing error. If you see one, it's a bug worth
reporting back to me.

### GitHub Actions build fails on mdbook-epub install

`cargo binstall` may not have a prebuilt binary for `mdbook-epub`
in all cases. Fallback: replace that line in `publish.yml` with
`cargo install mdbook-epub` — slower (~2 min compile) but always works.

## Upstream bug report

mdbook-epub's asset resolution behaviour is a real bug worth filing.
A minimal repro:

> Given a book with structure `src/chapters/foo.md` containing
> `![](../images/foo.png)` and file `src/images/foo.png`, `mdbook-epub`
> v0.5.2 fails with:
>
> ```
> Failed to find resource file by 'root + src + path' = '<root>/images/foo.png'
> ```
>
> mdbook's HTML renderer correctly resolves the image as
> `src/images/foo.png` (interpreting `../images/foo.png` relative to
> the containing markdown file). mdbook-epub instead joins paths as
> `root + src + path`, which doesn't collapse the `..` against the
> chapter's directory.

Worth filing at https://github.com/Michael-F-Bryan/mdbook-epub/issues —
the project is actively maintained (`blandger` published v0.5.2 in
December 2025). When it's fixed, you can remove the preprocessor
config from `book.toml` and the script file. The rest of the EPUB
setup stays.

## What's intentionally not done

- **No PDF output.** If wanted later, cleanest path is `mdbook-pdf`
  against the HTML theme so PDFs match the web version.
- **No mermaid pre-rendering.** You confirmed no mermaid diagrams in
  the book. If they're added later, install `@mermaid-js/mermaid-cli`
  and add a pre-build step.
- **No Kindle-specific KFX build.** Calibre conversion from the EPUB
  is the standard workflow.
