## Capture Groups

### Numbered Groups

`(...)` captures and assigns a number:

```lisp
(bind rx (regex "(\\w+)@(\\w+\\.\\w+)"))
(bind m (rx:exec "alice@example.com"))
(console:log (get m 1))    ;; → "alice"
(console:log (get m 2))    ;; → "example.com"
```

### Named Groups

`(?<name>...)` for self-documenting captures:

```lisp
(bind rx (regex "(?<year>\\d{4})-(?<month>\\d{2})-(?<day>\\d{2})"))
(bind m (rx:exec "2026-04-15"))
(console:log m:groups:year)     ;; → "2026"
(console:log m:groups:month)    ;; → "04"
(console:log m:groups:day)      ;; → "15"
```

### Named Groups with Destructuring

The match result's `groups` property works with Lykn destructuring:

```lisp
(bind rx (regex "(?<year>\\d{4})-(?<month>\\d{2})-(?<day>\\d{2})"))
(bind (object (alias groups (object year month day)))
  (rx:exec "2026-04-15"))
(console:log year month day)
```

This is where Lykn's destructuring (Ch 15) and regex interact productively — named captures flow directly into bindings.
