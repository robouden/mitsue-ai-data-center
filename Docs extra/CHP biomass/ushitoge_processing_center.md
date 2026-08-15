<!-- Version: v1.1 | Last modified: 2026-08-14 -->

# 御杖村森林組合 牛峠工場 — Reference Sheet
**Ushitoge Thinning-Timber Processing Center**

Reference notes on the cooperative's sawmill/processing facility and its relevance to the biomass-CHP plan. Verified contact details vs. unconfirmed assumptions are kept separate on purpose.

---

## Two sites, one cooperative

The 御杖村森林組合 (Mitsue Village Forestry Cooperative, "Mitsue Village Forest Association") operates from **two separate locations** in the village:

| | **Head office (本所)** | **Processing facility (牛峠工場)** |
|---|---|---|
| District | 菅野 / Sugano (central village) | 神末 / Kōzue (up the valley) |
| Address | 〒633-1301 奈良県宇陀郡御杖村神末797 | 奈良県宇陀郡御杖村神末797 |
| Tel | 0745-95-2010 | 0745-95-2410 |
| Role | Admin, membership, forestry planning | Sawmilling + timber processing |
| Coords | (central village) | ~34.4890°N, 136.2060°E |

The two sites are ~3–4 km apart (straight line); ~5–7 km by valley road. The office handles paperwork; the physical timber work happens at the Ushitoge (牛峠) site, which has the yard space and truck access.

**Status: verified** — head office address & phone confirmed via Mapion phonebook (2026-06-30); factory address & phone confirmed in project records.

### Watch-outs
- **0745-95-2001 / 菅野368** is the **village hall 総務課** (municipal government), *not* the cooperative. Don't conflate.
- **mitsuemori.org is dead / hijacked** — it now resolves to an unrelated page. There is no usable official coop website; use the 御杖村観光協会 (mitsue-kanko.jp) listing instead.

---

## What the factory does (confirmed)

Processes thinning timber (間伐材) from forest management into marketable products: structural lumber, civil-engineering stakes, benches, wood blocks, and timber for public works — from local sugi (cedar) and hinoki (cypress).

Why it matters to the project: it is an **existing** processing site, so a biomass pilot can route thinnings here for chipping/drying instead of building new chip/dry capacity — those costs become per-m³ operating fees rather than capex. (Reflected in the forest-twin model as `transport_distance_km ≈ 6`, chipping/drying as fees.)

---

## CHP relevance — confirmed vs. assumed

**Confirmed:** it is a wood-*processing* facility (lumber + products), not a dedicated biomass fuel plant. Facilities of this type generate residues (sawdust, slabs, offcuts, bark, low-grade logs) that are commonly chipped for fuel.

**NOT confirmed (do not state as fact):**
- Whether the factory currently has an industrial **chipper**.
- Whether it already produces **biomass fuel chips**.
- Annual throughput (m³/yr), lumber-vs-residue split, or volume of unused low-grade material.

**Sizing reality check:** our only empirical anchor (Mishima Town, Fukushima — NIES 2020) shows a village/forest of this type sustainably supports a **≤50 kWe CHP eating ~700–800 t/yr**. Any feasibility figure should cite Mishima, not the larger "100 kW–1 MW" range floated in informal notes. (See `degraded_forests_paper_summary_and_application.md`.)

---

## Questions to ask the cooperative

Approach the **head office** (専務理事 / 森林整備担当 / 木材利用担当), not the factory directly. Open with resource, not requests:

1. How much residual wood do you generate per year after producing lumber?
2. How many m³ of thinning timber do you process annually? What % becomes lumber?
3. What happens to slabs, bark, and sawdust now?
4. Do you already produce biomass chips? If not, would you, given a local customer?
5. How much low-grade timber currently has little or no market value?

---

## Cascading-use logic (target model)

```
Forest → Thinning → 牛峠工場 ─┬─ Lumber (highest value)
                              ├─ Construction timber
                              ├─ Benches / stakes
                              └─ Residual wood → chipper → dry/store
                                                              → Biomass CHP / gasifier
                                                              → Electricity + Heat
                                                              → Village / EV charging / data centre / onsen
                                 (ash → soil amendment)
```

High-quality logs to lumber, low-grade residues to energy — standard "cascading use." Extracts maximum value per tree before the remainder is burned for energy.

---

## Sources
- Mapion phonebook — 御杖村森林組合: https://www.mapion.co.jp/phonebook/M16006/29386/22930070324/
- 御杖村観光協会 (Mitsue Kanko) listing: https://www.mitsue-kanko.jp/sightseeing/%E5%BE%A1%E6%9D%96%E6%9D%91%E6%A3%AE%E6%9E%97%E7%B5%84%E5%90%88/
- Mishima/NIES anchor: `degraded_forests_paper_summary_and_application.md`
