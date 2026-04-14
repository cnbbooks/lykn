## Edge Cases

### Destructuring `null` or `undefined`

Destructuring a non-destructurable value throws a runtime `TypeError` — same as JavaScript:

```lisp
(bind (object name) null)    ;; TypeError at runtime
```

### `rest` Must Be Last

```lisp
;; COMPILE ERROR
(bind (array (rest first) last) items)
```

`rest` collects *remaining* elements. It can only appear at the end of a pattern.

### `_` in Object vs Array Patterns

In array patterns, `_` is a skip marker — it skips a position. In object patterns, `_` is a regular binding name — it extracts a property called `_`. The distinction matters: `(array _ second)` skips the first element, but `(object _)` extracts a property named `_`.

### Empty Patterns

`(bind (object) x)` compiles to `const {} = x` — valid JavaScript, but useless. The compiler allows it without error.
