## Logical Operators

Lykn's surface language provides three logical operators: `and`, `or`, and `not`. These compile to JavaScript's `&&`, `||`, and `!`.

### Short-Circuit Evaluation

`and` and `or` are not merely boolean operators — they're control flow. They evaluate their operands left to right and stop as soon as the result is determined:

`and` returns the first falsy value, or the last value if all are truthy:

```lisp
(and user user:name)       ;; → user && user.name
;; If user is null, returns null (doesn't try user:name)
```

`or` returns the first truthy value, or the last value if all are falsy:

```lisp
(bind name (or user-name "Anonymous"))
;; → const name = userName || "Anonymous"
```

`not` inverts truthiness:

```lisp
(not active)               ;; → !active
(not (= x 0))             ;; → !(x === 0)
```

### Variadic Logical Operators

Like arithmetic operators, `and` and `or` accept multiple arguments:

```lisp
(and logged-in verified (not banned))
;; → loggedIn && verified && !banned

(or cached (fetch-from-db) (fetch-from-api) default-value)
;; → cached || fetchFromDb() || fetchFromApi() || defaultValue
```

### Nullish Coalescing

`??` provides a more precise alternative to `or` for default values. It triggers only on `null` or `undefined` — not on `0`, `""`, or `false`:

```lisp
(bind port (?? config-port 3000))
;; → const port = configPort ?? 3000
```

This matters when `0` or `""` are valid values. `(or config-port 3000)` would replace a port of `0` with `3000`. `(?? config-port 3000)` preserves `0` and only falls back for `null`/`undefined`.

### Optional Chaining

JavaScript's `?.` operator (optional chaining) is not currently a surface form in Lykn. For nil-safe property access chains, use `some->` (covered in Chapter 13):

```lisp
(some-> user (get :address) (get :street))
```

This compiles to an IIFE with `== null` checks at each step, providing the same safety as `?.` with more flexibility.
