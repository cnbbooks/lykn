## Async/Await in Lykn

Async/await is syntactic sugar over promises. `async` makes a function return a promise. `await` pauses execution until a promise settles.

### `async` as a Wrapper

In Lykn, `async` wraps any function form — `func`, `fn`, `lambda`:

```lisp
(async (func fetch-user
  :args (:string id)
  :body
  (bind response (await (fetch (template "/api/users/" id))))
  (await (response:json))))
```

```javascript
async function fetchUser(id) {
  if (typeof id !== "string")
    throw new TypeError(
      "fetch-user: arg 'id' expected string, got " + typeof id);

  const response = await fetch(`/api/users/${id}`);
  return await response.json();
}
```

`async` sets `async: true` on the compiled function. Type checks, contracts, everything else works the same — it's just an async function now.

### Async `fn`

```lisp
(bind handler (async (fn (:any event)
  (bind data (await (fetch-data)))
  (process data))))
```

```javascript
const handler = async (event) => {
  const data = await fetchData();
  process(data);
};
```

### `await` Is Unary

`(await expr)` compiles to `await expr`. It can only appear inside an `async` function — or at the top level of a module.

### Top-Level Await

Because all Lykn code is ESM, `await` works at the top level without wrapping in `async`:

```lisp
(bind config (await (load-config "app.json")))
(bind db (await (connect config:database-url)))
(console:log "Ready")
```

```javascript
const config = await loadConfig("app.json");
const db = await connect(config.databaseUrl);
console.log("Ready");
```

No async wrapper needed. The module itself is the async context. This is one of the quiet benefits of ESM-only — top-level await is free.
