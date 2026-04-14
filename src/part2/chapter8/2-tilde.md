## The `~` Placeholder

`~` is Lykn's placeholder sigil. In `:post` clauses, it refers to the function's return value — the value that `:body` produced.

### Usage

```lisp
;; Return value must be positive
:post (> ~ 0)

;; Return value must have a valid property
:post (> (get ~ :balance) 0)

;; Composed conditions on the return value
:post (and (not (= ~ null)) (> (get ~ :length) 0))
```

The name comes from format-string conventions in Common Lisp and Erlang, where `~` means "something goes here." In Lykn, what goes here is the return value.

### Constraints

`~` is only valid in `:post`. Using it in `:pre` is a compile error — the return value doesn't exist before the function has run.

`:post` requires `:returns`. A function without `:returns` is void — it has no return value, so `~` would refer to nothing. Writing `:post` on a void function is a compile error.
