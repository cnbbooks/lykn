## The Surface: Where Safety Lives

The surface is the Department of Functional Safety. Its job is to make it difficult to write dangerous code and easy to write correct code. It accomplishes this by having opinions — strong, specific opinions — about how programs should be structured.

### The Functional Commitment

All bindings are immutable. There is no `let` in the surface language, no mutable variable form, no way to rebind a name once it's been bound. `bind` compiles to `const` and there is no alternative.

If you need mutation — and sometimes you do — the surface provides `cell`: a controlled, explicit container.

```lisp
(bind counter (cell 0))
(swap! counter (=> (n) (+ n 1)))
(console:log (express counter))  ;; → 1
```

```javascript
const counter = {value: 0};
counter.value = ((n) => n + 1)(counter.value);
console.log(counter.value);
```

The `!` in `swap!` is not decoration. It is a convention enforced across the surface language: every mutating operation wears a `!` suffix, so you can see state changes at a glance. If a function name doesn't end in `!`, it's pure.

### Type Annotations

Surface functions require type annotations on all parameters:

```lisp
(func greet
  :args (:string name)
  :returns :string
  :body (+ "Hello, " name "!"))
```

```javascript
function greet(name) {
  if (typeof name !== "string")
    throw new TypeError(
      "greet: arg 'name' expected string, got " + typeof name);
  const result__gensym0 = "Hello, " + name + "!";
  if (typeof result__gensym0 !== "string")
    throw new TypeError(
      "greet: return value expected string, got "
      + typeof result__gensym0);
  return result__gensym0;
}
```

The annotations compile to runtime `typeof` checks in development. Pass `--strip-assertions` and they vanish for production. The surface compiler *requires* these annotations — a bare `(func greet :args (name) ...)` without a type keyword is a compile error. `:any` is the explicit opt-out, because even opting out should be a conscious decision.

### Algebraic Data Types and Pattern Matching

This is what the kernel *cannot* do. The surface provides `type` for defining algebraic data types and `match` for exhaustive pattern matching:

```lisp
(type Shape
  (Circle :number radius)
  (Rect :number width :number height)
  (Point))

(func describe
  :args (:any shape)
  :returns :string
  :body (match shape
    ((Circle r) (+ "circle with radius " r))
    ((Rect w h) (+ w "×" h " rectangle"))
    ((Point) "a point")))
```

The `type` form defines three constructors: `Circle` (one field), `Rect` (two fields), and `Point` (no fields). Each compiles to a function that returns a tagged object — `{ tag: "Circle", radius: 5 }`. The `match` form compiles to an if-chain that tests the `tag` field and extracts the relevant values.

The critical word is *exhaustive*. If you add a `(Triangle ...)` variant to `Shape` and forget to update the `match`, the compiler refuses to compile. This is a compile error, not a runtime surprise. The kernel has no concept of this — it would happily emit a switch statement with a missing case. The surface catches it before the kernel ever sees the code.

### The Surface Form Vocabulary

Eight forms constitute the core of the surface language:

| Form | Purpose | Kernel expansion |
|---|---|---|
| `bind` | Immutable binding | `const` |
| `func` | Named function with contracts | `function` + type checks |
| `fn` / `lambda` | Anonymous function | `=>` or `lambda` + type checks |
| `type` | Algebraic data type | Constructor functions |
| `match` | Exhaustive pattern matching | `if` chain |
| `obj` | Object with keywords | `object` with grouped pairs |
| `cell` | Mutable container | `{ value: x }` |
| `macro` | User-defined syntax | Expansion-time transform |

Eight forms and a macro system. That's the surface language. Everything else — `assoc`, `dissoc`, `conj`, threading macros, `if-let`, `when-let` — is built from these primitives or provided as standard macros. The same Lisp insight, applied one more time: a small set of primitives, composed through macros, can express everything.
