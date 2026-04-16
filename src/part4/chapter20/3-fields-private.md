## Fields and Private Members

### Public Fields

```lisp
(class Counter ()
  (field count 0)

  (increment ()
    (+= this:count 1)
    (return this:count)))
```

```javascript
class Counter {
  count = 0;
  increment() {
    this.count += 1;
    return this.count;
  }
}
```

### Private Members: The `-` Prefix

Lykn uses a naming convention that the compiler enforces at the JS engine level. A leading `-` on a name compiles to `#_` — JavaScript's private field syntax:

```lisp
(class BankAccount ()
  (field -balance 0)

  (constructor (initial)
    (assign this:-balance initial))

  (deposit (amount)
    (+= this:-balance amount))

  (get balance ()
    (return this:-balance)))
```

```javascript
class BankAccount {
  #_balance = 0;
  constructor(initial) {
    this.#_balance = initial;
  }
  deposit(amount) {
    this.#_balance += amount;
  }
  get balance() {
    return this.#_balance;
  }
}
```

`-balance` → `#_balance`. The developer writes a naming convention; the compiler produces engine-enforced privacy. No new syntax required — the `-` prefix is the entire mechanism.

Private methods work the same way:

```lisp
(-validate (amount)
  (if (<= amount 0)
    (throw (new Error "Amount must be positive"))))
```

Compiles to `#_validate(amount) { ... }` — a private method, invisible outside the class.
