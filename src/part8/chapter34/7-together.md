## Putting It All Together

```sh
lykn new mdify
cd mdify

# Write the source files...

lykn test                                    # verify
lykn run packages/mdify/mod.lykn input.md    # run
lykn run packages/mdify/mod.lykn input.md -o output.html  # with output file
```

~200 lines of Lykn source. Compiles to ~250 lines of clean JavaScript. Runs anywhere Deno runs. No `node_modules`. One config file.

The project exercises: `type` (the IR), `match` (rendering), `func` with typed params (every function), `cell`/`swap!` (parsing state), threading macros (inline rendering), `Result` (CLI args), `async`/`await` (file I/O), regex (inline formatting), and `for-of` iteration through the concept cards of every chapter since Chapter 4.
