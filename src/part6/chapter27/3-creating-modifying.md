## Creating and Modifying Elements

### Creating

```lisp
(bind div (document:create-element "div"))
(set! div:class-name "card")
(set! div:text-content "Hello!")

(bind container (document:get-element-by-id "app"))
(container:append-child div)
```

### Attributes and Classes

```lisp
(div:set-attribute "data-id" "42")

;; classList API — chained colon syntax
(div:class-list:add "active" "visible")
(div:class-list:remove "hidden")
(div:class-list:toggle "selected")
```

### Style

```lisp
(set! div:style:color "blue")
(set! div:style:font-size "16px")
```

### innerHTML vs textContent

`text-content` for plain text — safe from XSS. `inner-HTML` for HTML strings — dangerous with user input. Prefer creating elements programmatically over `innerHTML`.

### Batch Insertion

Document fragments minimize DOM updates:

```lisp
(bind frag (document:create-document-fragment))
(for-of item items
  (bind el (document:create-element "li"))
  (set! el:text-content item)
  (frag:append-child el))
(list:append-child frag)  ;; single DOM update
```
