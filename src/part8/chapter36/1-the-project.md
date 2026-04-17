## The Project: `mdify`

`mdify` is a CLI tool that converts Markdown to HTML. It reads a file, parses it into a structured intermediate representation, renders it as HTML, and writes the output.

### Supported Features

- Headings: `# H1` through `###### H6`
- Paragraphs
- Bold (`**bold**`) and italic (`*italic*`)
- Inline code (`` `code` ``)
- Fenced code blocks (` ``` `)
- Links (`[text](url)`)
- Unordered lists (`- item`)
- Blockquotes (`> quoted`)

### Usage

```sh
lykn run mdify.lykn input.md
lykn run mdify.lykn input.md -o output.html
```

### Project Structure

```text
mdify/
  project.json
  packages/
    mdify/
      mod.lykn           ← entry point
      parser.lykn        ← Markdown parser
      renderer.lykn      ← HTML renderer
  test/
    parser.test.js
    renderer.test.js
```
