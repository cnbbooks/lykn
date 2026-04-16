## The IR: Markdown as `type` Variants

Start with the data. What does a parsed Markdown document look like in memory?

```lisp
(type Block
  (Heading :number level :string text)
  (Paragraph :string text)
  (CodeBlock :string language :string code)
  (ListBlock :array items)
  (Blockquote :string text)
  (Empty))
```

A document is a list of `Block` values. Each variant represents one structural element. Inline formatting — bold, italic, code, links — happens during rendering, not parsing.

This is the `type`-driven design from Chapter 10. The IR is a closed set of variants. `match` on a `Block` is exhaustive — the compiler tells you if you forgot a case. Add a `Table` variant later and every `match` in the codebase must handle it before the code compiles.

This is why Lykn has `type` and `match`. A real program has data with known shapes. Making those shapes explicit lets the compiler help.
