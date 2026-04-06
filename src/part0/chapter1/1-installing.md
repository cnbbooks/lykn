## Installing Lykn

Lykn is a young language, and young languages have the charming habit of being installed by cloning a repository rather than downloading a polished binary. This will change. For now, the process is straightforward, involves no suffering whatsoever, and Cardinal Naggum is very disappointed about that.

### Prerequisites

You need two things: **Rust** and **Git**. If you already have both, skip ahead. If not:

**Rust** is the language the Lykn compiler is written in. Install it via rustup:

```sh
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

Verify with `cargo --version`. Any recent stable Rust will do.

**Git** is Git. You almost certainly have it already. If `git --version` prints something, you're fine.

You will also want **Deno** (or any JavaScript runtime) to *run* the compiled output, since the compiler produces JavaScript. But Deno is not required for compilation itself — that's pure Rust.

```sh
brew install deno
```

### Getting Lykn

Clone the repository and build the compiler:

```sh
git clone https://github.com/oxur/lykn.git
cd lykn
cargo build --release
cp ./target/release/lykn ./bin/
```

That's it. You now have a self-contained `lykn` binary that compiles `.lykn` files to JavaScript with no runtime dependencies.

### Verifying the Installation

Compile and run the surface syntax example that ships with the project:

```sh
lykn compile examples/surface/main.lykn -o /tmp/main.js
deno run /tmp/main.js
```

You should see output like:

```text
hello, world, lykn!
S-expression syntax for JavaScript
```

If you do, the compiler is working. If you don't, check that `./bin/lykn` is on your path (or use `./bin/lykn compile ...` explicitly).

### The Full Toolkit

The `lykn` binary does more than compile:

```sh
lykn compile main.lykn                    # compile to stdout
lykn compile main.lykn -o main.js         # compile to file
lykn compile main.lykn --strip-assertions # omit type checks / contracts
lykn fmt main.lykn                        # format to stdout
lykn fmt -w main.lykn                     # format in place
lykn check main.lykn                      # syntax check
```

One binary, no runtime dependencies, no configuration files. The Inquisition, one suspects, would have preferred something more complicated.
