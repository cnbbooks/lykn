## Truthiness

JavaScript's `if` doesn't require a boolean. It accepts any value and coerces it to a boolean. The values that become `false` are called *falsy*. Everything else is *truthy*.

### The Falsy Values

There are exactly eight:

| Value | Type | Notes |
|---|---|---|
| `false` | boolean | The obvious one |
| `0` | number | Zero |
| `-0` | number | Negative zero (yes, it exists) |
| `0n` | bigint | BigInt zero |
| `""` | string | Empty string |
| `null` | null | Intentional absence |
| `undefined` | undefined | Unintentional absence |
| `NaN` | number | Not a Number |

Everything else is truthy. `[]` is truthy. `{}` is truthy. `"false"` is truthy. `"0"` is truthy. `new Boolean(false)` is truthy — a wrapped `false` that evaluates as `true`, which is the sort of thing that makes you question whether the language is being philosophical on purpose.

### The Danger

Truthiness checks conflate several very different conditions:

```javascript
if (user) { ... }       // false if user is: null, undefined, 0, "", false, NaN
```

If `user` is `0` — perhaps a user ID — the truthiness check fails. If `user` is `""` — perhaps a username that hasn't been validated yet — the truthiness check fails. The check is convenient but imprecise: it can't distinguish "this value doesn't exist" from "this value is zero or empty."

### Lykn's Approach

In Lykn surface code, truthiness works the same way — `if` evaluates its test using JavaScript's truthiness rules, because the compiled output is JavaScript. But the surface language encourages a more precise pattern: `Option` types with `if-let`:

```lisp
;; Truthiness check (JS-style — works but imprecise)
(if user
  (greet user)
  (redirect-to-login))

;; Option check (Lykn-style — explicit and precise)
(if-let ((Some user) (find-user id))
  (greet user)
  (redirect-to-login))
```

The `Option` version distinguishes "user not found" (returns `None`) from "user exists but has a falsy value" (returns `(Some 0)` or `(Some "")`). This is a preview of Chapter 10, where `Option`, `Result`, and exhaustive pattern matching get their full treatment. For now, the point is: Lykn gives you truthiness because JavaScript gives you truthiness, but it also gives you better alternatives.
