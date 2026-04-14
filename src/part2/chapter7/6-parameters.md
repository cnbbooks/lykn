## Parameters in Depth

### Default Values

Use `default` in the parameter list to provide a fallback value:

```lisp
(func greet
  :args (:string name (default :string greeting "Hello"))
  :returns :string
  :body (template greeting ", " name "!"))

(greet "World")            ;; → "Hello, World!"
(greet "World" "Howdy")    ;; → "Howdy, World!"
```

```javascript
function greet(name, greeting = "Hello") {
  // ... type checks ...
  return `${greeting}, ${name}!`;
}
```

The `default` form wraps the parameter: `(default :type name value)`. The type annotation applies to the parameter when a value is provided; the default must be type-compatible.

### Rest Parameters

Use `rest` to collect remaining arguments into an array:

```lisp
(func log-with-level
  :args (:string level (rest :any messages))
  :body (console:log level messages))

(log-with-level "INFO" "server started" "port 3000")
```

```javascript
function logWithLevel(level, ...messages) {
  // ... type check on level ...
  console.log(level, messages);
}
```

The `rest` form wraps the final parameter: `(rest :type name)`. It collects all remaining arguments into an array. Only the last parameter can be a rest parameter.

### Destructuring

Parameters can be destructured — unpacking objects and arrays inline. This is covered in Chapter 15 (Destructuring). For now, know that it works and that it follows the same patterns as `bind` destructuring.
