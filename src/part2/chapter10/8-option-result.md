## `Option` and `Result`: The Prelude Types

`Option` and `Result` are defined in `lykn/core` and auto-imported into every module. No explicit `import` needed — they're available from the first line.

### `Option` Replaces Nullable Values

```lisp
(func find-user
  :args (:string id)
  :returns :any
  :body
  (bind user (db:get id))
  (if user (Some user) None))
```

The caller must handle both cases:

```lisp
(match (find-user "abc")
  ((Some user) (greet user))
  (None (console:log "not found")))
```

No truthiness ambiguity. `(Some 0)` is a valid `Some` — zero is a value, not an absence. `(Some "")` is a valid `Some` — an empty string is a value, not nothing. The `None` case is the *only* case that means "no value."

### `Result` Replaces Try/Catch for Expected Failures

```lisp
(func parse-port
  :args (:string input)
  :returns :any
  :body
  (bind port (Number input))
  (if (Number:is-NaN port)
    (Err "not a number")
    (Ok port)))
```

The caller handles success and failure explicitly:

```lisp
(match (parse-port "8080")
  ((Ok p) (console:log "port:" p))
  ((Err e) (console:log "error:" e)))
```

No catch-everything problem. `Ok` means the operation succeeded. `Err` means it failed in an expected way. If something *unexpected* happens — a bug, a null dereference, resource exhaustion — that's still an exception. `Result` is for failures you can enumerate; exceptions are for failures you can't.

### The Distinction

**Exceptions** are for *unexpected* failures — bugs, runtime errors, resource exhaustion. They unwind the stack. They're caught by `try`/`catch`. You don't enumerate them because you can't predict them.

**`Result`** is for *expected* failures — invalid input, file not found, authentication failed. They flow through normal returns. You handle them with `match`. You enumerate them because they're part of the function's contract.

This is a Rust pattern that Lykn adopts. It's a design opinion, not a universal truth. But it pays off: when `Result` handles the expected cases, `try`/`catch` only catches genuine bugs — and catching bugs is what `try`/`catch` was designed for.

### Blessed Types

The compiler recognizes `Option` and `Result` by their prelude definitions and provides enhanced error messages. If you forget to handle `None`, the error says:

```
non-exhaustive match on Option — missing None
```

Not the generic "missing variant" — the specific type and the specific variant you forgot. This is a small thing, but in a large codebase, specific errors save hours.

For quick `Option`/`Result` unwrapping without a full `match`, see `if-let` and `when-let` in Chapter 13.
