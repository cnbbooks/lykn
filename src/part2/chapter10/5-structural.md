## Structural Matching on Plain Objects

Not all data comes from `type`. JavaScript APIs return plain objects — fetch responses, DOM events, parsed JSON. `match` handles them with structural patterns using `obj` keyword-value syntax.

### An API Response

```lisp
(match response
  ((obj :ok true :data d) (process d))
  ((obj :ok false :error e) (handle-error e))
  (_ (throw (new Error "unexpected response"))))
```

```javascript
if (typeof response === "object" && response !== null
    && response.ok === true && "data" in response) {
  const d = response.data;
  process(d);
} else if (typeof response === "object" && response !== null
    && response.ok === false && "error" in response) {
  const e = response.error;
  handleError(e);
} else {
  throw new Error("unexpected response");
}
```

### The Rules

**Keywords are property names, values are patterns.** `:ok true` checks `response.ok === true`. `:data d` checks `"data" in response` and binds `response.data` to `d`.

**Structural patterns always require `_`.** The compiler can't enumerate all possible object shapes — they're open types. A `_` (or a `throw`) handles everything that doesn't match.

**Nested structural patterns work.** `(obj :body (obj :users u))` drills into nested objects, generating nested property checks.

### Why This Matters

Without structural matching, `match` would only work on Lykn-native ADTs. The reader would feel trapped — real JavaScript data arrives as plain objects, and wrapping every API response in a `type` is impractical.

Structural patterns bridge the gap. Fetch a JSON API, parse the result, `match` on its shape. No wrapping. No conversion. Just pattern matching on the data as it arrives.
