## Maranget's Algorithm

One algorithm, two consumers.

Maranget's algorithm works on a *pattern matrix*: each row is a clause, each column is a parameter position. The algorithm *specializes* the matrix by testing each constructor and recursively checking the remaining matrix. If any specialization produces an empty matrix — no clause handles it — the match is non-exhaustive.

### For `match` Exhaustiveness

The pattern matrix is the match clauses. Non-exhaustive → compile error with a message naming the missing variant.

### For `func` Overlap Detection

The pattern matrix is the clause signatures. Two rows that both match the same input → overlap → compile error.

### The Provenance

Published by Luc Maranget at JACM 2008. Used by Rust, OCaml, and Haskell for the same purpose. Lykn's implementation is a direct application of the published algorithm. The reader who wants the details should read the paper; the reader who wants the benefit already has it — every `match` and multi-clause `func` in the book has been checked by this algorithm.
