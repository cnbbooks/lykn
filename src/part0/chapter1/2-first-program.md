## Your First Program

Every programming book begins with Hello World. This tradition dates to Kernighan and Ritchie's *The C Programming Language* (1978) and has been observed faithfully ever since, in much the same way that christenings have been observed faithfully ever since someone decided that splashing water on an infant was an appropriate response to the miracle of new life. One does it because one does it. The infant — or, in this case, the programming language — is too new to object.

### Hello, World

Here is Hello World in Lykn:

```lisp
(bind greeting "Hello, World!")
(console:log greeting)
```

And here is what the compiler produces:

```javascript
const greeting = "Hello, World!";
console.log(greeting);
```

Two lines in, two lines out. Let's look at what each piece means.

### What You Just Wrote

`(bind greeting "Hello, World!")` creates an immutable binding. The name `greeting` is bound to the string `"Hello, World!"` and cannot be reassigned. Under the hood, `bind` compiles to `const` — JavaScript's own immutable declaration. There is no `bind!`, no mutable variant, no way to later decide that `greeting` should be something else. If you want mutation, Lykn has a mechanism for that (`cell`), but it's explicit, deliberate, and wears a `!` suffix so you can see it coming. Chapter 4 covers bindings in detail.

`(console:log greeting)` calls `console.log` with `greeting` as its argument. The colon in `console:log` is Lykn's member access syntax — it compiles to a dot. Colons are used throughout Lykn where JavaScript uses dots: `Math:floor`, `Array:is-array`, `document:get-element-by-id`. The pattern is consistent and, once you've seen it three times, invisible.

The parentheses are the function call. In Lykn, as in all Lisps, function application is written `(function arg1 arg2 ...)` — the operator comes first, followed by its arguments, all wrapped in parentheses. This is prefix notation, and it is the entirety of Lykn's syntax. There are no special cases, no operator precedence to memorize, no ambiguity about what is being called with what arguments. The parentheses *are* the grammar.

### Something With Teeth

Hello World establishes that the compiler works. Let's write something that shows *why* you'd use Lykn rather than plain JavaScript:

```lisp
(func greet
  :args (:string name)
  :returns :string
  :body (+ "Hello, " name "!"))

(console:log (greet "World"))
```

This compiles to:

```javascript
function greet(name) {
  if (typeof name !== "string")
    throw new TypeError(
      "greet: arg 'name' expected string, got " + typeof name);

  const result__gensym0 = "Hello, " + name + "!";
  if (typeof result__gensym0 !== "string")
    throw new TypeError(
      "greet: return value expected string, got "
      + typeof result__gensym0);

  return result__gensym0;
}
console.log(greet("World"));
```

The `:args (:string name)` annotation tells Lykn that `name` must be a string. The `:returns :string` annotation says the function must return one. The compiler turns these annotations into runtime `typeof` checks — if someone calls `greet(42)`, they get a clear `TypeError` with the function name, parameter name, expected type, and actual type. In production, pass `--strip-assertions` and the checks vanish, leaving behind nothing but the clean function.

This is the transaction at the heart of Lykn: you write s-expressions with type annotations and contracts; you get JavaScript that a careful human might have written, plus safety guarantees that a careful human would have forgotten by the third function.
