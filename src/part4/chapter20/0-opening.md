## The Knights Who Say "class"

"We demand," announces the tallest Knight, "a CONSTRUCTOR!"

A developer offers a factory function:

```lisp
(func make-dog
  :args (:string name :string breed)
  :returns :object
  :body (obj :name name :breed breed :speak (fn () (template name " barks"))))
```

"No!" The Knights are not impressed. "A *real* constructor! With `new`! And `this`!"

"But we don't have `this` in the surface language."

"Then you must use... the KERNEL!"

The developer reluctantly writes:

```lisp
(class Dog ()
  (constructor (name breed)
    (assign this:name name)
    (assign this:breed breed))
  (speak ()
    (return (template this:name " barks"))))
```

The Knights are satisfied. The developer mutters something about closures being better. Nobody listens.
