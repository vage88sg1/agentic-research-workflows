# Concurrency post-mortem: why in-tree LaTeX builds corrupt

A condensed account of a real failure class, kept so the reasoning survives.

## The mechanism

A LaTeX build is not one program writing one file. A typical `latexmk` run is a
pipeline: latex writes `.aux`/`.toc`/`.bcf`, biber reads `.bcf` and writes `.bbl`,
latex runs again reading `.aux`/`.bbl`, possibly again. Between passes, the
intermediates on disk are the *only* shared state. Anything that mutates the
directory mid-pipeline desynchronizes that state:

- An **editor save** (human or AI agent) changes a `.tex` while pass 2 reads
  structures pass 1 derived from the old text. Labels move, the `.aux` no longer
  matches, and the run reports phantom undefined references or builds a PDF whose
  table of contents belongs to a document that no longer exists.
- A **second build** in the same directory interleaves writes to the same `.aux`
  files. Both builds read each other's half-written output. The classic symptom is
  `File ended while scanning use of ...` on a file nobody edited.
- A **sync tool** (Dropbox, iCloud, git checkout) replaces files at arbitrary
  moments with the same effects.

The trap: every symptom points at the *document*, not at the race. The
errors name your chapters and your citations, so the natural response is to "fix"
the source, which changes nothing, or to delete `.aux` files, which appears to
work because it forces a clean rebuild, until the race recurs. In a project with
multiple AI agent sessions editing concurrently, this failure recurred until
in-tree builds were banned entirely (the history is in WHY.md).

## The fix and its properties

Snapshot the source tree (rsync to scratch), build in the snapshot, copy only the
final PDF back. This gives three guarantees:

1. **Isolation**: edits after the snapshot cannot affect the running build.
2. **Cleanliness**: the working tree never contains intermediates, so it cannot
   hold corrupt ones, and version control never sees build noise.
3. **Determinism**: the build corresponds exactly to the snapshot moment. This is
   testable: mutate a source file mid-build and assert the output does not
   contain the mutation. The repo's test (g) does exactly that.

The cost is one rsync of the project per build, typically well under a second.

## Retrofitting a project that has its own Makefile

Do not delete or rewrite an existing build setup unasked. The drop-in pattern:

```make
# Before:
pdf:
	latexmk -pdf main.tex

# After:
pdf:
	path/to/safe-build.sh . main.tex
```

The output lands in the same place (`main.pdf` in the project root), so
downstream targets keep working. If the Makefile also has a `clean` target that
removes `.aux` files, it will simply find nothing to remove, because the working
tree no longer accumulates artifacts. That is the point.

## The stale-wrapper trap

One caution from the same history: a build wrapper with a hardcoded source path
is a liability. When the project moves or forks, the wrapper silently builds the
OLD tree, and "BUILD OK" certifies the wrong artifact. That is why
`safe-build.sh` takes the source dir as an argument, resolves everything at run
time, and prints the resolved source, main file, engine and output path in a
banner on every run. If you write any wrapper around it, preserve that property:
never hardcode what can be resolved, and always print what was resolved.
