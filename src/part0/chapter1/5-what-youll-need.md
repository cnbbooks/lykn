## What You'll Need for This Book

### The Essentials

To follow along with the examples in this book, you need:

- **Deno** (2.x or later) — the runtime that powers the Lykn compiler
- **A text editor** — any editor that can save a file with a `.lykn` extension. Lykn files are plain text. If your editor supports Lisp or Scheme syntax highlighting, enable it — the parenthesis matching alone is worth it.
- **The Lykn repository** — cloned as described in the installation section above

That's the list. There is no build system to configure, no `package.json` to maintain, no `node_modules` to summon from the void. The compiler is JavaScript running on Deno. The output is JavaScript with no dependencies. The Rust tooling is optional.

### What You Should Know

This book assumes you know what a variable is, what a function does, and that computers exist. Beyond that, it assumes remarkably little.

If you have JavaScript experience, you will find familiar ground quickly — every Lykn concept maps to a JavaScript concept, and this book points out the mapping at every step. The concept cards drawn from *Exploring JavaScript*, *Deep JavaScript*, *Eloquent JavaScript*, and *JavaScript: The Definitive Guide* ensure that the JavaScript side is covered with depth and precision.

If you're new to JavaScript, this book teaches it. You will learn JavaScript's scoping rules, its type system, its prototype chain, its module system, and its async model — but you'll learn them through Lykn's lens, which has the advantage of making the dangerous parts visible and the safe parts default.

If you have Lisp experience, you will feel at home with the syntax and occasionally startled by the vocabulary. Lykn uses `bind` where you expect `def`, `func` where you expect `defun`, and `fn` where you expect `lambda`. The reason — short English words over traditional abbreviations — is a deliberate design choice. The parentheses, at least, are exactly where you left them.

### Editor Support

There is no dedicated Lykn editor plugin yet. For now, configure your editor's file associations to treat `.lykn` files as Scheme or Common Lisp. This gives you parenthesis matching, rainbow delimiters (if your editor supports them), and reasonable indentation. The keyword syntax (`:string`, `:args`) won't highlight perfectly, but the structural editing — the part that actually matters when writing s-expressions — will work.
