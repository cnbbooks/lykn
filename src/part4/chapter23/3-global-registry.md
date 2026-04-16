## `Symbol:for` and the Global Registry

`Symbol()` creates a unique symbol every time. `Symbol:for` returns the *same* symbol for the same key, from a global registry.

```lisp
(bind s1 (Symbol:for "app.id"))
(bind s2 (Symbol:for "app.id"))
(console:log (= s1 s2))           ;; → true — same key, same symbol

(console:log (Symbol:key-for s1))  ;; → "app.id"
```

```javascript
const s1 = Symbol.for("app.id");
const s2 = Symbol.for("app.id");
console.log(s1 === s2);           // true
console.log(Symbol.keyFor(s1));   // "app.id"
```

### When to Use It

The global registry enables sharing symbols across modules or realms (iframes, Web Workers) without passing the symbol reference directly. The string key acts as a coordination mechanism.

**Convention**: use namespaced keys (`"app.metadata"`, `"mylib.version"`) to avoid collisions in the global registry — ironic, since symbols exist to avoid collisions. The irony is intentional: the registry keys are strings (which can collide), but the symbols they produce are unique within the registry.
