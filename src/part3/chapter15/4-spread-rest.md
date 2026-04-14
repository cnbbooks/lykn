## `spread` and `rest`

JavaScript uses `...` for both spreading (constructing) and rest (collecting). Lykn separates them into two distinct forms.

### `spread` — Expression Context

For constructing new values from existing ones:

```lisp
;; Spread in arrays
(bind combined (array 0 (spread arr) 4))
```

```javascript
const combined = [0, ...arr, 4];
```

```lisp
;; Spread in object literals
(bind merged (object (spread defaults) (name "override")))
```

```javascript
const merged = {...defaults, name: "override"};
```

```lisp
;; Spread in function calls
(console:log (spread args))
```

```javascript
console.log(...args);
```

### `rest` — Pattern Context

For collecting remaining elements:

```lisp
;; Rest in array patterns
(bind (array first (rest others)) items)
```

```javascript
const [first, ...others] = items;
```

```lisp
;; Rest in object patterns
(bind (object name (rest extras)) user)
```

```javascript
const {name, ...extras} = user;
```

### The Enforced Split

Lykn enforces the distinction at compile time:

```lisp
;; COMPILE ERROR: spread in pattern position
(bind (array (spread x)) items)

;; COMPILE ERROR: rest in expression position
(array 1 (rest x) 4)
```

JavaScript uses `...` for both and relies on syntactic position to determine the meaning. Lykn gives them different names, making the intent unambiguous in source code. It's a small thing — but in code review, knowing whether `...` is constructing or collecting matters.
