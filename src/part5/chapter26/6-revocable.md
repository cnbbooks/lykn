## Revocable Proxies

`Proxy:revocable` creates a proxy that can be permanently disabled:

```lisp
(bind (object proxy revoke) (Proxy:revocable target handler))
;; Use proxy normally...
(revoke)
;; Any further access throws TypeError
```

After `revoke()`, every operation on the proxy throws. The target is unaffected — only the proxy is disabled.

Use cases: granting temporary access to an object (timed sessions, capability-based security), sandbox teardown, test cleanup.
