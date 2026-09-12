## Task Composition with `deno.json`

The pipeline can live in `deno.json` as composable tasks. A developer runs `deno task verify` locally before pushing. CI runs the same sequence. Same steps, same order, same results.

### The Task Configuration

```json
{
  "tasks": {
    "check": "lykn check packages/my-app/mod.lykn test/mod_test.lykn",
    "build": "lykn build",
    "lint": "lykn lint packages/ test/",
    "test": "lykn test",
    "test:docs": "lykn test --docs docs/",
    "dist": "lykn dist",
    "publish:dry": "lykn publish --jsr --dry-run",
    "verify": "deno task check && deno task build && deno task lint && deno task test && deno task test:docs"
  }
}
```

### What Each Task Does

**`check`** — fast syntax and analysis validation, no output files. The first gate.

**`build`** — workspace compilation to `target/lykn/build/`. The source of truth for generated JavaScript during local development and CI.

**`lint`** — lint the Lykn source. If you also need JavaScript linting, add a separate `deno lint target/lykn/build/` task after `build`.

**`test`** — run all `.lykn` and `.lyk` test files through `lykn test`. The generated JavaScript lands under `target/lykn/test/`.

**`test:docs`** — verify Markdown code examples. For this book's 0.6.0 `lisp` fences, the command is `lykn test --docs src --fence lisp`.

**`dist`** — stage publishable packages under `target/lykn/dist/`.

**`publish:dry`** — ask the publish command to run its staging and registry dry-run checks without uploading anything.

**`verify`** — the full local gate, sequenced with `&&`. If `lykn check` fails, nothing builds. If the build fails, nothing lints. A semicolon would run every step regardless of failures, which is the CI equivalent of a doctor who finishes the checkup even after discovering the patient is no longer present.
