## The Compiler

The compiler walks the reader's tree and produces ESTree nodes. It's a pattern-matching dispatch table in `packages/lykn/compiler.js`.

### The Dispatch

The compiler's core is a `switch` on the head atom of each list:

```javascript
// Simplified — the actual code handles more cases
function compile(node) {
  if (isAtom(node)) return compileAtom(node);
  if (isString(node)) return { type: "Literal", value: node.value };
  if (isNumber(node)) return { type: "Literal", value: node.value };
  if (isList(node)) {
    const head = node.values[0].value;
    const handler = forms[head];
    if (handler) return handler(node.values.slice(1));
    return compileCall(node);  // default: function call
  }
}
```

Each kernel form has a handler function. The handler receives the arguments (everything after the head atom) and returns an ESTree node.

### `const` → `VariableDeclaration`

```lisp
(const x 42)
```

The handler produces:

```javascript
{
  type: "VariableDeclaration",
  kind: "const",
  declarations: [{
    type: "VariableDeclarator",
    id: { type: "Identifier", name: "x" },
    init: { type: "Literal", value: 42 }
  }]
}
```

astring prints: `const x = 42;`

### `function` → `FunctionDeclaration`

```lisp
(function add (a b) (return (+ a b)))
```

Produces a `FunctionDeclaration` with `Identifier` params, a `BlockStatement` body containing a `ReturnStatement` with a `BinaryExpression`. The tree maps directly to ESTree — no transformation, no optimization, just structural translation.

### Colon Splitting

When the compiler encounters an atom containing colons — `console:log` — it splits on `:` and produces a `MemberExpression` chain. Each segment gets camelCase conversion. `document:get-element-by-id` → `document.getElementById`.

### Expression vs Statement

The compiler tracks context: is this form in expression position or statement position? A standalone `(if ...)` produces an `IfStatement`. An `(if ...)` inside a `const` initializer would be different. The surface compiler handles complex cases (IIFE wrapping for `match`), but the kernel compiler handles the basic context detection.
