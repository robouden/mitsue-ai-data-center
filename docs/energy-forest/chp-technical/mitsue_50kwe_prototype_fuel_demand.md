<!-- Version: v1.0 | Last modified: 2026-10-02 -->

# 50 kWe Prototype CHP — Wood Fuel Demand for 24 h Operation

Prepared for the local forestry partner (meeting 2026-10-02). Estimate of the wood needed to run a first **50 kWe** biomass gasification CHP prototype **24 hours a day**. Three independent methods are compared, because no 50 kWe unit has been selected yet.

## 1. Fuel demand (dry-matter basis)

| Method | Basis (source) | kg/h | **t/day** | t/yr at 8,000 h | Green chips/day (50% moisture) | Solid m³/day (314 kg/m³) |
|---|---|---|---|---|---|---|
| **A.** Scaled from Tokuo's 10 kWe design | 10 kWe needs 45.5 kWth input = 10.9 kg/h (meeting_tokuo_aomi.md) | 54.5 | **1.31** | 436 | 2.6 t | 4.2 |
| **B.** Measured at Spa Hotel Abukuma | ~1 kWh electric per kg pellet (Entrade units, running since 2018) | 50 | **1.20** | 400 | 2.4 t | 3.8 |
| **C.** Forest Twin model | 18.5 GJ/t, net electrical efficiency 0.13 (workforce plan) | 74.8 | **1.80** | 599 | 3.6 t | 5.7 |
| *Reference: Mishima scenario* | ~750 t/yr for ≤50 kWe (NIES simulation, not a built plant) | 85 | 2.05 | 750 | 4.1 t | 6.5 |

**Planning figure: 1.3–1.8 t dry wood per day = 2.5–3.5 t fresh green chips per day = about 450–600 t/yr.** Method B is a measured plant (most reliable); Method C is the conservative upper bound.

## 2. How each figure was calculated

| Method | Calculation |
|---|---|
| A | 50 kWe ÷ 10 kWe × 10.9 kg/h = 54.5 kg/h; × 24 h = 1,308 kg/day; × 8,000 h = 436 t/yr |
| B | 50 kWe ÷ 1 kWh/kg = 50 kg/h; × 24 h = 1,200 kg/day; × 8,000 h = 400 t/yr |
| C | 50 kWe ÷ 0.13 = 384.6 kWth input; × 3.6 = 1,385 MJ/h; ÷ 18.5 MJ/kg = 74.8 kg/h; × 24 h = 1.80 t/day |
| Green chips | dry mass ÷ (1 − 0.50) = 2 × dry mass |
| Solid volume | dry mass ÷ 314 kg/m³ (sugi, Forest Twin density) |

## 3. Drying heat (50% → 15% moisture)

- Water to evaporate ≈ 0.82 t per tonne of dry wood.
- At 2.45 GJ per tonne of water (EIS 2024 paper), this is ≈ **2.0 GJ per tonne of dry wood**.
- For Method A (1.31 t/day): ≈ 2.6 GJ/day ≈ **30 kWth continuous**.
- The CHP should deliver ≈ 100 kWth (about 2× the electric output, per the Abukuma ratio), so drying would use **~30% of the heat**, before real dryer losses.
- Applies only if the chosen unit needs dry chips (Volter ≤15%, Entrenco ≤12%). Wet-tolerant units (ESPE ≤45%, Esperia ≤40%) fold drying into the package.

## 4. Caveats

- Tokuo's sheet (21.8 t/yr) assumes only 2,000 h/yr of operation. **Do not quote it for 24 h operation.**
- Figures are gasifier input only. Chipping losses, actual wood species and actual moisture are not included.
- Method B is for pellets (dry); equivalent chip demand depends on chip moisture.
- Henry's Mie-plant experience may give better numbers.
- No unit or maker has been selected, so efficiency is an assumption in A and C.
