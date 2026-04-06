## The Seven Primitive Types

JavaScript has seven primitive types. Every value in JavaScript is either one of these seven primitives or an object. There is no third category, no matter how strenuously `typeof null` suggests otherwise.

### Number

```lisp
(bind age 42)
(bind pi 3.14159)
(bind price 19.99)
```

JavaScript has one numeric type: 64-bit IEEE 754 double-precision floating point. Both `42` and `42.0` are the same value, the same type, the same representation in memory. There are no separate integer and float types.

This has consequences. `0.1 + 0.2` evaluates to `0.30000000000000004`, not `0.3`. The safe integer range extends to plus-or-minus 2⁵³ - 1 (roughly 9 quadrillion). Beyond that, arithmetic silently loses precision.

And then there is NaN — Not a Number — which is, by `typeof`, a number. `typeof NaN === "number"` is `true`. NaN is the value you get when a numeric operation fails: `parseInt("hello")`, `Math.sqrt(-1)`, `0 / 0`. It propagates silently through arithmetic — one NaN in a chain of calculations infects every subsequent result, producing NaN all the way to the output. DLint's analysis of production websites found `$NaN` displayed as product prices on IKEA and eBay.

`typeof` says `"number"`. Lykn's `:number` says no: `typeof x === "number" && !Number.isNaN(x)`. A number is a number. NaN is something else.

### String

```lisp
(bind name "Duncan")
(bind empty "")
(bind greeting (template "Hello, " name "!"))
```

UTF-16 encoded sequences. Immutable — you cannot change a character in a string. You can only create new strings. Template literals (the `template` form) provide interpolation.

`typeof "hello"` is `"string"`. No surprises here.

### Boolean

```lisp
(bind active true)
(bind deleted false)
```

Two values. `true` and `false`. `typeof true` is `"boolean"`. The simplest of the types and the only one that has never caused a controversy.

### Undefined

The value JavaScript gives to things that don't have a value. Uninitialized variables. Missing function arguments. Missing object properties. Functions that don't explicitly return.

```javascript
let x;              // x is undefined
function f() {}     // f() returns undefined
const obj = {};
obj.name;           // undefined
```

`typeof undefined` is `"undefined"`. It is falsy. Accessing a property on it throws a `TypeError`.

In Lykn surface code, `undefined` is less prevalent because `bind` always requires an initializer — you can't write `(bind x)` without a value. But `undefined` still appears at the JavaScript boundary: calling a function that returns nothing, accessing a missing property.

### Null

The intentional absence of a value. Where `undefined` means "nothing was provided," `null` means "I explicitly chose nothing."

`typeof null` is `"object"`. This is a bug from JavaScript's first implementation in 1995. It has never been fixed because fixing it would break existing code. The language carries this scar permanently — a reminder that design decisions made in ten days can persist for thirty years.

`null` is falsy. It coerces to `0` in arithmetic (unlike `undefined`, which coerces to `NaN`). And in one of JavaScript's stranger design choices, `null == undefined` is `true` under loose equality, despite being different types with different `typeof` results. This particular quirk is, as we'll see, the one loose equality that Lykn's compiler deliberately uses.

### Symbol

```lisp
(bind id (Symbol "user-id"))
```

Unique identifiers, guaranteed never to collide with any other value. Used internally by JavaScript for iterator protocols (`Symbol.iterator`), type conversion (`Symbol.toPrimitive`), and other metaprogramming hooks. Rarely needed in application code. `typeof Symbol()` is `"symbol"`.

### BigInt

Arbitrary-precision integers for when the safe integer range isn't enough. `42n` in JavaScript syntax. Used for cryptography, database IDs, and the sort of calculations that involve numbers too large for IEEE 754 to represent faithfully. `typeof 42n` is `"bigint"`.

### The `typeof` Summary

| Value | `typeof` | Surprise? |
|---|---|---|
| `42` | `"number"` | |
| `NaN` | `"number"` | Yes |
| `"hello"` | `"string"` | |
| `true` | `"boolean"` | |
| `undefined` | `"undefined"` | |
| `null` | `"object"` | Yes |
| `Symbol()` | `"symbol"` | |
| `42n` | `"bigint"` | |

Two surprises in seven types. Not a bad ratio, but those two — NaN being a "number" and `null` being an "object" — are responsible for a disproportionate number of bugs.
