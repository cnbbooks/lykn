## The Project: `shortn`

A URL shortener API. It accepts long URLs, generates short codes, stores the mapping, and redirects.

### Endpoints

- **`POST /api/shorten`** — accepts `{ "url": "https://..." }`, returns `{ "code": "abc123", "short_url": "..." }`
- **`GET /:code`** — redirects (302) to the original URL
- **`GET /api/list`** — returns JSON array of all entries
- **`GET /api/stats/:code`** — returns click count and creation time
- **`OPTIONS`** — CORS preflight (for the browser app in Ch 38)

### Usage

```sh
# Start
lykn run packages/shortn/mod.lykn

# Shorten a URL
curl -X POST http://localhost:8080/api/shorten \
  -H "Content-Type: application/json" \
  -d '{"url": "https://oxur.io/lykn"}'

# Follow the short URL
curl -L http://localhost:8080/abc123
```

### Project Structure

```text
shortn/
  project.json
  packages/
    shortn/
      mod.lykn           ← server entry point
      routes.lykn        ← route handlers
      storage.lykn       ← Deno KV wrapper
      codes.lykn         ← short code generation
  test/
    routes.test.js
```
