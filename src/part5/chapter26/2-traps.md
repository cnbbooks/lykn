## The Traps

Every fundamental object operation has a corresponding trap.

### Reference Table

| Trap | Intercepts | Reflect Equivalent |
|---|---|---|
| `get` | Property read | `Reflect:get` |
| `set` | Property write | `Reflect:set` |
| `has` | `in` operator | `Reflect:has` |
| `delete-property` | `delete` operator | `Reflect:delete-property` |
| `apply` | Function call | `Reflect:apply` |
| `construct` | `new` operator | `Reflect:construct` |
| `own-keys` | `Object:keys` etc. | `Reflect:own-keys` |
| `get-own-property-descriptor` | Descriptor lookup | `Reflect:get-own-property-descriptor` |
| `define-property` | `Object:define-property` | `Reflect:define-property` |
| `get-prototype-of` | `Object:get-prototype-of` | `Reflect:get-prototype-of` |
| `set-prototype-of` | `Object:set-prototype-of` | `Reflect:set-prototype-of` |
| `is-extensible` | `Object:is-extensible` | `Reflect:is-extensible` |
| `prevent-extensions` | `Object:prevent-extensions` | `Reflect:prevent-extensions` |

### `get` — The Most Common Trap

Default values for missing properties:

```lisp
(bind handler (obj
  :get (fn (:any target :string prop :any receiver)
    (if (in prop target)
      (Reflect:get target prop receiver)
      (template "No property '" prop "'")))))
```

### `set` — Validation on Write

```lisp
(bind handler (obj
  :set (fn (:any target :string prop :any value :any receiver)
    (if (and (= prop "age") (or (not (= (typeof value) "number")) (< value 0)))
      (throw (new TypeError "age must be a non-negative number")))
    (Reflect:set target prop value receiver))))
```

### `apply` — Intercept Function Calls

```lisp
(func with-logging
  :args (:function f)
  :returns :any
  :body
  (new Proxy f (obj
    :apply (fn (:any target :any this-arg :any args)
      (console:log (template "Calling with " args))
      (Reflect:apply target this-arg args)))))
```

### The Pattern

Every trap follows the same shape: do your custom logic, then call the corresponding `Reflect` method to perform the default operation. `Reflect` is the Proxy API's companion — it provides exactly the default behaviour that each trap would perform if not intercepted.
