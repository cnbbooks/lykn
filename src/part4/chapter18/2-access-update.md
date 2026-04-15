## Accessing and Updating Objects

The reader has seen these patterns across four earlier chapters. This section brings them together.

### Static Access: Colon Syntax (Ch 12)

```lisp
user:name                  ;; → user.name
user:address:city          ;; → user.address.city
```

### Dynamic Access: `get` (Ch 12)

```lisp
(get user key)             ;; → user[key]
(get user :name)           ;; → user["name"]
```

### Immutable Updates: `assoc` / `dissoc` (Ch 13)

```lisp
(bind updated (assoc user :age 43 :active true))
(bind trimmed (dissoc user :temp-id))
```

```javascript
const updated = {...user, age: 43, active: true};
const trimmed = (() => {
  const {tempId: ___gensym0, ...rest__gensym1} = user;
  return rest__gensym1;
})();
```

`assoc` uses spread — the original is unchanged. `dissoc` uses destructuring to extract and discard the key, returning the rest.

### Structural Matching (Ch 10)

```lisp
(match response
  ((obj :ok true :data d) (process d))
  ((obj :ok false :error e) (handle-error e))
  (_ (throw (new Error "unexpected response"))))
```

### The Convergence

Four features, four chapters, one data structure. Construction with `obj`, access with colons and `get`, updates with `assoc`/`dissoc`, pattern matching with structural `match`. The reader who has followed the book to this point already knows how to work with objects — this chapter adds the deeper mechanics.
