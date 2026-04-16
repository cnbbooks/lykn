## ESLint: When You Need It

Biome is the default. ESLint is the alternative — for projects that need custom rules, framework-specific plugins, or integration with existing ESLint infrastructure.

### When ESLint over Biome

- Project already has extensive ESLint configuration
- Need framework-specific plugins (React, Vue, Angular)
- Need custom rules Biome doesn't support
- Organizational standards require ESLint

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

The `"smart"` option for `eqeqeq` allows `== null` comparisons while enforcing `===` everywhere else — exactly what Lykn's output needs.

### The ESTree Connection

ESLint parses JavaScript into an ESTree AST — the same format Lykn's JS compiler produces. The analysis operates on the same data structure that Lykn emits. This means ESLint's rules apply naturally to Lykn output without special handling.
