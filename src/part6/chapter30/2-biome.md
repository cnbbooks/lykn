## Deno: Linting and Formatting

Deno includes a linter (`deno lint`) and a formatter (`deno fmt`) built in. No external tools needed, no configuration files, no plugins to install.

### Linting

```sh
deno lint dist/              # lint compiled JS output
deno lint src/               # lint JS source (if any)
```

Deno's linter uses recommended rules by default. It catches common JavaScript issues — unused variables, implicit type coercion, unreachable code.

### Formatting

```sh
deno fmt dist/               # format compiled output
deno fmt --check dist/       # check without modifying (CI mode)
```

Deno's formatter is opinionated — consistent indentation, semicolons, quote style. Like Prettier, but built in.

### Lykn-Specific Considerations

**The `== null` exception**: Lykn's `some->` and compiler-generated null checks use `== null` (loose equality). Deno's `no-explicit-any` and equality rules may flag these. Configure exceptions in `project.json` if needed:

```json
{
  "lint": {
    "rules": {
      "exclude": ["no-explicit-any"]
    }
  }
}
```

**Generated code patterns**: The compiled JS is generated output. Some lint rules may flag patterns from `match` IIFEs or gensym variable names. These are correct code — suppress or exclude generated directories as needed.

### Why Not a Separate Linter?

Deno's built-in tools align with Lykn's philosophy: fewer tools, fewer config files, fewer things that can go wrong. The lykn project itself uses `deno lint` — no Biome, no ESLint, no external dependencies. One runtime does it all.
