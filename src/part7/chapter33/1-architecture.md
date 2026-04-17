## Architecture: Six Modules

The surface compiler is a Rust toolchain *library*, not a monolithic binary. Six modules, three consumers.

### The Modules

| Module | Purpose | Crate location |
|---|---|---|
| Reader | S-expression text → generic tree | `lykn-lang/reader` |
| Classifier | Generic tree → typed surface AST | `lykn-lang/classifier` |
| Macro expander | Three-pass expansion pipeline | `lykn-lang/expander` |
| Analysis | Exhaustiveness, overlap, scope | `lykn-lang/analysis` |
| Emitter | Surface AST → kernel forms | `lykn-lang/emitter` |
| Diagnostics | Error messages with source locations | `lykn-lang/diagnostics` |

### The Consumers

| Consumer | Uses |
|---|---|
| `lykn compile` | All six modules → JavaScript output |
| `lykn check` | Reader + classifier + analysis → diagnostics only |
| `lykn fmt` | Reader → reformatted source |
| `lykn run` | All six modules → execute via Deno |
| `lykn test` | All six modules → compile tests, run via Deno |

The key insight: the compiler, linter, and formatter share the same reader and classifier. A bug found by `lykn check` uses the same AST as `lykn compile`. This is the DD-20 architecture — a modular library, not a monolithic tool.
