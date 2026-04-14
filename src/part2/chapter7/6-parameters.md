## Parameters in Depth

### Surface Parameters: Typed Pairs Only

`func`'s `:args` list accepts strictly alternating type-name pairs: `:type name :type name`. This is by design — the surface language keeps parameter syntax simple and uniform.

```lisp
(func greet
  :args (:string name :number age)
  :returns :string
  :body (template name " is " age " years old"))
```

### Default Values and Rest Parameters

Default values and rest parameters are available through kernel function forms, not through `func`'s `:args` syntax:

```lisp
;; Kernel: default parameter
(function greet (name (default greeting "Hello"))
  (return (template greeting ", " name "!")))
```

```javascript
function greet(name, greeting = "Hello") {
  return `${greeting}, ${name}!`;
}
```

```lisp
;; Kernel: rest parameter
(function log-all (level (rest messages))
  (console:log level messages))
```

```javascript
function logAll(level, ...messages) {
  console.log(level, messages);
}
```

These are kernel forms — they compile to their JavaScript equivalents directly, without type checking. If you need default values or rest parameters with type checking, use multi-clause `func` dispatch (Ch 8) as the surface alternative:

```lisp
;; Surface alternative to default parameters
(func greet
  (:args (:string name)
   :returns :string
   :body (template "Hello, " name "!"))

  (:args (:string greeting :string name)
   :returns :string
   :body (template greeting ", " name "!")))
```

The two-clause version provides the same behavior as a default parameter — call with one argument for the default greeting, two for a custom one — with full type checking on both clauses.

### Destructuring

Parameters can be destructured — unpacking objects and arrays inline. This is covered in Chapter 15 (Destructuring). For now, know that it works and that it follows the same patterns as `bind` destructuring.
