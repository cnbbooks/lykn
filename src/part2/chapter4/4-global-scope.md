## The Global Scope

Every Lykn program compiles to a JavaScript module (`sourceType: "module"`). This has a practical consequence that's worth understanding: there are no accidental globals.

### Module Scope

Top-level `bind` forms in a Lykn program are module-scoped, not global. They're visible throughout the module but not to other modules (unless explicitly exported) and not as properties on the global object.

```lisp
(bind name "Duncan")       ;; module-scoped, not global
(export (bind version "0.4.0"))  ;; exported, visible to importers
```

In JavaScript terms: the compiled `const name = "Duncan"` at the top of a module is scoped to that module. It's not `globalThis.name`. It's not `window.name`. It's just a local constant that happens to be at the top level.

### Accessing Global APIs

Global APIs — `console`, `Math`, `JSON`, `setTimeout`, `Date` — are simply available, as they are in JavaScript. You don't need to import them:

```lisp
(console:log "hello")           ;; globalThis.console.log
(bind n (Math:floor 3.7))       ;; globalThis.Math.floor
(bind now (Date:now))           ;; globalThis.Date.now
```

### Why This Matters

In pre-module JavaScript, assigning to an undeclared variable in non-strict mode silently created a property on the global object. This was responsible for an entire category of bugs: misspelling a variable name didn't produce an error — it created a new global, which then leaked across the entire runtime.

Module code is always strict. Undeclared variables are always errors. `bind` always emits `const`. Between these three facts, accidental global pollution is impossible in Lykn — not because of any special Lykn mechanism, but because the compilation target (ES modules with `const`) already prevents it.

Under the hood, JavaScript's scope model is implemented via a chain of environment records — lexical environments, declarative records, object records for the global scope. These internals are covered in depth in *Deep JavaScript* for readers who want the full specification-level picture. For working Lykn code, the practical rule is simpler: your bindings are visible where you'd expect them to be, and nowhere else.
