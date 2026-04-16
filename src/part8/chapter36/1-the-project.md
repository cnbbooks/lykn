## The Project: `shortn-ui`

A web interface for the `shortn` URL shortener (Ch 35).

### Features

- Form for entering a long URL
- POSTs to the `shortn` API, displays the short URL
- Lists all shortened URLs with click counts
- Copy button for each short URL
- Error display for failed requests

### Project Structure

```text
shortn-ui/
  index.html           ← static HTML shell
  packages/
    shortn-ui/
      app.lykn         ← entry point, state, wiring
      api.lykn         ← fetch wrappers
      render.lykn      ← DOM rendering
  project.json
```

### The HTML Shell

```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>shortn</title>
  <style>
    body { font-family: system-ui; max-width: 600px; margin: 2em auto; }
    form { display: flex; gap: 0.5em; margin-bottom: 2em; }
    input[type=url] { flex: 1; padding: 0.5em; }
    .entry { padding: 1em; border: 1px solid #ddd; margin-bottom: 0.5em; }
    .code { font-family: monospace; font-weight: bold; }
    .error { color: #c00; }
  </style>
</head>
<body>
  <h1>shortn</h1>
  <form id="shorten-form">
    <input type="url" id="url-input" placeholder="https://..." required>
    <button type="submit">Shorten</button>
  </form>
  <div id="error" class="error"></div>
  <h2>Shortened URLs</h2>
  <div id="entries"></div>
  <script type="module" src="dist/app.js"></script>
</body>
</html>
```

Minimal HTML. All logic is in the compiled JS.
