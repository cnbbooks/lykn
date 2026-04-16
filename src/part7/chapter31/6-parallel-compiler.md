## The Parallel JS Surface Compiler

The Rust compiler has a parallel JS implementation — a reference compiler in `packages/lykn/surface.js` that implements all surface forms as macros using the DD-13 pipeline. It's the same compiler the browser shim uses.

### Why Two Compilers?

**The JS compiler is the reference**: canonical test fixtures, easier to iterate during design. It was written first and defines the semantics.

**The Rust compiler is the production tool**: faster, emits diagnostics, runs analysis. It's what `lykn compile` invokes.

**Cross-compiler tests verify agreement**: both compilers produce identical kernel output for the same input. This means the surface language is defined by its *expansion rules*, not by either implementation. A surface form's definition is: "what kernel forms does it produce?" Both compilers answer the same way.

### In the Browser

The browser shim (Ch 27) bundles the JS surface compiler + the JS kernel compiler. When a `<script type="text/lykn">` tag is compiled in the browser, it runs through the JS pipeline — the same reference implementation that defines the semantics. The Rust compiler isn't available in the browser; the JS compiler is.
