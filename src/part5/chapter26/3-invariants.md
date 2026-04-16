## Proxy Invariants

Proxies can't lie about everything. The JavaScript engine enforces *invariants* — consistency rules between the proxy's behaviour and the target's state.

If a property is non-configurable and non-writable on the target, the `get` trap must return the actual value — not a fabricated one. If `Object:is-extensible target` returns `false`, the proxy's `is-extensible` trap must also return `false`.

These invariants prevent proxies from creating impossible objects. A proxy can intercept and customize, but it can't contradict the target's non-configurable properties. The target's constraints are the proxy's constraints.

The reader doesn't need to memorize every invariant. The key insight: proxies customize behaviour, they don't override reality.
