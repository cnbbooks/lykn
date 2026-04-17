## Suites and Steps

### Grouped Tests with `suite`

`suite` groups related tests with shared context. Child `test` forms compile to `t.step()` calls, giving hierarchical output in the test reporter.

```lisp
(suite "math operations"
  :setup    (bind fixtures (load-fixtures))
  :teardown (cleanup fixtures)

  (test "addition"
    (is-equal (+ 1 2) 3))

  (test "division by zero throws"
    (is-thrown (/ 1 0))))
```

```javascript
Deno.test("math operations", async (t) => {
  const fixtures = loadFixtures();
  try {
    await t.step("addition", () => {
      assertEquals(1 + 2, 3);
    });
    await t.step("division by zero throws", () => {
      assertThrows(() => 1 / 0);
    });
  } finally {
    cleanup(fixtures);
  }
});
```

The `:setup` and `:teardown` apply to the entire suite — all child tests share the fixtures and the cleanup runs after the last step completes (or fails). The suite function is always `async` because `t.step()` returns a promise.

### Sub-Steps with `step`

`step` defines a sub-step within a test. Where `suite` groups independent tests, `step` sequences dependent operations within a single test.

```lisp
(test "user workflow"
  (step "create user"
    (bind user (await (create-user :name "Alice")))
    (is-equal user:name "Alice"))
  (step "delete user"
    (await (delete-user 1))
    (is-equal (await (get-user 1)) null)))
```

```javascript
Deno.test("user workflow", async (t) => {
  await t.step("create user", async () => {
    const user = await createUser({ name: "Alice" });
    assertEquals(user.name, "Alice");
  });
  await t.step("delete user", async () => {
    await deleteUser(1);
    assertEquals(await getUser(1), null);
  });
});
```

When `step` appears inside a `test`, the enclosing test automatically receives the `t` parameter and becomes async. Each step independently detects `await` in its own body. The reader sees structured, sequential operations; Deno sees standard `t.step()` calls and reports each one individually.
