## The Lykn Development Workflow

The `lykn` CLI handles the entire development lifecycle:

```text
lykn new → lykn run → lykn test → lykn compile → lykn lint → lykn publish
```

### Create

```sh
lykn new my-app
cd my-app
```

Scaffolds a workspace with standard project structure, `project.json`, and a starter module.

### Develop

```sh
lykn run packages/my-app/mod.lykn    # compile + run
lykn check packages/my-app/mod.lykn  # syntax check
lykn fmt -w packages/my-app/         # format in place
```

### Test

```sh
lykn test                            # run all tests
```

Delegates to Deno's test runner under the hood.

### Build for Production

```sh
lykn compile packages/my-app/mod.lykn --strip-assertions -o dist/app.js
```

### Lint

```sh
lykn lint                            # lint compiled output via Deno
```

### Publish

```sh
lykn publish                         # publish package(s)
```

### One Tool

The `lykn` binary is the single entry point. It delegates to Deno for running, testing, and linting, but the developer doesn't need to know the underlying commands. One binary, one workflow.
