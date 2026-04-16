## The Three Compilation Phases

After macro expansion, the surface compiler runs three phases.

### Phase 1: Collection

Build the type registry and function signatures.

- Scan for `type` definitions: register constructors, field names, field types, blessed type flags (`Option`, `Result`)
- Scan for `func` signatures: register arities, type keywords, multi-clause dispatch signatures
- Load prelude: `Option` and `Result` from `lykn/core`, auto-imported into every module

### Phase 2: Analysis

Check correctness using the collected information.

**Exhaustiveness checking** (DD-21): For every `match` expression, verify all variants are covered. Uses Maranget's algorithm. Guards make clauses partial — they don't count toward coverage.

**Overlap detection**: For every multi-clause `func`, verify no two clauses accept the same argument types. Same algorithm, different consumer.

**Scope tracking**: Track every binding introduced by `bind`, `func`, `fn`, destructuring, `for-of`, `try`/`catch`. Detect unused bindings (warnings) and undefined references (errors).

**Type inference from patterns**: Constructor patterns infer the matched type. Mixed constructors from different types are a compile error.

### Phase 3: Emission

Transform the analyzed surface AST into kernel forms.

- `func` → `function` with type checks, contracts, dispatch chain
- `bind` → `const` with type check if annotated (DD-24)
- `fn` → `=>` with type checks
- `type` → constructor functions with field validation
- `match` → nested `if` chains (IIFE in value position)
- `cell` → `{ value: x }`, threading macros → nested calls or IIFEs
- `--strip-assertions` → type checks and contracts removed

The emitter produces kernel forms that feed into the JS kernel compiler (Ch 30) or the Rust codegen. The full pipeline from surface source to JavaScript is complete.
