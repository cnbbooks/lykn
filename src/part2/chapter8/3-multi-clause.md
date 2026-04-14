## Multi-Clause Dispatch

A single `func` can have multiple clauses, each with its own `:args`, `:returns`, `:pre`, `:post`, and `:body`. The compiler generates a dispatch chain that selects the right clause at runtime.

### Multi-Arity Dispatch

Different numbers of arguments:

```lisp
(func greet
  (:args (:string name)
   :returns :string
   :body (template "Hello, " name))

  (:args (:string greeting :string name)
   :returns :string
   :body (template greeting ", " name)))
```

```javascript
function greet(...args) {
  if (args.length === 2 && typeof args[0] === "string"
      && typeof args[1] === "string") {
    const greeting = args[0];
    const name = args[1];
    return `${greeting}, ${name}`;
  }
  if (args.length === 1 && typeof args[0] === "string") {
    const name = args[0];
    return `Hello, ${name}`;
  }
  throw new TypeError("greet: no matching clause for arguments");
}
```

Call with one argument, get the default greeting. Call with two, provide your own. The dispatch is on arity — the cheapest check.

### Multi-Type Dispatch

Same arity, different types:

```lisp
(func describe
  (:args (:number x)
   :returns :string
   :body (template "number: " x))

  (:args (:string x)
   :returns :string
   :body (template "string: " x))

  (:args (:boolean x)
   :returns :string
   :body (template "boolean: " x)))
```

The compiler checks the type of the argument and routes to the matching clause. Each clause handles one type; there's no ambiguity about which clause runs.

### Per-Clause Contracts

Each clause can have its own `:pre` and `:post`:

```lisp
(func divide
  (:args (:number a :number b)
   :returns :number
   :pre (not (= b 0))
   :body (/ a b))

  (:args (:number a)
   :returns :number
   :pre (not (= a 0))
   :body (/ 1 a)))
```

Two-argument `divide` requires a non-zero divisor. One-argument `divide` computes the reciprocal and requires a non-zero input. Each clause has its own contract, checked only when that clause is selected.

### The Syntax

The difference between single-clause and multi-clause is structural:

```lisp
;; Single clause: :args directly after name
(func add
  :args (:number a :number b)
  :returns :number
  :body (+ a b))

;; Multi-clause: each clause wrapped in parens
(func add
  (:args (:number a :number b)
   :returns :number
   :body (+ a b))

  (:args (:number a :number b :number c)
   :returns :number
   :body (+ a b c)))
```

The compiler detects multi-clause by the presence of a parenthesized group immediately after the function name.

### The No-Match Error

The compiled output always includes a final `throw new TypeError("name: no matching clause for arguments")`. Even if you believe your clauses cover every case, the runtime guard exists. This is a safety net — if a value of an unexpected type reaches the dispatch chain, you get a clear error instead of silent fallthrough.
