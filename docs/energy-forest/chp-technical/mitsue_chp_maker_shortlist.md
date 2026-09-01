<!-- Version: v1.3 | Last modified: 2026-08-14 -->

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

| Maker | Tech / scale | Domestic? | Price | Notes |
|---|---|---|---|---|
| **巴商会 (Tomoe Shokai)** | wood-chip boiler + **Stirling engine**, ~10 kWe / ~180 kWth | ✅ (distributor) | Not published — quote-only | Closest domestic match to prototype scale; combustion+Stirling, *not* gasification. Lead for option (a). |
| **ネオナイト (Neonite)** | downdraft 2-stage **gasification**, smallest ~350 kWe | ✅ | Not published | Too big for a prototype — belongs to Tier B. Biochar/wood-tar recovery. |
| **静岡製機 (Shizuoka Seiki)** | small outdoor gasification, ~200 kWe | ✅ | Not published | Also above prototype scale; Tier B cluster candidate. |
| **All Power Labs (Power Pallet)** | downdraft micro-**gasification**, ~10–25 kWe | ❌ US (on JWBA list) | Historically listed ~$40,000–50,000 on their own site — **not re-verified this session, confirm on apl.solar before citing** | Best *gasification* size match; **import → pilot-exception only**. |
| **Volter** | CHP micro-gasifier, ~40 kWe | ❌ Finland | Not published | Benchmark; import-only. |
| **Spanner Re² (HKA-9 / HKA-30 / HKA-45)** | wood gasifier-CHP modules, ~9–45 kWe | ❌ Germany | Not published | Benchmark; smallest module near prototype scale; import-only. |

**⚠️ Price caveat:** none of the domestic makers (巴商会/ネオナイト/静岡製機/中外炉/神鋼) publish list
prices — this is a quote-only industry (site conditions, fuel spec, grid connection, and heat-offtake
design all move the number). The only figures found with any public backing are the imported micro-
gasifiers above, and even those are indicative, not confirmed current quotes. **Do not present the
prices in this doc as firm — they are a planning placeholder until vendor RFQs come back**, per the
outreach already drafted in `mitsue_biomass_visit_request_emails.md`.

---

## Tier B — 2 × 0.6 MWe (1.2 MWe) commercial fleet

Small woody-gasification tops out ~200–500 kWe, so 0.6 MWe per line is a **cluster of
modules**. (Reproduced from `mitsue_forest_workforce_energy_plan.md` §5.)

| Maker | Tech / scale | Fit | Price | Notes |
|---|---|---|---|---|
| **中外炉工業 (Chugai Ro)** | rotary-kiln gasification cogen | ✅ **lead** | Not published | Since 1997, NEDO-backed; reaches our per-unit size; tolerates rough fuel (branches/bark). |
| **神鋼環境ソリューション (Shinko / Kobe Steel grp)** | ~500 kWe-class up | backup | Not published | ⚠️ confirm **gasification** vs steam (big plants are combustion). |
| **静岡製機 (Shizuoka Seiki)** | small ~200 kWe outdoor unit | cluster | Not published | METI-funded, aimed at agriculture/forestry — closest in spirit. |
| **ネオナイト (Neonite)** | downdraft two-stage, ~350 / 750 kWe | cluster | Not published | Recovers charcoal + wood tar (biochar angle). |

**The only hard cost figure found in public sources** is operating (not capital) cost: 中外炉's own
published paper on small-scale gasification puts **generation cost at ~¥5/kWh**, meaning even a
¥40/kWh FIT tariff nets a thin margin — no installed-cost (¥/kW capex) figure is published anywhere
for these units. This reinforces [[reference_fit_grid_biomass]]'s "compute >> FIP" finding: margin
depends on a high-value offtake (the DC load), not the FIT rate. **No capex number should be quoted
to Mizuho/investors until a vendor RFQ comes back** — treat any capex figure elsewhere in this project
as a placeholder.

> **Imported — benchmark-only, not for procurement:** FORTES Energy (Latvia; 0.14–1.2 MWe
> gasification CHP, new Tokyo entity), Spanner Re² and Burkhardt (Germany; e.g. V3.90 module).
> Useful for spec comparison; do not meet the Japanese-manufacturer requirement.

---

## Prototype siting (decided 2026-07-17)
Site the Tier-A prototype on the **grounds of Sugano Organic (菅野, Tokuo Aomi; near 丹羽製材)**,
fed by **wood chips trucked a short haul (~2 km straight-line; road distance to confirm) from the Mitsue Village Forest Association worksite (牛峠工場, 神末797)**. Rationale:
it de-risks the gasification tech *and* builds the Sugano Organic / 丹羽製材 fuel partnership on a
real-fuel test, at a volume where the short chip haul is acceptable. (The later **commercial** CHP
sits *at* 神末 to avoid haul and use waste heat for drying; the **GPU compute** co-locates there
behind-the-meter — see `mitsue_fit_grid_check.md` three-node siting. A public prototype demo can
also run at the Koryukan / an unused factory.)

---

## Fuel chippers — sized to each CHP tier

Fuel spec: **non-construction-grade wood only** — thinnings, branches, bark, slabwood, reject logs
(see [[project_sugano_fuel_partner]]'s cascading-use model with 丹羽製材, whose *existing* chipper
makes pulp/paper chips and is NG for fuel — a separate fuel-spec chipper is needed either way).
Fuel-grade chip spec: <20% moisture after drying, no strict size-grading (unlike pulp chips).

Tonnage benchmark: [[reference_mishima_fukushima_chp]]'s real anchor is **~750 t/yr per 50 kWe**.

| CHP tier | Approx. fuel demand | Chipper class needed | Example models found | Price |
|---|---|---|---|---|
| **Tier A prototype** (10–20 kWe) | ~150–300 t/yr | Small tractor-mount / PTO or hand-fed | 富士テックス GS75G–GS126G (小型), or Kyoritz/Yamamoto small self-propelled | Small PTO unit (e.g. MKW-100, 18 HP tractor-mount): **¥390,000 new**. Small self-propelled diesel (used market): **¥400,000–650,000** (Yahoo Auctions closed-lot range). New small self-propelled: no confirmed list price found — expect roughly ¥1–3M range based on used-market floor, **unconfirmed, get a dealer quote**. |
| **Tier B commercial** (1.2 MWe, ~18,000 t/yr scaled from Mishima ratio) | ~15,000–18,000 t/yr | Mid-size self-propelled (continuous-duty, ~100–150 HP class) | 富士テックス GS133GH / GS152GH / GS285D (中型) — no public price found | Not published — **request quote from Fujitex/フジテックス directly**; do not guess a figure for the RFQ stage. |
| **Reference — industrial continuous-feed class** (for scale comparison, not a Mitsue-size recommendation) | 200–380 m³/h capacity | Track-mounted drum chippers | Morbark 4036 Track (200 m³/h, 765–800 HP, 25.8 t), Komptech Axtor (300 m³/h, 23 t), Pezzolato drum (up to 380 m³/h) | No prices published (imported industrial capital equipment, quote-only); shown only to illustrate that Tier B's tonnage does **not** require this class — a mid-size Japanese unit run on a normal work schedule (not 24/7) covers it. |

**Bottom line on chipper price data:** like the CHP units themselves, essentially no manufacturer
publishes a chipper list price in Japan — confirmed for Fujitex, Kyoritz/Yamabiko, and all imported
industrial brands searched. The only two real figures found are the ¥390,000 tractor-mount unit and
the ¥400–650k used-market range for small self-propelled units. **Next action: request quotes from
Fujitex (中型 GS133GH/GS152GH) and confirm with 丹羽製材/Niwa-san whether a shared fuel chipper at
Tier-B scale is realistic for their yard, or whether it should sit at 牛峠工場 instead.**

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
- 中外炉 小規模ガス化発電コスト論文（笹内, ~¥5/kWh 発電コスト）— https://www.npobin.net/research/data/155thSasauchi.pdf
- JWBA 木質破砕機・チッパー一覧 — https://jwba.or.jp/database/list-chipper/
- JWBA チッパー仕様一覧 PDF — https://jwba.or.jp/wp/wp-content/uploads/2022/04/木材破砕機_チッパーの一覧-破砕チップ対応_20190510.pdf
- フジテックス 木材チッパー製品一覧 — https://www.fjtex.co.jp/kankyo/products/tipper/
- Forest Journal「木材破砕機・2023年チッパー5選」（Morbark/Doppstadt/ERJO/Komptech/Pezzolato spec) — https://forest-journal.jp/tools/38595/
- MKW-100 トラクター装着チッパー ¥390,000 — https://chuko-noki.com/704/

## Related docs
- `mitsue_forest_workforce_energy_plan.md` §5 (energy stack) — CHP maker table source
- `mitsue_biomass_visit_request_emails.md` — vendor visit outreach
