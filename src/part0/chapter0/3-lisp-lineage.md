## The Lisp Lineage

But before we dive into Lykn, a few nods and notes to its other half.

### McCarthy's Nine Operators

John McCarthy did not set out to design a programming language. He set out to axiomatize computation — and accidentally built something you could run on actual hardware, which was roughly as surprising as discovering that your proof of the four-colour theorem could also make toast. His 1960 paper, "Recursive Functions of Symbolic Expressions and Their Computation by Machine," established the first formal specification of what would become Lisp with exactly nine operators.

Five were elementary functions that evaluated their arguments: **ATOM** (test if something is atomic), **EQ** (test equality of atoms), **CAR** (first element of a pair), **CDR** (rest of a pair), and **CONS** (construct a new pair). These handle all data manipulation.

Four were special forms with non-standard evaluation rules: **QUOTE** (prevent evaluation — treat code as data), **COND** (conditional with lazy branch evaluation), **LAMBDA** (function abstraction), and **LABEL** (give a name to a recursive function).

Nine operators. A universal function `eval` that dispatched on them. And a complete, Turing-complete programming language that McCarthy himself described as "a way of describing computable functions *much neater than Turing machines* or the general recursive definitions used in recursive function theory."

Paul Graham later characterized this as discovery rather than design: "It's not something McCarthy designed so much as something he discovered. It's what you get when you try to axiomatize computation."

LABEL was later shown to be unnecessary — D.M.R. Park pointed out it could be achieved using the Y combinator, which reduced the special forms to three. McCarthy had included it for the practical convenience of writing recursive definitions, establishing a pattern that would echo through the next three decades: theoretical minimalism in creative tension with practical utility.

### The Lambda Papers

In 1975, Guy L. Steele Jr. and Gerald Jay Sussman set out to understand Carl Hewitt's Actor model of computation. What they discovered, serendipitously, was that actors and lambda expressions were the same thing.

Their series of MIT AI Memos — published between 1975 and 1979 and known collectively as the Lambda Papers — fundamentally reconceived what counted as primitive in a programming language. "Lambda: The Ultimate Imperative" (1976) articulated the key insight: "The models require only (possibly self-referent) lambda application, conditionals, and (rarely) assignment."

The original Scheme implementation made the hierarchy explicit. Seven forms were **AINTs** — primitive special forms built into the interpreter: `LAMBDA`, `IF`, `QUOTE`, `LABELS`, `ASET'` (assignment), `CATCH` (continuations), and `DEFINE`. Everything else — `COND`, `AND`, `OR`, `BLOCK`, `DO` — was "explicitly not primitive," implemented through macro expansion to the primitive core.

The derivations were elegant. `BLOCK` (sequencing) became nested lambda applications. `OR` became a conditional wrapped in lambdas to avoid evaluating both branches:

```scheme
(OR x . rest) => ((LAMBDA (V R) (IF V V (R))) x (LAMBDA () (OR . rest)))
```

Steele's 1978 RABBIT compiler thesis made this philosophy operational. He wrote: "All of the traditional imperative constructs, such as sequencing, assignment, looping, GOTO, as well as many standard LISP constructs such as AND, OR, and COND, are expressed as macros in terms of the applicative basis set." The compiler treated most of the language as syntactic sugar over a lambda-calculus core — and produced code "as good as that produced by more traditional compilers."

Steele and Sussman later reflected on the experience with characteristic understatement: "This minimalism was the unintended outcome of the design process. We were actually trying to build something complicated and discovered, serendipitously, that we had accidentally designed something that met all our goals but was much simpler than we had intended."

### The Progressive Reduction

What followed was three decades of the Scheme community asking: *how little do you actually need?*

R2RS (1985) first introduced formal "essential" versus "non-essential" categories, establishing a principle that R3RS (1986) sharpened into an explicit structural distinction: **Primitive Expression Types** (Section 4.1) versus **Derived Expression Types** (Section 4.2). The six primitives were variable references, literal expressions, procedure calls, lambda expressions, conditionals, and assignments. Everything else — `cond`, `case`, `and`, `or`, `let`, `let*`, `letrec`, `begin`, `do` — was derived.

R3RS stated it plainly: "By the application of these rules, any expression can be reduced to a semantically equivalent expression in which only the primitive expression types (literal, variable, call, lambda, if, set!) occur."

R4RS (1991) maintained this structure while providing the explicit rewrite rules, noting that derived forms "are redundant in the strict sense of the word, but they capture common patterns of usage, and are therefore provided as convenient abbreviations."

R5RS (1998) reached the definitive formulation: six expression primitives plus three macro-related forms. Fourteen derived forms, all defined as macros in terms of the primitives. The practical minimum for a complete language.

### The Irreducible Five

Theoretical work from the 1980s and 1990s established what truly cannot be derived from anything simpler:

**QUOTE** must be special because it prevents evaluation. A function would evaluate its argument before you could prevent evaluation — the snake eats its own tail. A macro that defines `quote` would need `quote` to return its argument unevaluated. Quote provides the fundamental mechanism for treating code as data, and there is no deeper mechanism from which it can be built.

**LAMBDA** creates closures that capture the lexical environment. It is the primitive binding mechanism; all other binding forms — `let`, `letrec`, every local variable in every language descended from Algol — derive from it. You cannot define lambda in terms of something simpler because it *is* the foundation on which definitions rest.

**IF** must not evaluate both branches. In a language with eager evaluation and side effects, evaluating the branch you didn't choose is not merely wasteful but potentially catastrophic. While Church booleans can encode conditionals in pure lambda calculus, practical programming requires `if` as a primitive.

**SET!** requires access to a variable's *location* in the environment, not its value. A function receives values; mutation requires the address. Assignment needs store semantics beyond pure lambda calculus.

**DEFINE** modifies the environment to create new bindings. It requires privileged access to the definition context that cannot be expressed through ordinary function application.

Five forms. Quote, lambda, if, set!, define. Sixty-six years of refinement, from McCarthy's nine to this. Everything else is syntactic convenience — which is not to diminish it, because syntactic convenience is what separates a language you can *use* from one you merely *admire*.

### A Lisp of Yet Another Flavour

The trajectory from McCarthy to R5RS is a story about discovering how little you need. The trajectory from Scheme to LFE — Lisp Flavoured Erlang — is a story about discovering what you can *do* with that discovery once you stop being precious about your runtime.

Robert Virding created LFE in 2008, and the premise was, on its face, audacious: take Lisp syntax — s-expressions, macros, the whole parenthetical apparatus — and compile it not to its own runtime but to the BEAM, Erlang's virtual machine. The language you *wrote* was a Lisp. The language you *ran* was Erlang. LFE programs had access to OTP supervision trees, hot code loading, distributed message passing, and the full Erlang ecosystem, while the programmer's fingers typed `defmodule` and `defun` and `cond` and `caddr` and felt, unmistakably, the shape of a Lisp beneath them.

The key insight was architectural: LFE did not attempt to *replace* Erlang's semantics. It provided an alternative *syntax* for them. Erlang's pattern matching, its immutable variables, its process model — all of these survived compilation unchanged. LFE was a thin skin. A very good thin skin, with macros and a REPL and all the affordances a Lisper expects, but a thin skin nonetheless. The compiled output was standard BEAM bytecode, indistinguishable from compiled Erlang, with no runtime overhead and no LFE-specific dependencies.

If this sounds familiar, it should.

Lykn applies the same architectural principle to a different host. Where LFE is a Lisp over Erlang's BEAM, Lykn is a Lisp over JavaScript's ESTree. Where LFE preserves Erlang's immutability and pattern matching, Lykn's surface language *introduces* immutability and pattern matching that JavaScript lacks. Where LFE's compiled output is clean BEAM bytecode, Lykn's compiled output is clean JavaScript. The thin-skin philosophy — respect the host, don't reinvent its semantics, provide better syntax and let the programmer keep everything the host already gives them — runs directly from Virding's work into the design decisions documented in this book.

The debt is not merely philosophical. LFE's macro system, its approach to module namespacing, its conviction that a Lisp flavour should feel like a *native* of its host platform rather than a tourist — these shaped Lykn's priorities from the first commit. When Lykn compiles `console:log` to `console.log` using colon syntax instead of inventing its own I/O abstraction, that is LFE's influence. When Lykn uses `func` and `bind` and `match` instead of `defun` and `def` and `case`, preferring short English words to traditional Lisp abbreviations, that is a conscious departure from LFE — but a departure made possible by LFE having already proven that the *important* thing about a Lisp is not its vocabulary but its architecture.

### The Lykn Connection

The Lykn kernel language has approximately thirty forms that map to ESTree nodes — JavaScript's own AST representation. This is a larger set than Scheme's six, because JavaScript is a larger language than Scheme, and a thin skin must follow the contours of what it covers.

But the Lykn surface language sits on top of that kernel. It not only allows for the includsion of ingenious innovations from the likes of Erlang, LFE, and Clouure -- but more to the very core of things, it recapitulates the insight mentioned abouve, one that has driven Lisp for six decades: a small set of primitives, composed through a macro system, can express everything. `bind`, `func`, `fn`, `type`, `match`, `obj`, `cell`, `macro` — eight surface forms, and a macro system that lets you build anything you need from them.

The surface compiler handles safety. The kernel compiler handles JavaScript generation. Neither needs to understand the other's domain. And underneath both, it's the same architecture McCarthy stumbled upon in 1960, the same architecture Steele and Sussman refined in 1975, the same architecture the Scheme reports progressively distilled through 1998: a small core, a macro system, and the conviction that most complexity is an illusion that dissolves when you find the right primitives.
