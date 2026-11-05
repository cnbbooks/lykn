# Mermaid Assets

- `mermaid.min.js`: Mermaid 12.3.0, vendored without modification from
  <https://cdn.jsdelivr.net/npm/mermaid@12.3.0/dist/mermaid.min.js>.
- `mermaid-init.js`: the mdbook-mermaid initializer, adapted for the book's
  `lfe-pdp` theme and mdBook 0.5 theme-menu IDs.
- Preprocessor: mdbook-mermaid 0.17.1.

`make deps` installs the pinned preprocessor and refreshes the pinned browser
bundle. It deliberately preserves the customized initializer. Update the two
version variables in the Makefile when upgrading.

The local preprocessor was rebuilt with `mdbook-core` and
`mdbook-preprocessor` 0.5.3 to match `mdbook --version` and avoid a patch-version
mismatch warning. Binary releases or a fresh Cargo install can use a different
compatible mdBook patch version; keep the renderer and preprocessor aligned.
