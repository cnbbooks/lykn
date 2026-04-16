## DOM Selection and Traversal

### Finding Elements

```lisp
;; By ID
(bind app (document:get-element-by-id "app"))

;; By CSS selector (first match)
(bind header (document:query-selector "h1.title"))

;; By CSS selector (all matches — returns NodeList)
(bind items (document:query-selector-all ".item"))

;; Convert NodeList to array for functional methods
(bind item-array (Array:from items))
(item-array:for-each (fn (:any el) (console:log el:text-content)))
```

camelCase conversion makes DOM methods read naturally: `query-selector-all` → `querySelectorAll`, `get-element-by-id` → `getElementById`.

### Traversal

```lisp
el:parent-element          ;; → parentElement
el:children                ;; → children (HTMLCollection, live)
el:first-element-child     ;; → firstElementChild
el:next-element-sibling    ;; → nextElementSibling
(el:closest ".container")  ;; → walk up the tree to matching ancestor
```
