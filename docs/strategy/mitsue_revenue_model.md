<div style="font-family:-apple-system,Helvetica,Arial,sans-serif;">
<p style="font-size:7.5pt; font-weight:600; letter-spacing:0.25em; color:#3a7a5a; margin:0 0 4mm;">PROJECT DOCUMENT</p>
<h1 style="font-size:28pt; font-weight:700; margin:0 0 2mm; border-bottom:1px solid #eee; padding-bottom:2mm;">BIOMASS ENERGY & AI</h1>
<p style="font-style:italic; color:#666; margin:1mm 0 0;">Reforesting in Mitsue</p>
<p style="font-style:italic; color:#666; margin:2mm 0 8mm;">Revenue & Payback Summary</p>
<img src="assets/logo_go.png" alt="御" width="50%" style="display:block;margin:0 auto;">
<div style="height:105mm;"></div>
<table style="width:100%; border-collapse:collapse; font-size:9pt;">
<tr><td style="padding:3mm 4mm; border:1px solid #ccc; font-weight:bold; width:30%;">Version</td><td style="padding:3mm 4mm; border:1px solid #ccc;">v1.4</td></tr>
<tr><td style="padding:3mm 4mm; border:1px solid #ccc; font-weight:bold;">Date</td><td style="padding:3mm 4mm; border:1px solid #ccc;">2026-07-17</td></tr>
<tr><td style="padding:3mm 4mm; border:1px solid #ccc; font-weight:bold;">Author</td><td style="padding:3mm 4mm; border:1px solid #ccc;">Rob Oudendijk</td></tr>
</table>
</div>

<div style="page-break-after:always; break-after:page; height:0; margin:0; padding:0;"></div>

---

# BIOMASS ENERGY & AI — Revenue & Payback Summary
### Reforesting in Mitsue
### One-Page Funder-Facing Overview

*All figures are illustrative early-stage estimates. Phase 1 feasibility studies (due M9, Dec 2026) will replace these with vetted figures anchored to real survey data.*

*Full detail in [`mitsue_implementation_plan.md`](mitsue_implementation_plan.md) — "Return on Investment" section.*

---

## 1. Revenue Streams

Biomass CHP (fuelled by sugi forest thinnings) is the **primary energy source**, providing 24/7 baseload electricity and heat. Solar, battery storage, and EV charging are complementary. The circular local energy economy — where the forest powers the village — underpins all revenue streams.

> **The plant is an exporter first — size the revenue accordingly.** The CHP is sized to the
> *forest* (~1.15 MWe, ~8,000 MWh/yr), not to any local load. The co-located **data center is a
> small, stable 24/7 baseload (~18 kW ≈ ~2% of output)** — valuable because it is behind-the-meter
> (cap-free, worth avoided-retail not export price) and anchors CHP stability, but it absorbs
> almost nothing. **The bulk of generation goes to the village (via the Kansai T&D grid) and to
> grid export.** So grid interconnection and Henry's 事前相談 are **central**, and at ~1.15 MW the
> plant is over the FY2026 <1,000 kW new-FIT cap → most output likely sells via **FIP** (market
> premium), *not* the 40 円 FIT. A separate ≤1,000 kW line *could* take FIT, TBD. See
> `../energy-forest/mitsue_fit_grid_check.md` (figures provisional, pending primary confirmation).
>
> **This ~2% figure is the CHP's own electrons only — it does not cap total DC hosting revenue.**
> (Reconciled 2026-07-17.) The siting decision in `mitsue_fit_grid_check.md` puts compute in
> **both** places: a small anchor cluster behind-the-meter at the CHP (the ~2% above, valued for
> stability + avoided-retail), **and** the larger flagship showcase DC at the old school, powered
> by grid/green retail. So "Data center hosting fees" in the table below is driven by GPU fill-rate
> across both sites, not by the CHP's export share — see the compute-vs-FIP economics immediately
> below.

| Revenue / Savings Category | Year 1 | Year 5 | Year 10 | Notes |
|----------------------------|--------|--------|---------|-------|
| Data center hosting fees | ¥0 | ¥15–30M | ¥40–80M | Edge computing / AI specialist workloads |
| Electricity export (FIP/FIT) | ¥0 | ¥5–15M | ¥10–30M | Plant's main energy-revenue stream (village + grid export); >1,000 kW → likely **FIP**, a ≤1,000 kW slice may take 40 円 FIT. **Magnitude provisional — re-model in Phase 1 once FIP terms + village offtake are set** |
| EV charging fees | ¥0 | ¥1–3M | ¥3–8M | Growing as EV fleet expands |
| Carbon credits (J-Credit) | ¥0 | ¥1–3M | ¥3–10M | From native forest restoration |
| Forestry products (timber, lumber) | ¥0 | ¥3–8M | ¥10–20M | Beyond fuel-residue use |
| Education / consulting ("playbook") | ¥0 | ¥1–3M | ¥3–8M | Replication licensing and training |
| **Total annual revenue (illustrative)** | **¥0** | **¥28–67M** | **¥74–166M** | |

> **Why "compute" ranks above "electricity export": 1 kWh is worth ~6–20× more as AI compute
> than as exported power.** (Added 2026-07-17.)
>
> | Use of 1 kWh | Revenue | Basis |
> |---|---|---|
> | Sell to grid (FIP) | ~¥30–40 | 未利用材 biomass FIP effective (基準価格 ~32–40円 + JEPX premium) |
> | Village displacement | ~¥20–30 | avoided retail import |
> | Feed an A100 GPU (GPUSOROBAN retail) | ~¥360–650 | ¥361/hr ÷ ~0.55–1 kW/node |
> | Feed 8×H200 server (retail → 50%-off enterprise) | ~¥390 → ~¥190 | ¥2.78M→¥1.39M /mo ÷ 720h ÷ ~10 kW |
>
> **Consequence:** the CHP's best "customer" is an **on-site GPU DC, not the grid.** Grid export
> (FIP) is the **overflow valve** for power we can't yet convert to compute — a revenue *floor*.
> Size the DC as large as we can (a) fill with paying GPU demand and (b) fit+cool at 神末. The
> scarce factors flip from power to **GPU capex + fill-rate**: a rented A100 earns ~¥360/kWh, an
> idle one ¥0 while ~¥1.3M capex depreciates → **utilization, not power, is the constraint** (→
> HIGHRESO partnership / offtake pipeline). Sources: GPUSOROBAN pricing
> https://soroban.highreso.jp/ ; FIP/未利用材 per `../energy-forest/mitsue_fit_grid_check.md`.

### 1a. Net-of-capex reality check — compute only beats FIP above a breakeven fill-rate

(Added 2026-07-17.) The ~6–20× figure above is **gross revenue per kWh** — it doesn't net out
GPU capex/depreciation/opex, which FIP export doesn't carry (the CHP is already sunk capex either
way). On a **net-profit** basis the comparison is capex- and utilization-sensitive, so it belongs
in the doc as a breakeven condition, not a single multiple.

**Assumptions (sourced, not invented):**

| Input | Value | Source |
|---|---|---|
| 8×H200 server capex | ~¥53M (range ¥46–60M) | $320–420K typical $370K, ×¥143/$ — [Mercatus H200 server price](https://www.mercatus-ai.com/blog/h200-server-price) |
| Power draw per server | ~10 kW | Existing GPUSOROBAN-based calc, this doc §1 |
| Hosting revenue, list | ¥2.53M/mo (¥30.36M/yr @ 100% util) | [HIGHRESO GPUSOROBAN H200 pricing](https://highreso.jp/en/) |
| Hosting revenue, long-contract discount | up to −39% → ¥1.54M/mo (¥18.52M/yr @ 100% util) | Same source |
| Opex | ~20% of realized revenue | Planning assumption (typical colo/cloud opex ratio) — not vendor-quoted |
| Depreciation life | 4 yr (small-operator planning) vs 6 yr (hyperscaler accounting standard) | [CNBC — AI GPU depreciation debate](https://www.cnbc.com/2025/11/14/ai-gpu-depreciation-coreweave-nvidia-michael-burry.html); AWS/Google/Microsoft moved 3–4yr → 6yr in 2023–24 |
| FIP-equivalent net (same ~87,600 kWh/yr, no meaningful capex) | ~¥3.07M/yr | ¥30–40/kWh mid ¥35, this doc §1 |

**Breakeven utilization — the fill-rate a server needs to beat simply exporting its power via FIP:**

| Price tier | Depreciation life | Utilization needed to beat FIP |
|---|---|---|
| List price | 4 yr | **~67%** |
| List price | 6 yr | **~49%** |
| Long-contract discount (−39%) | 4 yr | **>100% — can never beat FIP at this price/life** |
| Long-contract discount (−39%) | 6 yr | **~80%** |

**The finding:** netting real GPU capex reverses the naive "compute always wins" reading of the
6–20× gross figure above. A GPU server only beats simply exporting its power once it clears
roughly **45–70% fill-rate at list pricing** — and essentially **never** at the deep long-term
discount unless depreciation stretches to the 6-year hyperscaler standard. This does not
contradict §1's per-kWh economics (compute is still the higher-value use of a kWh) — it says the
*server*, as a ¥46–60M capital deployment, needs a real utilization floor to convert that per-kWh
advantage into net profit. Grid-export FIP requires no such floor because the CHP capex is already
committed regardless.

> **Open question — not yet answered:** what fill-rate can the HIGHRESO offtake pipeline actually
> underwrite? That number (not a guess) picks which row of the table above is the honest one to
> plan and pitch against. Until confirmed, treat the anchor-compute buildout size as **fill-rate-
> gated**, not power-gated — matching `../energy-forest/mitsue_fit_grid_check.md`'s "utilization,
> not power, is the constraint," now quantified.

---

## 2. Cost Displacement

The project *replaces or avoids* significant existing costs:

- **Energy imports**: Mitsue residents and businesses currently import ~100% of electricity. Local generation displaces approximately **¥40–60M/yr** of energy spending leaving the village economy.
- **Data-center power (self-consumption)**: the CHP supplies the co-located data center's electricity behind-the-meter, **avoiding retail grid purchase** — the foundation of the "cheap green compute" thesis. It is a *small* load (~18 kW ≈ ~2% of plant output), so the value is per-kWh (avoided retail > export) and CHP-stability, not volume. Because it is *avoided cost*, not grid sales, it is unaffected by the FIT capacity cap.
- **Former Sugano school maintenance burden**: The Koryukan costs the village an estimated **¥3–8M/yr** in basic upkeep with no return. Active reuse as a data center hub converts a stranded asset into a productive facility.
- **Forest management liability**: Untended sugi plantations impose ecological costs (pollen, biodiversity loss) and physical risks (landslide, fire). Active management converts this liability into feedstock and timber revenue.

---

## 3. Payback Framework

| Metric | Value |
|--------|-------|
| Total capital deployed (Phases 1–3) by Year 5 | ¥200–290M |
| Annual revenue by Year 5 | ¥28–67M |
| Operating costs by Year 5 (est. 60% of revenue) | ¥18–35M |
| **Net annual surplus by Year 5** | **¥10–32M** |
| **Approximate capital payback period** | **10–18 years** (depending on grant vs. loan vs. revenue-financing mix) |
| Break-even / net-surplus year (base case) | ~Year 5 |

Once net surplus is achieved, reinvestment priority: (1) forestry scale-up → (2) data-center expansion → (3) replication support for other villages.

---

## 4. Honest Caveat

These are **framework figures, not a forecast**. They assume successful execution of all three project elements (biomass CHP energy, data center, forestry) at target scale. Phase 1 feasibility studies will sharpen these numbers significantly. Real-world performance — particularly biomass CHP sizing, data center occupancy, and FIT/FIP tariff outcomes — will determine actual ROI.

---

## Sources

These are the project's **own illustrative early-stage estimates**, consolidated from the "Return on Investment" section of [`mitsue_implementation_plan.md`](mitsue_implementation_plan.md) — not externally audited figures. The underlying load, PUE, and carbon assumptions and their references (HIGHRESO PUE target, J-Credit methodology, Forestry Agency sequestration data, edge-data-center power benchmarks) are documented in that plan's Phase 1 "Sources & assumptions" block.

The categories above will be validated against METI FIT/FIP tariff schedules, J-Credit pricing, and biomass/timber market data **during** the Phase 1 feasibility studies (M9, December 2026), which will replace these framework figures with vetted estimates.

---

*Rob Oudendijk — YR-Design / Safecast*
*Mitsue, Nara Prefecture, Japan*
*June 2026*
