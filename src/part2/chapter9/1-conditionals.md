## Conditionals: `if`

The most fundamental control flow form. Lykn's `if` is a kernel form that maps directly to JavaScript's `if` statement.

### Simple `if`

```lisp
(if (> temperature 100)
  (console:log "boiling"))
```

```javascript
if (temperature > 100) {
  console.log("boiling");
}
```

### `if`-`else`

```lisp
(if (>= age 18)
  (console:log "adult")
  (console:log "minor"))
```

```javascript
if (age >= 18) {
  console.log("adult");
} else {
  console.log("minor");
}
```

The second argument is the then-branch; the third is the else-branch. No `else` keyword — the structure tells you which is which.

### Nested `if` (and Why You'll Want `match`)

```lisp
(if (= status 200)
  (process-response data)
  (if (= status 404)
    (not-found)
    (server-error status)))
```

This works but reads poorly. Each nested level adds indentation and cognitive load. Chapter 10 introduces `match`, which handles multi-way dispatch with exhaustiveness checking:

```lisp
;; Preview — covered fully in Ch 10
(match status
  (200 (process-response data))
  (404 (not-found))
  (_ (server-error status)))
```

When you find yourself nesting `if` more than two levels deep, `match` is almost certainly the better tool.

### No `cond`, No `when`

Lykn's surface language doesn't provide `cond` (multi-branch conditional) or `when` (one-branch conditional without else). For multi-branch, use `match`. For conditional execution without an else, use `if` without a third argument. For conditional binding, use `if-let` or `when-let` (Chapter 13).
