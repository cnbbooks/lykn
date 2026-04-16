## Edge Cases

### Destructuring `null` or `undefined`

Destructuring a non-destructurable value throws a runtime `TypeError` — same as JavaScript:

```lisp
(bind (object name) null)    ;; TypeError at runtime
```

### `rest` Must Be Last

```lisp
;; COMPILE ERROR
(bind (array (rest first) last) items)
```

`rest` collects *remaining* elements. It can only appear at the end of a pattern.

### `_` in Object vs Array Patterns

In array patterns, `_` is a skip marker — it skips a position. In object patterns, `_` is a regular binding name — it extracts a property called `_`. The distinction matters: `(array _ second)` skips the first element, but `(object _)` extracts a property named `_`.

### Empty Patterns

`(bind (object) x)` compiles to `const {} = x` — valid JavaScript, but useless. The compiler allows it without error.

### Destructured `func` Parameters

In surface `func` and `fn`, destructured params require type annotations on every field. A bare name is a compile error:

```lisp
;; COMPILE ERROR: field 'name' missing type annotation (use :any to opt out)
(func f :args ((object name)) :body ...)
```

In multi-clause functions, two clauses that both destructure objects at the same position overlap — because dispatch can only check `typeof`, not the shape of the object's properties.

### Nested Destructuring Rules

Nested patterns in object destructuring must use `alias` to specify the property name:

```lisp
;; COMPILE ERROR: must use alias
(func f :args ((object (object :string name))) :body ...)

;; OK: alias provides the property key
(func f :args ((object (alias :any c (object :string name)))) :body ...)
```

In array destructuring, nesting is positional — no `alias` needed.

### Defaults and `--strip-assertions`

Default values survive `--strip-assertions` — they're runtime semantics, not assertions. Only type checks are stripped:

```javascript
// --strip-assertions: defaults preserved, type checks removed
function createUser({name, age = 0, role = "viewer"}) {
  return {name, age, role};
}
```

### `rest` with `default`

`rest` collects all remaining elements. A default on `rest` is nonsensical and produces a compile error.
