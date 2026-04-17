## Markdown Documentation Testing

The book you're reading has 39 chapters. All of them contain Lykn code examples. Without automated testing, those examples break silently when the compiler changes — and compiler changes, in a project that is still actively evolving, are not hypothetical. They happen. Often on Tuesdays.

`lykn test --docs` extracts Lykn code blocks from Markdown files and verifies them.

### Code Block Annotations

The fence language identifier controls what the tester does with each block:

| Fence | Behaviour |
|-------|-----------|
| `` ```lykn `` | Compile check — assert no errors |
| `` ```lykn,run `` | Compile and execute |
| `` ```lykn,compile-fail `` | Assert compilation *fails* (for anti-pattern examples) |
| `` ```lykn,skip `` | Don't test this block |
| `` ```lykn,fragment `` | Partial expression — skip |
| `` ```lykn,continue `` | Concatenate with preceding blocks |

The default — a bare `` ```lykn `` fence — is a compile check. If it parses and compiles without errors, the test passes. Most documentation examples need nothing more.

### Output Matching

When a Lykn block is followed by a JavaScript block, the tester compiles the Lykn and asserts the output matches the JavaScript:

````markdown
```lykn
(bind max-retries 3)
```

Compiles to:

```js
const maxRetries = 3;
```
````

The comparison trims whitespace and, for single-line output, normalises internal whitespace. Multi-line expected output uses exact matching — when the reader is shown a formatted function body, the formatting matters.

### Block Accumulation

By default, each block compiles independently. Documentation examples should stand alone, and most do. But some sections build up a program incrementally — a type defined in one block, used in the next.

The `continue` annotation concatenates blocks within a section:

````markdown
```lykn,continue
(type Color Red Green Blue)
```

Now use it:

```lykn,continue
(match my-color
  (Red "stop") (Green "go") (Blue "sky"))
```
````

These two blocks are concatenated and compiled as a single unit. Section boundaries (`##` headings) reset the accumulator, preventing cross-section coupling — each section starts fresh, and any dependency is explicit.

### Why This Matters

Every code example in this book is tested on every commit. The Lykn code blocks are extracted, compiled, and (where annotated) executed automatically in CI. When the compiler changes — a new surface form, a formatting adjustment, a bugfix that alters output — the documentation tests catch the examples that need updating.

The testing infrastructure was built partly *for* this book. The self-referential quality is worth noting: the chapter you're reading describes a tool that tests the chapter you're reading. If this paragraph's code examples were wrong, the CI build would have failed before you saw them.
