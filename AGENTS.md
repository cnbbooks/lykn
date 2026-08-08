# AGENTS.md — The Lykn Book

This file provides guidance to Codex, Claude, and compatible coding agents when working in this repository.

## What this repo is

The Lykn Book — *And Now for Something Completely Parenthetical: A Lisp
Flavoured JavaScript*. An mdBook project; content in `src/`, published to
<https://cnbbooks.github.io/lykn/>.

## ⚠ Planning lives in the `lang` repo — do not create a planning tree here

The book's 0.6.0 edition is **arc16 of the lykn language project**, and it
**gates the 0.6.0 release** (operator decision, 2026-07-24). Its plan-of-record
is therefore in the language repo, not here:

- **`~/lab/lykn/lang/docs/design-v0.6.0/arc16-book-0.6.0-edition/`** — the arc
  plan, its slices, and the design/source material (the drift inventory, the
  0.6.0 kickoff thread, the fence-wiring spec, the dogfooding friction log).
- **`~/lab/lykn/lang/docs/backlog/discoveries.md`** — the Discovery Register.
  Book findings are `D-…` rows in the `Book (arc16)` section. Read
  `docs/backlog/README.md` there for the protocol **and the routing rule**.

Layout confirmed with the operator 2026-07-25, per
`collaboration-framework/docs/PROJECT-MANAGEMENT.md` Part VI. **Split by
design:** the *plan* lives with the project that gates on it; the *content*
lives here. Do not create `docs/design-vX.Y/` in this repo, and do not route
work to "the Book project" — that phantom owner is `D-2607-8HTN`, the finding
that cost this book three cold months.

`design/docs/{05-active,06-final}/` is an empty odm skeleton for design
decisions. It is **not** a planning tree; leave it alone unless promoting a DD.

## `workbench/` is gitignored scratch

Nothing durable and nothing cited by another document may live there. If an
artifact is worth referencing, it goes to a tracked home first. A path cited in
a tracked document must resolve in git before that document lands. This rule
exists because the dogfooding friction log and the book's entire 6–8 iteration
program sat untracked in `workbench/` while committed documents pointed at them.

## Code fences

Through 0.6.0, lykn code blocks use ` ```lisp `, **not** ` ```lykn ` — the
Linguist submission is deferred to 0.7.0+. Consequence: `lykn test --docs`
cannot see any of the book's blocks. Fix specced at
`arc16-book-0.6.0-edition/design/fence-wiring-spec.md` (`D-2607-R4NW`).

## Tools

`tools/book-audit/fences.lykn` — the fence-extraction tool, written in lykn as a
dogfooding exercise. Its friction log is the arc16 design material cited above.

## Commit messages

Every assistant-authored commit message includes these trailers:

```
Co-authored-by: Codex <noreply@openai.com>
Co-authored-by: Billo AI <ai-engineering@billo.systems>
```
