## Dennis Returns

Carol yells, "Come and see the violence inherent in the system!" She holds up a JavaScript variable. It's been reassigned from three different modules. A callback has closed over it and incremented it in a `setInterval`. Something in the event loop has set it to `NaN`.

"Help! Help! It's being mutated!"

Alice lumbers over and shows her a `cell`.

```lisp
(bind counter (cell 0))
(swap! counter (fn (:number n) (+ n 1)))
```

Carol stares at it, mesmerised ... the `!` in `swap!` ensnaring her.

"It *announces* its mutation with a bang!"

"Oh, that's lovely ..."

"And you can only update it through a function."

"You what?"

"And the binding itself is `const` — you can't replace the whole cell."

"But ..."

Carol considers this for a long moment.

"That's ... actually rather civilized," she says, returning to her bit-farming.
