## Zero-Arg Shorthand

When a function takes no arguments, `func` uses a compact positional form:

```lisp
(func get-timestamp (Date:now))
(func get-pi (3.14159))
(func create-user-id ((crypto:random-UUID)))
```

```javascript
function getTimestamp() {
  return Date.now();
}

function getPi() {
  return 3.14159;
}

function createUserId() {
  return crypto.randomUUID();
}
```

The parenthesized body expression is both the body and the implicit return value. No `:args`, no `:returns`, no `:body` — just the function name and a single expression in parentheses.

This is syntactic sugar for the common pattern of a named function that computes and returns a value with no inputs. You'll encounter it throughout the book for simple accessor and factory functions.
