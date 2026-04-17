## Building for Deployment

```sh
lykn compile --strip-assertions packages/shortn-ui/ -o dist/
```

Deploy `index.html` and `dist/` to any static host: GitHub Pages, Netlify, Cloudflare Pages, or a simple file server.

### Configuration by HTML

For production, read the API base URL from a data attribute:

```html
<body data-api-base="https://api.shortn.example.com">
```

```lisp
(bind api-base document:body:dataset:api-base)
```

Same compiled JS deploys to dev and prod. No build-time substitution required.
