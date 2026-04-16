## The `lykn` CLI

The compiler binary:

```sh
# Compile
lykn compile src/app.lykn              # to stdout
lykn compile src/app.lykn -o dist/app.js  # to file
lykn compile --strip-assertions src/   # production mode
lykn compile --kernel-json src/app.lykn   # debug: kernel JSON output

# Check
lykn check src/app.lykn               # syntax validation, no output

# Format
lykn fmt src/app.lykn                  # format to stdout
lykn fmt -w src/app.lykn              # format in place
```

### `--strip-assertions`

Removes type checks, contracts (`:pre`/`:post`), `bind` type checks (DD-24), and constructor validation from the output. Multi-clause dispatch checks are NOT stripped — they're runtime semantics. Development builds catch type errors; production builds run clean.

### Exit Codes

`0` on success, `1` on compile error. Error messages include source location (file, line, column) and the failing expression. The reader has seen these errors throughout the book — every "COMPILE ERROR" example comes from the same error reporting system.
