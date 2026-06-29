# Mitsue Forest Twin (simple version)

A 50-year "what if" simulator for Mitsue's sugi forest. Stdlib Python only.

It runs three loops per year:

1. **Forest** – grow stands, harvest under the chosen `regime` (convert / rotation / mixed), measure wood out.
2. **Carbon** – standing forest carbon, carbon locked in timber/biochar, CO₂ avoided vs. fossil fuel.
3. **Money** – revenue (logs, electricity, heat, biochar, carbon credits) vs. costs (felling, transport, chipping, drying, roads, planting, auto-sized CHP).

## Run

```bash
python3 forest_model.py
```

Prints a yearly table + summary and writes `results.csv`.

Compare scenarios or grid-search the levers:

```bash
python3 forest_model.py --compare   # named regimes (rotation / convert / mixed / leave)
python3 forest_model.py --sweep     # harvest rate × CHP capacity factor (CHP auto-sized)
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

## How the CHP is sized & calibrated

An earlier version guessed a fixed ¥30–80M gasifier, which made small forests
look unprofitable. The model now **sizes the CHP to the fuel flow**
(`chp_size_auto`): nameplate kWe = peak annual electricity ÷ (capacity factor ×
8760 h), and capex/O&M follow from ¥/kWe install + O&M rates.

> **Calibration note:** `elec_efficiency` is 0.13 (net), set so the model
> reproduces the real Mishima Town (Fukushima) anchor: ~750 green t/yr → ~50 kWe
> at 70% capacity factor. The Sugano/Tokuo figures are *generated estimates*, not
> real data, and are NOT used for calibration.

Lessons: (1) match the machine to the wood — a small forest wants a small
gasifier, not a ¥30M one; (2) one-way *convert* depletes the sugi and leaves the
CHP idle for decades — use *rotation* for sustained fuel; (3) selling more
high-value sawlogs and building a smaller CHP beats burning everything.

**Sizing rule of thumb:** a ¥30M gasifier ≈ ~43 kWe nameplate, needing
~300 MWh/yr of fuel — roughly the sustained yield of ~250 ha in rotation.

## Tuning

Open `forest_model.py`, edit `CONFIG`. Useful knobs:
`regime`, `rotation_age`, `convert_fraction`, the `alloc_*` wood split,
`elec_efficiency`, `chp_capacity_factor`, `chp_install_yen_per_kwe`, prices.
Re-run with `--compare` / `--sweep` to compare scenarios.

## Not included yet (Phase 2+)

GIS maps, web dashboard, biodiversity/hydrology, scenario UI. Add only once the
core numbers look right.
