## Destructuring in Function Parameters

Destructuring works directly in function parameters. This is the "named parameters" pattern — the caller passes an object, the callee destructures it.

### Kernel Functions

```lisp
(function create-user ((object name age email))
  (return (obj :name name :age age :email email :active true)))
```

```javascript
function createUser({name, age, email}) {
  return {name, age, email, active: true};
}
```

### With Defaults

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

### A Note on `func`

Destructured parameters in kernel `function` forms work as shown above. In surface `func` with typed `:args`, destructuring interacts with the type annotation system — the parameter receives a type annotation on the whole object, and the individual fields are extracted inside the body. For complex parameter shapes, kernel `function` with destructuring is often more natural than `func` with `:args`.
