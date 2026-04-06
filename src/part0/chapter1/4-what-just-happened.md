## What Just Happened?

You have now written Lykn code, compiled it, and run the output. Something happened between the s-expressions you typed and the JavaScript that emerged. This section explains what, at a level sufficient to satisfy curiosity without spoiling the architectural deep-dive in Chapter 2.

### The Pipeline

The Rust compiler processes your code through six stages:

```
.lykn source → reader → expander → classifier → analyzer → emitter → codegen → JavaScript
```

Each stage does one thing and passes its output to the next.

### Stage 1: The Reader

The reader parses your text into a tree of s-expressions. It understands four kinds of things: **atoms** (symbols like `bind`, `console:log`, `+`), **strings** (`"Hello, World!"`), **numbers** (`42`, `3.14`), and **lists** (anything in parentheses). It also understands keywords (`:string`, `:args`, `:body`) — atoms that start with a colon and compile to JavaScript strings.

The reader doesn't know what `bind` means. It doesn't know that `func` is special or that `:string` is a type annotation. It just builds a tree. Meaning comes later.

### Stage 2: The Expander

If your code uses macros — either built-in surface forms or user-defined macros — the expander resolves them. User macros involve a Deno subprocess for evaluation; built-in surface forms are handled by the compiler directly. After expansion, the tree contains only forms the later stages understand.

### Stage 3: The Classifier

The classifier walks the expanded tree and produces a typed surface AST. It dispatches on each form's head symbol — recognizing `bind`, `func`, `type`, `match`, and the rest of the surface vocabulary — and builds a structured representation that the analyzer can reason about.

### Stage 4: The Analyzer

The analyzer performs static checks: building a type registry for algebraic data types, checking `match` exhaustiveness (does every case get handled?), tracking scope for unused bindings and undefined references, and verifying contracts. This is where the surface language earns its safety guarantees.

### Stage 5: The Emitter

The emitter transforms the analyzed surface AST into kernel s-expressions. `bind` becomes `const`. `func` becomes `function` with injected type checks. `match` becomes a chain of `if` tests. `cell` becomes `{ value: x }`. The output is a tree of kernel forms — the s-expression spelling of JavaScript.

### Stage 6: The Codegen

The codegen walks the kernel forms and produces JavaScript text directly. `const` becomes `const x = ...;`. `function` becomes `function f(...) { ... }`. The mapping is mechanical and nearly one-to-one. The codegen is pure Rust with no external dependencies — no AST format, no code generation library, just string building guided by the kernel form structure.

This is why the compiled output looks hand-written — the codegen produces clean, properly indented JavaScript with no transpiler artefacts, no source maps referencing a framework, and no runtime imports.

### The Whole Journey

When you wrote:

```lisp
(bind greeting "Hello, World!")
(console:log greeting)
```

The reader produced a tree: two lists, each containing atoms and a string. The classifier identified `bind` as a surface binding form. The emitter rewrote it as `const`. The codegen produced:

```javascript
const greeting = "Hello, World!";
console.log(greeting);
```

At no point did anything depend on Lykn at runtime. The compiler ran, produced JavaScript, and stepped aside. The output has no imports, no runtime library, no evidence of its parenthetical origins. You could delete the Lykn repository from your machine and the compiled code would continue to run, serenely unaware that it had ever been anything other than JavaScript.

Chapter 2 explores this architecture in detail — the kernel/surface split, why two layers, and what each one knows about the other (which is, by design, very little).
