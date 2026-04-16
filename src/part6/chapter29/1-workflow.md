## The Lykn Development Workflow

The complete pipeline, end to end:

```text
.lykn source → lykn compile → .js output → deno lint → deno fmt → deno test → deno run
```

### Compile

```sh
lykn compile src/app.lykn              # single file to stdout
lykn compile src/app.lykn -o dist/app.js  # single file to file
lykn compile --strip-assertions src/   # production mode
lykn check src/app.lykn               # syntax check without output
lykn fmt src/app.lykn                  # format lykn source
```

### Lint and Format

```sh
deno lint dist/                       # lint compiled output
deno fmt dist/                        # format compiled output
deno lint src/ && deno test test/     # check + test in one step
```

### Test and Run

```sh
deno test test/                       # run test suite
deno run --allow-net dist/app.js      # execute with permissions
deno task build                       # project scripts from deno.json
```

### Three Tools

`lykn` compiles and formats `.lykn` source. `deno` lints, formats, tests, and runs the compiled JavaScript. No npm. No `package.json`. No `node_modules`. Two binaries do everything.
