## Well-Known Symbols

JavaScript defines well-known symbols that serve as extension points for built-in behaviour. The reader has already encountered the most important ones.

### `Symbol:iterator` (Ch 21)

Makes an object iterable by `for-of`, spread, and destructuring. This is the symbol the reader knows best — it powers the entire iteration protocol.

### `Symbol:to-primitive` (Ch 5)

Controls how an object converts to a primitive value when used with `+`, template literals, or comparisons:

```lisp
(bind my-obj (obj :name "forty-two"))
(Object:define-property my-obj Symbol:to-primitive
  (obj :value (fn (:string hint)
    (if (= hint "number") 42
      (if (= hint "string") "forty-two"
        42)))))
```

The `hint` parameter tells the symbol whether the context wants a `"number"`, `"string"`, or `"default"` conversion.

### `Symbol:has-instance`

Controls `instanceof` behaviour. Allows a class or constructor to define a custom check for what constitutes an "instance."

### `Symbol:to-string-tag`

Controls the string returned by `Object:prototype:to-string`. Libraries use it to give custom classes meaningful `[object ...]` output.

### `Symbol:species`

Controls which constructor is used when built-in methods create derived objects (e.g., `Array.prototype.map` on a subclass). Rarely needed in application code.

### The Pattern

Well-known symbols are JavaScript's protocol mechanism — the language equivalent of "if you implement this method, the runtime will call it in this context." They're how JavaScript achieves extensibility without modifying built-in prototypes.

The [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol#well-known_symbols) have the full list. For working Lykn code, `Symbol:iterator` is the one that matters most.
