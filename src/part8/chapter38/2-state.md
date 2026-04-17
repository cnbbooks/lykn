## State Management with `cell`

App state as a single `cell`:

```lisp
(bind state (cell (obj :entries #a() :error null)))

(func update-state
  :args (:object new-state)
  :body
  (reset! state new-state)
  (render (express state)))
```

Every state change goes through `update-state`, which replaces the state and triggers a render. This is a tiny reactive system — `cell` + render. Not a framework, just a pattern.

```lisp
(func set-entries
  :args (:array entries)
  :body
  (update-state (assoc (express state) :entries entries :error null)))

(func set-error
  :args (:string message)
  :body
  (update-state (assoc (express state) :error message)))
```

`assoc` produces a new state object. `update-state` replaces the cell and re-renders. Every mutation point has `!` (inside `reset!`). The pattern is explicit.
