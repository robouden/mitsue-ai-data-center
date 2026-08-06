<!-- Version: v1.1 | Last modified: 2026-08-06 (added WBS 5.6a prototype CHP/chipper gap flag) -->
<div style="font-family:-apple-system,Helvetica,Arial,sans-serif;">
<p style="font-size:7.5pt; font-weight:600; letter-spacing:0.25em; color:#3a7a5a; margin:0 0 4mm;">PROJECT DOCUMENT</p>
<h1 style="font-size:28pt; font-weight:700; margin:0 0 2mm; border-bottom:1px solid #eee; padding-bottom:2mm;">BIOMASS ENERGY & AI</h1>
<p style="font-style:italic; color:#666; margin:1mm 0 0;">Reforesting in Mitsue</p>
<p style="font-style:italic; color:#666; margin:2mm 0 8mm;">Earned Value Management Plan</p>
<img src="assets/logo_go.png" alt="御" width="50%" style="display:block;margin:0 auto;">
<div style="height:105mm;"></div>
<table style="width:100%; border-collapse:collapse; font-size:9pt;">
<tr><td style="padding:3mm 4mm; border:1px solid #ccc; font-weight:bold; width:30%;">Version</td><td style="padding:3mm 4mm; border:1px solid #ccc;">v2.9</td></tr>
<tr><td style="padding:3mm 4mm; border:1px solid #ccc; font-weight:bold;">Date</td><td style="padding:3mm 4mm; border:1px solid #ccc;">2026-07-17</td></tr>
<tr><td style="padding:3mm 4mm; border:1px solid #ccc; font-weight:bold;">Author</td><td style="padding:3mm 4mm; border:1px solid #ccc;">Rob Oudendijk</td></tr>
</table>
</div>

<div style="page-break-after:always; break-after:page; height:0; margin:0; padding:0;"></div>

---

# BIOMASS ENERGY & AI — Earned Value Management Plan
### Reforesting in Mitsue
### Performance Baseline · Cost Control · Forecast Framework

*Phases 0–3 · April 2026 – September 2028*

---

## 1. Purpose and Scope

This EVM Plan establishes the **Performance Measurement Baseline (PMB)** for the Mitsue Sustainable Energy & AI Data Center project across its four build phases (Phase 0 through Phase 3). It defines how the project will measure schedule and cost performance, report progress to stakeholders, and forecast the cost and date at completion.

The plan covers the **30-month period April 2026 – September 2028**. Phase 4 (Operations & Scale, Month 31+) is not included in the baseline because it is funded differently (operating revenue) and planned in Year 2 once Phase 1 results are confirmed. *The operating revenue model and capital-payback analysis that fund Phase 4 are set out in `mitsue_revenue_model.md` and the Implementation Plan's expanded Phase 4 section — see those documents; this PMB deliberately stops at the end of Phase 3 (construction). The month-by-month funding **inflow** that must keep the cash balance positive against this spend baseline is set out in `mitsue_cashflow_model.md`.*

**Data Date for current baseline**: 2026-05-18 (end of Month 2)

> **Schedule reconciliation (2026-07-03).** This PMB is anchored to the original compressed schedule (M1 = Apr 2026, 30 months to Sep 2028). The **live OpenProject Gantt** — now the operative schedule — runs materially later: Phase 0 to Oct 2026, Phase 1 to May 2027, Phase 2 to May 2028, Phase 3 to Nov 2029 (~44 months). Phase 0 is on-track against the Gantt; the earlier sense of slippage came from comparing to this compressed baseline. The monthly PV curve and CPI/SPI figures below remain **Baseline Rev 1** and have **not** been re-timed to the Gantt — re-timing the PMB is the explicit **Baseline Rev 2** deliverable (due M9 / Dec 2026), which will also fold in any confirmed 交付金 amount. Until then, read schedule variance against the live Gantt, not this Rev 1 curve.

---

## 2. EVM Fundamentals — Key Metrics

| Term | Symbol | Formula | What it means |
|------|--------|---------|---------------|
| Planned Value | **PV** | Time-phased budget | Budgeted cost of work **scheduled** to date |
| Earned Value | **EV** | % complete × BAC | Budgeted cost of work **actually performed** |
| Actual Cost | **AC** | Invoices + payroll | Real money **spent** to date |
| Budget at Completion | **BAC** | Sum of all PV | Total approved budget for the PMB |
| Schedule Variance | **SV** | EV − PV | Negative = behind plan |
| Cost Variance | **CV** | EV − AC | Negative = over budget |
| Schedule Performance Index | **SPI** | EV ÷ PV | < 1.0 = behind schedule |
| Cost Performance Index | **CPI** | EV ÷ AC | < 1.0 = over budget |
| Estimate at Completion | **EAC** | AC + (BAC−EV)÷CPI | Projected final cost |
| Estimate to Complete | **ETC** | EAC − AC | Remaining work cost forecast |
| Variance at Completion | **VAC** | BAC − EAC | Projected over/under at end |
| To-Complete Perf. Index | **TCPI** | (BAC−EV)÷(BAC−AC) | Efficiency needed to finish on budget |

---

## 3. Budget Structure

### 3.1 Summary Budget

| Level | Item | Budget (¥M) | % of BAC |
|-------|------|-------------|----------|
| Total Project Budget | | **¥245.0M** | — |
| — Management Reserve (~11%) | Not in PMB | **¥25.0M** | — |
| **Performance Measurement Baseline (BAC)** | | **¥220.0M** | 100% |
| 1.0 | Project Management & Governance | ¥15.0M | 6.8% |
| 2.0 | Phase 0 — Pre-Foundation | ¥0.25M | 0.1% |
| 3.0 | Phase 1 — Foundation | ¥5.5M | 2.5% |
| 4.0 | Phase 2 — Pilot Design | ¥22.25M | 10.1% |
| 5.0 | Phase 3 — Pilot Build | ¥177.0M | 80.5% |

> **Management Reserve** (¥25M) is held by the Representative Director and is **not part of the PMB**. It may be drawn down only with explicit board approval to address unforeseen scope.

> **Baseline Rev 1 (May 2026)** — Reality-checked against real-world Japan benchmarks for solar PV (¥200–300K/kW), school seismic retrofit (¥200–500K/㎡), commercial EV fast-chargers (¥5–6M each), and forestry road works. Phase 3 line items, PM/governance, and contingency uplifted accordingly; BAC raised from ¥168M to ¥220M.

### 3.2 Work Breakdown Structure (WBS) — Budget Detail

| WBS | Element | Budget (¥M) | Phase |
|-----|---------|-------------|-------|
| 1.0 | **Project Management & Governance** | | |
| 1.1a | Representative Director (compensation — phased; see §13) | ¥5.0M | All |
| 1.1b | Project coordinator / admin | ¥3.0M | All |
| 1.2 | Legal, accounting, 行政書士 fees | ¥4.0M | All |
| 1.3 | Communications, website, translation | ¥3.0M | All |
| | *Sub-total 1.0* | *¥15.0M* | |
| 2.0 | **Phase 0 — Pre-Foundation** | | |
| 2.1 | Community stakeholder meetings & travel | ¥0.10M | P0 |
| 2.2 | Charter & document preparation | ¥0.10M | P0 |
| 2.3 | Founding team identification | ¥0.05M | P0 |
| | *Sub-total 2.0* | *¥0.25M* | |
| 3.0 | **Phase 1 — Foundation** | | |
| 3.1 | 一般社団法人 incorporation | ¥0.5M | P1 |
| 3.2 | Forestry feasibility study | ¥1.5M | P1 |
| 3.3 | Energy systems feasibility study | ¥1.5M | P1 |
| 3.4 | Building & site assessment | ¥0.8M | P1 |
| 3.5 | Connectivity assessment | ¥0.4M | P1 |
| 3.6 | Advisory board, bank, accounting setup | ¥0.8M | P1 |
| | *Sub-total 3.0* | *¥5.5M* | |
| 4.0 | **Phase 2 — Pilot Design** | | |
| 4.1 | Structural & architectural design | ¥2.0M | P2 |
| 4.2 | Energy systems engineering | ¥2.0M | P2 |
| 4.3 | Data center & IT design | ¥1.0M | P2 |
| 4.4 | EV charging system design | ¥1.0M | P2 |
| 4.5 | Permitting & regulatory (METI, FIT, forestry) | ¥3.5M | P2 |
| 4.6 | Partnership & landowner agreements | ¥1.5M | P2 |
| 4.7 | Grant writing & funding applications | ¥2.0M | P2 |
| 4.8 | Staff hiring & onboarding (2–3 part-time) | ¥6.0M | P2 |
| 4.9 | Vendor pre-qualification | ¥1.5M | P2 |
| 4.10 | Phase 2 contingency | ¥1.75M | P2 |
| | *Sub-total 4.0* | *¥22.25M* | |
| 5.0 | **Phase 3 — Pilot Build** | | |
| 5.1 | School building renovation (1 wing) | ¥38.0M | P3 |
| 5.2 | Solar PV installation (~100 kW) | ¥22.0M | P3 |
| 5.3 | Battery storage system | ¥12.0M | P3 |
| 5.4 | EV charging infrastructure (4 stations) | ¥15.0M | P3 |
| 5.5 | Data center fitout (10–20 servers) | ¥20.0M | P3 |
| 5.6 | Forestry operations (5–10 ha harvest + replant) | ¥25.0M | P3 |
| 5.6a | ⚠️ Prototype CHP + fuel chipper (10–20 kWe, Sugano site) — **NOT YET IN THE ¥25.0M ABOVE, pending vendor RFQ** | *placeholder ¥7–13M* | P3 |
| 5.7 | Fiber connectivity upgrade | ¥10.0M | P3 |
| 5.8 | Testing, commissioning, and startup | ¥8.0M | P3 |
| 5.9 | Phase 3 contingency (18%) | ¥27.0M | P3 |
| | *Sub-total 5.0 (excl. 5.6a placeholder)* | *¥177.0M* | |
| | **TOTAL BAC (excl. 5.6a placeholder)** | **¥220.0M** | |

> **5.6a is a gap, not a committed cost.** The Sugano prototype CHP + chipper (see
> `mitsue_chp_maker_shortlist.md`) was **sited** 2026-07-17 but never costed into any WBS —
> it falls outside Phase 4's commercial-scale table (§14, sized for the 2×0.6 MWe fleet,
> not the 10–20 kWe pilot). The ¥7–13M placeholder = domestic 巴商会 Stirling unit or
> import-exception micro-gasifier (~¥6–7.5M, unconfirmed) + a small chipper (¥0.4–3M, see
> `mitsue_email_fujitex_chipper_rfq.md` / `mitsue_chipper_rfq_form_drafts.md`). **Not summed
> into Sub-total 5.0 or the ¥220M BAC yet** — do it once the RFQs return real quotes, then
> decide whether it raises the BAC or is absorbed by the existing ¥27M Phase 3 contingency /
> ¥25M Management Reserve.

---

## 4. Time-Phased Baseline (S-Curve)

Monthly planned expenditure and cumulative planned value over the 30-month baseline. Spending is front-loaded within phases on studies and design; construction spending peaks in Months 22–27.

| Month | Calendar | Phase | Monthly PV (¥M) | Cumulative PV (¥M) | % Complete |
|-------|----------|-------|-----------------|---------------------|------------|
| M1 | Apr 2026 | P0 | 0.05 | 0.05 | 0.0% |
| M2 | May 2026 | P0 | 0.10 | 0.15 | 0.1% |
| **M2 ← Status Date** | | | | | |
| M3 | Jun 2026 | P0 | 0.10 | 0.25 | 0.1% |
| M4 | Jul 2026 | P1 | 0.20 | 0.45 | 0.2% |
| M5 | Aug 2026 | P1 | 0.50 | 0.95 | 0.4% |
| M6 | Sep 2026 | P1 | 0.80 | 1.75 | 0.8% |
| M7 | Oct 2026 | P1 | 1.20 | 2.95 | 1.3% |
| M8 | Nov 2026 | P1 | 1.50 | 4.45 | 2.0% |
| M9 | Dec 2026 | P1 | 1.30 | 5.75 | 2.6% |
| M10 | Jan 2027 | P2 | 1.50 | 7.25 | 3.3% |
| M11 | Feb 2027 | P2 | 2.20 | 9.45 | 4.3% |
| M12 | Mar 2027 | P2 | 2.80 | 12.25 | 5.6% |
| M13 | Apr 2027 | P2 | 3.00 | 15.25 | 6.9% |
| M14 | May 2027 | P2 | 3.00 | 18.25 | 8.3% |
| M15 | Jun 2027 | P2 | 3.00 | 21.25 | 9.7% |
| M16 | Jul 2027 | P2 | 2.50 | 23.75 | 10.8% |
| M17 | Aug 2027 | P2 | 2.50 | 26.25 | 11.9% |
| M18 | Sep 2027 | P2 | 2.00 | 28.25 | 12.8% |
| M19 | Oct 2027 | P3 | 4.00 | 32.25 | 14.7% |
| M20 | Nov 2027 | P3 | 7.00 | 39.25 | 17.8% |
| M21 | Dec 2027 | P3 | 11.00 | 50.25 | 22.8% |
| M22 | Jan 2028 | P3 | 16.50 | 66.75 | 30.3% |
| M23 | Feb 2028 | P3 | 20.50 | 87.25 | 39.7% |
| M24 | Mar 2028 | P3 | 20.50 | 107.75 | 49.0% |
| M25 | Apr 2028 | P3 | 25.00 | 132.75 | 60.3% |
| M26 | May 2028 | P3 | 25.00 | 157.75 | 71.7% |
| M27 | Jun 2028 | P3 | 20.50 | 178.25 | 81.0% |
| M28 | Jul 2028 | P3 | 20.50 | 198.75 | 90.3% |
| M29 | Aug 2028 | P3 | 14.00 | 212.75 | 96.7% |
| M30 | Sep 2028 | P3 | 7.25 | 220.00 | 100.0% |
| | **BAC** | | **¥220.0M** | | |

### S-Curve Shape

The expenditure profile follows a classic **slow-fast-slow** S-curve:
- **M1–M9** (Phases 0–1): Ramp-up — legal, feasibility studies, advisory engagement
- **M10–M18** (Phase 2): Acceleration — engineering design, permitting, grant applications
- **M19–M28** (Phase 3 core): Peak spend — construction, procurement, installation
- **M29–M30** (Phase 3 close): Tail-off — commissioning, punch-list, handover

<div style="page-break-inside:avoid; margin: 10pt 0">

**Figure 1 — Baseline S-Curve (Cumulative Planned Value)**

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 325" style="width:100%;display:block">
  <!-- Phase background bands -->
  <rect x="60" y="28" width="64" height="252" fill="#eef4ff"/>
  <rect x="124" y="28" width="128" height="252" fill="#dce8ff"/>
  <rect x="252" y="28" width="193" height="252" fill="#fff4e6"/>
  <rect x="445" y="28" width="235" height="252" fill="#fff0f0"/>
  <!-- Phase labels -->
  <text x="92" y="42" text-anchor="middle" font-size="8" fill="#6796e6" font-weight="bold" font-family="Segoe UI,sans-serif">Phase 0</text>
  <text x="188" y="42" text-anchor="middle" font-size="8" fill="#4a7ac4" font-weight="bold" font-family="Segoe UI,sans-serif">Phase 1</text>
  <text x="348" y="42" text-anchor="middle" font-size="8" fill="#c06010" font-weight="bold" font-family="Segoe UI,sans-serif">Phase 2</text>
  <text x="562" y="42" text-anchor="middle" font-size="8" fill="#d94f4f" font-weight="bold" font-family="Segoe UI,sans-serif">Phase 3</text>
  <!-- Horizontal gridlines -->
  <line x1="60" y1="280" x2="680" y2="280" stroke="#bbb" stroke-width="0.6"/>
  <line x1="60" y1="250" x2="680" y2="250" stroke="#ddd" stroke-width="0.4"/>
  <line x1="60" y1="220" x2="680" y2="220" stroke="#ddd" stroke-width="0.4"/>
  <line x1="60" y1="191" x2="680" y2="191" stroke="#ddd" stroke-width="0.4"/>
  <line x1="60" y1="161" x2="680" y2="161" stroke="#ddd" stroke-width="0.4"/>
  <line x1="60" y1="131" x2="680" y2="131" stroke="#ddd" stroke-width="0.4"/>
  <line x1="60" y1="101" x2="680" y2="101" stroke="#ddd" stroke-width="0.4"/>
  <line x1="60" y1="72" x2="680" y2="72" stroke="#ddd" stroke-width="0.4"/>
  <line x1="60" y1="42" x2="680" y2="42" stroke="#ddd" stroke-width="0.4"/>
  <!-- Vertical gridlines at M6,M12,M18,M24,M30 -->
  <line x1="167" y1="28" x2="167" y2="280" stroke="#ddd" stroke-width="0.4"/>
  <line x1="295" y1="28" x2="295" y2="280" stroke="#ddd" stroke-width="0.4"/>
  <line x1="423" y1="28" x2="423" y2="280" stroke="#ddd" stroke-width="0.4"/>
  <line x1="552" y1="28" x2="552" y2="280" stroke="#ddd" stroke-width="0.4"/>
  <line x1="680" y1="28" x2="680" y2="280" stroke="#ddd" stroke-width="0.4"/>
  <!-- BAC line -->
  <line x1="60" y1="30" x2="680" y2="30" stroke="#d94f4f" stroke-width="1" stroke-dasharray="5,4"/>
  <text x="683" y="33" font-size="7" fill="#d94f4f" font-family="Segoe UI,sans-serif">BAC ¥220M</text>
  <!-- Status date line -->
  <line x1="103" y1="28" x2="103" y2="288" stroke="#e58520" stroke-width="1.5" stroke-dasharray="4,3"/>
  <text x="106" y="299" font-size="7" fill="#e58520" font-weight="bold" font-family="Segoe UI,sans-serif">▲ Status Date 2026-05-18</text>
  <!-- Y-axis labels -->
  <text x="55" y="283" text-anchor="end" font-size="8" fill="#555" font-family="Segoe UI,sans-serif">0</text>
  <text x="55" y="253" text-anchor="end" font-size="8" fill="#555" font-family="Segoe UI,sans-serif">25</text>
  <text x="55" y="223" text-anchor="end" font-size="8" fill="#555" font-family="Segoe UI,sans-serif">50</text>
  <text x="55" y="194" text-anchor="end" font-size="8" fill="#555" font-family="Segoe UI,sans-serif">75</text>
  <text x="55" y="164" text-anchor="end" font-size="8" fill="#555" font-family="Segoe UI,sans-serif">100</text>
  <text x="55" y="134" text-anchor="end" font-size="8" fill="#555" font-family="Segoe UI,sans-serif">130</text>
  <text x="55" y="104" text-anchor="end" font-size="8" fill="#555" font-family="Segoe UI,sans-serif">160</text>
  <text x="55" y="75" text-anchor="end" font-size="8" fill="#555" font-family="Segoe UI,sans-serif">195</text>
  <text x="55" y="45" text-anchor="end" font-size="8" fill="#555" font-family="Segoe UI,sans-serif">220</text>
  <text x="16" y="165" text-anchor="middle" font-size="8" fill="#555" transform="rotate(-90,16,165)" font-family="Segoe UI,sans-serif">¥ Million (cumulative)</text>
  <!-- X-axis labels -->
  <text x="60" y="295" text-anchor="middle" font-size="8" fill="#555" font-family="Segoe UI,sans-serif">M1</text>
  <text x="167" y="295" text-anchor="middle" font-size="8" fill="#555" font-family="Segoe UI,sans-serif">M6</text>
  <text x="295" y="295" text-anchor="middle" font-size="8" fill="#555" font-family="Segoe UI,sans-serif">M12</text>
  <text x="423" y="295" text-anchor="middle" font-size="8" fill="#555" font-family="Segoe UI,sans-serif">M18</text>
  <text x="552" y="295" text-anchor="middle" font-size="8" fill="#555" font-family="Segoe UI,sans-serif">M24</text>
  <text x="680" y="295" text-anchor="middle" font-size="8" fill="#555" font-family="Segoe UI,sans-serif">M30</text>
  <text x="60" y="307" text-anchor="middle" font-size="7" fill="#999" font-family="Segoe UI,sans-serif">Apr'26</text>
  <text x="167" y="307" text-anchor="middle" font-size="7" fill="#999" font-family="Segoe UI,sans-serif">Sep'26</text>
  <text x="295" y="307" text-anchor="middle" font-size="7" fill="#999" font-family="Segoe UI,sans-serif">Mar'27</text>
  <text x="423" y="307" text-anchor="middle" font-size="7" fill="#999" font-family="Segoe UI,sans-serif">Sep'27</text>
  <text x="552" y="307" text-anchor="middle" font-size="7" fill="#999" font-family="Segoe UI,sans-serif">Mar'28</text>
  <text x="680" y="307" text-anchor="middle" font-size="7" fill="#999" font-family="Segoe UI,sans-serif">Sep'28</text>
  <!-- Axes -->
  <line x1="60" y1="28" x2="60" y2="282" stroke="#888" stroke-width="1.5"/>
  <line x1="60" y1="280" x2="685" y2="280" stroke="#888" stroke-width="1.5"/>
  <!-- Fill under curve -->
  <polygon points="60,279.9 81,279.8 103,279.6 124,279.3 146,278.6 167,277.4 188,275.6 210,273.4 231,271.4 252,269.2 274,265.9 295,261.8 316,257.3 338,252.8 359,248.4 381,244.7 402,240.9 423,237.9 445,233.5 466,226.1 487,214.2 509,196.3 530,174 552,151.7 573,124.9 594,98.1 616,75.8 637,53.4 658,38.6 680,30 680,280 60,280" fill="#6796e6" fill-opacity="0.12"/>
  <!-- S-curve PV line -->
  <polyline points="60,279.9 81,279.8 103,279.6 124,279.3 146,278.6 167,277.4 188,275.6 210,273.4 231,271.4 252,269.2 274,265.9 295,261.8 316,257.3 338,252.8 359,248.4 381,244.7 402,240.9 423,237.9 445,233.5 466,226.1 487,214.2 509,196.3 530,174 552,151.7 573,124.9 594,98.1 616,75.8 637,53.4 658,38.6 680,30" fill="none" stroke="#6796e6" stroke-width="2.5" stroke-linejoin="round"/>
  <!-- Gate markers — diamond shape; ↩ label shows hold action if threshold not met -->
  <polygon points="124,274.3 129,279.3 124,284.3 119,279.3" fill="#4a7ac4" stroke="white" stroke-width="1.5"/>
  <text x="116" y="270" font-size="6.5" fill="#4a7ac4" font-family="Segoe UI,sans-serif">Gate 1</text>
  <text x="116" y="263" font-size="5.5" fill="#4a7ac4" font-style="italic" font-family="Segoe UI,sans-serif">↩ FAIL: Hold &amp; re-pitch</text>
  <polygon points="252,264.2 257,269.2 252,274.2 247,269.2" fill="#4a7ac4" stroke="white" stroke-width="1.5"/>
  <text x="244" y="260" font-size="6.5" fill="#4a7ac4" font-family="Segoe UI,sans-serif">Gate 2</text>
  <text x="244" y="253" font-size="5.5" fill="#4a7ac4" font-style="italic" font-family="Segoe UI,sans-serif">↩ FAIL: Descope</text>
  <polygon points="445,228.5 450,233.5 445,238.5 440,233.5" fill="#c06010" stroke="white" stroke-width="1.5"/>
  <text x="437" y="224" font-size="6.5" fill="#c06010" font-family="Segoe UI,sans-serif">Gate 3</text>
  <text x="437" y="217" font-size="5.5" fill="#c06010" font-style="italic" font-family="Segoe UI,sans-serif">↩ FAIL: Stage build</text>
  <polygon points="680,25 685,30 680,35 675,30" fill="#d94f4f" stroke="white" stroke-width="1.5"/>
  <text x="648" y="25" font-size="6.5" fill="#d94f4f" font-family="Segoe UI,sans-serif">Gate 4</text>
  <text x="648" y="38" font-size="5.5" fill="#d94f4f" font-style="italic" font-family="Segoe UI,sans-serif">↩ FAIL: Pilot mode</text>
  <!-- Current status dot (EV) -->
  <circle cx="103" cy="279.8" r="5" fill="#e58520" stroke="white" stroke-width="1.5"/>
  <text x="107" y="274" font-size="7" fill="#e58520" font-weight="bold" font-family="Segoe UI,sans-serif">EV=¥0.12M</text>
</svg>

</div>

<div style="page-break-inside:avoid; margin: 10pt 0">

**Figure 2 — Monthly Planned Expenditure by Phase**

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 240" style="width:100%;display:block">
  <!-- Y gridlines -->
  <line x1="60" y1="200" x2="680" y2="200" stroke="#bbb" stroke-width="0.6"/>
  <line x1="60" y1="160" x2="680" y2="160" stroke="#ddd" stroke-width="0.4"/>
  <line x1="60" y1="120" x2="680" y2="120" stroke="#ddd" stroke-width="0.4"/>
  <line x1="60" y1="80" x2="680" y2="80" stroke="#ddd" stroke-width="0.4"/>
  <line x1="60" y1="40" x2="680" y2="40" stroke="#ddd" stroke-width="0.4"/>
  <line x1="60" y1="20" x2="680" y2="20" stroke="#ddd" stroke-width="0.4"/>
  <!-- Bars — width 18px, gap ~2.7px, scale: 180px = ¥18M → 10px/¥1M -->
  <!-- P0: light blue #b8c9ee -->
  <rect x="60" y="199.5" width="18" height="0.5" fill="#b8c9ee"/>
  <rect x="81" y="199" width="18" height="1" fill="#b8c9ee"/>
  <rect x="102" y="199" width="18" height="1" fill="#b8c9ee"/>
  <!-- P1: #6796e6 -->
  <rect x="122" y="198" width="18" height="2" fill="#6796e6"/>
  <rect x="143" y="195" width="18" height="5" fill="#6796e6"/>
  <rect x="163" y="192" width="18" height="8" fill="#6796e6"/>
  <rect x="184" y="188" width="18" height="12" fill="#6796e6"/>
  <rect x="205" y="185" width="18" height="15" fill="#6796e6"/>
  <rect x="225" y="187" width="18" height="13" fill="#6796e6"/>
  <!-- P2: #e58520 -->
  <rect x="246" y="185" width="18" height="15" fill="#e58520"/>
  <rect x="267" y="178" width="18" height="22" fill="#e58520"/>
  <rect x="287" y="172" width="18" height="28" fill="#e58520"/>
  <rect x="308" y="170" width="18" height="30" fill="#e58520"/>
  <rect x="329" y="170" width="18" height="30" fill="#e58520"/>
  <rect x="349" y="170" width="18" height="30" fill="#e58520"/>
  <rect x="370" y="175" width="18" height="25" fill="#e58520"/>
  <rect x="391" y="175" width="18" height="25" fill="#e58520"/>
  <rect x="411" y="180" width="18" height="20" fill="#e58520"/>
  <!-- P3: #d94f4f -->
  <rect x="432" y="170" width="18" height="30" fill="#d94f4f"/>
  <rect x="453" y="150" width="18" height="50" fill="#d94f4f"/>
  <rect x="473" y="120" width="18" height="80" fill="#d94f4f"/>
  <rect x="494" y="80" width="18" height="120" fill="#d94f4f"/>
  <rect x="515" y="50" width="18" height="150" fill="#d94f4f"/>
  <rect x="535" y="50" width="18" height="150" fill="#d94f4f"/>
  <rect x="556" y="20" width="18" height="180" fill="#d94f4f"/>
  <rect x="577" y="20" width="18" height="180" fill="#d94f4f"/>
  <rect x="597" y="50" width="18" height="150" fill="#d94f4f"/>
  <rect x="618" y="50" width="18" height="150" fill="#d94f4f"/>
  <rect x="639" y="100" width="18" height="100" fill="#d94f4f"/>
  <rect x="659" y="142" width="18" height="57.5" fill="#d94f4f"/>
  <!-- Axes -->
  <line x1="60" y1="20" x2="60" y2="202" stroke="#888" stroke-width="1.5"/>
  <line x1="60" y1="200" x2="685" y2="200" stroke="#888" stroke-width="1.5"/>
  <!-- Y labels -->
  <text x="55" y="203" text-anchor="end" font-size="8" fill="#555" font-family="Segoe UI,sans-serif">0</text>
  <text x="55" y="163" text-anchor="end" font-size="8" fill="#555" font-family="Segoe UI,sans-serif">5</text>
  <text x="55" y="123" text-anchor="end" font-size="8" fill="#555" font-family="Segoe UI,sans-serif">11</text>
  <text x="55" y="83" text-anchor="end" font-size="8" fill="#555" font-family="Segoe UI,sans-serif">17</text>
  <text x="55" y="43" text-anchor="end" font-size="8" fill="#555" font-family="Segoe UI,sans-serif">22</text>
  <text x="55" y="23" text-anchor="end" font-size="8" fill="#555" font-family="Segoe UI,sans-serif">25</text>
  <text x="16" y="120" text-anchor="middle" font-size="8" fill="#555" transform="rotate(-90,16,120)" font-family="Segoe UI,sans-serif">¥ Million / month</text>
  <!-- X labels every 6 months -->
  <text x="69" y="213" text-anchor="middle" font-size="7.5" fill="#555" font-family="Segoe UI,sans-serif">M1</text>
  <text x="172" y="213" text-anchor="middle" font-size="7.5" fill="#555" font-family="Segoe UI,sans-serif">M6</text>
  <text x="296" y="213" text-anchor="middle" font-size="7.5" fill="#555" font-family="Segoe UI,sans-serif">M12</text>
  <text x="420" y="213" text-anchor="middle" font-size="7.5" fill="#555" font-family="Segoe UI,sans-serif">M18</text>
  <text x="544" y="213" text-anchor="middle" font-size="7.5" fill="#555" font-family="Segoe UI,sans-serif">M24</text>
  <text x="668" y="213" text-anchor="middle" font-size="7.5" fill="#555" font-family="Segoe UI,sans-serif">M30</text>
  <!-- Legend -->
  <rect x="120" y="225" width="12" height="8" fill="#b8c9ee"/><text x="136" y="233" font-size="7.5" fill="#444" font-family="Segoe UI,sans-serif">Phase 0</text>
  <rect x="200" y="225" width="12" height="8" fill="#6796e6"/><text x="216" y="233" font-size="7.5" fill="#444" font-family="Segoe UI,sans-serif">Phase 1</text>
  <rect x="280" y="225" width="12" height="8" fill="#e58520"/><text x="296" y="233" font-size="7.5" fill="#444" font-family="Segoe UI,sans-serif">Phase 2</text>
  <rect x="360" y="225" width="12" height="8" fill="#d94f4f"/><text x="376" y="233" font-size="7.5" fill="#444" font-family="Segoe UI,sans-serif">Phase 3 (peak spend M25–M26: ¥25M/month)</text>
</svg>

</div>

---

## 5. Current Performance Status

**Data Date: 2026-05-18 (End of Month 2)**

### 5.1 Status Narrative

The project is in **Phase 0 — Pre-Foundation**. Activities in progress include quiet stakeholder conversations with village leadership, preliminary charter drafting, and identifying founding team candidates. The Japanese co-founder search is underway but not yet resolved — this is the single most critical Phase 0 dependency.

Expenditure to date is personal travel, document translation, and a preliminary consultation with a Nara-based 行政書士. No major contracts have been signed.

### 5.2 Performance Metrics — Phase 0

| Metric | Value | Notes |
|--------|-------|-------|
| PV (Planned Value to date) | ¥0.15M | Planned spend through M2 |
| EV (Earned Value to date) | ¥0.12M | ~80% of planned Phase 0 work done |
| AC (Actual Cost to date) | ¥0.08M | Under plan — mostly personal time |
| **SV (Schedule Variance)** | **−¥0.03M** | Slightly behind: co-founder not yet identified |
| **CV (Cost Variance)** | **+¥0.04M** | Under budget: Phase 0 costs lower than planned |
| **SPI** | **0.80** | 80% of planned work achieved on schedule |
| **CPI** | **1.50** | Each ¥1 spent is delivering ¥1.50 of value |

<div style="page-break-inside:avoid; margin: 8pt 0">

**Figure 3 — Current EVM Performance Dashboard (Data Date: 2026-05-18)**

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 115" style="width:100%;display:block">
  <!-- PV box -->
  <rect x="10" y="10" width="150" height="90" rx="6" fill="#eef4ff" stroke="#6796e6" stroke-width="1.5"/>
  <text x="85" y="28" text-anchor="middle" font-size="9" fill="#4a7ac4" font-weight="bold" font-family="Segoe UI,sans-serif">PLANNED VALUE (PV)</text>
  <text x="85" y="55" text-anchor="middle" font-size="22" fill="#4a7ac4" font-weight="bold" font-family="Segoe UI,sans-serif">¥0.15M</text>
  <text x="85" y="72" text-anchor="middle" font-size="8" fill="#888" font-family="Segoe UI,sans-serif">Budgeted work scheduled</text>
  <text x="85" y="88" text-anchor="middle" font-size="8" fill="#888" font-family="Segoe UI,sans-serif">to date (end M2)</text>
  <!-- EV box -->
  <rect x="175" y="10" width="150" height="90" rx="6" fill="#eefff0" stroke="#4aaa60" stroke-width="1.5"/>
  <text x="250" y="28" text-anchor="middle" font-size="9" fill="#2a8040" font-weight="bold" font-family="Segoe UI,sans-serif">EARNED VALUE (EV)</text>
  <text x="250" y="55" text-anchor="middle" font-size="22" fill="#2a8040" font-weight="bold" font-family="Segoe UI,sans-serif">¥0.12M</text>
  <text x="250" y="72" text-anchor="middle" font-size="8" fill="#888" font-family="Segoe UI,sans-serif">Budgeted value of work</text>
  <text x="250" y="88" text-anchor="middle" font-size="8" fill="#888" font-family="Segoe UI,sans-serif">actually completed</text>
  <!-- AC box -->
  <rect x="340" y="10" width="150" height="90" rx="6" fill="#fff8ee" stroke="#e58520" stroke-width="1.5"/>
  <text x="415" y="28" text-anchor="middle" font-size="9" fill="#b05000" font-weight="bold" font-family="Segoe UI,sans-serif">ACTUAL COST (AC)</text>
  <text x="415" y="55" text-anchor="middle" font-size="22" fill="#b05000" font-weight="bold" font-family="Segoe UI,sans-serif">¥0.08M</text>
  <text x="415" y="72" text-anchor="middle" font-size="8" fill="#888" font-family="Segoe UI,sans-serif">Real spend to date</text>
  <text x="415" y="88" text-anchor="middle" font-size="8" fill="#888" font-family="Segoe UI,sans-serif">(travel, 行書士, docs)</text>
  <!-- SPI box -->
  <rect x="505" y="10" width="88" height="42" rx="6" fill="#fffbe6" stroke="#cca000" stroke-width="1.5"/>
  <text x="549" y="24" text-anchor="middle" font-size="8" fill="#886600" font-weight="bold" font-family="Segoe UI,sans-serif">SPI = 0.80</text>
  <text x="549" y="36" text-anchor="middle" font-size="7" fill="#886600" font-family="Segoe UI,sans-serif">🟡 Slightly behind</text>
  <text x="549" y="47" text-anchor="middle" font-size="6.5" fill="#aaa" font-family="Segoe UI,sans-serif">Co-founder search pending</text>
  <!-- CPI box -->
  <rect x="505" y="60" width="88" height="42" rx="6" fill="#eefff0" stroke="#4aaa60" stroke-width="1.5"/>
  <text x="549" y="74" text-anchor="middle" font-size="8" fill="#2a8040" font-weight="bold" font-family="Segoe UI,sans-serif">CPI = 1.50</text>
  <text x="549" y="86" text-anchor="middle" font-size="7" fill="#2a8040" font-family="Segoe UI,sans-serif">🟢 Under budget</text>
  <text x="549" y="97" text-anchor="middle" font-size="6.5" fill="#aaa" font-family="Segoe UI,sans-serif">Phase 0 personal-time effect</text>
  <!-- BAC label -->
  <text x="605" y="55" text-anchor="middle" font-size="7.5" fill="#666" font-weight="bold" font-family="Segoe UI,sans-serif">BAC</text>
  <text x="605" y="67" text-anchor="middle" font-size="9" fill="#333" font-weight="bold" font-family="Segoe UI,sans-serif">¥220M</text>
  <text x="605" y="79" text-anchor="middle" font-size="6.5" fill="#999" font-family="Segoe UI,sans-serif">0.04% spent</text>
</svg>

</div>

> **Note:** CPI of 1.50 at Month 2 is partly a Phase 0 artefact — most value creation is through personal time rather than budgeted spend. Do not extrapolate CPI to total project forecast until Phase 1 feasibility contracts are in place.

### 5.3 Phase 0 Forecast

| Metric | Value |
|--------|-------|
| Phase 0 BAC | ¥0.25M |
| EAC (Phase 0) = AC + (BAC−EV)÷CPI | ¥0.16M |
| ETC (Phase 0) = EAC − AC | ¥0.08M |
| VAC (Phase 0) = BAC − EAC | **+¥0.09M under budget** |
| TCPI | 0.87 — need only 0.87 efficiency to finish Phase 0 within budget |

---

<div class="page-break"></div>

## 6. Phase-by-Phase Forecast (Baseline Projections)

These projections assume execution at the planned efficiency levels. They will be revised monthly from Phase 1 onwards when contract values and feasibility study costs are confirmed.

### 6.1 Phase 0 — Pre-Foundation

| Item | Value |
|------|-------|
| Duration | M1–M3 (Apr–Jun 2026) |
| BAC | ¥0.25M |
| Planned end date | 2026-06-30 |
| Key gate | Founding team verbal commitments; village leadership informed |
| Current forecast end | On track for Jun 2026 |
| Current forecast cost | ¥0.16–0.22M |

### 6.2 Phase 1 — Foundation

| Item | Value |
|------|-------|
| Duration | M4–M9 (Jul–Dec 2026) |
| BAC | ¥5.5M |
| Planned end date | 2026-12-31 |
| Key gate | ¥3–8M secured; legal entity registered; feasibility studies complete |
| Critical path | Forestry + Energy feasibility studies (procurement Q3 2026) |
| Primary risk | Government grant approvals often take 2–3 months longer than planned |
| Contingency plan | Reduce feasibility scope slightly; delay P2 start by 1–2 months |

### 6.3 Phase 2 — Pilot Design

| Item | Value |
|------|-------|
| Duration | M10–M18 (Jan–Sep 2027) |
| BAC | ¥22.25M |
| Planned end date | 2027-09-30 |
| Key gate | ¥30–50M secured; detailed engineering complete; key permits in hand |
| Critical path | METI permitting + FIT registration (can take 6+ months) |
| Primary risk | Permit delays push Phase 3 start past Oct 2027 |
| Contingency plan | Stage Phase 3 procurement independently of permit approvals for non-permit items |

### 6.4 Phase 3 — Pilot Build

| Item | Value |
|------|-------|
| Duration | M19–M30 (Oct 2027–Sep 2028) |
| BAC | ¥177M |
| Planned end date | 2028-09-30 |
| Key gate | Revenue operational; Phase 4 plan confirmed |
| Critical path | Building renovation → solar/battery install → EV charging → commissioning |
| Primary risk | Building structural findings requiring scope increase (currently low probability, high impact) |
| Contingency plan | Phase 3 WBS 5.9 includes ¥27M contingency (18%); Management Reserve of ¥25M backstop |

---

## 7. Three-Scenario Forecast

For a project with this level of regulatory and geographic complexity, planning in three scenarios is more honest than a single-point estimate.

| Scenario | Description | EAC | End Date |
|----------|-------------|-----|----------|
| **Optimistic** | All grants awarded on first application; building in good condition; no permit delays; lower-bound vendor quotes | ¥185M | Aug 2028 |
| **Base Case** | One major permit delay (+2 months); one grant deferred to Year 2; CPI ≈ 1.0; mid-range vendor quotes | **¥220M** | Sep 2028 |
| **Pessimistic** | Two permit delays; building remediation required; government grant shortfall — draws on MR and beyond | ¥285M | Mar 2029 |

> The scenario band is intentionally wider than the Rev 0 baseline. Phase 1 feasibility studies (M9) will narrow the range substantially once school structural condition, vendor quotes, and grant awards are confirmed.

<div style="page-break-inside:avoid; margin: 8pt 0">

**Figure 4 — Three-Scenario EAC Comparison**

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 175" style="width:100%;display:block">
  <!-- Background -->
  <rect x="160" y="10" width="500" height="140" fill="#fafafa" stroke="#ddd" stroke-width="0.5" rx="3"/>
  <!-- New scale: 500px / 300M = 1.667 px/¥M -->
  <!-- BAC reference line: 220M → x = 160 + 220*1.667 = 160 + 367 = 527 -->
  <line x1="527" y1="10" x2="527" y2="155" stroke="#6796e6" stroke-width="1" stroke-dasharray="5,3"/>
  <text x="527" y="166" text-anchor="middle" font-size="7.5" fill="#6796e6" font-weight="bold" font-family="Segoe UI,sans-serif">BAC ¥220M</text>
  <!-- MR limit: 245M → x = 160 + 245*1.667 = 160 + 408 = 568 -->
  <line x1="568" y1="10" x2="568" y2="155" stroke="#e58520" stroke-width="1" stroke-dasharray="3,3"/>
  <text x="568" y="176" text-anchor="middle" font-size="7" fill="#e58520" font-family="Segoe UI,sans-serif">Total Budget ¥245M</text>
  <!-- X axis labels: 0, 75, 150, 225, 300 -->
  <text x="160" y="166" text-anchor="middle" font-size="7.5" fill="#666" font-family="Segoe UI,sans-serif">0</text>
  <text x="285" y="166" text-anchor="middle" font-size="7.5" fill="#666" font-family="Segoe UI,sans-serif">75</text>
  <text x="410" y="166" text-anchor="middle" font-size="7.5" fill="#666" font-family="Segoe UI,sans-serif">150</text>
  <text x="535" y="166" text-anchor="middle" font-size="7.5" fill="#666" font-family="Segoe UI,sans-serif">225</text>
  <text x="660" y="166" text-anchor="middle" font-size="7.5" fill="#666" font-family="Segoe UI,sans-serif">300 ¥M</text>
  <!-- Optimistic: 185M → w = 185*1.667 = 308 -->
  <rect x="160" y="22" width="308" height="30" fill="#4aaa60" rx="3"/>
  <text x="148" y="40" text-anchor="end" font-size="8.5" fill="#222" font-weight="bold" font-family="Segoe UI,sans-serif">Optimistic</text>
  <text x="155" y="50" text-anchor="end" font-size="7" fill="#555" font-family="Segoe UI,sans-serif">Aug 2028</text>
  <text x="476" y="41" font-size="9" fill="#222" font-weight="bold" font-family="Segoe UI,sans-serif">¥185M  (−¥35M vs BAC)</text>
  <!-- Base: 220M → w = 220*1.667 = 367 -->
  <rect x="160" y="62" width="367" height="30" fill="#6796e6" rx="3"/>
  <text x="148" y="80" text-anchor="end" font-size="8.5" fill="#222" font-weight="bold" font-family="Segoe UI,sans-serif">Base Case</text>
  <text x="155" y="90" text-anchor="end" font-size="7" fill="#555" font-family="Segoe UI,sans-serif">Sep 2028</text>
  <text x="535" y="81" font-size="9" fill="#222" font-weight="bold" font-family="Segoe UI,sans-serif">¥220M  (on budget)</text>
  <!-- Pessimistic: 285M → w = 285*1.667 = 475 -->
  <rect x="160" y="102" width="475" height="30" fill="#d94f4f" rx="3"/>
  <text x="148" y="120" text-anchor="end" font-size="8.5" fill="#222" font-weight="bold" font-family="Segoe UI,sans-serif">Pessimistic</text>
  <text x="155" y="130" text-anchor="end" font-size="7" fill="#555" font-family="Segoe UI,sans-serif">Mar 2029</text>
  <text x="643" y="121" font-size="9" fill="#222" font-weight="bold" font-family="Segoe UI,sans-serif">¥285M</text>
  <text x="168" y="121" font-size="7.5" fill="white" font-family="Segoe UI,sans-serif">Exceeds total budget — requires additional funding round or scope reduction</text>
  <!-- X gridlines -->
  <line x1="285" y1="10" x2="285" y2="155" stroke="#ddd" stroke-width="0.4"/>
  <line x1="410" y1="10" x2="410" y2="155" stroke="#ddd" stroke-width="0.4"/>
  <line x1="535" y1="10" x2="535" y2="155" stroke="#ddd" stroke-width="0.4"/>
</svg>

</div>

> The pessimistic scenario at ¥285M **exceeds the total approved budget of ¥245M by ¥40M** and would trigger a Gate 3 funding decision: either (a) raise an additional funding round, (b) reduce Phase 3 scope (e.g., defer EV chargers or fiber upgrade), or (c) extend the schedule and stage construction. Absolute failure scenarios (community resistance, no funding at Gate 1) are still managed at the funding gate level, not the EVM level.

---

## 8. Performance Thresholds and Escalation

EVM metrics trigger review actions at the following levels. Thresholds are intentionally tighter in early phases when course-correction is cheapest.

| Threshold | SPI or CPI | Action |
|-----------|------------|--------|
| **Green** | 0.95 – 1.10 | Normal reporting; no action required |
| **Yellow** | 0.85 – 0.94 | Representative Director notified; recovery plan drafted within 2 weeks |
| **Orange** | 0.75 – 0.84 | Board briefing required; recovery plan presented with options |
| **Red** | < 0.75 | Formal board review; consider phase rescoping or Management Reserve draw |

**Schedule threshold override**: If SPI < 0.90 at any funding gate checkpoint, the gate decision is automatically deferred pending a recovery assessment, regardless of CPI.

### 8.1 Liquidity control — cash balance is a hard rule

SPI/CPI measure *efficiency*; they do not tell you whether cash is in the bank. Because inflow arrives in lumps while spend is continuous (see `mitsue_cashflow_model.md`), the project separately tracks the **monthly cash balance = cumulative cash-in − cumulative cash-out** against a mandatory floor:

| Liquidity floor | Rule |
|---|---|
| **Phases 0–2** | Balance must stay **≥ ¥5M** (≥ ¥3M absolute minimum at the M7 pinch, when founder capital is the only inflow) |
| **Phase 3** | Balance must stay **≥ one month of planned burn** (≥ ¥25M at the M25–M26 ¥25M/mo peak) |
| **Breach forecast** | If the 3-month rolling balance forecast projects a floor breach, the Representative Director triggers a tranche pull-forward or bridge draw **before** the breach month |

These floors are **hard rules, not targets**: a projected breach is a stop/act condition equal in weight to a Red SPI/CPI. The monthly report tracks **balance, not just spend** (§9).

---

## 9. EVM Reporting Cadence

| Frequency | Report | Recipients | Content |
|-----------|--------|------------|---------|
| **Monthly** | EVM Status Update | Board, key funders | PV/EV/AC table; SPI/CPI; SV/CV; EAC update; **cash balance vs §8.1 liquidity floor + 3-month balance forecast**; issues |
| **At each Gate** | Gate Review Package | Board + major funders | Full EVM review; scenario forecast; go/no-go recommendation |
| **Quarterly** | Stakeholder Summary | Village government, advisors | High-level cost and schedule status; milestone progress |
| **Annual** | Year-End Review | All stakeholders | Full financial report; EVM audit; next-year baseline |

Monthly reports are generated from OpenProject time tracking + invoicing. The first formal monthly EVM report is due **2026-06-30** (end of Phase 0). From Phase 1 onward, every monthly report carries the cash-balance line (cum-in − cum-out) against the §8.1 floor — the project tracks **balance, not just spend**.

---

## 10. Assumptions and Constraints

**Assumptions**
- Project start date: 2026-04-01 (Month 1)
- All phase durations are calendar months, including Japanese holidays
- Feasibility studies are awarded to single vendors per study; no multi-vendor splits
- Phase 3 construction prices are based on 2026 Nara Prefecture rural construction indices, with a 15–25% rural mobilisation premium applied to commercial benchmarks for solar PV, EV charging, and seismic retrofit work
- Exchange rate assumptions (for Dutch/international corporate partnerships): ¥150/EUR
- Forestry operations are weather-dependent; M19–M23 baseline avoids typhoon season
- **The ¥28M funding gap is closed and disbursable before Gate 3 (M21).** Even in the best case where the ¥192M target stack lands as planned (none of it secured today), the cash balance runs negative at **M28 (Jul 2028)**, the shortfall equalling the gap exactly (see `mitsue_cashflow_model.md` §5)

**Constraints**
- BAC of ¥220M is a **ceiling**; Phase 3 cannot proceed without confirmed funding at Gate 3
- Management Reserve requires board approval for any drawdown
- **The §8.1 liquidity floor is binding:** the monthly cash balance may not fall below the floor; funding tranches must be scheduled to land before the spend they cover
- **Phase-3 funding tranches must be contracted 2–3 months ahead of their planned disbursement month** to absorb grant pay-in-arrears lag
- **A ~¥25M bridge facility** (bank line, Management Reserve draw, or signed-grant advance) must be arranged before Gate 3 as the working-capital shock absorber for the M22–M28 burn peak
- EVM data must be reported in JPY; foreign currency transactions converted at transaction-date rate
- The Phase 1 feasibility studies are the **single largest driver of overall project accuracy** — all EAC figures before M9 carry high uncertainty (±40%)

---

## 11. Limitations and Honest Caveats

This is an **early-stage EVM plan** written at Month 2 of a 30-month project. The following limitations apply:

1. **CPI and SPI at Month 2 are not statistically reliable.** With only ¥0.08M of actual cost data, the performance indices reflect Phase 0 characteristics (personal time, low hard costs) rather than the project overall. Trust these numbers only after ¥2–3M of Phase 1 costs are confirmed.

2. **The Phase 3 budget range is wide.** The ¥120–290M range from the implementation plan reflects genuine uncertainty about building condition (¥30–100M school renovation range alone), equipment procurement conditions, and grid connection costs. The EVM baseline uses ¥177M for WBS 5.0; the ¥27M Phase 3 contingency (18%) and ¥25M Management Reserve exist precisely to absorb this range.

3. **Funding gate gating is the primary control mechanism.** EVM monitors cost and schedule efficiency within a phase; the funding gates control whether the next phase begins at all. These two controls are complementary, not redundant.

4. **Phase 1 feasibility studies will substantially revise this baseline.** After M9, expect a formal baseline revision (Rev 2). The revised Phase 2 and Phase 3 budgets will be anchored to real survey data — particularly the school structural assessment and vendor quotes — not Japan-market benchmarks.

---

## 12. Baseline Revision Policy

The PMB may be formally revised:
- After completion of Phase 1 feasibility studies (mandatory revision at M9)
- At any funding gate when confirmed funding differs from planned by more than ±20%
- When board-approved scope changes are incorporated
- When Management Reserve is drawn down

Each baseline revision is documented with: old baseline, new baseline, reason, approving authority, and date. Revisions are numbered:
- **Rev 0** (v1.1, Apr 2026) — Original BAC ¥168M, drafted from planning estimates
- **Rev 1** (v2.0, May 2026) — Current document. BAC ¥220M, reality-checked against real-world Japan benchmarks (solar, EV chargers, school seismic retrofit, forestry). Reason: pre-emptive correction in advance of Phase 1 feasibility studies.
- **Rev 2** (planned M9, Dec 2026) — Post-Phase 1 revision anchored to feasibility study results and vendor quotes. **Should also fold in any confirmed 地域脱炭素移行・再エネ推進交付金 amount** (2/3–3/4 subsidy on solar/battery/EV/private-wire capex, via village 官民連携) — the primary named path to closing the ¥28M–¥53M gap during Phases 2–3, which **must be secured and disbursable before Gate 3 (M21)**, not deferred to end-of-project (see `mitsue_cashflow_model.md` §5). Rev 2 must also **re-time the cashflow model to the live Gantt** in lockstep with the cost re-sync, and fold in confirmed 交付金 disbursement dates and any bridge-loan terms. Sources: https://policies.env.go.jp/policy/roadmap/grants/ · https://www.env.go.jp/content/900470616.pdf

**Two additional FY2026 subsidy tracks (identified 2026-07-06)** — both fund the biomass-power-plus-data-center model directly and should be evaluated at Rev 2:
  - **経産省 GX地域共創補助金 (脱炭素電源地域貢献型投資促進事業)** — ¥210B FY2026 pool, integrated support for *decarbonized power + DC/factory* build-out; Round 1 Jul–Sep 2026, Round 2 autumn–winter 2026, 38 regions pre-screened. Strongest structural match (biomass power + compute co-located). Source: https://sustainablejapan.jp/2026/05/30/meti-gx-local/126036
  - **環境省 データセンターのゼロエミッション化・地域共生加速化事業** — up to ¥1B/project on DC-linked renewable + battery equipment. ⚠️ FY2026 application deadline **2026-07-03 (passed)**; target the FY2027 cycle. Source: https://sustainablejapan.jp/2026/06/07/japan-datacenter-renewable-energy/126312

---

## 13. Founder Compensation & Sustainability

Early-phase founder time has been **largely unpaid**, representing the project's single most significant hidden dependency and top operational risk (see also the Implementation Plan's Risk Management table).

**Target compensation.** The Representative Director's target is **¥300,000/month (¥3.6M/yr)** — a defensible full-time-equivalent figure for rural Japan. This is a *target and norm*, **not a legal requirement**: a 一般社団法人 director may legally be unpaid; if paid, the amount must be set by **社員総会 (members' meeting) resolution**, not self-determined. For an NPO法人, pay for actual work performed by a director as staff (役員給与) is uncapped and separate from capped 役員報酬 for the role itself; once revenue is earned, salary must comply with 定期同額給与 tax rules.

> **Sources:** https://www.koueki-houjin.net/shadan/hosyu.html · https://www.koueki-houjin.net/shadan/kyuyo.html · https://ashiyakaikei.com/directors-npo/ · https://cliser.co.jp/non-profit/npo/159/

**Phasing plan:**

| Period | Compensation | Funding source |
|--------|--------------|----------------|
| Phase 0–1 (M1–M9) | Volunteer / nominal stipend | Founder capital; personal commitment |
| Phase 2 (M10–M18) | Partial stipend, ramping toward target | Layer-1 founding capital + first grants |
| Phase 3+ (M19+) | Full ¥300k/mo target | Phase 2 grants (¥30–50M) once confirmed |

WBS 1.1a (¥5.0M over 30 months, ~¥167k/month average) covers the ramp inside the baseline. Reaching the full ¥300k/month run-rate from M10 is contingent on Phase 2 grant funding and will be confirmed at **Baseline Rev 2 (M9, December 2026)**.

Layer-1 founding capital is earmarked to cover the Phase 0–1 founder stipend so that early runway does not depend on entirely unpaid time.

The same phasing logic extends to the JP co-founder if that role is compensated — terms to be agreed and documented in the Founder Agreement before Phase 1.

---

## 14. Phase 4 Forward Capital — Biomass Fuel-Prep & CHP (out of PMB)

This section is **informational and explicitly outside the ¥220M Performance
Measurement Baseline**. It captures the scale-up capital for the biomass energy loop
so funders can see the full trajectory; it does **not** alter the BAC. Phase 4 is
funded by operating revenue + grants (see `mitsue_revenue_model.md`), not the PMB.

Sizing per the Forest Twin doubled-workforce baseline (~50% of forest under management,
~13,000 dry-t/yr fuel, 2×0.6 MWe). See `mitsue_forest_workforce_energy_plan.md` §5–6.

| Bucket | Item | Forward capital (¥M) | Funding |
|---|---|---|---|
| F1 | Biomass CHP gensets (2×0.6 MWe gasifier-genset) | ~800 | Revenue + FIT + 再エネ交付金 |
| F2 | Fuel-prep — active dryer, chip store, screening, handling, yard | ~75–215 (mid ~120) | Revenue + grants; existing 牛峠工場 offsets ¥30–70 |
| F3 | Thermal store (molten-salt / packed-bed) + island-mode battery | *TBD (feasibility)* | 国土強靱化 / 緊急防災債 |
| F4 | Network connectivity to 神末797 (anchor compute) — NTT/leased-line or microwave-backup assessment + build | *TBD (feasibility)* | Revenue + grants |
| | **Indicative Phase 4 forward capital** | **~¥0.9–1.0 B + F4** | out-of-PMB |

**Relationship to the PMB:** the Phase 3 pilot already carries a small forestry line
(WBS 5.6, ¥25M, 5–10 ha harvest + replant). A **pilot-scale drying line** legitimately
sits within that WBS; the full fuel-prep chain and the CHP fleet above are Phase 4.
When Phase 4 is baselined (Year 2, after Phase 1 feasibility confirms accessible forest
area and vendor quotes), these buckets become a separate Phase 4 PMB with its own BAC.

**F4 is a separate connectivity problem from WBS 3.5/5.7.** Those PMB line items
(¥0.4M assessment + ¥10M upgrade) are scoped to the **old-school showcase DC** only.
神末797 (the anchor-compute site, co-located with the CHP) is a different, more remote
location — its connectivity has not been assessed and should not be assumed to piggyback
on the school's fiber build. Cost it alongside the grid 事前相談 already underway for
神末 (see `mitsue_fit_grid_check.md` §"Grid interconnection"), once NTT/ISP reach and a
microwave-backup option are scoped.

> **Do not sum F1–F3 into the ¥245M total budget.** They belong to a later, separately
> funded phase and are shown here only for trajectory transparency.

---

*Rob Oudendijk — YR-Design / Safecast*
*Mitsue, Nara Prefecture, Japan*
*May 2026*
