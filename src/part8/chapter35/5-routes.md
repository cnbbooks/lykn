## The Route Handlers

Each endpoint is an async function that returns a `Response`.

### JSON Response Helper

```lisp
(bind cors-headers (obj
  :access-control-allow-origin "*"
  :access-control-allow-methods "GET, POST, OPTIONS"
  :access-control-allow-headers "Content-Type"))

(func json-response
  :args (:any data :number status)
  :returns :any
  :body
  (bind headers (new Headers))
  (headers:set "Content-Type" "application/json")
  (headers:set "Access-Control-Allow-Origin" "*")
  (new Response (JSON:stringify data) (obj :status status :headers headers)))
```

### Shorten Handler

```lisp
(export (async (func handle-shorten
  :args (:any request)
  :body
  (try
    (bind body (await (request:json)))
    (if (= body:url undefined)
      (json-response (obj :error "url required") 400)
      (do
        (bind code (await (generate-unique-code)))
        (bind entry (Entry code body:url (Date:now) 0))
        (await (save-entry entry))
        (json-response
          (obj :code code :short-url (template "http://localhost:8080/" code)) 200)))
    (catch e
      (json-response (obj :error e:message) 400))))))
```

### Redirect Handler

```lisp
(export (async (func handle-redirect
  :args (:string code)
  :body
  (bind entry (await (get-entry code)))
  (if (= entry null)
    (new Response "Not Found" (obj :status 404))
    (do
      (await (increment-clicks code))
      (match entry
        ((Entry c url ca clicks)
         (bind headers (new Headers))
         (headers:set "Location" url)
         (new Response null (obj :status 302 :headers headers)))))))))
```

Each handler takes typed inputs, returns a Promise of Response, uses `match` on `type` variants, and returns appropriate HTTP status codes.
