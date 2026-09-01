<!-- Version: v0.3 | Last modified: 2026-08-14 -->

# Biomass → Hydrogen vs Electricity-sale vs DC-compute — Pathway Comparison

Desk-research comparison of three ways to monetize sugi thinnings via the CHP plant:
(1) gasify to hydrogen and sell it, (2) generate electricity and sell it via FIT/FIP,
(3) generate electricity and run the AI data center. Triggered by the question of
whether hydrogen avoids the FIT/FIP grid-connection constraints described in
[mitsue_fit_grid_check.md](mitsue_fit_grid_check.md).

---

## 1. Biomass-to-hydrogen reality check

- **Yield:** gasification produces roughly **0.08–0.13 kg H₂ per kg dry biomass**,
  at an overall biomass-to-H₂ energy efficiency of **~35–50%**. Figures vary widely
  across studies — this is not a standardized, mature process.
- **Cost at scale:** levelized cost of hydrogen (LCOH) ≈ **$3–4/kg at 200 MW scale**.
  Literature explicitly flags **small-scale gasification (~100 kWth, our range) as
  "techno-economically challenging"** — no commercial off-the-shelf small-scale
  vendor was found, unlike biomass CHP where domestic vendors already exist
  (中外炉/神鋼/静岡製機/ネオナイト — must be Japanese-manufactured per project policy).
- **Market price context (Japan):** current wholesale/CIF hydrogen ≈ **¥675–1,050/kg**.
  Government targets: **¥334/kg by 2030**, **¥222/kg by 2050**. Selling into that market
  as a rural micro-producer additionally requires gas purification (tar/CO removal),
  high-pressure storage under 高圧ガス保安法, and tube-trailer transport to a buyer —
  御杖村 is far from any FCEV station or industrial hydrogen user (Nara/Osaka).

## 2. Does hydrogen actually avoid the FIT/FIP/grid problem?

No — not relative to the DC pathway. Per
[mitsue_fit_grid_check.md](mitsue_fit_grid_check.md), the DC pathway **already**
sidesteps FIT/FIP dependency: the data center simply consumes on-site power, so it
needs no high-capacity grid *export* interconnection. Grid/FIP is only the "overflow"
outlet for surplus in that model. So hydrogen's main claimed advantage — no grid
dependency — is a wash against DC, while hydrogen adds conversion losses, unproven
small-scale technology, purification/compression capex, and no local offtake market.

## 3. Comparison

| Pathway | Maturity at our scale | Value per kWh of biomass energy input | Key blocker |
|---|---|---|---|
| Electricity → FIT/FIP sale | Proven (CHP vendors exist) | Baseline (1×) | ≥1,000 kW forces FIP (market-based, volatile) — see [[mitsue_fit_grid_check.md]] |
| Electricity → DC / AI compute | Proven (needs GPU capex + demand) | **6–20× FIT/FIP** | Needs capex + compute demand, not grid |
| Biomass → H₂ → sell externally | **Unproven at small scale** | Likely **below** FIT/FIP once purification/compression/transport are counted | No local buyer; capex-heavy; not commercially available at village scale |

## 4. Recommendation

**Don't pursue hydrogen-for-sale.** A mix of pathways is still right, but not a
three-way split with external H₂ sales:

- **Primary:** CHP electricity → DC (existing thesis, strongest value capture — see
  [[project_forest_workforce_energy_plan]], [[reference_fit_grid_biomass]]).
- **Secondary:** grid/FIP export for true surplus, as already planned.
- **Where hydrogen could still fit — on-site use only, not external sale:** a small
  electrolyzer/fuel-cell loop using surplus CHP electricity (not gasification-derived
  H₂) to fuel forestry equipment (chippers, trucks) or as DC backup power, displacing
  diesel. This avoids the transport/offtake problem because it's consumed locally, and
  it only mops up electricity the DC and FIP export don't already claim.

## 5. Wood Co-op site → other off-takers: private wire vs 自己託送

A related question came up (ChatGPT-drafted): if the CHP sits at the Wood Co-op
processing center (牛峠工場, 神末797 — already the established site, see §4 and
[mitsue_fit_grid_check.md](mitsue_fit_grid_check.md)), what would it cost to
physically wire electricity to other off-takers, e.g. the Village Office or the
Kozure Youth Travel Village (1–2 km away)?

**ChatGPT's private-wire (自営線) cost estimate was checked and is unreliable on the
low end:**

| Build type | ChatGPT estimate | Sourced Japanese figure | Note |
|---|---|---|---|
| Overhead private line | ¥5M–15M/km | **≈¥100M/km** ([Nikkei BP](https://project.nikkeibp.co.jp/ms/atcl/19/feature/00006/00020/?ST=msb&P=2)) | ChatGPT's number is far too low — real cost is closer to its own *underground* estimate |
| Underground / 無電柱化 | ¥100M–300M/km | ¥350M–530M/km full duct-bank; simpler direct-burial cheaper ([response.jp](https://response.jp/article/2018/02/21/306336.html)) | Plausible only for basic rural direct burial, not standard conduit |

For 1–2 km, a realistic private-wire budget is **¥100M–400M**, not the ¥15M–320M
range ChatGPT gave. Get an actual quote from 関西電力送配電 before budgeting off
either figure.

**A cheaper regulatory path exists and should be checked first: 自己託送
(self-wheeling).** This is an established METI-regulated scheme
([資源エネルギー庁 2023 資料](https://www.meti.go.jp/shingikai/enecho/denryoku_gas/denryoku_gas/pdf/068_03_00.pdf))
that lets a generator supply its own remote facilities **through the existing
utility grid**, paying 託送 (wheeling) fees instead of building new poles/cable.
No private-wire capex at all.

Conditions to verify:
- Generator and off-taker(s) must be in the **same 電力エリア** (same utility
  service area — 関電 here, so this is satisfied).
- Off-takers need a **"close relationship" (密接な関係)** with the generator —
  typically same corporate group or affiliated entity. Village Office and Kozure
  are separate legal entities from Mitsue Village Forest Association / the project NGO — **this is the
  open question to check with 関電 / 経産省 early**, since it determines whether
  自己託送 is even available for those two off-takers.
- Supply and demand must be matched in **30-minute blocks**, with financial
  penalties for deviation — an operational cost, not a capital one.

**Recommendation:** investigate 自己託送 eligibility alongside the existing grid
事前相談 (see [mitsue_fit_grid_check.md](mitsue_fit_grid_check.md)) before pricing
out physical private wire. If the "close relationship" test can be met (e.g. by
structuring the off-take agreements under the project NGO), this likely beats
building ¥100M+/km of cable outright.

## Sources

- [IEA Bioenergy — Biomass gasification for hydrogen production](https://www.ieabioenergy.com/wp-content/uploads/2025/03/IEA-Bioenergy_T33_Bio-H2_Final_v2.pdf)
- [Techno-economic Analysis of Hydrogen Production Using Biomass Gasification — Small Scale Power Plant Study](https://www.sciencedirect.com/science/article/pii/S187661021631311X)
- [Hydrogen production from woody biomass gasification: techno-economic analysis](https://scijournals.onlinelibrary.wiley.com/doi/10.1002/bbb.2647)
- [Thermochemical Production of Hydrogen from Biomass: Pyrolysis and Gasification (MDPI)](https://www.mdpi.com/1996-1073/17/2/537)
- [Hydrogen Insight — Japan fuel subsidy / pricing context](https://www.hydrogeninsight.com/transport/japan-to-offer-nearly-5-kg-towards-hydrogen-refuelling-costs-for-fuel-cell-powered-commercial-vehicles/2-1-1821366)
- [CSIRO HyResource — Japan hydrogen cost targets](https://research.csiro.au/hyresource/policy/international/japan/)
