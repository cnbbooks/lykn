## HTTP Servers

### Deno Native: `Deno:serve`

```lisp
(Deno:serve (obj :port 8080)
  (fn (:any request)
    (bind headers (new Headers))
    (headers:set "Content-Type" "text/plain")
    (new Response "Hello from Lykn!" (obj :headers headers))))
```

```javascript
Deno.serve({port: 8080}, (request) => {
  const headers = new Headers();
  headers.set("Content-Type", "text/plain");
  return new Response("Hello from Lykn!", {headers});
});
```

One function. Web API `Request` and `Response` objects — the same standard web platform APIs the browser uses. No legacy callback interface.

### With Routing

```lisp
(Deno:serve (obj :port 8080)
  (async (fn (:any req)
    (bind url (new URL req:url))
    (match url:pathname
      ("/api/users" (await (handle-users req)))
      ("/api/health" (new Response "ok"))
      (_ (new Response "Not Found" (obj :status 404)))))))
```

`match` on the pathname provides clean routing. Each arm returns a `Response`.

### A Note on HTTP Headers

Lykn keywords undergo camelCase conversion (`:content-type` → `contentType`), but HTTP headers use their own casing (`Content-Type`). Use the `Headers` constructor with string keys for headers instead of `obj` with keywords.

### Node.js Compatibility

```lisp
(import "node:http" (create-server))

(bind server (create-server (fn (:any req :any res)
  (set! res:status-code 200)
  (res:set-header "Content-Type" "text/plain")
  (res:end "Hello from Lykn!"))))

(server:listen 8080)
```

`Deno:serve` is dramatically simpler — one function vs a multi-step callback. Use `node:http` only when porting existing Node.js code.
