<!-- Version: v1.2 | Last modified: 2026-06-30 -->

<div style="font-family:-apple-system,Helvetica,Arial,sans-serif;">
<p style="font-size:7.5pt; font-weight:600; letter-spacing:0.25em; color:#3a7a5a; margin:0 0 4mm;">PROJECT DOCUMENT</p>
<h1 style="font-size:28pt; font-weight:700; margin:0 0 2mm; border-bottom:1px solid #eee; padding-bottom:2mm;">Mitsue-kun Project</h1>
<p style="font-style:italic; color:#666; margin:2mm 0 8mm;">Candidate CHP + Compute Sites — Distributed Node Portfolio</p>
<img src="../../assets/logo_go.png" alt="御" width="50%" style="display:block;margin:0 auto;">
<div style="height:105mm;"></div>
<table style="width:100%; border-collapse:collapse; font-size:9pt;">
<tr><td style="padding:3mm 4mm; border:1px solid #ccc; font-weight:bold; width:30%;">Version</td><td style="padding:3mm 4mm; border:1px solid #ccc;">v1.2</td></tr>
<tr><td style="padding:3mm 4mm; border:1px solid #ccc; font-weight:bold;">Date</td><td style="padding:3mm 4mm; border:1px solid #ccc;">2026-06-30</td></tr>
<tr><td style="padding:3mm 4mm; border:1px solid #ccc; font-weight:bold;">Author</td><td style="padding:3mm 4mm; border:1px solid #ccc;">Rob Oudendijk</td></tr>
</table>
</div>

<div style="page-break-after:always; break-after:page; height:0; margin:0; padding:0;"></div>

# Candidate CHP + Compute Sites — Distributed Node Portfolio

> Early-stage idea capture. The project's biomass-CHP + community-compute model is **replicable across sites**; this note lists candidate locations in Mitsue. All are subject to the Phase 1 energy feasibility study (Gantt WP 57 / JP 164) — nothing here is committed.

## Why distributed nodes

The thesis is forest restoration + **distributed** energy + community-owned compute. Each viable node needs three things in one place: **local fuel** (sugi thinnings), a **local heat sink** (something that needs the CHP's waste heat), and a **local electrical load** (an anchor offtaker so the generator runs economically). Different sites supply these in different mixes.

## Candidate sites

| # | Site | Location | Role | Status |
|---|------|----------|------|--------|
| 1 | **Sugano Organic** (Tokuo Aomi) | Sugano | 10 kW home + workshop — lead Phase-1 living prototype | Proposal drafted |
| 2 | **Former Sugano Elementary (Koryukan / みつえ体験交流館)** | Sugano | Community hub: project's main small data center + community EV charging, powered by nearby CHP | Leading Phase-1 site candidate |
| 3 | **Mitsue Onsen — 姫石の湯 / 道の駅 伊勢本街道御杖** | Kozue (神末) | **Anchor CHP plant + small compute node + disaster-resilience hub** | New idea — to assess |
| 4 | **Former 青海林業 yard** (idle ~13 yrs) | Sugano | Roadside **demonstration / showcase hub** — visible CHP + chip storage on 国道369 | New idea — to assess (ownership unknown) |

---

## Site 3 — Mitsue Onsen — detail

A standalone node at the village centre (Kozue), separate from the Sugano hub — too far to serve the Koryukan's community charging, but a strong candidate in its own right.

### Technology reality — combustion ≠ gasification

The onsen's existing wood heater is almost certainly a **combustion boiler** (burn wood → extract heat → hot water). **It cannot generate electricity.** Power requires a **gasification CHP**: wood → gasifier → wood gas (syngas) → gas cleaning → gas engine → generator → electricity, with the engine's waste heat recovered for hot water. The gasifier is **new, separate kit** — not a modification of the boiler. The existing hot-water distribution can usually be kept.

| Reusable at the onsen | NOT reusable |
|---|---|
| Sugi fuel supply + on-site wood storage/handling | The existing **combustion boiler** (wrong technology for power) |
| Staff familiarity with wood fuel | — |
| The **heat sink** (baths need continuous hot water) | — |

Gasifiers are fussier than boilers: they need uniform chips (~20–50 mm), **moisture <20%** (fresh cedar is 40–60%, so drying is required), and minimal bark/dirt, plus gas cleaning and more operator attention.

### Scale

Indicative for an onsen-anchored plant: **100–250 kWe / 200–500 kWth** — an order of magnitude above Tokuo's 10 kW home unit. So this is the **anchor plant**, not a small prototype. It could supply onsen heat, village-facility electricity, EV fast charging, a small edge/AI compute load, and surplus power.

### Heat cascade (this is the key to making the scale pay)

CHP economics depend on **using** the waste heat. The onsen alone — daytime/opening-hours only, possibly closed some days — is **not a 24/7 heat sink**, while a compute load wants 24/7 electrical baseload. Reconcile by cascading the heat:

1. **Baths** (primary, daytime)
2. **Chip drying** — surplus/off-hours heat dries the next fuel batch → self-supporting fuel cycle (also soaks up night-time heat when baths are closed)
3. **Greenhouses / year-round agriculture**
4. **Community buildings**

**Caveat to keep honest:** 100–250 kWe is the *upside* case and is **contingent on building out these heat uses**. If demand stays at "onsen baths only, daytime," the system sizes down. Heat demand — not fuel supply — is the binding constraint.

### Other points
- **Co-located 50 kW DC fast charger** (Terra Charge / Nichicon, 24h, installed 2024, grid-powered today) — a local CHP could power it with renewable electricity, making it blackout-resilient.
- **Promotion value** — "a hot spring powered by its own forest" is an authentic, marketable eco-friendly story for the onsen and the village.

---

## Site 4 — Former 青海林業 yard — detail

An idle forestry property in central 菅野/Sugano (~34.4883°N, 136.1673°E), on 国道369 / 伊勢本街道, **unused ~13 years**. Defunct as a *business* (no crew/equipment) — but attractive as a **site we could occupy**.

### Why it's appealing (Rob's observation)
- **Existing building + open yard** — shelter for a CHP/gasifier, a **covered dry-chip store** (moisture <20% is mandatory for gasification — see onsen note), workshop, log deck. Reuse > new build.
- **High visibility** — heavy through-traffic on 国道369/伊勢本街道. A working "forest → power" demonstrator here is **free, continuous promotion** ("a village powered by its own forest").
- **Institutional cluster** — next to the **Mitsue Kanko head office** (菅野1581), the **village hall**, 御杖村社会福祉協議会, and the **active private sawmill 丹羽製材 (Niwa Seizai)** — 御杖村大字菅野400-5, on 伊勢本街道/国道369; owner (丹羽/Niwa family) known to Rob, owner + wife already informed about the project. Forestry-industrial context, likely existing truck access and possibly 3-phase grid.

> **Note on the active mill's chipper (Rob checked, 2026-06-30):** it HAS a chipper, but the chips are made for **paper/pulp** → **NG as CHP fuel**. The output is a *sold product* committed to a paper mill (not surplus), and pulp-chip spec ≠ gasifier fuel-chip spec. So their *existing* chipper is **not a drop-in fuel source**.

### Fuel-supply partnership idea (owner + wife already informed — 2026-06-30)

**Niwa-san (丹羽製材)** and his wife **know about the project**, and there's a live idea to **set up a (new, fuel-spec) chipper together so the mill supplies the CHP fuel** — a win-win local fuel SME. This is potentially our **best fuel-supply route**: a partner who already has crew, yard, log-handling, and chipping experience, with an existing trust relationship.

**Why it works:** *cascading use* — their high-value **pulp chips stay their product**; the new fuel chipper processes only the **lower grade** (slabwood, bark, offcuts, reject logs, thinnings) that currently has little value → new revenue from near-waste. Money stays in the village.

**Three things that make or break it:**
1. **Capex / who funds the fuel chipper** — new kit, separate from the pulp chipper. Target a **forestry/biomass subsidy**: grant-funded shared infrastructure the mill owns + operates.
2. **Drying + storage, not just chipping** — gasification needs **<20% moisture** (fresh sugi 40–60%) + uniform 20–50 mm. Scope = chipper **+ covered dry store**; cheapest drying = **CHP waste heat** (heat-cascade link).
3. **Volume match, sustainably** — ~50 kWe ≈ 700–800 t/yr (Mishima anchor). Confirm residue + thinnings can supply that without over-harvest, and **coordinate with 御杖村森林組合** (sole forestry operator) so it complements 牛峠工場, not competes.

**Structure if it checks out:** grant-funded chipper → mill operates → sells fuel chips to CHP node(s) under a simple supply agreement. Mill gains asset + revenue; project gains secure local fuel.

**TODO:** identify the chipper subsidy line; quantify available residue/thinning tonnage; structure the chipper JV + supply agreement with Niwa-san.
- **Central to the people** — matches the project principle of anchoring demos in 菅野, not remote mountain. ~0.7 km from Sugano Organic (Tokuo) and the Koryukan candidate.

### What it does NOT solve (the binding constraints)
Per the three-things test (fuel + heat sink + electrical load in one place), this site is **strong on space/visibility but weak on a heat sink and an anchor load**:
- **No obvious heat sink** — unlike the onsen (baths) or greenhouses. Waste heat would need a created use (chip drying at minimum; ideally a paired greenhouse/workshop). Without it, CHP economics suffer.
- **No anchor electrical offtaker** on site — would rely on the neighbouring facilities (coop, hall) or a co-located compute/EV load taking the power.
- So this is best framed as a **demonstration + chip-processing/storage + small-compute showcase**, possibly feeding the coop/hall, *not* as a self-justifying anchor plant like the onsen.

### Blockers to clear before it's real (in priority order)
1. **Ownership** — who owns it, and will they sell or lease? 13-years-idle rural property often carries **inheritance/空き家 (相続)** complications. This is the gating question; nothing else matters until it's answered. (Owner & whether it's Tokuo's same 青海 family currently unknown.)
2. **Building condition** — 13 years idle: roof/structure, and **old industrial sheds may contain asbestos** → survey before any reuse.
3. **Permits** — zoning + 消防 (fire) sign-off for an on-site gasifier/combustion plant.
4. **Grid** — confirm 3-phase capacity / connection cost.

### Next step
Low-cost, high-value: **ask locally** (coop / village hall both adjacent) who owns the 青海林業 parcel and whether it's available. If yes, fold into the WP 57 feasibility study as the **Sugano demonstration-hub option** alongside the Koryukan.

---

## Disaster-resilience hub (防災拠点) — the strongest funding angle

Equipped with biomass CHP + battery storage + **island-mode (microgrid)**, the onsen could serve as a **Disaster Resilience Center**: emergency electricity, heating, **hot showers**, kitchen/food, communications, medicine refrigeration, and phone/medical-device charging — running through multi-day outages.

**Why it fits Mitsue's hazards:** landslides, typhoon flooding, and heavy-snow road isolation all cause **multi-day, night-time outages** — exactly where biomass CHP beats solar-only (it runs at night and through extended bad weather), provided fuel is stored on site (which snow isolation demands anyway). No tsunami/nuclear risk; main risks are weather and landslide.

**Plausible funding (verify current 要綱 — programs/rates change):**
- **環境省 地域脱炭素移行・再エネ推進交付金** (2/3–3/4) — already a project target; explicitly rewards 再エネ + 防災拠点 at public facilities. Maps to the village RE plan's "one resilient renewable-energy site."
- **緊急防災・減災事業債** (総務省/消防庁) — favorable local-government bond financing for disaster facilities.
- **防災・安全交付金 / 国土強靱化** (MLIT / Cabinet Office) — national-resilience funding.
- **NEDO / 経産省 自立分散型エネルギー** — disaster-time distributed energy supply.

**Verify points:**
1. Is 姫石の湯 an **officially designated shelter (指定避難所)**? Could not confirm from public docs. If yes → eligibility strengthens; if no → pursue designation with the village.
2. Resilience grants almost always require **battery + island-mode** — this gives the "battery TBD in feasibility" question a clear justification.
3. Most funding flows **through the village (官民連携)** — village is applicant, our entity the operating partner → mayor buy-in matters.

---

## Next step

Fold these candidates into the **Phase 1 energy systems feasibility study** (WP 57 / JP 164) for site comparison: heat load + heat-cascade build-out, fuel logistics, electrical offtaker, ownership/operator, shelter-designation status, and the night-time heat-sink question for any onsen + compute pairing.
