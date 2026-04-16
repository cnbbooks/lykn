## What Is a Proxy?

A Proxy wraps a target object with a handler that can intercept fundamental operations — property access, assignment, deletion, function calls, construction.

```lisp
(bind target (obj :name "Arthur" :title "King"))
(bind handler (obj
  :get (fn (:any target :string prop :any receiver)
    (console:log (template "Accessing " prop))
    (Reflect:get target prop receiver))))

(bind proxy (new Proxy target handler))
proxy:name    ;; logs "Accessing name", returns "Arthur"
proxy:title   ;; logs "Accessing title", returns "King"
```

```javascript
const target = {name: "Arthur", title: "King"};
const handler = {
  get(target, prop, receiver) {
    console.log(`Accessing ${prop}`);
    return Reflect.get(target, prop, receiver);
  }
};
const proxy = new Proxy(target, handler);
```

### The Components

**Target** — the real object being wrapped. The proxy forwards operations to it.

**Handler** — an object with *trap* methods. Each trap intercepts a specific operation.

**Trap** — a method on the handler that fires when the corresponding operation occurs on the proxy.

**`Reflect`** — provides the default behaviour for each trap. Call `Reflect:get`, `Reflect:set`, etc. to "do what would normally happen" after your custom logic.

### Transparency

The proxy is transparent to the caller — `typeof proxy` returns `"object"`, `proxy:name` works, `Object:keys proxy` works. The caller can't tell they're talking to a proxy unless the handler makes it obvious. The illusion is the feature.
