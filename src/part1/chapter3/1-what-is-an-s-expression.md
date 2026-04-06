## What Is an S-Expression?

An s-expression is either an **atom** or a **list** of s-expressions wrapped in parentheses. That is the entire syntax. There is nothing else to learn, in much the same way that there is nothing else to chess once you know how the pieces move — the complexity is emergent, not specified.

### Atoms

An atom is anything that isn't a list. Numbers are atoms. Strings are atoms. Symbols — the names you give things — are atoms.

```lisp
42                          ;; a number
"hello"                     ;; a string
console:log                 ;; a symbol
+                           ;; also a symbol
true                        ;; also a symbol
```

### Lists

A list is a pair of parentheses containing zero or more s-expressions:

```lisp
(+ 1 2)                     ;; a list of three atoms
(bind x 42)                 ;; a list of three things
(bind x (+ 1 2))            ;; a list containing a list
(console:log "hello")       ;; a list of two atoms
()                          ;; an empty list
```

### What JavaScript Needs That Lykn Doesn't

Consider a JavaScript declaration:

```javascript
const x = 1 + 2;
```

To parse this, JavaScript needs: the keyword `const`, the assignment operator `=`, the arithmetic operator `+`, operator precedence rules (does `+` bind tighter than `=`?), and a semicolon. Five different syntactic mechanisms.

In Lykn:

```lisp
(bind x (+ 1 2))
```

The parentheses are the only syntactic mechanism. They tell you what's grouped with what. `bind` is the first element of the outer list — the operator. `x` is the second element — the name. `(+ 1 2)` is the third element — the value, which is itself a list where `+` is the operator and `1` and `2` are the arguments.

### Parentheses Replace Precedence

In JavaScript, you need to know that `*` binds tighter than `+`:

```javascript
1 + 2 * 3    // → 7, not 9
```

In Lykn, you write the tree you mean:

```lisp
(+ 1 (* 2 3))              ;; → 7
(* (+ 1 2) 3)              ;; → 9
```

There is no ambiguity. There are no precedence tables. The structure is right there in the text, visible and explicit. You trade a few extra keystrokes for the elimination of an entire category of bugs — the kind where the code does something different from what you thought it did because you misremembered which operator binds tighter.

### Code Is Data

One more thing, and then we'll move on. An s-expression is simultaneously a program and a data structure. `(+ 1 2)` is both "add one and two" and "a list of three things." This dual nature is what makes macros possible — a macro receives code as a list, transforms the list, and returns a new list that becomes code. But macros are a later chapter. For now, hold this thought: the reason the syntax is so simple is that it needs to be simple enough for *programs* to read and write, not just humans.
