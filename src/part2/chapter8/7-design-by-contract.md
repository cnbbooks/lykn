## Design by Contract: A Brief History

Contracts aren't a Lykn invention. The concept has been refined across three decades and four language families.

### Eiffel (1986)

Bertrand Meyer introduced Design by Contract in Eiffel. Every method has a `require` (precondition) and an `ensure` (postcondition). The class has an `invariant` that holds before and after every method. Violations produce clear errors identifying the broken contract. Meyer's insight: a function is an agreement between caller and implementer, and like any agreement, both parties should know what they're signing.

### Racket

Racket took contracts further with higher-order contract wrapping — checking contracts on functions passed as arguments. If you pass a function that violates the contract when eventually called, the error blames the *passer*, not the callee. Lykn's current contracts are simpler: they fire at the definition site when called, and the stack trace provides blame. Racket-style wrapping is on the roadmap.

### Clojure

Clojure's `clojure.spec` provides composable runtime validation with a `*compile-asserts*` toggle. Specs can generate test data automatically. Lykn's `--strip-assertions` follows this pattern — development-time validation with zero production cost.

### Lykn's Position

Lykn's contracts sit in the proven, boring end of this tradition. Single-expression preconditions and postconditions, blame identification, source expression in error messages, strippable in production. Nothing experimental. Nothing novel. Just the well-tested version of an idea that works.
