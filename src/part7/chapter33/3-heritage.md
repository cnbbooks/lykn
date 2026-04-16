## What Lykn Learned from Other Languages

Lykn's design draws from a specific lineage. No idea is original; every idea is composed.

**From Scheme**: the irreducible core. Five primitive forms from which everything else derives. Lykn's kernel follows this: a small set of forms that map to JavaScript.

**From Common Lisp**: keywords (`:name`), the colon-package convention adapted to `obj:prop`. Practical macros — `defmacro` style, not `syntax-rules`.

**From Clojure**: threading macros (`->`, `->>`), immutability by default, atoms (renamed to `cell`), the `!` convention for mutation. Keywords as data.

**From Erlang/LFE**: multi-clause function dispatch. Pattern matching. The functional commitment. The thin-skin-over-host philosophy — LFE over BEAM, Lykn over JavaScript. Duncan's direct heritage as an LFE contributor.

**From Rust**: `Cell<T>` naming, `Option`/`Result` types, exhaustiveness checking. The "make illegal states unrepresentable" philosophy.

**From Fennel**: thin-skin-over-Lua as proof that the approach works. No runtime. Compile-time macros. Small compiler. Clean output.

**From JavaScript itself**: ESTree, ESM, async/await, the event loop, template literals, destructuring. Lykn doesn't fight JavaScript — it embraces its good parts and constrains its hazardous ones.
