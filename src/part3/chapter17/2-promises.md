## Promises

A Promise is a value that will arrive in the future. It has three states: **pending** (not yet settled), **fulfilled** (resolved with a value), or **rejected** (failed with a reason). Once settled, a promise never changes state.

### Creating Promises

```lisp
(bind promise (new Promise (fn (:function resolve :function reject)
  (set-timeout (fn () (resolve 42)) 1000))))
```

```javascript
const promise = new Promise((resolve, reject) => {
  setTimeout(() => resolve(42), 1000);
});
```

The constructor takes a function with two callbacks: `resolve` (fulfill the promise) and `reject` (reject it). In practice, you rarely create promises manually — most async APIs already return them.

### Consuming Promises

The `.then`/`.catch`/`.finally` methods handle promise results:

```lisp
(-> (fetch "/api/data")
  (:then (fn (:any response) (response:json)))
  (:then (fn (:any data) (process data)))
  (:catch (fn (:any error) (console:error error)))
  (:finally (fn () (cleanup))))
```

```javascript
fetch("/api/data")
  .then(response => response.json())
  .then(data => process(data))
  .catch(error => console.error(error))
  .finally(() => cleanup());
```

### Promise Chaining

`.then` returns a *new* promise. This is why chaining works — each `.then` produces a new promise that resolves when the handler's return value resolves. Returning a plain value wraps it in a resolved promise. Returning a promise chains to that promise.

This "flattening" behaviour is the key insight: promises compose. You don't nest them — you chain them.

### In Practice

You'll rarely write `.then` chains in Lykn. Async/await (next section) provides the same semantics with cleaner syntax. But understanding promises is essential because async/await is built on top of them — `await` consumes a promise, `async` produces one.
