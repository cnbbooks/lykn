## The Testing Philosophy

Lykn doesn't reinvent the test runner. Deno already has discovery, parallel execution, watch mode, filtering, coverage, and four reporters. What Deno doesn't have is a way to write tests in s-expression syntax with keyword clauses and assertion forms that feel like the rest of the language. That's the gap.

### What `lykn test` Does

Two phases. That's the whole thing.

1. Discover `*_test.lykn` and `*.test.lykn` files
2. Compile them to `.js`
3. Invoke `deno test` on the compiled output
4. Report Deno's exit code

The Rust compiler handles compilation. Deno handles execution, parallelism, reporters, coverage, sanitizers, and everything else a test runner should do. `lykn test` is the thin glue between them.

### What the Macros Do

The testing DSL lives in `packages/testing/` — a macro module, not a compiler feature. The macros `test`, `suite`, `step`, and the assertion forms expand to `Deno.test()` + `jsr:@std/assert` calls at compile time. The compiled output is standard Deno test code. A developer who reads the generated JavaScript would recognise it immediately.

```lisp
(import-macros "testing" (test is-equal))

(test "addition works"
  (is-equal (+ 1 2) 3))
```

```javascript
import { assertEquals } from "jsr:@std/assert";

Deno.test("addition works", () => {
  assertEquals(1 + 2, 3);
});
```

No runtime dependency. No custom test runner. No framework. Just macros that erase themselves and leave clean, portable JavaScript behind — which is, if you think about it, the politest thing a testing framework can do.
