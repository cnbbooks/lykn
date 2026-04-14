## When to Use Cells

Cells are intentional friction. The ceremony of `cell`/`express`/`swap!` compared to direct variable reassignment is *by design*. If mutation feels slightly inconvenient, good — it should make you consider whether you actually need it.

### Good Use Cases

- **Counters and accumulators** — loop indices, request counts, retry trackers
- **Caches** — memoization, lazy initialization, computed values
- **Event-driven state** — UI state, handler coordination, observable values
- **Interop with mutable JS APIs** — DOM manipulation, timer state

### When Cells Aren't the Answer

- **Data transformation** — use `map`/`filter`/`reduce`, threading macros, or `assoc`/`dissoc`/`conj`
- **Accumulating results** — use `reduce` or recursion
- **Branching on state** — use `match` on an immutable value

### The Rule of Thumb

If you find yourself wanting more than two or three cells in a function, you're probably solving a data transformation problem imperatively. Step back and think functionally. Threading macros and immutable updates (later in this chapter) handle most of what people reach for mutation to do.
