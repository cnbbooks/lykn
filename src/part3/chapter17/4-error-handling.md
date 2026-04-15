## Error Handling in Async

Async errors are promises that reject. Two mechanisms for handling them.

### try/catch with await

```lisp
(async (func safe-fetch
  :args (:string url)
  :body
  (try
    (bind response (await (fetch url)))
    (if (not response:ok)
      (throw (new Error (template "HTTP " response:status))))
    (await (response:json))
    (catch e
      (console:error (template "Fetch failed: " e:message))
      null))))
```

```javascript
async function safeFetch(url) {
  if (typeof url !== "string")
    throw new TypeError(
      "safe-fetch: arg 'url' expected string, got " + typeof url);

  try {
    const response = await fetch(url);
    if (!response.ok)
      throw new Error(`HTTP ${response.status}`);
    return await response.json();
  } catch (e) {
    console.error(`Fetch failed: ${e.message}`);
    return null;
  }
}
```

### The Result Pattern

For expected failures, return `Result` instead of catching:

```lisp
(async (func safe-fetch
  :args (:string url)
  :body
  (try
    (bind response (await (fetch url)))
    (Ok (await (response:json)))
    (catch e
      (Err e:message)))))

;; Caller uses match
(match (await (safe-fetch "/api/data"))
  ((Ok data) (process data))
  ((Err msg) (show-error msg)))
```

The distinction, reinforced from Chapters 9 and 10:

- **try/catch** for unexpected failures — network errors, bugs, resource exhaustion
- **`Result`** for expected failures — 404, invalid input, authentication denied

If you can enumerate the failure modes, return `Result`. If you can't, let the exception propagate.

### Common Pitfalls

**Forgetting to `await`**: `(bind data (fetch url))` binds a Promise, not the data. You need `(bind data (await (fetch url)))`.

**Swallowing errors**: a `.catch` that logs but doesn't rethrow silently hides failures. If the caller needs to know about the error, rethrow it or return `Result`.

**`await` is shallow**: `(await promise)` waits for *that* promise, not for promises nested inside the resolved value. If the resolved value is an array of promises, you still need `Promise:all`.
