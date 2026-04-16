## How the Shim Works

The compile-then-eval pipeline, in the browser.

### Step 1: Load the Shim

```html
<script src="lykn-browser.js"></script>
```

`lykn-browser.js` bundles the JS reader, the JS surface compiler, the JS kernel compiler, and astring. It registers a handler that runs on `DOMContentLoaded`.

### Step 2: Scan for Lykn Script Tags

The shim finds every `<script type="text/lykn">` tag on the page:

```javascript
document.querySelectorAll('script[type="text/lykn"]')
  .forEach(tag => {
    const source = tag.textContent;
    const js = lykn(source);    // compile
    new Function(js)();          // execute
  });
```

### Step 3: Compile and Execute

Each tag's `textContent` is compiled to JavaScript via the bundled compiler and executed. The compiled JS runs in the page's scope — it can access the DOM, call `fetch`, use `console:log`.

### External Files

```html
<script type="text/lykn" src="app.lykn"></script>
```

The shim fetches the file, compiles it, and executes the result. This requires the page to be served (not opened as `file://`) because `fetch` doesn't work on local files.

### Compile, Not Interpret

The shim doesn't *interpret* Lykn. It compiles it to JavaScript and runs the JavaScript. The compiled output is identical to what `lykn compile` produces on the command line. The Lykn compiler is a compiler, even in the browser.
