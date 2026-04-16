## The Lykn Development Workflow

The complete pipeline, end to end:

```text
.lykn source → lykn compile → .js output → biome check → deno test → deno run
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
biome check dist/                     # lint + format + organize imports
biome check --write dist/             # auto-fix
biome ci dist/                        # CI mode (fail on any issue)
```

### Test and Run

```sh
deno test test/                       # run test suite
deno run --allow-net dist/app.js      # execute with permissions
deno task build                       # project scripts from deno.json
```

### The Four Tools

`lykn` compiles. `biome` lints and formats the output. `deno test` verifies. `deno run` executes. No npm. No `package.json`. No `node_modules`. Each tool is a single binary.
