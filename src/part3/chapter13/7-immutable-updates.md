## Immutable Updates: `assoc`, `dissoc`, `conj`

Producing new values from existing ones. These macros expand to spread-based copies — no mutation, no runtime library.

### `assoc` — Add or Replace Properties

```lisp
(bind user (obj :name "Duncan" :age 42))
(bind updated (assoc user :age 43))
(bind extended (assoc user :age 43 :active true))
```

```javascript
const user = {name: "Duncan", age: 42};
const updated = {...user, age: 43};
const extended = {...user, age: 43, active: true};
```

`user` is unchanged. `updated` and `extended` are new objects.

### `dissoc` — Remove a Property

```lisp
(bind safe (dissoc user :password))
```

The original object is not modified. `safe` is a new object without the `:password` key.

### `conj` — Append to an Array

```lisp
(bind items #a(1 2 3))
(bind more (conj items 4))
```

```javascript
const items = [1, 2, 3];
const more = [...items, 4];
```

### Shallow Copy

`assoc` uses spread (`...`), which is a shallow copy. Nested objects are shared, not deep-cloned. For nested updates:

```lisp
(bind user (obj :name "Duncan" :address (obj :city "London")))
(bind moved (assoc user :address (assoc user:address :city "Paris")))
```

The outer `assoc` creates a new user. The inner `assoc` creates a new address. The original `user` and its original `:address` are both unchanged.

### Keywords as Property Names

`:age` compiles to `"age"`. camelCase conversion applies: `(assoc user :first-name "D")` produces `{...user, firstName: "D"}`. The same keywords used in `obj` construction and `get` access.
