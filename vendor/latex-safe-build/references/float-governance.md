# Float governance

Settings and fixes, proven in long use on a large figure-heavy document, for the
three float problems that quietly degrade large documents. Apply when diagnosing
layout complaints, not preemptively on documents that look fine.

## Preamble block: make placement deterministic

```latex
% No float may appear before its first in-text reference.
\usepackage{flafter}
% Keep floats inside their own section.
\usepackage[section]{placeins}
% Provides the [H] placement used in the fixes below.
\usepackage{float}
% Let pages be mostly-float instead of pushing floats to the end.
\renewcommand{\topfraction}{0.85}
\renewcommand{\bottomfraction}{0.7}
\renewcommand{\textfraction}{0.1}
\renewcommand{\floatpagefraction}{0.75}
\setcounter{topnumber}{3}
\setcounter{bottomnumber}{2}
\setcounter{totalnumber}{5}
% For the orphan fixes below.
\usepackage{needspace}
```

Why the fractions matter: LaTeX's defaults refuse to place a float on a page unless
the page keeps a large text share, so big figures drift chapters away from their
references. Relaxing the fractions lets a page be 75 to 85 percent float, which is
what a figure-heavy engineering document needs.

For hard chapter boundaries, add `\FloatBarrier` (from `placeins`) at each chapter
end, or use a class hook so it happens automatically.

## Fix: a section renders as a bare heading

A section whose entire body is one `[htbp]` float renders as a lonely heading,
because the float drifts onward while the heading stays. Put `\FloatBarrier`
immediately **before** that `\section` so the previous section's floats flush, then
keep the float with its heading:

```latex
\FloatBarrier
\section{Results}
\begin{figure}[H] ... \end{figure}
```

## Fix: a single figure stranded alone on a page

The orphan-figure page pattern. Force the figure to stay with its paragraph:

```latex
\FloatBarrier
\Needspace{16\baselineskip}
\begin{figure}[H]
  ...
\end{figure}
```

`\Needspace{16\baselineskip}` starts a fresh page early only when fewer than 16
lines remain, so the figure and its intro paragraph move together instead of
splitting. Tune the multiplier to roughly the figure height in lines.
