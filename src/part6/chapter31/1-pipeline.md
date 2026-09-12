## The Complete Pipeline

A Lykn project's CI pipeline has five ordinary stages. Each one is a gate — it must pass before the next one claims the project is ready.

### The Stages

```text
git push
  → CI triggers
    → lykn check packages/my-app/mod.lykn test/mod_test.lykn  (syntax and analysis)
    → lykn build                      (workspace build to target/lykn/build/)
    → lykn lint packages/ test/       (Lykn source lint)
    → lykn test                       (tests compile to target/lykn/test/ and run in Deno)
    → lykn test --docs docs/          (documentation verification)
  → All green → lykn dist / deploy / publish dry-run
```

### What Each Stage Catches

**`lykn check`** — syntax errors, unused bindings, missing type annotations, overlap failures, exhaustiveness failures, and macro expansion errors. Fast, no output files. This catches mistakes before the full pipeline starts — a courtesy to the developer who just pushed a missing parenthesis, and to the CI minutes budget.

**`lykn build`** — full workspace compilation. Generated JavaScript goes to `target/lykn/build/<pkg>/`, preserving package-relative paths. This is the output that JavaScript tests, Deno APIs, and deployment inspection should consume.

**`lykn lint`** — source-level Lykn linting. It catches anti-patterns in what the author wrote: CommonJS habits, unsafe JavaScript idioms expressed through Lykn, shadowing, and test-file import traps. Optional `deno lint target/lykn/build/` can audit generated or hand-written JavaScript separately.

**`lykn test`** — run the test suite. The `.lykn` and `.lyk` test files compile to JavaScript under `target/lykn/test/`, and Deno's test runner executes them.

**`lykn test --docs`** — verify documentation code examples. By default it extracts `lykn` fences; this book uses `lisp` fences through 0.6.0 and therefore runs with `--fence lisp`.

### What's Unusual Here

Two of these stages are uncommon in JavaScript projects. Most JS pipelines don't have a source-language check phase before JavaScript exists. And most projects don't test their documentation at all, because most languages don't make it easy. Lykn provides both, and both earn their place by catching failures that would otherwise surface as confused issues from users who copied a broken code example.
