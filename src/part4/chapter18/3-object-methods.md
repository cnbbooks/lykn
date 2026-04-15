## `Object.*` Utility Methods

The JavaScript `Object` namespace provides essential utilities, all accessible via colon syntax.

### Keys, Values, Entries

```lisp
(bind keys (Object:keys user))        ;; → ["name", "age", "active"]
(bind vals (Object:values user))       ;; → ["Duncan", 42, true]
(bind entries (Object:entries user))   ;; → [["name", "Duncan"], ...]
```

Iterate entries with destructuring:

```lisp
(for-of (array key val) (Object:entries user)
  (console:log key val))
```

These return own, enumerable properties only — no inherited properties from the prototype chain.

### `Object:assign` — Copy Properties

```lisp
(bind merged (Object:assign (obj) defaults overrides))
```

`Object:assign` *mutates* its first argument. Pass an empty `(obj)` as the target to avoid mutating `defaults`. In most cases, `assoc` is preferred — it always produces a new object.

### `Object:freeze` — Immutability

```lisp
(bind frozen (Object:freeze (obj :x 1 :y 2)))
```

A frozen object can't have properties added, removed, or changed. But `Object:freeze` is shallow — nested objects are still mutable. For deep immutability, freeze recursively or use a utility.

### `Object:from-entries` — Construct from Pairs

```lisp
(bind obj (Object:from-entries #a(#a("name" "Duncan") #a("age" 42))))
```

The inverse of `Object:entries`. Useful for transforming key-value pairs back into objects.

### `Object:has-own` — Check Own Property

```lisp
(if (Object:has-own user :name)
  (console:log "has name"))
```

Prefer `Object:has-own` over `(in :name user)` — `in` checks the prototype chain, `has-own` checks only the object itself.
