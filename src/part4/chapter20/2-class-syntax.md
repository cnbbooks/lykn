## Class Syntax in Lykn

The kernel `class` form (DD-07):

```lisp
(class Dog (Animal)
  (constructor (name breed)
    (super name)
    (assign this:breed breed))

  (speak ()
    (return (template this:name " barks")))

  (describe ()
    (return (template this:name " is a " this:breed))))
```

```javascript
class Dog extends Animal {
  constructor(name, breed) {
    super(name);
    this.breed = breed;
  }
  speak() {
    return `${this.name} barks`;
  }
  describe() {
    return `${this.name} is a ${this.breed}`;
  }
}
```

### The Syntax

**`(class Name (Parent) ...body)`** — class declaration. The second element is the parent class; empty parens `()` for no parent.

**Methods are bare lists** — `(method-name (params) body)`. No `func` keyword. Methods use kernel function syntax — `this` is available, explicit `return` required, no type annotations.

**`constructor`** is a regular method name. No special form — just a method the JS engine recognizes.

**`this` is available** inside class bodies because this is kernel territory. `this:name` compiles to `this.name`.

**`super`** for parent calls — `(super args)` in the constructor, `(super:method args)` for parent method calls.

**camelCase applies** — `to-string` → `toString`, `get-balance` → `getBalance`.
