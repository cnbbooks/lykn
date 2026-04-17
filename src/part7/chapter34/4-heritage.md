## Heritage: BiwaScheme and Wisp

The browser shim pattern comes from two predecessors.

### BiwaScheme

A Scheme interpreter that runs in the browser via `<script type="text/biwascheme">`. It finds script tags, reads their content, and interprets it. The key difference: BiwaScheme *interprets* Scheme. Lykn *compiles* to JavaScript. Compilation is faster for repeated execution and produces standard JS that the browser's JIT can optimize.

### Wisp

A Clojure-like Lisp that compiles to JavaScript. Its browser shim uses `<script type="application/wisp">` with a similar scan-compile-eval pattern. Wisp proved that compile-then-eval works for Lisp-to-JS languages in the browser.

### Lykn's Contribution

Lykn's shim follows the same pattern but bundles a surface compiler with type checking and exhaustiveness analysis. The compile errors are richer — source locations, typed parameter hints, exhaustiveness warnings — because the surface compiler (Ch 33) runs in the browser too.
