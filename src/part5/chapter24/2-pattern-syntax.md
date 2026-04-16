## Pattern Syntax

The reference tables. The reader will come back to scan these.

### Character Classes

| Pattern | Matches |
|---|---|
| `.` | Any character except newline |
| `\d` | Digit (0–9) |
| `\D` | Non-digit |
| `\w` | Word character (letter, digit, underscore) |
| `\W` | Non-word character |
| `\s` | Whitespace |
| `\S` | Non-whitespace |
| `[abc]` | Any of a, b, c |
| `[^abc]` | Any character NOT a, b, c |
| `[a-z]` | Any character in range a–z |

### Quantifiers

| Pattern | Meaning |
|---|---|
| `*` | Zero or more |
| `+` | One or more |
| `?` | Zero or one |
| `{n}` | Exactly n |
| `{n,}` | n or more |
| `{n,m}` | Between n and m |
| `*?`, `+?`, `??` | Non-greedy (lazy) versions |

### Anchors and Boundaries

| Pattern | Meaning |
|---|---|
| `^` | Start of string (or line with `m` flag) |
| `$` | End of string (or line with `m` flag) |
| `\b` | Word boundary |
| `\B` | Non-word boundary |

### Grouping and Alternation

| Pattern | Meaning |
|---|---|
| `a\|b` | a or b |
| `(...)` | Capture group |
| `(?:...)` | Non-capturing group |
| `(?<name>...)` | Named capture group |

### Complete Examples

```lisp
;; Match a date: YYYY-MM-DD
(bind date-pattern (regex "^(\\d{4})-(\\d{2})-(\\d{2})$"))

;; Match an email (simple)
(bind email-pattern (regex "^\\S+@\\S+\\.\\S+$"))

;; Match a hex color
(bind hex-color (regex "^#([0-9a-fA-F]{3}|[0-9a-fA-F]{6})$"))
```
