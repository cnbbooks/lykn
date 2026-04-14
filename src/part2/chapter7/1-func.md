## `func`: Named Functions

`func` is Lykn's primary function form. It uses keyword-labeled clauses — `:args`, `:returns`, `:body` — that make the function's contract visible at a glance.

### The Basics

```lisp
(func add
  :args (:number a :number b)
  :returns :number
  :body (+ a b))
```

```javascript
function add(a, b) {
  if (typeof a !== "number" || Number.isNaN(a))
    throw new TypeError("add: arg 'a' expected number, got " + typeof a);
  if (typeof b !== "number" || Number.isNaN(b))
    throw new TypeError("add: arg 'b' expected number, got " + typeof b);
  const result__gensym0 = a + b;
  if (typeof result__gensym0 !== "number" || Number.isNaN(result__gensym0))
    throw new TypeError("add: return value expected number, got " + typeof result__gensym0);
  return result__gensym0;
}
```

With `--strip-assertions`:

```javascript
function add(a, b) {
  return a + b;
}
```

### The Clause Structure

Every `func` has a name, followed by keyword-labeled clauses:

**`:args`** lists the typed parameters. Every parameter requires a type keyword. `:any` is the explicit opt-out for untyped parameters. Bare symbols — `(func add :args (a b) ...)` — are a compile error.

**`:returns`** declares the return type. When present, the compiler emits a `return` statement on the last body expression and a type check on the returned value. Without `:returns`, the function is void — no return statement is emitted.

**`:body`** contains all remaining expressions. Everything after `:body` is the function body. Multi-expression bodies are natural — each expression becomes a statement, and the last one is returned (if `:returns` is present):

```lisp
(func greet-and-log
  :args (:string name)
  :returns :string
  :body
  (console:log (template "Greeting " name))
  (template "Hello, " name "!"))
```

```javascript
function greetAndLog(name) {
  // ... type checks ...
  console.log(`Greeting ${name}`);
  return `Hello, ${name}!`;
}
```

### Void Functions

Functions without `:returns` emit no return statement:

```lisp
(func log-message
  :args (:string msg)
  :body (console:log msg))
```

```javascript
function logMessage(msg) {
  // ... type check ...
  console.log(msg);
}
```

Use `:returns :void` if you want to be explicit about the void return. The behaviour is the same — no return statement — but the intent is documented.

### camelCase

The function name follows the standard conversion: `log-message` becomes `logMessage`, `get-user-by-id` becomes `getUserById`. You write lisp-case; the output is idiomatic JavaScript.

### A Preview

In Chapter 8, we'll see how `func` supports multiple clauses with different arities and types — Erlang-style dispatch on arguments — and contracts with `:pre`/`:post` for runtime validation. For now, single-clause `func` covers the vast majority of functions you'll write.
