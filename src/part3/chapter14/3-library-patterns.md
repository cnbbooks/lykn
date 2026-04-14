## Working with JS Libraries

Practical patterns for common interop scenarios.

### Callback-Based APIs

Most JavaScript APIs accept callbacks. `fn` (arrow functions, no `this` binding) handles these naturally:

```lisp
;; Express-style handler
(bind app (express))
(app:get "/users" (fn (:any req :any res)
  (bind users (get-users))
  (res:json users)))
```

The callback is an `fn` — it receives `req` and `res` as explicit arguments. No `this` needed.

### DOM Manipulation

```lisp
(bind el (document:get-element-by-id "counter"))
(bind count (cell 0))

(func update-display
  :body (= el:text-content (template (express count))))

(el:add-event-listener "click" (fn (:any event)
  (swap! count (fn (:number n) (+ n 1)))
  (update-display)))
```

The DOM element is accessed via colon syntax. State is managed in a cell. The click handler updates the cell and refreshes the display. No `this`, no class, no method binding.

### API Responses with Structural `match`

```lisp
(bind response (await (fetch "/api/users")))
(bind data (await (response:json)))

(match data
  ((obj :ok true :users users) (render users))
  ((obj :ok false :error msg) (show-error msg))
  (_ (show-error "unexpected response")))
```

JavaScript APIs return plain objects. Structural `match` (Ch 10) handles them without wrapping in ADTs. The `obj` pattern checks property existence and destructures in one step.

### Class-Based Libraries

When a library requires `new` or expects `this`-bound methods:

```lisp
(bind ws (new WebSocket "ws://localhost:8080"))

(ws:add-event-listener "message" (fn (:any event)
  (bind data (JSON:parse event:data))
  (match data
    ((obj :type "chat" :text t) (display-message t))
    (_ (console:log "unknown message type")))))
```

`new` creates the instance. Event listeners use `fn` (no `this` needed — the data arrives as arguments or properties of the event object).
