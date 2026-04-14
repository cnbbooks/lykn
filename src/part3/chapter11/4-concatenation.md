## String Concatenation: The Old Way

Before template literals, JavaScript used `+` for concatenation. In Lykn, this still works:

```lisp
(bind greeting (+ "Hello, " name "!"))
```

```javascript
const greeting = "Hello, " + name + "!";
```

### Why `template` Is Better

Three reasons:

**No ambiguity with arithmetic.** `(+ "5" 3)` produces `"53"` — JavaScript's `+` is overloaded for both addition and concatenation. `(template "5" 3)` produces `` `5${3}` `` — the intent is unambiguous. The separated-operator philosophy from the hazard research: keep arithmetic and string building in different forms.

**Cleaner for multi-part strings.** `(+ "Hello, " name ", you have " count " items")` gets unwieldy. `(template "Hello, " name ", you have " count " items")` reads the same way but compiles to a template literal — the modern JavaScript idiom.

**The compiled output is idiomatic.** Template literals are what a JavaScript developer would write by hand. `+` concatenation is the pre-ES2015 pattern. The output should look contemporary.

### When `+` Is Fine

For simple two-part concatenation — `(+ prefix suffix)` — either form works. Use whichever reads better. The guidance isn't "never use `+` for strings" — it's "prefer `template` when you're building a string with mixed text and values."
