## Task Composition with `deno.json`

The pipeline lives in `deno.json` as composable tasks. A developer runs `deno task verify` locally before pushing. CI runs the same sequence. Same steps, same order, same results.

### The Task Configuration

```json
{
  "tasks": {
    "check": "lykn check src/",
    "compile": "lykn compile src/ --out-dir dist/",
    "lint": "biome check dist/",
    "test": "lykn test test/",
    "test:docs": "lykn test --docs docs/",
    "verify": "deno task check && deno task compile && deno task lint && deno task test && deno task test:docs",
    "build": "lykn compile --strip-assertions src/ --out-dir dist/ && biome check --write dist/",
    "dev": "deno task compile && deno run --allow-all dist/app.js"
  }
}
```

### What Each Task Does

**`check`** — fast syntax validation, no output files. The first gate.

**`compile`** — full compilation to `dist/`. The source of truth for what the project produces.

**`lint`** — lint and format the compiled output. `biome check` combines lint and format verification in a single pass.

**`test`** — run all `.lykn` test files. Compiles them, hands the `.js` to Deno.

**`test:docs`** — verify Markdown code examples. Separate from `test` because you might want to run code tests without documentation tests, or vice versa.

**`verify`** — the full pipeline, sequenced with `&&`. Each step must pass before the next runs. This is what a developer runs before pushing, and what CI runs after.

**`build`** — production build. `--strip-assertions` removes type checks and contracts; `biome check --write` auto-fixes formatting. The output is deploy-ready JavaScript.

**`dev`** — compile and run for development. Quick feedback loop — edit `.lykn`, run `deno task dev`, see the result.

### The `&&` Matters

The `verify` task chains steps with `&&`, not `;`. If `lykn check` fails, nothing compiles. If compilation fails, nothing lints. The pipeline is a sequence of gates, not a list of independent jobs. A semicolon would run every step regardless of failures, which is the CI equivalent of a doctor who finishes the checkup even after discovering the patient is no longer present.
