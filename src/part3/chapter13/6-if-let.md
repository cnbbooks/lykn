## Conditional Binding: `if-let` and `when-let`

Pattern-based conditional binding. Bind a value and branch based on whether a pattern matches. Uses the same pattern system as `match` (Ch 10).

### `if-let` — With an Else Branch

```lisp
(if-let ((Some user) (find-user id))
  (greet user)
  (redirect-to-login))
```

```javascript
{
  const t__gensym0 = findUser(id);
  if (t__gensym0.tag === "Some") {
    const user = t__gensym0.value;
    greet(user);
  } else {
    redirectToLogin();
  }
}
```

### `when-let` — No Else Branch

```lisp
(when-let ((Ok data) (fetch-data url))
  (process data))
```

If the pattern doesn't match, nothing happens. No else branch, no fallback.

### Three Pattern Types

**ADT constructor** — PascalCase triggers constructor matching:

```lisp
(if-let ((Some v) (find id))
  (use v)
  (fallback))
```

**Simple binding** — lowercase triggers nil check:

```lisp
(if-let (config (load-config))
  (start-with config)
  (start-default))
```

This binds `config` if `(load-config)` is not null/undefined. PascalCase distinguishes constructors from simple bindings: `Some` checks `.tag`, `config` checks `!= null`.

**Structural** — `obj` pattern checks properties:

```lisp
(if-let ((obj :data d) response)
  (process d)
  (handle-error response))
```

### The Convenience

`if-let` is a convenience over `match` for the common pattern of "unwrap or fallback." For complex multi-way dispatch, use full `match`. For quick one-pattern checks, `if-let` reads cleaner.
