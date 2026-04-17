## Rendering

DOM rendering with `document:create-element` — no `innerHTML` for user data (XSS safe).

```lisp
(export (func render
  :args (:object state)
  :body
  (render-error (get state :error))
  (render-entries (get state :entries))))

(func render-error
  :args (:any message)
  :body
  (bind el (document:get-element-by-id "error"))
  (set! el:text-content (if (= message null) "" message)))

(func render-entries
  :args (:array entries)
  :body
  (bind container (document:get-element-by-id "entries"))
  (set! container:text-content "")
  (for-of entry entries
    (container:append-child (entry-element entry))))

(func entry-element
  :args (:any entry)
  :returns :any
  :body
  (bind div (document:create-element "div"))
  (set! div:class-name "entry")

  (bind link (document:create-element "a"))
  (set! link:href (template "http://localhost:8080/" entry:code))
  (set! link:target "_blank")
  (set! link:class-name "code")
  (set! link:text-content entry:code)
  (div:append-child link)

  (div:append-child (document:create-text-node (template " → " entry:url)))

  (bind stats (document:create-element "div"))
  (set! stats:class-name "stats")
  (set! stats:text-content (template entry:clicks " clicks"))
  (div:append-child stats)

  (bind btn (document:create-element "button"))
  (set! btn:text-content "Copy")
  (btn:add-event-listener "click" (fn (:any e)
    (navigator:clipboard:write-text
      (template "http://localhost:8080/" entry:code))
    (set! btn:text-content "Copied!")
    (set-timeout (fn () (set! btn:text-content "Copy")) 1500)))
  (div:append-child btn)

  div)
```

Every element created programmatically. `set!` for DOM property assignment. `text-content` escapes automatically. The render is destructive (clear + rebuild) — simple and correct for a small app.
