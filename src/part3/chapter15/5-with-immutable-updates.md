## Destructuring and Immutable Updates

Destructuring (taking apart) and `assoc`/`dissoc`/`conj` (putting together differently) are complementary tools. Both are immutable operations — neither mutates the original.

### Extract, Transform, Reassemble

```lisp
(bind (object name age) user)
(bind updated (obj
  :name (name:to-upper-case)
  :age (+ age 1)))
```

Destructuring extracts the parts; `obj` builds a new object from transformed parts. The original `user` is unchanged.

### `assoc` Preserves What You Don't Touch

```lisp
(bind updated (assoc user :name (user:name:to-upper-case)))
```

`assoc` (Ch 13) produces a shallow copy with overrides. Properties you don't mention are preserved. Destructuring + `obj` builds from scratch; `assoc` copies and modifies. Choose based on whether you want to keep the other properties.

### The Pattern

The idiomatic flow in surface Lykn:

1. **Destructure** — extract the parts you need
2. **Transform** — apply functions to the extracted values
3. **Reassemble** — build a new value with `obj` or `assoc`

No mutation at any step. The original value survives. The new value has the changes. The functional update pattern, expressed through s-expressions.
