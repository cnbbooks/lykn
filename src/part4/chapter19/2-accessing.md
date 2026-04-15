## Accessing Elements

### By Index

```lisp
(get items 0)                        ;; → items[0]
(get items (- items:length 1))       ;; last element
```

`get` with a numeric index compiles to bracket access. Colon syntax (`items:0`) doesn't work — colons expect property names, not numeric indices.

### `.at()` — Negative Indices

```lisp
(items:at -1)                        ;; → items.at(-1) — last element
(items:at -2)                        ;; → items.at(-2) — second to last
```

`.at()` (ES2022) supports negative indices, counting from the end. Cleaner than `(get items (- items:length 1))`.

### Length

```lisp
items:length                         ;; → items.length
```

### Searching

```lisp
(items:includes "Alice")             ;; → items.includes("Alice")
(items:index-of "Bob")               ;; → items.indexOf("Bob")  (-1 if not found)
```

Note: `includes` uses `SameValueZero` comparison (handles `NaN` correctly). `index-of` uses `===` (cannot find `NaN`).
