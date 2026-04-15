## `obj`: The Surface Form

The surface form for object construction. Keywords become property names, values follow each keyword.

### The Basics

```lisp
(bind user (obj
  :name "Duncan"
  :age 42
  :active true))
```

```javascript
const user = {name: "Duncan", age: 42, active: true};
```

### How It Works

**Keywords → string property names**: `:name` compiles to `"name"`. camelCase conversion applies: `:first-name` → `"firstName"`.

**Keyword-value alternation**: keyword, value, keyword, value. No commas in the source. No colons (in lykn — the JS output has them). No braces.

**Expressions as values**: any expression can be a value:

```lisp
(bind receipt (obj
  :total (* price quantity)
  :tax (* price quantity tax-rate)
  :timestamp (Date:now)))
```

**Nested objects**:

```lisp
(bind user (obj
  :name "Duncan"
  :address (obj :city "London" :zip "W1")))
```

### `obj` vs Kernel `object`

The kernel form uses grouped pairs:

```lisp
;; Kernel: grouped (key value) pairs
(object (name "Duncan") (age 42))

;; Surface: keyword-value alternation
(obj :name "Duncan" :age 42)
```

Both compile to `{name: "Duncan", age: 42}`. Use `obj` in surface code — keywords are self-documenting and get camelCase conversion. Use `object` in kernel passthrough contexts (class bodies) or when you need computed keys in key position.
