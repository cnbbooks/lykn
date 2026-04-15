## When to Use Generators

Generators add laziness at the cost of statefulness (`yield` pauses and resumes, which is inherently stateful). The trade-off is worth it in specific situations.

### Generators Shine

- **Infinite sequences** — Fibonacci, primes, counters, random streams. Can't be represented as arrays.
- **Large datasets** — processing millions of rows without loading them all into memory.
- **Custom iteration** — tree traversal, graph walking, tokenizers. Complex iteration logic that doesn't fit `map`/`filter`/`reduce`.
- **Lazy pipelines** — compose with iterator helpers (`filter`, `take`, `map`) for memory-efficient processing.

### Arrays Are Usually Better

For finite transformations on data you already have:

```lisp
;; Array pipeline — eager but clear
(->> items
  (:filter (fn (:any x) (> x 0)))
  (:map (fn (:any x) (* x 2)))
  (:slice 0 10))
```

Arrays are simpler to reason about, compose with the full method API, and don't involve `yield` semantics. If your data fits in memory and you know its length, arrays win.

### The Rule

Use generators when the data is *too large*, *infinite*, or *arrives over time*. Use arrays when it's *finite and available*. When in doubt, start with arrays and reach for generators when you hit a memory or laziness need.
