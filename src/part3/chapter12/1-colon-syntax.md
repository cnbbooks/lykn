## Colon Syntax: `obj:prop`

Lykn's most distinctive syntactic feature. Where JavaScript writes dots, Lykn writes colons.

### The Basics

```lisp
console:log                    ;; → console.log
document:body                  ;; → document.body
Math:PI                        ;; → Math.PI
```

```javascript
console.log;
document.body;
Math.PI;
```

Method calls work the same way — the colon-separated atom is the function, the arguments follow:

```lisp
(console:log "hello")          ;; → console.log("hello")
(Array:is-array items)         ;; → Array.isArray(items)
(JSON:parse text)              ;; → JSON.parse(text)
```

```javascript
console.log("hello");
Array.isArray(items);
JSON.parse(text);
```

### Chained Access

Colons chain for nested property access:

```lisp
document:body:style:color      ;; → document.body.style.color
response:data:users:length     ;; → response.data.users.length
```

```javascript
document.body.style.color;
response.data.users.length;
```

Each colon becomes a dot. The compiler splits the atom on `:` and generates a chain of `MemberExpression` nodes.

### camelCase in Action

Each segment of a colon-separated atom gets independent camelCase conversion:

```lisp
document:get-element-by-id     ;; → document.getElementById
my-obj:some-method             ;; → myObj.someMethod
local-storage:get-item         ;; → localStorage.getItem
```

```javascript
document.getElementById;
myObj.someMethod;
localStorage.getItem;
```

This is where camelCase conversion (Ch 3) really shines. You write `document:get-element-by-id` — lisp-case, readable, no abbreviations — and the output is `document.getElementById` — idiomatic JavaScript. Both sides are natural in their own world.

### How It Works

The reader (the parser) sees `console:log` as a single atom — it doesn't split it. The *compiler* handles the splitting: it finds the colons, generates a `MemberExpression` chain, and applies camelCase conversion to each segment. This means macros and the reader can manipulate `console:log` as one token without worrying about its internal structure.

### The Heritage

Common Lisp uses `:` for `package:symbol` — accessing a symbol from a specific package. ZetaLisp (the Lisp Machine dialect) used the same convention. Lykn adapts it for `object:property`, which is semantically similar: you're accessing something inside a namespace.

The dot was available — DD-01 considered a `(. obj prop)` form (inherited from eslisp). It was rejected because: one syntax is better than two, the dot character as a form head is visually noisy in Lisp code, and colon syntax enables camelCase conversion to happen at the same point as member access splitting. The colon does two jobs at once and does both well.
