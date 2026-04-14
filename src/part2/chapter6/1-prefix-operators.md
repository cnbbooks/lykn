## Prefix Notation for Operators

Chapter 3 introduced the idea. This chapter makes it real: every operator in Lykn is prefix. The operator comes first, the operands follow, and the parentheses tell you what groups with what.

### The Core Pattern

```lisp
(+ 1 2)              ;; → 1 + 2
(* 4 5)              ;; → 4 * 5
(< a b)              ;; → a < b
(and x y)            ;; → x && y
(not active)         ;; → !active
```

One rule. No exceptions. The first element is the operator; everything else is an operand.

### Precedence Is Explicit

In JavaScript, you need to know the precedence table to parse this:

```javascript
a + b * c ** d
```

Does `**` bind tighter than `*`? (Yes.) Does `*` bind tighter than `+`? (Yes.) Is `**` right-to-left associative? (Also yes.) The expression means `a + (b * (c ** d))`, but you need a reference table to be sure.

In Lykn, you write what you mean:

```lisp
(+ a (* b (** c d)))
```

The nesting *is* the precedence. No table required. The compiler generates clean JavaScript with the appropriate parentheses inserted:

```javascript
a + b * c ** d;
```

The JS output uses standard infix notation and relies on precedence — because JS developers reading the output expect it. But the Lykn source is unambiguous regardless of whether you've memorized the table.

### Variadic Operators

Prefix notation makes variadic operators natural. Several Lykn operators accept more than two arguments:

```lisp
(+ 1 2 3 4 5)        ;; → 1 + 2 + 3 + 4 + 5
(* a b c)             ;; → a * b * c
(and x y z)           ;; → x && y && z
(or a b c d)          ;; → a || b || c || d
```

In JavaScript, you'd chain the operators manually. In Lykn, you just add operands to the list.
