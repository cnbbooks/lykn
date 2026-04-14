## Assignment and Update Operators

In surface Lykn, `bind` is immutable. So who's doing assignment?

### Where Assignment Appears

Assignment is a kernel-level operation. It appears in Lykn code in three contexts:

1. **Inside cell expansions**: `swap!` and `reset!` compile to assignments on the cell's `.value` property. You write surface forms; the compiler writes the assignment.

2. **Kernel passthrough code**: When you use kernel forms directly — inside a `class` body, for JS interop, or when surface forms don't cover your use case.

3. **DOM and API interop**: Setting properties on browser objects, response headers, or other mutable JS APIs.

```lisp
;; Cell mutation (surface) — you write this
(swap! counter (fn (:number n) (+ n 1)))

;; The compiler produces this (kernel-level assignment)
;; counter.value = ((n) => ...)(counter.value)
```

### Compound Assignment

For kernel/interop contexts, compound assignment operators are available:

| Lykn | JS |
|---|---|
| `(+= x 1)` | `x += 1` |
| `(-= x 1)` | `x -= 1` |
| `(*= x 2)` | `x *= 2` |
| `(/= x 2)` | `x /= 2` |
| `(%%= x 3)` | `x %= 3` |
| `(**= x 2)` | `x **= 2` |

Logical assignment operators:

| Lykn | JS | Behaviour |
|---|---|---|
| `(&&= x val)` | `x &&= val` | Assign if `x` is truthy |
| `(\|\|= x val)` | `x \|\|= val` | Assign if `x` is falsy |
| `(??= x val)` | `x ??= val` | Assign if `x` is null/undefined |

### Update Operators

Prefix increment and decrement:

```lisp
(++ counter)          ;; → ++counter
(-- remaining)        ;; → --remaining
```

Lykn only supports the prefix form — `++x`, not `x++`. This was a deliberate design choice: the difference between prefix and postfix increment is a perennial source of bugs, and prefix is the more predictable behaviour (increment, then return the new value).

### The Practical Reality

In pure surface Lykn, you almost never write assignment directly. `swap!` and `reset!` handle cell mutation. `assoc` and `dissoc` produce new objects. Threading macros transform values through pipelines. Direct assignment is the escape hatch for JS interop — and like all escape hatches, it should be visible and rare.
