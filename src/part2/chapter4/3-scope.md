## Scope

Even though `bind` simplifies declarations, it compiles to `const`, which means JavaScript's scope rules apply. The good news is that `const`'s rules are the *good* rules — the ones JavaScript got right on the second try.

### Block Scope

A `bind` is visible only within the block where it's declared. A block is any pair of braces in the compiled output — an `if` body, a `for` body, a function body:

```lisp
(bind x 10)

(if (> x 5)
  (block
    (bind y 20)
    (console:log (+ x y)))    ;; y is visible here → 30
  (block
    (console:log y)))          ;; y is NOT visible here → error
```

The compiled JavaScript:

```javascript
const x = 10;
if (x > 5) {
  const y = 20;
  console.log(x + y);
} else {
  console.log(y);             // ReferenceError: y is not defined
}
```

This is exactly how `const` works in JavaScript. No surprises, no special Lykn behavior.

### Lexical Scope

Inner scopes can see outer bindings. Outer scopes cannot see inner bindings. The visibility of a name is determined by where it appears in the source text — not by when or how the code executes. This is lexical scoping, and it's the same in Lykn, JavaScript, Scheme, and virtually every modern language.

```lisp
(bind greeting "Hello")

(func greet
  :args (:string name)
  :returns :string
  :body (template greeting ", " name "!"))

(greet "World")  ;; → "Hello, World!" — greeting is visible inside greet
```

### Closures

A function captures the bindings from its enclosing scope. This captured environment travels with the function wherever it goes:

```lisp
(func make-greeter
  :args (:string prefix)
  :returns :function
  :body (fn (:string name) (template prefix ", " name "!")))

(bind hello (make-greeter "Hello"))
(bind howdy (make-greeter "Howdy"))

(console:log (hello "World"))   ;; → "Hello, World!"
(console:log (howdy "Partner")) ;; → "Howdy, Partner!"
```

`hello` and `howdy` are closures. Each one remembers the `prefix` it was created with. This is the mechanism that makes functional programming work — functions carry their context with them, which means they can be passed around, stored in data structures, and called later, and they'll still know what `prefix` means.

Closures get their full treatment in Chapter 7 (Functions). For now, the essential point: because `bind` is immutable, closures in Lykn are safe. The value a closure captures will never change behind its back. In JavaScript, a closure over a `let` variable can be surprised by a later reassignment. In Lykn, the value is the value.

### No Hoisting

`bind` has no hoisting behavior. The name doesn't exist until the execution reaches the `bind` form. There is no temporal dead zone because there is no period where the name "exists but is inaccessible" — it simply doesn't exist yet.

In JavaScript, `var` is hoisted (the name exists from the start of the function, initialized to `undefined`). `let` and `const` have the temporal dead zone — the name exists from the start of the block but accessing it before the declaration throws a `ReferenceError`. `bind` avoids the entire question: the surface compiler doesn't hoist anything. The name appears at the point where you wrote it, and that's that.

If you use kernel forms directly (`const`, `let`), you get JavaScript's native scoping behavior, including the temporal dead zone. But in surface Lykn, there's just `bind` and the simple rule: it exists from where you declared it, not before.
