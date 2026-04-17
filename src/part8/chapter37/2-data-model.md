## The Data Model

Two `type` declarations define all the data flowing through the server:

```lisp
(type ShortUrl
  (Entry
    :string code
    :string url
    :number created-at
    :number clicks))
```

Every short URL entry has a code, the original URL, a creation timestamp, and a click counter. The compiler tracks this shape throughout the codebase.
