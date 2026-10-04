#!/usr/bin/env python3
"""Report a PDF's total page count and its "text page" count.

Text pages are what universities and journals actually count: the span from the
first content chapter to the last page before the bibliography or appendix. Both
numbers are printed because reporting only the PDF total to someone with a page
limit is misleading; the two numbers can differ by a wide margin.

With no arguments the script tries a set of common boundary markers and reports
which ones matched. When it cannot find boundaries it says so and reports the
total honestly instead of guessing.

Usage:
    text_pages.py document.pdf
    text_pages.py document.pdf --start "1 Introduction" --end "References"

Requires: pypdf (pip install pypdf). Exits 0 with a notice if missing, so build
wrappers can call it unconditionally.
"""
import argparse
import sys

START_CANDIDATES = ["Chapter 1", "1 Introduction", "Introduction", "Kapitel 1",
                    "1 Einleitung", "Einleitung"]
END_CANDIDATES = ["Bibliography", "References", "Literaturverzeichnis",
                  "Appendix", "Anhang"]


def find_page(pages, markers, after=-1):
    """First (index, marker) whose page text contains a marker, after `after`.

    Candidate order is priority order, so each marker is searched across all
    pages before the next marker is tried; otherwise a stray 'Introduction' in
    an abstract would beat 'Chapter 1'.
    """
    for marker in markers:
        for i, text in enumerate(pages):
            if i > after and marker in text:
                return i, marker
    return None, None


def main() -> int:
    ap = argparse.ArgumentParser(
        description="Report total and text page counts of a PDF.")
    ap.add_argument("pdf")
    ap.add_argument("--start", default=None,
                    help="text found on the first text page "
                         "(default: try common chapter-one headings)")
    ap.add_argument("--end", default=None,
                    help="text found on the first page AFTER the text pages "
                         "(default: try common bibliography/appendix headings)")
    args = ap.parse_args()

    try:
        from pypdf import PdfReader
    except ImportError:
        print("text_pages.py: pypdf not installed (pip install pypdf); "
              "skipping page-count report", file=sys.stderr)
        return 0

    reader = PdfReader(args.pdf)
    pages = [(p.extract_text() or "") for p in reader.pages]
    total = len(pages)
    print(f"TOTAL PDF PAGES: {total}")

    starts = [args.start] if args.start else START_CANDIDATES
    ends = [args.end] if args.end else END_CANDIDATES

    start, start_marker = find_page(pages, starts)
    if start is None:
        tried = ", ".join(repr(s) for s in starts)
        print(f"TEXT PAGES: not determined (no start marker found; tried {tried}). "
              f"Pass --start matching your first chapter heading.")
        return 0

    # Search the end marker only after the start page, so a table-of-contents
    # entry naming the bibliography cannot end the count early.
    end, end_marker = find_page(pages, ends, after=start)
    if end is None:
        tried = ", ".join(repr(e) for e in ends)
        print(f"TEXT PAGES ({start_marker!r} -> end of document): {total - start} "
              f"(no end marker found; tried {tried}; pass --end to bound it)")
        return 0

    print(f"TEXT PAGES ({start_marker!r} -> before {end_marker!r}): {end - start}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
