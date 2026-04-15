## `dynamic-import`

For lazy loading and conditional imports:

```lisp
(bind module (await (dynamic-import "./heavy-module.js")))
(bind result (module:process data))
```

```javascript
const module = await import("./heavy-module.js");
const result = module.process(data);
```

`dynamic-import` is an expression — it returns a Promise that resolves to the module namespace object. Use it for:

- **Code splitting** — load modules only when needed
- **Conditional loading** — different modules for different environments
- **Computed paths** — `(dynamic-import (template "./lang/" locale ".js"))`

Note: `dynamic-import` uses JavaScript's `import()` expression, not the `import` declaration. They share the keyword but are different mechanisms — `import` declarations are static (analyzed at compile time, hoisted), while `import()` expressions are dynamic (evaluated at runtime, return promises).
