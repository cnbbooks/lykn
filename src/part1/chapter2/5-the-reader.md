## The Reader: Structure, Not Semantics

Beneath both compilers — shared by kernel and surface, by Rust pipeline and browser bundle alike — sits the reader. It is the most stable component in the system and the least interesting, which is exactly how infrastructure should be.

### Five Node Types

The reader understands five kinds of things:

1. **Atom** — a symbol name: `bind`, `console:log`, `my-function`, `+`
2. **String** — a quoted string: `"Hello, World!"`
3. **Number** — a numeric literal: `42`, `3.14`, `1e6`
4. **List** — a parenthesized group: `(bind x 42)`, `(+ 1 2 3)`
5. **Keyword** — a colon-prefixed atom: `:name`, `:string`, `:args`

That is the entire syntax of Lykn. Five node types. No operator precedence. No statement-vs-expression distinction. No semicolons, no commas, no curly braces. Lists containing atoms, strings, numbers, keywords, and other lists, all the way down.

### What the Reader Doesn't Know

The reader doesn't know that `bind` creates an immutable binding. It doesn't know that `:string` is a type annotation. It doesn't know that `(func ...)` is a function definition or that `(+ 1 2)` is addition. It sees *structure* — which things are grouped with which other things — and nothing else. All meaning is assigned later, by whichever compiler processes the tree.

This is the Lisp insight, and it is the reason s-expressions have survived for sixty-six years while syntax fashions have come and gone: by separating structure from semantics, you make the language infinitely extensible without changing the parser. Adding `match` to Lykn didn't require a new grammar rule. Adding `type` didn't require a new parser state. The reader is the same reader it was in v0.1.0 — it just reads trees, and the trees can contain anything.

### Dispatch Syntax

The reader does handle one piece of sugar: the `#` dispatch character, which provides literal syntax for common data structures:

- `#a(1 2 3)` — array literal → `[1, 2, 3]`
- `#o((name "x") (age 42))` — object literal → `{name: "x", age: 42}`
- `#16rff` — radix literal → `255`
- `#;` — expression comment (discards the next form)
- `` #| ... |# `` — nestable block comment

These are reader-level transformations. By the time the compiler sees the tree, `#a(1 2 3)` has already become a list tagged as an array literal. The compiler doesn't know — or need to know — how the reader produced it.
