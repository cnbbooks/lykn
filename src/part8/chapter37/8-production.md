## Production Notes

**Deno Deploy**: upload the compiled JS to Deno's serverless platform. KV works natively. No server management.

**Self-hosted**: run behind a reverse proxy (nginx, Caddy) that handles TLS. Use the `PORT` environment variable.

**Compiled binary**: `deno compile --allow-net --unstable-kv --output shortn dist/shortn.js` produces a single executable with Deno embedded. No Deno installation required on the target.

### What's Missing

- No authentication (anyone can shorten any URL)
- No rate limiting (vulnerable to abuse)
- Logs go to stdout (no rotation)
- Single instance only (no horizontal scaling without external state)

These are real gaps. A production URL shortener would address all of them. For the purpose of this book — demonstrating that Lykn can build a real server — `shortn` is complete.
