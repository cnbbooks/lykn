## Short Code Generation

Random 6-character codes from a 62-character alphabet:

```lisp
(bind alphabet "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")

(export (func generate-code
  :returns :string
  :body
  (bind bytes (new Uint8Array 6))
  (crypto:get-random-values bytes)
  (bind chars (cell #a()))
  (for-of byte bytes
    (swap! chars (fn (:array c)
      (conj c (get alphabet (% byte alphabet:length))))))
  ((express chars):join "")))
```

Collision probability with 62^6: about 1 in 56 billion. The handler checks for collisions and regenerates if needed.
