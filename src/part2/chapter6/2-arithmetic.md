## Arithmetic Operators

### The Six Operations

| Lykn | JS | Operation |
|---|---|---|
| `(+ a b)` | `a + b` | Addition |
| `(- a b)` | `a - b` | Subtraction |
| `(* a b)` | `a * b` | Multiplication |
| `(/ a b)` | `a / b` | Division |
| `(% a b)` | `a % b` | Remainder |
| `(** a b)` | `a ** b` | Exponentiation |

All six compile to their JavaScript counterparts. The semantics are JavaScript's — IEEE 754 floating-point arithmetic, with all the precision implications that entails.

### A Note on `%`

JavaScript's `%` is a *remainder* operator, not a modulo operator. The difference matters for negative numbers: `(-7 % 3)` produces `-1` in JavaScript (the sign follows the dividend), while a true modulo operation would produce `2`. If you need mathematical modulo, use `((+ (% a b) b) % b)` or write a utility function.

### Unary Negation

A single-argument `-` produces unary negation:

```lisp
(- x)                 ;; → -x
(- (- x))             ;; → -(-x)   (double negation)
```

### Real Examples

```lisp
(bind total (+ price (* quantity tax-rate)))
(bind average (/ (+ a b c) 3))
(bind is-even (= (% n 2) 0))
(bind area (* Math:PI (** radius 2)))
```

```javascript
const total = price + quantity * taxRate;
const average = (a + b + c) / 3;
const isEven = n % 2 === 0;
const area = Math.PI * radius ** 2;
```

Remember from Chapter 5: `+` is overloaded for string concatenation in JavaScript. `(+ "5" 3)` produces `"53"`, not `8`. Type keywords on function boundaries catch this at the gate; inside a function body, the coercion rules apply as they do in JavaScript.
