## Documentation Verification in CI

The `lykn test --docs` step is the most unusual part of the pipeline. Most projects don't test their documentation. Lykn does.

### What It Catches

**Compiler changes that break examples.** A surface form's output changes — perhaps `bind` now emits a slightly different variable declaration, or `func` adjusts its whitespace. Every "Compiles to:" block in every Markdown file that shows the old output is now wrong. Without automated testing, those examples stay wrong until a reader notices, files an issue, and waits for a fix. With `lykn test --docs`, the CI build fails immediately.

**Anti-patterns that stop being anti-patterns.** Documentation often includes `` ```lykn,compile-fail `` blocks showing code that *should* fail — demonstrating what the compiler rejects. When a new feature accidentally makes one of these examples valid, the documentation test catches it. The anti-pattern is no longer an anti-pattern, and the documentation needs updating.

**Output drift.** The compiled JavaScript for a given Lykn input may change subtly between compiler versions — additional semicolons, reordered declarations, different whitespace. The Markdown test catches the drift before it becomes a discrepancy between what the documentation shows and what the compiler actually produces.

### What It Doesn't Catch

**Prose that contradicts the code.** If a paragraph says "this produces an array" but the code example clearly produces an object, no automated test will catch it. That's a human review. The tool verifies *code*, not *claims about code*.

**Runtime behavior.** A bare `` ```lykn `` block is compile-checked only. If the code compiles but does something unexpected at runtime, the test passes. Use `` ```lykn,run `` for examples where runtime correctness matters.

### The Self-Referential Quality

This book's code examples are tested in CI. Every `` ```lykn `` block in every chapter is verified on every commit. The book tests itself — not as a marketing claim, but as a CI step that fails the build when an example breaks. The reader is reading documentation that has been mechanically verified to be correct, which is a higher bar than most technical writing clears, and a lower bar than most technical writing should.
