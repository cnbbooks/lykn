## Kernel Passthrough

Surface Lykn is a superset of kernel Lykn. Any kernel form works in surface code — the surface compiler classifies it as passthrough and sends it through without surface-level analysis.

### Classes Work

```lisp
(class Counter ()
  (constructor ()
    (= this:count 0))

  (increment ()
    (+= this:count 1)
    (return this:count)))

(bind c (new Counter))
(console:log (c:increment))
```

```javascript
class Counter {
  constructor() {
    this.count = 0;
  }
  increment() {
    this.count += 1;
    return this.count;
  }
}
const c = new Counter();
console.log(c.increment());
```

Inside a class body, `this` is available — it's kernel territory. The surface compiler doesn't analyze class methods; the kernel compiler handles them.

### Imperative Loops Work

```lisp
(for (let i 0) (< i items:length) (++ i)
  (process (get items i)))
```

The `for` loop uses kernel `let` (mutable) for the loop variable. Surface `bind` wouldn't work here because the variable needs to be reassigned each iteration.

### `let` Works (But Don't)

```lisp
(let x 0)
(+= x 1)
(console:log x)
```

```javascript
let x = 0;
x += 1;
console.log(x);
```

You *can* use `let` for mutable bindings. But `cell` is almost always better — it's explicit, `!`-marked, and plays well with the rest of the surface language. `let` is for interop situations where the overhead of a cell wrapper isn't justified.

### What Passthrough Loses

When you use kernel forms, you bypass surface analysis. No type checking on parameters. No unused binding detection. No exhaustiveness verification. The tradeoff is honest: kernel forms work, but they're outside the safety net.
