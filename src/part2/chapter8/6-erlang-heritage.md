## The Erlang Heritage

Multi-clause dispatch didn't arrive in Lykn by accident. The lineage runs through three languages.

### Erlang

```erlang
%% Erlang
greet(Name) -> "Hello, " ++ Name;
greet(Greeting, Name) -> Greeting ++ ", " ++ Name.
```

In Erlang, function heads with pattern matching on arguments are the primary mechanism for polymorphism. No classes. No inheritance. Just: "if the arguments look like this, do this; if they look like that, do that." The BEAM runtime dispatches at call time, selecting the first matching clause.

### LFE

```lisp
;; LFE (Lisp Flavoured Erlang)
(defun greet
  ((name) (++ "Hello, " name))
  ((greeting name) (++ greeting ", " name)))
```

LFE wraps the same mechanism in s-expressions. The parenthesized clause groups, the arity-based dispatch, the compile-to-BEAM pipeline — all preserved. The syntax changes; the semantics don't.

### Lykn

```lisp
;; Lykn
(func greet
  (:args (:string name)
   :returns :string
   :body (template "Hello, " name))

  (:args (:string greeting :string name)
   :returns :string
   :body (template greeting ", " name)))
```

Lykn's version adds keyword-labeled clauses (for self-documentation and contracts), type-keyword dispatch (Erlang dispatches on pattern shape; Lykn dispatches on type predicates), and overlap detection as a compile error (Erlang uses first-match-wins).

The lineage is direct. Duncan McGreggor, Lykn's creator, is a core contributor to LFE. Multi-clause dispatch in Lykn isn't a borrowed feature — it's a family trait, adapted for a JavaScript host.
