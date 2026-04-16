## The Pipeline

The JS kernel compiler has three stages:

```text
.lykn source  →  Reader  →  S-expression tree
                               ↓
                            Compiler  →  ESTree AST
                               ↓
                            astring   →  JavaScript text
```

### Stage 1: Reading

Text becomes a tree of atoms, strings, lists, and numbers. No semantic knowledge. The reader doesn't know what `bind` means — it's just an atom. (The reader was covered in Ch 3; this section is about how it fits in the pipeline.)

### Stage 2: Compilation

The tree becomes an ESTree AST. The compiler walks the tree and dispatches on the head atom of each list: `const` → `VariableDeclaration`, `if` → `IfStatement`, `function` → `FunctionDeclaration`. One handler per kernel form.

### Stage 3: Code Generation

The ESTree AST becomes JavaScript text. astring — a vendored library — pretty-prints the AST as clean, readable JavaScript with correct operator precedence and minimal parentheses.

### What's NOT in the Pipeline

No optimizer. No type system (that's the surface compiler — Ch 31). No intermediate representation beyond ESTree. No runtime library. The pipeline is deliberately minimal: read, compile, print.

Note: the Rust compiler (the primary `lykn compile` tool) has a richer pipeline — reader → expander → classifier → analyzer → emitter → codegen (Ch 2). This chapter describes the *JS kernel compiler*, which powers the browser bundle and serves as the reference implementation.
