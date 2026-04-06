## Type Coercion: JavaScript's Party Trick

JavaScript's type coercion system operates on a principle not entirely unlike the philosophy of a very polite but fundamentally confused butler: when asked to combine incompatible types, it doesn't refuse or ask for clarification. It simply does its best. Its best is frequently astonishing.

### The `+` Problem

The `+` operator is overloaded. It performs addition on numbers and concatenation on strings. When it receives one of each, it must choose. It chooses string concatenation:

```javascript
"5" + 3         // → "53"    (string wins)
"5" - 3         // → 2       (- is not overloaded — numeric only)
"5" * 3         // → 15      (same — numeric only)
```

This asymmetry is the single most common source of type confusion in JavaScript. The expression `count + 1` might produce `2` or `"11"` depending on whether `count` is a number or a string, and nothing in the syntax tells you which it is.

Lykn addresses this by separating the operations: `(+ a b)` for arithmetic, `(template ...)` or string `+` for concatenation. The surface compiler's type checks at function boundaries catch string-where-number-expected errors before they reach the `+` operator.

### The Coercion Table of Horrors

JavaScript coerces values implicitly in dozens of contexts. A small selection of the more educational results:

```javascript
[] + []          // → ""                  (arrays → strings → concatenation)
[] + {}          // → "[object Object]"   (array → "", object → string)
{} + []          // → 0                   (or "[object Object]" — depends on context)
true + true      // → 2                   (booleans → numbers)
"" == false      // → true                (both coerce to 0)
"0" == false     // → true                (both coerce to 0)
"" == "0"        // → false               (same type, compared directly)
null == 0        // → false               (null only equals null or undefined)
null == undefined // → true               (special case)
```

The third row — `{} + []` — deserves special mention. Whether this produces `0` or `"[object Object]"` depends on whether JavaScript's parser interprets `{}` as an empty object literal or an empty block statement. The parser makes this decision based on syntactic context. The same six characters produce different values depending on where they appear. This is not a corner case; this is the language working as designed.

### What Lykn Does About It

Lykn's surface language doesn't change JavaScript's coercion rules — the compiled output is still JavaScript, and JavaScript still coerces. But the surface language provides two layers of defence:

**At the boundary**: Type keywords (`:number`, `:string`, etc.) catch wrong types at function entry. If `count` enters your function as a string when you expected a number, the type check fires before any arithmetic occurs.

**At the equality operator**: `(= a b)` compiles to `===`, which never coerces. The entire loose-equality coercion table — where `"" == false` and `"0" == false` but `"" != "0"` — is simply unreachable from surface Lykn code.

The coercion that happens *inside* a function body — `(+ x "hello")` where `x` is a number — is still JavaScript's coercion. A full type system would catch this; Lykn's boundary checks don't. But the empirical evidence suggests that boundary checks catch the majority of type-related bugs in practice, because most coercion errors enter through function parameters, not through expressions where the programmer knows the types of both operands.
