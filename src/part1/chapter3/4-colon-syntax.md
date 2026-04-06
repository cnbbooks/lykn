## Colon Syntax

Lykn uses colons where JavaScript uses dots:

```lisp
console:log                 ;; → console.log
document:body:style:color   ;; → document.body.style.color
Math:floor                  ;; → Math.floor
my-obj:some-method          ;; → myObj.someMethod
```

### What the Reader Sees

The reader treats `console:log` as a single atom. It does not split it, does not recognise it as member access, and does not know that `console` is an object. It simply stores the characters `console:log` as an atom node and moves on.

The *compiler* handles the splitting. When it encounters an atom containing colons, it generates a member access chain. This is important because it means the reader — and by extension, the macro system — can manipulate `console:log` as a single token without worrying about its internal structure.

### Why Colons?

The dot was already spoken for — in many Lisps, dots have special meaning in dotted pairs `(a . b)`. The colon has a long history in Lisp as a namespace separator: Common Lisp uses `package:symbol`, and LFE uses the same convention for Erlang module access. Lykn adopted it for JavaScript member access, which gives the syntax a natural Lisp feel while mapping cleanly to JavaScript's dot notation.

### Computed Access

For dynamic property access — where the property name is a variable rather than a literal — use `get`:

```lisp
(get obj key)               ;; → obj[key]
(get arr 0)                 ;; → arr[0]
(get data "some-key")       ;; → data["some-key"]
```

Colon syntax is for static, known-at-compile-time member access. `get` is for everything else. The full story of property access comes in a later chapter; for now, these two forms cover every case you'll encounter in the examples ahead.
