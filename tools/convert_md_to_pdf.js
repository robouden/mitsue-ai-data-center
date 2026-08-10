#!/usr/bin/env node
'use strict';

// =============================================================================
// PDF CONVERSION — ALWAYS USE THIS SCRIPT
// =============================================================================
// Command:
//   node convert_md_to_pdf.js --theme=github <file.md> [file2.md ...]
//   node convert_md_to_pdf.js --theme=github --all   (all .md files in cwd)
//
// Why this script:
//   Uses puppeteer + Typora github theme (Open Sans font, correct styling).
//   DO NOT use pandoc, weasyprint, or any other tool — they produce different
//   fonts and layout that do not match the project's visual standard.
//
// Page-size control (for 2-page A4 docs):
//   Add a <style> block at the top of the .md file:
//
//     <style>
//       html { font-size: 10.5px !important; }
//       body { line-height: 1.3 !important; }
//       p, blockquote, ul, ol, dl, table { margin: 5px 0 !important; }
//       h1, h2, h3, h4, h5, h6 { margin-top: 6px !important; margin-bottom: 3px !important; }
//       hr { margin: 6px 0 !important; }
//       .page-break { page-break-after: always; break-after: page; height: 0; margin: 0; padding: 0; }
//     </style>
//
//   To force a page break at a specific point, insert:
//     <div class="page-break"></div>
//
//   Tune font-size (10–11px range) to hit exactly 2 pages.
//   10.5px = 2 pages for the current government onepager content.
// =============================================================================

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

// Typora theme support: --theme=<name> wraps content in #write and prepends the theme CSS
const THEMES_DIR = path.join(os.homedir(), '.config/Typora/themes');

function loadTyporaTheme(name) {
  const cssPath = path.join(THEMES_DIR, name + '.css');
  if (!fs.existsSync(cssPath)) {
    throw new Error(`Typora theme not found: ${cssPath}`);
  }
  let css = fs.readFileSync(cssPath, 'utf8');
  // Strip Typora-specific @include-when-export (we use the bundled local woff2 instead)
  css = css.replace(/@include-when-export[^;]*;\s*/g, '');
  // Resolve relative url(./...) paths to absolute file:// so puppeteer can load assets
  css = css.replace(/url\(\s*['"]?\.\/([^'")]+)['"]?\s*\)/g, (_, rel) =>
    `url('file://${path.join(THEMES_DIR, rel)}')`
  );
  return css;
}

// Counter the theme's screen-oriented #write padding (Typora itself bypasses this on export).
// Table: force full content width + CJK line breaking to prevent Japanese text overflow.
const PRINT_OVERRIDE = `
  html, body { margin: 0; padding: 0; }
  #write { max-width: none !important; margin: 0 !important; padding: 0 !important; }
  table { width: 100% !important; table-layout: fixed !important; border-collapse: collapse !important; border-spacing: 0 !important; }
  table th, table td { 
    padding: 2px 6px !important; 
    word-wrap: break-word !important; 
    overflow-wrap: break-word !important; 
    line-break: anywhere !important; /* Critical for CJK/Japanese table wrapping */
    word-break: break-all !important;
  }
`;

function buildStyleBlock(themeName) {
  if (themeName) {
    const themeCss = loadTyporaTheme(themeName);
    return `<style>\n${CSS_HL}\n${themeCss}\n${PRINT_OVERRIDE}\n</style>`;
  }
  return `<style>\n${CSS_HL}\n${CSS_MD}\n${CSS_PDF}\n</style>`;
}

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

  // Resolve a relative asset ref against the md file's own dir first, then fall
  // back to the repo root (cwd). Lets docs live in nested folders (docs/<theme>/)
  // while still referencing shared root-anchored paths like assets/… .
  const resolveAsset = (href) => {
    const local = path.resolve(path.dirname(mdFile), href);
    if (fs.existsSync(local)) return local;
    const fromRoot = path.resolve(process.cwd(), href);
    if (fs.existsSync(fromRoot)) return fromRoot;
    return local; // keep original resolution if neither exists
  };

  // Fix image paths to absolute file:// URLs
  const defaultRender = md.renderer.rules.image;
  md.renderer.rules.image = (tokens, idx, options, env, self) => {
    const token = tokens[idx];
    let href = token.attrs[token.attrIndex('src')][1];
    if (href && !href.startsWith('http') && !href.startsWith('data:')) {
      href = 'file://' + resolveAsset(href);
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
        $(this).attr('src', 'file://' + resolveAsset(src));
      }
    });
    return $.html();
  };

  // Render mermaid code blocks as <div class="mermaid"> for the library to pick up
  const defaultFence = md.renderer.rules.fence;
  md.renderer.rules.fence = (tokens, idx, options, env, self) => {
    const token = tokens[idx];
    if (token.info.trim() === 'mermaid') {
      return `<div class="mermaid">\n${token.content}\n</div>\n`;
    }
    return defaultFence(tokens, idx, options, env, self);
  };

  return md.render(text);
}

// For .html brochures: use system Chrome + modern puppeteer for correct page size
const SYSTEM_CHROME = '/usr/bin/google-chrome';
const NEW_PUPPETEER = '/tmp/pup-brochure/node_modules/puppeteer-core';

async function convertHtmlToPdf(htmlFile) {
  const pup = require(NEW_PUPPETEER);
  const pdfFile = htmlFile.replace(/\.html$/, '.pdf');
  const browser = await pup.launch({
    executablePath: SYSTEM_CHROME,
    args: ['--no-sandbox', '--disable-setuid-sandbox']
  });
  try {
    const page = await browser.newPage();
    await page.goto('file://' + htmlFile, { waitUntil: 'networkidle0', timeout: 30000 });
    await page.pdf({ path: pdfFile, printBackground: true, preferCSSPageSize: true });
    console.log('  OK:', path.basename(pdfFile));
    return pdfFile;
  } finally {
    await browser.close();
  }
}

function todayLocal() {
  const d = new Date();
  const pad = n => String(n).padStart(2, '0');
  return `${d.getFullYear()}-${pad(d.getMonth() + 1)}-${pad(d.getDate())}`;
}

// Ensure the .md carries a version/date the running-header regex can read.
// If absent, inject an invisible HTML comment (v1.0 + today) and write it back
// to disk — placed after a leading <style> block if present, else at the top.
// The filename always appears in the running header, so only version+date go here.
function ensureHeader(mdFile, text) {
  const hasVersion = /Version:\s*v[\d.]+/.test(text) || /["'>]v\d+\.\d+[\d.]*</.test(text);
  if (hasVersion) return text;

  const header = `<!-- Version: v1.0 | Last modified: ${todayLocal()} -->`;
  const styleEnd = text.match(/<\/style>\s*?\n/i);
  let updated;
  if (styleEnd) {
    const idx = styleEnd.index + styleEnd[0].length;
    updated = text.slice(0, idx) + '\n' + header + '\n' + text.slice(idx);
  } else {
    updated = header + '\n\n' + text;
  }
  fs.writeFileSync(mdFile, updated, 'utf8');
  console.log(`  (added header to ${path.basename(mdFile)})`);
  return updated;
}

async function convertToPdf(mdFile, opts = {}) {
  // Route .html files to the HTML→PDF path
  if (mdFile.endsWith('.html')) return convertHtmlToPdf(path.resolve(mdFile));

  const text = ensureHeader(mdFile, fs.readFileSync(mdFile, 'utf8'));
  const title = path.basename(mdFile, '.md');
  const rendered = convertMarkdownToHtml(mdFile, text);
  // Typora theme styles target #write; wrap content so they apply.
  const content = opts.theme ? `<div id="write" class="is-node">${rendered}</div>` : rendered;

  const html = mustache.render(TEMPLATE, {
    title,
    style: buildStyleBlock(opts.theme),
    mermaid: `<script src="file://${path.join(__dirname, 'mermaid.min.js')}"></script>
<script>
  if (typeof mermaid !== 'undefined') {
    mermaid.initialize({ startOnLoad: false, theme: 'default' });
    document.addEventListener('DOMContentLoaded', async () => {
      try {
        await mermaid.run();
      } catch (e) {
        console.error("Mermaid run failed:", e);
      }
    });
  }
</script>`,
    content
  });

  const tmpFile = path.join(os.tmpdir(), title + '_tmp.html');
  fs.writeFileSync(tmpFile, html, 'utf8');

  const versionMatch = text.match(/Version:\s*(v[\d.]+)/) || text.match(/["'>](v\d+\.\d+[\d.]*)</);
  const dateMatch = text.match(/Last modified:\s*([\d-]+)/) || text.match(/["'>](\d{4}-\d{2}-\d{2})</);
  const headerText = [
    path.basename(mdFile),
    versionMatch ? `Version: ${versionMatch[1]}` : '',
    dateMatch ? `Last modified: ${dateMatch[1]}` : ''
  ].filter(Boolean).join(' &nbsp;|&nbsp; ');

  const browser = await puppeteer.launch({
    executablePath: puppeteer.executablePath(),
    args: ['--no-sandbox', '--disable-setuid-sandbox', '--disable-web-security']
  });

  try {
    const page = await browser.newPage();
    await page.setDefaultTimeout(0);
    await page.goto('file://' + tmpFile, { waitUntil: 'networkidle0' });

    // Wait for Mermaid to finish rendering
    await new Promise(resolve => setTimeout(resolve, 3000));

    const pdfFile = mdFile.replace(/\.md$/, '.pdf');
    const sizeOpts = opts.width && opts.height
      ? { width: opts.width, height: opts.height }
      : { format: opts.pageSize || 'A4' };
    await page.pdf({
      path: pdfFile,
      ...sizeOpts,
      landscape: !!opts.landscape,
      scale: opts.scale || 1,
      printBackground: true,
      margin: { top: '1.2cm', right: '1.5cm', bottom: '2cm', left: '1.5cm' },
      displayHeaderFooter: true,
      headerTemplate: `<div style="width:100%; font-family:-apple-system,Helvetica,Arial,sans-serif; font-size:7pt; line-height:1.1; color:#555; padding:0 1.5cm; text-align:right; box-sizing:border-box;">${headerText}</div>`,
      footerTemplate: '<div style="width:100%; font-family:-apple-system,Helvetica,Arial,sans-serif; font-size:8pt; color:#999; padding:0 1.5cm; text-align:right; box-sizing:border-box;">Page <span class="pageNumber"></span> of <span class="totalPages"></span></div>',
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
  const raw = process.argv.slice(2);
  const opts = {};
  const args = [];
  for (const a of raw) {
    const m = a.match(/^--theme=(.+)$/);
    const ps = a.match(/^--page-size=(.+)$/);
    const sc = a.match(/^--scale=(.+)$/);
    const w = a.match(/^--width=(.+)$/);
    const h = a.match(/^--height=(.+)$/);
    if (m) opts.theme = m[1];
    else if (ps) {
      if (ps[1].toUpperCase() === 'B5') { opts.width = '182mm'; opts.height = '257mm'; }
      else opts.pageSize = ps[1];
    }
    else if (w) opts.width = w[1];
    else if (h) opts.height = h[1];
    else if (sc) opts.scale = parseFloat(sc[1]);
    else if (a === '--landscape') opts.landscape = true;
    else args.push(a);
  }
  if (args.length === 0) {
    console.error('Usage: node convert_md_to_pdf.js [--theme=<name>] <file.md|file.html> [...]');
    console.error('       node convert_md_to_pdf.js [--theme=<name>] --all   (convert all .md/.html in cwd)');
    console.error('Available Typora themes:', fs.readdirSync(THEMES_DIR).filter(f => f.endsWith('.css')).map(f => f.replace('.css','')).join(', '));
    process.exit(1);
  }

  let files;
  if (args[0] === '--all') {
    const dir = process.cwd();
    files = fs.readdirSync(dir)
      .filter(f => (f.endsWith('.md') || f.endsWith('.html')) && !f.startsWith('convert_'))
      .map(f => path.join(dir, f));
  } else {
    files = args.map(f => path.resolve(f));
  }

  console.log(`Converting ${files.length} file(s) to PDF${opts.theme ? ` with Typora theme "${opts.theme}"` : ''}...`);
  let ok = 0, fail = 0;
  for (const f of files) {
    process.stdout.write('  ' + path.basename(f) + ' ... ');
    try {
      await convertToPdf(f, opts);
      ok++;
    } catch (err) {
      console.log('FAIL:', err.message);
      fail++;
    }
  }
  console.log(`\nDone: ${ok} converted, ${fail} failed.`);
}

main().catch(e => { console.error(e); process.exit(1); });
