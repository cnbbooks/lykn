## Primitives Are Values

Primitive types have three properties that distinguish them from objects, and these properties matter for how you think about `bind`:

### Immutable

You cannot modify a primitive. You cannot change the third character of a string. You cannot make `42` become `43`. You can only create new primitives. When you write `(+ x 1)`, you don't modify `x` — you produce a new number.

This means `bind` + primitives is truly immutable in every sense. The binding can't be reassigned (that's `const`), and the value can't be modified (that's how primitives work). There is no backdoor, no mutation through a reference, no `const`-but-actually-mutable gotcha.

### Compared by Value

Two primitives with the same content are equal:

```lisp
(= "hello" "hello")     ;; → true
(= 42 42)               ;; → true
```

Two objects with the same content are *not* equal — they're different objects:

```javascript
[1, 2] === [1, 2]       // → false (different arrays)
{a: 1} === {a: 1}       // → false (different objects)
```

This distinction becomes important in Chapter 9 (Arrays) and Chapter 12 (Objects). For now: primitives compare by what they contain; objects compare by *which one* they are.

### Passed by Value

Assigning a primitive to a new binding copies the value. Changing the copy doesn't affect the original — because you can't change a primitive anyway. This makes reasoning about primitive bindings trivially simple: the value is what it is, wherever you look at it, forever.

The combination of `bind` (immutable binding) and primitives (immutable values) is the safest possible foundation. No mutation. No aliasing. No action at a distance. This is why Lykn starts here — the simple case where immutability is complete and unambiguous — before introducing objects, where `const` prevents reassignment but not mutation, and where `cell`, `assoc`, and `dissoc` become necessary.
