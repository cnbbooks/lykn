## Why Async?

JavaScript is single-threaded. It can only do one thing at a time. But it needs to handle things that take time — network requests, file reads, timers, user input.

### The Event Loop

The solution: don't wait. Start the operation, keep doing other things, and deal with the result when it arrives. JavaScript processes a queue of events, one at a time, never blocking. Each event handler runs fully before the next event is processed — this is "run-to-completion."

### The Callback Era

Before promises, async results were handled via callbacks — functions passed as arguments, called when the operation completed:

```javascript
// JavaScript: callback pattern
fetchData(url, function(error, data) {
  if (error) {
    handleError(error);
  } else {
    processData(data, function(error, result) {
      if (error) {
        handleError(error);
      } else {
        saveResult(result, function(error) {
          if (error) handleError(error);
        });
      }
    });
  }
});
```

Three sequential operations, three levels of nesting, three error checks. This is "callback hell" — the pyramid of doom. It works, but it doesn't scale, and it certainly doesn't read.

### The Promise Revolution

Promises (ES2015) and async/await (ES2017) replaced callbacks with a linear, readable model. The same sequence:

```lisp
(async (func process-data
  :args (:string url)
  :body
  (bind data (await (fetch-data url)))
  (bind result (await (process data)))
  (await (save-result result))))
```

Three operations, three lines, zero nesting. This is what the rest of the chapter teaches.
