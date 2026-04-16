## Streams

Data processed in chunks rather than loaded entirely into memory. Essential for large files and real-time data.

### Web Streams API

The modern standard — `ReadableStream`, `WritableStream`, `TransformStream`. Both Deno and modern Node.js support them:

```lisp
(bind file (await (Deno:open "large-file.txt")))
(bind decoder (new TextDecoderStream))
(bind stream (file:readable:pipe-through decoder))

(for-await-of chunk stream
  (process-chunk chunk))
```

### When Streams Matter

- **Large files** — reading a 1GB log file without loading it all into memory
- **Real-time data** — WebSocket messages, server-sent events
- **Network responses** — `fetch` returns a `Response` with a readable body stream

For most Lykn code, `Deno:read-text-file` and `fetch` handle the common cases. Streams are for when the data is too large or too continuous for buffering.
