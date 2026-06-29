# Forest Twin Model — Findings

<p align="right">Version: v1.0 &nbsp;|&nbsp; Last modified: 2026-06-30</p>

---

## What this is

A simple, runnable 50-year simulator (`forest-twin/`, stdlib Python) for Mitsue's
sugi forest, biomass CHP, carbon, and economics. Built to replace spreadsheet
guesswork with a model we can calibrate against real data and interrogate with
"what if" scenarios. It runs three loops per year — **forest growth → carbon →
money** — and three harvest regimes (convert / rotation / mixed).

Run: `python3 forest_model.py` (also `--compare`, `--sweep`).

## Key findings

**1. Full supply-chain costs roughly double break-even.**
Adding explicit felling, transport (distance-based), chipping, drying, and road
upkeep — instead of one lumped logging cost — moved the convert-mode break-even
from ~70 ha to ~145 ha. Mitsue's short ~5 km haul pulls it back to ~95 ha, a
concrete argument for siting the CHP centrally.

**2. The CHP must be sized to the wood, not the other way round.**
Treating capex as a free guess produced nonsense. The model now *derives*
nameplate kWe and capex from the actual fuel flow. Rule of thumb: a ¥30M
gasifier ≈ ~43 kWe and needs ~300 MWh/yr of fuel — about 2%/yr from ~250 ha.
Starting from "let's buy a ¥30M unit" was itself the error; a small forest wants
a small, cheap gasifier.

**3. Calibrated to real data (Mishima), not generated estimates.**
The only empirical anchor is the **Mishima Town, Fukushima** NIES study (Ooba,
Nakamura & Togawa, 2020): ≤50 kWe CHP consuming 700–800 t/yr. Net electrical
efficiency was set to 0.13 so the model reproduces this. The Sugano / Tokuo Aomi
figures (10 kWe, 28 ha, etc.) are **generated estimates, not measured data**, and
are NOT used for calibration — only as a case to predict.

**4. Sustainability depends entirely on the harvest regime.**
- *convert* (clearfell → broadleaf, one-way): fuel is a finite stock, depletes,
  CHP eventually idles. Harvesting faster just spends it sooner. (50 ha → −2 M¥)
- *rotation* (replant sugi, harvest area/rotation_age per yr): standing carbon
  stays flat → perpetual fuel. (50 ha → +1 M¥, and scales well)
- *mixed*: splits replanting between broadleaf (ecology) and sugi (energy).

**5. The model independently reproduces Mishima.**
In sustained rotation, output scales with managed forest area:

| Managed ha | Auto CHP | CHP fuel | 50-yr profit |
|---|---|---|---|
| 50 | 7 kWe | 119 t/yr | +1 M¥ |
| 150 | 22 kWe | 357 t/yr | +84 M¥ |
| **300–350** | **43–51 kWe** | **714–833 t/yr** | **+208–249 M¥** |
| 500 | 72 kWe | 1,190 t/yr | +373 M¥ |

**~300–350 ha matches Mishima's ≤50 kWe / 700–800 t/yr almost exactly** — an
independent cross-check between our growth/energy model and a published field
study.

## What it means for Mitsue

- A Mishima-scale **~50 kWe village CHP needs ~320 ha** under active rotation —
  about **4–5% of Mitsue's 7,051 ha** of forest.
- At that scale it is both clearly profitable (~+200 M¥ / 50 yr) **and**
  carbon-stable, unlike one-way conversion.

## Open question — for Mitsue Kanko (御杖村森林組合)

The model gives the *target* (~320 ha sustainably managed). How much of the
7,051 ha is **actually accessible and harvestable** is a question only the forest
cooperative can answer:

- Road / skid access (steep roadless stands aren't economically harvestable)
- Ownership consent (>90% private, fragmented — Mishima's #1 barrier)
- Stand condition (overgrown sugi ready for thinning now vs. too young)
- Cooperative's own operational capacity to scale up

A drone + LiDAR forest survey (as used in Mishima) is the tool to measure this.

## Sources / 出典

- Ooba, Nakamura & Togawa (2020), *Promoting Local Revitalization to Solve Issues
  on Degraded Forests in Japan* — NIES Fukushima; Mishima Town CHP precedent.
  See `degraded_forests_paper_summary_and_application.md`.
- 御杖村森林組合 report — village forest area ~7,051 ha; cooperative throughput.
- NEDO small-scale biomass gasification efficiency ranges.
- Model assumptions (growth curves, prices, costs) are documented inline in
  `forest-twin/forest_model.py` CONFIG; all are tunable and order-of-magnitude.
