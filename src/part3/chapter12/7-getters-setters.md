## Getters and Setters

Accessor properties look like data but run code when accessed or assigned.

```lisp
(class Rectangle ()
  (constructor (width height)
    (assign this:width width)
    (assign this:height height))

  (get area ()
    (return (* this:width this:height))))

(bind r (new Rectangle 10 5))
(console:log r:area)           ;; → 50
```

```javascript
class Rectangle {
  constructor(width, height) {
    this.width = width;
    this.height = height;
  }
  get area() {
    return this.width * this.height;
  }
}
const r = new Rectangle(10, 5);
console.log(r.area);           // → 50
```

`r:area` looks like a property access — no parentheses, no arguments. But `area` is a getter that runs a computation every time it's read. The colon syntax works identically for data properties and accessor properties; the difference is invisible at the call site.

Setters work the same way, using `set` instead of `get` in the class definition. Both appear primarily in class bodies (kernel passthrough territory). Their full treatment comes in Chapter 20 (Classes).
