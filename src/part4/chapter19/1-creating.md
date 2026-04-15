## Creating Arrays

Three ways to create arrays in Lykn.

### Reader Literal: `#a(...)`

The preferred form for literal values:

```lisp
(bind nums #a(1 2 3 4 5))
(bind names #a("Alice" "Bob" "Carol"))
(bind empty #a())
```

```javascript
const nums = [1, 2, 3, 4, 5];
const names = ["Alice", "Bob", "Carol"];
const empty = [];
```

`#a(...)` is a reader-level form (DD-12) — the reader transforms it before the compiler sees it. Clean, concise, no overhead.

### Kernel Form: `(array ...)`

Useful when mixing with `spread`:

```lisp
(bind extended (array 0 (spread existing) 99))
```

```javascript
const extended = [0, ...existing, 99];
```

Both `#a(...)` and `(array ...)` produce `[...]` in JavaScript. Use `#a()` for literal values; use `(array ...)` when constructing with spread or computed elements.

### Utility Constructors

```lisp
(bind from-string (Array:from "hello"))   ;; → ["h", "e", "l", "l", "o"]
(bind explicit (Array:of 1 2 3))          ;; → [1, 2, 3]
```

`Array:from` converts any iterable to an array. `Array:of` creates an array from its arguments (avoids the `new Array(3)` gotcha where a single numeric argument creates a sparse array of that length instead of an array containing that number).

### Type Checking

```lisp
(Array:is-array items)    ;; → Array.isArray(items)
```

This is what Lykn's `:array` type keyword compiles to internally.
