## Putting Together a Project

`lykn new` generates a workspace with this structure:

```text
my-app/
  project.json              ← tasks, import maps, workspace config
  README.md
  LICENSE                    ← Apache-2.0
  packages/
    my-app/
      deno.json             ← package config (name, version, lykn.kind)
      mod.lykn              ← main module
  test/
    mod_test.lykn            ← starter test (using @lykn/testing DSL)
  .gitignore
```

### Workspaces

Lykn projects use workspaces by default — each package lives under `packages/`. This scales from a single module to a multi-package monorepo without restructuring.

### The Workflow

```sh
lykn new my-app           # create
cd my-app
lykn run packages/my-app/mod.lykn   # develop
lykn test                 # verify
lykn compile --strip-assertions packages/my-app/mod.lykn -o dist/app.js  # build
lykn publish              # ship
```

Five commands, one config file, zero `node_modules`. The developer who has been reading since Chapter 1 now has everything: a language, a compiler, a project scaffold, and a deployment path. Write `.lykn`, run with `lykn run`, test with `lykn test`, compile for production.
