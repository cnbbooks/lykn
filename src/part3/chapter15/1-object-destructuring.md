## Object Destructuring

Taking properties out of an object and binding them to names. The most common destructuring pattern.

### The Basics

```lisp
(bind person (obj :name "Duncan" :age 42))
(bind (object name age) person)
(console:log name age)
```

```javascript
const person = {name: "Duncan", age: 42};
const {name, age} = person;
console.log(name, age);
```

The `(object name age)` pattern extracts properties matching the names `name` and `age` from `person`. Each extracted property becomes an immutable `const` binding.

### Renaming with `alias`

When the property name and the binding name need to differ:

```lisp
(bind (object (alias name full-name)) person)
```

```javascript
const {name: fullName} = person;
```

`alias` renames: `name` is the property key in the object, `full-name` is the local binding name. camelCase conversion applies to the binding: `full-name` → `fullName`.

### Default Values

```lisp
(bind (object (default age 0) name) person)
```

```javascript
const {age = 0, name} = person;
```

If `person.age` is `undefined`, the default `0` is used. Note: `null` does NOT trigger defaults in JavaScript — only `undefined`. A property that exists with value `null` stays `null`.

### Nested Destructuring

```lisp
(bind (object (alias address (object city zip))) person)
```

```javascript
const {address: {city, zip}} = person;
```

The outer `alias` reaches into `person.address`; the inner `(object city zip)` extracts `city` and `zip` from the address object. Nesting can go as deep as the data structure requires.

### The Constructor-Destructor Principle

Notice the symmetry: `(object (name "Duncan") (age 42))` constructs an object in kernel syntax. `(object name age)` in pattern position destructures one. Same form, opposite direction. This is the constructor-as-destructor principle from DD-06, and it's the same insight that makes `(Some v)` work as both a constructor and a `match` pattern in Chapter 10.
