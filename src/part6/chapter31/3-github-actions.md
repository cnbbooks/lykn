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

      - name: Install Rust
        uses: dtolnay/rust-toolchain@stable

      - name: Install lykn
        run: cargo install lykn-cli

      - name: Check syntax and analysis
        run: lykn check packages/my-app/mod.lykn test/mod_test.lykn

      - name: Build workspace packages
        run: lykn build

      - name: Lint Lykn source
        run: lykn lint packages/ test/

      - name: Run tests
        run: lykn test

      - name: Test documentation
        run: lykn test --docs docs/

      - name: Verify publish staging
        run: lykn publish --jsr --dry-run
```

### Walking Through the Steps

**Setup** installs Deno (the runtime), Rust (for installing the compiler), and Lykn. There is no `node_modules` step in the default path.

**Check** runs `lykn check` for syntax and analysis validation. This catches missing parentheses, bad parameter shapes, overlap errors, and other source problems before the full build starts.

**Build** runs the workspace build and writes generated JavaScript under `target/lykn/build/`.

**Lint** runs `lykn lint`, the source-language linter. If your project also wants JavaScript linting, add `deno lint target/lykn/build/` as a separate explicit step.

**Test** runs the Lykn test suite. The source tests compile under `target/lykn/test/`; Deno executes the generated files.

**Documentation** runs `lykn test --docs` against the project's Markdown files. This book uses `--fence lisp`; most new Lykn project docs can use the default `lykn` fence.

**Publish dry-run** runs the same staging path used by real publication, without uploading. `lykn publish` refuses dirty working trees by default; CI should be boring enough to appreciate that.

### Portability

This workflow uses GitHub Actions because it's the most common CI platform, but the steps translate directly to any CI system. The pipeline is just shell commands — `lykn check`, `lykn build`, `lykn lint`, `lykn test`, `lykn test --docs`, `lykn publish --dry-run`. GitLab CI, CircleCI, Buildkite, or a shell script in a `Makefile` — the commands are the same. The CI configuration is plumbing; the pipeline is the substance.
