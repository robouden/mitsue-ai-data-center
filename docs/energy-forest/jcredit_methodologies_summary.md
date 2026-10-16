# J-Credit Methodologies — Fit for Mitsue (EN-R-001, EN-S-007, FO-001)

<p align="right">Version: v0.1 | Last modified: 2026-10-16</p>

Sources (saved in `source-scans/`): EN-R-001 v2.7, EN-S-007 v3.3, FO-001 v3.2 (English). Inquiry on points marked ❓ sent to the secretariat 2026-10-16 — see `docs/outreach/jcredit_secretariat_gasification_chp_inquiry_jp.md`.

## 1. Gasification vs. other CHP
No separate credit exists. EN-R-001 is defined by **fuel** (solid woody biomass: pellets, chips, firewood), not conversion technology. "ガス化" appears nowhere in EN-R-001 or EN-S-007. Gasification and steam CHP are treated identically. ❓ Explicit confirmation requested.

## 2. CHP credits (EN-R-001 + EN-S-007)
- Must displace fossil fuel or grid power.
- Wood must be **unused** (would not otherwise be used for material/energy) and legally harvested; imported wood needs legality documents. Condition 6: environmental/social compliance (dioxin, air pollution laws, etc.).
- **Only self-consumed heat/power is credited.** Power eligible for non-fossil certificates (非化石証書), and FIT/FIP power, counts as "supplied to others" → excluded, unless a contract assigns the environmental value to the project owner and double counting is prevented (※3). ❓
- New CHP must also meet EN-S-007. Its condition 1① names city gas/LNG (or LPG) fuel — unclear whether waived for biomass. ❓
- Baseline for a new heat source: standard boiler, LPG if no gas main; efficiency = average of ≥3 catalogue models.
- Implication: the AI data center must consume CHP output on site (captive load) for credits. Separate DC operator entity → needs contract (※2/※3). ❓

## 3. Forest credits (FO-001 v3.2, Forest Management Activity)
Credits CO₂ removals from forest growth under an approved 森林経営計画 (planting, nurturing, thinning, protection); final cutting counts as emissions.

Eligibility (all):
1. Project plan covers the **entire area** of the mayor-approved forest management plan (or own/managed forest in full; or a selected part if ≥500 ha and not cherry-picked).
2. Cumulative expected removals over the certification period are positive (incl. final-cut stands).
3. At least one thinning area planned in the period (else afforestation/nurturing).
4. No land conversion planned.
5. Plan maintained to 10 years after certification ends; replenishment duty if not.

Calculation: above/below-ground biomass growth + reforestation after final cut (to standard cutting age) + **carbon fixed in long-lived harvested wood products** (lumber, plywood, boards) − baseline removals (growth without management).

## 4. Interaction CHP ↔ forest credits
- FO-001 carbon-fixation counts permanent wood products (lumber/boards); wood burned as CHP fuel earns no fixation credit. No double-counting rule found between FO-001 and EN-R-001 (not checked in the implementation rules — verify).
- Thinning that yields CHP fuel (EN-R-001 "unused" wood) can sit in a FO-001 plan; fuel chips come from thinning that the forest plan already requires.
- Owners with an existing 森林経営計画 are the natural FO-001 participants. Number/area of such owners in 御杖村 not yet checked.

## Open items
- Secretariat reply (sent 2026-10-16).
- Check J-Credit implementation rules for double-counting between forest and energy credits.
- Check how much of 御杖村 forest is under 森林経営計画 (≥500 ha threshold only matters for partial registration).
