## The API Client

Fetch wrappers for the `shortn` server. Uses `Result` for error handling.

```lisp
(bind api-base "http://localhost:8080")

(export (async (func shorten-url
  :args (:string url)
  :body
  (try
    (bind response (await (fetch (template api-base "/api/shorten") (obj
      :method "POST"
      :headers (new Headers #a(#a("Content-Type" "application/json")))
      :body (JSON:stringify (obj :url url))))))
    (if (not response:ok)
      (Err "server error")
      (Ok (await (response:json))))
    (catch e
      (Err (template "network error: " e:message)))))))

(export (async (func list-entries
  :body
  (try
    (bind response (await (fetch (template api-base "/api/list"))))
    (if (not response:ok)
      (Err "failed to load entries")
      (Ok (await (response:json))))
    (catch e
      (Err (template "network error: " e:message)))))))
```

Each function returns `Result` — either `Ok` with data or `Err` with a message. The caller uses `match`:

```lisp
(async (func refresh-entries
  :body
  (match (await (list-entries))
    ((Ok entries) (set-entries entries))
    ((Err message) (set-error message)))))
```

Chapter 10's pattern, applied to real HTTP requests.
