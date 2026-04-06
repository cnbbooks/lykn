## Why Not `let` and `var`?

JavaScript arrived at three declaration keywords through a process not entirely unlike geological sedimentation: each layer was deposited by a different era, and the older layers cannot be removed without destabilizing the ones above.

### `var`: The Original Sin

`var` was JavaScript's only declaration keyword for its first twenty years. It has three properties, each of which is a documented source of bugs:

**Function scope.** A `var` inside an `if` block is visible throughout the entire enclosing function. This violates the principle of least surprise so reliably that it constitutes its own entry in the BugAID catalog.

**Hoisting.** The declaration (but not the initialization) is moved to the top of the function. This means you can reference a `var` before its declaration line and get `undefined` instead of an error — silently, without warning, as though this were a perfectly reasonable thing for a language to do.

**Redeclaration.** You can declare the same `var` twice in the same scope without error. This makes typos invisible and copy-paste errors undetectable.

Lykn never emits `var`. Not for any reason. Not in any context.

### `let`: The Compromise

ES2015 introduced `let` as the modern replacement for `var`. It fixed the scope (block-scoped instead of function-scoped) and the hoisting (temporal dead zone instead of silent `undefined`). But it kept the one property that Lykn considers unacceptable: reassignment.

```javascript
let count = 0;
count = 1;        // allowed
count = "hello";  // also allowed — no type checking
```

Reassignment is the mechanism by which state becomes invisible. Once a name can hold different values at different times, every reference to that name requires the reader to trace the execution history to know what it currently contains. The binding has become a variable, and variables — by their nature — resist reasoning.

Lykn doesn't emit `let` from surface code. If you genuinely need it (rare, and usually for JS interop), the `js:` namespace provides `(js:let x 0)`.

### `const`: The Right Idea, Incomplete

`const` is what `bind` compiles to, and it's the closest JavaScript gets to what Lykn wants. Block-scoped, no redeclaration, no reassignment. But `const` has a famous limitation that every JavaScript developer has encountered:

```javascript
const scores = [98, 87, 92];
scores.push(100);              // allowed!
const user = { name: "Duncan" };
user.name = "Someone Else";    // also allowed!
```

`const` prevents *reassignment* of the binding, not *mutation* of the value. The name `scores` will always point to the same array, but the array itself can be changed from anywhere.

Lykn addresses this not by changing what `const` means (it can't — that's JavaScript's semantics) but by providing tools that make immutable patterns the default. `assoc`, `dissoc`, and `conj` produce new values instead of mutating existing ones. `cell` makes mutation explicit and visible. The surface language doesn't prevent you from mutating a `const` object through kernel code or JS interop — but it makes the immutable path so convenient that mutation becomes the exception rather than the rule.

### The Punchline

JavaScript needed three keywords because it couldn't decide how strict to be. `var` was too loose. `let` was half-strict. `const` was strict about the wrong thing. Lykn decided: one keyword, always `const`, and a separate mechanism for the cases where mutation is genuinely needed.
