## External Linters: When You Need Them

Deno's built-in tools and `lykn lint` are the default. ESLint and Biome are optional tools for projects with specific JavaScript-side needs.

### When to Reach for External Linters

- Framework-specific JavaScript plugins: React, Vue, Angular, and their cousins in increasingly elaborate hats
- Organizational standards that already require ESLint
- Custom JavaScript lint rules Deno does not support
- Very large generated or hand-written JS codebases where Biome's speed matters

### ESLint for Lykn Output

Flat config (`eslint.config.js`):

```javascript
export default [
  {
    ignores: ["target/lykn/**"],
    rules: {
      "eqeqeq": ["error", "smart"],
      "no-unused-vars": ["warn", { "argsIgnorePattern": "^_" }],
      "prefer-const": "error",
    }
  }
];
```

The `"smart"` option for `eqeqeq` allows `== null` while enforcing `===` elsewhere. That matters because Lykn intentionally emits nullish checks in a few places where JavaScript's loose-null idiom is the correct spell.

### Biome

Biome is a fast standalone formatter and linter. Use it if your project already standardizes on Biome or needs one binary outside Deno's toolchain. For ordinary Lykn projects, start with `lykn lint`, `lykn fmt`, `deno lint`, and `deno fmt`.

### The Recommendation

Do not start by installing a second linting ecosystem. Start with Lykn's source linter and Deno's built-ins. Add ESLint or Biome when a concrete JavaScript requirement appears, and keep generated `target/lykn/` output out of source-style policy unless that policy is intentionally about compiler output.
