## Enumerability

Which properties show up where:

| Operation | Own | Inherited | Enumerable only? |
|---|---|---|---|
| `for-in` | Yes | Yes | Yes |
| `Object:keys` | Yes | No | Yes |
| `Object:get-own-property-names` | Yes | No | No |
| `Reflect:own-keys` | Yes | No | No |

### The Practical Rule

Use `Object:keys` or `Object:entries` with `for-of` — they enumerate own, enumerable properties, which is what you want 95% of the time. Avoid `for-in` — it includes inherited properties, which is almost never what you want.

```lisp
;; Safe: own enumerable properties
(for-of entry (Object:entries obj)
  (console:log entry))

;; Unsafe: includes inherited properties
(for-in key obj
  (console:log key))
```

Non-enumerable properties are used by the language itself (built-in methods like `to-string`) and by library code that wants to hide implementation details. You'll rarely create non-enumerable properties yourself.
