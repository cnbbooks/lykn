## `break` and `continue`

### Basic Usage

```lisp
(for-of item items
  (if (= item :stop)
    (break))
  (if (= item :skip)
    (continue))
  (process item))
```

```javascript
for (const item of items) {
  if (item === "stop") break;
  if (item === "skip") continue;
  process(item);
}
```

`break` exits the loop entirely. `continue` skips to the next iteration.

### Labelled Breaks

For breaking out of nested loops, use `label`:

```lisp
(label :outer
  (for-of row rows
    (for-of cell row
      (if (= cell target)
        (break :outer)))))
```

```javascript
outer:
for (const row of rows) {
  for (const cell of row) {
    if (cell === target) break outer;
  }
}
```

The label `:outer` compiles to a JavaScript label. `(break :outer)` breaks out of the labelled statement, not just the inner loop. This is a kernel form used as-is — rare in practice, but indispensable when you need it.
