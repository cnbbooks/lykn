## Dennis Returns

Dennis is back, and he's been mutated.

"Come and see the violence inherent in the system!" He holds up a JavaScript variable. It's been reassigned from three different modules. A callback has closed over it and incremented it in a `setInterval`. Something in the event loop has set it to `NaN`.

"Help! Help! I'm being mutated!"

A Lykn developer walks over and shows him a `cell`.

```lisp
(bind counter (cell 0))
(swap! counter (fn (:number n) (+ n 1)))
```

Dennis stares at it. The `!` in `swap!` catches his eye.

"It says `!`," he says. "It's *announcing* that it mutates."

"Yes."

"And you can only update it through a function."

"Yes."

"And the binding itself is `const` — you can't replace the whole cell."

"Yes."

Dennis considers this for a long moment.

"That's... actually rather civilized," he says. He goes back to his mud, occasionally calling `(swap! mud-pile add-mud)`.
