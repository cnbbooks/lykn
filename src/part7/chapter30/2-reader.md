## The Reader

The reader turns text into a tree. It's 320 lines of JavaScript in `packages/lykn/reader.js`.

### Five Node Types

| Type | Examples | Representation |
|---|---|---|
| Atom | `bind`, `console:log`, `+` | `{ type: "atom", value: "bind" }` |
| String | `"hello"`, `"world"` | `{ type: "string", value: "hello" }` |
| Number | `42`, `3.14` | `{ type: "number", value: 42 }` |
| List | `(bind x 42)` | `{ type: "list", values: [...] }` |
| Keyword | `:name`, `:string` | `{ type: "keyword", value: "name" }` |

### A Concrete Example

```lisp
(bind greeting (template "Hello, " name "!"))
```

Reader output:

```text
List [
  Atom "bind",
  Atom "greeting",
  List [
    Atom "template",
    String "Hello, ",
    Atom "name",
    String "!"
  ]
]
```

The reader sees structure — which things are grouped with which other things. All meaning is assigned by the compiler.

### What the Reader Also Handles

- **Reader dispatch**: `#a(...)` → `(array ...)`, `#o(...)` → `(object ...)`
- **Quasiquote**: `` ` ``, `,`, `,@` for macro templates
- **Comments**: `;` line, `#| ... |#` block, `#;` expression
- **Colon syntax**: `console:log` stays as one atom (the compiler splits it)

### What the Reader Doesn't Do

Semantic analysis, type checking, macro expansion. The reader is pure syntax — trees, not meaning.
