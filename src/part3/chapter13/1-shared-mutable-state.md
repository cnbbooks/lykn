## The Problem with Shared Mutable State

JavaScript allows any code to mutate any object it has a reference to. This is both its greatest flexibility and its most prolific source of bugs.

### Three Ways It Goes Wrong

```javascript
// 1. Functions can silently modify their arguments
const user = { name: "Duncan", age: 42 };
doSomething(user);
// Did doSomething change user.name? You have to read doSomething to know.

// 2. Closures can mutate shared variables
let count = 0;
setInterval(() => count++, 1000);
// count is changing in the background. Any code can read stale values.

// 3. const doesn't prevent mutation
const items = [1, 2, 3];
items.push(4);  // No error! const prevents reassignment, not mutation.
```

### Three Strategies

The Deep JavaScript research identifies three strategies for dealing with shared mutable state:

1. **Defensive copying** — copy data before sharing it, so changes to the copy don't affect the original
2. **Immutability** — make data unchangeable, so nobody can modify it
3. **Controlled mutation** — mutate through a single, explicit path, so all changes are visible and auditable

Surface Lykn uses all three. `bind` makes bindings immutable (strategy 2). `assoc`, `dissoc`, and `conj` produce new values via copy (strategy 1). And `cell` provides a single, explicit mutation path (strategy 3).

This chapter teaches all three.
