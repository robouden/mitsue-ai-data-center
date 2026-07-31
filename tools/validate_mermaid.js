#!/usr/bin/env node
'use strict';

// =============================================================================
// MERMAID SYNTAX VALIDATOR — see tools/MERMAID_A3_GUIDE.md
//
// Command:
//   node validate_mermaid.js <file.html> [file2.html ...]
//
// Extracts every <pre class="mermaid">...</pre> block from each HTML file
// and asks mermaid itself to parse it, without rendering a PDF. Catches
// syntax errors (most commonly: em dashes or "&" inside |edge labels|,
// which mermaid 9.4.3 chokes on) in seconds instead of debugging a blank
// PDF panel.
// =============================================================================

const fs = require('fs');
const path = require('path');

const EXT = '/home/rob/.antigravity/extensions/yzane.markdown-pdf-1.5.0-universal';
const NM  = path.join(EXT, 'node_modules');
const puppeteer = require(path.join(NM, 'puppeteer-core'));

const MERMAID_JS = path.join(__dirname, 'mermaid.min.js');
const CHROME = '/usr/bin/google-chrome';

async function validateOne(browser, file) {
  const html = fs.readFileSync(file, 'utf8');
  const blocks = [...html.matchAll(/<pre class="mermaid">\n([\s\S]*?)<\/pre>/g)].map((m) => m[1]);

  console.log(`\n${path.basename(file)} - found ${blocks.length} diagram(s)`);
  if (!blocks.length) return true;

  const page = await browser.newPage();
  await page.goto('about:blank');
  await page.addScriptTag({ path: MERMAID_JS });

  let allOk = true;
  for (let i = 0; i < blocks.length; i++) {
    const result = await page.evaluate(async (text) => {
      try {
        await window.mermaid.mermaidAPI.parse(text);
        return { ok: true };
      } catch (e) {
        return { ok: false, err: e.message.slice(0, 300) };
      }
    }, blocks[i]);

    if (result.ok) {
      console.log(`  diagram ${i + 1}: OK`);
    } else {
      allOk = false;
      console.log(`  diagram ${i + 1}: FAILED`);
      console.log(`    ${result.err.replace(/\n/g, '\n    ')}`);
    }
  }
  await page.close();
  return allOk;
}

async function main() {
  const files = process.argv.slice(2);
  if (!files.length) {
    console.error('Usage: node validate_mermaid.js <file.html> [file2.html ...]');
    process.exit(1);
  }

  const browser = await puppeteer.launch({
    executablePath: CHROME,
    args: ['--no-sandbox', '--disable-gpu'],
  });

  let allOk = true;
  try {
    for (const f of files) {
      if (!fs.existsSync(f)) {
        console.error(`Skipping ${f}: not found`);
        allOk = false;
        continue;
      }
      const ok = await validateOne(browser, f);
      allOk = allOk && ok;
    }
  } finally {
    await browser.close();
  }

  process.exit(allOk ? 0 : 1);
}

main();
