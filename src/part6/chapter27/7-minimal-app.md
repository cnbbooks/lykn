## A Minimal Browser App

Everything together — a counter app.

```lisp
(bind count (cell 0))
(bind display (document:get-element-by-id "count"))
(bind inc-btn (document:get-element-by-id "increment"))
(bind dec-btn (document:get-element-by-id "decrement"))

(func render
  :body (set! display:text-content (template (express count))))

(inc-btn:add-event-listener "click"
  (fn (:any e)
    (swap! count (fn (:number n) (+ n 1)))
    (render)))

(dec-btn:add-event-listener "click"
  (fn (:any e)
    (swap! count (fn (:number n) (- n 1)))
    (render)))

(render)
```

### What's Happening

**`cell`** holds state — the count is a mutable container (Ch 13).

**`fn`** handles events — arrow functions, no `this` binding, the event object arrives as an argument.

**`swap!`** updates state — the `!` marks the mutation. The function receives the current value and returns the new one.

**`render`** writes to the DOM — `set!` assigns the display's text content. This is the bridge between functional state management and imperative DOM updates.

Every mutation point has a `!`. Every event handler is an `fn`. Every DOM access uses colon syntax. Surface Lykn works in the browser — not by hiding the DOM's imperative nature, but by providing a controlled boundary between functional state and imperative rendering.
