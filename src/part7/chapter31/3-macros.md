## Macro Expansion

The three-pass pipeline (DD-13):

### Pass 0: Import

Scan for `import-macros` declarations. Compile the referenced macro modules to JavaScript. Register exported macros in the macro environment.

### Pass 1: Fixed-Point Expansion

Process each top-level form. If it contains a macro call, expand it. If the expansion introduces new macro calls, expand again. Repeat until no more expansions occur. This is order-independent — a macro defined on line 10 is available on line 1.

### Pass 2: Final Walk

Recursive top-down expansion with a per-node limit to prevent infinite loops.

### How Macros Execute

Macro bodies are compiled to JavaScript and evaluated via `new Function()` — not `import()`. This keeps compilation synchronous: no async pipeline, no Promise-based phases. The macro runs immediately and returns the expansion.

### User-Defined Macros

```lisp
(macro unless (test (rest body))
  `(if (not ,test) (block ,@body)))
```

The macro receives s-expression arguments and returns an s-expression expansion. Quasiquote (`` ` ``), unquote (`,`), and splicing (`,@`) build the template. Enforced gensym (`#` suffix on identifiers) prevents variable capture — accidental hygiene.
