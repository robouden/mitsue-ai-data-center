# PDF Conversion Guide

This document outlines the standardized process for converting Markdown (`.md`) files to PDF in the Mitsue Village Project AI Data Center.

## Why This Method?
We use a custom Node.js script (`convert_md_to_pdf.js`) powered by Puppeteer and the `markdown-pdf` extension. This method was chosen over alternatives (like Pandoc + LaTeX) because it provides:
1. **Superior Visual Fidelity**: Retains custom CSS styling, fonts, and Typora theme compatibility.
2. **Reliable CJK (Japanese) Text Wrapping**: Solves the critical issue of Japanese text overflowing table boundaries, which is a known limitation in standard LaTeX `tabular` environments.

## Prerequisites
- Node.js installed on the system.
- The `yzane.markdown-pdf` extension installed (located at `~/.antigravity/extensions/yzane.markdown-pdf-1.5.0-universal`).

## The Japanese Table Fix (Critical)
The script includes a `PRINT_OVERRIDE` CSS constant that enforces strict line-breaking rules specifically for table cells. This prevents long Japanese strings from breaking the layout. The critical CSS rules applied to `table th, table td` are:
```css
line-break: anywhere !important;
word-wrap: break-word !important;
overflow-wrap: break-word !important;
word-break: break-all !important;
```

## Mermaid Diagram Support
The script natively supports rendering Mermaid.js diagrams (e.g., flowcharts, sequence diagrams) from ````mermaid` code blocks. 
- It uses a local copy of `mermaid.min.js` (v9.4.3) to avoid browser security restrictions on `file://` protocol CDN loading.
- Version 9.x is specifically used because newer versions (v10+) require `structuredClone`, which is not supported by the older Chromium engine bundled with the extension.
- The script intercepts Mermaid code blocks and wraps them in `<div class="mermaid">`, then waits 3 seconds for the SVG rendering to complete before generating the PDF.

## Standard Workflow

### Step 1: Update Document Headers
Before converting, always ensure the document's version and date are up to date. Run the header update script:
```bash
python3 update_doc_headers.py
```
*This script automatically increments the version number and sets the "Last modified" date to the current date (e.g., `2026-06-05`) in the HTML header of all `.md` files.*

### Step 2: Convert to PDF
Run the conversion script. You can target specific files or convert all Markdown files in the directory.

**Convert specific files:**
```bash
node convert_md_to_pdf.js file1.md file2.md
```

**Convert all Markdown files in the directory:**
```bash
node convert_md_to_pdf.js --all
```

## Troubleshooting
- **Japanese text still overflowing?** Verify that `convert_md_to_pdf.js` contains the `PRINT_OVERRIDE` CSS rules mentioned above. Do not remove or alter these rules.
- **Script fails to run?** Ensure Node.js is installed and the `markdown-pdf` extension path is correct in the script's configuration.
- **Need smaller file sizes?** A fallback script (`convert_md_to_pdf_pandoc.py`) exists using Pandoc + `xelatex`, but it may lose custom CSS styling and requires manual `tabularx` configuration for Japanese tables. Use only if file size is a strict constraint and visual fidelity is secondary.

---
*Last updated: 2026-06-05*