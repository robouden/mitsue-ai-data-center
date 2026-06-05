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

async function convertToPdf(mdFile, opts = {}) {
  const text = fs.readFileSync(mdFile, 'utf8');
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
  const raw = process.argv.slice(2);
  const opts = {};
  const args = [];
  for (const a of raw) {
    const m = a.match(/^--theme=(.+)$/);
    if (m) opts.theme = m[1];
    else args.push(a);
  }
  if (args.length === 0) {
    console.error('Usage: node convert_md_to_pdf.js [--theme=<name>] <file.md> [file2.md ...]');
    console.error('       node convert_md_to_pdf.js [--theme=<name>] --all   (convert all .md in cwd)');
    console.error('Available Typora themes:', fs.readdirSync(THEMES_DIR).filter(f => f.endsWith('.css')).map(f => f.replace('.css','')).join(', '));
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
