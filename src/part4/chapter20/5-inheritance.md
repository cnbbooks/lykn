## Inheritance

```lisp
(class Animal ()
  (constructor (name)
    (= this:name name))
  (speak ()
    (return (template this:name " makes a sound"))))

(class Dog (Animal)
  (constructor (name breed)
    (super name)
    (= this:breed breed))
  (speak ()
    (return (template this:name " barks"))))

(class Cat (Animal)
  (constructor (name)
    (super name))
  (speak ()
    (return (template this:name " meows"))))
```

```javascript
class Animal {
  constructor(name) { this.name = name; }
  speak() { return `${this.name} makes a sound`; }
}
class Dog extends Animal {
  constructor(name, breed) { super(name); this.breed = breed; }
  speak() { return `${this.name} barks`; }
}
class Cat extends Animal {
  constructor(name) { super(name); }
  speak() { return `${this.name} meows`; }
}
```

### The Mechanics

`(class Dog (Animal) ...)` — the second element is the parent class. The compiled output is `class Dog extends Animal`.

`(super name)` — calls the parent constructor. Required in derived class constructors before accessing `this`.

`(super:speak)` — calls a parent method by name.

### The Lykn Perspective

Inheritance creates coupling — changing the parent can break every child. Surface Lykn prefers composition: closures, `obj` with shared functions, `type`/`match` for polymorphism. Inheritance is appropriate for extending built-in classes (`Error`, `HTMLElement`) and for frameworks that expect class hierarchies. For your own domain logic, consider the alternatives.
