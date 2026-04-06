## Lykn's Type Keywords

Lykn's type keywords are not a type system. They are a safety net — runtime checks that fire at boundaries (function entry, binding sites) and catch type errors before they propagate. In development, they throw clear errors. In production, they vanish.

### The Full Table

| Keyword | Compiled check | Notes |
|---|---|---|
| `:number` | `typeof x === "number" && !Number.isNaN(x)` | Excludes NaN |
| `:string` | `typeof x === "string"` | |
| `:boolean` | `typeof x === "boolean"` | |
| `:function` | `typeof x === "function"` | |
| `:object` | `typeof x === "object" && x !== null` | Excludes null |
| `:array` | `Array.isArray(x)` | Not a typeof check |
| `:symbol` | `typeof x === "symbol"` | |
| `:bigint` | `typeof x === "bigint"` | |
| `:any` | *(no check)* | Explicit opt-out |
| `:void` | *(return type only)* | No return value |
| `:promise` | `x instanceof Promise` | Async returns |

This table is worth memorizing. Every type keyword in Lykn maps to a specific runtime check, and that check is exactly what you'd write by hand if you were being careful. The difference is that Lykn writes it for you, every time, without forgetting.

### Where Type Keywords Appear

Type keywords appear in four places:

```lisp
;; 1. Function parameters
(func add
  :args (:number a :number b)
  :returns :number
  :body (+ a b))

;; 2. Anonymous function parameters
(fn (:number x) (* x 2))

;; 3. Binding annotations
(bind :number result (compute-something))

;; 4. ADT constructor fields
(type Circle (Circle :number radius))
```

### What the Check Looks Like

```lisp
(func double
  :args (:number x)
  :returns :number
  :body (* x 2))
```

In development:

```javascript
function double(x) {
  if (typeof x !== "number" || Number.isNaN(x))
    throw new TypeError(
      "double: arg 'x' expected number, got " + typeof x);
  const result__gensym0 = x * 2;
  if (typeof result__gensym0 !== "number" || Number.isNaN(result__gensym0))
    throw new TypeError(
      "double: return value expected number, got "
      + typeof result__gensym0);
  return result__gensym0;
}
```

With `--strip-assertions`:

```javascript
function double(x) {
  return x * 2;
}
```

The development version is verbose but informative — the error message includes the function name, the parameter name, the expected type, and the actual type. The production version is clean. The switch between them is a single compiler flag.

### Why `:number` Excludes NaN

This is a deliberate safety choice. `typeof NaN === "number"` is `true` in JavaScript, but NaN is not a number in any meaningful sense. It's a sentinel value that means "this numeric operation failed." Allowing it to pass a `:number` check would defeat the purpose of the check.

The DLint study found NaN propagation on production websites — `$NaN` displayed as a product price on IKEA's site, NaN in calculated values on eBay. In every case, the bug entered through a function boundary where a number was expected but NaN was received. Lykn's `:number` catches this at the gate.

If you genuinely need to handle NaN — which is rare, but possible in parsing or mathematical code — use `:any` and validate manually. The opt-out is explicit, the default is safe.

### Runtime Checks, Not a Type System

Lykn's type keywords check values at boundaries. They do not perform type inference. They do not propagate types through expressions. They do not catch type errors inside a function body. `(+ x "hello")` will pass the `:number` check on `x` at the function boundary and then produce string concatenation inside the body — because by that point, the compiler is emitting JavaScript, and JavaScript's `+` operator does what it does.

This is intentional. Gao et al.'s research found that type systems — both Flow and TypeScript — catch exactly 15% of real JavaScript bugs. The other 85% are specification errors, logic errors, and async issues that no type system can reach. Lykn's boundary checks target the most cost-effective 15% — the bugs caused by wrong types crossing function boundaries — with zero production overhead and zero annotation burden beyond what you'd document anyway.

A full type system is on the roadmap (gradual typing with Coalton-style inference). For now, type keywords are the right tool: lightweight, zero-cost in production, and sufficient to catch the class of bugs they're designed for.
