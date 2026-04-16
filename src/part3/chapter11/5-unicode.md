## Unicode Essentials

Three facts about Unicode in JavaScript that every developer needs. Three facts, and then we move on.

### `.length` Lies

JavaScript strings are UTF-16 encoded. Most characters are one code unit, but emoji and many non-Latin scripts are two (surrogate pairs). `.length` counts code units, not characters:

```javascript
"hello".length    // → 5 (correct)
"😀".length       // → 2 (not 1 — it's a surrogate pair)
"café".length     // → 4 (correct — é is one code unit here)
"🇺🇸".length       // → 4 (two surrogate pairs for one flag emoji)
```

If you need character counts, use `Array:from` to split by code points: `(Array:from str):length`. But even that doesn't handle grapheme clusters (combinations of code points that render as one visible character).

### `for-of` Is Safer

`for-of` iterates code points, which handles surrogate pairs correctly. Indexed access (`(get str 0)`) and `for` loops over indices do not — they see individual code units, which means an emoji at position 0 takes up indices 0 and 1.

```lisp
;; Safe: iterates code points
(for-of char "hello 😀"
  (console:log char))
;; Logs: h, e, l, l, o,  , 😀 (seven iterations)
```

### `Intl.Segmenter` Exists

For grapheme-accurate text processing — correctly counting what humans think of as "characters," handling combined emoji, zero-width joiners, and regional indicators — use `Intl:Segmenter`. It's a built-in API, available in all modern runtimes, and it's the only reliable way to segment text by visual characters.

These three facts cover the survival knowledge. *Exploring JavaScript* and the [MDN Unicode guide](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String#utf-16_characters_unicode_code_points_and_grapheme_clusters) provide the full deep dive for readers who need it.
