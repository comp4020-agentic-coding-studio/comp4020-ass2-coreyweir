# Harness

## What this repo is

A course website for Slop University. The platform — the Slop branding, the four
content collections, the build pipeline and the generated API — is fixed, and
`README.md` documents it. Read it there. Do not restate it in this file, which
is for decisions and for the things that keep going wrong.

Everything else is mine: the course itself, its pages, components, navigation,
visual treatment and every word of content.

## The course

<!-- Not yet decided. Concept, level digit and voice land here once they are,
     and every content decision below should be checkable against them. -->

## Content rules

- One idea, carried across twelve weeks. Before adding a page, say which week it
  belongs to and how it advances that idea. A page that would sit just as well
  in some other course is a page to cut.
- No filler. If a paragraph would survive a find-and-replace of the subject, it
  is not written yet.
- `src/course-config.ts` and the content collections are the source for course
  facts. Pages read from them; do not restate a date, a weight or a code in
  prose where it can drift.

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

## Working rules

- Run `pnpm check` before reporting something done. "It should work" is not a
  result.
- Commit as you go, one logical change per commit. Do not batch.
- When I correct something that will recur, add the rule to this file in the
  same commit as the fix.
