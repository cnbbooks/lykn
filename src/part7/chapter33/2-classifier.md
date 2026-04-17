## The Classifier

The classifier turns the reader's generic s-expression tree into a *typed* surface AST. It dispatches on the head symbol of each list:

```text
(func add ...)    → SurfaceForm::Func { name, clauses, ... }
(bind x 42)       → SurfaceForm::Bind { name, type_ann, value, ... }
(match opt ...)   → SurfaceForm::Match { target, clauses, ... }
(type Option ...) → SurfaceForm::Type { name, constructors, ... }
(-> x (+ 3))     → SurfaceForm::ThreadFirst { initial, steps, ... }
```

If the head symbol isn't a known surface form, the classifier checks if it's a kernel form. If so, it creates `SurfaceForm::KernelPassthrough` — the surface compiler passes it through without analysis (Ch 14).

### Why Classify?

The reader's output is untyped — `bind`, `func`, `if`, and `console:log` are all atoms. The classifier adds structure. It knows that `func` has `:args`, `:returns`, `:pre`, `:post`, `:body` keywords. It parses typed parameter lists (including destructuring patterns from DD-25). It detects single-clause vs multi-clause dispatch.

Without classification, the emitter would have to re-parse every form from raw s-expressions. The classifier does it once, producing a strongly-typed Rust enum that the analysis and emission phases consume.
