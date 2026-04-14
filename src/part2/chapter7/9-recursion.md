## Recursion

Named functions can call themselves:

```lisp
(func factorial
  :args (:number n)
  :returns :number
  :body (if (<= n 1)
          1
          (* n (factorial (- n 1)))))

(factorial 5)  ;; → 120
```

```javascript
function factorial(n) {
  // ... type check ...
  if (n <= 1) return 1;
  return n * factorial(n - 1);
}
```

### A Practical Note

JavaScript's specification includes tail call optimization (TCO) — the optimization that makes deep recursion safe by reusing stack frames. In practice, only Safari implements it. All other engines will stack-overflow on deep recursion.

For algorithms that recurse deeply, use iteration (kernel `for` or `while` forms) or trampolining (a technique where recursive calls return thunks that are evaluated iteratively). For most practical recursion — tree traversals, recursive data structures, algorithms with bounded depth — the stack is fine.
