## The Renderer

Render a list of `Block` values to HTML.

### Block Rendering

```lisp
(func render-blocks
  :args (:array blocks)
  :returns :string
  :body
  (->> blocks
    (:map render-block)
    (:filter (fn (:string s) (not (= s ""))))
    (:join "\n")))

(func render-block
  :args (:any block)
  :returns :string
  :body
  (match block
    ((Heading level text)
     (template "<h" level ">" (render-inline text) "</h" level ">"))
    ((Paragraph text)
     (template "<p>" (render-inline text) "</p>"))
    ((CodeBlock language code)
     (template "<pre><code class=\"language-" language "\">"
       (escape-html code) "</code></pre>"))
    ((ListBlock items)
     (template "<ul>\n"
       (->> items
         (:map (fn (:string item) (template "  <li>" (render-inline item) "</li>")))
         (:join "\n"))
       "\n</ul>"))
    ((Blockquote text)
     (template "<blockquote>" (render-inline text) "</blockquote>"))
    ((Empty) "")))
```

Every variant of `Block` gets its own rendering arm. The compiler checks exhaustiveness — add a variant, the renderer won't compile until you handle it.

### Inline Rendering

Regex pipeline for bold, italic, code, and links:

```lisp
(func render-inline
  :args (:string text)
  :returns :string
  :body
  (-> text
    (escape-html)
    (:replace (regex "`([^`]+)`" "g") "<code>$1</code>")
    (:replace (regex "\\*\\*([^*]+)\\*\\*" "g") "<strong>$1</strong>")
    (:replace (regex "\\*([^*]+)\\*" "g") "<em>$1</em>")
    (:replace (regex "\\[([^\\]]+)\\]\\(([^)]+)\\)" "g") "<a href=\"$2\">$1</a>")))

(func escape-html
  :args (:string text)
  :returns :string
  :body
  (-> text
    (:replace (regex "&" "g") "&amp;")
    (:replace (regex "<" "g") "&lt;")
    (:replace (regex ">" "g") "&gt;")))
```

The threading macro makes the pipeline readable: escape, replace code, replace bold, replace italic, replace links. Each step transforms the string.
