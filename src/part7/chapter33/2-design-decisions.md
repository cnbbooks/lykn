## The Design Decisions That Matter

Every language has a handful of decisions that shape everything downstream. For Lykn, these were:

### S-Expressions as Syntax

The reader is trivial (~320 lines) because s-expressions have no syntactic ambiguity. Macros are natural because code is data. The trade-off: parentheses, and the cultural resistance they provoke. Every developer who sees `(+ 1 2)` for the first time has the same reaction.

### JavaScript as the Target

ESTree provides a well-specified IR. astring (JS) and the Rust codegen provide pretty-printers. The JS ecosystem provides the runtime, the package registry, the deployment infrastructure. The trade-off: inheriting JavaScript's semantics — floating-point only, `typeof null === "object"`, the coercion table.

### Two-Layer Architecture

Kernel maps 1:1 to JavaScript. Surface adds safety. The kernel never changes for surface features. The trade-off: two compilers to maintain, and the surface must express everything in terms of kernel forms. But changes to `match` never break `const` emission.

### Required Type Annotations

Every parameter, every constructor field. `:any` is the opt-out. The trade-off: more typing (literally). But every boundary is checked, and the runtime cost strips in production.

### Immutability by Default

`bind` is `const`. Mutation requires `cell`. The trade-off: `cell`/`express`/`swap!` ceremony for every mutable value. But every mutation point has `!` — visible, greppable, intentional.

### No `this`

The trade-off: classes are kernel passthrough. OOP patterns require dropping to kernel syntax. But the entire `this`-binding hazard category is eliminated.

Each decision has a trade-off. The book has been teaching the decisions. This section names the trade-offs honestly.
