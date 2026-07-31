#!/usr/bin/env node
'use strict';

// =============================================================================
// MERMAID A3 ONE-PAGER RENDERER — see tools/MERMAID_A3_GUIDE.md for the full
// process this automates (grid template, uniform-scale trick, known gotchas).
//
// Command:
//   node render_mermaid_a3.js <file.html> [file2.html ...]
//
// What it does, per file:
//   1. Loads the HTML in headless Chrome (via the markdown-pdf extension's
//      bundled puppeteer-core — no extra npm install needed).
//   2. Waits for every .diagram container to actually contain a rendered
//      mermaid <svg> (avoids the classic race condition where the fit-scale
//      script runs before mermaid.init() has finished).
//   3. Re-applies the "one shared scale" fit: measures each diagram's
//      viewBox against its own .diagram cell, takes the SMALLEST scale
//      needed across all diagrams on the page, and applies that one scale
//      to every diagram — so boxes/text render at the same physical size
//      everywhere instead of each diagram independently maxing out its cell.
//   4. Prints to <file>.pdf in the same directory, A3 landscape.
//
// The HTML file must already contain the matching inline script (see the
// template referenced in MERMAID_A3_GUIDE.md) — this script's job is just to
// drive Chrome reliably and log the computed scale so you can judge whether
// diagram content needs trimming.
// =============================================================================

const path = require('path');
const fs = require('fs');

const EXT = '/home/rob/.antigravity/extensions/yzane.markdown-pdf-1.5.0-universal';
const NM  = path.join(EXT, 'node_modules');
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

    const info = await page.evaluate(() => {
      var items = [];
      document.querySelectorAll('.diagram').forEach(function (container) {
        var svg = container.querySelector('svg');
        if (!svg) return;
        var vb = (svg.getAttribute('viewBox') || '').split(/\s+/).map(Number);
        if (vb.length < 4 || !vb[2] || !vb[3]) return;
        items.push({ svg: svg, vbW: vb[2], vbH: vb[3], cw: container.clientWidth, ch: container.clientHeight });
      });
      if (!items.length) return { scale: null, items: [] };
      var scale = Math.min.apply(null, items.map(function (it) {
        return Math.min(it.cw / it.vbW, it.ch / it.vbH);
      }));
      items.forEach(function (it) {
        it.svg.style.width = (it.vbW * scale) + 'px';
        it.svg.style.height = (it.vbH * scale) + 'px';
        it.svg.style.maxWidth = 'none';
        it.svg.style.display = 'block';
        it.svg.style.margin = '0 auto';
      });
      return {
        scale: scale,
        items: items.map(function (it) { return { vbW: it.vbW, vbH: it.vbH, cw: it.cw, ch: it.ch }; }),
      };
    });

    await page.pdf({
      path: outPdf,
      format: 'A3',
      landscape: true,
      printBackground: true,
      margin: { top: 0, bottom: 0, left: 0, right: 0 },
    });

    console.log(`\n${path.basename(htmlPath)} -> ${path.basename(outPdf)}`);
    console.log(`  shared scale: ${info.scale ? info.scale.toFixed(3) : 'n/a'}`);
    if (info.scale !== null && info.scale < 0.5) {
      console.log('  WARNING: scale below 0.5 — text will look small on paper.');
      console.log('  Fix: trim edge-label text, or tighten the densest diagram\'s');
      console.log('  %%{init: {\'flowchart\': {\'nodeSpacing\':.., \'rankSpacing\':.., \'padding\':..}}}%% directive.');
    }
    info.items.forEach(function (it, i) {
      const s = Math.min(it.cw / it.vbW, it.ch / it.vbH);
      console.log(`  diagram ${i + 1}: viewBox ${Math.round(it.vbW)}x${Math.round(it.vbH)}, cell ${it.cw}x${it.ch}, own-fit scale ${s.toFixed(3)}`);
    });
  } finally {
    await browser.close();
  }
}

async function main() {
  const files = process.argv.slice(2);
  if (!files.length) {
    console.error('Usage: node render_mermaid_a3.js <file.html> [file2.html ...]');
    process.exit(1);
  }
  for (const f of files) {
    if (!fs.existsSync(f)) {
      console.error(`Skipping ${f}: not found`);
      continue;
    }
    await renderOne(f);
  }
}

main();
