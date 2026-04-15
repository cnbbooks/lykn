## Objects vs `type`

When to use plain objects vs algebraic data types.

### Use `obj` For

**Data bags** — configuration, options, API responses. Anything whose shape varies or comes from external sources:

```lisp
(bind config (obj :port 3000 :host "localhost" :debug true))
```

**Key-value maps** — when the keys aren't known at compile time:

```lisp
(bind headers (obj :content-type "application/json" :authorization token))
```

**JS interop** — everything JavaScript gives you is a plain object.

### Use `type` For

**Domain models** — entities with known variants where the compiler should enforce shape:

```lisp
(type HttpResult
  (Success :any data)
  (Failure :number status :string message))
```

**Exhaustive dispatch** — when you want the compiler to catch missing cases:

```lisp
(match result
  ((Success data) (render data))
  ((Failure status msg) (show-error status msg)))
```

### The Principle

`obj` is for the *outside world* — JS interop, APIs, parsed JSON. Structural `match` with `obj` patterns handles it, but `_` is always required because the compiler can't enumerate open shapes.

`type` is for the *inside world* — your domain, your invariants, your compiler-checked safety. Exhaustive `match` catches every case. Missing a variant is a compile error, not a runtime surprise.

Push data from `obj` (open, external) to `type` (closed, internal) as early as possible in your code. Parse the API response with structural `match`, convert to your domain types, then work with `type`/`match` for the rest.
