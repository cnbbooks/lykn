## Symbols and Lykn Keywords

Lykn keywords (`:name`, `:age`) compile to strings. Symbols are a different mechanism for property keys — guaranteed unique, not enumerable, not serializable.

### When to Use Which

**Keywords** (`:name` → `"name"`): normal property access, `obj` construction, `match` patterns, JSON-serializable data. This is the default for virtually all Lykn code.

**Symbols**: collision-free extension of objects you don't own, implementing protocols (`Symbol:iterator`), hiding implementation details from casual enumeration.

Most Lykn code uses keywords exclusively. Symbols appear in interop (implementing `Symbol:iterator` for custom iterable types) and in advanced patterns (metadata keys, framework extension points). If you're not implementing a protocol or extending foreign objects, you don't need symbols.
