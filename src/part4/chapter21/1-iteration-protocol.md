## The Iteration Protocol

JavaScript's iteration protocol is a contract between producers (iterables) and consumers (`for-of`, spread, destructuring). The reader has been consuming iterables since Chapter 9. This section explains the mechanism underneath.

### The Contract

**Iterable**: any object with a `Symbol:iterator` method that returns an iterator.

**Iterator**: any object with a `next` method that returns `{ value, done }`.

That's the entire protocol. When you write `(for-of item items ...)`, JavaScript calls `items[Symbol.iterator]()` to get an iterator, then calls `.next()` repeatedly until `done` is `true`.

### What's Iterable

Arrays, strings, Maps, Sets, `arguments`, NodeLists, typed arrays, and generators are all iterable by default. They implement `Symbol:iterator`.

### What's NOT Iterable

Plain objects. `(for-of x (obj :a 1))` is a runtime error. Objects don't have `Symbol:iterator`. To iterate an object's properties, use `Object:entries`:

```lisp
(for-of (array key val) (Object:entries user)
  (console:log key val))
```

### Why It Matters

The iteration protocol is why `for-of`, spread, destructuring, `Array:from`, and `Promise:all` all work on the same data structures. They all consume the same protocol. If your custom object implements `Symbol:iterator`, all of these features work on it automatically.
