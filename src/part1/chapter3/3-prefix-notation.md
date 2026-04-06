## Prefix Notation

The thing that most surprises JavaScript developers about Lykn is not the parentheses — it's where the operator goes. In JavaScript, operators live between their arguments: `1 + 2`. In Lykn, the operator comes first: `(+ 1 2)`. This is prefix notation, and it is older than most programming languages.

### You Already Know Prefix Notation

Here's the thing: JavaScript *already uses* prefix notation for function calls.

```javascript
console.log("hello")        // function first, argument second
Math.max(a, b)              // function first, arguments second
parseInt("42", 10)          // function first, arguments second
```

Lykn just extends this pattern to everything:

```lisp
(console:log "hello")       ;; same shape as JS
(Math:max a b)              ;; same shape as JS
(+ 1 2)                     ;; now operators work the same way too
```

There is exactly one rule for reading any Lykn expression: the first thing in the list is the operator, everything else is an argument. No special cases.

### Variadic Operators

Prefix notation has a practical advantage that infix can't match: operators can take any number of arguments.

```lisp
(+ 1 2 3 4 5)              ;; → 1 + 2 + 3 + 4 + 5
(* a b c)                   ;; → a * b * c
(and x y z)                 ;; → x && y && z
```

In JavaScript, you'd chain the operators manually. In Lykn, you just add arguments to the list.

### Reading Nested Expressions

Here's a JavaScript expression:

```javascript
(a + b) * (c - d) / e
```

In Lykn:

```lisp
(/ (* (+ a b) (- c d)) e)
```

Read it from the inside out. `(+ a b)` adds `a` and `b`. `(- c d)` subtracts `d` from `c`. `(* ...)` multiplies those two results. `(/ ... e)` divides by `e`. Each sub-expression is a self-contained list. The nesting makes the evaluation order explicit — you never need to wonder what happens first.

Yes, there are more parentheses. But there is also zero ambiguity, zero reliance on precedence tables, and zero possibility of the expression meaning something different from what it looks like.
