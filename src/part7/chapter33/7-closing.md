## Both Compilers Have Been Seen

The surface compiler sits back down next to the kernel compiler. Two compilers, one pipeline. The kernel reads and dispatches. The surface analyzes and expands. Together they produce clean JavaScript from s-expression source.

"Was that the whole compiler?"

"Both of them, yes."

The audience claps politely. The compilers have been seen — the kernel in Chapter 30, the surface in Chapter 31. Between them: a reader, a classifier, a macro expander, an analysis engine, an emitter, a dispatch table, and a pretty-printer. The complete path from `(bind greeting "Hello, World!")` to `const greeting = "Hello, World!";`.

Not magic. Just compilation. And now the reader knows how it works.
