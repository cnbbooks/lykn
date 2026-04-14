## Threading Macros: `->` and `->>`

Pipeline composition. Threading macros take a value and pass it through a series of transformations, eliminating deeply nested function calls.

### `->` Thread-First

Inserts the threaded value as the *first* argument of each step:

```lisp
(-> 5 (+ 3) (* 2))
```

```javascript
(5 + 3) * 2   // → 16
```

The value `5` is threaded into `(+ 3)` as the first argument → `(+ 5 3)` → `8`. Then `8` is threaded into `(* 2)` → `(* 8 2)` → `16`.

### Method Calls in Threading

Use `(:method-name)` to call a method on the threaded value:

```lisp
(-> "hello" (:to-upper-case))
```

```javascript
"hello".toUpperCase()   // → "HELLO"
```

A more complete example:

```lisp
(-> user
  (get :name)
  (:to-upper-case)
  (:slice 0 3))
```

This reads: take `user`, get its `:name`, uppercase it, take the first 3 characters. Each step flows naturally from the previous one.

### `->>` Thread-Last

Inserts the threaded value as the *last* argument. Used for collection pipelines where the collection comes last:

```lisp
(->> items
  (:filter (fn (:number x) (> x 0)))
  (:map (fn (:number x) (* x 2))))
```

### When to Use Which

`->` for object/method chains — the subject comes first. `->>` for collection pipelines — the collection comes last. This follows Clojure convention, where `->` and `->>` have the same semantics.

### Heritage

Threading macros are Clojure heritage. `->` and `->>` are standard Clojure forms, adopted by virtually every Clojure-influenced language. The semantics are identical — Lykn adds nothing and changes nothing.
