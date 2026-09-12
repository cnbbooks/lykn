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

Lykn projects use root `project.json` for workspace imports, dependency pins, and project metadata. Each package keeps package metadata in its own `deno.json`; generated publish metadata is staged under `target/lykn/dist/` by `lykn dist`. `lykn new` creates the root and package files for you.
