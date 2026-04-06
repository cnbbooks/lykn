## The Five Node Types

The reader — the component that parses your `.lykn` source into a tree — produces five kinds of nodes. If you understand these five, you can read any Lykn program.

### 1. Atom

A symbol name. Anything that isn't a string, number, keyword, or list:

```lisp
bind                ;; a form name
console:log         ;; member access (colon syntax)
my-function         ;; lisp-case identifier (→ myFunction in JS)
+                   ;; operator
true                ;; boolean literal
null                ;; null literal
```

The reader doesn't know that `bind` is special. It doesn't know that `true` is a boolean or that `+` is an operator. They're all atoms — text tokens that the compiler will interpret later.

### 2. String

Quoted text, with standard escape sequences:

```lisp
"Hello, World!"
"He said \"hi\""
"line one\nline two"
```

Strings are the one node type that means the same thing in the reader and the compiler — a string is always a string.

### 3. Number

Numeric literals, including decimals and hex:

```lisp
42
3.14
0xFF
1_000_000           ;; numeric separators
```

The reader parses these into actual numbers, not strings. `42` becomes a number node with value `42`.

### 4. List

A parenthesized group of forms. This is where all structure lives:

```lisp
(bind x 42)
(func greet :args (:string name) :body (console:log name))
(+ 1 (* 2 3))
()
```

A list can contain any mix of atoms, strings, numbers, keywords, and other lists. Nesting is unlimited. The reader builds the tree; it doesn't evaluate it.

### 5. Keyword

A colon-prefixed atom. The reader treats these as a distinct node type:

```lisp
:name               ;; → "name" in JS
:first-name         ;; → "firstName" in JS (camelCase conversion)
:args               ;; used in func clause labels
:string             ;; used as a type annotation
```

Keywords are the newest of the five types — they were activated in the surface language design (DD-15) and upgraded from "reserved but inactive" to a full reader-level type. The reader strips the leading colon and stores the value. `:name` becomes a keyword node with value `"name"`.

### A Comparison to JSON

JSON has six types: string, number, boolean, null, array, and object. Lykn's reader has five: atom, string, number, list, and keyword.

Both are tree structures. Both are unambiguous — you can always determine the type of a node from its syntax. The difference is that Lykn's trees are *executable*: the first element of a list is, by convention, the operator. A JSON array `["bind", "x", 42]` is data. A Lykn list `(bind x 42)` is a program.

This convention — first element is the operator — is not enforced by the reader. The reader doesn't know about it. The compiler does. And that brings us to what the reader *doesn't* do, which is at least as important as what it does.
