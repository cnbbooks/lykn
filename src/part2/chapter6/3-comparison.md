## Comparison Operators

### The Four Comparisons

| Lykn | JS | Operation |
|---|---|---|
| `(< a b)` | `a < b` | Less than |
| `(> a b)` | `a > b` | Greater than |
| `(<= a b)` | `a <= b` | Less than or equal |
| `(>= a b)` | `a >= b` | Greater than or equal |

These work on numbers (numeric comparison) and strings (lexicographic comparison, by UTF-16 code unit). Comparing values of different types triggers JavaScript's coercion rules — another reason to type your function parameters.

```lisp
(bind eligible (>= age 18))
(bind first-alphabetically (< name-a name-b))
```

```javascript
const eligible = age >= 18;
const firstAlphabetically = nameA < nameB;
```

### Equality

Equality was covered in Chapter 5 and doesn't change here: `(= a b)` compiles to `a === b`. `(js:eq a b)` compiles to `a == b`. Use the first one. Always.
