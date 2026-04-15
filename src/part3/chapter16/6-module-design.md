## Module Design

Brief guidance on structuring Lykn modules.

### One Module, One Concern

A module should do one thing well. A `math-utils.lykn` that also handles string formatting is two modules wearing one filename.

### Export Types and Functions, Not State

If a module exports a `cell`, you've created shared mutable state across module boundaries — exactly what Chapter 13 warned against. Export functions that *manage* state internally; don't export the state itself.

```lisp
;; Good: state is internal, interface is functional
(bind db (cell #a()))

(export (func add-record
  :args (:object record)
  :body (swap! db (fn (:array items) (conj items record)))))

(export (func get-records
  :returns :array
  :body (express db)))
```

### Prefer Named Exports

Named exports enable tree-shaking and make imports self-documenting. Default exports are for modules that genuinely have one primary thing — a component, a main function, a configuration object.

### Keep Import Lists Explicit

Even though it's more typing, `(import "./utils.js" (add subtract multiply))` tells you exactly what a module depends on. Lykn enforces this by banning namespace imports. The explicitness isn't a cost — it's the documentation.
