## Error Handling

When compilation fails, the shim catches the error and reports it to the browser console:

```text
lykn compile error (line 5, col 12):
  expected type keyword or destructuring pattern, got bare symbol 'x'
  in: (func add :args (x y) :body (+ x y))
                       ^
  Hint: all parameters require type annotations, e.g. (:number x :number y)
```

Compile errors include source location, the failing expression, and a hint when available. For pages with multiple `<script type="text/lykn">` tags, the tag index is included.

Runtime errors — from the compiled JavaScript — appear as normal browser errors. Type check assertions from `func` and `fn` produce `TypeError` with the function name and expected type, same as compiled output from `lykn compile`.

Source maps are a future enhancement. Currently, the shim compensates by including the lykn source expression in compile error messages.
