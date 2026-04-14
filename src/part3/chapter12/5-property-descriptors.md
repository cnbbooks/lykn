## Property Attributes and Descriptors

JavaScript properties have hidden attributes that control their behaviour. Most of the time you don't need to think about them — but understanding they exist explains some otherwise puzzling behaviour.

### The Three Attributes

Every data property has:

- **`writable`** — can the value be changed? (`true` by default)
- **`enumerable`** — does it show up in `for-in` and `Object.keys`? (`true` by default)
- **`configurable`** — can the descriptor be modified or the property deleted? (`true` by default)

Properties you create with normal code — `(obj :name "x")`, `bind`, assignment — have all three set to `true`. Properties defined by the language itself (like `Array.prototype.map`) are typically non-enumerable, which is why they don't show up when you iterate an object's keys.

### Inspecting and Defining

```lisp
;; Inspect a property's descriptor
(bind desc (Object:get-own-property-descriptor obj :name))
(console:log desc)
;; → { value: "x", writable: true, enumerable: true, configurable: true }

;; Define a property with specific attributes
(Object:define-property obj :frozen-name
  (obj :value "immutable"
       :writable false
       :enumerable true
       :configurable false))
```

### Assignment vs Definition

Assignment (`(= obj:name value)`) goes through the prototype chain and calls setters. Definition (`Object:define-property`) creates or modifies the property directly on the object, bypassing setters. The distinction rarely matters in daily code, but it explains why some patterns behave unexpectedly. The Deep-JS concept cards cover this in full detail.
