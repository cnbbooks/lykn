## Installing Lykn

Lykn is a young language, and young languages have the charming habit of being installed by cloning a repository rather than downloading a polished binary. This will change. For now, the process is straightforward, involves no suffering whatsoever, and Cardinal Naggum is very disappointed about that.

### Prerequisites

You need two things: **Deno** and **Git**. If you already have both, skip ahead. If not:

**Deno** is the JavaScript runtime Lykn uses. Not Node.js — Deno. It's a single binary with built-in TypeScript support, a security-first permission model, and no `node_modules` directory. Install it with:

```sh
curl -fsSL https://deno.land/install.sh | sh
```

Or, on macOS with Homebrew:

```sh
brew install deno
```

Verify with `deno --version`. You want Deno 2.x or later.

**Git** is Git. You almost certainly have it already. If `git --version` prints something, you're fine.

### Getting Lykn

Clone the repository and build the Rust tooling:

```sh
git clone https://github.com/oxur/lykn.git
cd lykn
```

That's it for the compiler. The Lykn-to-JavaScript compiler is written in JavaScript and runs under Deno — no build step required. You can compile Lykn source code the moment the clone finishes.

### The Rust Tooling (Optional)

If you have Rust installed (`rustup` and `cargo`), you can also build the Rust-based formatter and syntax checker:

```sh
cargo build --release
cp ./target/release/lykn ./bin/
```

This gives you `lykn fmt` for formatting and `lykn check` for syntax checking. These are convenience tools, not required for compilation. The compiler itself is the JavaScript pipeline running on Deno.

It is worth noting that `deno` itself is _also_ written in Rust.

### Verifying the Installation

Run the surface syntax example that ships with the project:

```sh
deno eval "import {lykn} from './src/index.js'; \
  const src = await Deno.readTextFile('examples/surface/main.lykn'); \
  eval(lykn(src))"
```

You should see output like:

```
hello, world, lykn!
S-expression syntax for JavaScript
```

If you do, the compiler is working. If you don't, check that you're in the `lykn` directory and that Deno is on your path.

### A Note on the Workflow

The observant reader will have noticed that the compile-and-run command above is somewhat... verbose. This is the current state of affairs. A proper `lykn compile` CLI and a `deno install`-able package are planned. For the examples in this book, we'll use shorter incantations — typically a small runner script or `deno eval` one-liner. The mechanics of _how_ you invoke the compiler will improve; the mechanics of _what_ it does will not change.
