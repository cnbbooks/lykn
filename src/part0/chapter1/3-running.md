## Running Lykn Code

There are three ways to run Lykn, each suited to a different context. Think of them as the three weapons the Inquisition actually remembered to bring.

### The CLI

The primary workflow is compile-and-run via Deno. From the Lykn project directory:

```sh
deno eval "import {lykn} from './src/index.js'; \
  const src = await Deno.readTextFile('hello.lykn'); \
  console.log(lykn(src))"
```

This reads a `.lykn` file, compiles it to JavaScript, and prints the output. To *run* the compiled code instead of printing it, replace `console.log` with `eval`:

```sh
deno eval "import {lykn} from './src/index.js'; \
  const src = await Deno.readTextFile('hello.lykn'); \
  eval(lykn(src))"
```

For a more permanent setup, you can write a small runner script:

```javascript
import { lykn } from './src/index.js';
const src = await Deno.readTextFile(Deno.args[0]);
eval(lykn(src));
```

Save that as `run.js` and invoke it with `deno run -A run.js hello.lykn`. The examples in this book assume some such convenience exists.

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

### The Rust Tools

The Rust binary (`./bin/lykn` after `cargo build --release`) provides two commands:

```sh
lykn fmt hello.lykn          # format to stdout
lykn fmt -w hello.lykn       # format in place
lykn check hello.lykn        # syntax check
```

These are developer tools — they don't compile to JavaScript. The formatter produces consistently indented Lykn source. The syntax checker validates that your s-expressions are well-formed without running the full compilation pipeline. Both are fast (they're Rust) and have no runtime dependencies.

### What's Coming

A standalone `lykn compile` command, a Deno-installable package, and a watch mode are all on the roadmap. The compilation pipeline itself — reader, surface compiler, kernel compiler, astring — is stable and tested (555 tests at last count). What's missing is packaging, not capability. The parrot can speak; it just hasn't been given a proper stage yet.
