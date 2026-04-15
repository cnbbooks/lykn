## Sequential vs Parallel

A common pitfall: accidentally running independent async operations sequentially.

### The Problem

```lisp
;; SEQUENTIAL — each waits for the previous
(bind user (await (fetch-user id)))
(bind posts (await (fetch-posts id)))
(bind comments (await (fetch-comments id)))
;; Total time: user + posts + comments
```

Each `await` pauses until the previous operation completes. If each takes 200ms, total time is 600ms.

### The Fix

```lisp
;; PARALLEL — all start at once
(bind (array user posts comments) (await (Promise:all #a(
  (fetch-user id)
  (fetch-posts id)
  (fetch-comments id)))))
;; Total time: max(user, posts, comments)
```

`Promise:all` starts all three operations simultaneously and waits for all to complete. If each takes 200ms, total time is 200ms.

### The Rule

When operations are independent — they don't need each other's results — use `Promise:all`. When each operation depends on the previous result, sequential `await` is correct:

```lisp
;; SEQUENTIAL is correct here — each step needs the previous result
(bind token (await (authenticate credentials)))
(bind user (await (fetch-user-with-token token)))
(bind profile (await (load-profile user:id)))
```

The difference: in the parallel version, all three `fetch` calls start immediately. In the sequential version, each call waits for the previous one's result before starting.
