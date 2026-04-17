## Wiring It Up

The entry point ties form submission, state, rendering, and the API together.

```lisp
(bind form (document:get-element-by-id "shorten-form"))
(bind input (document:get-element-by-id "url-input"))

(form:add-event-listener "submit" (async (fn (:any event)
  (event:prevent-default)
  (bind url input:value)
  (set-error null)
  (match (await (shorten-url url))
    ((Ok data)
     (set! input:value "")
     (await (refresh-entries)))
    ((Err message)
     (set-error message))))))

;; Initial load
(await (refresh-entries))
```

The flow:

1. Page loads, compiled JS runs
2. `refresh-entries` fetches existing URLs from the server
3. State updates, `render` runs, entries appear
4. User submits form → `shorten-url` POSTs to server
5. On success: clear input, refresh entries
6. On error: update state with error message, re-render

Every state change goes through `update-state`, which calls `render`.
