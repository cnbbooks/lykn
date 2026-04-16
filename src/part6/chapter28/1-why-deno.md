## Why Deno?

The Lykn toolchain uses Deno exclusively. The reasons align with Lykn's own design principles:

**ESM-native** — all code is ES modules. No `require`, no CommonJS, no `.mjs` vs `.js`. This matches Lykn's ESM-only compilation (Ch 16).

**Single binary** — `deno` is one executable. No `npm install` for the toolchain. Install Deno, clone lykn, build with `cargo` — done.

**Permissions** — network, file, and environment access must be explicitly granted. `deno run --allow-read app.js` is the minimum. Security by default, not by opt-in.

**Built-in tools** — test runner, formatter, linter, bundler. No external tooling needed for basic workflows.

**Node.js compatibility** — Deno runs most Node.js code via `node:` specifiers (`import "node:fs"`) and npm packages via `npm:` specifiers. The ecosystem is accessible.

**Standard library** — `jsr:@std/*` provides vetted, maintained utilities: HTTP servers, path manipulation, assertions, encoding.

### The Daily Workflow

The Lykn developer's commands:

```sh
lykn compile src/app.lykn -o dist/app.js   # compile
deno run --allow-net dist/app.js            # run
deno test test/                              # test
deno task build                              # project tasks
```
