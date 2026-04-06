## The Pipeline

Enough abstraction. Let's trace a real value through the compiler and watch the transformation happen.

### The Source

Here is a small surface program:

```lisp
(bind x 42)
(console:log x)
```

Two lines. One binding, one function call. Let's follow them through all six stages of the Rust compiler.

### Stage 1: Reader

The reader parses the text into s-expressions — a tree of lists, atoms, strings, and numbers:

```text
List[ Atom("bind"), Atom("x"), Number(42) ]
List[ Atom("console:log"), Atom("x") ]
```

The reader doesn't know what `bind` means. It just sees structure.

### Stage 2: Expander

The expander looks for macros to expand. `bind` and `console:log` are not user-defined macros — they're handled by later stages. For this simple program, the expander passes the tree through unchanged.

### Stage 3: Classifier

The classifier walks the tree and identifies each form. It sees `bind` and classifies it as a surface binding form. It sees `console:log` and classifies it as a kernel passthrough (a function call that the surface compiler doesn't need to transform). The output is a typed surface AST — a structured representation that the analyzer can reason about.

### Stage 4: Analyzer

The analyzer checks the classified AST for errors. For `(bind x 42)`, it registers `x` in the scope and notes that it's immutable. If `x` were never used, the analyzer would flag it. If `x` were referenced before this point, the analyzer would catch that too. For this program, everything checks out.

### Stage 5: Emitter

The emitter transforms surface forms into kernel s-expressions. `bind` becomes `const`:

```text
List[ Atom("const"), Atom("x"), Number(42) ]
List[ Atom("console:log"), Atom("x") ]
```

The `console:log` call was already a kernel-compatible form, so it passes through unchanged. More complex surface forms — `func` with type annotations, `match` with exhaustiveness checking — would produce substantially different kernel output than their surface input. But `bind` → `const` is a clean one-to-one mapping.

### Stage 6: Codegen

The codegen walks the kernel s-expressions and produces JavaScript text. `const` becomes a variable declaration. The colon in `console:log` becomes a dot. The atom `x` stays as `x` (no camelCase conversion needed — it's already lowercase with no hyphens).

```javascript
const x = 42;
console.log(x);
```

### The Full Picture

```text
(bind x 42)              → reader    → List[bind, x, 42]
                          → expander  → (unchanged)
                          → classifier → SurfaceBind { name: x, value: 42 }
                          → analyzer  → (scope registered, no errors)
                          → emitter   → List[const, x, 42]
                          → codegen   → const x = 42;
```

Six stages, each doing one thing. The reader builds structure. The expander resolves macros. The classifier identifies forms. The analyzer checks safety. The emitter rewrites surface to kernel. The codegen writes JavaScript. No stage needs to understand any other stage's domain.

### A More Interesting Example

For `(bind x 42)`, the pipeline is almost trivial. Here's what happens with something richer — a typed function:

```lisp
(func double
  :args (:number n)
  :returns :number
  :body (* n 2))
```

The reader sees a list with atoms, keywords, and a nested list. The classifier identifies it as a `func` form and parses the keyword-labeled clauses. The analyzer registers the function signature and checks that the type keywords are valid. The emitter produces:

```lisp
;; Kernel output (what the emitter produces):
(function double (n)
  (if (!== (typeof n) "number")
    (throw (new TypeError "double: arg 'n' expected number, got ...")))
  (const result__gensym0 (* n 2))
  (if (!== (typeof result__gensym0) "number")
    (throw (new TypeError "double: return value expected number, got ...")))
  (return result__gensym0))
```

And the codegen produces:

```javascript
function double(n) {
  if (typeof n !== "number")
    throw new TypeError(
      "double: arg 'n' expected number, got " + typeof n);
  const result__gensym0 = n * 2;
  if (typeof result__gensym0 !== "number")
    throw new TypeError(
      "double: return value expected number, got "
      + typeof result__gensym0);
  return result__gensym0;
}
```

The surface wrote four lines. The kernel received twelve. The JavaScript output is fourteen. The safety was added by the emitter; the JavaScript was produced by the codegen. Neither knew what the other was doing, and the output is clean, readable, and correct.
