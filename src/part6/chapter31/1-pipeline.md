## The Complete Pipeline

A Lykn project's CI pipeline has six stages. Each one is a gate — it must pass before the next runs.

### The Stages

```text
git push
  → CI triggers
    → lykn check src/           (syntax validation)
    → lykn compile src/         (full compilation)
    → biome check dist/         (lint + format compiled JS)
    → lykn test test/           (unit + integration tests)
    → lykn test --docs docs/    (documentation verification)
  → All green → deploy
```

### What Each Stage Catches

**`lykn check`** — syntax errors, unused bindings, missing type annotations. Fast, no output files. This catches typos before the full pipeline starts — a courtesy to the developer who just pushed a missing parenthesis, and to the CI minutes budget.

**`lykn compile`** — full compilation through the surface compiler and kernel codegen. This catches semantic errors that `check` doesn't: type mismatches in multi-clause `func` overlap detection, exhaustiveness failures in `match`, and macro expansion errors. The output is JavaScript, written to `dist/`.

**`biome check`** — lint and format the compiled JavaScript. Lykn's output is clean by design, but `biome` catches edge cases in hand-written JS helpers, interop files, or generated code that drifted.

**`lykn test`** — run the test suite. The `.lykn` test files are compiled to `.js` and handed to Deno's test runner (Ch 29). Unit tests, integration tests, and compiler output tests all run here.

**`lykn test --docs`** — verify documentation code examples. Every `` ```lykn `` block in the project's Markdown files is extracted, compiled, and (where annotated) executed. This is the step most projects don't have.

### What's Unusual Here

Two of these stages are uncommon in JavaScript projects. Most JS pipelines don't have a pre-compilation syntax check — their language doesn't have a separate check phase. And most projects don't test their documentation at all, because most languages don't make it easy. Lykn provides both, and both earn their place in the pipeline by catching failures that would otherwise surface as confused issues from users who copied a broken code example.
