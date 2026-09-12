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
cargo install lykn-cli
```

That's it. You now have the `lykn` binary on your path — a self-contained compiler with no runtime dependencies.

If you prefer to build from source:

```sh
git clone https://github.com/lykn-lang/lykn.git
cd lykn
cargo build --release
mkdir -p bin
cp target/release/lykn bin/
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
lykn compile packages/my-app/mod.lykn       # compile to stdout
lykn run packages/my-app/mod.lykn           # compile + run from source
lykn build                                  # build workspace packages to target/lykn/build/
lykn test                                   # compile tests to target/lykn/test/ and run them
lykn test --docs docs/guides/ --fence lykn  # verify Markdown examples
lykn lint packages/my-app test              # lint Lykn source
lykn dist                                   # stage publishable packages in target/lykn/dist/
lykn publish --jsr --dry-run                # verify the staged JSR package
lykn check packages/my-app/mod.lykn         # syntax and analysis check
lykn fmt -w packages/my-app/mod.lykn        # format in place
lykn new project-name                       # scaffold a project
```

One binary for compilation, formatting, checking, running, testing, linting, package staging, publishing, and project creation. The Inquisition, one suspects, would have preferred something more complicated.
