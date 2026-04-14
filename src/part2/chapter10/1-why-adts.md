## Why Algebraic Data Types?

Before syntax, motivation. The reader has just learned `if`, `switch`, and `try`/`catch`. Here are the problems those tools can't solve.

### The Falsy Problem

```javascript
// JavaScript: did the function find a user?
const user = findUser(id);
if (user) {
  greet(user);
} else {
  redirect();
}
```

This looks reasonable. It's also wrong. If `findUser` returns `0` (a valid user ID), the truthiness check fails. If it returns `""` (a valid but empty username), the truthiness check fails. JavaScript's `if` conflates "no value" with "falsy value" — six different things that are `false`, and the code can't distinguish between them.

### The Exception Problem

```javascript
// JavaScript: did the API call succeed?
try {
  const data = fetchData(url);
  process(data);
} catch (e) {
  handleError(e);
}
```

What if `process()` throws? The `catch` catches that too. The error handler intended for fetch failures is now handling processing bugs. JavaScript's `try`/`catch` conflates "expected failure" (network error) with "unexpected bug" (null dereference in `process`).

### The Solution

Data types that *say what they mean*:

```lisp
(type Option
  (Some :any value)
  None)
```

`Some` means "I have a value." `None` means "I don't." There's no ambiguity. No falsy confusion. And `match` forces you to handle both:

```lisp
(match (find-user id)
  ((Some user) (greet user))
  (None (redirect)))
```

If you forget `None`, it's a compile error — not a runtime surprise three months later when a user with ID `0` can't log in.

This is where BugAID's research pays off: "dereferenced non-values" is the #1 bug pattern across 105,133 commits. `Option` eliminates it by construction. You can't dereference a `None` because `match` won't let you reach the `Some` branch without also handling the `None` branch.
