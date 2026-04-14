## Functions as Values

Functions in JavaScript — and therefore in Lykn — are first-class values. They can be bound to names, passed as arguments, returned from other functions, and stored in data structures.

### Binding Functions

```lisp
(func double
  :args (:number x)
  :returns :number
  :body (* x 2))

;; Bind an existing function to a new name
(bind transform double)
(transform 5)  ;; → 10

;; Bind an anonymous function
(bind increment (fn (:number x) (+ x 1)))
(increment 5)  ;; → 6
```

### Functions in Data Structures

```lisp
(bind operations (obj
  :add (fn (:number a :number b) (+ a b))
  :sub (fn (:number a :number b) (- a b))
  :mul (fn (:number a :number b) (* a b))))

((get operations :add) 3 4)  ;; → 7
((get operations :mul) 3 4)  ;; → 12
```

### Why This Matters

First-class functions are why `fn` exists as a separate form. If functions couldn't be values, you'd only ever need `func` — named, declared, called by name. But functions *are* values, and that means you need a way to create them inline, without a name, as arguments to other functions. That's `fn`.

This is also why the Lisp tradition calls functions "first-class citizens" — they have the same rights as any other value. They can go anywhere a number or string can go. The lambda calculus is built on this principle: everything is a function, and functions can operate on other functions. JavaScript inherited this from Scheme. Lykn inherited it from both.
