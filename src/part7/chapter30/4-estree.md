## ESTree as Intermediate Representation

ESTree is the standard AST format for JavaScript. Originally defined by SpiderMonkey, it's now used by ESLint, Babel, Prettier, acorn, and dozens of other tools.

### Why ESTree?

Lykn doesn't invent its own IR. It uses ESTree directly:

- **Verified against the spec** — every node Lykn produces is a valid ESTree node
- **Tooling compatible** — ESLint can lint the AST, Prettier can format it
- **Well-documented** — the [ESTree spec](https://github.com/estree/estree) is the documentation
- **No custom node types** — nothing Lykn-specific in the AST

### The Node Inventory

The kernel uses approximately 53 ESTree node types. The most common:

`Identifier`, `Literal`, `BinaryExpression`, `CallExpression`, `MemberExpression`, `VariableDeclaration`, `FunctionDeclaration`, `ArrowFunctionExpression`, `IfStatement`, `ReturnStatement`, `BlockStatement`, `ObjectExpression`, `ArrayExpression`, `TemplateLiteral`, `ClassDeclaration`, `ImportDeclaration`, `ExportDeclaration`.

Each kernel form maps to one or a few of these. The mapping is mechanical — the compiler is a translator, not a transformer.
