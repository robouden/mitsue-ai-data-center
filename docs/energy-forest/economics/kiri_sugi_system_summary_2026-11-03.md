<style>
  body, #write { font-size: 10px !important; line-height: 1.3 !important; }
  table { font-size: 9.5px !important; width: 100% !important; }
  td, th { padding: 2px 5px !important; vertical-align: top !important; }
  h1 { font-size: 15px !important; } h2 { font-size: 11.5px !important; }
  p, ul, table { margin: 3px 0 !important; }
</style>

<p align="right">Version: v1.0 | Last modified: 2026-11-03</p>

# Sugi clear-cut + thinning residue + kiri + CHP — system summary

Working model: `kiri_sugi_integrated_system_model_2026-11-03.xlsx` (v1.2). **All prices and costs are placeholders, not quotes.**

## Base case: owners get 30% of sawlog net, 75% of cut-and-left thinning wood collected

- Clear-cut **50 ha/yr** of sugi (600 m³/ha = 30,000 m³, one 931XC at its minimum). Sawlogs (A, B) are sold; C+D wood is chipped for the CHP.
- Half of the cleared land is planted to **kiri** at ¥1M/ha (Tokushima growth, 8.6 t dry/ha/yr, 5-year rotation, coppice replant every 4th cut); the other half to broadleaf (¥0.7M/ha).
- **75% of the thinning wood now left in the forest** (about 6,050 m³/yr) is also chipped, at ¥4,000/t fresh (felling already paid by the village).
- CHP: 25% net electrical efficiency, ¥32/kWh FIT, 50% grant (unconfirmed), sized to the fuel.

| Result (¥M/yr) | Years 1–5 | Steady state (year 6+) |
|---|---|---|
| CHP size | 0.58 MWe | **0.75 MWe** |
| Paid to landowners | 34 | 34 |
| **System net** | **+48** | **+45** |

## Cases (steady-state system net, ¥M/yr)

| Case | Net | Case | Net |
|---|---|---|---|
| **Base** | **+45** | Replant kiri every cut | +26 |
| Owners 0% / 50% | +79 / +22 | Thinning-type grade split (22% A) | +4 |
| No residue / 50% / 100% residue | +32 / +41 / +49 | Low sawlog price, high cost | −10 |
| Kiri at ¥2M/ha | +39 | **317 m³/ha, 95 ha/yr** (30,000 m³) | **+1** |
| | | 317 m³/ha, 50 ha/yr (15,900 m³) | +6 |

## What drives the result

1. **Volume per hectare.** The model uses 600 m³/ha; the village thinning plan shows only 277–317 m³/ha standing (50–60 yr stands). At 317 m³/ha the base case falls to about break-even.
2. **Grade split.** Sawlog sales fund everything. The 61% A share is the national all-harvest average; Mitsue's neglected stands may be far lower (thinning-type 22% A gives +4).
3. **Landowner share.** Each 10 points costs about ¥11M/yr. 30% is the planning choice, to give owners an incentive.
4. **Residue price and recovery.** The ¥4,000/t placeholder is untested. At ¥8,000/t the residue gain is only about ¥1.6M/yr. Slope and access (winch-assisted 931/855 may help) are unconfirmed.

## Not included

Carbon credits, GPU/data-center income, the ¥3,000/t village biomass subsidy, the 931XC/forwarder purchase and crew wages, deer-fence cost beyond the ¥1M/ha planting figure.

## What will settle the open inputs

- **Oba (11/6):** forest register / stand volume (B8), stumpage and who receives sale income (B9), clear-cut and replanting rules (B10), A/B log buyers (B11), road access (B5).
- **Komatsu:** slope limits with and without winch, road width, annual output per 931XC + 855 set.
- **Maker RFQ:** real CHP efficiency and capex at 0.6–0.8 MWe (over 1,000 kW would be FIP-only, no splitting).
