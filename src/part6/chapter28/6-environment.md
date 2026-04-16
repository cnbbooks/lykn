## Environment and Configuration

### Environment Variables

```lisp
(bind port (Deno:env:get "PORT"))
(bind mode (Deno:env:get "NODE_ENV"))
```

### Command-Line Arguments

```lisp
Deno:args    ;; → string array of CLI args (after --)
```

### `deno.json`

Lykn projects use `deno.json` for task definitions and configuration:

```json
{
  "tasks": {
    "compile": "lykn compile src/",
    "test": "deno test test/",
    "check": "lykn check src/"
  }
}
```

Run tasks with `deno task compile`, `deno task test`, etc. Import maps, compiler options, and permissions can also be configured here.
