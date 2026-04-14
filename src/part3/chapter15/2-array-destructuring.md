## Array Destructuring

Taking elements out of arrays by position.

### The Basics

```lisp
(bind items #a(1 2 3 4 5))
(bind (array first second) items)
(console:log first second)
```

```javascript
const items = [1, 2, 3, 4, 5];
const [first, second] = items;
console.log(first, second);     // 1 2
```

### Skipping Elements with `_`

`_` skips a position without binding:

```lisp
(bind (array _ _ third) items)
```

```javascript
const [, , third] = items;      // third = 3
```

Note: `_` as a skip marker only works in array patterns. In object patterns, `_` is a regular binding name.

### Collecting Remaining Elements

```lisp
(bind (array head (rest tail)) items)
```

```javascript
const [head, ...tail] = items;  // head = 1, tail = [2, 3, 4, 5]
```

`rest` collects all remaining elements into an array. It must be the last element in the pattern.

### Swapping Variables

A classic destructuring trick — no temporary variable needed:

```lisp
(bind (array b a) (array a b))
```

```javascript
[b, a] = [a, b];
```
