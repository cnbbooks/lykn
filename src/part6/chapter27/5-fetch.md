## The Fetch API

Modern HTTP requests from the browser.

### GET

```lisp
(async (func load-users
  :body
  (bind response (await (fetch "/api/users")))
  (if (not response:ok)
    (throw (new Error (template "HTTP " response:status))))
  (await (response:json))))
```

### POST

```lisp
(async (func create-user
  :args (:string name :string email)
  :body
  (bind response (await (fetch "/api/users" (obj
    :method "POST"
    :headers (obj :content-type "application/json")
    :body (JSON:stringify (obj :name name :email email))))))
  (await (response:json))))
```

### With Result

```lisp
(async (func safe-fetch
  :args (:string url)
  :body
  (try
    (bind response (await (fetch url)))
    (Ok (await (response:json)))
    (catch e (Err e:message)))))
```

The Fetch API returns promises — `async`/`await` (Ch 17) is the natural companion.
