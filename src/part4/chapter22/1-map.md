## Map

A Map is a key-value store where keys can be *any* type — objects, functions, numbers, not just strings. This is the killer feature that plain objects can't match.

### Creation and Basic Operations

```lisp
(bind users (new Map))
(users:set "alice" (obj :name "Alice" :age 30))
(users:set "bob" (obj :name "Bob" :age 25))

(users:get "alice")          ;; → { name: "Alice", age: 30 }
(users:has "carol")          ;; → false
(users:delete "bob")         ;; → true
users:size                   ;; → 1
```

```javascript
const users = new Map();
users.set("alice", {name: "Alice", age: 30});
users.set("bob", {name: "Bob", age: 25});
users.get("alice");
users.has("carol");
users.delete("bob");
users.size;
```

### Creating from Entries

```lisp
(bind config (new Map #a(
  #a("host" "localhost")
  #a("port" 5432)
  #a("ssl" true))))
```

### Non-String Keys

The feature that justifies Map's existence:

```lisp
(bind metadata (new Map))
(bind el (document:get-element-by-id "app"))
(metadata:set el (obj :created (Date:now) :version 1))

;; Look up by the same object reference
(metadata:get el)  ;; → { created: ..., version: 1 }
```

Objects, functions, DOM elements, anything — Maps accept them as keys. Plain objects coerce all keys to strings.

### Iteration

Maps are iterable and preserve insertion order:

```lisp
(for-of (array key val) config
  (console:log key val))

(for-of key (config:keys) (console:log key))
(for-of val (config:values) (console:log val))
```

### Map vs `obj`

| Feature | `obj` | `Map` |
|---|---|---|
| Key types | Strings/symbols only | Any type |
| Insertion order | ES2015+ (spec-guaranteed) | Guaranteed |
| Size | `(Object:keys o):length` | `.size` |
| Iteration | `Object:entries` | Direct `for-of` |
| Prototype pollution | Possible | Not possible |
| Serialization | `JSON:stringify` | Manual |
| Pattern matching | `match` with `obj` patterns | Not directly |
| Immutable updates | `assoc`/`dissoc` | Copy + mutate |

**Use Map**: dynamic key-value lookups, non-string keys, counting, grouping, anything where `.size` and direct iteration matter. **Use `obj`**: static shapes, JSON-serializable data, `match` patterns, `assoc`/`dissoc` updates.

### `Map:group-by` (ES2024)

```lisp
(bind grouped (Map:group-by users (fn (:any u) u:role)))
;; Map { "admin" => [...], "viewer" => [...] }
```

Groups iterable elements by a classifier function. Returns a Map where each key is a group and each value is an array of matching elements.
