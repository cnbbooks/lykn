## Development vs Production

### Development: The Shim

```html
<script src="lykn-browser.js"></script>
<script type="text/lykn">
  (bind app (document:get-element-by-id "app"))
  (set! app:text-content "Hello from Lykn!")
</script>
```

No build step. Edit the `.lykn` source, refresh the page. Compilation happens on every load — fine for prototyping, not for production.

### Production: Pre-Compiled ESM

```sh
lykn compile --strip-assertions src/app.lykn -o dist/app.js
```

```html
<script type="module" src="dist/app.js"></script>
```

Zero compilation overhead. Tree-shakeable. Smallest possible payload. The shim isn't loaded — just clean JavaScript.

### The Rule

Shim for prototyping and learning. Compiled ESM for anything served to users. You don't ship the compiler to production — the same principle as TypeScript's `tsc` vs shipping compiled JS.
