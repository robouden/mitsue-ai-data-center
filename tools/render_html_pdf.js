#!/usr/bin/env node
'use strict';

// =============================================================================
// PLAIN HTML -> PDF RENDERER (for flowing multi-section pages, not the A3
// one-pager grid template — see render_mermaid_a3.js for that).
//
// Command:
//   node render_html_pdf.js <file.html> [file2.html ...]
//
// Loads the HTML in headless Chrome, waits for every .diagram container to
// contain a rendered mermaid <svg>, then prints to <file>.pdf (A3 landscape,
// same directory). Relies on the page's own @media print CSS to handle wide
// diagrams (see .diagram-wide rules in mitsue_kanko_collaboration_diagrams*.html).
// =============================================================================

const path = require('path');

const EXT = '/home/rob/.antigravity/extensions/yzane.markdown-pdf-1.5.0-universal';
const NM = path.join(EXT, 'node_modules');
const puppeteer = require(path.join(NM, 'puppeteer-core'));

const CHROME = '/usr/bin/google-chrome';

async function renderOne(htmlPath) {
  const absHtml = path.resolve(htmlPath);
  const outPdf = absHtml.replace(/\.html?$/i, '.pdf');
  const fileUrl = 'file://' + absHtml;

  const browser = await puppeteer.launch({
    executablePath: CHROME,
    args: ['--no-sandbox', '--disable-gpu'],
  });
  try {
    const page = await browser.newPage();
    await page.goto(fileUrl, { waitUntil: 'networkidle0' });

    await page.waitForFunction(() => {
      const containers = document.querySelectorAll('.diagram');
      if (!containers.length) return false;
      return Array.from(containers).every((c) => c.querySelector('svg'));
    }, { timeout: 15000 });

    await page.pdf({
      path: outPdf,
      format: 'A3',
      landscape: true,
      printBackground: true,
      margin: { top: '10mm', bottom: '10mm', left: '10mm', right: '10mm' },
    });
    console.log(`OK  -> ${outPdf}`);
  } catch (err) {
    console.error(`FAILED ${htmlPath}: ${err.message}`);
    process.exitCode = 1;
  } finally {
    await browser.close();
  }
}

(async () => {
  const files = process.argv.slice(2);
  if (!files.length) {
    console.error('Usage: node render_html_pdf.js <file.html> [file2.html ...]');
    process.exit(1);
  }
  for (const f of files) {
    await renderOne(f);
  }
})();
