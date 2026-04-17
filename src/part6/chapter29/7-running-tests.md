## Running Tests

### The Commands

```bash
# Run all tests
lykn test

# Run tests in a directory
lykn test test/surface/

# Run a specific file
lykn test test/surface/bind_test.lykn

# Filter by name
lykn test --filter "addition"

# Fail on first failure
lykn test --fail-fast

# With coverage
lykn test --coverage

# Test documentation
lykn test --docs docs/guides/

# Both code and documentation
lykn test test/ --docs docs/
```

### Lykn-Specific Flags

`lykn test` recognises three flags of its own:

| Flag | Purpose |
|------|---------|
| `--docs <glob>` | Test Markdown code blocks |
| `--out-dir <dir>` | Write compiled JS to a separate directory |
| `--compile-only` | Compile but don't run |

### Deno Passthrough

Everything else passes through to `deno test`. Filtering, reporters, coverage, watch mode, permissions — all of Deno's test infrastructure is available without `lykn test` needing to know about it.

| Flag | Purpose |
|------|---------|
| `--filter <pattern>` | Run tests matching name pattern |
| `--fail-fast` | Stop on first failure |
| `--parallel` | Run test files in parallel |
| `--coverage` | Collect coverage data |
| `--reporter <name>` | Output format: pretty, dot, tap, junit |
| `--watch` | Re-run on file changes |

Any new flag Deno adds works automatically. `lykn test` doesn't gatekeep — it compiles the Lykn, then gets out of the way.

### Test File Conventions

Test files use the `_test.lykn` suffix and live alongside the code they test:

```text
my-project/
  src/
    math.lykn
    math_test.lykn
  test/
    integration_test.lykn
  project.json
```

The `_test.lykn` suffix compiles to `_test.js`, which Deno discovers with its standard glob. Co-located tests, no separate test directory required — though one is perfectly fine for integration tests or anything that doesn't belong next to a specific source file.
