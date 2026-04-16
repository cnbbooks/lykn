## Biome: Linting and Formatting

Biome is Lykn's recommended linter and formatter. It's a single Rust binary that handles both — no plugins, no configuration cascade, fast.

### Why Biome

- **Fast** — written in Rust, orders of magnitude faster than ESLint on large codebases
- **Single binary** — `brew install biome`, no npm
- **Lint + format in one pass** — `biome check` does both
- **Opinionated formatter** — Prettier-compatible with minimal config
- **Recommended rules** — sane defaults that rarely need customization

### Configuration

A typical Lykn project's `biome.json`:

```json
{
  "$schema": "https://biomejs.dev/schemas/1.9.4/schema.json",
  "organizeImports": { "enabled": true },
  "linter": {
    "enabled": true,
    "rules": { "recommended": true }
  },
  "formatter": {
    "enabled": true,
    "indentStyle": "space",
    "indentWidth": 2
  }
}
```

Recommended rules, space indentation, organize imports. That's the whole config.

### Lykn-Specific Considerations

**The `== null` exception**: Lykn's `some->` and compiler-generated null checks use `== null` (loose equality). Biome's `noDoubleEquals` rule flags these. Suppress with an inline comment or configure an exception for generated files.

**Generated code patterns**: The compiled JS is generated output. Some lint rules may flag patterns from `match` IIFEs or gensym variable names. Use Biome's ignore patterns for generated directories if needed.

**camelCase output**: Biome's naming convention rules (if enabled) should pass — Lykn already outputs camelCase.

### Commands

```sh
biome check dist/              # lint + format + organize imports
biome check --write dist/      # auto-fix what can be fixed
biome lint dist/               # lint only
biome format --write dist/     # format in place
biome ci dist/                 # CI mode (fail on any issue)
```
