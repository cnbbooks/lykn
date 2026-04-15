## Array-Like Objects and Conversion

Some JavaScript APIs return array-like objects — `arguments`, NodeLists, typed arrays — that have `.length` and numeric indices but aren't real arrays. They don't have `map`, `filter`, or any of the methods from this chapter.

### Convert Them

```lisp
(bind real-array (Array:from node-list))
(bind also-real (array (spread node-list)))
```

After conversion, all array methods work.

### Typed Arrays

`Int32Array`, `Float64Array`, `Uint8Array`, and friends — arrays with fixed numeric types and direct memory backing. Used for binary data, WebGL, audio processing, and cryptography. Same interface as regular arrays (`.map`, `.filter`, `.length`) but different backing storage.

The concept cards cover typed arrays in detail. For most application code, regular arrays are sufficient.
