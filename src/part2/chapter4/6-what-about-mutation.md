## What About Mutation?

You are, at this point, entirely within your rights to ask: "If everything is immutable, how do I do anything stateful?"

### The Short Answer

The tools exist. They're in Chapter 13.

- **For state that changes over time**: use `cell` — a controlled, explicit mutable container with `swap!` and `reset!`
- **For "updating" objects and arrays**: use `assoc`, `dissoc`, and `conj` — surface macros that produce new values via shallow copy instead of mutating the original
- **For JS interop with mutable APIs**: use the `js:` namespace, which provides access to kernel forms like `let` and direct property assignment

### Why Not Here?

`bind` and `cell` are separated into different chapters because they're different concepts. `bind` is about naming values. `cell` is about managing state. Conflating them — as JavaScript does by making `let` both a naming mechanism and a state mechanism — is precisely the source of the bugs that motivated Lykn's design.

When you reach Chapter 13, you'll find that cells are simple, explicit, and hard to misuse. The `!` suffix on every mutating operation (`swap!`, `reset!`) makes state changes visible at a glance. But the important thing for now is: immutability is the *default*, not the *only option*. The vast majority of bindings in a typical program never need to change, and `bind` handles all of them.

### A Promise

If at any point in the next eight chapters you find yourself thinking "but I need a mutable variable for this," make a note and keep reading. By Chapter 13, you'll either have found a functional alternative that's cleaner, or you'll learn the `cell` pattern that handles the case explicitly. Either way, the language has you covered.
