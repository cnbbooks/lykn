## Bundle Size

The shim bundle contains:

| Component | Approx size |
|---|---|
| Reader | ~320 lines |
| Surface compiler (JS) | ~1,700 lines |
| Kernel compiler | ~1,670 lines |
| Macro expander | ~950 lines |
| astring (vendored) | ~16KB |
| Shim handler | ~50 lines |

Total bundle: ~73KB. Small enough for development use. Far smaller than most JavaScript frameworks — the entire Lykn compiler is smaller than React's runtime.

For production, use pre-compiled ESM modules (Ch 27) — no shim needed, no compilation overhead, just clean JavaScript served directly.
