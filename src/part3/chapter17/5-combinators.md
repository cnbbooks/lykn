## Promise Combinators

When you need to coordinate multiple async operations.

### `Promise:all` — All Must Succeed

```lisp
(bind results (await (Promise:all #a(
  (fetch-user "alice")
  (fetch-user "bob")
  (fetch-user "carol")))))
```

```javascript
const results = await Promise.all([
  fetchUser("alice"), fetchUser("bob"), fetchUser("carol")]);
```

If any promise rejects, the whole thing rejects. Use when all operations must succeed for the result to be meaningful.

### `Promise:all-settled` — Wait for All, Success or Failure

```lisp
(bind outcomes (await (Promise:all-settled #a(
  (fetch-user "alice")
  (fetch-user "bob")))))
```

Each outcome is `{ status: "fulfilled", value: ... }` or `{ status: "rejected", reason: ... }`. Use when you want results from all operations regardless of individual failures.

Note the camelCase conversion: `all-settled` → `allSettled`.

### `Promise:race` — First to Settle Wins

```lisp
(bind first (await (Promise:race #a(
  (fetch-from-primary)
  (fetch-from-backup)))))
```

The first promise to settle (fulfilled or rejected) determines the result. Use for timeouts or redundant requests.

### `Promise:any` — First to Succeed Wins

```lisp
(bind result (await (Promise:any #a(
  (try-server-a)
  (try-server-b)
  (try-server-c)))))
```

The first fulfilled promise wins. If *all* reject, throws `AggregateError`. Use for fallback chains where any success is acceptable.
