## Mutating vs Non-Mutating Methods

JavaScript's array methods fall into two categories. The distinction matters in surface Lykn, where immutability is the default.

### Non-Mutating (Preferred)

| Method | Purpose |
|---|---|
| `map` | Transform each element |
| `filter` | Select matching elements |
| `slice` | Extract a sub-array |
| `concat` | Combine arrays |
| `flat` / `flat-map` | Flatten nested arrays |
| `to-sorted` | Sort (ES2023, non-mutating) |
| `to-reversed` | Reverse (ES2023, non-mutating) |
| `to-spliced` | Splice (ES2023, non-mutating) |
| `with` | Replace at index (ES2023) |

These return new arrays. The original is unchanged.

### Mutating (Use with Care)

| Method | Purpose |
|---|---|
| `push` / `pop` | Add/remove at end |
| `shift` / `unshift` | Add/remove at start |
| `sort` | Sort in place |
| `reverse` | Reverse in place |
| `splice` | Insert/remove at index |
| `fill` | Fill with value |

These change the array in place. In surface Lykn, use them inside `swap!` on cell-wrapped arrays, or on arrays that aren't shared.

### The Lykn Way: `conj`

For immutable append:

```lisp
(bind extended (conj items new-item))
```

```javascript
const extended = [...items, newItem];
```

`conj` is spread-based — it creates a new array. For multiple additions, `concat` or `reduce` is more efficient than repeated `conj` (each `conj` copies the entire array).

### The ES2023 Non-Mutating Variants

`to-sorted`, `to-reversed`, `to-spliced`, and `with` are JavaScript's own answer to the mutation problem. They do what their mutating counterparts do, but return new arrays:

```lisp
(bind sorted (nums:to-sorted))
(bind reversed (nums:to-reversed))
(bind replaced (nums:with 2 99))     ;; replace index 2 with 99
```

These are the methods Lykn's functional style prefers. Use them over the mutating versions wherever possible.
