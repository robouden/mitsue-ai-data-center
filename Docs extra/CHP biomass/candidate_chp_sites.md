<!-- Version: v1.1 | Last modified: 2026-06-24 -->

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
