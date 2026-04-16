## Running Lykn in the Browser

Two paths to the browser.

### Development: The Browser Shim

```html
<script src="lykn-browser.js"></script>
<script type="text/lykn">
  (bind el (document:get-element-by-id "app"))
  (set! el:text-content "Hello from Lykn!")
</script>
```

The browser shim finds `<script type="text/lykn">` tags, compiles them to JavaScript via the bundled JS compiler, and executes the result. Error messages appear in the browser console.

This is the development path — convenient for prototyping. The compiler runs on every page load, so it's not for production.

### Production: Compiled ESM

```sh
lykn compile src/app.lykn -o dist/app.js
```

```html
<script type="module" src="dist/app.js"></script>
```

Compile once, serve the JavaScript. No runtime compiler in the browser. The compiled output is clean ESM that any browser understands.

### Which to Use

The shim for rapid prototyping and learning. Compiled ESM for anything deployed. The compilation step adds nothing to the output — it's the same JavaScript either path produces.
