## `bind`: One Form to Rule Them All

JavaScript has three ways to declare a variable. Lykn has one. This is not a limitation — it is a decision, arrived at after careful consideration of the alternatives and a frank assessment of the damage the alternatives have done.

### The Basics

```lisp
(bind name "Duncan")
(bind age 42)
(bind active true)
(bind scores #a(98 87 92 100))
```

```javascript
const name = "Duncan";
const age = 42;
const active = true;
const scores = [98, 87, 92, 100];
```

`bind` compiles to `const`. Always. No exceptions. No flags. No configuration options. The binding is immutable — once `name` is `"Duncan"`, it stays `"Duncan"`. If you later write `(bind name "Someone Else")` in the same scope, the compiler will object, and it will be right to do so.

### Type Annotations

For literal values — strings, numbers, booleans — the type is self-evident, and no annotation is needed. For non-literal initializers, a type annotation documents the expected type and emits a development-mode check:

```lisp
;; Literals — type is obvious
(bind name "Duncan")
(bind count 42)

;; Non-literals — annotation recommended
(bind :number result (parse-float input))
(bind :string greeting (template "Hello, " name))
```

```javascript
const result = parseFloat(input);
if (typeof result !== "number" || Number.isNaN(result))
  throw new TypeError("bind: 'result' expected number, got " + typeof result);
const greeting = `Hello, ${name}`;
if (typeof greeting !== "string")
  throw new TypeError("bind: 'greeting' expected string, got " + typeof greeting);
```

The type keyword (`:number`, `:string`, `:boolean`, etc.) sits between `bind` and the name. Pass `--strip-assertions` at compile time and these checks vanish for production, leaving behind nothing but the clean `const` declaration.

### What `bind` Is Not

`bind` is not a variable declaration. Variables, by definition, vary. `bind` creates a *binding* — a name permanently attached to a value. The distinction is not merely semantic. It changes how you think about your program: instead of "what is `x` now?" you ask "what is `x`?" The answer doesn't depend on when you ask.

This is the functional commitment described in Chapter 2: all surface-language bindings are immutable. If you need a value that changes over time, that's a `cell` — a controlled, explicit mutable container. Cells are their own concept, with their own chapter (Ch 13). `bind` is for values that don't change, which, it turns out, is most of them.
