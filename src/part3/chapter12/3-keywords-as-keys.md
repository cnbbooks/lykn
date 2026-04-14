## Keywords as Property Names

Keywords connect three features in Lykn — and this chapter is where the connection becomes visible.

### One Concept, Four Roles

Keywords (`:name`, `:age`, `:first-name`) compile to string literals (`"name"`, `"age"`, `"firstName"`). They appear in:

**Object construction** (Ch 18):
```lisp
(obj :name "Duncan" :age 42)
;; → {name: "Duncan", age: 42}
```

**Property access**:
```lisp
(get user :name)
;; → user["name"]
```

**Type annotations** (Ch 5):
```lisp
(func greet :args (:string name) ...)
```

**Match patterns** (Ch 10):
```lisp
(match response
  ((obj :ok true :data d) (process d))
  ...)
```

### camelCase Applies

`:first-name` compiles to `"firstName"`. The conversion is consistent everywhere keywords appear: `(obj :first-name "Duncan")` produces `{firstName: "Duncan"}`, and `(get user :first-name)` produces `user["firstName"]`.

### The Syntactic Glue

Keywords are Lykn's syntactic glue for property names. You use the same `:name` keyword when constructing an object, accessing a property, matching on structure, and labelling function clauses. One concept, one syntax, used everywhere. This is the kind of internal consistency that makes a language feel coherent rather than assembled.
