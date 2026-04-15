## `genfn`: Anonymous Generators

`genfn` is to `genfunc` what `fn` is to `func` — an anonymous generator with positional typed parameters.

```lisp
;; Zero-arg generator
(bind gen (genfn () (yield 1) (yield 2) (yield 3)))

(for-of n (gen)
  (console:log n))     ;; 1, 2, 3
```

```javascript
const gen = function*() {
  yield 1;
  yield 2;
  yield 3;
};
for (const n of gen()) {
  console.log(n);
}
```

### With Typed Parameters

```lisp
(bind range (genfn (:number start :number end)
  (for (let i start) (< i end) (+= i 1)
    (yield i))))

(for-of n (range 0 5)
  (console:log n))
```

```javascript
const range = function*(start, end) {
  if (typeof start !== "number" || Number.isNaN(start))
    throw new TypeError(
      "anonymous: arg 'start' expected number, got " + typeof start);
  if (typeof end !== "number" || Number.isNaN(end))
    throw new TypeError(
      "anonymous: arg 'end' expected number, got " + typeof end);
  for (let i = start; i < end; i += 1) {
    yield i;
  }
};
```

### With `:yields`

```lisp
(bind doubler (genfn (:number x) :yields :number
  (yield (* x 2))
  (yield (* x 3))))

(for-of n (doubler 5)
  (console:log n))     ;; 10, 15
```

Per-yield type checks work the same as in `genfunc` — the yielded value is validated before being produced.

### When to Use `genfn`

`genfn` is useful when passing a generator as a value — to a higher-order function, as an argument, or stored in a data structure. For most named generators, prefer `genfunc` — the name appears in stack traces and error messages.
