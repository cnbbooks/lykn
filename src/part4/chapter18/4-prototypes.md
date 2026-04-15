## The Prototype Chain

JavaScript objects have a hidden link to another object — their *prototype*. When you access a property that doesn't exist on an object, JavaScript walks up the prototype chain until it finds the property or reaches `null`.

### The Chain

```lisp
(bind obj (obj :x 1))
;; obj → Object.prototype → null

(bind arr #a(1 2 3))
;; arr → Array.prototype → Object.prototype → null
```

This is why every object has `.toString()` even though you didn't define it — it's inherited from `Object.prototype`. Every array has `.map()` because it's on `Array.prototype`.

### Why It Matters

The prototype chain explains four things the reader has already encountered:

1. **`Object:keys` returns only own properties** — not inherited ones
2. **`for-in` includes inherited properties** — which is why it's avoided
3. **Class inheritance** (Ch 20) — classes set up prototype chains
4. **Built-in methods exist** — `toString`, `valueOf`, `hasOwnProperty` live on `Object.prototype`

### `Object:create`

For explicit prototype setting:

```lisp
(bind parent (obj :greet (fn () (console:log "hello"))))
(bind child (Object:create parent))
(child:greet)  ;; → "hello" — inherited from parent
```

Surface Lykn prefers `type`/`match` and closures over prototype-based inheritance. The prototype chain is infrastructure that powers JavaScript underneath — understanding it helps debug, but you rarely manipulate it directly.
