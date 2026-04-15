## ES Modules in Lykn

All Lykn code compiles with `sourceType: "module"`. There is no CommonJS. No `require`. No `module.exports`. No `.mjs` vs `.js` confusion. Just modules.

### What This Means

- **Top-level `bind` forms are module-scoped**, not global. No accidental pollution of `globalThis`.
- **Top-level `await` works** — modules can await at the top level (Ch 17 covers async in detail).
- **`import` and `export` are available** — the forms covered in this chapter.
- **Strict mode is implicit** — all module code runs in strict mode. No `"use strict"` needed.

### No CommonJS

Before ES modules, Node.js used CommonJS: `require()` for imports, `module.exports` for exports. CommonJS modules are synchronous, don't support tree-shaking, and have different semantics from ESM (value copies vs live bindings).

Lykn skips all of this. If your project needs to consume a CommonJS package, Deno handles the interop transparently. Lykn doesn't need to.

The reader coming from a Node.js background may miss `require`. The reader who has debugged a dual-package hazard will not.
