## Writing Tests

The testing module provides its forms through `import-macros`, the same mechanism used for all of Lykn's macro modules. Import what you need, write tests, and the macros handle the rest.

```lisp
(import-macros "testing"
  (test test-async suite step
   is is-equal is-not-equal is-strict-equal
   ok is-thrown is-thrown-async
   matches includes has obj-matches
   test-compiles))
```

Most test files import a subset — `test` and `is-equal` cover the majority of cases.

### The Minimal Form

A test is a name and a body. No ceremony.

```lisp
(import-macros "testing" (test is-equal))

(test "addition works"
  (is-equal (+ 1 2) 3)
  (is-equal (* 3 4) 12))
```

```javascript
Deno.test("addition works", () => {
  assertEquals(1 + 2, 3);
  assertEquals(3 * 4, 12);
});
```

Multiple assertions in a single test are fine. The test passes when all of them pass, which is to say it fails the moment any of them doesn't — a pattern that, in the context of software testing, passes for optimism.

### Setup and Teardown

When a test needs initialisation or cleanup, use the keyword-clause syntax. The reader already knows this pattern from `func`'s `:pre`/`:post`/`:body` clauses (Ch 8) — Lykn uses the same structural conventions across `func`, `test`, and `suite`.

```lisp
(test "database query"
  :setup    (bind db (create-temp-db))
  :teardown (close db)
  :body
    (bind result (query db "SELECT 1"))
    (is-equal result 1))
```

```javascript
Deno.test("database query", () => {
  const db = createTempDb();
  try {
    const result = query(db, "SELECT 1");
    assertEquals(result, 1);
  } finally {
    close(db);
  }
});
```

The `:teardown` clause wraps the body in `try { ... } finally { ... }` — cleanup runs even when the test fails. When only `:setup` is present without `:teardown`, the setup expressions are prepended to the body with no wrapping.

### Async Tests

The explicit form is `test-async`:

```lisp
(test-async "fetches data"
  (bind result (await (fetch-data)))
  (is-equal result:status :ok))
```

```javascript
Deno.test("fetches data", async () => {
  const result = await fetchData();
  assertEquals(result.status, "ok");
});
```

But `test` handles this automatically. If the macro finds `await` anywhere in the body, it emits an `async` function:

```lisp
(test "also fetches data"
  (bind result (await (fetch-data)))
  (is-equal result:status :ok))
```

Same output. The `test` macro walks the body at compile time, spots the `await`, and adjusts. `test-async` exists for the rarer case where the body delegates to an async helper without a lexically visible `await`, or where the author simply wants to be explicit about it.
