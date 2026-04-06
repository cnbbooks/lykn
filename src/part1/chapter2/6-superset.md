## Surface Is a Superset

One practical consequence of the two-layer architecture deserves its own section, because it affects how you write code every day: surface Lykn is a superset of kernel Lykn.

### Kernel Forms Work in Surface Code

You can drop a kernel form into a surface program and it compiles without complaint. The surface compiler classifies it as a "kernel passthrough" — it tracks scope but performs no semantic analysis.

```lisp
;; Surface code with a kernel form mixed in
(bind name "Duncan")
(class Greeter ()
  (greet (self)
    (return (+ "Hello, " name))))
```

`bind` is a surface form. `class` is a kernel form. They coexist because the surface compiler knows how to defer to the kernel: if it doesn't recognise a form as surface vocabulary, it passes it through.

### The `js:` Escape Hatch

For cases where you need to bypass a specific surface safety guarantee, the `js:` namespace provides explicit opt-out:

- `(js:eq a b)` — loose equality (`==`) instead of strict (`===`)
- `(js:let x 1)` — a mutable `let` binding, if you truly need one

The `js:` prefix is greppable. A code reviewer searching for `js:` in a project finds every place where the surface safety has been bypassed. The escape hatch exists because no safety system survives contact with the real world unbreached — but it makes every breach visible.

### Why This Matters

The surface doesn't trap you. It *defaults* to safety — immutable bindings, typed parameters, exhaustive matches — and lets you step outside when the situation demands it. The kernel is always there, complete and capable, one prefix away.

This is the architectural payoff of keeping the two layers separate: the surface can be opinionated without being authoritarian, because the kernel provides a well-lit exit.
