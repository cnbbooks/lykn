## What the Reader Doesn't Do

Equally important as what the reader does is what it refuses to do. The reader does not:

- **Know what `bind` means.** It's an atom. Four characters. The reader has no opinion on bindings.
- **Know that `:string` is a type annotation.** It's a keyword node with value `"string"`. What that keyword *does* is someone else's problem.
- **Know that the first element of a list is the operator.** That's a convention the compiler relies on. The reader just sees a list.
- **Know that `console:log` is member access.** It's an atom with a colon in it. The compiler splits it; the reader doesn't.
- **Evaluate anything.** `(+ 1 2)` is not `3` to the reader. It's a list of three things.
- **Report errors about undefined variables.** The analyzer does that.
- **Distinguish surface forms from kernel forms.** The classifier does that.

### Why This Matters

The reader's ignorance is the foundation of everything that follows.

Because the reader doesn't know what forms mean, you can add new forms — `bind`, `func`, `type`, `match` — without changing the reader. The reader for v0.3.0 is the same reader from v0.1.0. It will be the same reader in v1.0.0. S-expressions don't need new grammar rules for new language features.

Because the reader doesn't evaluate, code is data. A macro can receive `(bind x (+ 1 2))` as a list, rearrange its elements, add new elements, wrap it in another list, and return the result — all without the reader knowing or caring. The macro system operates on the reader's output, and the reader's output is just trees.

Because the reader doesn't distinguish surface from kernel, you can mix them freely. Write `(bind x 42)` next to `(class Foo ...)` and the reader produces the same kind of tree for both. The classifier sorts them out later.

This separation — structure from semantics, parsing from compilation, syntax from meaning — is the oldest idea in Lisp and still the most powerful. The syntax hasn't fundamentally changed since McCarthy's 1960 paper, because there's almost nothing to it. And because there's almost nothing to it, everything else can change without disturbing it.
