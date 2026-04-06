## Running Lykn Code

There are three ways to run Lykn, each suited to a different context. Think of them as the three weapons the Inquisition actually remembered to bring.

### The CLI

The primary workflow is compile-then-run. The Lykn compiler produces JavaScript; you run it with any JavaScript runtime:

```sh
lykn compile hello.lykn -o hello.js
deno run hello.js
```

That's the full cycle. Compile to a file, run the file. For quick iteration, you can pipe the output directly:

```sh
lykn compile hello.lykn | deno run -
```

Or compile to stdout and inspect the JavaScript before running it:

```sh
lykn compile hello.lykn
```

The `--strip-assertions` flag removes all type checks and contracts from the output, producing the minimal JavaScript for production deployment:

```sh
lykn compile hello.lykn --strip-assertions -o hello.min.js
```

Deno is shown here, but the output is standard JavaScript — Node.js, Bun, or any other runtime will work.

### The Browser

Lykn ships a browser bundle that lets you write s-expressions directly in HTML:

```html
<script src="dist/lykn-browser.dev.js"></script>
<script type="text/lykn">
  (bind el (document:get-element-by-id "output"))
  (= el:text-content "Hello from Lykn!")
</script>
```

The browser shim finds every `<script type="text/lykn">` tag, compiles it, and evaluates the result. It also provides a programmatic API:

```javascript
lykn.compile('(+ 1 2)')   // → "1 + 2;\n"
lykn.run('(+ 1 2)')       // → 3
await lykn.load('/app.lykn')
```

To build the browser bundle from source: `deno task build`. The full browser story — loading external `.lykn` files, working with the DOM, inline macros — is covered in later chapters. For now, know that it exists and that it works.

### The Formatter and Checker

The same `lykn` binary that compiles your code also formats and checks it:

```sh
lykn fmt hello.lykn          # format to stdout
lykn fmt -w hello.lykn       # format in place
lykn check hello.lykn        # syntax check
```

The formatter produces consistently indented Lykn source. The syntax checker validates that your s-expressions are well-formed without running the full compilation pipeline. Both are fast — they're the same Rust binary — and have no runtime dependencies.
