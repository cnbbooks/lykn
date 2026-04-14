## The Conditional Expression

JavaScript's ternary operator (`test ? then : else`) becomes a three-argument form in Lykn:

```lisp
(? (> count 1) "items" "item")
```

```javascript
count > 1 ? "items" : "item"
```

### When to Use It

The conditional expression is for simple, inline choices — anywhere you'd use a ternary in JavaScript:

```lisp
(bind label (? (> count 1) "items" "item"))
(bind status (? active "online" "offline"))
(bind sign (? (< n 0) "negative" "non-negative"))
```

```javascript
const label = count > 1 ? "items" : "item";
const status = active ? "online" : "offline";
const sign = n < 0 ? "negative" : "non-negative";
```

### When Not to Use It

For anything more complex than a single expression per branch, use `if` (Chapter 9) or `match` (Chapter 10). Nested ternaries are as unreadable in Lykn as they are in JavaScript — possibly more so, since the nested parentheses compound the confusion rather than relieving it.

```lisp
;; Don't do this
(? (< x 0) "negative" (? (> x 0) "positive" "zero"))

;; Do this instead
(if (< x 0)
  "negative"
  (if (> x 0) "positive" "zero"))
```
