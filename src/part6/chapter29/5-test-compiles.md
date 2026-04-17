## Compiler Output Verification: `test-compiles`

Most testing DSLs provide forms for checking values, catching errors, and matching patterns. Lykn's testing module provides all of those — and one form that exists because Lykn is, at its core, a *compiler* project.

### The Pattern

`test-compiles` takes a name, a Lykn input string, and an expected JavaScript output string. It calls `compile()` on the input and asserts the output matches.

```lisp
(import "../../packages/lykn/mod.js" (compile))
(import-macros "testing" (test-compiles))

(test-compiles "bind simple"
  "(bind x 1)" "const x = 1;")

(test-compiles "func with body"
  "(func add :args (a b) :body (+ a b))"
  "function add(a, b) {\n  return a + b;\n}")
```

```javascript
import { compile } from "../../packages/lykn/mod.js";

Deno.test("bind simple", () => {
  const r_1 = compile("(bind x 1)");
  assertEquals(r_1.trim(), "const x = 1;");
});

Deno.test("func with body", () => {
  const r_2 = compile("(func add :args (a b) :body (+ a b))");
  assertEquals(r_2.trim(), "function add(a, b) {\n  return a + b;\n}");
});
```

One line replaces a five-line `Deno.test` + `compile` + `assertEquals` pattern. The `compile` import is not part of the macro — the test file imports it explicitly, keeping the testing module decoupled from the compiler.

### Why This Exists

Lykn's test suite has over 1,300 tests. The majority follow exactly this pattern: compile a Lykn string, check the JavaScript output. Fourteen surface test files and thirty kernel form test files, each with dozens of input-output pairs.

`test-compiles` captures that pattern in a single macro. The ergonomic gain is not just fewer characters — it's a test file that reads as a specification. Each line declares what the compiler should produce for a given input, without the ceremony of naming variables, calling functions, and comparing results.

Lykn's own tests are written in Lykn. The testing infrastructure was built partly to make this possible — dogfooding the language by testing the language in the language. The compiler tests the compiler tests the compiler, which is either a virtuous cycle or an ouroboros, depending on how you look at it.
