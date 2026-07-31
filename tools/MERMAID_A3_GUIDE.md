# Mermaid A3 One-Pager Guide

How to build a one-page A3 landscape PDF with 4 mermaid diagrams in a 2x2
grid (stakeholder/money/labor-flow style docs). Companion to
`PDF_CONVERSION_GUIDE.md` (that one is for plain markdown docs; this one is
for hand-built HTML pages with live mermaid diagrams arranged in a print grid).

## Why this exists

`convert_md_to_pdf.js` renders a single markdown flow start-to-finish and
picks page breaks for you. A 4-diagram business one-pager needs each diagram
to land in its own quadrant, at a consistent size, with lines/text that
actually read on paper — that requires direct control over the grid layout
and the mermaid render, which this guide + `render_mermaid_a3.js` provide.

## The pieces

- **`mermaid.min.js`** (v9.4.3, already in this folder) — loaded via a plain
  `<script src="../../tools/mermaid.min.js">` tag, no CDN, works offline over
  `file://`. Do not upgrade this version (see Gotchas below).
- **A hand-written HTML file** — one A3 page (`420mm x 297mm`), a 2x2 CSS
  grid of `.cell` boxes, each with a `<pre class="mermaid">...</pre>` block.
- **`render_mermaid_a3.js`** — drives headless Chrome to render the page
  properly and print it to PDF. Always use this instead of the CLI
  `google-chrome --print-to-pdf` flag (see Gotchas: race condition).

## Quick start: adding a new A3 one-pager

1. Copy an existing file as your template — `docs/meetings/mitsue_kanko_collaboration_diagrams_a3.html`
   or `mitsue_kanko_forest_led_diagrams_a3.html` are both known-good.
2. Keep the `<style>` block and the closing `<script>` block exactly as-is —
   that's the grid CSS and the fit-to-cell scaling logic. Only edit:
   - the header title/subtitle
   - the 4 `<div class="cell d1">` ... `<div class="cell d4">` blocks (each
     has an `<h2>`, `<div class="h2sub">`, and a `<pre class="mermaid">`)
3. Validate the mermaid syntax before rendering (catches typos in seconds
   instead of debugging a blank PDF panel):
   ```bash
   node tools/validate_mermaid.js docs/meetings/your_file_a3.html
   ```
4. Render:
   ```bash
   node tools/render_mermaid_a3.js docs/meetings/your_file_a3.html
   ```
5. Read the console output. It prints the **shared scale** (0-1) and each
   diagram's own-fit scale. If shared scale < 0.5, text will look small on
   paper — see "Getting the scale up" below.

## How the sizing actually works

Each of the 4 diagrams has a natural pixel size (`viewBox`) determined by
mermaid's layout engine. Each `.cell` has a fixed pixel size determined by
the CSS grid (roughly `724 x 425` for a 2x2 grid on A3 after header/legend/
padding). For each diagram, `own-fit scale = min(cellW/vbW, cellH/vbH)`.

If we scaled every diagram independently to max out its own cell, boxes and
text would come out different physical sizes per section — the diagram with
the least content would render huge, the busiest one tiny. Diagrams should
look like one coherent page, so instead we take **one shared scale = the
minimum own-fit scale across all four diagrams** and apply it to every
diagram. Diagrams with room to spare just get extra whitespace instead of
extra zoom.

This means **the busiest diagram sets the ceiling for the whole page.** If
one diagram is much bigger than the other three, the shared scale collapses
and everything looks small — even diagrams that would've fit fine on their
own.

## Getting the scale up (when it's below ~0.5)

In order of effort:

1. **Trim edge-label text.** Mermaid's dagre layout widens ranks to fit label
   text, so a label like `"proposed living-lab research, student program - Phase 0"`
   directly makes the diagram wider. Cut labels to 2-5 words. This was the
   single biggest lever in practice.
2. **Tighten the densest diagram's spacing** via an inline init directive at
   the top of that diagram's mermaid block:
   ```
   %%{init: {'flowchart': {'nodeSpacing': 6, 'rankSpacing': 22, 'padding': 3, 'useMaxWidth': false}}}%%
   ```
   Lower `nodeSpacing`/`rankSpacing`/`padding` shrinks the diagram's natural
   `viewBox` directly. This alone took one diagram from viewBox 1447x1088
   down to 1045x716 and raised the page's shared scale from 0.39 to 0.59.
   `useMaxWidth: false` is required — without it mermaid forces its own
   `width:100%` + inline `max-width:Npx` styling that fights the fit script.
3. **Don't fight the grid with row-height tricks.** It's tempting to give the
   busiest diagram a bigger cell (e.g. a 3-row layout with one full-width
   row). In practice the fixed per-cell header text (`h2` + `h2sub`, ~40px)
   eats a disproportionate share of small cells, and re-deriving the optimal
   split by hand is a time sink for a small gain. Tightening the diagram's
   own spacing (#2 above) was consistently more effective than reshaping the
   grid. A plain 2x2 grid with `grid-template-areas: "d1 d2" "d3 d4"` is the
   default; don't reach for anything fancier unless #1 and #2 are exhausted.
4. **`direction LR`/`TB` inside a `subgraph` does nothing in mermaid 9.4.3.**
   Don't spend time trying to reshape a cluster's internal layout this way —
   the old renderer silently ignores it. (Confirmed empirically: viewBox was
   byte-for-byte identical with and without the directive.)

## Known gotchas (all cost real debugging time — check these first)

- **`—` (em dash) and `&` inside edge labels crash the old mermaid parser**
  with a generic "Syntax error in graph" bomb icon and no useful message in
  the browser. Regular hyphens (`-`) and the word "and" work fine. This is
  the #1 cause of a diagram silently failing to render — if you see the bomb
  icon, grep your mermaid block for `—` and `&` first.
- **`grid-area: dN` rules with no matching `grid-template-areas` string
  create phantom implicit grid tracks** and silently stack all 4 diagrams on
  top of each other (they'll all report identical `clientWidth`/`clientHeight`
  if you inspect them). If you change the grid layout, make sure every
  `.cell.dN { grid-area: dN; }` rule has a corresponding cell name inside
  `grid-template-areas` — delete orphaned rules immediately when you remove
  a layout variant.
- **The fit-to-cell JS races mermaid's async render if you run it inline
  right after `mermaid.init()`.** In a plain browser load this sometimes
  works (v9.4.3's init is often synchronous) but it is not reliable — under
  puppeteer with `--print-to-pdf` from the CLI it reliably fails silently
  (`svg.style.width` stays empty, diagrams render at raw unscaled size and
  overflow their cells). Always render via `render_mermaid_a3.js`, which
  explicitly waits for `container.querySelector('svg')` to exist on every
  `.diagram` before touching anything.
- **Don't upgrade `mermaid.min.js` past v9.x.** v10+ requires
  `structuredClone`, which the Chromium bundled with the markdown-pdf
  extension doesn't support (this bit the markdown-PDF pipeline too — see
  `PDF_CONVERSION_GUIDE.md`).
- **Yen signs (`¥`) are fine, em dashes are not.** Japanese text and most
  punctuation renders without issue — it's specifically `—` and `&` inside
  `|edge labels|` that break the lexer.

## Validating diagrams before rendering

`tools/validate_mermaid.js` extracts every `<pre class="mermaid">` block from
an HTML file and asks mermaid to parse it (no PDF render, no page.pdf() cost)
— catches syntax errors in seconds:

```bash
node tools/validate_mermaid.js docs/meetings/your_file_a3.html
```

Exits non-zero if any diagram fails, prints the parser's error message
(usually points straight at the offending character).

## File naming convention

For a topic `X`, keep two files side by side:
- `X.html` — on-screen version, single column, mermaid's own default scaling
  (via `theme:'default'`, no custom fit script needed — it self-scales to
  the browser window fine for one-diagram-at-a-time viewing).
- `X_a3.html` / `X_a3.pdf` — the 4-diagram print one-pager described here.

---
*Last updated: 2026-08-01*
