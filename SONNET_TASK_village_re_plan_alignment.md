# SONNET EXECUTION BRIEF — Roll the Village RE Plan alignment through all project artifacts

**Author:** Opus (planning) · **Executor:** Claude Sonnet · **Date:** 2026-06-07
**Goal:** Update every project artifact to reflect a newly surfaced strategic asset — Mitsue Village's official, Ministry-of-Environment-funded **Plan for Maximum Introduction of Renewable Energy** (Jan 2025) — and the funding unlock it creates, while keeping **biomass CHP as the primary energy source**.

---

## 0. Read this first

**Source-of-truth documents (already written by Opus — DO NOT recreate, just cite/quote from them):**

1. `mitsue_village_re_plan_alignment.md` — the full English analysis (thesis, mapping table, funding ladder, citable figures, per-audience messaging). **This is your master reference. Every change below should be consistent with it.**
2. `mitsue_village_re_plan_alignment_jp.md` — the Japanese version.
3. `Docs extra/mitsue_files from Village hall/mitsue_village_re_plan_clean_translation_en.md` — clean EN translation of the plan's key pages, with citable figures.
4. The original plan PDF: `Docs extra/mitsue_files from Village hall/20250130saienekeikakugaiyou_translated_eng-1.pdf`.

**The one-sentence thesis to thread everywhere:** *The BIOMASS ENERGY & AI project is the implementation and operating vehicle ("官民連携 運営体制") for the renewable-energy plan the village has already written, funded, and committed to.*

**The funding headline:** The plan was produced under MoE's planning-support grant (step 1, done). That makes the village eligible for the **地域脱炭素移行・再エネ推進交付金** (step 2) — subsidy **2/3, or 3/4 for batteries/private-wire (蓄電池・自営線)** because Mitsue is 過疎 + low financial-capacity index. The grant is paid **to the village** via public-private partnership, so our solar/battery/EV/private-wire capex (Layer 2) can be largely subsidized **through** the village. This is a named path to close part of the existing **¥28M–¥53M** funding gap.

---

## 1. GLOBAL RULES (apply to every edit)

1. **Biomass CHP stays PRIMARY.** It is the engine of reforestation (sugi thinnings = fuel → faster thinning → faster native-broadleaf restoration). Solar + battery + EV charging are **complementary**. The village plan leads with solar/EV/small-hydro — do **not** let that invert our hierarchy. Frame it as: *we deliver the plan's solar/battery/EV/resilience targets AND supply the forest-carbon/J-Credit mechanism the plan wants but cannot deliver alone.* (See memory `energy-strategy-biomass-chp-primary-reinstated-may-2026`.)
2. **Version + date header.** Every `.md`/`.html` you edit: bump the version number and set `Last modified: 2026-06-10` in the existing right-aligned header line (`<p align="right">Version: vX.Y &nbsp;|&nbsp; Last modified: 2026-06-10</p>`), before the first `---`. If a doc lacks one, add it.
3. **Preserve sources.** Any externally-researched figure gets its source URL in a Sources / 出典 block. The grant/subsidy facts use the env.go.jp URLs listed in the alignment doc.
4. **Bilingual parity.** Whatever you change in an EN doc, mirror in its `_jp` / `_ja` counterpart, and vice versa.
5. **Regenerate PDFs** for every `.md` you edit (procedure in §6). Regenerate brochure PDFs from their HTML.
6. **Don't over-write.** These are mature documents. Make **surgical, additive** edits — add a section/row/sentence that introduces the alignment; do not rewrite whole documents or restructure them.
7. **Commit only when Rob asks.** Stage logically; propose a commit message; wait for go-ahead. (We are on `main`; branch first if Rob wants a PR.)

---

## 2. CORE STRATEGY DOCS

### `README.md` + `README_jp.md`
- In **§8 Funding Strategy** table, Layer 2 row: append "御杖村 地域脱炭素移行・再エネ推進交付金 (2/3–3/4 subsidy, via village)" to the source list.
- Add a short subsection (e.g. **§3.1 "Alignment with the Village's Renewable Energy Plan"** under Strategic Rationale, or a new bullet in §3) — 4–6 sentences: the village has an official MoE-funded RE plan; our project is its implementation vehicle; we deliver its "one resilient site" + EV-charging + distributed-resilience targets while supplying its wanted forest-carbon/J-Credit mechanism; link to `mitsue_village_re_plan_alignment.md`.
- Add `mitsue_village_re_plan_alignment.md` / `_jp` and the clean translation to the **§10 Repository Contents** tables (new sub-block "Policy alignment").

### `mitsue_implementation_plan.md` + `_jp`
- **Layer 2 — Government Grants** list: add a bullet for **地域脱炭素移行・再エネ推進交付金** with the 2/3–3/4 subsidy note and the "paid to the municipality via 官民連携; project is the operating partner" point. Keep the existing 森林環境譲与税 / Forest Environment Transfer Tax bullet.
- In the same list or a short new paragraph, note the **MoE funding ladder** (planning grant ✅ done → 交付金 → 脱炭素先行地域) and that the plan is the policy basis for our grant applications.
- Phase 1 deliverables: add "Coordinate with the village on its 交付金 multi-year 事業計画 (position project as 官民連携 operating partner)."
- Energy Systems Feasibility Study scope: add "small-scale hydropower from water-supply intake points (per village RE plan)" and "V2H" as items to evaluate — these are explicitly in the village plan. Keep biomass CHP listed FIRST as primary.

### `mitsue_phases_funding_flowchart.md` + `_jp`
- In the **Funding Stack — Current Position** note (the `> Note:` block about the ¥28M–¥53M gap): add a sentence naming the village-led 交付金 (2/3–3/4 on solar/battery/EV/private-wire) as a concrete path to close part of the gap during Phases 2–3.
- Optionally add one line to the Diagram 2 description that L2 (Government) now includes the village 交付金 routed through the municipality. (Editing the Mermaid graph itself is optional; a prose note is sufficient.)

---

## 3. FUNDING DOCS

### `mitsue_evm_plan.md` + `_jp`
- Where the funding stack / gap-closure narrative appears, add the village 交付金 (2/3–3/4, via village, on the complementary solar/battery/EV/private-wire portion) as the **named** primary path to close part of the ¥28M–¥53M gap. Do **not** alter BAC (¥220M), MR (¥25M), or committed figures (¥192M) — this is about *how the gap closes*, not changing the baseline. Note Baseline Rev 2 (due M9, Dec 2026) should fold in any confirmed 交付金 amount.

### `mitsue_wbs.md` + `_jp`
- Add WBS task(s) under Phase 1/2: "Village RE plan alignment & 交付金 事業計画 co-development (官民連携)." Keep numbering consistent with the existing scheme. Mirror in JP.

---

## 4. GOVERNMENT & COMMUNITY ENGAGEMENT

### `mitsue_village_government_onepager.md` + `_jp`  ← **highest priority for the mayor**
- This is the sheet the village reads. Add a prominent short section: **"This project delivers your own RE plan."** Use the mapping highlights: the "one resilient site" indicator (currently 0 → our data center = the 1), EV-charging priority (transport = 46%), distributed disaster-resilience, and the forest-carbon/J-Credit mechanism. Add the funding point: village-led 交付金 at 2/3–3/4, paid to the village, project as 官民連携 operating partner.
- Use the official village figures (9 kt-CO₂, 46% transport, 90% forest, 60%-by-2030, CN-2045) from the clean translation.

### `mitsue_mayor_meeting_talking_points.md` + `mitsue_mayor_meeting_talking_points_ja.md`
- Add a new talking block in "The Bridge" section: a Japanese line (with EN gloss) the mayor will appreciate — that the project is a concrete way to **execute the village's own 再エネ導入最大化計画**, contributing to the "one resilient site" target and the EV-charging priority, and that funding can flow through the village's 交付金 route (官民連携). Keep tone consultative, not promotional.
- In "If the Mayor Asks Substantive Questions," add a Q&A: **"How does this relate to the village's renewable-energy plan?"** with a compressed bilingual answer drawn from the alignment doc.
- Keep the existing "5 enterprises in 5 years" block; the RE-plan alignment sits alongside it.

### `mitsue_qa_briefing.md`
- Add a bilingual Q&A entry: **"How does the project align with Mitsue's official Renewable Energy Plan, and does that help funding?"** — summarize the thesis + the 交付金 2/3–3/4 funding route. Cross-reference `mitsue_village_re_plan_alignment.md`.

---

## 5. NARRATIVE & OUTREACH DOCS

Make a light **consistency pass** (1–3 sentences each, only where it strengthens the piece — don't force it):

- `mitsue_project_overview_pellegrom.md` + `mitsue_letter_pellegrom_support_request.md` — for the Dutch consulate: note the official policy tailwind + MoE funding ladder as a credibility/de-risking point.
- `Mitsue_Research_Brief.md` + `_jp` — add the village RE plan to the evidence base with its citable figures and the funding ladder.
- `mitsue_introduction_a4.md` + `_jp` — if space allows on the 2-pager, one line that the project advances the village's official RE plan. (Watch the A4 length constraint — see memory `project_introduction_docs`.)
- `mitsue_email_highreso_intro.md` — optional: one line citing official local commitment (the village RE plan) as evidence the project is real and policy-backed.
- `mitsue_project_founding_story.md` + `_jp`, `mitsue_quantum_mesh_outreach.md` + `_jp` — only touch if a natural sentence fits; otherwise skip.

---

## 6. STAKEHOLDERS

### `mitsue_stakeholders.md` + `_jp` (and the two `mitsue_stakeholder_graph*.html`)
- Add **Ministry of the Environment (環境省)** and the **village RE plan / 交付金 channel** to the stakeholder set if not present, and the relationship: village = grant recipient, project = 官民連携 operating partner. Update the Mermaid diagram in the `.md` and the node set in the `.html` to match. Regenerate the `.md` PDFs.

---

## 7. BROCHURES (print collateral) — **adjust, yes**

Files: `mitsue_brochure_trifold_a4.html`, `mitsue_brochure_trifold_a4_jp.html`, `mitsue_brochure_trifold_a3.html`, `mitsue_brochure_trifold_a3_jp.html` (then regenerate the 4 matching PDFs).

- **"Funded By" panel** (inside-center): add the village's **MoE decarbonization grant route** — e.g. append "御杖村 地域脱炭素移行・再エネ推進交付金 (via village)" to the existing list (林野庁 · METI/NEDO · FIT/FIP · J-Credit · …).
- **One small line** somewhere appropriate (e.g. under "Why Here?" or the cover sub / inside intro): *"Advances Mitsue Village's official Renewable Energy Plan (2025)."* Keep it short — brochure space is tight.
- Bump the brochure version (currently "Version 2.1 · May 2026" in the back-cover footer) to 2.2 · June 2026.
- **Do NOT** restructure the three pillars; the existing "Biomass CHP & Energy Resilience" pillar already leads correctly with biomass primary — leave that framing intact.

---

## 8. PRESENTATIONS — ⚠ needs special handling

Files: `Mitsue Project Presentation.pptx` (EN), `Mitsue Project Presentation - 日本語.pptx` (JP), and `Mitsue Project Presentation.pdf` (export of EN).

**These are binary `.pptx` — not editable with text tools.** Options, in order of preference:
1. **Preferred:** edit with `python-pptx` (`pip install python-pptx`). Add **one new slide** after the funding/rationale slide titled "Alignment with the Village RE Plan" containing: the one-sentence thesis, the mapping highlights (resilient site, EV priority, forest J-Credit mechanism), and the 交付金 2/3–3/4 funding point. Then re-export the EN deck to PDF (LibreOffice headless: `libreoffice --headless --convert-to pdf "Mitsue Project Presentation.pptx"`).
2. **If python-pptx edits are unreliable for this deck,** do NOT silently skip: produce a short markdown file `mitsue_presentation_re_plan_slide.md` with the exact slide content (EN + JP) ready for Rob to paste into PowerPoint, and flag it in your summary.
- Either way, **flag the presentation step explicitly** in your final report so Rob knows whether it was applied programmatically or needs a manual paste.

---

## 9. WEBSITE — `mitsue-v2` (WordPress theme, PHP)

Location: `/home/rob/Documents/Websites/Mitsue it/mitsue-v2`. Content lives in `template-parts/section-*.php` as PHP default arrays (the live DB may override these defaults, so **also** update the deployed content — see deploy note).

**9a. Fix a pre-existing inconsistency (important):** `template-parts/section-programme.php` pillar **ii** ("EV Charging & Energy Resilience") and `template-parts/section-rationale.php` item **02** currently describe biomass as a *"future biomass-to-electricity input"* / "no separate thermal plant" — this is the **stale EV-first framing** and contradicts the current "biomass CHP primary" position. Update both (EN + JP strings) so biomass CHP reads as the **primary** baseload, solar/EV complementary. Rename pillar ii to lead with biomass (e.g. "Biomass CHP & Energy Resilience") to match the brochure.

**9b. Add the village-plan alignment:**
- `section-funding.php`: L2 "Government grants" `desc`/`desc_jp` — add the village 交付金 (2/3–3/4, via village). EN and JP.
- `section-rationale.php` or `section-programme.php`: add one short element noting the project advances the village's official RE plan and delivers its "one resilient site" + EV targets. Keep it within the existing visual grammar (a rationale item or a sub-block).
- Consider a hero stat or a one-line mention only if it fits the design cleanly; do not bloat the hero.

**9c. Deploy** (see §11 deploy procedure). Then verify on https://mitsue.it (logged-out, after cache flush).

---

## 10. OPENPROJECT — work packages, timeline, wiki

**Access & rules (critical — follow exactly):**
- Project IDs: **3 (EN), 4 (JP), 6 (rob-personal)**. API base: `https://openproject.mitsue.it/api/v3`. Auth: `-u "apikey:<TOKEN>"` (admin token in `OPENPROJECT.md`).
- **Work packages: use the REST API (curl)** for field edits and creation (subject/description/dates). PATCH requires the current `lockVersion`. (This is how the May energy pivot updated WPs.)
- **NEVER run `rails runner` on the web container** (OOM → 503). For board ordering use direct psql on the db container (see memory `reference_board_maintenance`). You should not need board edits for this task.
- **Wiki pages: do NOT psql/rails-edit.** Prepare ready-to-paste markdown and hand it to Rob to paste in the UI (memory `feedback_openproject_wiki_edits`).

**10a. First, list current state** (don't guess IDs):
```bash
curl -s -u "apikey:<TOKEN>" "https://openproject.mitsue.it/api/v3/projects/3/work_packages?pageSize=200" \
  | python3 -c "import sys,json;[print(w['id'],'|',w['subject']) for w in json.load(sys.stdin)['_embedded']['elements']]"
```

**10b. Update existing energy/funding WPs** (IDs from the May pivot — verify they still match by subject before patching): EN **57** (energy feasibility), **71** (vendor selection), **85** (install); JP **164**, **177**, **190**. Append to each description a line that the energy scope aligns with the village RE plan and that complementary solar/battery/EV/private-wire is a candidate for the village-led 交付金 (2/3–3/4). Do **not** change their subjects (biomass CHP must stay first/primary, as set in May).

**10c. Add new WPs** (EN project 3 + JP project 4 mirror):
- "Village RE plan alignment — co-develop 交付金 事業計画 with village (官民連携)" — Phase 1/2, priority High.
- "Map project deliverables to village RE plan Basic Policies & indicators (incl. 'one resilient site')" — Phase 1.
- (Optional milestone) "Village RE plan published (Jan 2025) — policy basis established" as a context milestone, if a Milestone type fits the board.

**10d. Wiki (prepare for Rob, don't auto-edit):** Draft a paste-ready wiki page "Village RE Plan Alignment" summarizing the alignment doc, for the `mistue-ai-data-center` project wiki. Hand the markdown to Rob.

**Because OpenProject changes are outward-facing and harder to reverse, confirm the new-WP list and any subject changes with Rob before writing, per the global rules.**

---

## 11. OPERATIONAL PROCEDURES

### PDF regeneration (after any `.md` edit)
Full procedure in `OPENPROJECT.md` → "Generating PDFs from Markdown". Recreate `/tmp/md2pdf.js` and `/tmp/gen_pdfs.sh` from the blocks there, **add the new files** to the `files=(...)` array (`mitsue_village_re_plan_alignment`, `mitsue_village_re_plan_alignment_jp`, and any others you edit), then run the batch. Mermaid files (`README`, `_jp`, `mitsue_stakeholders`, `_jp`) render via `mermaid-filter`.

### Brochure PDFs (HTML → PDF)
Use the puppeteer/Chrome path (landscape A4/A3 per the `@page` size in each HTML). Confirm the trifold panels still align after text changes (text length changes can reflow panels — eyeball each PDF).

### Website deploy (mitsue.it VPS)
Per memory `feedback_deploy_website`: push to **Codeberg (primary)** + **GitHub (secondary)**, then `ssh root@80.208.225.44 "deploy-mitsue"`. If `deploy-mitsue` is unavailable, fall back to the README method: `rsync` the theme to `/home/mitsue.it/public_html/wp-content/themes/mitsue-v2/`, then flush cache (`wp cache flush` + delete `wpo-cache` and `wpo-minify`). **If content is DB-overridden, the PHP-default change won't show** — update the `mitsue_options` via WP-CLI per the README, or have Rob edit Settings → Mitsue Content. Verify logged-out.

### Git
Stage in logical groups. Proposed commit message (await Rob's go-ahead):
```
docs: align all artifacts with village RE plan + 交付金 funding route

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>
```

---

## 12. POEM & MAYOR CARD — assessment (recommended: LEAVE AS-IS)

Rob asked whether the **Kaya seed poem** and **mayor-meeting card** should change.

**Recommendation: do not alter them.** Reasons:
- They are **personal, timeless gift artifacts** (tanka/haiku/kintsugi, cedar-box, seeds) about forest, century-scale time, and generations. Bending them toward a 2025 policy document would cheapen them and break their register.
- They are **already aligned in spirit.** The poem literally asks *"電力は誰が決めるのか / Whose hand turns on the lights?"* — which resonates exactly with the village plan's "local production for local consumption" / energy self-determination theme. The spoken framing ("the trees we cut are cedar; the trees we plant are kaya") already embodies the reforestation-via-thinning logic.
- They are marked **"Personal — not for publication."** Policy alignment belongs in the public/strategy docs, not the gift.

**Optional (only if Rob wants it):** add ONE spoken talking-line to the *mayor meeting talking points* (not the card) connecting the gift's spirit to the village's own plan — e.g. *"村が掲げる再エネ計画と同じ方向を、私たちは長い時間軸で実行したいのです"*. Leave the card and poem text untouched.

---

## 13. ACCEPTANCE CHECKLIST

- [ ] Every edited `.md`/`.html` has version bumped + `Last modified: 2026-06-10`.
- [ ] Biomass CHP reads as **primary** everywhere touched (esp. website pillar ii + rationale 02 fixed).
- [ ] Village 交付金 (2/3–3/4, via village) added to: README, implementation plan, funding flowchart, EVM, brochures "Funded By", website funding, village onepager, mayor points, QA briefing — EN **and** JP.
- [ ] Citable figures used consistently (9 kt-CO₂, 46% transport, 90% forest, 60%/2030, CN-2045, "1 resilient site").
- [ ] All edited `.md` → PDFs regenerated; 4 brochure PDFs regenerated; presentation handled (programmatic or paste-ready md, **explicitly reported**).
- [ ] Website deployed + verified logged-out on mitsue.it.
- [ ] OpenProject WP changes confirmed with Rob, applied via API; wiki page prepared as paste-ready md.
- [ ] Poem & mayor card left unchanged (per §12).
- [ ] Sources blocks include env.go.jp URLs.
- [ ] Final report to Rob lists exactly what changed, what was skipped, and what needs his manual step (pptx paste, OpenProject confirm, website DB content, git push).

---

## 14. SUGGESTED EXECUTION ORDER

1. Core docs (README, implementation plan, funding flowchart, EVM, WBS) — EN+JP. Regenerate PDFs.
2. Government/community (village onepager, mayor points, QA briefing) — EN+JP. Regenerate PDFs.
3. Narrative/outreach consistency pass + stakeholders. Regenerate PDFs.
4. Brochures (4 HTML → 4 PDF).
5. Website (fix CHP framing + add alignment) → deploy → verify.
6. Presentations (python-pptx or paste-ready md).
7. OpenProject (list → confirm with Rob → API edits + new WPs; wiki md for Rob).
8. Stage git, propose commit, await Rob.

**Work in batches, keep biomass CHP primary, make surgical additive edits, and report clearly at the end.**
