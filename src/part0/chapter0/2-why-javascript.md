## Why JavaScript?

Of all the languages one might choose as a compilation target — and there are, at last count, rather a lot of them — JavaScript occupies a position unique in the history of computing. It is the only language that runs, without installation, in every web browser on every device on earth. It runs on servers via Node.js, Deno, and Bun. It runs on edge functions at Cloudflare, AWS Lambda, and GCP Whatsit. It runs, in a pinch, on microcontrollers. Brendan Eich created it in ten days in May 1995 as a glue language for Java applets, and it has since achieved the kind of ubiquity that empires dream about and plumbing has already attained.

JavaScript is, in other words, the world's most successful accident.

### Influences

Its influences read like a guest list for a very eclectic dinner party: syntax from Java (by executive decree — Netscape management required it to *look* like Java, regardless of what it actually *did*), prototypal inheritance from Self, closures from Scheme, string handling from Perl, and event-driven programming from HyperTalk. The result is a language of extraordinary versatility and occasionally breathtaking incoherence. It is multi-paradigm in the way that a Swiss Army knife is multi-tool: everything works, nothing is entirely comfortable, and there's always a surprising attachment you didn't know was there.

### Semantics

But incoherence is not the same as incompetence. JavaScript's semantics — the actual computational model beneath the syntax — are surprisingly sound. First-class functions, lexical closures, a flexible object system, and an event loop that handles concurrency without threads. Modern JavaScript, post-ES2015, has `let` and `const` for proper scoping, arrow functions for lexical `this`, destructuring, modules, generators, `async`/`await`, and optional chaining. The TC39 committee has spent two decades methodically addressing the language's worst footguns through annual specification releases, each one field-tested through a rigorous multi-stage proposal process before ratification.

### Issues

The problems that remain are real, but they are concentrated. Empirical research tells a consistent story. Hanam et al.'s BugAID tool, mining 105,133 commits from 134 Node.js projects, found that *dereferenced non-values* — the `undefined is not a function` family — constitute the single largest bug pattern. Pradel and Sen's dynamic analysis of 138.9 million runtime events found that 98.85% of JavaScript's implicit type coercions are harmless, but the remaining 1.15% cluster into five specific patterns that account for a disproportionate share of real bugs: non-strict equality between different types, string concatenation with `undefined`, arithmetic on non-numbers, incomparable relational comparisons, and wrapped primitives in conditionals. Gao et al. demonstrated that type systems — both Flow and TypeScript — catch exactly 15% of real JavaScript bugs. The other 85% resist type-level detection entirely.

### And So

The language, in other words, is not dead. It is genuinely resting. But it is resting on a bed of implicit coercions and lost `this` bindings, and it could use, at the very least, a better perch.
