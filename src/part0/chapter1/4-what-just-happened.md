## What Just Happened?

You have now written Lykn code, compiled it, and run the output. Something happened between the s-expressions you typed and the JavaScript that emerged. This section explains what, at a level sufficient to satisfy curiosity without spoiling the architectural deep-dive in Chapter 2.

### The Pipeline

Lykn compilation is a four-stage pipeline:

```
.lykn source → reader → surface compiler → kernel compiler → JavaScript
```

Each stage does one thing and passes its output to the next.

### Stage 1: The Reader

The reader parses your text into a tree of s-expressions. It understands four kinds of things: **atoms** (symbols like `bind`, `console:log`, `+`), **strings** (`"Hello, World!"`), **numbers** (`42`, `3.14`), and **lists** (anything in parentheses). It also understands keywords (`:string`, `:args`, `:body`) — atoms that start with a colon and compile to JavaScript strings.

The reader doesn't know what `bind` means. It doesn't know that `func` is special or that `:string` is a type annotation. It just builds a tree. Meaning comes later.

### Stage 2: The Surface Compiler

The surface compiler takes the reader's tree and transforms surface forms into kernel forms. When it sees `(bind x 1)`, it emits `(const x 1)`. When it sees `(func greet :args (:string name) ...)`, it emits a `(function greet (name) ...)` with type-checking code injected.

This is where safety lives. The surface compiler inserts `typeof` checks for type annotations, generates exhaustive if-chains for `match` expressions, wraps `cell` containers in `{ value: x }` objects, and transforms threading macros into nested function calls. Everything the surface language promises — immutability, type safety, pattern matching — is implemented here, by rewriting surface forms into kernel forms that the next stage can handle.

### Stage 3: The Kernel Compiler

The kernel compiler takes kernel forms — `const`, `function`, `if`, `import`, and roughly twenty-seven others — and transforms them into ESTree nodes. ESTree is the standard AST (Abstract Syntax Tree) format for JavaScript, used by tools like ESLint, Prettier, and Babel. Each kernel form maps to one or more ESTree node types. `const` becomes a `VariableDeclaration`. `function` becomes a `FunctionDeclaration`. `if` becomes an `IfStatement`. The mapping is mechanical and nearly one-to-one.

### Stage 4: astring

The ESTree AST is handed to [astring](https://github.com/davidbonnet/astring), an open-source JavaScript code generator that pretty-prints AST nodes into formatted source code. This is why the compiled output looks hand-written — astring produces clean, properly indented JavaScript with no transpiler artefacts, no source maps referencing a framework, and no runtime imports.

### The Whole Journey

When you wrote:

```lisp
(bind greeting "Hello, World!")
(console:log greeting)
```

The reader produced a tree: two lists, each containing atoms and a string. The surface compiler saw `bind` and emitted `const`. The kernel compiler turned `const` into a `VariableDeclaration` ESTree node and the function call into a `CallExpression`. astring printed:

```javascript
const greeting = "Hello, World!";
console.log(greeting);
```

At no point did anything depend on Lykn at runtime. The compiler ran, produced JavaScript, and stepped aside. The output has no imports, no runtime library, no evidence of its parenthetical origins. You could delete the Lykn repository from your machine and the compiled code would continue to run, serenely unaware that it had ever been anything other than JavaScript.

Chapter 2 explores this architecture in detail — the kernel/surface split, why two layers, and what each one knows about the other (which is, by design, very little).
