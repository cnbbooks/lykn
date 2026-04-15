## Classes in Lykn: The Honest Position

Surface Lykn has no `class` form. Classes are kernel forms available through passthrough (Ch 14). This was deliberate — classes bring `this`, and surface Lykn eliminates `this`.

### What Surface Lykn Uses Instead

| Need | OOP Approach | Lykn Approach |
|---|---|---|
| Encapsulation | Private fields | Closures (Ch 7) |
| Polymorphism | Inheritance + override | Multi-clause `func` (Ch 8) |
| Data modeling | Class + constructor | `type` + `match` (Ch 10) |
| State | Instance fields | `cell` containers (Ch 13) |
| Interface contract | Abstract class | Contracts `:pre`/`:post` (Ch 8) |

### When to Use Classes

- **JS interop** — a library expects class instances or extends a base class
- **Extending built-ins** — custom `Error` subclasses, `HTMLElement` for Web Components
- **Framework requirements** — some React patterns, some testing frameworks
- **Developer preference** — Lykn doesn't forbid classes, it just provides alternatives

The rest of this chapter teaches classes thoroughly — because you'll encounter them in every JavaScript library you use. But the recommendation stands: start with `type`/`match`. Reach for classes when interop requires it.
