## Why Build a Language?

Not because JavaScript is bad — but because JavaScript's syntax doesn't enforce the patterns that prevent bugs.

The hazard landscape research (Ch 0, the appendix) showed that specific, known mitigations reduce real-world bug rates:

- Strict equality eliminates coercion bugs (BugAID pattern #4)
- Immutability-by-default eliminates stale closure bugs
- No `this` eliminates binding confusion (BugAID pattern #10)
- Exhaustive `match` catches missing cases (5% of TypeScript projects — Tang et al.)
- Contracts catch invalid inputs (32% of server-side bugs — BugsJS)

These are *known* mitigations with empirical evidence. But JavaScript doesn't enforce any of them. TypeScript helps with some — and even with TypeScript, 12.4% of bugs are type errors.

Lykn's thesis: a thin syntactic layer that enforces these mitigations at compile time, producing the same clean JavaScript a careful developer would write by hand. Not a new language — a new *syntax* for existing semantics.

The "thin skin" philosophy: don't invent new runtime behaviour. Don't add a type system that requires a runtime. Don't create a standard library that must be imported. Just read s-expressions, enforce safety constraints, and emit JavaScript.
