## Set

A collection of unique values. Adding a duplicate is a no-op.

### Creation and Basic Operations

```lisp
(bind tags (new Set #a("js" "lykn" "lisp")))
(tags:add "rust")
(tags:add "js")             ;; no-op — already present
(tags:has "lykn")            ;; → true
(tags:delete "lisp")         ;; → true
tags:size                    ;; → 3
```

### Removing Duplicates

The classic one-liner:

```lisp
(bind unique (Array:from (new Set items)))
;; or
(bind unique (array (spread (new Set items))))
```

### Set Operations (ES2025)

Proper set algebra — check Deno's current support:

```lisp
(bind a (new Set #a(1 2 3 4)))
(bind b (new Set #a(3 4 5 6)))

(a:union b)                  ;; Set { 1, 2, 3, 4, 5, 6 }
(a:intersection b)           ;; Set { 3, 4 }
(a:difference b)             ;; Set { 1, 2 }
(a:symmetric-difference b)   ;; Set { 1, 2, 5, 6 }
(a:is-subset-of b)           ;; false
```

Twenty-five years of JavaScript without set algebra, and now it's built in.

### Iteration

Sets are iterable:

```lisp
(for-of tag tags
  (console:log tag))
```

### Element Equality

Sets use *same-value-zero* equality — like `===` but treats `NaN` as equal to `NaN`. Objects are compared by reference, not structure: two objects with identical properties are still two distinct Set elements.
