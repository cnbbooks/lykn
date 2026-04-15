## `export`

The `export` form wraps declarations — both surface and kernel forms.

### Exporting Surface Forms

```lisp
(export (func add
  :args (:number a :number b)
  :returns :number
  :body (+ a b)))
```

```javascript
export function add(a, b) {
  if (typeof a !== "number" || Number.isNaN(a))
    throw new TypeError(
      "add: arg 'a' expected number, got " + typeof a);

  if (typeof b !== "number" || Number.isNaN(b))
    throw new TypeError(
      "add: arg 'b' expected number, got " + typeof b);

  const result__gensym0 = a + b;
  if (typeof result__gensym0 !== "number" || Number.isNaN(result__gensym0))
    throw new TypeError(
      "add: return value expected number, got " + typeof result__gensym0);

  return result__gensym0;
}
```

```lisp
(export (bind VERSION "0.4.0"))
```

```javascript
export const VERSION = "0.4.0";
```

The surface form is expanded first (type checks, contracts, immutability), then the result is wrapped in `export`. You get the full safety of surface `func` and the visibility of `export`.

### Default Export

```lisp
(export default my-fn)
```

```javascript
export default myFn;
```

### What's Banned: Re-export-all

```lisp
;; NOT SUPPORTED in Lykn
;; (export (* from "utils"))
```

`export *` makes the module's public API invisible at the export site. Explicit lists are better — the reader of your module file can see exactly what's exported without following chains of re-exports.
