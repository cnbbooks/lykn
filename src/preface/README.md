# Preface

This book exists because I wanted to update a website.

That's it. That's the origin story. No grand vision, no manifesto,
no "I shall now design a programming language" moment. I needed
to write some frontend JavaScript for a project, I looked at the
toolchain — TypeScript, webpack, babel, node\_modules, a
`package.json` with forty-seven dependencies for a contact form — and
I thought: there has to be a better way. Or at least a
*different* way. Preferably one with more parentheses.

I'm a Lisper. I've spent years with Common Lisp, Clojure, Scheme,
and LFE — Lisp Flavoured Erlang, a language which Robert Virding created and
to which I am a contributor. In the Lisp world, you write
s-expressions, and the compiler turns them into whatever the host
platform needs. The syntax is simple. The macro system is powerful.
The parentheses are... numerous. But the thing about parentheses is
that once you stop noticing them, you start noticing everything else:
the regularity, the composability, the fact that your code and your
data have the same shape and your editor can manipulate both
structurally. It's a trade, and for me it's always been a good one.

So when I sat down to write JavaScript, my fingers kept reaching for
`(bind x 42)` instead of `const x = 42;`. And I wondered: does
someone already make a thin, lightweight Lisp that compiles to
clean JS?

Turns out ... sort of. I had used BiwaScheme in the past (though I had forgotten the name). Then I found others: Wisp, eslisp, Squint, Fennel
(via Fengari), and half a dozen more. Each occupied a different
point in the design space. None was quite right. BiwaScheme
interprets Scheme in the browser — beautiful, but I wanted
compilation, not interpretation. Wisp had the right philosophy but
was in maintenance mode. eslisp had the right architecture — a thin
s-expression encoding of JavaScript's own AST — but was abandoned
six years ago and only supported ES5. No arrow functions. No
`async`/`await`. No modules.

The tool I wanted didn't exist.

So I built it. In two evenings. And the poetic license of exaggeration. The first night produced a
proof-of-concept: a reader (~90 lines), a compiler (~250 lines), and
astring (a vendored pretty-printer) that together turned
s-expressions into clean, readable JavaScript. The second night
produced five research documents, a name, and packages published to
npm, jsr.io, and crates.io.

---

Lykn is not a replacement for JavaScript. It is a *syntax* for
JavaScript — a thin skin, a symbioitc orgnaism, if you will — that follows the contours of its host.
The compiled output is the same code a careful JavaScript developer
would write by hand. No runtime library. No framework. No
compilation artifacts. Just JavaScript, expressed in s-expressions,
with a few opinions about safety.

Those opinions matter. Lykn defaults to immutability (`bind` is
`const`). It requires type annotations on function parameters
(`:any` is the explicit opt-out). It provides algebraic data types
and exhaustive pattern matching. It eliminates `this` from the
surface language entirely. It wraps mutation in `cell` containers
where every mutation point is marked with `!` — visible, greppable,
intentional.

These aren't arbitrary restrictions. They're responses to
empirical evidence about where JavaScript bugs come from. The
research is in Chapter 0, if you're curious. The short version:
a 2017 study of 3.7 million bug fixes found that 12.4% of
JavaScript bugs are type errors, and that strict equality alone
eliminates an entire category of coercion bugs. Lykn makes the
safe patterns the default and the unsafe patterns the opt-in.

But underneath all the safety machinery, it's still JavaScript.
When you write `(console:log "hello")`, the compiler produces
`console.log("hello")`. When you write `(bind users (await
(fetch "/api/users")))`, the compiler produces `const users =
await fetch("/api/users")`. The parentheses compile away. What
remains is JavaScript that runs everywhere JavaScript runs:
browsers, servers, edge functions, your toaster if it has a
V8 engine.

---

The architecture comes from LFE. Robert Virding's insight —
that a Lisp can be a *thin skin* over a host platform,
respecting the host's semantics while providing better syntax
— is the idea that makes Lykn possible. LFE compiles to
Erlang's BEAM bytecode. Lykn compiles to JavaScript's ESTree
AST. Both produce results that are indistinguishable from hand-written
host-language code. Both give the programmer macros, pattern
matching, and the structural regularity of s-expressions. The
debt is real and gladly acknowledged.

The kernel/surface split is the other key architectural idea.
Lykn has two layers: the **kernel**, which maps s-expression
forms to JavaScript constructs one-to-one (`const`, `function`,
`if`, `class`, `import`), and the **surface**, which adds the
safety features (`bind`, `func`, `type`, `match`, `cell`).
The surface compiler expands surface forms into kernel forms.
The kernel compiler emits JavaScript. The reader doesn't need
to know this — but by the end of the book, they will, because
Part VII opens the hood and shows the whole pipeline.

---

A word about the voice.

This book is not a typical programming manual. It's objectively quirky and empirically silly. The chapters open with spoofs on well-know sketches. These are not mere decoration. Each sketch aims to both dramatise and depressurise the chapter's core technical tension.

We are certain that every attempt at humour in this book, if you look closely enough for for a long enough duration, contains a waft of
technical insight. Every technical insight, if you look even more carefully of have decades of experience in software engineering,
is structured not unlike a joke. A reader who skips every humorous
passage will still learn everything they need. A reader who reads
only the humorous passages will, surprisingly, learn quite a lot.

The intended experience is both at once.

---

This book teaches JavaScript through the lens of Lykn. The
reader will learn both: the surface syntax they write and the
JavaScript semantics underneath. Over 1,500 concepts from four
major JavaScript references have been catalogued, categorized,
and distributed across the chapters that follow. When you learn
`bind`, you learn `const` and `let` — their scoping, their
hoisting, their temporal dead zone. When you learn `func`, you
learn JavaScript functions, closures, and the `this` binding
problem that `func` eliminates by not having `this` at all.

By the end, you'll have built three complete programs: a CLI
tool, an HTTP server, and a browser app. One language, three
platforms. The parentheses compile to semicolons, the semicolons
execute, and the programs run.

Lykn is a young language, so mind the gaps.

And the parentheses.

Duncan McGreggor <br/>
Sleepy Eye, MN <br/>
2026
