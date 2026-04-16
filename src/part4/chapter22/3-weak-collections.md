## WeakMap and WeakSet

Weak collections hold *weak references* — when no other reference to the key (WeakMap) or value (WeakSet) exists, it can be garbage collected even though it's still in the collection.

### WeakMap

Object keys that don't prevent garbage collection:

```lisp
(bind cache (new WeakMap))

(func process-with-cache
  :args (:object item)
  :returns :any
  :body
  (if (cache:has item)
    (cache:get item)
    (do
      (bind result (expensive-computation item))
      (cache:set item result)
      result)))
```

When `item` is garbage collected elsewhere, the cache entry disappears automatically. No memory leak. No manual cleanup.

**Use cases**: caching computed results keyed by object identity, storing private data associated with DOM elements, associating metadata with objects you don't own.

### WeakSet

Tracking objects without preventing garbage collection:

```lisp
(bind processed (new WeakSet))

(func process-once
  :args (:object item)
  :body
  (if (not (processed:has item))
    (do
      (processed:add item)
      (do-work item))))
```

### Constraints

- Keys (WeakMap) / values (WeakSet) must be objects or symbols — not primitives
- Not iterable — no `for-of`, no `.size`, no `.keys()`
- Not enumerable — you can't list what's in them

These constraints exist because weak references interact with the garbage collector, which operates non-deterministically. If you could enumerate a WeakMap's keys, the result would depend on when GC last ran — a recipe for non-reproducible bugs.
