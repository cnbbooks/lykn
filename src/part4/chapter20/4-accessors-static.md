## Accessors and Static Members

### Getters and Setters

`get` and `set` markers before the method name:

```lisp
(class Circle ()
  (field -radius 0)

  (constructor (r)
    (assign this:-radius r))

  (get area ()
    (return (* Math:PI this:-radius this:-radius)))

  (set radius (r)
    (if (< r 0)
      (throw (new Error "Radius cannot be negative")))
    (assign this:-radius r)))
```

`circle:area` looks like a property access but runs a computation. `(= circle:radius 10)` looks like assignment but runs validation.

### Static Members

The `static` wrapper:

```lisp
(class MathUtils ()
  (static (add (a b) (return (+ a b))))
  (static (field PI 3.14159)))
```

```javascript
class MathUtils {
  static add(a, b) { return a + b; }
  static PI = 3.14159;
}
```

Static members belong to the class itself, not to instances. Access via the class name: `MathUtils:add`, `MathUtils:PI`.
