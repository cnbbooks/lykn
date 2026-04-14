## Unary Operators

A handful of unary operators round out the catalog:

| Lykn | JS | Purpose |
|---|---|---|
| `(not x)` | `!x` | Logical negation (surface form) |
| `(typeof x)` | `typeof x` | Type string |
| `(void 0)` | `void 0` | Evaluate and return `undefined` |
| `(delete obj:prop)` | `delete obj.prop` | Remove a property |

`typeof` is a kernel operator — in surface code, you use type keywords on function boundaries rather than checking types manually. But `typeof` is occasionally useful for JS interop or debugging.

`delete` removes a property from an object. In surface code, prefer `dissoc` for immutable removal. `delete` mutates the original object.

## Bitwise Operators

For completeness, and for the rare occasion when you need to manipulate bits:

| Lykn | JS | Operation |
|---|---|---|
| `(& a b)` | `a & b` | Bitwise AND |
| `(\| a b)` | `a \| b` | Bitwise OR |
| `(^ a b)` | `a ^ b` | Bitwise XOR |
| `(~ x)` | `~x` | Bitwise NOT |
| `(<< a n)` | `a << n` | Left shift |
| `(>> a n)` | `a >> n` | Sign-propagating right shift |
| `(>>> a n)` | `a >>> n` | Zero-fill right shift |

Bitwise operators convert their operands to 32-bit integers, perform the operation, and convert back. Most application code never uses them. They appear in cryptographic code, binary protocol handling, and the occasional performance trick like `(| 0 x)` for fast float-to-integer truncation.

If you need them, they're here. If you don't, this section has earned its keep by existing for the day you do.
