## Nil-Safe Threading: `some->` and `some->>`

Threading with nil short-circuiting. If any step produces `null` or `undefined`, the chain stops and returns the nil value.

```lisp
(some-> config
  (get :database)
  (get :host))
```

```javascript
(() => {
  const t__gensym0 = config;
  if (t__gensym0 == null) return t__gensym0;

  const t__gensym1 = t__gensym0["database"];
  if (t__gensym1 == null) return t__gensym1;

  return t__gensym1["host"];
})()
```

### How It Works

The compiler wraps `some->` in an IIFE with sequential bindings. After each step, a `== null` check short-circuits the chain if the value is null or undefined.

### The `== null` Exception

`some->` is one of the places where Lykn's compiled output contains `==` instead of `===`. The `== null` check catches both `null` and `undefined` in a single comparison — the only loose equality that ESLint's `eqeqeq` rule explicitly exempts. The developer never writes `==`; the compiler generates it.

### Not Option-Aware

`some->` checks for JavaScript null/undefined, not for `None`. For Option threading, use `match` or `if-let` with ADT patterns:

```lisp
;; JS interop: nullable values
(some-> user (get :address) (get :street))

;; Lykn-native: Option values
(if-let ((Some addr) (get-address user))
  addr:street
  "no address")
```

The two mechanisms serve different data: `some->` for JS interop (nullable APIs), `match`/`if-let` for surface-native data (Option/Result).
