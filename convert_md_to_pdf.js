#!/usr/bin/env node
'use strict';

// Batch markdown-to-PDF converter using the yzane.markdown-pdf extension's own
// node_modules and bundled Chromium — no extra installs needed.

const path = require('path');
const fs = require('fs');
const os = require('os');

const EXT = '/home/rob/.antigravity/extensions/yzane.markdown-pdf-1.5.0-universal';
const NM  = path.join(EXT, 'node_modules');

const markdownIt  = require(path.join(NM, 'markdown-it'));
const hljs        = require(path.join(NM, 'highlight.js'));
const cheerio     = require(path.join(NM, 'cheerio'));
const mustache    = require(path.join(NM, 'mustache'));
const puppeteer   = require(path.join(NM, 'puppeteer-core'));

// Extension assets
const TEMPLATE = fs.readFileSync(path.join(EXT, 'template', 'template.html'), 'utf8');
const CSS_MD   = fs.readFileSync(path.join(EXT, 'styles', 'markdown.css'), 'utf8');
const CSS_PDF  = fs.readFileSync(path.join(EXT, 'styles', 'markdown-pdf.css'), 'utf8');
const CSS_HL   = fs.readFileSync(path.join(EXT, 'styles', 'tomorrow.css'), 'utf8');

const STYLE_BLOCK = `<style>\n${CSS_HL}\n${CSS_MD}\n${CSS_PDF}\n</style>`;

function convertMarkdownToHtml(mdFile, text) {
  const md = markdownIt({
    html: true,
    breaks: false,
    highlight: (str, lang) => {
      if (lang && hljs.getLanguage(lang)) {
        try {
          return '<pre class="hljs"><code><div>' +
            hljs.highlight(lang, str, true).value +
            '</div></code></pre>';
        } catch (_) {}
      }
      return '<pre class="hljs"><code><div>' + md.utils.escapeHtml(str) + '</div></code></pre>';
    }
  });

  // Fix image paths to absolute file:// URLs
  const defaultRender = md.renderer.rules.image;
  md.renderer.rules.image = (tokens, idx, options, env, self) => {
    const token = tokens[idx];
    let href = token.attrs[token.attrIndex('src')][1];
    if (href && !href.startsWith('http') && !href.startsWith('data:')) {
      href = 'file://' + path.resolve(path.dirname(mdFile), href);
      token.attrs[token.attrIndex('src')][1] = href;
    }
    return defaultRender(tokens, idx, options, env, self);
  };

  // Fix img src in raw HTML blocks too
  md.renderer.rules.html_block = (tokens, idx) => {
    const html = tokens[idx].content;
    const $ = cheerio.load(html);
    $('img').each(function () {
      const src = $(this).attr('src');
      if (src && !src.startsWith('http') && !src.startsWith('data:')) {
        $(this).attr('src', 'file://' + path.resolve(path.dirname(mdFile), src));
      }
    });
    return $.html();
  };

  return md.render(text);
}

async function convertToPdf(mdFile) {
  const text = fs.readFileSync(mdFile, 'utf8');
  const title = path.basename(mdFile, '.md');
  const content = convertMarkdownToHtml(mdFile, text);

  const html = mustache.render(TEMPLATE, {
    title,
    style: STYLE_BLOCK,
    mermaid: '',
    content
  });

  const tmpFile = path.join(os.tmpdir(), title + '_tmp.html');
  fs.writeFileSync(tmpFile, html, 'utf8');

  const browser = await puppeteer.launch({
    executablePath: puppeteer.executablePath(),
    args: ['--no-sandbox', '--disable-setuid-sandbox']
  });

  try {
    const page = await browser.newPage();
    await page.setDefaultTimeout(0);
    await page.goto('file://' + tmpFile, { waitUntil: 'networkidle0' });

    const pdfFile = mdFile.replace(/\.md$/, '.pdf');
    await page.pdf({
      path: pdfFile,
      format: 'A4',
      printBackground: true,
      margin: { top: '1.5cm', right: '1.5cm', bottom: '1.5cm', left: '1.5cm' },
      timeout: 0
    });

    console.log('  OK:', path.basename(pdfFile));
    return pdfFile;
  } finally {
    await browser.close();
    fs.unlinkSync(tmpFile);
  }
}

async function main() {
  const args = process.argv.slice(2);
  if (args.length === 0) {
    console.error('Usage: node convert_md_to_pdf.js <file.md> [file2.md ...]');
    console.error('       node convert_md_to_pdf.js --all   (convert all .md in cwd)');
    process.exit(1);
  }

  let files;
  if (args[0] === '--all') {
    const dir = process.cwd();
    files = fs.readdirSync(dir)
      .filter(f => f.endsWith('.md') && !f.startsWith('convert_'))
      .map(f => path.join(dir, f));
  } else {
    files = args.map(f => path.resolve(f));
  }

  console.log(`Converting ${files.length} file(s) to PDF...`);
  let ok = 0, fail = 0;
  for (const f of files) {
    process.stdout.write('  ' + path.basename(f) + ' ... ');
    try {
      await convertToPdf(f);
      ok++;
    } catch (err) {
      console.log('FAIL:', err.message);
      fail++;
    }
  }
  console.log(`\nDone: ${ok} converted, ${fail} failed.`);
}

main().catch(e => { console.error(e); process.exit(1); });
