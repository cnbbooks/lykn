## Higher-Order Functions

A higher-order function is one that takes a function as an argument, returns a function, or both. The reader has already seen closures (which return functions) and callbacks (which accept them). This section makes the pattern explicit.

### Map, Filter, Reduce

The three workhorses of functional data transformation:

```lisp
(bind numbers #a(1 2 3 4 5))

;; Transform every element
(bind doubled (numbers:map (fn (:number x) (* x 2))))
;; → [2, 4, 6, 8, 10]

;; Keep matching elements
(bind evens (numbers:filter (fn (:number x) (= (% x 2) 0))))
;; → [2, 4]

;; Accumulate into a single value
(bind total (numbers:reduce (fn (:number acc :number x) (+ acc x)) 0))
;; → 15
```

These are JavaScript's `Array.prototype` methods, called via colon syntax. The `fn` is the transformation, predicate, or accumulator — passed as an argument, called by the higher-order function.

### Named Functions as Arguments

You don't have to use anonymous functions. Named functions compose just as well:

```lisp
(func double
  :args (:number x)
  :returns :number
  :body (* x 2))

(func is-even
  :args (:number x)
  :returns :boolean
  :body (= (% x 2) 0))

(bind result (-> numbers
  (:filter is-even)
  (:map double)))
;; → [4, 8]
```

The threading macro `->` (covered fully in Chapter 13) pipes the array through a sequence of method calls. Each step is readable, and the named functions serve as self-documenting predicates and transformations.

### Building Abstractions

Higher-order functions are how you build abstractions without classes. Instead of inheriting behaviour, you compose it:

```lisp
(func apply-twice
  :args (:function f :any x)
  :returns :any
  :body (f (f x)))

(apply-twice (fn (:number x) (+ x 1)) 5)   ;; → 7
(apply-twice (fn (:string s) (+ s "!")) "hello")  ;; → "hello!!"
```

The function doesn't know what `f` does. It doesn't need to. It just applies it twice. This is the composability that makes functional programming powerful — small, generic functions combined into complex behaviours.
