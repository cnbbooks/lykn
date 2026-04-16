## Dates

JavaScript's `Date` is widely regarded as one of the language's weakest APIs. Zero-indexed months, mutable objects, no time zone support, no duration type. But it's what we have, and the reader needs it.

### Creating Dates

```lisp
;; Current date/time
(bind now (new Date))

;; From ISO 8601 string
(bind birthday (new Date "1984-03-15"))

;; From components (month is 0-indexed!)
(bind specific (new Date 2026 3 15 10 30 0))
;;                       year month day hour min sec
;;                       Note: month 3 = April (0-indexed)

;; From timestamp (milliseconds since epoch)
(bind epoch (new Date 0))
```

**The zero-indexed month trap**: `(new Date 2026 3 15)` is *April* 15, not March 15. Month `0` is January, `11` is December. This surprises every developer exactly once. Now it has surprised you.

### Getting Components

```lisp
(bind now (new Date))
(now:get-full-year)        ;; → 2026
(now:get-month)            ;; → 3 (April — zero-indexed!)
(now:get-date)             ;; → 15 (day of month)
(now:get-day)              ;; → 3 (Wednesday — 0=Sunday)
(now:get-hours)            ;; → 10
(now:get-time)             ;; → milliseconds since epoch
```

### Formatting

`Intl:DateTimeFormat` for locale-aware formatting:

```lisp
(bind fmt (new Intl:DateTimeFormat "en-US"
  (obj :date-style "full")))
(console:log (fmt:format now))
;; → "Wednesday, April 15, 2026"
```

Or the simpler `to-locale-date-string`:

```lisp
(console:log (now:to-locale-date-string "en-US"
  (obj :weekday "long" :year "numeric" :month "long" :day "numeric")))
```

### Date Arithmetic

Dates don't have add/subtract methods. Use millisecond arithmetic:

```lisp
(bind tomorrow (new Date (+ (now:get-time) (* 24 60 60 1000))))
```

This is painful. It's correct, but painful.

### The Future: Temporal

The Temporal API (TC39 stage 3) is the upcoming replacement: immutable date objects, proper time zone support, duration types, sane arithmetic. When it ships, it will replace most uses of `Date`. Check Deno's support. For serious date handling today, most projects use a library (date-fns, Luxon, or a Temporal polyfill).
