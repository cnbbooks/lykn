## Deno Linting and Formatting

Deno includes a JavaScript linter (`deno lint`) and formatter (`deno fmt`) built in. Lykn adds a source linter of its own.

### Two Different Linters

```sh
lykn lint packages/my-app test     # lint Lykn source for surface-language issues
lykn build                         # generate JavaScript under target/lykn/build/
deno lint target/lykn/build/       # optional: lint generated or hand-written JS
```

`lykn lint` judges what you wrote before expansion: `require`, unsafe defaults, missing radix arguments, accidental shadowing, method-on-expression traps, and the other source-level patterns from the anti-pattern catalog. `deno lint` judges JavaScript. Both can be useful, but they are not the same tool wearing different hats.

### Formatting

```sh
lykn fmt -w packages/my-app/       # format Lykn source
deno fmt target/lykn/build/        # optional: format generated JS for inspection
```

Generated JavaScript is normally disposable. If you format it, do so because you are inspecting or packaging it, not because the project has become a tiny JavaScript monastery with a robe for every semicolon.

### Generated Code Patterns

Compiled JS may contain gensym names, inserted type checks, and IIFEs produced by `match` or position-aware control flow. Those are compiler output. Prefer excluding generated directories from style-only JS checks unless you are deliberately auditing emitted JavaScript.

### Why Not a Separate Default Linter?

The default stack is small: `lykn lint` for Lykn source, `deno lint` and `deno fmt` when you need JavaScript tooling, no `node_modules`, no separate formatter daemon. Biome can still be useful for projects that need it; it is no longer the default Lykn workflow.
