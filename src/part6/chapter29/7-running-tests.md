## Running Tests

### The Commands

```bash
# Run all tests
lykn test

# Run tests in a directory
lykn test test/surface/

# Run a specific file
lykn test test/surface/bind_test.lykn

# Filter by name (Deno passthrough after --)
lykn test -- --filter "addition"

# Fail on first failure
lykn test -- --fail-fast

# With coverage
lykn test -- --coverage

# Test documentation
lykn test --docs docs/guides/

# Opt into this book's 0.6.0 lisp fences
lykn test --docs src --fence lisp
```

### Lykn-Specific Flags

`lykn test` recognises three flags of its own:

| Flag | Purpose |
|------|---------|
| `--docs <path>` | Test Markdown/HTML code blocks; repeat for multiple paths |
| `--fence <tag>` | Select a Markdown fence tag for docs mode; repeat for mixed sweeps |
| `--out-dir <dir>` | Write compiled JS to a separate directory |
| `--compile-only` | Compile but don't run |

### Deno Passthrough

Everything after `--` passes through to `deno test`. Filtering, reporters, coverage, watch mode, permissions — all of Deno's test infrastructure is available without `lykn test` needing to know about it.

| Flag | Purpose |
|------|---------|
| `--filter <pattern>` | Run tests matching name pattern |
| `--fail-fast` | Stop on first failure |
| `--parallel` | Run test files in parallel |
| `--coverage` | Collect coverage data |
| `--reporter <name>` | Output format: pretty, dot, tap, junit |
| `--watch` | Re-run on file changes |

Any new Deno test-runner flag works automatically when passed after `--`. `lykn test` doesn't gatekeep — it compiles the Lykn, then gets out of the way.

### Test File Conventions

Project tests normally live under `test/` and use the `_test.lykn` suffix:

```text
my-project/
  project.json
  packages/
    my-app/
      mod.lykn
      math.lykn
  test/
    math_test.lykn
    integration_test.lykn
```

The `_test.lykn` suffix compiles to `_test.js` under `target/lykn/test/`, which Deno runs through the generated test configuration. The source tree stays clean; generated test JavaScript does not sit beside the `.lykn` file that produced it.
