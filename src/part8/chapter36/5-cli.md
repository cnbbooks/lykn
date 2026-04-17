## The CLI Entry Point

```lisp
(async (func main
  :args (:array args)
  :body
  (bind parsed (parse-args args))
  (match parsed
    ((Ok (obj :input input :output output))
     (bind source (await (read-input input)))
     (bind blocks (parse-markdown source))
     (bind html (render-blocks blocks))
     (await (write-output output html)))
    ((Err message)
     (console:error (template "Error: " message))
     (Deno:exit 1)))))

(func parse-args
  :args (:array args)
  :returns :any
  :body
  (bind input (cell null))
  (bind output (cell null))
  (bind i (cell 0))
  (while (< (express i) args:length)
    (bind arg (get args (express i)))
    (if (= arg "-o")
      (do
        (swap! output (fn () (get args (+ (express i) 1))))
        (swap! i (fn (:number n) (+ n 2))))
      (do
        (swap! input (fn () arg))
        (swap! i (fn (:number n) (+ n 1))))))
  (Ok (obj :input (express input) :output (express output))))

(async (func read-input
  :args (:any path)
  :body
  (if (= path null)
    (await (read-stdin))
    (await (Deno:read-text-file path)))))

(async (func write-output
  :args (:any path :string content)
  :body
  (if (= path null)
    (console:log content)
    (await (Deno:write-text-file path content)))))

(await (main Deno:args))
```

The `Result` pattern for `parse-args` means errors are data, not exceptions. The `match` in `main` handles both cases explicitly. The `async` functions handle file I/O with `await`.
