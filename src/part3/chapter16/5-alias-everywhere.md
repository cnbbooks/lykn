## `alias` Across the Language

The reader has now seen `alias` in three contexts:

**Destructuring** (Ch 15) — rename a binding in a pattern:
```lisp
(bind (object (alias name full-name)) person)
```

**Import** (this chapter) — rename an imported binding:
```lisp
(import "./utils.js" ((alias add my-add)))
```

**Nested destructured params** (Ch 15) — name the intermediate binding in a nested pattern:
```lisp
(func f :args ((object (alias :any addr (object :string city)))) :body city)
```

One form, multiple uses. `alias` is the universal rename operation in Lykn — wherever you need to say "this thing has one name there, but I want to call it something else here," `alias` is the tool.

This consistency isn't accidental. It traces back to the `as` universal pattern form (DD-11), which emerged during the macro system design and was applied backward across the language. The principle: if two features need renaming, they should use the same form.
