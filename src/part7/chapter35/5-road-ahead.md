## The Road Ahead

What Lykn doesn't have yet, honestly:

- **Self-hosting** — the compiler is Rust and JavaScript, not Lykn. Self-hosting requires a stable macro system and surface syntax. It's on the horizon.
- **LSP/editor support** — language server protocol for autocompletion, go-to-definition, inline errors. The modular compiler architecture (Ch 33) is designed to support this.
- **Ecosystem** — packages written in Lykn, a community, documentation beyond this book.
- **Gradual type system** — Coalton-inspired type inference with JSDoc output. Deferred to v0.4.0+.
- **Condition/restart system** — Common Lisp's three-layer error handling. Deferred to v0.4.0+.

The language is real, the compiler works, and the book exists. The road ahead is about community and tooling, not fundamental design — the design decisions are settled. The DDs document them. The tests verify them. The two compilers agree on them.

What remains is for developers to write Lykn, discover what works and what doesn't, and shape the language through use. That's what programming languages do — they evolve through contact with real problems. This book taught the language as it is. The next version will be shaped by the people who use it.
