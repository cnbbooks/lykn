## Putting It Together

A complete example combining cells, threading, pattern matching, and immutable updates.

### A Simple State Manager

```lisp
(type Option (Some :any value) None)

(bind state (cell (obj :users #a() :loading false)))

(func add-user
  :args (:string name)
  :body
  (swap! state (fn (:object s)
    (assoc s :users (conj (get s :users) (obj :name name))))))

(func get-user-count
  :returns :number
  :body (get (express state) :users):length)
```

Every mutation goes through `swap!`. Every data update produces a new value via `assoc` and `conj`. The cell contains the state; the functions transform it. The `!` in `swap!` marks the only place where anything changes.

### A Pipeline

```lisp
(bind result
  (-> raw-data
    (JSON:parse)
    (get :users)
    (:filter (fn (:any u) u:active))
    (:map (fn (:any u) (get u :name)))
    (:join ", ")))
```

No mutation. No intermediate variables. The data flows from raw JSON string to comma-separated names in a single pipeline. Each step is a pure transformation.

### The Pattern

The idiomatic surface Lykn style emerges from these three features:

- **Immutable by default** — `bind` for values, `assoc`/`dissoc`/`conj` for updates
- **Explicit mutation** — `cell` with `swap!`/`reset!`, marked with `!`
- **Pipeline composition** — `->` and `->>` for transformations, `some->` for nullable chains, `if-let` for conditional unwrapping

When you see Lykn code that follows this pattern, every mutation point is visible, every data transformation is traceable, and every function call reads top-to-bottom instead of inside-out.
