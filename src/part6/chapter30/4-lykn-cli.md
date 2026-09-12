## The `lykn` CLI

The current command surface:

```text
lykn language toolchain

Commands:
  fmt      Format .lykn files
  check    Check .lykn syntax
  compile  Compile .lykn to JavaScript
  run      Run a .lykn or .js file
  test     Run tests via Deno
  lint     Lint Lykn source for idiom/style issues
  new      Create a new lykn project
  build    Build workspace packages to target/lykn/build/
  dist     Stage workspace packages into target/lykn/dist/ for publishing
  add      Add an exact-pinned registry dependency to project.json
  link     Point a dependency at a local build for development
  unlink   Remove a local override
  publish  Publish package(s)
```

### `lykn new`

Scaffolds a new project with workspace structure, `project.json`, package metadata, starter tests, and a project-local binary:

```sh
lykn new my-app
```

### `lykn run`

Compiles and executes in one step:

```sh
lykn run packages/my-app/mod.lykn
lykn run packages/my-app/mod.lykn -- --port 3000
```

### `lykn build`

Builds workspace packages into `target/lykn/build/`:

```sh
lykn build
```

Use this when you want generated JavaScript on disk for Deno APIs, JS interop, deployment inspection, or tests that import built package output.

### `lykn test`

Runs the project's test suite via Deno:

```sh
lykn test
lykn test test/forms/
lykn test -- --filter addition
lykn test --docs docs/guides/
lykn test --docs src --fence lisp
```

The compiled tests land under `target/lykn/test/`, never next to source files.

### `lykn compile`

Produces JavaScript output for one file:

```sh
lykn compile packages/my-app/mod.lykn
lykn compile packages/my-app/mod.lykn -o target/lykn/build/my-app/mod.js
lykn compile packages/my-app/mod.lykn --strip-assertions
lykn compile packages/my-app/mod.lykn --kernel-json
```

Use `lykn compile` for inspection and one-off outputs. Use `lykn build` for normal workspace builds.

### `lykn check` / `lykn fmt` / `lykn lint`

```sh
lykn check packages/my-app/mod.lykn
lykn fmt packages/my-app/mod.lykn
lykn fmt -w packages/my-app/*.lykn test/*.lykn
lykn lint packages/my-app test
```

`lykn lint` is a Lykn-source linter. It does not replace `deno lint` for generated or hand-written JavaScript, and `deno lint` does not replace it for source-language traps.

### `lykn dist` / `lykn publish`

```sh
lykn dist
lykn publish --jsr --dry-run
lykn publish --npm --dry-run
lykn publish --jsr
```

`lykn dist` stages publishable packages under `target/lykn/dist/<pkg>/` with generated metadata. `lykn publish` runs the staging step first unless `--no-build` is passed, and it refuses dirty working trees unless `--allow-dirty` is explicit.
