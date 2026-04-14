## `fn` and `lambda`: Anonymous Functions

`fn` and `lambda` are aliases — identical behaviour, different names. `fn` for brevity; `lambda` for developers who prefer the traditional Lisp name. This chapter uses `fn` throughout; wherever you see `fn`, `lambda` works identically.

### The Syntax

```lisp
(fn (:number x :number y) (+ x y))
(fn (:string s) (s:to-upper-case))
(fn (:any x) (console:log x))
```

Parameters are positional — no `:args` keyword needed. Each parameter requires a type keyword, same as `func`. The body follows the parameter list.

### Compiled Output

```lisp
(fn (:number x) (* x 2))
```

In development:

```javascript
(x) => {
  if (typeof x !== "number" || Number.isNaN(x))
    throw new TypeError(
      "anonymous: arg 'x' expected number, got " + typeof x);

  return x * 2;
};
```

With `--strip-assertions`:

```javascript
(x) => x * 2;
```

`fn` compiles to an arrow function expression. Arrow functions have lexical `this` binding — which is irrelevant in surface Lykn because there is no `this`.

### Differences from `func`

| | `func` | `fn` / `lambda` |
|---|---|---|
| Named | Yes | No |
| Keyword clauses | `:args`, `:returns`, `:body` | Positional |
| Contracts | `:pre` / `:post` (Ch 8) | Not available |
| Compiles to | `function` declaration | Arrow expression |
| Type annotations | Required | Required |

### Where You Use `fn`

Anonymous functions appear wherever a function is a value — callbacks, event handlers, `map`/`filter`/`reduce`, and inline transformations:

```lisp
;; Callback to map
(bind doubled (numbers:map (fn (:number x) (* x 2))))

;; Event handler
(button:add-event-listener "click"
  (fn (:any event) (handle-click event)))

;; Inline in a binding
(bind transform (fn (:string s) (s:to-upper-case)))
(transform "hello")  ;; → "HELLO"
```

### Immediately Invoked

An `fn` can be called immediately by wrapping it in a list:

```lisp
((fn () (console:log "executed immediately")))
```

This compiles to an IIFE (Immediately Invoked Function Expression) — a pattern JavaScript uses for creating isolated scopes. In Lykn, the compiler generates IIFEs internally for `match`, `some->`, and `if-let`, but you can write them explicitly when you need an inline computation.
