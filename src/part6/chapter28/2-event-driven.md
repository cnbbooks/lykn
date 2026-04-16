## The Event-Driven Model

Both Node.js and Deno use the same model: single-threaded event loop with non-blocking I/O. The reader learned the event loop in Chapter 17. This section connects it to the server.

A server handles many connections on one thread. I/O operations — file reads, network requests, database queries — are non-blocking. The event loop multiplexes thousands of connections by never waiting for any single one.

Every request handler is an async function. Every I/O operation awaits. The event loop processes events between await points. CPU-intensive work blocks the loop — use Web Workers for that.

The key insight: `async`/`await` (Ch 17) is not just syntax sugar for convenience. On the server, it's *how concurrency works*. The entire programming model is built on the event loop, and `await` is the developer's interface to it.
