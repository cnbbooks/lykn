## Storage

### `localStorage` — Persists Across Sessions

```lisp
(local-storage:set-item "theme" "dark")
(bind theme (local-storage:get-item "theme"))
(local-storage:remove-item "theme")
```

### `sessionStorage` — Cleared When Tab Closes

Same API, different lifetime.

### Storing Objects

Both APIs store strings only. For objects, serialize with JSON:

```lisp
(local-storage:set-item "user"
  (JSON:stringify (obj :name "Duncan" :age 42)))

(bind user (JSON:parse (local-storage:get-item "user")))
```
