## astring: The Pretty-Printer

astring is a vendored library (~16KB) that converts ESTree ASTs to JavaScript source code. It's the last stage of the JS pipeline.

### What astring Does

- Prints valid JavaScript from any valid ESTree AST
- Handles operator precedence and parenthesization
- Produces clean, readable output — no unnecessary parentheses, consistent formatting
- Supports source maps (available for future use)

### Why Vendored

astring is stable, well-tested, and small. By vendoring it, Lykn avoids npm dependencies. The version is pinned and tested with every release.

### The Output Philosophy

Lykn's compiled JavaScript should look like a human wrote it. No compilation artifacts, no runtime markers, no generated variable names (except gensyms from macros). astring makes this possible — the output is clean because the pretty-printer is mature and the input (ESTree) is standard.

### The Rust Alternative

The Rust compiler's codegen module produces JavaScript directly — no ESTree, no astring. It's a pure-Rust code generator that walks kernel s-expressions and emits text. Both paths produce equivalent output; the Rust path is faster and has no external dependencies.
