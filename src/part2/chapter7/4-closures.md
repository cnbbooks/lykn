## Closures

A function captures the bindings from its enclosing scope. The captured environment travels with the function wherever it goes. This is a closure, and it is the mechanism that makes functional programming work.

### The Pure Pattern

```lisp
(func make-greeter
  :args (:string prefix)
  :returns :function
  :body (fn (:string name) (template prefix ", " name "!")))

(bind hello (make-greeter "Hello"))
(bind howdy (make-greeter "Howdy"))

(console:log (hello "World"))    ;; → "Hello, World!"
(console:log (howdy "Partner"))  ;; → "Howdy, Partner!"
```

`hello` and `howdy` are closures. Each one remembers the `prefix` it was created with. `hello` always knows that `prefix` is `"Hello"`. `howdy` always knows that `prefix` is `"Howdy"`. The value is captured at creation time and doesn't change.

### The Stateful Pattern

Closures can also capture cells — creating functions with mutable internal state:

```lisp
(func make-counter
  :args (:number start)
  :returns :function
  :body
  (bind count (cell start))
  (fn ()
    (swap! count (fn (:number n) (+ n 1)))
    (express count)))

(bind counter (make-counter 0))
(counter)  ;; → 1
(counter)  ;; → 2
(counter)  ;; → 3
```

Each call to `counter` updates the same cell. The cell is captured by the closure, not copied. This is the standard pattern for encapsulated state in functional languages — the state is invisible from outside, accessible only through the returned function.

### Why Immutability Helps

In JavaScript, a closure over a `let` variable can be surprised by a later reassignment:

```javascript
let greeting = "Hello";
const greet = (name) => `${greeting}, ${name}!`;
greeting = "Goodbye";
greet("World");  // → "Goodbye, World!" — surprise!
```

In Lykn, `bind` is `const`. The value a closure captures will never change behind its back (unless the captured value is a cell, in which case the mutation is explicit and deliberate). Pure closures in Lykn are safe by default.

### The Lambda Papers Connection

Closures are what make lambda powerful. A lambda that can't capture its environment is just a code block — useful for control flow, but not for abstraction. A lambda that captures its environment is something richer: it has state (the captured bindings) and behaviour (the body). This is the insight Steele and Sussman articulated in the Lambda Papers: actors and lambdas are the same thing. An object with one method is a closure. A closure with mutable state is an object. The difference is syntax, not substance.
