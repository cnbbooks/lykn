## Using Regex: Methods

Two families of methods use regular expressions: regex methods (called on the pattern) and string methods (called on the string).

### Regex Methods

```lisp
;; test — boolean match
(bind digits (regex "^\\d+$"))
(console:log (digits:test "42"))       ;; → true
(console:log (digits:test "hello"))    ;; → false

;; exec — detailed match with groups
(bind date-rx (regex "(\\d{4})-(\\d{2})-(\\d{2})"))
(bind m (date-rx:exec "2026-04-15"))
(console:log (get m 0))                ;; → "2026-04-15" (full match)
(console:log (get m 1))                ;; → "2026" (group 1)
```

### String Methods

```lisp
(bind input "hello world foo bar")

;; match — all matches with g flag
(bind matches (input:match (regex "\\w+" "g")))
;; → ["hello", "world", "foo", "bar"]

;; search — index of first match
(bind idx (input:search (regex "world")))
;; → 6
```

For `replace` and `split`, bind the string first:

```lisp
(bind messy "  hello   world  ")
(bind clean (messy:replace (regex "\\s+" "g") " "))
;; → " hello world "

(bind csv "a, b,  c")
(bind parts (csv:split (regex "\\s*,\\s*")))
;; → ["a", "b", "c"]
```

### `match-all` — The Modern Approach

For iterating all matches, `match-all` returns an iterator:

```lisp
(bind text "The year 2026 in month 04 on day 15")
(for-of m (text:match-all (regex "(\\d+)" "g"))
  (console:log (get m 0)))
;; → "2026", "04", "15"
```

`match-all` requires the `g` flag. It's cleaner than a `while` loop with `exec` and produces rich match objects with group information.
