## Events

Event handling is how browser apps respond to user interaction. This is the most important browser section.

### Adding Listeners

```lisp
(button:add-event-listener "click"
  (fn (:any event)
    (console:log "Clicked!" event:target)))
```

`fn` produces an arrow function — no `this` binding, which is exactly right for DOM event listeners. `event:target` gives you the element that triggered the event; `event:current-target` gives you the element the listener is attached to.

### Removing Listeners

```lisp
(func handle-click
  :args (:any event)
  :body (console:log "Clicked!"))

(button:add-event-listener "click" handle-click)
(button:remove-event-listener "click" handle-click)
```

To remove a listener, you need a reference to the same function. Anonymous `fn` can't be removed — use a named `func` when removal is needed.

### Event Object

```lisp
event:type                  ;; "click", "keydown", etc.
event:target                ;; element that triggered the event
event:current-target        ;; element the listener is on
(event:prevent-default)     ;; cancel default behaviour
(event:stop-propagation)    ;; stop bubbling
```

### Event Delegation

Attach one listener to a parent, handle events from children:

```lisp
(bind list (document:get-element-by-id "todo-list"))
(list:add-event-listener "click"
  (fn (:any event)
    (bind target event:target)
    (if (= target:tag-name "LI")
      (target:class-list:toggle "done"))))
```

One listener instead of many. Handles dynamically added elements. Efficient and composable.

### Common Events

`click`, `input`, `change`, `submit`, `keydown`, `keyup`, `focus`, `blur`, `load`, `DOMContentLoaded`, `scroll`, `resize`.
