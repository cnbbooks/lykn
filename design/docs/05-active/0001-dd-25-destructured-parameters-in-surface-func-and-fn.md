---
number: 1
title: "DD-25: Destructured Parameters in Surface `func` and `fn`"
author: "Duncan McGreggor"
component: All
tags: [change-me]
created: 2026-04-14
updated: 2026-04-14
state: Active
supersedes: null
superseded-by: null
version: 1.0
---

# DD-25: Destructured Parameters in Surface `func` and `fn`

## Context

Surface `func` and `fn` only accept flat `:type name` pairs in their parameter lists. Destructuring patterns (`(object ...)`, `(array ...)`) in parameter position cause a compile error because `parseTypedParams` (JS) and `parse_typed_params` (Rust) reject non-atoms in the name position.

The kernel `function` form already supports destructuring via DD-06. The gap is in the *surface layer* — no design was ever created for integrating the surface type annotation requirement with destructuring patterns.

**The decision**: Option B — every destructured field gets a type keyword. `:any` is the explicit opt-out. No bare names in destructuring patterns. This matches the existing surface principle: "if you name it in `:args`, you type it."

**Why this matters**: Without this, the book (Ch 15) has to recommend a two-step workaround — typed param + body destructuring — instead of the clean single-step pattern. And developers lose type safety at the destructuring boundary, which is exactly where bugs enter.

## Proposed Syntax

```lisp
;; Object destructuring in func :args
(func process
  :args ((object :string name :number age) :string action)
  :returns :string
  :body (template name " (" age ") — " action))

;; Array destructuring
(func head-tail
  :args ((array :number first (rest :number remaining)))
  :body (console:log first remaining))

;; fn with destructured params
(bind f (fn ((object :string name :number age)) (console:log name age)))

;; Mixed: destructured + simple
(func handler
  :args ((object :string method :string url) :any body)
  :body ...)
```

A destructuring pattern is a **list starting with `object` or `array`** containing `:type name` pairs inside. It appears in `:args` position where a `:type name` pair would normally go — but without a preceding type keyword (the pattern head `object`/`array` implies the type).

## Compiled Output

```javascript
// Dev mode
function process({name, age}, action) {
  if (typeof name !== "string")
    throw new TypeError("process: arg 'name' expected string, got " + typeof name);
  if (typeof age !== "number" || Number.isNaN(age))
    throw new TypeError("process: arg 'age' expected number, got " + typeof age);
  if (typeof action !== "string")
    throw new TypeError("process: arg 'action' expected string, got " + typeof action);
  return `${name} (${age}) — ${action}`;
}

// --strip-assertions
function process({name, age}, action) {
  return `${name} (${age}) — ${action}`;
}
```

The kernel handles the structural destructuring (`{name, age}`). The surface emits per-field type checks as body statements.

---

## Implementation Steps

### Step 1: JS Surface Compiler — `parseTypedParams` (src/surface.js:217)

**Current**: Steps by 2 through values, expects keyword at `i`, atom at `i+1`.

**Change**: Variable step size. When `values[i]` is a list (starts with `object`/`array`), parse it as a destructured param and step by 1. When `values[i]` is a keyword, consume the `:type name` pair and step by 2.

```javascript
function parseTypedParams(paramList) {
  const params = [];
  const values = paramList.values;
  let i = 0;
  while (i < values.length) {
    if (isArray(values[i])) {
      // Destructured param: (object :string name :number age)
      params.push(parseDestructuredParam(values[i]));
      i += 1;
    } else if (isKeyword(values[i])) {
      // Standard :type name pair
      if (i + 1 >= values.length) throw ...;
      params.push({ typeKw: values[i], name: values[i + 1] });
      i += 2;
    } else {
      throw new Error(`expected type keyword or destructuring pattern at position ${i}`);
    }
  }
  return params;
}
```

**New function `parseDestructuredParam(listNode)`**:
- Validates `listNode.values[0]` is atom `"object"` or `"array"`
- Parses remaining values as `:type name` pairs (same alternation)
- For `array` patterns: handles `(rest :type name)` as a 3-element sub-form
- Returns `{ destructured: true, kind: "object"|"array", fields: [...], rest: null|{...} }`

### Step 2: JS Surface Compiler — Type Check + Kernel Emission Helpers

**New helper `paramToKernel(p)`**: Converts a parsed param to kernel form:
- Simple: returns `p.name` (atom)
- Destructured object: returns `array(sym("object"), ...p.fields.map(f => f.name))`
- Destructured array: returns `array(sym("array"), ...elements)` with `(rest name)` if present

**New helper `paramTypeChecks(p, funcName)`**: Returns array of type check AST nodes:
- Simple: returns `[buildTypeCheck(p.name, p.typeKw, funcName, "arg")]` (filtering nulls)
- Destructured: returns `p.fields.map(f => buildTypeCheck(f.name, f.typeKw, funcName, "arg"))` (filtering nulls)

### Step 3: JS Surface Compiler — `buildSingleClauseFunc` (src/surface.js:989)

Change lines 1004-1015:
- `paramNames` → `params.map(paramToKernel)` (uses new helper)
- Type checks → `params.flatMap(p => paramTypeChecks(p, funcName))` (uses new helper)

### Step 4: JS Surface Compiler — `buildMultiClauseFunc` (src/surface.js:1133)

Changes:
- **Arity**: count each param as 1 (destructured or simple)
- **Dispatch condition**: for destructured object params, check `typeof args[i] === "object" && args[i] !== null`; for array, check `Array.isArray(args[i])`
- **Param binding**: emit `(const (object name age) (get args i))` for destructured params
- **Field type checks**: iterate fields, emit checks for each

### Step 5: JS Surface Compiler — `fnMacro` (src/surface.js:829)

Same pattern: `paramNames` uses `paramToKernel`, type checks use `paramTypeChecks`.

### Step 6: Rust AST — `ast/surface.rs`

Add `ParamShape` enum:

```rust
#[derive(Debug, Clone, PartialEq)]
pub enum ParamShape {
    Simple(TypedParam),
    DestructuredObject {
        fields: Vec<TypedParam>,
        span: Span,
    },
    DestructuredArray {
        elements: Vec<ArrayParamElement>,
        span: Span,
    },
}

#[derive(Debug, Clone, PartialEq)]
pub enum ArrayParamElement {
    Typed(TypedParam),
    Rest(TypedParam),
    Skip(Span),
}
```

Update `FuncClause::args` from `Vec<TypedParam>` to `Vec<ParamShape>`.
Update `SurfaceForm::Fn::params` from `Vec<TypedParam>` to `Vec<ParamShape>`.

**Note**: `Constructor::fields` stays as `Vec<TypedParam>` — destructuring doesn't apply to type constructors.

### Step 7: Rust Classifier — `classifier/forms.rs`

Update `parse_typed_params` to return `Vec<ParamShape>`. Variable-step loop matching JS implementation. Add `parse_destructured_param` for pattern parsing.

Add `parse_simple_typed_params` (the original behavior) for use by `type` constructor field parsing only.

### Step 8: Rust Emitter — `emitter/forms.rs`

Add helpers mirroring JS:
- `param_shape_to_kernel(shape) -> SExpr` — converts to kernel param
- `param_shape_type_checks(shape, func_name, ctx) -> Vec<SExpr>` — emits per-field checks

Update `emit_func_single`, `emit_func_multi`, `emit_fn_expr` to use these helpers.

### Step 9: Rust Analysis — `analysis/func_check.rs`

Multi-clause overlap detection uses param types. For destructured params, the "type" for overlap purposes is `object` or `array` (the pattern kind). Two clauses with `(object :string name)` and `(object :number x)` overlap because they both accept objects — Maranget's algorithm should treat them as overlapping at the outer type level.

### Step 10: Tests

**New JS fixture**: `test/fixtures/surface/func-destructuring.json`
- Object destructured param with typed fields
- Array destructured param with typed fields
- Mixed destructured + simple params
- `fn` with destructured param
- `:any` field in destructured pattern (no check)
- Nested destructuring (if supported)
- `rest` in array destructured param
- Error: bare name (no type) in destructured pattern
- Error: destructured pattern not starting with `object`/`array`

**New JS tests**: `test/surface/func-destructuring.test.js`
- Compilation output verification
- Execution verification (call with correct/incorrect types)
- `--strip-assertions` verification

**Rust tests**: In `classifier/forms.rs` and `emitter/forms.rs` test modules.

### Step 11: DD Document

Write `workbench/DD-25-destructured-func-params.md` documenting the decision, syntax, compilation strategy, edge cases, and rejected alternatives.

### Step 12: Book Update

Update `src/part3/chapter15/3-parameter-destructuring.md` to show the surface syntax now working, remove the "current limitation" note, and show the clean per-field typed pattern.

---

## Implementation Order

1. DD-25 document (design spec)
2. Rust AST changes (ParamShape enum) — foundational type
3. Rust classifier (parse_typed_params) — parsing
4. Rust emitter (func/fn emission) — code generation
5. Rust analysis (overlap detection update)
6. JS surface compiler (all four functions)
7. Tests (both compilers)
8. Book chapter update

## Edge Cases

| Case | Behavior |
|------|----------|
| Bare name in destructured pattern | Compile error — all fields must be typed |
| `:any` field | No type check emitted for that field |
| Nested destructuring `(object :string name (alias addr (object :string city)))` | Deferred to future — start with flat patterns |
| `default` in destructured fields | Syntax: `(object (default :string name "anon") :number age)` — needs design |
| Destructured param in `type` constructor | Not supported — constructors use simple TypedParam |
| Multi-clause with destructured + simple overlapping on object type | Overlap — compile error |
| `--strip-assertions` | Type checks removed, destructuring pattern preserved |

## Verification

1. `cargo test` — Rust compiler tests pass
2. `deno task test` — JS compiler tests pass
3. Manual: `lykn compile` a file with destructured func params → correct JS output
4. Manual: `lykn compile --strip-assertions` → checks stripped, destructuring preserved
5. Execute compiled JS to verify runtime behavior
6. `mdbook build` — book compiles after chapter update
