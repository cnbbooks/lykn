## The Interop Spectrum

Not all code needs the same level of surface safety. A real Lykn project has a spectrum.

### Pure Surface

Data modeling, business logic, algorithms. `type`, `match`, `func`, `bind`, `cell`. Full safety guarantees — type checks, exhaustiveness, immutability. This should be the majority of your code.

### Light Interop

Calling JS APIs with `fn` callbacks. Using colon syntax for method calls. Structural `match` on API responses. Still surface Lykn — just touching JS values that arrived from outside.

### Heavy Interop

Wrapping class-based libraries. DOM manipulation with direct property assignment. Framework integration requiring `this`. Kernel passthrough for classes, `js:bind` for method extraction, compound assignment operators for mutations.

### The Principle

Push as much code as possible toward the pure surface end. Use interop for the boundary — the thin layer where Lykn meets the JS world. Keep the interior functional.

The boundary is visible. `js:` calls and kernel forms stand out in surface code. A code reviewer can spot them. A linter could flag them. The interop boundary is a feature, not a limitation — it tells you exactly where your code touches the unsafe world and where it doesn't.

This is the same principle as Elm's ports, Haskell's IO monad, or Rust's `unsafe` blocks: a safe interior with controlled, marked exits. Lykn's version is lighter — no monad, no type-level enforcement — but the architectural guidance is the same. Safety by default. Escape by choice.
