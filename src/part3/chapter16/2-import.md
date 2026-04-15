## `import`

The `import` form puts the module path first, then the bindings. This is the opposite of JavaScript's `import { x } from "path"` but consistent with Lykn's "operator first" convention — the module path is the primary operand.

### Named Imports

```lisp
(import "./utils.js" (add subtract))
```

```javascript
import {add, subtract} from "./utils.js";
```

The binding names are grouped in a list. camelCase conversion applies: if you write `(import "./utils.js" (read-file))`, the compiled output is `import {readFile} from "./utils.js"`.

### Default Import

```lisp
(import "react" React)
```

```javascript
import React from "react";
```

A bare atom (not wrapped in a list) after the path imports the default export.

### Renamed Import with `alias`

```lisp
(import "./utils.js" ((alias add my-add)))
```

```javascript
import {add as myAdd} from "./utils.js";
```

`alias` renames: `add` is the exported name, `my-add` is what you call it locally. The same `alias` form used in destructuring (Ch 15) and `match` patterns.

### What's Banned: Namespace Imports

```lisp
;; NOT SUPPORTED in Lykn
;; (import "fs" (* as fs))
```

Namespace imports (`import * as fs from "fs"`) are not supported. Why? They hide dependencies. `fs:read-file` doesn't tell you at the import site which names you're using. Explicit binding lists make dependencies visible and enable tree-shaking.

If you need many names from a module, list them. It's more typing but every dependency is visible at the import site.
