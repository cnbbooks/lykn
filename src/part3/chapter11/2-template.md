## The `template` Form

Lykn's approach to string interpolation. This is the chapter's centerpiece.

### The Basics

```lisp
(template "Hello, " name "!")
```

```javascript
`Hello, ${name}!`
```

The `template` form uses type-based dispatch: string arguments become literal parts of the template, everything else becomes an interpolated expression. The compiler infers the boundaries — you just list the parts in order.

### More Examples

```lisp
;; Multiple interpolations
(template "Name: " user-name ", Age: " age)

;; Expressions as interpolations
(template "Total: $" (* price quantity))

;; Multi-part with newlines
(template "Dear " name ",\n"
          "Your order of " quantity " items "
          "totals $" total ".")
```

```javascript
`Name: ${userName}, Age: ${age}`
`Total: $${price * quantity}`
`Dear ${name},\nYour order of ${quantity} items totals $${total}.`
```

### How It Works

The compiler walks the `template` arguments left to right. String literals become `TemplateElement` nodes in the ESTree AST — the fixed text between interpolations. Everything else becomes an expression node — the `${}` parts. The boundary between literal and expression is inferred from the argument type: string literal → text, anything else → interpolation.

This is why `(template "Total: $" (* price quantity))` works: `"Total: $"` is a string literal (text), `(* price quantity)` is an expression (interpolation). The compiler doesn't need special delimiters — the types tell it everything.

### Why Not Backticks?

Lykn's reader (the parser) reserves backticks for quasiquote — the macro system's template mechanism (DD-10). JavaScript's backtick template literals and Lisp's quasiquote both use the `` ` `` character, and the reader can only interpret it one way. The macro system won.

The `template` form fills the gap. It provides the same functionality — string interpolation with embedded expressions — through an s-expression. The syntax is consistent with everything else in Lykn: a list, an operator, and its arguments.
