## The Parser

Parse Markdown source into a list of `Block` values.

### The Main Loop

```lisp
(func parse-markdown
  :args (:string source)
  :returns :array
  :body
  (bind lines (source:split "\n"))
  (bind blocks (cell #a()))
  (bind i (cell 0))
  (while (< (express i) lines:length)
    (bind line (get lines (express i)))
    (bind (object block consumed) (parse-block lines (express i)))
    (swap! blocks (fn (:array bs) (conj bs block)))
    (swap! i (fn (:number n) (+ n consumed))))
  (express blocks))
```

Each iteration: read the current line, identify the block type, produce a `Block` value, advance by the number of lines consumed.

### Block Detection

```lisp
(func parse-block
  :args (:array lines :number start)
  :returns :object
  :body
  (bind line (get lines start))
  (if (line:match (regex "^#{1,6} "))
    (parse-heading line)
    (if (line:starts-with "```")
      (parse-code-block lines start)
      (if (line:starts-with "- ")
        (parse-list lines start)
        (if (line:starts-with "> ")
          (parse-blockquote lines start)
          (if (= (line:trim) "")
            (obj :block (Empty) :consumed 1)
            (parse-paragraph lines start)))))))
```

### Heading Parser

The simplest block parser:

```lisp
(func parse-heading
  :args (:string line)
  :returns :object
  :body
  (bind m (line:match (regex "^(#{1,6}) (.+)$")))
  (obj :block (Heading (get m 1):length (get m 2)) :consumed 1))
```

Regex captures the `#` characters and the text. The heading level is the length of the capture group.

### Code Block Parser

Multi-line — scans forward to the closing fence:

```lisp
(func parse-code-block
  :args (:array lines :number start)
  :returns :object
  :body
  (bind first (get lines start))
  (bind lang ((first:slice 3):trim))
  (bind end (cell (+ start 1)))
  (while (and (< (express end) lines:length)
              (not ((get lines (express end)):starts-with "```")))
    (swap! end (fn (:number n) (+ n 1))))
  (bind code (-> (lines:slice (+ start 1) (express end))
               (:join "\n")))
  (obj :block (CodeBlock lang code)
       :consumed (+ (- (express end) start) 1)))
```

The pattern: each parser function takes the lines array and a start index, returns a `Block` and the number of lines consumed.
