## Markdown Documentation Testing

The book you're reading has 39 chapters. All of them contain Lykn code examples. Without automated testing, those examples break silently when the compiler changes — and compiler changes, in a project that is still actively evolving, are not hypothetical. They happen. Often on Tuesdays.

`lykn test --docs` extracts selected Lykn code blocks from Markdown files and verifies them. The default fence tag is `lykn`; this book keeps Lykn source under `lisp` fences through 0.6.0, so the book gate passes `--fence lisp`.

### Code Block Annotations

The fence language identifier controls what the tester does with each block:

| Fence | Behaviour |
|-------|-----------|
| `` ```lisp `` | Compile check when the command includes `--fence lisp` |
| `` ```lisp,run `` | Compile and execute |
| `` ```lisp,compile-fail `` | Assert compilation *fails* (for anti-pattern examples) |
| `` ```lisp,skip `` | Don't test this block |
| `` ```lisp,fragment `` | Partial expression — skip |
| `` ```lisp,continue `` | Concatenate with preceding blocks |

For this book, a bare `` ```lisp `` fence is a compile check because CI invokes `lykn test --docs src --fence lisp`. If it parses and compiles without errors, the test passes. Most documentation examples need nothing more.

### Output Matching

When a Lykn block is followed by a JavaScript block, the tester compiles the Lykn and asserts the output matches the JavaScript:

````markdown
```lisp
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
```lisp,continue
(type Color Red Green Blue)
```

Now use it:

```lisp,continue
(match my-color
  (Red "stop") (Green "go") (Blue "sky"))
```
````

These two blocks are concatenated and compiled as a single unit. Section boundaries (`##` headings) reset the accumulator, preventing cross-section coupling — each section starts fresh, and any dependency is explicit.

### Why This Matters

The book gate extracts Lykn code blocks, compiles them, and executes annotated runtime examples. During the 0.6.0 refresh, failures are routing input: a stale example gets fixed, a deliberate negative example gets `compile-fail`, and a language/tooling defect gets a discovery row instead of a prose workaround.

The testing infrastructure was built partly *for* this book. The self-referential quality is worth noting: the chapter you're reading describes a tool that tests chapters like this one. If an example is meant to compile, the gate should be able to prove it; if it is not meant to compile, the fence annotation should say so plainly.
