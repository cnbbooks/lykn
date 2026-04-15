## Async Generators

Async generators combine generators with async/await — they `yield` promises that are automatically awaited by the consumer. The `async` wrapper composes naturally with `genfunc`:

```lisp
(async (genfunc fetch-pages
  :args (:string url)
  :body
  (let page 1)
  (while true
    (bind response (await (fetch (template url "?page=" page))))
    (bind data (await (response:json)))
    (if (= data:results:length 0) (return))
    (yield data:results)
    (+= page 1))))
```

```javascript
async function* fetchPages(url) {
  if (typeof url !== "string")
    throw new TypeError(
      "fetch-pages: arg 'url' expected string, got " + typeof url);

  let page = 1;
  while (true) {
    const response = await fetch(`${url}?page=${page}`);
    const data = await response.json();
    if (data.results.length === 0) return;
    yield data.results;
    page += 1;
  }
}
```

### `for-await-of`

Consume async iterables with `for-await-of`:

```lisp
(for-await-of results (fetch-pages "/api/users")
  (for-of user results
    (process user)))
```

Each iteration awaits the next value. `for-await-of` can only appear inside an `async` function or at the top level of a module.

### When Async Generators Shine

- **Paginated APIs** — fetch pages until empty, yielding each page's data
- **Server-sent events** — yield events as they arrive from a stream
- **Line-by-line file reading** — yield each line without loading the whole file
- **Any async data source with unknown length**

### The Alternative

For known-length async operations, `Promise:all` is simpler:

```lisp
(bind all-pages (await (Promise:all
  (Array:from (obj :length 5) (fn (:any _ :number i)
    (fetch (template "/api/users?page=" (+ i 1))))))))
```

Async generators add value when the total count is unknown or when you want to process items as they arrive rather than waiting for all of them.
