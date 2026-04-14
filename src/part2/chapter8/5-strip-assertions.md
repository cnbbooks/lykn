## The Dev/Prod Split

Type checks and contracts are safety tools. They catch bugs during development. They cost cycles in production. Lykn lets you have both.

### The Flag

```sh
# Development — all assertions emitted
lykn compile src/app.lykn

# Production — assertions stripped
lykn compile --strip-assertions src/app.lykn
```

### What Gets Stripped

| Feature | Dev mode | `--strip-assertions` |
|---|---|---|
| `:args` type checks | Emitted | **Removed** |
| `:returns` type check | Emitted | **Removed** |
| `bind` type checks (DD-24) | Emitted | **Removed** |
| `:pre` contracts | Emitted | **Removed** |
| `:post` contracts | Emitted | **Removed** |
| `type` constructor validation | Emitted | **Removed** |
| Multi-clause dispatch checks | Emitted | **Kept** |

The last row is critical: **multi-clause dispatch checks are not assertions.** They're runtime semantics — they determine which clause runs. Stripping them would change the function's behaviour, not just its safety. The compiler keeps them.

### The Tradition

This follows a well-established pattern. Eiffel introduced assertion monitoring levels in 1986 — you could enable preconditions, postconditions, or both, independently, per class. Clojure's `*compile-asserts*` flag toggles spec-based validation. Common Lisp's `(declare (optimize (safety 0)))` tells the compiler to skip type checks.

The principle is consistent across all of them: contracts are a development tool, not a production tax. You write them once, they protect you during development, and they vanish when performance matters.
