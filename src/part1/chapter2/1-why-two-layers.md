## Why Two Layers?

Here is the problem. JavaScript has well-documented hazards — type coercion that violates transitivity, a `this` keyword whose binding depends on how a function is called rather than how it is defined, implicit global variables, and a null dereference pattern so pervasive that it constitutes the single largest bug category in empirical studies. You know this. Chapter 0 covered it.

### The Monolithic Temptation

The obvious solution is to build a compiler that fixes everything: a language with s-expression syntax, immutable bindings, typed parameters, exhaustive pattern matching, contracts, and threading macros, all compiled to JavaScript. One compiler. One pass. One giant ball of mutual dependencies where every safety feature is tangled with every code generation decision.

This is how languages die. Not from a lack of features, but from the impossibility of changing any one feature without disturbing all the others. Add a new pattern matching form and the code generator needs updating. Change how `const` is emitted and the type checker breaks. The compiler becomes a monolith — not in the architectural sense, but in the geological one: large, immovable, and of interest primarily to future archaeologists.

### The Separation

Lykn takes a different approach. It separates the problem into two layers, each of which solves exactly one half:

**The kernel** knows JavaScript. It translates s-expressions into JavaScript source code. It is thin, stable, and unopinionated. It does not know what `bind` is. It does not care about type annotations. It speaks `const`, `function`, `if`, `import`, `class`, and roughly twenty-five others — the s-expression spelling of JavaScript's own constructs. If you change how `match` works in the surface language, the kernel doesn't notice.

**The surface** knows safety. It translates developer-friendly forms into kernel forms. It handles type checking, exhaustiveness analysis, contracts, and immutability enforcement. It does not know how JavaScript is generated. It does not care about semicolons or operator precedence. It speaks `bind`, `func`, `type`, `match`, `cell`, and `obj`. If you change how `const` is emitted in the kernel, the surface doesn't notice.

### Precedent

This is not a novel architecture. It is, in fact, the standard architecture for serious compilers — just made explicit:

- Haskell compiles its surface syntax to **Core** (System FC), a tiny typed lambda calculus. Core compiles to STG, then to C--.
- Racket distinguishes **user-facing language** from **fully expanded programs**. The expander reduces surface syntax to a core the compiler understands.
- Scheme itself, as Chapter 0 explored, distinguishes **derived expression types** from **primitive expression types**. `let` is surface; `lambda` is kernel.

What makes Lykn's version distinctive is that both layers are *named*, *documented*, and *independently useful*. You can write kernel Lykn directly when you need low-level control. You can inspect the kernel output of any surface program. The boundary isn't hidden inside the compiler — it's a feature you can see and use.
