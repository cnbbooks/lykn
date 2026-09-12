## Putting Together a Project

`lykn new` generates a workspace with this structure:

```text
my-app/
  project.json              ← workspace imports and metadata
  README.md
  LICENSE                    ← Apache-2.0
  bin/
    lykn                    ← project-local CLI binary
  packages/
    my-app/
      deno.json             ← package config (name, version, exports, lykn.kind)
      mod.lykn              ← main module
      auth/
      users/
  test/
    mod_test.lykn            ← starter test using @lykn/testing
  target/lykn/              ← generated build/test/dist output
  .gitignore
```

### Workspaces

Lykn projects use workspaces by default — each package lives under `packages/`. This scales from a single module to a multi-package monorepo without restructuring.

### The Workflow

```sh
lykn new my-app                    # create
cd my-app
lykn run packages/my-app/mod.lykn   # develop
lykn build                         # build to target/lykn/build/
lykn test                          # verify tests under target/lykn/test/
lykn dist                          # stage target/lykn/dist/<pkg>/
lykn publish --jsr --dry-run       # verify the package before shipping
```

Six commands, one root workspace config, package-local metadata, zero `node_modules`. The developer who has been reading since Chapter 1 now has everything: a language, a compiler, a project scaffold, generated outputs under `target/lykn/`, and a deployment path. Write `.lykn`, run with `lykn run`, test with `lykn test`, build with `lykn build`, stage with `lykn dist`.
