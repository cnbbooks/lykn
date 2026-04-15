## `genfunc`: Named Generators

A generator is a function that can pause and resume, producing values lazily via `yield`. Lykn's `genfunc` form mirrors `func` — keyword-labeled clauses, typed parameters, and a new `:yields` annotation for per-yield type checking.

### Basic Generator

```lisp
(genfunc range
  :args (:number start :number end)
  :yields :number
  :body
  (for (let i start) (< i end) (+= i 1)
    (yield i)))
```

```javascript
function* range(start, end) {
  if (typeof start !== "number" || Number.isNaN(start))
    throw new TypeError(
      "range: arg 'start' expected number, got " + typeof start);

  if (typeof end !== "number" || Number.isNaN(end))
    throw new TypeError(
      "range: arg 'end' expected number, got " + typeof end);

  for (let i = start; i < end; i += 1) {
    yield (() => {
      const yv__gensym0 = i;
      if (typeof yv__gensym0 !== "number" || Number.isNaN(yv__gensym0))
        throw new TypeError(
          "range: yield expected number, got " + typeof yv__gensym0);
      return yv__gensym0;
    })();
  }
}
```

### What `:yields` Does

The `:yields :number` annotation generates a runtime type check on every `yield` expression — the yielded value is wrapped in an IIFE that validates the type before yielding. This catches type errors *at the production site*, not at the consumption site.

Without `:yields`, `yield` passes values through unchecked:

```lisp
(genfunc count-up
  :body
  (let i 0)
  (while true
    (yield i)
    (+= i 1)))
```

### Consuming Generators

Generators are iterable — they implement the iteration protocol automatically:

```lisp
;; for-of
(for-of n (range 0 5)
  (console:log n))      ;; 0, 1, 2, 3, 4

;; Spread into array
(bind nums (array (spread (range 0 5))))  ;; [0, 1, 2, 3, 4]

;; Manual iteration
(bind r (range 0 3))
(console:log (r:next))  ;; { value: 0, done: false }
(console:log (r:next))  ;; { value: 1, done: false }
(console:log (r:next))  ;; { value: 2, done: false }
(console:log (r:next))  ;; { value: undefined, done: true }
```

### `yield*` — Delegation

`yield*` delegates to another iterable, yielding each of its values:

```lisp
(genfunc concat-iters
  :args (:any a :any b)
  :body (yield* a) (yield* b))

(for-of n (concat-iters #a(1 2) #a(3 4))
  (console:log n))      ;; 1, 2, 3, 4
```

### Infinite Generators

Generators can be infinite — they yield forever until the consumer stops asking:

```lisp
(genfunc fibonacci
  :yields :number
  :body
  (let a 0)
  (let b 1)
  (while true
    (yield a)
    (let temp a)
    (= a b)
    (= b (+ temp b))))
```

Consume with `break` or `take`:

```lisp
(bind count (cell 0))
(for-of n (fibonacci)
  (console:log n)
  (swap! count (fn (:number c) (+ c 1)))
  (if (>= (express count) 10) (break)))
```

Generators are lazy — they compute the next value only when `next()` is called. This is what makes infinite sequences practical: memory usage is constant regardless of how many values are produced.
