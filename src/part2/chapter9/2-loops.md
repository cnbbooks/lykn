## Loops

Lykn inherits JavaScript's loop forms as kernel passthrough. They compile to their JS equivalents with no transformation.

### `for-of` — The Recommended Loop

For iterating over collections — arrays, strings, Maps, Sets, any iterable:

```lisp
(for-of item items
  (console:log item))
```

```javascript
for (const item of items) {
  console.log(item);
}
```

`for-of` is the loop that functional programmers reach for when `map`/`filter`/`reduce` don't fit — typically when the iteration performs side effects or needs early exit via `break`.

### `while`

```lisp
(while (> remaining 0)
  (console:log remaining)
  (-- remaining))
```

```javascript
while (remaining > 0) {
  console.log(remaining);
  --remaining;
}
```

### `for` — C-Style

The traditional three-part loop: `(for init test update body...)`.

```lisp
(for (let i 0) (< i 10) (++ i)
  (console:log i))
```

```javascript
for (let i = 0; i < 10; ++i) {
  console.log(i);
}
```

Note: the `for` initializer uses kernel `let` because the loop variable must be reassignable across iterations. This is one of the few places where `let` appears in Lykn code — a necessary concession to imperative iteration.

### `for-in` — Property Enumeration

```lisp
(for-in key obj
  (console:log key (get obj key)))
```

```javascript
for (const key in obj) {
  console.log(key, obj[key]);
}
```

`for-in` includes inherited properties from the prototype chain — a perennial source of bugs. Prefer `Object:keys` or `Object:entries` with `for-of`:

```lisp
(for-of entry (Object:entries obj)
  (console:log entry))
```

### `do-while`

Executes the body at least once, then checks the condition:

```lisp
(do-while (should-continue?)
  (console:log "at least once"))
```

```javascript
do {
  console.log("at least once");
} while (shouldContinue());
```

Note: in Lykn's `do-while`, the test comes first syntactically (for consistency with `while`), but the body executes first at runtime.

### When to Loop, When Not To

Surface Lykn prefers functional patterns over imperative loops:

- **Transforming data** → `map`, `filter`, `reduce` (Ch 7)
- **Chaining transformations** → threading macros (Ch 13)
- **Recursive structures** → recursion (Ch 7)
- **Side effects on each item** → `for-of`
- **Early exit needed** → `for-of` with `break`
- **Index-based iteration** → `for`
- **Condition-based repetition** → `while`

If you're reaching for `for` to transform an array, `map` is almost always cleaner. Loops exist because they're sometimes the right tool — but in a functional language, that's less often than you might expect.
