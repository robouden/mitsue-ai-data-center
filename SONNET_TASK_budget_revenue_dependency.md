# SONNET EXECUTION BRIEF — Address budget-tightness, dependency, revenue-model & director-pay feedback

**Author:** Opus (planning) · **Executor:** Claude Sonnet · **Date:** 2026-06-10
**Goal:** Roll five fixes (from two reviewers' feedback) through the project artifacts: (1) budget is too tight in early phases / founder pay; (2) over-dependence on the unidentified JP co-founder and Rob's unpaid time; (3) no visible revenue model / payback; (4) confirm & encode the director-salary norm (¥300k/month, *not* a legal requirement); (5) stakeholder trade-offs not visible. Make **surgical, additive** edits — these are mature documents.

---

## 0. Read this first

**Source-of-truth facts (already established — do not re-research, just apply):**

- **Director salary is a NORM, not a legal requirement.** A 一般社団法人 director may be **unpaid**; if paid, the amount must be set by **社員総会 (members' meeting) resolution**, not self-set. For NPO法人, 役員報酬 (pay for the *role*) is capped to **≤1/3 of all officers (理事+監事)**, BUT pay for actual *work as staff* (役員給与) is separate and uncapped — so a working director can draw a normal staff salary. If the entity earns revenue, salary must follow 定期同額給与 tax rules. **¥300,000/month (¥3.6M/yr)** is a sensible, defensible rural full-time figure — adopt it as a *target*, deferred until funding covers it.
  - Sources to cite: https://www.koueki-houjin.net/shadan/hosyu.html · https://www.koueki-houjin.net/shadan/kyuyo.html · https://ashiyakaikei.com/directors-npo/ · https://cliser.co.jp/non-profit/npo/159/
- **The budget math that forces the re-baseline:** EVM WBS line **1.1 (Core PM team — Rep. Director + coordinator) is ¥8.0M across all 30 months** (~¥267k/month for *two* roles). A ¥300k/month director salary alone = **¥3.6M/yr ≈ ¥9M over 30 months**, which already **exceeds** the whole 1.1 line. So encoding the director salary REQUIRES re-baselining PM/governance.
- **The revenue model already EXISTS** in `mitsue_implementation_plan.md` (the "Return on Investment" section: revenue table ¥28–67M/yr by Year 5, cost-displacement, 10–18yr payback) — the reviewer simply **couldn't find it** because Phase 4 is one paragraph and the EVM plan deliberately excludes Phase 4. The fix is **surfacing & consolidating**, not inventing new numbers.
- **Do NOT change** BAC (¥220M), Management Reserve (¥25M), total budget (¥245M), or the ¥28M–¥53M gap / ¥192M-raised figures. Re-baselining 1.1 is an *internal reallocation within the ¥15M PM/governance envelope* — see §2.

---

## 1. GLOBAL RULES (apply to every edit)

1. **Version + date header.** Every `.md`/`.html` you edit: bump the version number and set `Last modified: 2026-06-10` in the existing right-aligned header (`<p align="right">Version: vX.Y &nbsp;|&nbsp; Last modified: 2026-06-10</p>`), before the first `---`.
2. **Preserve sources.** Director-pay facts get the four URLs above in a Sources / 出典 block wherever the claim appears.
3. **Bilingual parity.** Every EN change mirrors to its `_jp` counterpart and vice versa. (Founder agreement has no JP file yet — EN only.)
4. **Surgical & additive.** Add a section/row/sentence; do not rewrite or restructure whole documents.
5. **Keep biomass CHP primary**, solar/battery/EV complementary — unchanged by this task; don't let revenue framing invert it.
6. **Regenerate PDFs** for every `.md` edited (procedure in §7). Use `node convert_md_to_pdf.js --theme=github`.
7. **Commit only when Rob asks.** Stage logically; propose a commit message; wait. On `main`; branch first if Rob wants a PR.

---

## 2. ISSUE 1 — Budget tightness & founder compensation

### `mitsue_evm_plan.md` + `mitsue_evm_plan_jp.md`

**A. Split WBS 1.1 in both budget tables (§3.1 summary and §3.2 detail).** Replace the single `1.1 Core PM team (Rep. Director + coordinator) ¥8.0M` row with two rows, keeping the **1.0 sub-total at ¥15.0M unchanged** (internal reallocation — do not change BAC):

| WBS | Element | Budget (¥M) | Phase |
|-----|---------|-------------|-------|
| 1.1a | Representative Director (compensation — phased; see §13) | ¥5.0M | All |
| 1.1b | Project coordinator / admin | ¥3.0M | All |

(1.1a + 1.1b = ¥8.0M, so 1.0 stays ¥15.0M, BAC stays ¥220M. ¥5.0M over 30 months ≈ a stipend ramping toward — not yet reaching — the ¥300k/mo target; the full target is funded from Phase 2 grants, noted below.)

**B. Add a new section `## 13. Founder Compensation & Sustainability`** (after current §12, before the closing signature). Content:
- State plainly that early-phase founder time has been **largely unpaid**, which is itself the project's top dependency risk (cross-reference Issue 2).
- **Target compensation:** Representative Director ¥300,000/month (¥3.6M/yr) full-time-equivalent, the rural-Japan norm — **not a legal requirement** (a 一般社団法人 director may be unpaid; if paid, set by 社員総会 resolution). Cite the four URLs.
- **Phasing:** volunteer/nominal (Phase 0–1, M1–M9) → partial stipend funded from Layer-1 founding capital and first grants (Phase 2, M10–M18) → full target once Phase 2 grants (¥30–50M) land. WBS 1.1a (¥5.0M) covers the ramp inside the baseline; reaching the full run-rate from M10+ is contingent on grant funding and will be confirmed at **Baseline Rev 2 (M9, Dec 2026)**.
- One sentence noting the same logic extends to the JP co-founder if that role is compensated.

**C. Revenue-bridge note (also serves Issue 3).** In §1 (Purpose & Scope) where it says Phase 4 is excluded because "funded by operating revenue," add one sentence: *"The operating revenue model and capital-payback analysis that fund Phase 4 are set out in the new `mitsue_revenue_model.md` one-pager and the Implementation Plan's expanded Phase 4 — see those documents; this PMB deliberately stops at the end of Phase 3 (construction)."*

### `mitsue_implementation_plan.md` + `_jp`
- In the **Risk Management** table, the "Funding gaps between phases" row: append to Mitigation: *"; Layer-1 founding capital earmarked to cover the Phase 0–1 founder stipend so early runway does not depend on unpaid time."*

---

## 3. ISSUE 2 — Dependency risk (JP co-founder + Rob's unpaid time)

### `mitsue_implementation_plan.md` + `_jp` — Risk Management table
- Strengthen the existing **"Founder dependency on Rob"** row Mitigation to: *"Strong co-founders, documented processes, written succession/continuity plan; **funding the Rep. Director role removes the unpaid-time dependency** (see EVM §13); **trigger: no JP co-founder verbal commitment by end of Phase 0 → Gate 1 decision is held** pending recovery assessment."*
- (Optional) add a distinct **"JP co-founder not secured"** row — Likelihood Medium, Impact High — if it reads better as its own line than folded into the Rob row.

### `mitsue_founder_agreement_template.md` (EN only — no JP file)
- **Director compensation:** in Article 2's role/compensation table guidance, add a note that the Representative Director's compensation **target is ¥300,000/month, phased per funding availability, set by members' meeting / 社員総会 resolution after incorporation** (not self-set; cite the norm vs. requirement distinction — a director may legally be unpaid).
- **Continuity clause:** promote Appendix item #1 ("What if Rob has to leave Japan?") into a short real clause — e.g. a new **Article 8a — Continuity & Succession**: on a key founder's incapacity/departure, the remaining founders + advisory board appoint an interim Representative Director within 30 days; documented processes and access credentials are maintained so the project survives a single-person loss.
- Bump version, set `Last modified: 2026-06-10`.

---

## 4. ISSUE 3 — Revenue model / payback visibility

### New file: `mitsue_revenue_model.md` (+ `mitsue_revenue_model_jp.md`)
A **single-page** funder-facing summary that consolidates content **already in** `mitsue_implementation_plan.md` (do not invent new figures — pull from its "Return on Investment" section). Include, tightly:
1. **Revenue streams** (Year 1 / Year 5 / Year 10 table — copy from implementation plan: data-center hosting, electricity FIT/FIP, EV charging, J-Credit carbon, forestry products, education/consulting; total ¥28–67M by Y5, ¥74–166M by Y10).
2. **Cost displacement** (energy imports ¥40–60M/yr leaving the village; Koryukan ¥3–8M/yr stranded-asset upkeep; forest-management liability).
3. **Payback framework** (capital ¥200–290M by Y5; net surplus ¥10–32M/yr by Y5; **10–18yr payback**).
4. **Honest caveat** that Phase 1 feasibility studies replace illustrative figures with vetted ones.
5. Use the same `<style>`/header block pattern as other 1-pagers; version v1.0, date 2026-06-10; **Sources block** carrying over the implementation-plan source URLs for the figures.

### `mitsue_implementation_plan.md` + `_jp` — expand Phase 4
- Replace the single thin Phase 4 paragraph with a real (illustrative) **operating model**: revenue streams ramping (point to the revenue table already in the doc), target operating run-rate, estimated **break-even / net-surplus year (≈ Year 5)**, and what reinvested surplus funds (forestry scale-up, data-center expansion, replication). Keep "detailed planning happens in Year 2 once Phase 1 results are in." Add a one-line pointer to `mitsue_revenue_model.md`.
- Near the top of the doc (Overview or the ROI section header), add a one-line pointer so a reader finds the revenue case early: *"A standalone revenue & payback summary is in `mitsue_revenue_model.md`."*

### `README.md` + `README_jp.md`
- Add `mitsue_revenue_model.md` / `_jp` to the Repository Contents table (Funding/financial block).

---

## 5. ISSUE 5 — Stakeholder trade-offs visible

### `mitsue_stakeholders.md` + `mitsue_stakeholders_jp.md`
- Add a **"Decisions Required of Each Stakeholder"** table making explicit what each party must actually decide. At minimum:

| Stakeholder | Decision(s) required | When |
|---|---|---|
| Village government | Koryukan use/lease terms; endorse project as 官民連携 operating partner; co-apply for 交付金; letter of interest | Phase 0–1 |
| Mountain landowners | Sugi harvesting terms / compensation; participation in restoration | Phase 1–2 |
| Advisory board (Ozzie) | Confirm named commitments in writing | Phase 0 |
| Funders / grantmakers | Award decisions at each gate | Phase 1–3 |

- Mirror to `mitsue_village_government_onepager.md` + `_jp` only if it fits naturally (optional) — primary home is the stakeholders doc.

---

## 6. CONSISTENCY CHECKS (do before finishing)
- BAC still ¥220M, MR ¥25M, total ¥245M, gap ¥28M–¥53M, raised ¥192M — **unchanged everywhere.**
- WBS 1.0 sub-total still ¥15.0M; 1.1a + 1.1b = ¥8.0M.
- Director ¥300k/mo described as **target/norm, deferred & resolution-set**, never as a legal requirement or a day-one obligation.
- Biomass CHP still primary; solar/battery/EV complementary.
- Every edited `.md` has bumped version + 2026-06-10 date; JP parity holds; new files have JP counterparts (except founder agreement).

## 7. PDF REGENERATION
For every edited/created `.md`:
```
node convert_md_to_pdf.js --theme=github <file>.md
```
(Per the PDF Conversion Pipeline rule — never pandoc/weasyprint. Use the 2-page CSS recipe already embedded in the docs' `<style>` blocks for the 1-pagers.)

## 8. COMMIT
Stage logically. Propose a commit message like:
`docs: address budget/founder-pay, dependency, and revenue-model feedback (EN+JP)`
Wait for Rob's go-ahead before committing. End commit message with the standard Co-Authored-By line.

---

*Prepared by Opus, 2026-06-10 — for Sonnet execution. Surgical, additive edits only.*
