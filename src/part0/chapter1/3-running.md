## Running Lykn Code

There are three ways to run Lykn, each suited to a different context. Think of them as the three weapons the Inquisition actually remembered to bring.

### `lykn run`

The primary workflow — compile and run in one step:

```sh
lykn run hello.lykn
```

That's it. The compiler produces JavaScript and executes it via Deno. For inspecting the compiled output before running, use `lykn compile`:

```sh
lykn compile hello.lykn          # print JS to stdout
lykn compile hello.lykn -o hello.js  # write to file
```

The `--strip-assertions` flag removes all type checks and contracts, producing minimal JavaScript for production:

```sh
lykn compile hello.lykn --strip-assertions -o hello.min.js
```

### The Browser

Lykn ships a browser bundle that lets you write s-expressions directly in HTML:

```html
<script src="dist/lykn-browser.js"></script>
<script type="text/lykn">
  (bind el (document:get-element-by-id "output"))
  (set! el:text-content "Hello from Lykn!")
</script>
```

The browser shim finds every `<script type="text/lykn">` tag, compiles it, and evaluates the result. It also provides a programmatic API:

```javascript
lykn.compile('(+ 1 2)')   // → "1 + 2;\n"
lykn.run('(+ 1 2)')       // → 3
await lykn.load('/app.lykn')
```

The full browser story — loading external `.lykn` files, working with the DOM, inline macros — is covered in later chapters. For now, know that it exists and that it works.

### The Formatter and Checker

The same `lykn` binary also formats and checks:

```sh
lykn fmt hello.lykn          # format to stdout
lykn fmt -w hello.lykn       # format in place
lykn check hello.lykn        # syntax check
```

The formatter produces consistently indented Lykn source. The syntax checker validates well-formedness without the full compilation pipeline. Both are fast — same Rust binary — and have no runtime dependencies.
