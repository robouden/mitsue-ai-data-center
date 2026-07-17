<div style="font-family:-apple-system,Helvetica,Arial,sans-serif;">
<p style="font-size:7.5pt; font-weight:600; letter-spacing:0.25em; color:#3a7a5a; margin:0 0 4mm;">PROJECT DOCUMENT</p>
<h1 style="font-size:28pt; font-weight:700; margin:0 0 2mm; border-bottom:1px solid #eee; padding-bottom:2mm;">BIOMASS ENERGY & AI</h1>
<p style="font-style:italic; color:#666; margin:1mm 0 0;">Reforesting in Mitsue</p>
<p style="font-style:italic; color:#666; margin:2mm 0 8mm;">Business Case & Decision Framework</p>
<img src="assets/logo_go.png" alt="御" width="50%" style="display:block;margin:0 auto;">
<div style="height:105mm;"></div>
<table style="width:100%; border-collapse:collapse; font-size:9pt;">
<tr><td style="padding:3mm 4mm; border:1px solid #ccc; font-weight:bold; width:30%;">Version</td><td style="padding:3mm 4mm; border:1px solid #ccc;">v1.6</td></tr>
<tr><td style="padding:3mm 4mm; border:1px solid #ccc; font-weight:bold;">Date</td><td style="padding:3mm 4mm; border:1px solid #ccc;">2026-07-17</td></tr>
<tr><td style="padding:3mm 4mm; border:1px solid #ccc; font-weight:bold;">Author</td><td style="padding:3mm 4mm; border:1px solid #ccc;">Rob Oudendijk</td></tr>
</table>
</div>

<div style="page-break-after:always; break-after:page; height:0; margin:0; padding:0;"></div>

---

# BIOMASS ENERGY & AI — Business Case & Decision Framework
### Reforesting in Mitsue

### The "Why Say Yes" Layer

> **"The forest our ancestors planted — the power that sustains the village they built"**
> 先人が植えた森が、今、村を支える力になる。

*This document sits **above** the [Implementation Plan](mitsue_implementation_plan.md). The implementation plan answers "what we will build and when." This document answers the question every decision-maker actually asks: **"Why should I say yes, and what do I get?"** It consolidates the financial and decision logic scattered across the revenue model, funding flowchart, EVM, and risk register, and fills the three gaps those documents leave open: (1) the entity & financing structure, (2) the alternatives the village is really choosing between, and (3) whole-project return, residual risk, and decision authority.*

*All financial figures are illustrative early-stage estimates consistent with [`mitsue_revenue_model.md`](mitsue_revenue_model.md) and [`mitsue_evm_plan.md`](mitsue_evm_plan.md). Phase 1 feasibility studies (due M9, Dec 2026) replace them with vetted figures.*

---

## 1. Entity & Financing Structure — what each funder gets

The project raises money three ways — **grants, equity, and revenue/energy-share (no debt)**. These cannot all live in one organisation: a Japanese non-profit (一般社団法人 / NPO法人) **cannot issue equity or distribute profit to investors**. The project therefore uses a deliberate **two-tier structure**, which is also its mission-protection mechanism.

### 1.1 The two tiers

| | **Tier 1 — Mission entity** | **Tier 2 — Operating company** |
|---|---|---|
| Form | 一般社団法人 (non-profit) | 合同会社 GK (for-profit) |
| Holds | Charter, 官民連携 relationship with village, brand, IP/"playbook", forestry-restoration programme, J-Credit registration | Data-center assets, energy plant (biomass CHP, solar, battery), grid/FIT contracts, hosting contracts, staff |
| Receives | Founder capital, government grants, foundation grants — **all non-distributing** | Equity investment, revenue/energy-share contracts, operating revenue |
| Controls | **Owns the majority of the GK** + holds a charter "mission-lock" clause | Operated under contract to the mission entity |
| Returns to funders | None — return *is* the mission (public benefit) | Dividends / revenue-share from operating surplus |

The mission entity owns and controls the operating company. Grant money (which legally cannot generate private profit) stays in Tier 1 or funds shared infrastructure; investor money that expects a return sits in Tier 2, where returns are legal and contractual. The 交付金 (MoE decarbonization grant) flows to the **village**, which co-invests the subsidized capex into the shared energy assets via the 官民連携 partnership.

### 1.2 What each funding layer is, and what it gets back

| Layer | Source | ¥M | Instrument | What they get |
|---|---|---|---|---|
| L1 | Founders (Rob + JP co-founder) | 6 | Founder equity in GK + sweat | Minority equity; mission stewardship |
| L2 | Government grants (national/pref./village) incl. **交付金 2/3–3/4 capex subsidy** | 115 | Non-refundable grant (to village / Tier 1) | RE-plan targets met; depopulation/carbon outcomes; no financial return expected |
| L3 | Foundations | 33 | Mission-restricted grant | SDG/impact outcomes; reporting; brand association |
| L4 | Corporate partners | 35 | **Choice of:** CSR grant · minority GK equity · prepaid hosting (revenue advance) · energy-share offtake | Green-compute capacity, ESG story, or contracted return depending on instrument chosen |
| L5 | Operating revenue | 3+ | Reinvested surplus | — |
| **Gap** | To close ¥28–53M | 28–53 | Additional 交付金 + corporate GK equity + revenue-financing | As per L2/L4 above |

### 1.2a How money and goods actually move between the two tiers

(Added 2026-07-17.) The tables above describe *what each layer gets*; this shows *how it flows* —
goods/services (green, solid) vs. money (gold, dashed) vs. governance (grey, dotted) — between
the two real legal entities.

<div style="page-break-inside:avoid; margin: 10pt 0">

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 300" style="width:100%;display:block">
  <defs>
    <marker id="bgood" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="#2f7d4f"/>
    </marker>
    <marker id="bmoney" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="#b8860b"/>
    </marker>
    <marker id="bgov" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="5.5" markerHeight="5.5" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="#8a949a"/>
    </marker>
  </defs>
  <!-- legend -->
  <line x1="0" y1="6" x2="22" y2="6" stroke="#2f7d4f" stroke-width="2"/>
  <text x="27" y="9" font-size="9.5" fill="#3d4a52">Goods / services</text>
  <line x1="150" y1="6" x2="172" y2="6" stroke="#b8860b" stroke-width="2" stroke-dasharray="4 3"/>
  <text x="177" y="9" font-size="9.5" fill="#3d4a52">Money</text>
  <line x1="255" y1="6" x2="277" y2="6" stroke="#8a949a" stroke-width="1.8" stroke-dasharray="1.5 2.5"/>
  <text x="282" y="9" font-size="9.5" fill="#3d4a52">Governance / advisory</text>
  <!-- External funders row -->
  <rect x="10" y="26" width="150" height="46" rx="3" fill="#f4f7f8" stroke="#d5dbde"/>
  <text x="85" y="45" text-anchor="middle" font-size="10" font-weight="700" fill="#16323d">Founders (L1)</text>
  <text x="85" y="58" text-anchor="middle" font-size="8" fill="#7a868d">¥6M · sweat + capital</text>
  <text x="85" y="68" text-anchor="middle" font-size="8" fill="#7a868d">Rob + JP co-founder</text>
  <rect x="183" y="26" width="150" height="46" rx="3" fill="#f4f7f8" stroke="#d5dbde"/>
  <text x="258" y="41" text-anchor="middle" font-size="10" font-weight="700" fill="#16323d">Government grants (L2)</text>
  <text x="258" y="54" text-anchor="middle" font-size="8" fill="#7a868d">via village 官民連携</text>
  <text x="258" y="65" text-anchor="middle" font-size="8" fill="#7a868d">¥115M · 交付金 2/3–3/4</text>
  <rect x="356" y="26" width="150" height="46" rx="3" fill="#f4f7f8" stroke="#d5dbde"/>
  <text x="431" y="45" text-anchor="middle" font-size="10" font-weight="700" fill="#16323d">Foundations (L3)</text>
  <text x="431" y="58" text-anchor="middle" font-size="8" fill="#7a868d">¥33M · mission-restricted</text>
  <text x="431" y="68" text-anchor="middle" font-size="8" fill="#7a868d">grant</text>
  <rect x="529" y="26" width="161" height="46" rx="3" fill="#f4f7f8" stroke="#d5dbde"/>
  <text x="609" y="41" text-anchor="middle" font-size="10" font-weight="700" fill="#16323d">Corporate partners (L4)</text>
  <text x="609" y="54" text-anchor="middle" font-size="8" fill="#7a868d">¥35M · CSR grant / equity /</text>
  <text x="609" y="65" text-anchor="middle" font-size="8" fill="#7a868d">prepaid hosting / offtake</text>
  <!-- Tier boxes -->
  <rect x="20" y="120" width="300" height="150" rx="4" fill="#fff" stroke="#bfe0cc" stroke-width="1.4"/>
  <rect x="20" y="120" width="300" height="22" rx="4" fill="#2f7d4f"/>
  <text x="170" y="135" text-anchor="middle" font-size="10.5" font-weight="700" fill="#fff" letter-spacing="0.03em">TIER 1 · MISSION ENTITY</text>
  <text x="170" y="153" text-anchor="middle" font-size="8.5" fill="#7a868d">一般社団法人 (or NPO法人)</text>
  <text x="34" y="170" font-size="8.3" fill="#3d4a52">Charter · 官民連携 relationship · brand / IP</text>
  <text x="34" y="182" font-size="8.3" fill="#3d4a52">"playbook" · forest-restoration programme ·</text>
  <text x="34" y="194" font-size="8.3" fill="#3d4a52">J-Credit registration.</text>
  <text x="34" y="211" font-size="8.3" font-weight="700" fill="#2f7d4f">Owns majority of GK + mission-lock clause.</text>
  <text x="34" y="228" font-size="8" font-weight="700" fill="#16323d">Receives:</text>
  <text x="34" y="240" font-size="8" fill="#3d4a52">founder capital, government grants, foundation</text>
  <text x="34" y="251" font-size="8" fill="#3d4a52">grants (all non-distributing) + GK dividends</text>
  <rect x="380" y="120" width="300" height="150" rx="4" fill="#fff" stroke="#c7cdf0" stroke-width="1.4"/>
  <rect x="380" y="120" width="300" height="22" rx="4" fill="#3a55c4"/>
  <text x="530" y="135" text-anchor="middle" font-size="10.5" font-weight="700" fill="#fff" letter-spacing="0.03em">TIER 2 · OPERATING COMPANY</text>
  <text x="530" y="153" text-anchor="middle" font-size="8.5" fill="#7a868d">合同会社 (GK)</text>
  <text x="394" y="170" font-size="8.3" fill="#3d4a52">Data-center assets · biomass CHP + solar +</text>
  <text x="394" y="182" font-size="8.3" fill="#3d4a52">battery · grid / FIT contracts · hosting</text>
  <text x="394" y="194" font-size="8.3" fill="#3d4a52">contracts · staff.</text>
  <text x="394" y="211" font-size="8.3" font-weight="700" fill="#3a55c4">Operated under contract to the mission entity.</text>
  <text x="394" y="228" font-size="8" font-weight="700" fill="#16323d">Receives:</text>
  <text x="394" y="240" font-size="8" fill="#3d4a52">founder + corporate equity, revenue/energy-</text>
  <text x="394" y="251" font-size="8" fill="#3d4a52">share contracts, operating revenue</text>
  <!-- Founders -> Tier1 / Tier2 -->
  <path d="M60,72 C 70,95 100,108 130,118" fill="none" stroke="#b8860b" stroke-width="1.6" stroke-dasharray="4 3" marker-end="url(#bmoney)"/>
  <text x="62" y="100" font-size="7.6" fill="#b8860b">founder capital + sweat</text>
  <path d="M130,72 C 250,100 350,105 400,118" fill="none" stroke="#b8860b" stroke-width="1.6" stroke-dasharray="4 3" marker-end="url(#bmoney)"/>
  <text x="243" y="111" font-size="7.6" fill="#b8860b">minority equity (GK)</text>
  <!-- Govt grants -> Tier1 -->
  <path d="M258,72 L 220,118" fill="none" stroke="#b8860b" stroke-width="1.8" stroke-dasharray="4 3" marker-end="url(#bmoney)"/>
  <text x="222" y="91" font-size="7.6" fill="#b8860b">交付金 (non-distributing)</text>
  <!-- Foundations -> Tier1 -->
  <path d="M420,72 C 380,95 320,105 260,118" fill="none" stroke="#b8860b" stroke-width="1.6" stroke-dasharray="4 3" marker-end="url(#bmoney)"/>
  <text x="330" y="112" font-size="7.6" fill="#b8860b">mission-restricted grant</text>
  <!-- Corporate -> Tier2 (equity/hosting) -->
  <path d="M600,72 L 570,118" fill="none" stroke="#b8860b" stroke-width="1.8" stroke-dasharray="4 3" marker-end="url(#bmoney)"/>
  <text x="522" y="100" font-size="7.6" fill="#b8860b">equity / prepaid hosting / offtake</text>
  <!-- Corporate -> Tier1 (CSR grant alt) -->
  <path d="M560,72 C 460,105 350,120 322,132" fill="none" stroke="#b8860b" stroke-width="1.3" stroke-dasharray="2 3" marker-end="url(#bmoney)" opacity="0.75"/>
  <text x="418" y="112" font-size="7.2" fill="#b8860b" opacity="0.85">or: CSR grant direct to Tier 1</text>
  <!-- Tier1 <-> Tier2 core loop -->
  <path d="M322,148 L 378,148" fill="none" stroke="#8a949a" stroke-width="1.5" stroke-dasharray="1.5 2.5" marker-end="url(#bgov)"/>
  <text x="325" y="151" font-size="7.2" fill="#8a949a">owns majority + mission-lock</text>
  <path d="M378,168 L 322,168" fill="none" stroke="#b8860b" stroke-width="1.8" stroke-dasharray="4 3" marker-end="url(#bmoney)"/>
  <text x="327" y="165" font-size="7.4" font-weight="700" fill="#b8860b">dividends</text>
</svg>

</div>

<p style="font-size:8.5pt; color:#666; margin-top:2mm;"><i>Reading it: every money line into Tier 1 is non-distributing by law — it funds mission activity, not investor return. Every money line into Tier 2 is a real financial instrument (equity, revenue-share) because Tier 2 is where legal profit distribution is possible at all. The only money flowing back <b>out</b> of Tier 2 is to Tier 1 (dividends, since Tier 1 owns the majority) — there is no path for grant money to leak into a private return, and no path for investor capital to bypass Tier 2's contractual bounds.</i></p>

### 1.3 Mission-lock — why investors cannot capture the project

Because equity exists only in Tier 2 and the Tier-1 non-profit holds the majority plus a charter clause, investors get a **real but minority** return and **cannot redirect the mission, sell the forest programme, or strip the community assets**. This is the answer to "what am I committing to / what do you promise": grant funders commit to a public good and are promised outcomes; equity/revenue-share investors commit capital to Tier 2 and are promised a contracted share of a defined operating surplus — bounded so the village always retains control.

### 1.4 Return profile (illustrative, base case)

Operating surplus accrues in the GK: **net surplus ¥10–32M/yr by Year 5**, project-level capital payback **10–18 years**. Equity-investor return depends on entry valuation and share, both set in Phase 2 once feasibility figures exist — **this document defines the *structure*; Phase 2 sets the *price*.** No instrument promises a return the operating surplus cannot support.

<div class="page-break"></div>

## 2. Alternatives Analysis — what the village is really choosing between

Every decision-maker has a "do nothing" option. For the village it is concrete: **underused space stays underused.** The project will choose its premises from **several candidate sites**, all underused village building stock. One strong candidate is the **former Sugano Elementary School (Koryukan / みつえ体験交流館)** — a former wooden elementary school that today operates under the name Mitsue Taiken Koryukan as a cultural and educational facility but has empty, underused classrooms; here the hub would occupy spare capacity and **complement** the Koryukan's existing crafts-and-experience role rather than replace it. Disused former factory or workshop buildings are other candidates. Final site selection is a Phase 1 decision.

> **Note on the dome school:** the dome school is a *separate* building, already in its own bidding/selection process to be reused by another party — it is **not** part of this project and should not be confused with the Koryukan.

A proposal is only persuasive against the alternatives it beats. For the candidate premises the village is realistically choosing among five paths:

| Option | Upfront cost to village | Ongoing | Jobs | Energy resilience | Forest / ecology | Productive reuse | Unlocks 交付金 | Reversible |
|---|---|---|---|---|---|---|---|---|
| **A. Status quo — spare capacity idle** | ¥0 now | Ongoing upkeep, no new return | 0 | None | Forest untended (liability grows) | No new use | No | Yes |
| **B. Solar-only** | Low–med capex | FIT income, thin | ~0 | Intermittent only | None | Partial | Partly (no resilient site) | Yes |
| **C. Forestry-only** | Low | J-Credit + timber, slow | Few | None | Restored ✓ | No | No | Yes |
| **D. Sell / lease to another party** | One-time cash or rent | Control lost | Uncertain | None | Lost | Buyer's choice¹ | No | Largely no |
| **E. Integrated project** (proposed) | Mostly grant-funded² | Net surplus by ~Y5 | 8–15 | 24/7 (biomass CHP island-mode) | Restored ✓ | Yes ✓ | **Yes ✓** | Staged / descopable |

¹ Where a private buyer is involved, the village should weigh buyer credibility — the dome-school bidding file shows prospective-buyer quality varies; selling or leasing does not guarantee a good village outcome.
² Village cash exposure is minimized because the 交付金 subsidizes 2/3–3/4 of eligible energy capex and other layers carry the rest.

### Why the integrated project wins

- **It is the only option that satisfies the village's *own* published RE plan.** That plan's "one resilient renewable + storage + EV site" indicator currently reads zero; only Option E provides the "1". Options A–D leave the village's adopted 2050 strategy without an operator.
- **It is the only option with an anchor offtaker.** Rural energy projects in Japan typically fail their financials for lack of steady demand. The data center is the 24/7 baseload that makes the energy economics — and therefore the EV charging and blackout resilience — actually close. Solar-only and forestry-only have no anchor and stall.
- **It puts underused space to productive use.** Option A keeps paying upkeep on empty classrooms; Option E turns spare capacity into a revenue-generating facility (and, at the Koryukan, complements its cultural role).
- **It is the only option that does several jobs at once** — heals the forest, generates energy, creates higher-skill local jobs, and produces a replicable model — because the thinnings that fund the energy are the same thinnings that restore the forest.

**Honest counter-point:** Option E is also the **highest in cost, complexity, and execution risk.** The mitigant is structural, not rhetorical — the **funding-gate / descope mechanism** (§4) means the village never commits to the full build up front; each phase proceeds only if the prior gate's funding and feasibility clear. If the project stalls, it stops at a gate having delivered partial value, not at an idle building.

<div class="page-break"></div>

## 3. The ask, the offer, the proof — per audience

Each decision-maker needs the same underlying story ordered for *their* question: **Why you? → What I'm asked for → What I get → How I know you'll deliver.**

| Audience | What we ask | What they get | How they can be confident |
|---|---|---|---|
| **Village government** | Lease premises (former Sugano school / factory — one of several candidate sites); endorse as 官民連携 partner; co-apply for 交付金 | Depopulation reversal, 8–15 jobs, RE-plan delivered, underused space activated | Staged gates (no lock-in); open data; feasibility studies before any build |
| **MoE / grant bodies** | Award 交付金 / planning grants | Adopted RE plan actually implemented; carbon; a replicable 過疎 model | Plan already adopted (step 1 done); milestone-based disbursement |
| **Equity investors (Tier 2)** | Minority capital into the GK opco | Contracted share of operating surplus (net ¥10–32M/yr by Y5); green-compute exposure | Two-tier structure; anchor offtaker; payback model; descope safety |
| **Corporate partners** | Hosting offtake / CSR / equity | Cheap green compute, ESG story, or contracted return | Working pilot before scale; named advisory bench |
| **Foundations** | Mission-restricted grant | Measurable SDG/impact outcomes, strong narrative | Open methodology; transparent reporting |
| **Forestry co-op / landowners** | Sugi harvesting access; restoration participation | Fair harvest compensation; J-Credit income; reduced wildlife damage | Phase-1 contracts; village backing |

**Proof of delivery capability** (the "how do I know" answer, assembled): founder's Safecast track record; named advisory bench (Ray Ozzie); the village's *already-adopted* RE plan; the open-data / open-methodology commitment; and the gate structure that makes every commitment conditional and reversible.

## 4. Whole-project return, sensitivity & go/no-go

### 4.1 Scenario P&L by Year 5 (illustrative)

| | Low | Base | High |
|---|---|---|---|
| Annual revenue | ¥28M | ¥45M | ¥67M |
| Operating cost (~60%) | ¥18M | ¥27M | ¥35M |
| **Net surplus** | **¥10M** | **¥18M** | **¥32M** |
| Payback (¥200–290M capital) | ~18 yr | ~14 yr | ~10 yr |

### 4.2 The three swing variables (what would break the ROI)

The return is most sensitive to three figures, all resolved in Phase 1–2 feasibility:

1. **Data-center occupancy / hosting price** — the anchor. If hosting demand is weak, the whole stack thins. *Mitigant: secure a corporate offtake LOI before Gate 3 build.*
2. **Biomass CHP feedstock cost & sizing** — if thinning logistics cost more than modelled, energy margin erodes. *Mitigant: independent feasibility early; forestry programme supplies fuel at internal cost.*
3. **FIT/FIP tariff outcome** — sets *surplus*-energy value only. *Mitigant: revenue is not FIT-dependent — it is one of six streams. But note the plant is an **exporter** (~1.15 MW, sized to the forest); the co-located data center is only a small behind-the-meter baseload (~2% of output). Most of the CHP's *own* output goes to the village + grid export, so at >1,000 kW that energy revenue is likely **FIP**, not the 40 円 FIT (confirm). Grid interconnection capacity (Henry's 事前相談) is therefore a real dependency. This is the plant's electrons only, though — it doesn't cap total hosting revenue, since the larger showcase DC at the old school runs on grid/green power, not CHP output (compute is worth ~6–20× more per kWh than FIP either way). Figures provisional — see `../energy-forest/mitsue_fit_grid_check.md`.* **Net of real GPU capex, that 6–20× gross figure only converts to net profit above a breakeven fill-rate (~45–70% depending on price tier/depreciation life) — see `mitsue_revenue_model.md` §1a. The swing variable is therefore GPU utilization (the HIGHRESO offtake pipeline), not the FIT/FIP outcome itself.*

### 4.2a GPU server net profit — 3-tier utilization scenario

(Added 2026-07-17.) Point 3 above nets real GPU capex against the gross ~6–20× compute-vs-FIP
figure — the result is fill-rate-gated, not a free multiple (full breakeven math in
`mitsue_revenue_model.md` §1a). Rather than one number, here is the same **Low / Base / High**
framing as §4.1, applied to a single 8×H200 anchor server (~¥53M capex, ~10 kW draw, list
pricing ¥2.53M/mo, 20% opex — see §1a for sources):

| | Low | Base | High |
|---|---|---|---|
| Utilization (fill-rate) | 50% | 65% | 85% |
| Depreciation life | 4 yr | 4 yr | 6 yr |
| Server revenue (at utilization) | ¥15.2M | ¥19.7M | ¥25.8M |
| Opex (~20%) | ¥3.0M | ¥3.9M | ¥5.2M |
| Depreciation | ¥13.25M | ¥13.25M | ¥8.83M |
| **Net profit per server/yr** | **−¥1.1M** | **+¥2.5M** | **+¥11.8M** |
| vs. FIP-equivalent (~¥3.1M/yr, same kWh, ~zero capex) | worse by ¥4.2M | worse by ¥0.5M | **~3.8× FIP** |

**Reading it:** below ~65% fill-rate at list pricing, a GPU server is *no better than* simply
exporting the same power via FIP — sometimes worse, once its own capex is serviced. The project
only clears a clear win at the **High** tier, which needs both strong utilization *and* the
6-year hyperscaler depreciation standard. **The swing variable is fill-rate, and that number is
not yet known** — it depends on what the HIGHRESO offtake relationship can actually underwrite.
Treat anchor-compute sizing as gated by that answer, not by available CHP output.

### 4.3 Go/no-go is already built in

The project's decision spine **is** a go/no-go system — it is just not labelled as one. Each gate is a whole-project kill/continue point:

| Gate | Funding test | If short |
|---|---|---|
| G1 (after Phase 0) | ¥3–8M secured | Hold & re-pitch |
| G2 (after Phase 1) | ¥30–50M + feasibility clears | Hold / descope |
| G3 (after Phase 2) | ¥120–290M + offtake LOI | Stage the build |
| G4 (after Phase 3) | Revenue online? | Partial → stay in pilot |

**Kill criteria** beyond funding: no JP co-founder verbal commitment by end of Phase 0 → G1 held; building structurally unfit (Phase 1 survey) → redesign or stop; feasibility shows negative base-case surplus → descope to forestry+solar only.

## 5. Residual risk & key dependencies

The [implementation plan risk register](mitsue_implementation_plan.md) lists 9 risks with mitigations. What it omits — and investors ask for — is the **residual** (what remains after mitigation) and a consolidated **dependency map**.

### 5.1 Residual risk (after mitigation)

| Risk | After mitigation, what remains |
|---|---|
| Founder dependency (Rob) | Reduced by funded Rep.-Director role + Article 8a succession, but a single-person loss in Phase 0–1 still sets the project back months. **Unmitigated tail.** |
| JP co-founder not secured | Gate-1 hold protects spend, but failure to find one *ends* the project. **Hard dependency.** |
| Hosting demand weak | Six revenue streams cushion it, but the anchor thesis weakens; project survives smaller, ROI lengthens. |
| Feedstock economics | Internal-cost fuel helps, but persistent high logistics cost permanently compresses energy margin. |

### 5.2 Key dependencies (in order)

1. **JP co-founder** — gates everything (legal entity, local trust, bus-factor).
2. **Village endorsement** — unlocks 交付金 and the building.
3. **交付金 award** — closes most of the funding gap.
4. **Corporate offtake LOI** — validates the anchor before the expensive build.
5. **Fiber/grid connection** — physical feasibility.

### 5.3 Key personnel & bus-factor

Currently the team's load-bearing point is the founder. Mitigations in place: funded Representative-Director role (removes unpaid-time dependency), Article 8a continuity/succession (interim Rep. Director appointed within 30 days of a key founder's loss; credentials and documented processes maintained). **Remaining exposure:** the JP co-founder seat is unfilled, and no second operational person yet exists — closing both is the top Phase-0 priority. *(A short positive team-profile — who the principals are and why they are credible to investors — should be added once the JP co-founder is named.)*

## 6. Decision table — authority + investor evaluation

Two linked views: **who decides what (authority)**, and **what each decision-maker needs to see (evaluation)**.

| Decision | Authority | Gate / when | Evidence they need | What they get if yes |
|---|---|---|---|---|
| Lease/endorse premises (former Sugano school / factory — site TBD Phase 1) | Village council / mayor | Phase 0–1 | Alternatives table; jobs forecast; site survey | Revitalization; RE-plan delivery; idle asset revived |
| Award 交付金 | MoE (via village) | Phase 1–2 | RE-plan fit; carbon; 過疎 eligibility | Adopted plan implemented |
| Commit as JP co-founder | The individual | Phase 0 (G1 trigger) | Charter; role; compensation (funded) | Founding equity + mission role |
| Invest equity in GK | Investor | Phase 2 (G3) | Two-tier structure; P&L; sensitivity; offtake LOI | Contracted minority return |
| Commit hosting offtake | Corporate partner | Phase 2–3 | Pilot performance; price/kWh; green cert | Cheap green compute / ESG |
| Supply feedstock | Forestry co-op / landowners | Phase 1 | Harvest terms; J-Credit share | Forest income; reduced crop damage |
| Proceed past each gate | Board (Tier 1) | G1–G4 | Funding secured + feasibility/kill-criteria | Authorisation to spend next phase |

---

## Sources & status

Financial ranges consolidate the project's own illustrative estimates from [`mitsue_revenue_model.md`](mitsue_revenue_model.md), [`mitsue_implementation_plan.md`](mitsue_implementation_plan.md) §ROI, and [`mitsue_evm_plan.md`](mitsue_evm_plan.md) — not externally audited. 交付金 terms: MoE 地域脱炭素移行・再エネ推進交付金, 実施要領 (補助率 2/3・3/4) https://www.env.go.jp/content/900470616.pdf. Entity structure (一般社団法人 + 合同会社 GK) per [`mitsue_implementation_plan.md`](mitsue_implementation_plan.md) §1A and the NGO-setup checklists. **Items still to confirm:** final site selection from the candidate premises (former Sugano school spare classrooms and/or a disused factory — Phase 1; the dome school is a separate building, out of scope); equity entry valuation (Phase 2); positive team profile (post JP co-founder).

---

*Rob Oudendijk — YR-Design / Safecast · Mitsue, Nara Prefecture, Japan · June 2026*
