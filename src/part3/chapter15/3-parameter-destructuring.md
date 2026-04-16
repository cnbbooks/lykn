## Destructuring in Function Parameters

JavaScript supports destructuring directly in function parameters — extracting properties from an argument inline. Lykn supports this in both kernel and surface function forms.

### Surface `func` with Destructuring

Surface `func` accepts destructuring patterns in `:args` position. A destructured parameter appears where a `:type name` pair would go, but as a list starting with `object` or `array`. Inside the pattern, fields follow the same `:type name` alternation — every field must be typed.

```lisp
(func process
  :args ((object :string name :number age) :string action)
  :returns :string
  :body (template name " (" age ") — " action))
```

```javascript
function process({name, age}, action) {
  if (typeof name !== "string")
    throw new TypeError("process: arg 'name' expected string, got " + typeof name);
  if (typeof age !== "number" || Number.isNaN(age))
    throw new TypeError("process: arg 'age' expected number, got " + typeof age);
  if (typeof action !== "string")
    throw new TypeError("process: arg 'action' expected string, got " + typeof action);
  return `${name} (${age}) — ${action}`;
}
```

Each field gets its own type check. The destructuring pattern (`{name, age}`) appears in the compiled parameter list, and the per-field assertions appear as body statements.

### Array Destructuring

```lisp
(func head-tail
  :args ((array :number first (rest :number remaining)))
  :body (console:log first remaining))
```

```javascript
function headTail([first, ...remaining]) {
  if (typeof first !== "number" || Number.isNaN(first))
    throw new TypeError("head-tail: arg 'first' expected number, got " + typeof first);
  console.log(first, remaining);
}
```

Array patterns support `_` for skipping positions and `(rest :type name)` for collecting remaining elements.

### `fn` with Destructuring

```lisp
(bind f (fn ((object :string name :number age))
  (console:log name age)))
```

```javascript
const f = ({name, age}) => {
  if (typeof name !== "string")
    throw new TypeError("anonymous: arg 'name' expected string, got " + typeof name);
  if (typeof age !== "number" || Number.isNaN(age))
    throw new TypeError("anonymous: arg 'age' expected number, got " + typeof age);
  console.log(name, age);
};
```

### Opting Out with `:any`

Use `:any` for fields that don't need type checking:

```lisp
(func f
  :args ((object :any name :number age))
  :body (console:log name age))
```

The `:any` field produces no type check — only `age` gets validated.

### Default Values in Destructured Parameters

Use `(default :type name value)` inside a destructuring pattern to provide fallback values:

```lisp
(func create-user
  :args ((object :string name
                 (default :number age 0)
                 (default :string role "viewer")))
  :returns :object
  :body (obj :name name :age age :role role))
```

```javascript
function createUser({name, age = 0, role = "viewer"}) {
  if (typeof name !== "string")
    throw new TypeError("createUser: arg 'name' expected string, got " + typeof name);
  if (typeof age !== "number" || Number.isNaN(age))
    throw new TypeError("createUser: arg 'age' expected number, got " + typeof age);
  if (typeof role !== "string")
    throw new TypeError("createUser: arg 'role' expected string, got " + typeof role);
  return {name, age, role};
}
```

Type checks fire on the final value — after JavaScript applies the default. Defaults also work in array destructuring:

```lisp
(func pad-triple
  :args ((array :number first
                (default :number second 0)
                (default :number third 0)))
  :body (+ first second third))
```

### Nested Destructuring

For object destructuring, use `alias` to name the intermediate binding and provide a nested pattern:

```lisp
(func process-order
  :args ((object :string id
                 (alias :any customer (object :string name :string email))
                 :number total))
  :returns :string
  :body (template name " (" email ") — $" total))
```

```javascript
function processOrder({id, customer: {name, email}, total}) {
  if (typeof id !== "string")
    throw new TypeError("processOrder: arg 'id' expected string, got " + typeof id);
  if (typeof name !== "string")
    throw new TypeError("processOrder: arg 'name' expected string, got " + typeof name);
  if (typeof email !== "string")
    throw new TypeError("processOrder: arg 'email' expected string, got " + typeof email);
  if (typeof total !== "number" || Number.isNaN(total))
    throw new TypeError("processOrder: arg 'total' expected number, got " + typeof total);
  return `${name} (${email}) — $${total}`;
}
```

The `alias` form names the property key (`customer`) and provides the nested pattern. Type checks target the leaf fields (`name`, `email`), not the intermediate object.

In array destructuring, nesting is positional — no `alias` needed:

```lisp
(func process-pair
  :args ((array (object :string name) :number score))
  :body (console:log name score))
```

```javascript
function processPair([{name}, score]) {
  if (typeof name !== "string")
    throw new TypeError("processPair: arg 'name' expected string, got " + typeof name);
  if (typeof score !== "number" || Number.isNaN(score))
    throw new TypeError("processPair: arg 'score' expected number, got " + typeof score);
  console.log(name, score);
}
```

### Kernel Functions with Destructuring

Kernel `function` forms also support destructuring, without the type annotation requirement:

```lisp
(function create-user ((object name age email))
  (return (obj :name name :age age :email email :active true)))
```

```javascript
function createUser({name, age, email}) {
  return {name, age, email, active: true};
}
```

### The Body Alternative

You can also destructure in the body instead:

```lisp
(func create-user
  :args (:object opts)
  :returns :object
  :body
  (bind (object name age email) opts)
  (obj :name name :age age :email email :active true))
```

This receives the whole object as a typed `:object` parameter (with a runtime type check), then destructures it on the next line. Both approaches are valid — surface parameter destructuring is more concise, body destructuring gives you a name for the whole object.
