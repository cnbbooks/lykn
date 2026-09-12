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

- **`/Users/oubiwann/lab/lykn/lang/.worktrees/planning/project02-language-toolchain-alignment/arc16-book-0.6.0-edition/`**
  — the arc plan, its slices, close reports, and source material (the drift
  inventory, the 0.6.0 kickoff thread, the fence-wiring spec, and the
  dogfooding friction log).
- **`/Users/oubiwann/lab/lykn/lang/.worktrees/planning/backlog/discoveries.md`**
  — the Discovery Register. Book findings are `D-...` rows in the
  `Book (arc16)` section. Read `backlog/README.md` there for the protocol
  **and the routing rule**.

Layout confirmed with the operator 2026-07-25, per
`collaboration-framework/docs/PROJECT-MANAGEMENT.md` Part VI. **Split by
design:** the *plan* lives with the project that gates on it; the *content*
lives here. Do not create `docs/design-vX.Y/` in this repo, and do not route
work to "the Book project" — that phantom owner is `D-2607-8HTN`, the finding
that cost this book three cold months.

`design/docs/{05-active,06-final}/` is an empty odm skeleton for design
decisions. It is **not** a planning tree; leave it alone unless promoting a DD.

## Instruction file convention

`AGENTS.md` is the canonical instruction file. `CLAUDE.md` remains a tracked
symlink to `AGENTS.md` for compatibility with agents that still probe for the
older filename. Preserve that relationship.

## `workbench/` is gitignored scratch

Nothing durable and nothing cited by another document may live there. If an
artifact is worth referencing, it goes to a tracked home first. A path cited in
a tracked document must resolve in git before that document lands. This rule
exists because the dogfooding friction log and the book's entire 6–8 iteration
program sat untracked in `workbench/` while committed documents pointed at them.

## Code fences

Through 0.6.0, lykn code blocks use ` ```lisp `, **not** ` ```lykn ` — the
Linguist submission is deferred to 0.7.0+. The 0.6.0 book-fence gate is now:

```sh
/Users/oubiwann/lab/lykn/lang/.worktrees/0.6.x/bin/lykn test --docs src --fence lisp
```

Use `--fence lisp --fence lykn` for a mixed-tag sweep. The current whole-book
gate is expected to fail on stale examples; that is routing input for lang
arc16 follow-up slices, not permission to edit around language/tooling defects
in prose.

Do not treat `deno test test/book/` as a universal book gate. For targeted
examples, use the release-worktree `lykn` wrapper commands and record failures
or coverage gaps in the language repo close/discovery artifacts.

## Current 0.6.0 authoring truth

- Lykn-owned workflows use `lykn` wrappers (`lykn check`, `lykn test`,
  `lykn lint`, `lykn build`, `lykn run`, `lykn dist`, `lykn publish`) unless a
  passage is specifically teaching Deno itself.
- Prefer top-level `(exports ...)` forms for module exports. Inline export
  wrappers remain compatibility syntax, not the preferred teaching surface.
- Use grouped, sequential `bind` where that is the clearest expression of a
  chapter example.
- Use `cond` for multi-branch conditionals when it fits the lesson.
- The Rust CLI is the primary authoring and verification path. The JS/Deno
  compiler is also a maintained implementation path; do not describe it as
  limited to browser use.
- Source trees may contain user-owned non-Lykn files. The 0.6.0 package/source
  ownership floor is about which Lykn files the toolchain owns, not a blanket
  ban on other files.

## Defect routing

Book review is expected to surface language, tooling, and DevX defects. Do not
normalize those defects away in prose. Add or update the relevant Discovery
Register row in the language repo and route the finding to a new slice or an
explicit deferral before relying on prose as the only fix.

## Tools

`tools/book-audit/fences.lykn` — the fence-extraction tool, written in lykn as a
dogfooding exercise. Its friction log is the arc16 design material cited above.

## Commit messages

Every assistant-authored commit message includes these trailers:

```
Co-authored-by: Codex <noreply@openai.com>
Co-authored-by: Billo AI <ai-engineering@billo.systems>
```
