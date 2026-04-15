## Consuming Iterables

The reader has been consuming iterables throughout the book. Every one of these features uses `Symbol:iterator` under the hood:

```lisp
;; for-of (Ch 9)
(for-of item items (process item))

;; Spread (Ch 15)
(bind all (array (spread iter1) (spread iter2)))

;; Destructuring (Ch 15)
(bind (array first second) some-iterable)

;; Array.from (Ch 19)
(bind arr (Array:from some-iterable))
```

The iteration protocol is the unifying mechanism. If an object implements `Symbol:iterator`, all of these features work on it automatically — including on generators, which implement the protocol by default.

### Iterator Helpers (ES2025)

New methods directly on iterators — lazy `map`, `filter`, `take`, `drop`, `flat-map`, `to-array`. These enable pipelines without materializing intermediate arrays:

```lisp
(bind result
  (-> (some-generator)
    (:filter (fn (:any x) (> x 0)))
    (:take 10)
    (:to-array)))
```

Iterator helpers are significant because they bring the functional array methods (`map`, `filter`) to lazy iteration — no intermediate arrays, no eager evaluation. Check Deno's current support level for these.
