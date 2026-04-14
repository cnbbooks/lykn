## Computed Access: `get`

When the property name isn't known at compile time, use `get`:

```lisp
(get obj key)                  ;; → obj[key]
(get arr 0)                    ;; → arr[0]
(get config :name)             ;; → config["name"]
(get data (template "env_" mode))  ;; → data[`env_${mode}`]
```

```javascript
obj[key];
arr[0];
config["name"];
data[`env_${mode}`];
```

### When to Use `get`

`get` compiles to bracket notation. Use it for:

- **Dynamic property names** — the key is a variable or expression
- **Numeric indices** — array element access
- **Keyword property access** — `(get obj :name)` produces `obj["name"]`, which is equivalent to `obj.name` in JavaScript
- **Symbol keys** — `(get obj (Symbol:for "id"))`

### The Contrast

`obj:name` is for when you know the property at write time. `(get obj key)` is for when it depends on a runtime value. Two forms, two use cases, no overlap.

```lisp
;; Static: you know the property name
user:name                      ;; → user.name

;; Dynamic: the key is a variable
(get user field)               ;; → user[field]

;; Keyword: static name, bracket notation
(get user :name)               ;; → user["name"]
```

The keyword form — `(get obj :name)` — is equivalent to `obj:name` in most cases. It appears in `match` patterns, `assoc`/`dissoc`, and other surface forms where the property name is syntactically a keyword argument.
