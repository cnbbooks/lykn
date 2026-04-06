## The Kernel: A Thin Skin over JavaScript

The kernel is the Department of JavaScript Compilation. It receives s-expressions and produces JavaScript. It does this with the focused efficiency of a civil servant who has been doing the same job for thirty years and does not intend to learn anything new.

### What the Kernel Knows

Approximately thirty forms, each mapping to one or a few JavaScript constructs. Here are three:

```lisp
;; Kernel: const
(const name "Duncan")
```

```javascript
const name = "Duncan";
```

```lisp
;; Kernel: function declaration
(function greet (name)
  (return (template "Hello, " name "!")))
```

```javascript
function greet(name) {
  return `Hello, ${name}!`;
}
```

```lisp
;; Kernel: colon syntax for member access
(console:log (greet "World"))
```

```javascript
console.log(greet("World"));
```

### What the Kernel Doesn't Know

The kernel has no concept of `bind`. It has never heard of `func`. It does not know what `:string` means in the context of a type annotation. It has no opinion on immutability, no mechanism for pattern matching, and no awareness that algebraic data types exist. If you hand it a `(bind x 42)`, it will not recognise the form and will not compile it.

This is not a limitation. This is the point.

### The Key Decisions

A handful of decisions, made early and maintained since, define the kernel's character:

**Colon syntax** — `console:log` compiles to `console.log`. Colons replace dots for member access. This was the first design decision in the project (DD-01) and it touches every line of Lykn code. The colon was chosen because the dot was needed for other purposes and because `:` reads naturally in a Lisp context, where it already suggests namespacing.

**camelCase conversion** — `my-function` compiles to `myFunction`. Lisp convention uses hyphens; JavaScript convention uses camelCase. The kernel handles the translation automatically. You write in the style natural to s-expressions; the output follows the style natural to JavaScript.

**Three function forms** — `function` for declarations, `lambda` for expressions, `=>` for arrows. Each maps to its JavaScript equivalent. The kernel doesn't prefer one over another — that's a surface-level opinion.

**No implicit return** — Kernel functions require explicit `return` statements, just like JavaScript. The surface language adds implicit returns for convenience; the kernel stays faithful to the host.

### Completeness

The kernel is *complete*. Any JavaScript program can be written in kernel Lykn. Classes, modules, destructuring, async/await, generators, template literals, regular expressions — if JavaScript has it, the kernel can express it. The surface language adds safety and ergonomics, but it does not add capability. Everything the surface can do, the kernel can do — just without the guardrails.

This matters because it means the surface language never needs to invent a new kernel form to support a new feature. `match` compiles to nested `if` statements. `type` compiles to constructor functions. `cell` compiles to `{ value: x }`. The kernel vocabulary is stable, and the surface innovates on top of it without asking the kernel's permission.
