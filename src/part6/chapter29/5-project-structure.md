## Putting Together a Project

A complete Lykn project structure:

```text
my-project/
  deno.json          ← tasks, import maps
  biome.json         ← linter/formatter config
  src/
    app.lykn         ← lykn source
    utils.lykn
  dist/              ← compiled JS output (gitignored)
    app.js
    utils.js
  test/
    app.test.js      ← Deno tests (in JS, on compiled output)
  README.md
```

### `deno.json`

```json
{
  "tasks": {
    "compile": "lykn compile src/ --out-dir dist/",
    "test": "deno test test/",
    "check": "lykn check src/ && biome check dist/",
    "dev": "lykn compile src/ --out-dir dist/ && deno run --allow-all dist/app.js",
    "build": "lykn compile --strip-assertions src/ --out-dir dist/ && biome check --write dist/"
  }
}
```

### The Workflow

`deno task compile` to build. `deno task test` to verify. `deno task build` for production. Three commands, two config files, zero `node_modules`.

The developer who has been reading since Chapter 1 now has everything: a language, a compiler, a linter, a test runner, and a deployment path. Write `.lykn`, compile to `.js`, lint with Biome, test with Deno, run anywhere JavaScript runs.
