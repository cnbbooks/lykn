## Guards: `:when` Clauses

Guards add conditions beyond pattern shape:

```lisp
(match temperature
  (n :when (> n 100) "boiling")
  (n :when (< n 0) "freezing")
  (_ "moderate"))
```

The guard `:when (> n 100)` is an additional check — the pattern `n` matches any value, but the body only runs if the guard is also true.

### Guards Make Clauses Partial

A guarded clause does not satisfy exhaustiveness for its pattern. This is the critical rule:

```lisp
;; COMPILE ERROR: guarded Some is partial, no unguarded Some
(match opt
  ((Some v) :when (> v 0) (use v))
  (None (fallback)))
```

The compiler rejects this — `(Some v) :when (> v 0)` only handles *some* `Some` values (the positive ones). What about negative ones? Zero? The guard makes the clause partial, and a partial clause doesn't count toward exhaustiveness.

### The Fix

Either add an unguarded clause for the same variant, or use `_` to catch everything else:

```lisp
;; OK: unguarded Some catches the rest
(match opt
  ((Some v) :when (> v 0) (use-positive v))
  ((Some v) (use-nonpositive v))
  (None (fallback)))

;; Also OK: wildcard catches everything else
(match opt
  ((Some v) :when (> v 0) (use-positive v))
  (_ (fallback)))
```

Guards are for refining a pattern, not replacing exhaustiveness. The compiler insists that every case is handled — guards just let you handle the same case differently depending on a condition.
