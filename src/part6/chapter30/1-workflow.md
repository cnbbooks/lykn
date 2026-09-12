## The Lykn Development Workflow

The `lykn` CLI handles the development lifecycle from source files to publishable packages:

```text
lykn new → lykn run/check/fmt → lykn build → lykn lint → lykn test → lykn dist → lykn publish
```

### Create

```sh
lykn new my-app
cd my-app
```

This scaffolds a workspace with `project.json`, a package under `packages/my-app/`, a starter `test/` file using `@lykn/testing`, and a project-local `bin/lykn`.

### Develop

```sh
lykn run packages/my-app/mod.lykn    # compile + run
lykn check packages/my-app/mod.lykn  # syntax and analysis check
lykn fmt -w packages/my-app/*.lykn   # format Lykn source in place
```

### Build, Lint, Test

```sh
lykn build                           # write JS to target/lykn/build/
lykn lint packages/my-app test       # lint Lykn source
lykn test                            # compile tests to target/lykn/test/ and run Deno
```

Deno is still doing the running. The difference is that Lykn owns the source workflow and puts generated JavaScript under `target/lykn/`, where it can be rebuilt, ignored, or discarded without pretending to be hand-written source.

### Stage and Publish

```sh
lykn dist                            # stage target/lykn/dist/<pkg>/
lykn publish --jsr --dry-run         # verify without publishing
lykn publish --jsr                   # publish to JSR
```

`lykn publish` runs `lykn dist` first unless you explicitly pass `--no-build`. It also refuses a dirty working tree unless you explicitly pass `--allow-dirty`, because a package should be an auditable source state rather than a rummage drawer with a version number.

### One Tool

The `lykn` binary is the single entry point. It delegates to Deno for execution and test running, but the developer starts from Lykn source and Lykn commands. One binary, one workflow, and generated files kept politely out of the sitting room.
