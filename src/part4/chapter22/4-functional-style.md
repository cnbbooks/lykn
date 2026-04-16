## Collections in Functional Lykn

Maps and Sets are mutable — `.set()`, `.add()`, `.delete()` all mutate in place. This sits oddly with surface Lykn's immutability preference.

### The Pragmatic Approach

Local mutation is fine — if a Map lives entirely inside a function and nobody else sees it, mutating it is safe:

```lisp
(func build-index
  :args (:array items)
  :returns :any
  :body
  (bind index (new Map))
  (for-of item items
    (index:set item:id item))
  index)
```

### Shared State: Use `cell`

For Maps/Sets that live beyond function scope:

```lisp
(bind cache (cell (new Map)))

;; Update via swap! — mutation is marked with !
(swap! cache (fn (:any m) (do (m:set key value) m)))
```

The `!` on `swap!` marks the mutation point. The Map itself mutates inside the swap function, but the cell boundary makes it visible and controlled.

### The Honest Tension

This is one of the places where Lykn's immutability ideal meets JavaScript's mutable reality. Copying a Map on every update is possible (`(new Map existing-map)`) but expensive for large collections. The pragmatic answer: use `cell` for the ownership boundary, mutate the collection inside `swap!`, and accept that JavaScript's built-in collections are mutable by design.
