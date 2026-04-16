## "It's Just a Model"

King Arthur approaches an object. He accesses a property.

```lisp
proxy:name    ;; → "Arthur"
```

Looks normal. Patsy whispers: "It's just a Proxy."

"Shh!"

The property access passes through a `get` trap, logs the access, and returns the value. Arthur is none the wiser. The illusion is seamless.

"What a fine object."

"It's intercepting everything you do."

"I *said* shh!"
