## Testing

Tests import the compiled JavaScript and use Deno's test runner:

```javascript
import { assertEquals } from "jsr:@std/assert";
import { parseMarkdown } from "../dist/parser.js";
import { renderBlocks } from "../dist/renderer.js";

Deno.test("parses a heading", () => {
  const blocks = parseMarkdown("# Hello");
  assertEquals(blocks.length, 1);
  assertEquals(blocks[0].tag, "Heading");
  assertEquals(blocks[0].level, 1);
  assertEquals(blocks[0].text, "Hello");
});

Deno.test("renders bold inline", () => {
  const blocks = parseMarkdown("This is **bold** text.");
  const html = renderBlocks(blocks);
  assertEquals(html, "<p>This is <strong>bold</strong> text.</p>");
});

Deno.test("renders a code block", () => {
  const md = "```python\nprint('hi')\n```";
  const html = renderBlocks(parseMarkdown(md));
  assertEquals(
    html,
    '<pre><code class="language-python">print(\'hi\')</code></pre>'
  );
});
```

Run with `lykn test`. Tests verify the full pipeline: parse Markdown → produce `Block` values → render HTML.
