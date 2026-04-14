## Destructuring in Function Parameters

JavaScript supports destructuring directly in function parameters — extracting properties from an argument inline. In Lykn, this works in kernel function forms.

### Kernel Functions with Destructuring

```lisp
(function create-user ((object name age email))
  (return (obj :name name :age age :email email :active true)))
```

```javascript
function createUser({name, age, email}) {
  return {name, age, email, active: true};
}
```

```lisp
(function connect ((object host (default port 3000) (default ssl true)))
  (console:log (template "Connecting to " host ":" port)))

(connect (obj :host "localhost"))
```

```javascript
function connect({host, port = 3000, ssl = true}) {
  console.log(`Connecting to ${host}:${port}`);
}
connect({host: "localhost"});
```

### Why Not `func`?

Surface `func`'s `:args` list expects strictly alternating `:type name` pairs. A destructuring pattern where a name is expected is a compile error. This is a current limitation — `func` provides type checking on parameters, and the interaction between type annotations and destructuring patterns hasn't been implemented yet.

### The Surface Alternative

Destructure in the body instead:

```lisp
(func create-user
  :args (:object opts)
  :returns :object
  :body
  (bind (object name age email) opts)
  (obj :name name :age age :email email :active true))
```

The `func` receives the whole object as a typed `:object` parameter (with a runtime type check), then destructures it on the next line. You get the type checking on the parameter boundary and the destructuring in the body — two steps instead of one, but both safe.

This pattern — typed parameter + body destructuring — is the recommended approach until surface parameter destructuring lands.
