## Storage with Deno KV

Deno KV is a built-in key-value store — persistent, async, zero configuration.

```lisp
(bind kv (await (Deno:open-kv)))

(export (async (func save-entry
  :args (:any entry)
  :body
  (match entry
    ((Entry code url created-at clicks)
     (await (kv:set #a("urls" code)
       (obj :code code :url url
            :created-at created-at :clicks clicks))))))))

(export (async (func get-entry
  :args (:string code)
  :body
  (bind result (await (kv:get #a("urls" code))))
  (if (= result:value null)
    null
    (Entry result:value:code result:value:url
           result:value:created-at result:value:clicks)))))

(export (async (func list-entries
  :body
  (bind entries (cell #a()))
  (for-await-of entry (kv:list (obj :prefix #a("urls")))
    (swap! entries (fn (:array arr)
      (conj arr (Entry entry:value:code entry:value:url
                       entry:value:created-at entry:value:clicks)))))
  (express entries))))

(export (async (func increment-clicks
  :args (:string code)
  :body
  (bind entry (await (get-entry code)))
  (if (not (= entry null))
    (match entry
      ((Entry c u ca clicks)
       (await (save-entry (Entry c u ca (+ clicks 1))))))))))
```

The storage module converts between `Entry` tagged variants and plain JSON-serializable objects for KV. The boundary is explicit — internal data uses `type`, stored data uses plain objects.
