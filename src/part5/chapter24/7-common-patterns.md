## Common Patterns

Quick-reference for patterns developers actually use.

```lisp
;; Trim whitespace (use str:trim instead, but for illustration)
(bind text "  hello  ")
(bind trimmed (text:replace (regex "^\\s+|\\s+$" "g") ""))

;; Extract all numbers from text
(bind text "I have 3 cats and 12 dogs")
(for-of m (text:match-all (regex "\\d+" "g"))
  (console:log (get m 0)))

;; Validate URL (simple)
(bind url-rx (regex "^https?://\\S+" "i"))

;; Split on multiple delimiters
(bind input "one;two,three four")
(bind parts (input:split (regex "[;,\\s]+")))
;; → ["one", "two", "three", "four"]
```

### A Note on Validation

For serious validation — emails, URLs, phone numbers, dates — use purpose-built libraries or the platform's built-in APIs (`URL` constructor, `Intl.DateTimeFormat`). Regex covers common patterns but not edge cases. The email regex that handles every RFC-compliant address is 6,000 characters long. Nobody writes that by hand.
