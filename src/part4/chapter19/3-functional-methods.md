## Functional Array Methods

The heart of the chapter. These methods align with Lykn's functional style and should be the primary way you work with arrays.

### `map` — Transform Each Element

```lisp
(bind doubled (nums:map (fn (:number x) (* x 2))))
```

```javascript
const doubled = nums.map((x) => {
  // ... type check ...
  return x * 2;
});
```

Returns a new array. The original is unchanged.

### `filter` — Select Matching Elements

```lisp
(bind evens (nums:filter (fn (:number x) (= (% x 2) 0))))
```

Returns a new array containing only elements where the predicate returned truthy.

### `reduce` — Fold to a Single Value

```lisp
(bind total (nums:reduce (fn (:number acc :number x) (+ acc x)) 0))
```

The second argument (`0`) is the initial accumulator. Without it, the first element becomes the initial accumulator — which fails on empty arrays.

### `find` and `find-index`

```lisp
(bind first-even (nums:find (fn (:number x) (= (% x 2) 0))))
(bind idx (nums:find-index (fn (:number x) (> x 3))))
```

`find` returns the first matching element (or `undefined`). `find-index` returns its index (or `-1`).

### `some` and `every`

```lisp
(bind has-negative (nums:some (fn (:number x) (< x 0))))
(bind all-positive (nums:every (fn (:number x) (> x 0))))
```

`some` returns `true` if any element matches. `every` returns `true` if all do. Both short-circuit — they stop as soon as the result is determined.

### `flat-map` — Map + Flatten

```lisp
(bind words (sentences:flat-map (fn (:string s) (s:split " "))))
```

Maps each element to an array, then flattens one level. Equivalent to `.map(...).flat()` but in one pass.

### Pipelines with Threading

```lisp
(-> users
  (:filter (fn (:any u) u:active))
  (:map (fn (:any u) u:name))
  (:sort))
```

The threading macro `->` (Ch 13) chains method calls. Each step receives the previous result as the receiver. The pipeline reads top-to-bottom: filter active users, extract names, sort.
