## The `js:` Namespace

The primary escape hatch. `js:` is a colon-namespace prefix recognized by the surface compiler. Forms starting with `js:` bypass surface safety for specific, controlled purposes.

### `js:eq` — Loose Equality

```lisp
(js:eq a b)              ;; → a == b
(js:eq x null)           ;; → x == null
```

```javascript
a == b;
x == null;
```

The only way to get `==` in surface Lykn. `(= a b)` compiles to `===` (Ch 5). `js:eq` is for the rare cases where loose equality is genuinely needed — most commonly `x == null` to check for both `null` and `undefined` in one test.

Note: the compiler *already generates* `== null` checks internally for `some->`, `if-let`, and `when-let` (Ch 13). `js:eq` is for cases where *you* need it in your own code.

### `js:bind` — Method Binding

```lisp
(bind bound-method (js:bind obj:method obj))
```

For extracting a method from an object while preserving its `this` binding. Without binding, calling the extracted method would lose its context — BugAID's pattern #10, one of the most common JavaScript confusions.

### The Design Principle

`js:` is greppable. `grep -r "js:" src/` finds every interop escape hatch in a codebase. Code reviewers can audit JS-specific code without reading every line. The prefix announces: "I am crossing the boundary. I know what I'm doing."

The surface language doesn't trap you. It *defaults* to safety and makes the exits visible.
