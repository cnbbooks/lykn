## Contracts: `:pre` and `:post`

A contract is a promise. `:pre` is what the caller promises: "I will give you valid inputs." `:post` is what the function promises: "I will give you a valid output." When a promise is broken, the error says whose fault it is.

### A Complete Example

```lisp
(func deposit
  :args (:number amount :object account)
  :returns :object
  :pre (> amount 0)
  :post (> (get ~ :balance) (get account :balance))
  :body (assoc account :balance (+ (get account :balance) amount)))
```

In development mode:

```javascript
function deposit(amount, account) {
  if (typeof amount !== "number" || Number.isNaN(amount))
    throw new TypeError(
      "deposit: arg 'amount' expected number, got " + typeof amount);

  if (typeof account !== "object" || account === null)
    throw new TypeError(
      "deposit: arg 'account' expected object, got " + typeof account);

  if (!(amount > 0))
    throw new Error(
      "deposit: pre-condition failed: (> amount 0) — caller blame");

  const result__gensym0 = {...account, balance: account["balance"] + amount};
  if (!(result__gensym0["balance"] > account["balance"]))
    throw new Error(
      "deposit: post-condition failed: (> (get ~ :balance) (get account :balance)) — callee blame");

  return result__gensym0;
}
```

With `--strip-assertions`:

```javascript
function deposit(amount, account) {
  return {...account, balance: account["balance"] + amount};
}
```

Eight lines of safety in development. One line of logic in production. Same function, same source.

### Caller Blame, Callee Blame

**`:pre` blames the caller.** The error message says "caller blame" because the caller broke their promise — they passed invalid arguments. If `deposit` is called with a negative amount, it's the caller's fault, not the function's.

**`:post` blames the callee.** The error message says "callee blame" because the function broke *its* promise — it returned something that doesn't meet its own guarantee. If the balance somehow decreased after a deposit, that's the function's fault.

This distinction matters for debugging. When a contract fails in a large codebase, "caller blame" tells you to look at the call site; "callee blame" tells you to look at the implementation.

### Error Messages Include the Source

The compiler serializes the `:pre`/`:post` expression to text at compile time. When the error fires at runtime, you see the exact condition that failed:

```
deposit: pre-condition failed: (> amount 0) — caller blame
```

Not "assertion failed." Not "Error at line 42." The actual s-expression that was violated, right there in the error message. This is possible because s-expressions are trivially serializable — they're already text.

### Single Expression, Composed with `and`/`or`

Each contract clause takes one expression. For multiple conditions, use `and` or `or`:

```lisp
(func transfer
  :args (:number amount :object from :object to)
  :returns :object
  :pre (and (> amount 0)
            (<= amount (get from :balance))
            (not (= from to)))
  :body ...)
```

`and` short-circuits: if the first condition fails, the rest aren't evaluated. This means you can safely write `(and (not (= x null)) (> (get x :balance) 0))` — the second check won't run if `x` is null.
