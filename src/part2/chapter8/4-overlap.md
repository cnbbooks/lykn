## Overlap Is a Compile Error

If two clauses could match the same arguments, the compiler rejects the function. This is not a warning. It is an error.

### What Overlap Looks Like

```lisp
;; COMPILE ERROR: both clauses match (:number)
(func bad
  (:args (:number x)
   :body (* x 2))
  (:args (:number x)
   :body (+ x 1)))
```

```
Error: bad: clauses 1 and 2 overlap — both match (:number)
```

```lisp
;; COMPILE ERROR: :any overlaps with :number
(func also-bad
  (:args (:number x)
   :body (* x 2))
  (:args (:any x)
   :body (console:log x)))
```

```
Error: also-bad: clause 2 (:any) overlaps with clause 1 (:number)
```

`:any` matches everything, including numbers. So clause 2 would match any input that clause 1 matches. The compiler catches this.

### Why Not First-Match-Wins?

Many languages with multi-clause dispatch use first-match-wins: the first clause whose pattern matches gets selected, and the rest are ignored. Erlang does this. Clojure's `defmulti` does this. It works — but it has a cost.

When clause order determines behaviour, *reordering clauses changes semantics*. Move a clause up or down during refactoring and the function silently does something different. The compiler won't warn you. Your tests might not catch it. The bug is invisible until a specific input triggers the wrong clause.

Lykn makes clause order irrelevant by requiring non-overlapping types. If no two clauses can match the same input, the order doesn't matter. Refactoring is safe. The developer's intent is unambiguous.

### Destructured Parameters and Dispatch

Destructured object parameters (Ch 15) have dispatch type `:object`. Destructured array parameters have dispatch type `:array`. Two clauses that both destructure objects at the same position overlap — because dispatch checks `typeof`, not the shape of the object's properties:

```lisp
;; COMPILE ERROR: both clauses accept objects at position 0
(func bad
  (:args ((object :string name))
   :body name)
  (:args ((object :number id))
   :body id))
```

But a destructured object vs a simple `:string` does not overlap — different dispatch types:

```lisp
;; OK: :object vs :string at position 0
(func process
  (:args ((object :string name :string email) :string action)
   :body (template name " — " action))
  (:args (:string raw :string action)
   :body (template raw " — " action)))
```

### The Algorithm

Overlap detection uses Maranget's algorithm (DD-21) — the same framework used for `match` exhaustiveness checking in Chapter 10. It's a well-studied algorithm from the pattern matching literature, applied here to function clause signatures instead of match arms.
