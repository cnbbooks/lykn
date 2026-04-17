## ESLint and Biome: When You Need Them

Deno's built-in tools are the default. ESLint and Biome are alternatives for projects with specific needs.

### When to Reach for External Linters

- Project needs framework-specific plugins (React, Vue, Angular)
- Organizational standards require ESLint
- Need custom lint rules Deno doesn't support
- Want Biome's speed on very large codebases

### ESLint for Lykn Output

Flat config (`eslint.config.js`):

```javascript
export default [
  {
    rules: {
      "eqeqeq": ["error", "smart"],
      "no-unused-vars": ["warn", { "argsIgnorePattern": "^_" }],
      "prefer-const": "error",
    }
  }
];
```

The `"smart"` option for `eqeqeq` allows `== null` while enforcing `===` everywhere else.

### Biome

A single Rust binary that lints and formats in one pass. Install with `brew install biome`. Fast, minimal config, Prettier-compatible formatting. A solid choice if you need a standalone tool outside Deno's ecosystem.

### The Recommendation

Start with `deno lint` and `deno fmt`. They're already installed, already configured, and already what the lykn project uses. Reach for ESLint or Biome when you have a specific reason to.
