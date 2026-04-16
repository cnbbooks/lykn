## The Kernel Form Vocabulary

Every kernel form, its ESTree node, and its JavaScript output. This is the table the reader has been implicitly relying on since Chapter 2.

### Declarations

| Kernel | ESTree | JS |
|---|---|---|
| `const` | `VariableDeclaration` (const) | `const x = ...;` |
| `let` | `VariableDeclaration` (let) | `let x = ...;` |
| `function` | `FunctionDeclaration` | `function f() {}` |
| `lambda` | `FunctionExpression` | `function() {}` |
| `=>` | `ArrowFunctionExpression` | `() => {}` |
| `class` | `ClassDeclaration` | `class X {}` |

### Modules

| Kernel | ESTree | JS |
|---|---|---|
| `import` | `ImportDeclaration` | `import ... from "..."` |
| `export` | `ExportNamedDeclaration` | `export ...` |
| `dynamic-import` | `ImportExpression` | `import("...")` |

### Control Flow

| Kernel | ESTree | JS |
|---|---|---|
| `if` | `IfStatement` | `if (...) {} else {}` |
| `?` | `ConditionalExpression` | `... ? ... : ...` |
| `for` | `ForStatement` | `for (...) {}` |
| `for-of` | `ForOfStatement` | `for (... of ...) {}` |
| `for-in` | `ForInStatement` | `for (... in ...) {}` |
| `while` | `WhileStatement` | `while (...) {}` |
| `do-while` | `DoWhileStatement` | `do {} while (...)` |
| `switch` | `SwitchStatement` | `switch (...) {}` |
| `return` | `ReturnStatement` | `return ...` |
| `throw` | `ThrowStatement` | `throw ...` |
| `try` | `TryStatement` | `try {} catch {}` |
| `break` | `BreakStatement` | `break` |
| `continue` | `ContinueStatement` | `continue` |

### Expressions

| Kernel | ESTree | JS |
|---|---|---|
| `+`, `-`, `*`, `/`, `%`, `**` | `BinaryExpression` | `a + b` |
| `<`, `>`, `<=`, `>=` | `BinaryExpression` | `a < b` |
| `===`, `!==` | `BinaryExpression` | `a === b` |
| `&&`, `\|\|` | `LogicalExpression` | `a && b` |
| `??` | `LogicalExpression` | `a ?? b` |
| `!` | `UnaryExpression` | `!x` |
| `typeof` | `UnaryExpression` | `typeof x` |
| `new` | `NewExpression` | `new X()` |
| `get` | `MemberExpression` (computed) | `obj[key]` |
| `template` | `TemplateLiteral` | `` `...` `` |
| `object` | `ObjectExpression` | `{ ... }` |
| `array` | `ArrayExpression` | `[ ... ]` |
| `regex` | `RegExpLiteral` | `/pattern/flags` |
| `spread` | `SpreadElement` | `...x` |
