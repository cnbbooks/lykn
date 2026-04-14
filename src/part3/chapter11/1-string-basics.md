## String Basics

JavaScript strings are UTF-16 encoded, immutable sequences. You can't modify a character in place — you can only create new strings. In Lykn, string literals use double quotes:

```lisp
(bind greeting "Hello, World!")
(bind name "Duncan")
(bind empty "")
```

```javascript
const greeting = "Hello, World!";
const name = "Duncan";
const empty = "";
```

### Escape Sequences

The standard set: `\"` for a literal quote, `\\` for a backslash, `\n` for newline, `\t` for tab, `\u{1F600}` for Unicode code points.

### String Methods

String methods are called via colon syntax, with camelCase conversion:

```lisp
(bind len name:length)                ;; → name.length
(bind upper (name:to-upper-case))     ;; → name.toUpperCase()
(bind first (name:char-at 0))         ;; → name.charAt(0)
(bind has-d (name:includes "D"))      ;; → name.includes("D")
(bind sub (name:slice 0 3))           ;; → name.slice(0, 3)
```

```javascript
const len = name.length;
const upper = name.toUpperCase();
const first = name.charAt(0);
const hasD = name.includes("D");
const sub = name.slice(0, 3);
```

The camelCase conversion — `to-upper-case` → `toUpperCase`, `char-at` → `charAt` — makes method calls read naturally in both worlds. You write lisp-case; the output is idiomatic JavaScript.

JavaScript's string API is extensive: `.split()`, `.replace()`, `.match()`, `.trim()`, `.padStart()`, `.repeat()`, `.startsWith()`, `.endsWith()`, and more. All are accessible via colon syntax. This chapter covers the pattern; the full API is in the JavaScript references.

### String Comparison

Strings compare by UTF-16 code unit values with `(= a b)` → `===`. For ordering, `(< "a" "b")` is `true`, but be aware that `(< "Z" "a")` is also `true` — uppercase letters come before lowercase in Unicode. For locale-aware sorting, use `(a:locale-compare b)`.
