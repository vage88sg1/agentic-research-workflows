# Why this exists

This skill is the build discipline that emerged from writing a large,
figure-heavy master's thesis (a PDF in the low hundreds of pages) with several AI
agent sessions editing the LaTeX tree at the same time, over several weeks.

What kept happening: a session would run `latexmk` in the working tree while
another session saved a chapter, and the half-written `.aux`/`.bcf` intermediates
produced failures that looked exactly like source bugs. Hours went into "fixing"
documents that were never broken. At the worst point it happened twice in one
day. The fix that ended it was boring and total: no compiler ever runs in the
working tree again; every build snapshots the tree to scratch, builds there, and
copies only the PDF back. The thesis shipped from that workflow, and the working
tree never held a build artifact again.

Two more lessons rode along and are encoded here:

- Page counts: the university counted text pages (first chapter through
  conclusion), not PDF pages. Every build therefore reported both numbers, which
  turned "how long is it now?" from a manual ritual into a build byproduct.
- The stale wrapper: at one point a leftover build script pointed at a frozen
  copy of the document and cheerfully rebuilt the wrong tree. Since then the rule
  is that a build tool must print what it resolved (source, main file, engine,
  output) on every run, so a wrong-tree build is visible in the first five lines.

A last lesson that did not make it into the tooling: when a document must lose
pages, mid-chapter word cuts often save nothing, because float placement pins
the page boundaries; the productive targets are chapters whose final page holds
only a few spilled lines. And after any cut, comparing per-chapter counts of
labels, figures, and citations before and after proves that only prose was lost.

None of this is thesis-specific. Any long-lived LaTeX project touched by more
than one process (a human plus an agent is already two) has the same failure
modes; this skill just packages the discipline so the next project starts with
it instead of rediscovering it.
