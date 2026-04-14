## Exhaustiveness: The Safety Guarantee

Non-exhaustive `match` is a compile error. Not a warning. Not a linter suggestion. An error that prevents compilation.

### The Rules

**ADT matches**: every variant must be covered, either explicitly or by `_`:

```lisp
;; COMPILE ERROR: non-exhaustive — missing None
(match opt
  ((Some v) v))
```

**Literal matches on open types**: `_` is required — the compiler can't enumerate every possible number or string:

```lisp
;; COMPILE ERROR: no wildcard for open type
(match status
  (200 "ok")
  (404 "not found"))
```

**Boolean matches**: `true` + `false` = exhaustive. No `_` needed.

**Guards make clauses partial**: a guarded clause doesn't count toward coverage for its variant.

**Nested ADTs**: the compiler tracks all combinations. If you match `(Ok (Some v))` and `(Err e)`, you've missed `(Ok None)`.

### The Escape Hatch

If you genuinely want partial handling, make the crash explicit:

```lisp
(match status
  (200 (process-ok))
  (404 (not-found))
  (_ (throw (new Error (template "unexpected status: " status)))))
```

The crash isn't hidden in a silent fall-through. It's visible in the source, greppable in code review, and intentional. The developer chose to crash on unexpected values — they didn't *forget* to handle them.

### The Algorithm

The compiler uses Maranget's algorithm — the same framework used by Rust and OCaml — to verify that every possible value is covered. It's the same algorithm that checks `func` clause overlap in Chapter 8. One pattern analysis engine, two consumers: `match` for exhaustiveness, `func` for non-overlap.

### Why It Matters

Elm and Rust treat exhaustiveness checking as one of their most valued features. Tang et al. found missing-case bugs in 5% of TypeScript projects — bugs that would have been compile errors with exhaustive matching. Every `switch` in JavaScript that's missing a `default` is a potential bug. Every `if`/`else` chain that doesn't handle a case is a potential crash. `match` makes these impossible.

The Bridgekeeper doesn't ask questions to be cruel. The Bridgekeeper asks questions because the Gorge is real, and the answers matter.
