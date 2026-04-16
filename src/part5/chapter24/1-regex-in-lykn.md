## Regex in Lykn

The `regex` kernel form constructs regular expression literals:

```lisp
(bind pattern (regex "^hello" "i"))
```

```javascript
const pattern = /^hello/i;
```

The first argument is the pattern string, the second is the flags string (optional). The form compiles to a `RegExpLiteral` ESTree node.

### Double Backslashes

Because the pattern is a Lykn string literal, backslashes need escaping: `\\d` in Lykn source produces `\d` in the compiled regex. This is more verbose than JavaScript's `/\d/` literal syntax — a trade-off of using string-based construction.

```lisp
(bind digits (regex "\\d+" "g"))   ;; → /\d+/g
(bind word (regex "\\w+"))          ;; → /\w+/
```

### Dynamic Patterns

For patterns built from variables, use `new RegExp`:

```lisp
(bind dynamic (new RegExp (template "^" prefix "\\d+") "gi"))
```

Use `regex` for static patterns (known at write time, visible, lintable). Use `new RegExp` for patterns computed at runtime.

### Tagged Templates for Composition

For complex regex built from fragments, tagged templates (Ch 11) enable composition without string concatenation.
