## Installing Lykn

### Prerequisites

You need two things: **Deno** and **Rust** (for the compiler).

**Deno** is the JavaScript runtime Lykn uses for running compiled output, testing, and the development workflow:

```sh
brew install deno
```

**Rust** is the language the Lykn compiler is written in. Install it via rustup:

```sh
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

### Installing the Compiler

```sh
cargo install lykn
```

That's it. You now have the `lykn` binary on your path — a self-contained compiler with no runtime dependencies.

If you prefer to build from source:

```sh
git clone https://github.com/oxur/lykn.git
cd lykn
cargo build --release && cp target/release/lykn bin/
```

### Your First Project

```sh
lykn new my-app
cd my-app
```

`lykn new` scaffolds a workspace with `project.json`, a starter module, a test file using the `@lykn/testing` DSL, and `README.md` + `LICENSE` for publishing.

### Verifying

```sh
lykn run packages/my-app/mod.lykn
```

If you see output, the compiler is working.

### The Full Toolkit

```sh
lykn compile main.lykn                    # compile to stdout
lykn compile main.lykn -o main.js         # compile to file
lykn compile main.lykn --strip-assertions # production mode
lykn run main.lykn                        # compile + run
lykn test                                 # run project tests
lykn check main.lykn                      # syntax check
lykn fmt main.lykn                        # format to stdout
lykn fmt -w main.lykn                     # format in place
lykn new project-name                     # scaffold a project
```

One binary for compilation, formatting, checking, running, testing, and project creation. The Inquisition, one suspects, would have preferred something more complicated.
