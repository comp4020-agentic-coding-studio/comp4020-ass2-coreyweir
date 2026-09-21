# Harness

## What this repo is

A course website for Slop University. The platform — the Slop branding, the four
content collections, the build pipeline and the generated API — is fixed, and
`README.md` documents it. Read it there. Do not restate it in this file, which
is for decisions and for the things that keep going wrong.

Everything else is mine: the course itself, its pages, components, navigation,
visual treatment and every word of content.

## The course

`SLOP8815`, level 8 — final-year masters. Working title: **How to Run Anything
in the Browser** (provisional).

**Thesis.** Everything is technically possible; trade-offs decide. Proofs of
concept are cheap now, and the engineering is in knowing which options are
justifiable, what each costs, and what evidence licences a decision.

**Audience.** Masters students who can already program. Never explain the
obvious. That polyfilling Node's API will not run a C++ browser is a one-line
joke, not a slide.

**Register.** Dead straight on every page — a real prospectus for a real course.
No winking, no nudging, no "yes, we know this is absurd". The subject is funny
because it is treated seriously. The deck is the one place the frame can show.

## Structure

Twelve weeks, locked:

1. Running code in the browser — plugin history, then the option space
2. Characterising a target — what a program actually requires
3. Shims, polyfills and reimplementation
4. Compiling for the web — which interface stops you first
5. The web is not POSIX-compatible (i)
6. The web is not POSIX-compatible (ii)
7. The filesystem
8. The network
9. Running "native" binaries
10. Running a full OS kernel
11. Graphics
12. Committing, and changing your mind

**Threads**, carried as `tags`: `polyfills`, `reimplementation`, `interfaces`,
`processes`, `filesystem`, `network`, `pipes`, `performance`, `graphics`.

A thread returning to a concern in a new context is coherence, not repetition.
Week 5 introduces a filesystem; week 7 is about filesystems. That is the course
working, not a duplicated topic.

**Lectures are hubs.** Short. They say what was covered and link to the pages
that own the detail. Nothing is explained twice.

**Sessions are practice, decoupled from the assignment target.** Each session
picks a program and applies the week's technique: *one technique, many
programs*. Students are encouraged to use their assignment target where it
suits, and every session offers suggestions so nobody burns the hour choosing.
Suggested sets are picked so the room's results differ along the axis the week
teaches.

**Assignments are depth: one program, many techniques.** Sessions do not build
toward them.

## Assessment

Three, totalling 100%.

| | Week | Weight | What it is |
|---|---|---|---|
| A1 | 4 | 20% | The reduction: characterise the target, reduce the justifiable option set |
| A2 | 9 | 40% | The commitment: build, measure, commit on evidence |
| A3 | 12 | 40% | The re-opening: a new requirement, and an audit of A1 |

Students choose their own target, carry it all semester, and choose A3's new
requirement themselves. A1 must warn that the initial choice constrains what A3
can be.

Do not mark breadth of the option space — for any target it is everything. Mark
accuracy of option analysis, quality of trade-off reasoning, difficulty of the
A3 adjustment, and calibration of the A1 audit.

## Content rules

- One idea across twelve weeks. Before adding a page, say which week it belongs
  to and which thread it advances.
- **Specificity is the whole defence against slop.** Prefer the real detail from
  real work — a named syscall, a measured number, an actual error — over a
  fluent paragraph that would suit any course on this subject. If a paragraph
  survives a find-and-replace of the technology, it is not written yet.
- Trade-offs, never feasibility. Reduce the justifiable set; do not "rule out".
- **A student commits to nothing in a session.** Sessions are practice and the
  target is optional in them, so the scope decisions a later week holds them to
  were made in **Assignment 1**, not "in week 2". Anchor every such reference to
  the assignment. This has been corrected four times.
- `src/course-config.ts` and the content collections are the source for course
  facts. Do not restate a date, a weight or a code in prose where it can drift.
- **Open every source before citing it.** A link label is a claim about what is
  on that page, so write it from the page — never from memory, never from a
  summary, and never from a URL I handed you without reading it first. Getting
  this wrong has cost us twice; the failure is treating a URL as a fact to
  paraphrase rather than a document to read.
- Bernhardt's talk is a citation, not a costume. The course tests the claim that
  "it's just compilers"; it does not retell the joke.
- History only where it is load-bearing for how you build now.
- Do not reproduce COMP4020's course design. No weekly prototypes, no crits.

## Platform traps

- A root-absolute link in an `.astro` file (`href="/sessions/"`) works on
  localhost and 404s on the deployed site. Use markdown links or the theme's
  components, which are rewritten for the base path.
- A collection key is the file, the URL, the API path and the ref all at once.
  Renaming one means renaming all four.
- Never hand-edit anything under `dist/`.
- The course code's last three digits are `815` and are fixed. Only the leading
  level digit is mine to choose, and `level` must match it.
- Replacing a `STARTER_CONTENT` fragment means deleting its marker comment in
  the same edit.
- A lecture's `slides:` is regex-locked to `/decks/<name>/`. Deep links to a
  slide go in the body as markdown, using `{/* _id: name */}` and `#/name`.
- `tags` on content nodes is unbounded; the 1–3 limit applies only to the course
  record.
- A markdown table with an empty leading header cell — the `| | A | B |` habit
  for a row-label column — fails the build's `empty-table-header` check. Name
  every column.

## Working rules

- Run `pnpm check` before reporting something done. "It should work" is not a
  result.
- Commit as you go, one logical change per commit. Do not batch.
- When I correct something that will recur, add the rule to this file in the
  same commit as the fix.
- Bring me the decision, not the finished page, when a course-design call is
  involved. The curriculum is mine.
