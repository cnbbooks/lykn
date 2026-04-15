## Iteration Patterns

Four ways to iterate arrays, ordered by preference.

### 1. Higher-Order Methods

For data transformations — `map`, `filter`, `reduce`. Preferred because they're declarative, composable, and return new values:

```lisp
(bind result (->> items
  (:filter is-valid)
  (:map transform)
  (:reduce combine initial)))
```

### 2. `for-of`

For effectful iteration — logging, DOM updates, side effects:

```lisp
(for-of item items
  (console:log item))
```

Use `for-of` when you need to *do* something with each element rather than *produce* something from it.

### 3. `for-each`

JavaScript's `.forEach` — similar to `for-of` but as a method:

```lisp
(items:for-each (fn (:any item) (console:log item)))
```

`for-each` can't `break` or `return` from the enclosing function. Prefer `for-of` when you need early exit.

### 4. `for` Loop

For index-based access or performance-critical iteration:

```lisp
(for (let i 0) (< i items:length) (++ i)
  (console:log i (get items i)))
```

### What to Avoid

`for-in` on arrays — it iterates property keys (strings, not numbers), includes inherited properties, and doesn't guarantee order. Never use `for-in` on arrays.
