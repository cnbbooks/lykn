## What Is lykn?

lykn is a Lisp that compiles to JavaScript. Not a subset of JavaScript, not a framework, not a transpiler with opinions about semicolons — a *Lisp*. S-expressions in, clean JavaScript out. The compiled output has no runtime, no dependencies, no evidence that a Lisp was ever involved except for a certain suspicious elegance in the variable naming and an absence of `var`.

Here is a lykn program:

```lisp
(func greet
  :args (:string name)
  :returns :string
  :body (+ "Hello, " name "!"))

(bind result (greet "world"))
(console:log result)
```

Here is what the compiler produces:

```javascript
function greet(name) {
  if (typeof name !== "string")
    throw new TypeError(
      "greet: arg 'name' expected string, got " + typeof name);
  const result__gensym0 = "Hello, " + name + "!";
  if (typeof result__gensym0 !== "string")
    throw new TypeError(
      "greet: return 'result__gensym0' expected string, got "
      + typeof result__gensym0);
  return result__gensym0;
}
const result = greet("world");
console.log(result);
```

That's it. That is the entire transaction. You write s-expressions with type annotations; you get JavaScript that a fastidious human might have written by hand, had that human been raised in an environment where runtime type checking was considered a basic social courtesy rather than an optional extra.

The type annotations — `:string` on the parameter, `:returns :string` on the function — compile to runtime `typeof` checks in development. In production, you pass `--strip-assertions` and they vanish, leaving behind nothing but the clean function. Contracts without consequences, if you prefer. Or consequences without contracts, depending on your build flag.

lykn has two layers, and understanding them is the key to understanding everything else in this book.

**lykn/kernel** is the lower layer: approximately thirty forms that map one-to-one to JavaScript's own constructs. `const`, `function`, `lambda`, `=>`, `if`, `import`, `class` — these are the kernel. They are the s-expression spelling of JavaScript's AST, and the compiler translates them to ESTree nodes with the serene indifference of a very precise dictionary. If you write kernel syntax, you are writing JavaScript with different punctuation. Nothing more.

**lykn/surface** is what you actually use. It sits on top of the kernel and provides the things JavaScript was too polite to insist upon: immutable bindings via `bind` (which compiles to `const` and does not have a mutable cousin), typed functions via `func` (with contracts, pattern-based dispatch, and the aforementioned type checks), algebraic data types via `type`, exhaustive pattern matching via `match`, controlled mutation via `cell` containers, and threading macros that let you write data transformation pipelines without nesting your code to the point where it begins to resemble a geological formation.

Surface forms compile to kernel forms. Kernel forms compile to JavaScript. At no point does anything magical happen — the magic, such as it is, lies in the *absence* of magic. The compiled output is readable. Debuggable. Ordinary. The sort of JavaScript you would write yourself, if you had infinite patience and a deep personal commitment to `const`.
