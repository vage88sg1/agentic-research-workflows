---
name: academic-writing-latex
description: Use when drafting, revising, or polishing an academic graduation thesis report in English (or expanding rough notes into thesis prose). Enforces formal academic register, IMRaD-style structure, IEEE-style citations, LaTeX-compatible formatting, and zero-hallucination technical writing. Triggers on requests like "draft chapter", "polish this thesis section", "rewrite academically", "expand these notes into thesis prose", "write the introduction/methodology/evaluation".
license: MIT
---

# Academic Writing with LaTeX — Guidelines

Behavioral guidelines for producing academic writing that is formal, coherent, well-structured, and ready for a student to adapt into a final graduation thesis submission.

**Tradeoff.** These guidelines prioritize academic rigor, depth, and formal structure over quick summarization or casual explanation. Output will be longer and more deliberate than a typical chat reply, and structured specifically for thesis review by an academic committee.

**Scope.** Applies to undergraduate and master's-level graduation theses, conference and journal papers, and technical reports written in English. The default citation style is IEEE; switch only when the user specifies a different university template.

---

## 1. Academic Tone and Structure

Write in clear academic English with a formal and consistent register.

- Prefer fully developed paragraphs over bullet points. Use bullet lists only when the content is inherently list-shaped (contributions, requirements, evaluation criteria, enumerations).
- Avoid over-fragmented subsections. Keep the document hierarchy clean, readable, and proportional to the content — do not introduce a subsection for every paragraph.
- Use `-` for list items, never `*` or `---`.
- **Quotation marks (LaTeX-compatible).** Use LaTeX-style quotes: two backticks to open and two apostrophes to close (`` ``double quotes'' ``); single backtick and apostrophe for single quotes (`` `single' ``). Never use Unicode smart quotes (`" "`, `' '`) or straight ASCII quotes (`"`, `'`) — they render incorrectly when compiled with `pdflatex`/`xelatex`.
- From the second paragraph onward within the same section, indent the first line when the target format supports it (LaTeX does this automatically; in Markdown drafts, leave it to the renderer).
- Keep transitions smooth between paragraphs and sections so the report reads as a continuous academic argument, not a sequence of disconnected notes.
- Avoid casual wording, unsupported superlatives ("the best", "extremely powerful"), marketing language, and rhetorical questions.

### 1.1 Tense and Voice

- **Past tense** for completed work the author performed: methods used, experiments conducted, results obtained ("The model was trained on...", "We measured...").
- **Present tense** for established knowledge, definitions, and statements about the thesis itself ("The kernel manages...", "This chapter presents...").
- **Future tense** sparingly, mostly in the introduction's roadmap ("Chapter 4 will analyze...") and in Future Work.
- Prefer the **third person** or the **authorial "we"** consistent with the chosen style guide; avoid "I" unless the program explicitly permits it.
- Passive voice is acceptable in Methods and Results to keep focus on the work; do not use it to obscure agency in the Discussion.

### 1.2 Hedging and Claims

- Calibrate certainty. Use hedges ("suggests", "indicates", "is consistent with") for inferential claims and reserve definitive language ("proves", "demonstrates") for results that are formally established.
- Never write "it is well known that X" without a citation. If you cannot cite it, rephrase it as an assumption or remove it.

---

## 2. Content Development Workflow

Expand rough ideas into academic prose; do not translate them literally.

- **Analyze context.** Before drafting, identify the report topic, scope, academic level (B.Sc., M.Sc.), target chapter (Introduction, Background, Methodology, Results, Discussion, Conclusion), and any rubric or template constraints the user has shared.
- **Expand with purpose.** Read rough notes carefully and expand each main idea into full academic prose with logical transitions and sufficient explanation to stand on its own. A reader from the same field but unfamiliar with this specific project must be able to follow without external context.
- **Logical hierarchy.** Organize content into a sensible hierarchy: chapter → section → subsection. Each section should advance a single argumentative purpose.
- **Refine and polish.** Revise for clarity, remove repetition, and keep wording neutral. Read the draft aloud (mentally) — if a sentence feels conversational, rewrite it.
- **Light assumptions.** If non-technical contextual information is missing, make the lightest reasonable assumption and flag it (e.g., "Assuming the target platform is ARM Cortex-M..."). Never invent unsupported facts.

### 2.1 Suggested Chapter Structure (IMRaD-aligned)

For most engineering theses, the following structure is a safe default. Adjust to match the user's university template.

1. **Introduction** — problem statement, motivation, scope, contributions, thesis outline.
2. **Background / Related Work** — theoretical foundations and a critical review of prior art (not a list of paper summaries).
3. **Methodology / System Design** — the proposed approach, design decisions, and rationale.
4. **Implementation** — concrete realization, tooling, and engineering details (only if substantial enough to warrant a chapter).
5. **Evaluation / Results** — experimental setup, metrics, and observed outcomes, reported objectively.
6. **Discussion** — interpretation, comparison with related work, threats to validity, limitations.
7. **Conclusion and Future Work** — summary of contributions and concrete directions for extension.
8. **References** — formatted according to the chosen citation style.
9. **Appendices** — supplementary material that would interrupt the main narrative.

---

## 3. Technical Rigor and Presentation

Maintain strict technical accuracy and clean formatting for engineering content.

- **Zero hallucination.** Do not invent technical mechanisms, vulnerability details, hardware architectures, API behaviors, or numerical results. If a specific technical constraint is missing, explicitly state the limitation or ask the user for clarification — never fill the gap with plausible-sounding fabrication.
- **Code and logs formatting.** Present code snippets, memory layouts, register dumps, and terminal output in fenced Markdown code blocks with the correct language tag (` ```c `, ` ```asm `, ` ```python `, ` ```bash `). Keep listings short; elide irrelevant lines with `// ...` and explain the elision.
- **Terminology.** Define every technical acronym on first use, e.g., "Real-Time Operating System (RTOS)", and use the acronym consistently thereafter. Maintain a single canonical spelling for each technical term across the document.
- **Numbers and units.** Use SI units with a non-breaking space between the value and unit ("16~kHz" in LaTeX). Be explicit about precision: state the number of significant figures and the measurement uncertainty when reporting empirical results.

### 3.1 Figures, Tables, and Equations

High-level expectations only; full conventions live in §5.4 (LaTeX floats), §6 (math), and §7 (figures and tables).

- Every figure and table must be **numbered, captioned, and referenced by number** from the body text — never by position.
- Captions are full sentences that convey the take-away, not just describe contents.
- Equations are numbered only when referenced.

---

## 4. Research and Referencing

Support claims with credible academic sources and proper citations.

- Search for related theses, journal articles, conference papers, and authoritative documentation when background material is needed. Prefer venues with peer review (IEEE, ACM, USENIX, Springer, Elsevier) and reputable preprint servers (arXiv) when accompanied by a venue.
- Prefer reliable sources: university repositories, indexed journals, official standards documents (ISO, IETF RFCs, vendor reference manuals), and recognized research databases. Avoid blog posts, Wikipedia, and Stack Overflow as primary citations; if they are the only source, indicate so and seek a stronger replacement.
- **Verify every reference** before citing it: confirm the URL resolves, the DOI is valid, and the work actually supports the specific claim being made. Do not cite a paper for something it does not say.
- Connect each citation directly to the claim it supports — placement matters. A citation at the end of a paragraph attaches to the whole paragraph; place it immediately after the specific sentence when only one claim is supported.
- Format citations in **IEEE style** by default unless the user specifies a different template (ACM, APA, university-specific). A typical IEEE entry:

  ```
  [1] J. Smith and A. Doe, ``Title of the paper,'' in Proc. IEEE Int. Conf. Computer Systems (ICCS), 2024, pp. 123--130, doi: 10.1109/ICCS.2024.0001.
  ```

- Avoid citation padding (citing many papers for a trivial claim) and citation laundering (citing a survey instead of the original work).

---

## 5. LaTeX Conventions

When the output is intended for LaTeX compilation, follow these conventions strictly. They are the most common sources of compilation errors and ugly typesetting in student theses.

### 5.1 Quotes, Dashes, and Spacing

- **Quotation marks.** See §1 — use `` ``...'' `` and `` `...' ``, never Unicode or ASCII straight quotes.
- **Dashes.** Three lengths, three uses:
  - Hyphen `-` for compound words ("real-time").
  - En-dash `--` for ranges ("pp.~123--130", "1990--1995").
  - Em-dash `---` for parenthetical breaks in prose — like this — with no surrounding spaces.
  - Limit the use of em-dashes in academic prose. Prefer commas, parentheses, semicolons, or sentence restructuring when the same meaning can be expressed more formally and clearly.
- **Non-breaking space `~`.** Use between a label and its number, and between a value and its unit, to prevent line breaks: `Figure~3.2`, `Section~4.1`, `16~kHz`, `Dr.~Smith`.
- **Sentence-ending periods after abbreviations.** After a lowercase abbreviation that is not the end of a sentence, use a backslash-space to suppress the inter-sentence stretch: `e.g.,\ FreeRTOS`, `i.e.,\ the kernel`. Or use the `\@` trick when an uppercase letter ends a sentence: `...published by NASA\@.`
- **Ellipsis.** Use `\dots` (or `\ldots`), not three periods `...`.
- **Percent sign.** Always escape: `95\%`, never `95%` (which begins a comment).

### 5.2 Cross-References and Labels

- Use `\label{}` and `\ref{}` (or `\eqref{}` for equations, `\autoref{}` if `hyperref` is loaded). Never write section or figure numbers by hand — they will desynchronize.
- Use a label-prefix convention to keep namespaces clear:
  - `\label{ch:intro}`, `\label{sec:methodology}`, `\label{subsec:freertos}`
  - `\label{fig:architecture}`, `\label{tab:results}`, `\label{eq:loss}`, `\label{alg:scheduler}`, `\label{lst:kernel-init}`
- Place `\label{}` immediately after `\caption{}` inside floats, not before — placing it before captures the wrong counter.
- Cross-reference with a non-breaking space: `Figure~\ref{fig:architecture}`, `Equation~\eqref{eq:loss}`.

### 5.3 Math Mode

LaTeX-syntax essentials only; symbol conventions, equation numbering, punctuation around equations, and multi-line layouts are covered in §6.

- **Inline math** uses `$...$` or `\(...\)`. Do not use the deprecated `$$...$$` for display math; use `\[...\]` or the `equation` / `align` environments.
- Use `align` (from `amsmath`) for multi-line equations, not `eqnarray` (deprecated and badly spaced).

### 5.4 Floats: Figures, Tables, and Listings

LaTeX mechanics only; design and authoring guidelines are in §7.

- Wrap figures and tables in `figure` / `table` floats with placement specifier `[htbp]`. Avoid `[H]` (forced placement) except when truly necessary.
- Place `\label{}` immediately after `\caption{}` inside floats, never before.
- **Code listings.** Use the `listings` or `minted` package, not verbatim screenshots. Wrap long listings inside a float so they can be cross-referenced.

### 5.5 BibLaTeX / BibTeX

- Prefer **BibLaTeX with the `biber` backend** for new theses; it handles Unicode, modern citation styles, and IEEE-Trans variants correctly. Fall back to BibTeX only if the university template mandates it.
- Keep entries in a single `references.bib` file. One entry per work; do not duplicate.
- **Capitalize titles defensively.** BibTeX lowercases titles in many styles; protect proper nouns with braces: `title = {{FreeRTOS}: A real-time kernel for {ARM} {Cortex-M}}`.
- Always include a stable identifier: `doi`, `isbn`, or `url` + `urldate` for online sources.
- Use semantic citation keys: `smith2024freertos`, not `ref1`.
- Cite with `\cite{}` (numeric IEEE) or `\textcite{}` / `\parencite{}` (BibLaTeX author-year). Use `\cite[p.~42]{key}` for page-specific citations.

### 5.6 Document Structure and Packages

- Standard preamble for an engineering thesis:

  ```latex
  \documentclass[12pt,a4paper,oneside]{report}
  \usepackage[utf8]{inputenc}
  \usepackage[T1]{fontenc}
  \usepackage{lmodern}
  \usepackage[english]{babel}
  \usepackage{microtype}              % subtle typographic improvements
  \usepackage{amsmath,amssymb,amsthm} % math
  \usepackage{graphicx}               % figures
  \usepackage{booktabs}               % professional tables
  \usepackage{siunitx}                % SI units and number formatting
  \usepackage{listings}               % code listings
  \usepackage[hidelinks]{hyperref}    % load LAST, except for cleveref
  \usepackage[capitalize]{cleveref}   % smart cross-references; load AFTER hyperref
  ```

- **Package load order matters.** `hyperref` should be loaded last among most packages; `cleveref` must come after `hyperref`. `biblatex` should be loaded before `csquotes` is used.
- **One sentence per line in the source.** Makes diffs and version control reviewable. LaTeX collapses single newlines into spaces, so this does not affect the output.
- **Comment with `%`** to leave notes for collaborators. Use `\todo{}` (from the `todonotes` package) for visible drafting reminders that you intend to remove before submission.
- **Compile pipeline.** Run `pdflatex` → `biber` (or `bibtex`) → `pdflatex` → `pdflatex` to resolve all references and bibliography. Use `latexmk -pdf` to automate this.

### 5.7 Common LaTeX Mistakes to Avoid

- Hardcoded numbers for figures, sections, or equations instead of `\ref{}`.
- Using `\\` to break paragraphs (it breaks lines without starting a new paragraph; leave a blank line instead).
- Forgetting `~` before `\ref` and `\cite`, producing line breaks before "Figure 3" or "[7]".
- Italicizing entire blocks of text with `{\it ...}` instead of `\emph{...}`.
- Using `\centerline` or `\center` instead of the `center` environment.
- Mixing `\bf`, `\it`, `\rm` (deprecated TeX commands) with `\textbf`, `\textit`, `\textrm` (modern LaTeX commands).

---

## 6. Mathematical Notation and Equations

These conventions apply to academic math regardless of typesetting tool, but the LaTeX hints assume the `amsmath` package is loaded.

### 6.1 Symbol Conventions

- **Scalars and variables:** italic lowercase Latin or Greek (`x`, `\theta`, `\lambda`).
- **Vectors:** bold lowercase (`\mathbf{x}`) or arrow (`\vec{x}`). Pick one and use it consistently throughout the thesis.
- **Matrices:** bold uppercase (`\mathbf{A}`) or uppercase italic depending on the field's convention.
- **Tensors of order ≥ 3:** calligraphic (`\mathcal{T}`) or sans-serif bold.
- **Sets and number systems:** blackboard bold for canonical sets — `\mathbb{R}`, `\mathbb{N}`, `\mathbb{Z}`, `\mathbb{C}`, `\mathbb{Q}`. Custom sets in calligraphic (`\mathcal{D}` for a dataset, `\mathcal{H}` for a hypothesis space).
- **Functions and operators:** named operators are upright. Use `\sin`, `\cos`, `\log`, `\exp`, `\max`, `\min`, `\arg\max`, `\arg\min`. For custom operators, declare with `\DeclareMathOperator{\softmax}{softmax}` in the preamble and call as `\softmax(\cdot)`.
- **Constants vs. variables:** mathematical constants are upright (`\mathrm{e}`, `\mathrm{i}`, `\pi` is conventionally italic by tradition). The differential `d` is upright in IEEE/engineering style: `\mathrm{d}x`.
- **Probability:** `\Pr(A)` or `\mathbb{P}(A)`; expectation `\mathbb{E}[X]`; variance `\mathrm{Var}(X)`. Conditional bars use `\mid` (correct spacing), not `|`.
- **Multi-letter identifiers** must be wrapped in `\text{}` or `\mathrm{}` to avoid being typeset as a product: `\text{loss}`, `\mathrm{MSE}`, `\mathrm{IoU}` — never `loss` or `MSE` raw in math mode. This also applies to subscripts: `x_{\text{train}}`, not `x_{train}`.

### 6.2 Equation Numbering

- **Number only equations that are referenced** from the body text. Unreferenced equations clutter the document.
- Use `equation` (or `align`) for numbered displays, and `equation*` / `align*` (or `\[...\]`) for unnumbered displays.
- Reference with `\eqref{eq:label}` (renders as "(3.1)") not `\ref{}` (renders as "3.1" without parentheses). With `cleveref`, `\cref{eq:label}` produces "Eq.~(3.1)" automatically.
- For derivations, suppress numbering on intermediate steps with `\nonumber` (in `align`) or use `align*` and number only the final result.
- Subordinate numbering with `subequations` for related equations: `(3.1a)`, `(3.1b)`, `(3.1c)`.

### 6.3 Punctuation and Grammar Around Equations

Treat equations as part of the sentence, not as separate blocks.

- **Punctuate as if reading aloud.** A display equation that ends a sentence ends with a period; one that continues a sentence ends with a comma or no punctuation at all. The mark goes **inside** the math environment.

  ```latex
  The loss is defined as
  \begin{equation}
      \mathcal{L}(\theta) = \frac{1}{N} \sum_{i=1}^{N} \ell(f_\theta(x_i), y_i),
      \label{eq:loss}
  \end{equation}
  where $\ell$ denotes the per-sample loss and $N$ the batch size.
  ```

- **Capitalization after a display.** Continue with lowercase ("where $\ell$...") if the equation is part of the sentence. Start a new sentence (capital) only if the equation ended one.
- **Do not start a sentence with a symbol.** Rewrite: not "$x$ denotes..." but "Let $x$ denote..." or "The variable $x$ denotes...".
- **Read the equation in your head.** If "Equation~\eqref{eq:loss}, where $\ell$..." reads as a fragment, the punctuation is wrong.

### 6.4 Defining Symbols

- **Introduce every symbol on first use.** "Let $\theta \in \mathbb{R}^d$ denote the model parameters, where $d$ is the parameter count." Do not assume the reader can infer meaning from context.
- **Do not redefine symbols** within the same chapter. If two concepts collide, rename one.
- **Maintain a Nomenclature / List of Symbols** at the front matter for theses with heavy math. Use the `nomencl` package or `glossaries`. Group by category (sets, scalars, vectors, operators).
- When borrowing notation from prior work, cite the source on first use: "Following the notation of Smith~\cite{smith2024}, we write $\mathcal{H}$ for the hypothesis space."

### 6.5 Display vs. Inline

- **Inline** (`$...$`) for short expressions that fit on a single line and do not disrupt line spacing: `$x^2 + 1$`, `$O(n \log n)$`, `$\theta \in \Theta$`.
- **Display** (`\[...\]` or `equation`) for any expression with `\sum`, `\int`, `\prod`, large fractions, matrices, or that you intend to reference later. Inline `\sum_{i=1}^{n}` forces the limits to subscript position and looks cramped.
- **Force display-style limits inline** when needed: `$\sum\limits_{i=1}^{n} x_i$` or wrap in `\displaystyle`.

### 6.6 Multi-line Equations and Cases

- Use `align` (from `amsmath`) for systems of equations or step-by-step derivations. Align on `&` at the relation (`=`, `\leq`, `\Rightarrow`).

  ```latex
  \begin{align}
      \mathcal{L}(\theta)
          &= \mathbb{E}_{(x,y) \sim \mathcal{D}} [\ell(f_\theta(x), y)] \label{eq:loss-pop} \\
          &\approx \frac{1}{N} \sum_{i=1}^{N} \ell(f_\theta(x_i), y_i). \label{eq:loss-emp}
  \end{align}
  ```

- Use `cases` for piecewise definitions:

  ```latex
  \[
      \mathrm{ReLU}(x) = \begin{cases} x & \text{if } x \geq 0, \\ 0 & \text{otherwise.} \end{cases}
  \]
  ```

- Long single equations that must break: use `split` (single equation number) or `multline` (no `&` alignment, suitable for one long expression).
- Never use `eqnarray` — its spacing is broken by design.

### 6.7 Operator Limits and Big Operators

- Place limits **above and below** for `\sum`, `\prod`, `\bigcup`, `\bigcap`, `\lim`, `\max`, `\min` in display mode (default). Inline mode pushes them to the side (default and correct).
- For integrals, the IEEE convention is **side-set** limits: `\int_{0}^{T} f(t)\,\mathrm{d}t`. Use `\,` (thin space) before the differential.
- Use `\left( ... \right)` for delimiters that must scale to their content (fractions, matrices). Do not use `\left( \right)` mechanically — fixed-size `(...)` is better when the content is small.

### 6.8 Spacing in Math Mode

LaTeX's automatic spacing is wrong in a few common cases. Fix them manually:

- `\,` — thin space, before differentials: `f(x)\,\mathrm{d}x`.
- `\;` — medium space, between conditions: `x \in \mathbb{R}\;\text{such that}\;x > 0`.
- `\quad`, `\qquad` — wider gaps for visual separation in piecewise definitions or "for all" qualifiers.
- `\!` — negative thin space, occasionally needed before subscripts on integrals.
- Use `\colon` (not `:`) when colon means "such that" or function-type signature: `f \colon \mathbb{R} \to \mathbb{R}`.

### 6.9 Theorems, Definitions, and Proofs

For thesis chapters with formal results, use `amsthm` environments:

```latex
\newtheorem{theorem}{Theorem}[chapter]
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{proposition}[theorem]{Proposition}
\theoremstyle{definition}
\newtheorem{definition}[theorem]{Definition}
\newtheorem{example}[theorem]{Example}
\theoremstyle{remark}
\newtheorem{remark}[theorem]{Remark}
```

- Use a single shared counter (`[theorem]`) so theorems, lemmas, and definitions share a sequential numbering — easier for readers.
- End proofs with `\begin{proof} ... \end{proof}` (auto-inserts the QED tombstone).
- State theorems precisely: include all hypotheses in the statement, not in surrounding prose.

### 6.10 Common Math-Writing Pitfalls

- **Unbalanced delimiters.** `\left(` must pair with `\right)`. Use `\right.` or `\left.` for invisible counterparts.
- **Mixing notation.** Do not switch between `\mathbf{x}` and `\vec{x}` for the same vector across chapters.
- **Reusing letters.** Do not let `n` mean both "sample count" and "dimensionality" in the same chapter.
- **Implicit summations.** Einstein summation convention is acceptable only if explicitly declared, and only in fields where it is standard.
- **Walls of math without prose.** Every non-trivial equation deserves a sentence of prose explaining what it captures, what is novel, or how it follows from the previous equation.
- **Overusing display equations.** If three short formulas appear in a row as displays, consider running them inline or merging them into an `align` block.
- **Assuming the reader knows your notation.** If in doubt, define it.

---

## 7. Figures and Tables

Figures and tables are first-class content, not decoration. This section is the section of record for figure and table conventions; §3.1 and §5.4 only state the high-level expectation and the float mechanics.

### 7.1 When to Use a Figure vs. a Table vs. Prose

- **Prose** — for one or two values that fit naturally in a sentence ("accuracy improved from 87.2\% to 91.4\%").
- **Table** — for precise numeric comparison, especially when the reader needs exact values, statistical significance, or many metrics at once.
- **Figure (chart)** — for trends, distributions, and qualitative comparisons where the shape matters more than the exact value.
- **Figure (diagram/schematic)** — for system architectures, data flow, hardware layouts, and algorithmic structure.
- Never duplicate the same data in both a table and a figure. Choose the form that best supports the argument and reference it once.

### 7.2 Figure Design

- **File format.** Use vector formats — PDF, EPS, SVG (via the `svg` package or pre-rendered) — for plots, diagrams, and schematics. Use raster (PNG, JPG) only for photographs or screenshots that genuinely contain pixel data. Never embed JPG for line art (compression artifacts on edges).
- **Resolution.** Raster figures should be at least 300~dpi at the printed size.
- **Source files.** Keep the script or source that generated each figure (`*.py`, `*.gnuplot`, `*.tex` with TikZ) inside a `figures/src/` directory. Any figure that cannot be regenerated from source is a liability for revision.
- **Sizing.** Use `\includegraphics[width=0.8\linewidth]{...}` (relative to text width), not absolute centimeters. Single-column figures: `0.8\linewidth`; full-width across both columns of a two-column layout: `\textwidth` inside `figure*`.
- **Typography in figures.** Match the body text font and size where possible. Axis labels and legends should be readable at the printed size — a rule of thumb: if axis tick labels are smaller than the body text, the figure is too dense.
- **Color.** Use a colorblind-safe palette (Viridis, Cividis, ColorBrewer's diverging schemes). Verify legibility in grayscale — many theses are printed in black and white. Distinguish series by **both** color and line style / marker shape so the figure survives photocopying.
- **Avoid chartjunk.** No 3D bar charts for 2D data, no gratuitous gridlines, no decorative shadows, no rainbow colormaps for ordered data.
- **Axes.** Always label both axes with quantity and unit ("Latency (ms)", not just "Latency"). Start the y-axis at zero unless the data genuinely warrants otherwise — if not, indicate the truncation explicitly.
- **Error bars / confidence intervals.** Show them whenever results are aggregated over multiple runs. Caption must specify what they represent (standard deviation, 95\% CI, interquartile range).

### 7.3 Table Design

- **Use `booktabs`.** Three rules — `\toprule`, `\midrule`, `\bottomrule` — and nothing else. Never `\hline`, never vertical bars `|`, never double rules.
- **Alignment.** Left-align text columns, right-align integer columns, decimal-align numeric columns with `siunitx`'s `S` column type. Center-align only for short categorical labels.
- **Units in the header**, not in every cell. "Latency (ms)" in the column header beats "12.3~ms / 14.7~ms / ..." down the column.
- **Significant figures.** Be consistent within a column. Reporting "91.4, 87, 89.23" mixes precisions and looks careless — pick one and stick to it.
- **Highlight the winner.** Bold the best value in each metric column (and tie values), so the reader's eye lands on the comparison conclusion. State the bolding convention in the caption: "Best results in each column are shown in **bold**."
- **Footnotes in tables.** Use `\tnote{}` from `threeparttable`, not `\footnote{}` (which renders at the page bottom and breaks the float).
- **Wide tables.** If a table does not fit the page width: shrink the font with `\small` / `\footnotesize`; rotate with `sidewaystable` from the `rotating` package; or split across multiple tables with shared row labels.
- **Long tables.** For tables that span multiple pages, use `longtable` (cannot be inside `table` float — it manages its own captioning).

### 7.4 Captions

- **Position.** Figure captions go **below** the figure; table captions go **above** the table. This is the IEEE and most-engineering convention. Do not mix.
- **Content.** A caption is a self-contained sentence (or short paragraph). It should let a reader who only skims figures understand what they are looking at without reading the surrounding text.
- **Structure.** Begin with a concise label phrase, then explain. Example: "Figure~3.2: System architecture. The sensor subsystem (left) feeds the kernel scheduler (center), which dispatches tasks to the actuator drivers (right)."
- **Caption length.** Two to four lines is normal. A single five-word caption ("Figure 3.2: System architecture.") is too thin for a thesis.
- **Take-aways belong in the caption** for results figures: "Figure~5.1: Test accuracy across batch sizes. Accuracy plateaus beyond batch size 256, motivating the choice in §5.3."
- **No empty captions.** Every figure and every table must have a caption.

### 7.5 Cross-References

- Reference every figure and table from the body text by **number**, not by position. Write "Figure~3.2 shows...", never "the figure below" or "the table on the next page" — floats move during typesetting.
- Use `~` (non-breaking space) between the word and the number: `Figure~\ref{fig:arch}`, `Table~\ref{tab:results}`.
- Prefer `cleveref`'s `\cref{}` / `\Cref{}` (capitalized at sentence start) — it produces the correct prefix and handles ranges (`\cref{fig:a,fig:b,fig:c}` → "Figures~3.1 to~3.3").
- Every figure and table must be **referenced at least once** from the prose. A figure no one points to does not belong in the thesis.

### 7.6 Placement and Floats

Float mechanics (placement specifiers, `\label`/`\caption` order) are covered in §5.4. A few authoring-level points:

- Place the `\begin{figure}` / `\begin{table}` block **near, but not necessarily adjacent to**, the first prose reference. LaTeX will move it to a good location.
- If LaTeX is starving floats (deferring them to the end), use `\clearpage` at the end of a section to flush pending floats before moving on.

### 7.7 Sub-figures and Sub-tables

- Use `subcaption` (modern; preferred over the older `subfig` package).
- Number with letters: `(a)`, `(b)`, `(c)`. Reference as `Figure~3.2(a)` or `\cref{fig:arch:sub-a}`.
- Each sub-figure deserves its own short caption explaining that panel; the parent caption explains the overall figure.

### 7.8 Reused or Adapted Figures

- A figure copied from another source must include `Source:~\cite{key}` at the end of the caption. Permissions may also be required for non-fair-use reproduction.
- A figure adapted from another source uses `Adapted from~\cite{key}`.
- A figure produced by the author from a public dataset cites the dataset, not the figure: "Data: ImageNet~\cite{deng2009imagenet}."
- Do not paste figures from other papers without attribution — this is plagiarism even when the surrounding prose is original.

### 7.9 Common Figure and Table Pitfalls

- **Screenshots of tables** instead of typeset tables. Always retype tabular data; pixelated table screenshots are a clear sign of laziness to a reviewer.
- **Inconsistent figure styles** across chapters. If Chapter 3's plots use a Viridis colormap and Helvetica labels, Chapter 5's plots should too.
- **Tiny labels.** Axis ticks set to a 6~pt font that becomes illegible when the figure is shrunk to half-column width.
- **Legend overlapping data.** Move the legend outside the plot area or to an empty corner.
- **Bar charts where line charts are needed** (or vice versa). Bar charts compare discrete categories; line charts show trends over a continuous variable.
- **Tables with vertical rules and double horizontal rules.** Hallmarks of a default-LaTeX table that did not get the `booktabs` treatment.
- **Mixing units across rows or columns** without indication ("ms" in one row, "s" in another) — convert to a common unit, or split into separate columns.
- **Captions that just repeat the section text.** Captions complement, not duplicate.
- **Floats stranded at the end of the document** because too many were deferred. Use `\clearpage` strategically.

---

## 8. Quality Verification

Before declaring a section finished, run through this checklist.

- **Language.** Formal, grammatical, free of contractions ("do not", not "don't"), and appropriate for an academic committee.
- **Structure.** Paragraphs are fully developed (typically 3–6 sentences). The section is not a sequence of bullets standing in for prose. Each paragraph has a topic sentence and a clear function in the argument.
- **Consistency.** Acronyms are defined on first use; terminology is uniform; tense and voice are consistent within each section.
- **Citations.** Every non-trivial claim is supported. Every reference in the bibliography is cited at least once in the body, and every in-text citation appears in the bibliography.
- **Technical correctness.** No hallucinated mechanisms, numbers, or APIs. Limitations and assumptions are stated explicitly.
- **The ultimate test.** Does the output read like a real graduation thesis draft — not a blog post, slide deck, marketing copy, or product documentation?

---

## 9. Common Pitfalls to Avoid

- **Bullet-point hell.** Long sequences of bullets are a sign that prose has not been written yet. Convert them to paragraphs unless the content is genuinely enumerative.
- **First-person narration of the thesis process.** "I struggled to choose a framework, but eventually decided..." belongs in a blog post, not a thesis.
- **Vague quantifiers.** "Significantly faster", "much better", "a lot of memory" — replace with measured values or remove.
- **Forward references without grounding.** Do not say "as we will see" if the corresponding section does not yet exist or has not yet been outlined.
- **Marketing tone.** "This thesis presents a novel, powerful, and revolutionary system..." — drop the adjectives; let the results make the case.
- **Translated idioms.** Phrases that read naturally in the author's first language often translate to redundant or awkward English ("it can be said that", "with the aim of", "in order to be able to"). Rewrite the meaning, not the words.

---

## 10. Worked Example

**Rough note (input):**

> chap 3 — explain why we use FreeRTOS. it's small, real-time, open source, popular for embedded. fits cortex-m4. we picked it over zephyr because zephyr is too heavy.

**Polished thesis prose (output):**

> The proposed system is built on top of FreeRTOS, an open-source real-time operating system widely adopted in resource-constrained embedded environments [1]. FreeRTOS was selected for three reasons. First, its kernel footprint — under 10~kB on ARM Cortex-M targets — is compatible with the memory budget of the Cortex-M4 platform used in this work. Second, its preemptive scheduler provides the deterministic latency guarantees required by the real-time constraints described in Section~3.1. Third, its permissive MIT license imposes no obligations that would conflict with the deployment scenario considered in this thesis.
>
> Zephyr was considered as an alternative and rejected. Although Zephyr offers a richer driver ecosystem, its baseline RAM requirement exceeds the available SRAM on the target microcontroller, and its build complexity introduces overhead disproportionate to the scope of this project.

Notice how the polished version: defines the acronym, supports each design choice with a concrete reason, references prior sections, cites a source for the popularity claim, and treats the rejected alternative with neutral, evidence-based language rather than the dismissive "too heavy".
