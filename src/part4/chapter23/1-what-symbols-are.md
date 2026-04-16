## What Symbols Are

A symbol is a unique, immutable primitive value. Every call to `Symbol()` creates a new, distinct symbol — even with the same description.

```lisp
(bind s1 (Symbol "description"))
(bind s2 (Symbol "description"))
(console:log (= s1 s2))    ;; → false — every symbol is unique
```

```javascript
const s1 = Symbol("description");
const s2 = Symbol("description");
console.log(s1 === s2);    // false
```

The description is for debugging only — it appears in `console.log` and error messages but doesn't affect identity. Two symbols with the same description are still different symbols.

### Symbols as Property Keys

Symbols can be used as object property keys via `get`:

```lisp
(bind id (Symbol "id"))
(bind user (obj :name "Duncan"))
(Object:define-property user id (obj :value 42 :writable true))

(console:log (get user id))        ;; → 42
(console:log (Object:keys user))   ;; → ["name"] — symbol key hidden
```

Symbol-keyed properties don't show up in `Object:keys`, `for-in`, or `JSON:stringify`. They're hidden from casual inspection but accessible if you have the symbol reference.

### Collision-Free Extension

The use case that justifies symbols: when you need to attach data to an object you don't control, a symbol key guarantees no collision with existing or future string keys. Framework authors use this pattern to extend DOM elements, class instances, and library objects without risking name clashes.
