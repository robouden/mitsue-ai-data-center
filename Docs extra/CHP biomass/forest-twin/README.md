# Mitsue Forest Twin (simple version)

A 50-year "what if" simulator for Mitsue's sugi forest. Stdlib Python only.

It runs three loops per year:

1. **Forest** – grow stands, convert X% of area/year from sugi to broadleaf, measure wood harvested.
2. **Carbon** – standing forest carbon, carbon locked in timber/biochar, CO₂ avoided vs. fossil fuel.
3. **Money** – revenue (logs, electricity, heat, biochar, carbon credits) vs. costs (logging, planting, CHP).

## Run

```bash
python3 forest_model.py
```

Prints a yearly table + summary and writes `results.csv`.

Compare scenarios side by side:

```bash
python3 forest_model.py --compare
```

Edit the `SCENARIOS` dict in `forest_model.py` to add/change scenarios
(each is just a set of `CONFIG` overrides).

## Files

- `forest_model.py` – the whole model. All assumptions are in `CONFIG` at the top, with source notes.
- `data/species.csv` – per-species growth + wood traits. Add a species = add a row.
- `data/stands.csv` – your forest stands (id, species, area, age).

## Validated result (rotation mode + Mishima calibration)

The model runs three harvest regimes (`regime` in CONFIG):
- **convert** — clearfell X%/yr, replant broadleaf. One-way: fuel is a finite
  stock, depletes, CHP eventually idles. (50 ha → −2 M¥)
- **rotation** — sustained yield: harvest area/`rotation_age` per yr, replant
  sugi so stands re-enter the cycle. Standing carbon stays flat = perpetual fuel.
- **mixed** — `convert_fraction` of replanting goes to broadleaf (ecology), the
  rest to sustained sugi (energy). Captures the ecology↔energy trade-off.

With `elec_efficiency` calibrated to Mishima, sustained rotation reproduces the
real Mishima envelope as a function of **managed forest area**:

| Managed ha | Auto CHP | CHP fuel | 50-yr profit |
|---|---|---|---|
| 50 | 7 kWe | 119 t/yr | +1 M¥ |
| 150 | 22 kWe | 357 t/yr | +84 M¥ |
| **300–350** | **43–51 kWe** | **714–833 t/yr** | **+208–249 M¥** |
| 500 | 72 kWe | 1,190 t/yr | +373 M¥ |

**~300–350 ha matches Mishima's ≤50 kWe / 700–800 t/yr almost exactly** —
independent validation. Mitsue has ~7,051 ha forest, so a Mishima-scale village
CHP needs only ~4–5% of it under sustained management.

## Earlier (convert-mode) notes

The earlier "needs ≥95–145 ha to break even" result was an artefact of assuming a
fixed ¥30–80M gasifier fed by a trickle of wood. The model now **sizes the CHP to
the fuel flow** (`chp_size_auto`): nameplate kWe = peak annual electricity ÷
(capacity factor × 8760 h), and capex/O&M follow from ¥/kWe install + O&M rates.

> **Calibration note:** `elec_efficiency` is now 0.13 (net), set so the model
> reproduces the real Mishima Town (Fukushima) anchor: ~750 green t/yr → ~50 kWe
> at 70% capacity factor. The Sugano/Tokuo figures are *generated estimates*, not
> real data, and are NOT used for calibration. With this honest efficiency the
> 50 ha clearcut-conversion baseline is ~break-even (−2 M¥), not +38 M¥. The
> table below predates this calibration and overstates profit ~2×.

With a *right-sized* unit, even the 50 ha sample is profitable:

| Scenario | Auto kWe | Capex | 50-yr profit |
|---|---|---|---|
| A 2%/yr | 11 kWe | ¥7.7M | +38 M¥ |
| B 4%/yr | 22 kWe | ¥15M | +17 M¥ |
| C timber-first | 6 kWe | ¥3.9M | +65 M¥ |
| D leave forest | 0 | 0 | 0 |

Lessons: (1) match the machine to the wood — a small forest wants a small
gasifier, not a ¥30M one; (2) harvesting *faster* hurts, because it depletes the
sugi and leaves the (larger) CHP idle for decades; (3) selling more high-value
sawlogs and building a smaller CHP (C) beats burning everything.

**Sizing rule of thumb:** a ¥30M gasifier ≈ ~43 kWe nameplate, which needs
~300 MWh/yr of fuel — roughly 2%/yr from ~250 ha, or 4%/yr from ~125 ha.

Caveat: this models a *one-way* conversion (broadleaf is never re-harvested), so
the wood is a finite stock, not a sustainable flow — harvesting faster just
front-loads it. Sustained operation needs either a large enough forest base or a
rotation that keeps producing fuel.

Modes: `--compare` (named scenarios), `--sweep` (harvest × CHP capex grid).

## Tuning

Open `forest_model.py`, edit `CONFIG`. Useful knobs:
`harvest_pct_per_year`, the `alloc_*` wood split, `elec_efficiency`,
`chp_capex_yen`, prices. Re-run to compare scenarios.

## Not included yet (Phase 2+)

GIS maps, web dashboard, biodiversity/hydrology, scenario UI. Add only once the
core numbers look right.
