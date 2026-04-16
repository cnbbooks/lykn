## Testing

Tests invoke handler functions directly — no server startup needed:

```javascript
import { assertEquals } from "jsr:@std/assert";
import { handleShorten } from "../dist/routes.js";

Deno.test("POST /api/shorten creates a short URL", async () => {
  const request = new Request("http://localhost:8080/api/shorten", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ url: "https://example.com" })
  });
  const response = await handleShorten(request);
  assertEquals(response.status, 200);
  const data = await response.json();
  assertEquals(typeof data.code, "string");
  assertEquals(data.code.length, 6);
});

Deno.test("returns 400 for missing url", async () => {
  const request = new Request("http://localhost:8080/api/shorten", {
    method: "POST",
    body: JSON.stringify({})
  });
  const response = await handleShorten(request);
  assertEquals(response.status, 400);
});
```

Construct a Web API `Request`, call the handler, check the `Response`. Fast, reliable, no port allocation.
