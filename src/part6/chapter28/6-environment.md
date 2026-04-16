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

### `project.json`

Lykn projects use `project.json` for configuration — workspace settings, dependencies, and project metadata. `lykn new` generates this automatically.
