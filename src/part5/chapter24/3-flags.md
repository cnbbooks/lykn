## Flags

| Flag | Meaning |
|---|---|
| `g` | Global — find all matches, not just first |
| `i` | Case-insensitive |
| `m` | Multiline — `^`/`$` match line boundaries |
| `s` | Dotall — `.` matches newline too |
| `u` | Unicode — proper Unicode matching |
| `v` | Unicode sets (ES2024) — set operations in character classes |
| `d` | Indices — capture group positions in result |
| `y` | Sticky — match from `lastIndex` only |

### The Unicode Recommendation

Always use the `u` or `v` flag for new code. Without it, regex treats surrogate pairs as two characters — the same Unicode issue from Chapter 11 (strings). The `v` flag (ES2024) is the modern replacement for `u`, adding set operations within character classes.

```lisp
(bind emoji (regex "\\p{Emoji}" "gu"))  ;; Unicode property escape
```
