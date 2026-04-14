## Exception Handling

JavaScript reports errors through exceptions. Lykn inherits the mechanism directly — `throw`, `try`, `catch`, `finally` are kernel forms with no surface transformation.

### `throw`

```lisp
(throw (new Error "something went wrong"))
(throw (new TypeError "expected a number"))
```

```javascript
throw new Error("something went wrong");
throw new TypeError("expected a number");
```

Always throw `Error` instances — not strings, not numbers, not objects. `Error` provides a stack trace; a thrown string does not.

### `try` / `catch` / `finally`

```lisp
(try
  (bind data (parse-json input))
  (process data)
  (catch e
    (console:error "Parse failed:" e:message))
  (finally
    (cleanup)))
```

```javascript
try {
  const data = parseJson(input);
  process(data);
} catch (e) {
  console.error("Parse failed:", e.message);
} finally {
  cleanup();
}
```

`catch` binds the error to a name (`e`). `finally` runs regardless of whether an error occurred. Both are optional, but you need at least one.

### Error Chaining

ES2022's `cause` property lets you wrap errors with context:

```lisp
(try
  (bind config (load-config path))
  (catch e
    (throw (new Error
      (template "Failed to load config from " path)
      (obj :cause e)))))
```

The inner error is preserved as `e.cause`. This produces error chains that show both *what* failed and *why* — invaluable in production debugging.

### Error Types

JavaScript provides a hierarchy of error classes:

| Type | When to use |
|---|---|
| `Error` | General-purpose errors |
| `TypeError` | Wrong type (also used by Lykn's type checks) |
| `RangeError` | Value out of range |
| `SyntaxError` | Malformed input |
| `ReferenceError` | Undefined variable (rarely thrown manually) |

Lykn doesn't add custom error classes — zero runtime dependencies. Contract violations (Ch 8) use `Error` with structured messages. Type violations use `TypeError`.

### Never Empty Catches

```lisp
;; BAD — swallows the error silently
(try
  (risky-operation)
  (catch e))

;; GOOD — handle, rethrow, or both
(try
  (risky-operation)
  (catch e
    (console:error "Operation failed:" e:message)
    (throw e)))
```

An empty `catch` is a bug waiting to happen. If you catch an error, do something with it.

### The Functional Alternative

Exceptions are for *unexpected* failures — bugs, network errors, resource exhaustion. For *expected* failures — "user not found," "invalid input," "file doesn't exist" — Lykn offers a different pattern: `Result` types.

```lisp
;; Preview — covered fully in Ch 10
(type Result
  (Ok :any value)
  (Err :string message))

(func find-user
  :args (:string id)
  :returns :any
  :body (if (users:has id)
          (Ok (users:get id))
          (Err "user not found")))
```

A `Result` is a value, not a control flow disruption. You handle it with `match`, and the compiler ensures you handle both cases. Exceptions unwind the stack; `Result` values flow through normal returns.

The guidance: exceptions for bugs (things that shouldn't happen), `Result` for expected failures (things that might happen). This is a Rust pattern that Lykn adopts — not the only way, but the Lykn way.
