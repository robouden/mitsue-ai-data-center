<!-- Version: v1.1 | Last modified: 2026-07-17 -->

# Biomass CHP — Maker Shortlist

Potential manufacturers for the Mitsue biomass CHP, split by the two build stages:
**Tier A — a 10–20 kWe first prototype**, and **Tier B — the 2 × 0.6 MWe (1.2 MWe)
commercial fleet**.

**Policy reminder:** the *commercial* units must be a **Japanese manufacturer** (domestic
service/parts, simpler FIT + 交付金 paperwork, local supply-chain story). Imported units
are **benchmark-only, not for procurement** — with one possible, explicitly-flagged
exception at prototype scale (see Tier A).

**Authoritative reference:** the JWBA list *国内で販売されている小規模木質バイオマス発電機器の一覧*
catalogues every domestic unit with specs — use it to confirm any figure below.

> ⚠️ All kW ratings here are **indicative / to verify** against the JWBA list or a vendor
> quote before use. CHP sizing in the wider project is still a planning estimate.

---

## The key finding — the prototype scale has no domestic gasifier

Domestic woody-**gasification** CHP has a floor around **~200–350 kWe** (Neonite's smallest
is ~350 kWe; Shizuoka Seiki ~200 kWe). A 10–20 kWe prototype is an **order of magnitude
below that floor**, so there is **no domestic-maker, gasification unit at prototype scale.**

This forces an explicit choice for the prototype (a decision, not a spec gap):

- **(a) Domestic non-gasification micro-CHP** — a wood-chip **boiler + Stirling engine**
  at ~10 kWe *does* exist domestically (巴商会). Keeps the Japanese-maker policy intact;
  trades gasification for Stirling/combustion at this stage.
- **(b) Imported micro-gasifier as a one-off pilot exception** — All Power Labs / Volter /
  Spanner HKA-class. Matches the eventual gasification tech, but breaks the domestic-maker
  policy for the prototype only — would need to be justified as pilot-only.
- **(c) Research / university partnership build** — slower, but keeps IP and learning local.

Recommendation to decide: **(a) for a fast, policy-clean, revenue-visible prototype**, or
**(b) if the prototype's main job is to de-risk the exact gasification tech** we scale to.

---

## Tier A — 10–20 kWe first prototype

| Maker | Tech / scale | Domestic? | Notes |
|---|---|---|---|
| **巴商会 (Tomoe Shokai)** | wood-chip boiler + **Stirling engine**, ~10 kWe / ~180 kWth | ✅ (distributor) | Closest domestic match to prototype scale; combustion+Stirling, *not* gasification. Lead for option (a). |
| **ネオナイト (Neonite)** | downdraft 2-stage **gasification**, smallest ~350 kWe | ✅ | Too big for a prototype — belongs to Tier B. Biochar/wood-tar recovery. |
| **静岡製機 (Shizuoka Seiki)** | small outdoor gasification, ~200 kWe | ✅ | Also above prototype scale; Tier B cluster candidate. |
| **All Power Labs (Power Pallet)** | downdraft micro-**gasification**, ~10–25 kWe | ❌ US (on JWBA list) | Best *gasification* size match; **import → pilot-exception only**. |
| **Volter** | CHP micro-gasifier, ~40 kWe | ❌ Finland | Benchmark; import-only. |
| **Spanner Re² (HKA-9 / HKA-30 / HKA-45)** | wood gasifier-CHP modules, ~9–45 kWe | ❌ Germany | Benchmark; smallest module near prototype scale; import-only. |

---

## Tier B — 2 × 0.6 MWe (1.2 MWe) commercial fleet

Small woody-gasification tops out ~200–500 kWe, so 0.6 MWe per line is a **cluster of
modules**. (Reproduced from `mitsue_forest_workforce_energy_plan.md` §5.)

| Maker | Tech / scale | Fit | Notes |
|---|---|---|---|
| **中外炉工業 (Chugai Ro)** | rotary-kiln gasification cogen | ✅ **lead** | Since 1997, NEDO-backed; reaches our per-unit size; tolerates rough fuel (branches/bark). |
| **神鋼環境ソリューション (Shinko / Kobe Steel grp)** | ~500 kWe-class up | backup | ⚠️ confirm **gasification** vs steam (big plants are combustion). |
| **静岡製機 (Shizuoka Seiki)** | small ~200 kWe outdoor unit | cluster | METI-funded, aimed at agriculture/forestry — closest in spirit. |
| **ネオナイト (Neonite)** | downdraft two-stage, ~350 / 750 kWe | cluster | Recovers charcoal + wood tar (biochar angle). |

> **Imported — benchmark-only, not for procurement:** FORTES Energy (Latvia; 0.14–1.2 MWe
> gasification CHP, new Tokyo entity), Spanner Re² and Burkhardt (Germany; e.g. V3.90 module).
> Useful for spec comparison; do not meet the Japanese-manufacturer requirement.

---

## Prototype siting (decided 2026-07-17)
Site the Tier-A prototype on the **grounds of Sugano Organic (菅野, Tokuo Aomi; near 丹羽製材)**,
fed by **wood chips trucked a short haul (~2 km straight-line; road distance to confirm) from the Mitsue Kanko worksite (牛峠工場, 神末797)**. Rationale:
it de-risks the gasification tech *and* builds the Sugano Organic / 丹羽製材 fuel partnership on a
real-fuel test, at a volume where the short chip haul is acceptable. (The later **commercial** CHP
sits *at* 神末 to avoid haul and use waste heat for drying; the **GPU compute** co-locates there
behind-the-meter — see `mitsue_fit_grid_check.md` three-node siting. A public prototype demo can
also run at the Koryukan / an unused factory.)

## Next steps
- Pull the current **JWBA small-scale list** and confirm every kW figure above.
- Decide the prototype path — option (a) / (b) / (c) — before requesting quotes.
- Confirm **Sugano Organic site readiness** (space, siting consent from Tokuo Aomi) and the
  chip-supply handshake with 丹羽製材 / the 牛峠工場 chipper.
- Vendor/site-visit outreach already drafted in `mitsue_biomass_visit_request_emails.md`
  (中外炉 / 神鋼 / 静岡製機 / ネオナイト priority; Spanner / Burkhardt as imported benchmarks).

## Sources
- JWBA 小規模木質バイオマス発電機器の一覧 — https://jwba.or.jp/database/list-small-woody-biomass-generation/
- JWBA list PDF (alphabetical, incl. All Power Labs) — https://jwba.or.jp/wp/wp-content/uploads/2024/11/20241122_国内で販売されている小規模木質バイオマス発電機器の一覧.pdf
- 巴商会 木質バイオマスボイラ＋発電（Stirling, ~10 kWe/180 kWth） — https://tomoeshokai.com/product/woody_biomass_boiler/generator
- ネオナイト 小規模木質バイオマスガス化発電（350/750 kW） — http://www.neonite.jp/biomass_lp/
- Metoree バイオマス発電機メーカー一覧 — https://metoree.com/categories/2730/

## Related docs
- `mitsue_forest_workforce_energy_plan.md` §5 (energy stack) — CHP maker table source
- `mitsue_biomass_visit_request_emails.md` — vendor visit outreach
