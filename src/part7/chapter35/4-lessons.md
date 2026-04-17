## Lessons from Building

### The Compiler Is the Easy Part

Parsing s-expressions and emitting ESTree is straightforward. The hard part is deciding *what to emit*: what type checks to generate, when to use IIFE wrapping, how to handle `await` in expression position, what error messages to show. Design decisions outnumber implementation decisions ten to one.

### Error Messages Are a Feature

A compiler's quality is measured by its errors as much as its output. "Expected type keyword at position 3" is bad. "Field 'name' missing type annotation (use :any to opt out)" is good. Every error should suggest a fix. The error message is the compiler's user interface.

### Tests Are the Specification

With two independent compilers (JS and Rust), the test fixtures are the language's ground truth. If both compilers produce the same output for a test case, the behaviour is specified. Cross-compiler tests are worth more than documentation.

### Design Documents Prevent Re-Litigation

Every settled decision has a DD. When a question arises during implementation, the DD answers it. When a new feature interacts with an old decision, the DD records the reasoning. Without DDs, the same argument happens three times.

### Thin Skin Means Inheriting Problems

JavaScript's floating-point-only arithmetic, `typeof null === "object"`, and `Array.isArray` vs `typeof` for arrays are all inherited by Lykn. The surface compiler can warn about them but can't fix them. Some hazards are below the skin.
