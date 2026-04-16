## Math

The `Math` namespace — constants and functions, all via colon syntax.

### Constants

```lisp
Math:PI              ;; → 3.141592653589793
Math:E               ;; → 2.718281828459045
Math:SQRT2           ;; → 1.4142135623730951
```

### Common Operations

```lisp
;; Rounding
(Math:floor 4.7)     ;; → 4
(Math:ceil 4.2)      ;; → 5
(Math:round 4.5)     ;; → 5
(Math:trunc 4.7)     ;; → 4 (toward zero)

;; Basics
(Math:abs -5)        ;; → 5
(Math:max 1 5 3)     ;; → 5
(Math:min 1 5 3)     ;; → 1

;; Powers and roots
(Math:pow 2 10)      ;; → 1024 (or use (** 2 10))
(Math:sqrt 16)       ;; → 4

;; Logarithms
(Math:log 100)       ;; → natural log (ln)
(Math:log10 100)     ;; → 2
```

### Random Numbers

```lisp
;; Random float in [0, 1)
(Math:random)

;; Random integer in [min, max]
(func random-int
  :args (:number min :number max)
  :returns :number
  :body (+ min (Math:floor (* (Math:random) (+ (- max min) 1)))))
```

### The Floating-Point Trap

```lisp
(console:log (= (+ 0.1 0.2) 0.3))   ;; → false!
(console:log (+ 0.1 0.2))            ;; → 0.30000000000000004
```

IEEE 754 double-precision floating-point cannot represent `0.1` exactly. The error accumulates through arithmetic. This affects every programming language that uses doubles — it's not a JavaScript bug.

For financial calculations, work in cents (integers) and convert for display. For exact integer arithmetic beyond the safe range (2⁵³ - 1), use `BigInt`:

```lisp
(bind big (BigInt 9007199254740993))
(console:log (+ big (BigInt 1)))    ;; → exact
```
