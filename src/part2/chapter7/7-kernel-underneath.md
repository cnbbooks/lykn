## The Kernel Underneath

The surface has two function forms. The kernel has three, because JavaScript does:

| Surface | Kernel | JS output |
|---|---|---|
| `func` | `function` | `function name(...) { ... }` |
| `fn` | `=>` | `(...) => ...` |
| `lambda` | `=>` | `(...) => ...` (same as `fn`) |

### The Three Kernel Forms

```lisp
;; Kernel: function declaration (explicit return required)
(function add (a b) (return (+ a b)))

;; Kernel: arrow function
(=> (x) (* x 2))

;; Kernel: function expression (anonymous, non-arrow)
(lambda (x) (return (* x 2)))
```

```javascript
function add(a, b) { return a + b; }
(x) => x * 2;
function(x) { return x * 2; }
```

The kernel's `function` requires explicit `return` statements — just like JavaScript. The surface's `func` handles return insertion automatically based on `:returns`.

### Why You'd Use Kernel Forms

Rarely, in practice. `func` and `fn` provide type checking, and that's usually what you want. But kernel forms are available for:

- **JS interop** where you need a specific function shape
- **Inside `class` bodies** where methods use kernel syntax
- **Performance-critical code** where you want to skip type checks without `--strip-assertions`

The kernel forms are documented in the README's form tables. The surface forms are what this book teaches.
