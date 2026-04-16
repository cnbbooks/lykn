## The Server and Routing

```lisp
(async (func route-request
  :args (:any request)
  :body
  (bind url (new URL request:url))
  (bind method request:method)
  (bind path url:pathname)

  ;; CORS preflight
  (if (= method "OPTIONS")
    (do
      (bind headers (new Headers))
      (headers:set "Access-Control-Allow-Origin" "*")
      (headers:set "Access-Control-Allow-Methods" "GET, POST, OPTIONS")
      (headers:set "Access-Control-Allow-Headers" "Content-Type")
      (new Response null (obj :status 204 :headers headers)))

    ;; Static routes
    (if (and (= method "POST") (= path "/api/shorten"))
      (await (handle-shorten request))
      (if (and (= method "GET") (= path "/api/list"))
        (await (handle-list))
        ;; Dynamic routes
        (await (route-dynamic method path)))))))

(console:log "shortn running on http://localhost:8080")
(Deno:serve (obj :port 8080) route-request)
```

Static routes first (exact path match), dynamic routes second (regex matching for `:code` parameters), 404 fallback. CORS preflight handled explicitly for the browser app in Chapter 36.
