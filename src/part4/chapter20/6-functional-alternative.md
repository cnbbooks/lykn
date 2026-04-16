## The Functional Alternative

The same problem, two solutions.

### With Classes

```lisp
(class Circle ()
  (constructor (r) (assign this:r r))
  (area () (return (* Math:PI this:r this:r))))

(class Rect ()
  (constructor (w h) (assign this:w w) (assign this:h h))
  (area () (return (* this:w this:h))))

(bind shapes #a((new Circle 5) (new Rect 3 4)))
(bind areas (shapes:map (fn (:any s) (s:area))))
```

### With `type` + `match`

```lisp
(type Shape
  (Circle :number radius)
  (Rect :number width :number height))

(func area
  :args (:any shape)
  :returns :number
  :body (match shape
    ((Circle r) (* Math:PI r r))
    ((Rect w h) (* w h))))

(bind shapes #a((Circle 5) (Rect 3 4)))
(bind areas (shapes:map (fn (:any s) (area s))))
```

### The Comparison

The `type`/`match` version:
- No `this`, no `new`, no inheritance chain
- **Exhaustive `match`** — add a `Triangle` variant, the compiler tells you everywhere you forgot to handle it
- **Functions separate from data** — add new operations without modifying the type
- **Data is transparent** — `console.log` shows `{tag: "Circle", radius: 5}`, not `Circle {}`

The class version:
- Familiar to OOP developers
- Required by some JS frameworks
- **Engine-enforced privacy** via `#_` private fields
- Supports `instanceof`

### The Recommendation

Start with `type`/`match`. The compiler catches missing cases. The data is inspectable. The functions are composable. Reach for classes when interop, frameworks, or engine-enforced privacy require it.

Neither is wrong. But in a language that provides exhaustive pattern matching, the class hierarchy is rarely the tool you need first.
