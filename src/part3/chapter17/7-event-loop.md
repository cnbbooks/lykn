## The Event Loop: Just Enough

Three things the reader needs to know about how JavaScript processes async operations underneath.

### The Call Stack

Synchronous code runs on the call stack. When a function calls another function, the new frame goes on top. When a function returns, its frame comes off. The stack must be empty before any async callback runs.

### Two Queues

**Microtask queue**: promise callbacks (`.then`, `.catch`), `queueMicrotask`. These run *immediately* after the current synchronous code finishes — before the next timer or I/O event.

**Task queue** (macrotask): `setTimeout`, `setInterval`, I/O callbacks, event handlers. These run one at a time, with the microtask queue fully drained between each.

### Processing Order

1. Run the call stack to empty
2. Drain the entire microtask queue
3. Process one task from the task queue
4. Repeat

This is why `Promise:resolve():then(...)` runs before `(set-timeout ... 0)` — promise callbacks are microtasks, timers are macrotasks. Microtasks always go first.

### What This Means for `await`

`await` pauses the *function*, not the *thread*. The event loop keeps processing other events while your function waits. When the awaited promise settles, the function's continuation is added to the microtask queue and resumes at the next opportunity.

*Exploring JavaScript* and [MDN's event loop documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Event_loop) have the full model for readers who want the deep dive. For working code, the practical knowledge is: `await` doesn't block, microtasks run before macrotasks, and JavaScript handles concurrent I/O without threads by never waiting for anything.
