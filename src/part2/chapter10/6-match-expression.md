## `match` Is an Expression

Unlike `switch` and `if`/`else`, `match` can appear in value position:

```lisp
(bind message
  (match status
    (200 "ok")
    (404 "not found")
    (_ "unknown")))
```

```javascript
const message = (() => {
  const target__gensym0 = status;
  if (target__gensym0 === 200) {
    return "ok";
  }
  if (target__gensym0 === 404) {
    return "not found";
  }
  {
    return "unknown";
  }
})();
```

### How It Works

The compiler wraps the match in an IIFE (Immediately Invoked Function Expression) when it appears in value position. Each clause body gets a `return` instead of falling through. The IIFE evaluates immediately and produces the matched value.

### Three Contexts, Three Strategies

The compiler picks the most efficient codegen strategy based on where `match` appears:

- **Statement position**: plain if-chain, no IIFE
- **Value position**: IIFE with returns (as shown above)
- **Tail position** (last expression in a `func` with `:returns`): if-chain with `return`, no IIFE — the enclosing function provides the return context

The reader doesn't need to think about which strategy the compiler picks. Write `match` anywhere an expression goes, and the compiler handles the rest.

### Why This Matters

JavaScript has no expression-level multi-way dispatch. The ternary operator handles two branches; beyond that, you need `if`/`else` statements assigned to a variable. `match` in value position — `(bind x (match ...))` — is genuinely new to most JavaScript developers, and once they have it, the `if`/`else`-plus-`let` pattern feels like a workaround.
