## Cells: Controlled Mutation

Four forms, one concept. Cells are the only mutation mechanism in surface Lykn.

### The Four Forms

| Form | Purpose | Compiled output |
|---|---|---|
| `(cell value)` | Create mutable container | `{value: value}` |
| `(express c)` | Read current value | `c.value` |
| `(swap! c f)` | Update via function | `c.value = f(c.value)` |
| `(reset! c v)` | Replace value directly | `c.value = v` |

### In Action

```lisp
(bind counter (cell 0))

;; Read
(console:log (express counter))   ;; → 0

;; Update via function
(swap! counter (fn (:number n) (+ n 1)))
(console:log (express counter))   ;; → 1

;; Replace directly
(reset! counter 100)
(console:log (express counter))   ;; → 100
```

```javascript
const counter = {value: 0};

console.log(counter.value);

counter.value = ((n) => {
  if (typeof n !== "number" || Number.isNaN(n))
    throw new TypeError(
      "anonymous: arg 'n' expected number, got " + typeof n);

  return n + 1;
})(counter.value);
console.log(counter.value);

counter.value = 100;
console.log(counter.value);
```

### What Makes Cells Different

**`bind` is still `const`.** The cell itself can't be reassigned. Only its `.value` can change. The binding is immutable; the container's content is mutable. This is the same distinction JavaScript's `const` makes — but in Lykn, the mutability is concentrated in one place and marked with a `!`.

**`!` means mutation.** Every mutating form has a `!` suffix: `swap!`, `reset!`. If a form name doesn't end in `!`, it's pure. A code reviewer scanning a Lykn file can spot every mutation point by searching for `!`. This is Scheme convention, adopted by Clojure.

**`swap!` takes a function, not a value.** This is the most important detail. `(swap! counter 5)` is not valid. You write `(swap! counter (fn (:number n) (+ n 5)))` or, for simple replacement, `(reset! counter 5)`. The distinction: `swap!` is read-modify-write (the function receives the current value); `reset!` is just write (the old value is ignored).

**No runtime library.** `cell` compiles to `{value: x}`. `express` compiles to `.value`. Any JavaScript code can read or write the property. Zero dependencies, zero magic.

### Heritage

`cell` from Rust's `Cell<T>` and ML's `ref` cells. `express` from biology — gene expression reads information from a cell without altering it. `swap!` and `reset!` from Clojure's atom operations with the same semantics.
