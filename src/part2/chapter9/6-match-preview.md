## A Note on `match`

Many of the control flow patterns in this chapter — nested `if`/`else` chains, `switch` on values, error handling with `Result` — have a better tool waiting in Chapter 10.

```lisp
;; Instead of nested if-else
(match response
  ((Ok data) (process data))
  ((Err e) (handle-error e)))

;; Instead of switch
(match status
  (200 (process-ok))
  (404 (not-found))
  (_ (unknown-status status)))

;; With guards for complex conditions
(match temperature
  (n :when (> n 100) "boiling")
  (n :when (< n 0) "freezing")
  (_ "moderate"))
```

`match` provides exhaustiveness checking — missing a case is a compile error, not a runtime surprise. It provides pattern destructuring — extracting values from tagged objects in the same expression that tests their shape. And it provides guards — arbitrary conditions attached to individual arms.

When you reach for a chain of `if`/`else` that dispatches on shape or value, consider `match` instead. The next chapter covers it in full.
