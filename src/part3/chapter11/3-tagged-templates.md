## Tagged Templates

The `tag` form applies a function to a template:

```lisp
(tag html (template "<p>" user-input "</p>"))
```

```javascript
html`<p>${userInput}</p>`
```

### What Tag Functions Receive

A tag function receives the literal parts and interpolated values separately. The literal parts arrive as an array of strings; the values arrive as additional arguments. This separation is what makes tagged templates powerful — the function can process values before assembling the result.

### Use Cases

Tagged templates power some of JavaScript's most widely used libraries:

- **HTML escaping**: `html` tag functions sanitize interpolated values, preventing XSS
- **CSS-in-JS**: styled-components and lit-html use tagged templates for component styles
- **SQL queries**: tag functions parameterize interpolated values, preventing SQL injection
- **Internationalization**: tag functions look up translations for the literal parts

### `String:raw`

JavaScript's built-in `String.raw` tag returns the raw string without processing escape sequences:

```lisp
(bind path (tag String:raw (template "C:\new\test")))
```

```javascript
String.raw`C:\new\test`
```

The backslashes are literal — `\n` is not a newline, it's a backslash followed by `n`. Useful for regular expressions, file paths, and any context where you want literal backslashes.

### A Note on Usage

Most Lykn developers will *use* tagged templates (calling library-provided tag functions) rather than *write* them (implementing tag functions). The pattern is worth knowing — when you encounter `html` or `css` or `sql` tags in a library, you'll understand what they do and why they're safe.
