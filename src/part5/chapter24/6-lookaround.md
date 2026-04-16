## Lookaround

Assertions that match a position without consuming characters.

| Pattern | Name | Meaning |
|---|---|---|
| `(?=...)` | Positive lookahead | Followed by ... |
| `(?!...)` | Negative lookahead | NOT followed by ... |
| `(?<=...)` | Positive lookbehind | Preceded by ... |
| `(?<!...)` | Negative lookbehind | NOT preceded by ... |

```lisp
;; Match a number followed by "px" (but don't capture "px")
(bind rx (regex "\\d+(?=px)"))
(bind text "width: 16px")
(bind m (rx:exec text))
(console:log (get m 0))    ;; → "16"

;; Match digits NOT preceded by "$"
(bind rx2 (regex "(?<!\\$)\\d+" "g"))
(bind text2 "price $42 count 7")
(for-of m (text2:match-all rx2)
  (console:log (get m 0)))  ;; → "2", "7"  (not "42")
```

Lookaround is powerful for extracting values from context without including the context in the match. Use lookahead when you care about what follows; lookbehind when you care about what precedes.
