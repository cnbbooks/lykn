# Lambda: The Ultimate GOTO

In 1977, Guy Steele published a paper called *Lambda: The Ultimate GOTO*. The title was a provocation. At the time, the programming world was consumed by Dijkstra's crusade against GOTO — the idea that unstructured jumps made programs incomprehensible. Steele's response was not to defend GOTO or to ban it, but to make it irrelevant:

> A GOTO is simply a procedure call with no arguments and no returned value.

The dangerous, low-level, "considered harmful" thing was just a degenerate special case of the safe, high-level thing. Lambda was not built on top of GOTO. GOTO was a crippled lambda all along.

Steele showed that if a compiler treats procedure calls in tail position as jumps — not pushing a stack frame, not saving a return address, just *jumping* — then every GOTO pattern (loops, early exits, multi-way branches) is expressible as a procedure call with zero overhead. The expensive abstraction was only expensive because compilers were lazy.

---

You have spent this book inside s-expressions. You have written `func` and `fn` and `lambda`. You have bound values with `bind`, matched patterns with `match`, threaded pipelines with `->`. Every surface form compiled to kernel forms, which compiled to JavaScript you could read and understand.

All of it was lambda.

The typed functions? Lambda with contracts. The generators? Lambda with suspension. The destructured parameters? Lambda with pattern matching. The macros? Lambda at compile time. The threading macros? Lambda composition, unrolled.

And now, for the first time in this book, we define GOTO:

```lisp
;; Lambda: The Ultimate GOTO
(macro goto (target)
  `(,target))
```

One line. A macro that takes a target and calls it. A GOTO is a function call. It always was.

And so:

```lisp
(bind chapter-0 (fn ()
  (console:log "Chapter 0: Opening Night")
  (console:log "You have returned to the beginning.")
  (console:log "The parrot is not dead. It is resting.")))

(goto chapter-0)
```

```javascript
const chapter0 = () => {
  console.log("Chapter 0: Opening Night");
  console.log("You have returned to the beginning.");
  console.log("The parrot is not dead. It is resting.");
};
chapter0();
```

You have reached the end. Which is the beginning. Which is a function call.

`(goto chapter-0)`

Happy hacking.
