## `switch`

```lisp
(switch status
  (200 (process-ok) (break))
  (404 (not-found) (break))
  (500 (server-error) (break))
  (default (unknown-status status)))
```

```javascript
switch (status) {
  case 200: processOk(); break;
  case 404: notFound(); break;
  case 500: serverError(); break;
  default: unknownStatus(status);
}
```

### The Syntax

`(switch expr (case-value body...) ... (default body...))`. Each case is a parenthesized group: the first element is the test value, the rest is the body. `default` handles the fallback.

### Explicit `break`

Lykn's `switch` does not auto-break. Each case needs an explicit `(break)` to prevent fallthrough — the same as JavaScript. If you *want* fallthrough (rare), omit the `break`.

### But Consider `match`

`switch` has no exhaustiveness checking. If you add a new status code and forget to add a case, the `default` branch runs silently — or worse, if there's no `default`, nothing runs at all.

`match` (Chapter 10) catches missing cases at compile time. For dispatching on tagged data types, `match` is strictly better. Use `switch` when the value is an open type (arbitrary status codes, string commands) where a `default` fallback is the correct behaviour.
