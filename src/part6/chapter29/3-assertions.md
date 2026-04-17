## Assertion Forms

Each assertion form maps to a specific `@std/assert` function. No clever dispatch, no compile-time inspection to guess what you meant — the form name determines the assertion. Predictable, documented, and debuggable.

### The Assertion Vocabulary

| Form | Purpose | Compiles to |
|------|---------|-------------|
| `(is expr)` | Truthiness | `assert(expr)` |
| `(is-equal actual expected)` | Deep equality | `assertEquals` |
| `(is-not-equal actual expected)` | Deep inequality | `assertNotEquals` |
| `(is-strict-equal actual expected)` | Reference equality (`===`) | `assertStrictEquals` |
| `(ok expr)` | Not null/undefined | `assertExists` |
| `(is-thrown body ErrorType)` | Expects throw | `assertThrows` |
| `(is-thrown-async body ErrorType)` | Expects async rejection | `assertRejects` |
| `(matches str pattern)` | Regex match | `assertMatch` |
| `(includes str substr)` | String contains | `assertStringIncludes` |
| `(has arr items)` | Array contains | `assertArrayIncludes` |
| `(obj-matches actual subset)` | Partial object match | `assertObjectMatch` |

The names follow Lykn's convention: named English words, not abbreviations. `is-equal`, not `eq`. `is-thrown`, not `throws`. The same preference that gave us `func` instead of `defun` and `bind` instead of `def`.

### Deep Equality: `is-equal`

The workhorse. Handles objects, arrays, nested structures — deep structural comparison, not reference identity.

```lisp
(test "data structures"
  (is-equal #a(1 2 3) #a(1 2 3))
  (is-equal (obj :a 1 :b 2) (obj :a 1 :b 2)))
```

When it fails, Deno's built-in diff output shows both values with colour-coded differences — actual vs expected, no ambiguity. The assertion macros currently defer to Deno's error formatting, which is already quite good at the business of making a developer feel slightly uncomfortable about their assumptions.

### Catching Errors: `is-thrown`

The body expression is wrapped in a closure and passed to `assertThrows`. The optional second argument specifies the expected error type; the optional third specifies the message.

```lisp
(test "invalid input throws"
  (is-thrown (parse-json "not json") SyntaxError)
  (is-thrown (validate nil) TypeError "expected non-null"))
```

```javascript
Deno.test("invalid input throws", () => {
  assertThrows(() => parseJson("not json"), SyntaxError);
  assertThrows(() => validate(null), TypeError, "expected non-null");
});
```

For async rejections, `is-thrown-async` wraps the body in an `async` closure and uses `assertRejects`:

```lisp
(test-async "rejects on bad URL"
  (is-thrown-async (await (fetch-data "bad-url")) NetworkError))
```

### Partial Matching: `obj-matches`

When you care about shape, not completeness. The actual object may have additional fields — `obj-matches` only checks the ones you specify.

```lisp
(test "response shape"
  (obj-matches response
    (obj :status 200 :ok true)))
```

This passes even if `response` contains a dozen other fields. The assertion verifies the *subset*, not the entirety — which is precisely the right default for testing API responses, where you care that the fields you need are present and correct, and are content to let the rest of the response live its own life undisturbed.
