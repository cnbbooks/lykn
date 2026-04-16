## Metaprogramming Patterns

### Reactive State

The pattern behind Vue, MobX, and similar frameworks:

```lisp
(func reactive
  :args (:object initial :function on-change)
  :returns :any
  :body
  (new Proxy initial (obj
    :set (fn (:any target :string prop :any value :any receiver)
      (bind old (Reflect:get target prop receiver))
      (Reflect:set target prop value receiver)
      (if (not (= old value)) (on-change prop value old))
      true))))

(bind state (reactive (obj :count 0)
  (fn (:string prop :any val :any old)
    (console:log (template prop ": " old " → " val)))))
```

Every property assignment triggers the callback. The UI framework uses this to re-render when state changes.

### Immutable Wrapper

```lisp
(func immutable
  :args (:object target)
  :returns :any
  :body
  (new Proxy target (obj
    :set (fn () (throw (new TypeError "Object is immutable")))
    :delete-property (fn () (throw (new TypeError "Object is immutable"))))))
```

### Logging Wrapper

The simplest useful proxy — forward everything, log access:

```lisp
(bind logged (new Proxy target (obj
  :get (fn (:any t :string p :any r)
    (console:log (template "get " p))
    (Reflect:get t p r)))))
```

### Membrane Pattern

Wraps an entire object graph — any object returned from the proxy is also wrapped. Used for sandboxing and security boundaries. This is a library-level pattern; the concept cards have the implementation details.
