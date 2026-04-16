## Parameters in Depth

### Surface Parameters: Typed Pairs

`func`'s `:args` list accepts strictly alternating type-name pairs: `:type name :type name`. This is by design — the surface language keeps parameter syntax simple and uniform.

```lisp
(func greet
  :args (:string name :number age)
  :returns :string
  :body (template name " is " age " years old"))
```

### Default Values

Use `default` in the parameter list to provide fallback values with type checking:

```lisp
(func greet
  :args (:string name (default :string greeting "Hello"))
  :returns :string
  :body (template greeting ", " name "!"))
```

```javascript
function greet(name, greeting = "Hello") {
  if (typeof name !== "string")
    throw new TypeError("greet: arg 'name' expected string, got " + typeof name);
  if (typeof greeting !== "string")
    throw new TypeError("greet: arg 'greeting' expected string, got " + typeof greeting);
  return `${greeting}, ${name}!`;
}
```

The type check fires on the final value — after JavaScript applies the default. So if the caller omits `greeting`, it defaults to `"Hello"`, and the `:string` check passes.

### Rest Parameters

Use `rest` to collect remaining arguments:

```lisp
(func log-all
  :args (:string level (rest :any messages))
  :body (console:log level messages))
```

```javascript
function logAll(level, ...messages) {
  if (typeof level !== "string")
    throw new TypeError("log-all: arg 'level' expected string, got " + typeof level);
  console.log(level, messages);
}
```

### Destructured Parameters

`func` and `fn` accept destructuring patterns — an `(object ...)` or `(array ...)` list in `:args` — with per-field type annotations. This lets you type each destructured field individually:

```lisp
(func connect
  :args ((object :string host :number port (default :boolean ssl true)))
  :body (open-connection host port ssl))

(connect (obj :host "localhost" :port 5432))
```

```javascript
function connect({host, port, ssl = true}) {
  if (typeof host !== "string")
    throw new TypeError("connect: arg 'host' expected string, got " + typeof host);
  if (typeof port !== "number" || Number.isNaN(port))
    throw new TypeError("connect: arg 'port' expected number, got " + typeof port);
  if (typeof ssl !== "boolean")
    throw new TypeError("connect: arg 'ssl' expected boolean, got " + typeof ssl);
  openConnection(host, port, ssl);
}
```

This is the idiomatic "named parameters" pattern — the caller passes `(obj :key value ...)` and the function destructures with typed fields. Full coverage in Chapter 15, including nested patterns and the interaction with multi-clause dispatch.
