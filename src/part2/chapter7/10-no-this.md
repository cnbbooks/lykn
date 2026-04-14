## A Note on `this`

The JavaScript developer will notice something missing: `this`.

### The Short Answer

Lykn's surface language has no `this`. The keyword doesn't exist in the surface vocabulary. It was deliberately excluded — DD-15 documents the decision and the rationale.

### The Rationale

`this` binding is the source of BugAID pattern #10 — one of the most frequently reported JavaScript confusions. Extracting a method loses its context: `const fn = obj.greet; fn()` produces `undefined` for `this.name`. Event handlers, callbacks, `setTimeout`, `Promise.then` — all of these silently rebind `this` in ways that surprise even experienced developers.

Lykn eliminates the entire hazard by not providing the form.

### The Escape Hatch

If you need `this` for JS interop — calling a library that expects method-style invocation, working with a framework that binds `this` to components — use kernel forms directly. Inside a `class` body (which is kernel syntax), `this` is available. For standalone functions, `js:bind` binds a function to a specific `this` context. Chapter 14 (JS Interop) covers the details.

### The Alternative

In surface Lykn, the patterns that require `this` in JavaScript — objects with methods that reference their own state — are handled with closures and `obj`. An object with methods that close over shared state is more explicit, more composable, and immune to binding confusion. Chapter 12 (Objects) shows how.
