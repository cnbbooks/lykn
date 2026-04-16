## Proxy and Lykn's Surface Language

Surface Lykn's functional patterns cover many use cases where other languages reach for metaprogramming:

| Need | Proxy Approach | Lykn Surface Approach |
|---|---|---|
| Validation | `set` trap | `:pre` contracts (Ch 8) |
| Immutability | `set`/`delete` traps | `bind` + `cell` (default) |
| Default values | `get` trap | Destructuring defaults (Ch 15) |
| Logging | `get`/`set` traps | `swap!` callback (Ch 13) |
| Reactive state | `set` trap + notify | `cell` + observer pattern |

Proxy is the escape hatch for cases where surface patterns aren't enough — typically when you need to intercept operations on an object you *don't control*: a library's return value, a DOM element, a third-party API response.

If you're intercepting your own objects, contracts and cells are simpler. If you're intercepting someone else's, Proxy is the tool.
