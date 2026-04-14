## camelCase Conversion

Lykn source is written in lisp-case: `my-function-name`, `get-element-by-id`, `is-valid?`. JavaScript convention is camelCase: `myFunctionName`, `getElementById`, `isValid`. The compiler handles the translation automatically.

### The Simple Rule

Hyphens become camelCase boundaries. The character after a hyphen is uppercased, and the hyphen is removed:

```lisp
my-function         ;; → myFunction
get-element-by-id   ;; → getElementById
is-valid            ;; → isValid
set-value           ;; → setValue
```

### Edge Cases

A few patterns have special handling:

```lisp
-private            ;; → _private (leading hyphen → underscore)
JSON                ;; → JSON (no hyphens, no conversion)
console:log         ;; → console.log (both sides converted independently)
my-obj:some-method  ;; → myObj.someMethod
```

Names without hyphens pass through unchanged. This means JavaScript's own naming conventions — `JSON`, `NaN`, `parseInt` — work as-is.

### Why This Matters

You write in the style natural to Lisps. The output follows the style natural to JavaScript. A Lisp programmer reading the source sees idiomatic lisp-case. A JavaScript developer reading the output sees idiomatic camelCase. Neither has to compromise.

The full conversion table — with rules for consecutive hyphens, trailing hyphens, and private-field prefixes — lives in Appendix B. For the chapters ahead, the simple rule covers virtually every case: hyphens become camelCase boundaries, and both sides of a colon are converted independently.
