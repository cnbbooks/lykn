## `this` and `super`

Surface Lykn has no `this` — Chapter 7 covered the rationale. But `this` and `super` exist in kernel code, and the reader needs to recognize them for JS interop.

### `this` in Kernel Code

Inside a `class` body (which uses kernel syntax), `this` accesses instance properties via colon syntax:

```lisp
(class Dog ()
  (constructor (name)
    (= this:name name))

  (speak ()
    (console:log (template this:name " barks"))))

(bind d (new Dog "Rex"))
(d:speak)
```

```javascript
class Dog {
  constructor(name) {
    this.name = name;
  }
  speak() {
    console.log(`${this.name} barks`);
  }
}
const d = new Dog("Rex");
d.speak();
```

`this:name` compiles to `this.name`. The colon syntax works the same way here as everywhere else — `:` becomes `.`.

### `super` in Kernel Code

For class inheritance, `super` calls the parent constructor or parent methods:

```lisp
(class Puppy (Dog)
  (constructor (name)
    (super name))

  (speak ()
    (super:speak)
    (console:log "...and wags tail")))
```

`(super name)` compiles to `super(name)`. `(super:speak)` compiles to `super.speak()`.

### In Surface Code

If you need `this` for JS interop — calling a library that expects method-style invocation, working with a framework — use kernel passthrough (write the class in kernel forms) or `js:bind`. Chapter 14 (JS Interop) covers the full story.

In surface Lykn, the patterns that need `this` in JavaScript are handled with closures and explicit parameters. An object with methods that close over shared state is more explicit, more composable, and immune to binding confusion.
