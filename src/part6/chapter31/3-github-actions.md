## GitHub Actions

The `deno.json` tasks define *what* runs. GitHub Actions defines *when* and *where*. The workflow below is a complete CI configuration for a Lykn project — copy it, adjust the paths, and push.

### The Workflow

```yaml
name: CI
on: [push, pull_request]

jobs:
  verify:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Install Deno
        uses: denoland/setup-deno@v2
        with:
          deno-version: v2.x

      - name: Install lykn
        run: cargo install lykn-cli

      - name: Install Biome
        run: |
          curl -fsSL https://biomejs.dev/install.sh | sh
          echo "$HOME/.biome/bin" >> $GITHUB_PATH

      - name: Check syntax
        run: lykn check src/

      - name: Compile
        run: lykn compile src/ --out-dir dist/

      - name: Lint compiled output
        run: biome ci dist/

      - name: Run tests
        run: lykn test test/

      - name: Test documentation
        run: lykn test --docs docs/
```

### Walking Through the Steps

**Setup** installs three tools: Deno (the runtime), lykn (the compiler), and Biome (the linter). Each is a single binary — no `node_modules`, no dependency trees, no install scripts that phone home.

**Check** runs `lykn check` for fast syntax validation. This catches obvious errors — missing parentheses, undefined symbols, unused bindings — before the full compilation pipeline starts.

**Compile** runs the full surface compiler and kernel codegen. If this fails, the source has a semantic error: a type mismatch, an exhaustiveness failure, a macro expansion that produced invalid kernel forms.

**Lint** runs `biome ci` — the CI-specific mode that fails on any issue without auto-fixing. In development you might use `biome check --write` to fix formatting automatically. In CI, you want to know about it, not hide it.

**Test** runs the lykn test suite. The `.lykn` test files compile to `.js` and Deno's test runner executes them.

**Documentation** runs `lykn test --docs` against the project's Markdown files. Every code example is verified.

### Portability

This workflow uses GitHub Actions because it's the most common CI platform, but the steps translate directly to any CI system. The pipeline is just shell commands — `lykn check`, `lykn compile`, `biome ci`, `lykn test`. GitLab CI, CircleCI, Buildkite, or a shell script in a `Makefile` — the commands are the same. The CI configuration is plumbing; the pipeline is the substance.
