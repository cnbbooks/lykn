## File System Access

### Deno Native API

```lisp
;; Read a text file
(bind content (await (Deno:read-text-file "config.json")))

;; Write a text file
(await (Deno:write-text-file "output.txt" content))

;; Read directory entries
(for-await-of entry (Deno:read-dir "src")
  (console:log entry:name entry:is-file))
```

Deno's API is simple — `read-text-file` is always UTF-8, no encoding option needed.

### Node.js Compatibility

```lisp
(import "node:fs/promises" (read-file write-file mkdir))

(bind data (await (read-file "config.json" (obj :encoding "utf-8"))))
(await (write-file "output.txt" data))
(await (mkdir "dist" (obj :recursive true)))
```

Both work in Deno. The Deno native API is simpler; the `node:fs` API is compatible with Node.js documentation and code.

### Permissions

Deno requires explicit permission flags for file access:

```sh
deno run --allow-read=config.json --allow-write=output.txt app.js
```

Without the flags, file operations throw a `PermissionError`. This is a feature — explicit permissions prevent accidental file system access from untrusted code. You can grant broad access (`--allow-read`) or narrow it to specific paths (`--allow-read=src,config.json`).
