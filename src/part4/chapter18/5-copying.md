## Copying Objects

### Shallow Copy

Three equivalent approaches:

```lisp
;; assoc with no overrides (preferred)
(bind copy (assoc original))

;; Kernel spread
(bind copy (object (spread original)))

;; Object.assign
(bind copy (Object:assign (obj) original))
```

All produce `{...original}` — a new object with the same own, enumerable properties.

### Deep Copy

`structured-clone` (modern, built-in):

```lisp
(bind deep (structured-clone original))
```

```javascript
const deep = structuredClone(original);
```

`structured-clone` handles nested objects, arrays, Maps, Sets, Dates, RegExps, and most built-in types. It does *not* copy functions, DOM nodes, or `Error` objects. For those, write a recursive copy or use a library.

### The Shallow Copy Gotcha

Nested objects are shared, not copied:

```lisp
(bind user (obj :name "Duncan" :address (obj :city "London")))
(bind updated (assoc user :age 43))
;; updated.address === user.address — same object!
```

For nested updates, nest `assoc`:

```lisp
(bind moved (assoc user
  :address (assoc user:address :city "Paris")))
```

The outer `assoc` creates a new user. The inner `assoc` creates a new address. Both originals are unchanged. This is the idiomatic Lykn pattern for deep immutable updates — verbose for deeply nested structures, but explicit about what changes and what doesn't.

The reader coming from Clojure may expect persistent data structures with structural sharing. Lykn uses spread-based copies — simpler implementation, same immutability guarantees, but O(n) per update instead of O(log n). For most application code, this is fine. For performance-critical paths with large objects, consider `structured-clone` or mutable buffers via `cell`.
