## Shadowing

An inner `bind` can use the same name as an outer binding. The inner one *shadows* the outer one — within its scope, the inner binding wins:

```lisp
(bind x 10)

(func double-it
  :args (:number x)        ;; shadows outer x
  :returns :number
  :body (* x 2))           ;; refers to the parameter, not outer x

(console:log (double-it 5))  ;; → 10
(console:log x)              ;; → 10 — outer x unchanged
```

### When Shadowing Is a Problem

Shadowing is sometimes intentional — a function parameter naturally has the same name as something in the outer scope. But it's often accidental: you meant to use the outer `x` and didn't notice that the inner scope had its own.

The Lykn analyzer emits a warning (not an error) for shadowed bindings. Warnings appear during compilation and don't prevent output, but they signal that you should double-check your intention.

### The `_` Convention

Names prefixed with `_` are exempt from unused-binding warnings — this is the standard convention for values you need to destructure but don't intend to use. Shadowing warnings still apply to `_`-prefixed names, though, because shadowing is about *ambiguity*, not about whether the binding is used.
