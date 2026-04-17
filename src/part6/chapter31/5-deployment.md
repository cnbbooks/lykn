## Deployment Patterns

Lykn's compiled output is standard JavaScript. Any JavaScript deployment mechanism works. This section is brief because it should be — deployment is the least Lykn-specific part of the entire pipeline.

### CLI Tool

Deno can compile JavaScript to a self-contained binary. No Deno installation required on the target machine.

```bash
deno compile --allow-read --output mdify dist/app.js
```

The reader will build exactly this in Ch 36 — a Markdown-to-HTML converter called `mdify`. The compiled binary includes the Deno runtime, so it runs anywhere without dependencies.

### Server

Two options: Deno Deploy for managed hosting, or self-hosted with the Deno runtime.

```bash
# Deno Deploy — managed, edge-distributed
deployctl deploy --project=shortn dist/shortn.js

# Self-hosted — just run it
deno run --allow-net --allow-read dist/shortn.js
```

The reader will build this in Ch 37 — a URL shortener called `shortn`. The deployment is the same as any Deno server deployment, because the compiled output is the same as any Deno server code.

### Browser App

Static files. Copy them to a web server or CDN.

```bash
cp index.html dist/app.js /var/www/html/
```

The reader will build this in Ch 38 — a browser UI for the `shortn` server. The deployment is a file copy. The compiled JavaScript runs in any modern browser with no build step beyond what `lykn compile` already did.

### The Pattern

All three deployment targets share the same upstream pipeline: check, compile, lint, test, verify documentation. The only difference is the final step — what you do with the JavaScript that comes out the other end. A CLI tool compiles to a binary. A server runs on Deno. A browser app ships as static files. The pipeline doesn't care which one you choose.
