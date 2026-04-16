## The `lykn` CLI

The full command reference:

```text
lykn language toolchain

Commands:
  new      Create a new lykn project
  run      Run a .lykn or .js file
  test     Run tests via Deno
  compile  Compile .lykn to JavaScript
  check    Check .lykn syntax
  fmt      Format .lykn files
  lint     Lint compiled JS via Deno
  publish  Publish package(s)
  help     Print help for a command
```

### `lykn new`

Scaffolds a new project with workspace structure, `project.json`, and starter files:

```sh
lykn new my-app
```

### `lykn run`

Compiles and executes in one step:

```sh
lykn run packages/my-app/mod.lykn
```

### `lykn test`

Runs the project's test suite via Deno:

```sh
lykn test
```

### `lykn compile`

Produces JavaScript output:

```sh
lykn compile main.lykn                    # to stdout
lykn compile main.lykn -o main.js         # to file
lykn compile main.lykn --strip-assertions # production mode
lykn compile main.lykn --kernel-json      # debug: kernel JSON
```

**`--strip-assertions`** removes type checks, contracts, `bind` type checks, and constructor validation. Multi-clause dispatch checks are NOT stripped — they're runtime semantics.

### `lykn check` / `lykn fmt` / `lykn lint`

```sh
lykn check main.lykn        # syntax validation
lykn fmt main.lykn           # format to stdout
lykn fmt -w main.lykn        # format in place
lykn lint                    # lint compiled JS via Deno
```
