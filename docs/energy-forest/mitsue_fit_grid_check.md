<!-- Version: v0.9 | Last modified: 2026-08-09 -->

# FIT / FIP & Grid-Connection Check — Mitsue Kanko Working Site

Following Henry Takata's advice (check the grid *before* the plant — solar has eaten the
FIT export capacity in many rural areas), this is the first-pass desk check for the
**Mitsue Kanko forest co-op working site** — the 牛峠工場 chip/dry yard at
**神末797, 御杖村 (≈34.489, 136.206)** — as the candidate biomass-CHP location.
This is **not** the village office. Everything below is a desk estimate; the binding
answers come from a Kansai T&D 事前相談.

---

## 1. FIT / FIP — what a small biomass plant qualifies for in FY2026

| Item | Price (円/kWh) | Notes |
|---|---|---|
| 未利用木質バイオマス, **< 2,000 kW** | **40** | **higher** tier — this is our band |
| 未利用木質バイオマス, ≥ 2,000 kW | 32 | |
| 一般木質バイオマス | 24 | |
| 一般木材等 (≥10,000 kW) / 液体燃料 | — | **No longer eligible** for new FIT/FIP from FY2026 |

Term is **20 years**. Small-scale (<2,000 kW) 未利用材 gets the **higher** 40 円 rate —
standard tiered-FIT logic (small tier priced up to offset diseconomies of scale).
⚠️ These are the long-standing 未利用材 values; **confirm the exact FY2026 figure against
the primary METI table** (enecho `fit_kakaku.html` / the 2026 guidebook PDF) — the public
price-history site had the two tiers reversed, so treat any single secondary source with care.

**The decisive rule (confirmed):** for FY2026 new certification, **biomass ≥ 1,000 kW is
FIP-only** — it **cannot** get FIT. FIT (the 40 円 rate + 20-yr fixed price + 地域活用要件)
is available **only to plants < 1,000 kW** (waste-incineration-sited: < 2,000 kW). From FY2027
the FIP-only floor drops to ≥ 50 kW.

➡️ **Our ~1.15 MW plant → FIP.** Consequences:
- **No 40 円 fixed FIT** for the main plant. FIP pays **wholesale market price (JEPX) + a premium**
  — higher upside, but *variable*, not a guaranteed 20-yr tariff. Model revenue on FIP, not FIT.
- **The 地域活用要件 does not bind FIP** → the "10% self-consumption" question is **moot** for the
  main plant. (It would only matter if we deliberately built a separate <1,000 kW FIT unit.)
- Still needs full grid interconnection for export (the 事前相談).

### 地域活用要件 — moot for our plant (it's FIP), kept for reference
The requirement binds **FIT** plants only. Since our ~1.15 MW plant is **FIP**, it does **not**
apply. It would only matter if we built a *separate* <1,000 kW **FIT** unit — in which case a
CHP meets it by any one of: (1) self-consume ≥30 % elec; (2) 地域消費 via 再エネ特定卸供給 within
the prefecture; (3) CHP heat continuously used + ≥10 % elec self-consumed. Note the ~18 kW DC is
only ~2 % of output, so route (3) would **not** be cleared by the DC alone — it needs ~90 kW of
on-site load. Not a live constraint under the FIP base case.

### 分割禁止 — cannot split 2×600 kW on one site (confirmed)
Japan's anti-division rule: if **substantially the same applicant** files multiple facilities
on **adjacent / effectively one site** (same operator or same landowner), they are **deemed a
single facility**. So **2 × 600 kW on the same 神末797 yard = one 1.2 MW plant → over the
1,000 kW new-FIT cap → the new-FIT route is closed for that layout.** Splitting is not a way in.

### ✅ Siting decision (2026-07-17): compute in BOTH places, generation at working sites
Key economic reframe: **compute is worth ~6–20× more per kWh than power** (¥190–650/kWh vs FIP
¥30–40), so the power *source* for a GPU is ~1–5 % of its revenue. A DC therefore doesn't *need*
behind-the-meter CHP power to be profitable — **so compute goes in both places**, and co-locating
some at the CHP is about giving the CHP a high-value offtake (compute, not FIP), not cheap power.

> **Net of real GPU capex, this is a fill-rate-gated bet, not a free multiple.** The 6–20× above is
> gross revenue per kWh; netting a sourced 8×H200 server capex (~¥53M) and depreciation, a server
> only beats simply exporting its power once utilization clears **~45–70%** (price/depreciation-life
> dependent) — and essentially never at deep long-term-contract discounts on a 4-yr life. Full
> breakeven table in `../strategy/mitsue_revenue_model.md` §1a. This is the quantified version of
> "utilization, not power, is the constraint" below — size the anchor cluster to a fill-rate the
> HIGHRESO pipeline can actually underwrite, not to available CHP output.

| Node | Where | Role |
|---|---|---|
| **1. Commercial CHP + anchor compute** | **牛峠工場, 神末797** | Full ~1.15 MWe CHP at the chipping/drying site (heat→dryer loop). **Anchor / back-end GPU compute co-located** so the CHP's output feeds compute (~¥190–650/kWh) instead of FIP export (~¥30–40). |
| **2. Flagship showcase + experience DC** | **Old school (Koryukan)** | Public-facing GPU room + education/experience/reception center. Powered by **grid / green retail** (compute economics swamp the power cost). Gives the village **lease income + the exposure that drives the revitalization feeling.** Pitch for a use-exception (precedent: the *ECC* arrangement — confirm exact precedent). |
| **3. Prototype CHP** | **Sugano Organic grounds, 菅野** (Tokuo Aomi; near 丹羽製材) | Tier-A 10–20 kW prototype to de-risk tech + build the fuel partnership. Fed by chips hauled a short way from 神末 (~2 km straight-line; confirm road km). |
| **Promotion overflow** | unused factory | Optional extra demo/booth space if the Koryukan is full. |

**Why this keeps (not drops) the "activate the old school" pitch:** the school becomes the
**flagship, staffed, revenue-paying showcase** — stronger for revitalization than a back-end
compute shed, and it pays the village rent. The heavy generation stays at working sites; the
separate *dome* school is out of scope (billiards); onsen = separate **防災** node.

**Chip-transport note:** the *commercial* plant sits **at** 神末 to avoid haul + use waste heat for
drying. Only the **prototype** hauls chips (神末 → 菅野, ~2 km straight-line; confirm road km) —
acceptable at prototype volume, and it buys the Sugano Organic / 丹羽製材 partnership + a real-fuel test.

> **Extra option (parked): prototype CHP on the empty land *behind the old school*.** Upside: it
> could power the school's showcase compute **behind-the-meter on one site** — a self-contained
> "forest → power → compute" showcase, a strong revitalization visual. **Downsides (Rob, 2026-07-17):
> noise (engine/gasifier), on-site maintenance labor, and skilled supervision** (gasifiers need
> active supervision — Henry) — all poor neighbors for a **public education/community hub**. So
> generation is better kept at the working sites (Sugano / 神末); keep this only as a fallback if a
> quiet, well-managed micro-unit proves feasible.

### What this means for the design — the plant is an EXPORTER
Magnitudes matter: plant ~1.15 MWe / ~8,000 MWh/yr, sized to the **forest**, not to any load.
- **Data center (behind-the-meter, cap-free) — but small.** ~18 kW ≈ ~2 % of output. Real value:
  a **stable 24/7 baseload for the CHP** + avoided-retail price per kWh. It is the *stability
  anchor*, **not** the offtake.
- **Village — NOT behind-the-meter.** Dispersed on Kansai T&D's grid → reached only via **grid
  export** (FIP, or 再エネ特定卸供給) or a costly private line (自営線). Interconnection required.
- **The bulk → grid export via FIP** (confirmed: ≥1,000 kW = FIP-only in FY2026). Revenue = JEPX
  market price + premium (variable), **not** a fixed 40 円 tariff. So **the grid 事前相談 is central,
  not marginal** — this plant needs real export capacity, exactly Henry's concern.
- Net framing: **co-located DC baseload (behind-the-meter) → village + grid export on FIP → store.**
  NOT "self-consumption absorbs the plant", NOT "2×600 kW both on FIT", NOT "40 円 FIT on the plant".

---

## 2. Grid connection — who to ask and how

- **Network operator:** 関西電力送配電 (Kansai Transmission & Distribution). 御杖村 is in
  their Nara service area; the local office is the **奈良配電営業所**.
- **Public capacity map (< 154 kV):** Kansai T&D publishes downloadable **PDF 空き容量 maps
  per prefecture/municipality**, colour-coded (red/green) for substation areas where
  connection constraints may arise. There is **no interactive tool** — download the Nara
  PDF and read the substation serving the 神末 area.
- **The binding step — 事前相談 (preliminary consultation):** file a 高圧系統連系 事前相談
  with Kansai T&D for the exact site. Their reply names the serving 配電用変電所, the
  available 空き容量, and any reinforcement cost/lead-time (can be multi-year if the local
  bank is full — the exact risk Henry flagged).

### ✅ Serving substations — pinned (2026-08-03)
From Kansai T&D's public 154kV-未満 mapping (`kansai_td_nara_grid_map_2026-07-29.pdf`, 2 pages)
+ 空き容量一覧 (`154kv_less_space.pdf`, 36pp, both dated 2026-07-29/31): 御杖村 sits at the far
end of a 22kV loop off the **奈AD hub** (Tenri/Sakurai side) via 大野(室生)→赤瀬→**室生→長野→掛**
(奈CL→CM→CN→CO→CP, lines 奈96 東宇陀線 / 奈97 南宇陀線). **掛 (奈CP)** and **長野 (奈CO)** are the
substations physically closest to 御杖村/神末. See crop: `kansai_td_mitsue_area_grid_crop.png`.

**Capacity — bad news, confirms Henry's warning:** every substation on this loop shows **0 MW
available once the upstream network (上位系) is considered**, even where the local transformer
itself has a few MW nameplate headroom:

| 変電所 | 電圧 | 設備容量(MW) | 空容量 当該設備 | 空容量 上位系考慮 |
|---|---|---|---|---|
| 大野 (室生, 奈CL) | 22/6.6kV | 2 | 0 | **0** |
| 赤瀬 (奈CM) | 22/6.6kV | 2 | 1 | **0** |
| 室生 (奈CN) | 22/6.6kV | 2 | 2 | **0** |
| 長野 (奈CO) | 22/6.6kV | 2 | 2 | **0** |
| 掛 (奈CP, closest to 御杖村) | 22/6.6kV | 5 | 3 | **0** |
| 榛原 (奈AE, 77/22kV) | — | 42 | ー (予想潮流 **-20**, already over) | N-1電制不可 |
| 大宇陀 (奈AC, 22/6.6kV) | — | 11 | 0 | 0 |

➡️ **The whole eastern Uda→Soni→Mitsue 22kV branch is already saturated** (likely prior solar
interconnections, matching Henry's "solar ate the capacity" warning). A 1.2 MW export at 神末
will almost certainly need either (a) grid reinforcement (cost/lead-time TBD via 事前相談,
plausibly multi-year) or (b) a **ノンファーム型接続** (non-firm connection — allowed without
reinforcement, but subject to curtailment at congestion times, which cuts into FIP revenue
unpredictably). This raises the value of the on-site DC load (Node 1, §1) — every kWh consumed
behind-the-meter is a kWh that doesn't need this constrained export path.

### ✅ 事前相談 — how to file (2026-08-09)
- **Application portal:** https://www.kansai-td.co.jp/application/preliminary-consultation/index.html
  — download the Excel form (PDF no longer accepted as of 2025-12-16), fill it in, attach a
  location map, and submit to the **ネットワークサービスセンター** (☎ 06-7501-0695,
  Mon–Fri 9:00–12:00/13:00–17:00). **No fee. Reply within ~1 month.**
- **Two form variants** — 高圧 (6.6kV, `application-prior-consultation-6-6.xlsx`) vs 特別高圧
  (22–77kV, `application-prior-consultation.xlsx`). The form's own logic recommends voltage by
  capacity: **<2,000kW → 6.6kV** — so our ~1,150kW plant defaults to the **高圧 (6.6kV) form**,
  though a free-text override field (希望受電電圧, non-standard) lets us explicitly request 22kV
  instead, given the 6.6kV-side saturation found above.
- **Draft started:** `kansai_td_prior_consultation_DRAFT_2026-08-09.xlsx` (this folder) — site
  coords, plant type/capacity, and a note requesting 掛(奈CP)/長野(奈CO) pre-filled. Still needs:
  applicant legal entity name (Mitsue-it isn't incorporated yet — confirm with the Network Service
  Center whether pre-incorporation applicants are accepted), address, phone, self-consumption kW,
  and the location-map image paste-in.
- **Related applications surfaced (not yet needed at this stage):**
  - 供給側接続事前検討申込 (wheeling pre-study, once export volume is being formalized) —
    https://www.kansai-td.co.jp/application/consignment/low-pressure-supply-side.html
  - 申込様式一覧 (all KEPCO application form templates) —
    https://www.kansai-td.co.jp/application/documents.html
  - OCCTO 接続検討申込書 (broader-scope study, only if Kansai T&D's own study escalates there) —
    https://www.occto.or.jp/access/kentou/youshiki.html#kentou

### What we still need (open items)
1. ~~Identify the 配電用変電所 serving 神末797~~ — **done above.**
2. ~~File the 事前相談~~ — **portal + form identified, draft started** (above). Next: fill
   remaining fields and confirm applicant-entity question with the Network Service Center, then
   submit and ask specifically about ノンファーム接続 terms for this feeder.
3. ≥1,000 kW = **FIP-only** — **confirmed** (資源エネルギー庁 santeii materials). Still worth
   pinning to the primary 調達価格等算定委員会 PDF (`santeii/pdf/101_02_00.pdf`) for the file.
4. **★ Get FIP economics** — the plant's revenue now rides on FIP: what is the FY2026 biomass FIP
   **premium / 基準価格** for 未利用材, and how does JEPX price volatility hit the model? (Replaces the
   old "40 円 FIT" assumption.)
5. 分割禁止 — **confirmed**: cannot split 2×600 kW on one site.
6. 地域活用要件 — **moot** under the FIP base case (binds FIT only).
7. Model the **DC-load / village / export split** with real kW (DC ~2 %, village + export ~98 %) →
   drives the FIP export volume and the grid-capacity ask.
8. File the grid **事前相談** for 神末 — the binding 空き容量 answer for the export.

---

## 3. Network connectivity to 神末797 — open item (Phase-4 bucket F4)

The anchor-compute node (§1, Node 1) is the highest-value part of this whole loop — it
sells compute, not power (~¥190–650/kWh vs FIP ~¥30–40) — yet its network connectivity
has **not** been assessed. This is distinct from the fiber budget already in the PMB
(`mitsue_wbs.md` 3.5 Connectivity Assessment ¥0.4M + 5.7 Fiber Upgrade ¥10M), which is
scoped only to the **old-school showcase DC** (Node 2), not to 神末797.

神末797 is more remote than the school site — do not assume it can piggyback on the
school's fiber build. Logged as **Phase-4 bucket F4** in `mitsue_evm_plan.md` §14,
**TBD-pending-feasibility** (same status as F3, the thermal store), rather than guessing
a number now.

### ✅ NTT flets — CONFIRMED unavailable at 神末797 (2026-08-04)
Rob ran the NTT West flets-w.com/cart area checker directly for 〒633-1301 奈良県宇陀郡御杖村
大字神末797: result = **「未提供エリアです」(not a service-provided area) — フレッツ光を
ご利用いただけません.** This is a definitive negative, not an estimate. Since 御杖村's
village-wide FTTH coverage is 95% (below) but NTT's own network doesn't reach this address,
**Komadori Cable must be running independent fiber plant, not reselling NTT's.** NTT direct is
now ruled out for 神末797 — Komadori is the only remaining fiber candidate to confirm (call
them directly for this exact address, their web servicearea pages 404 for outside lookups). If
Komadori also comes back negative, the realistic options narrow to **Starlink as primary** or
an NTT dedicated-line/新設 build (likely a worse lead-time than the school's 6–9mo, since this
address is confirmed outside their standard footprint).

### FTTH coverage rate — village-wide, sourced (2026-08-03)
No public NTT fiber-route map exists (unlike Kansai T&D's grid map — telecom route maps aren't
published; only an address-by-address availability checker is). But 総務省's per-municipality
FTTH household coverage dataset (令和5年度末, i.e. as of 2024-03) gives a real number:
**御杖村 = 95% FTTH household coverage.** Better news than the Komadori price-list ambiguity
alone suggested — though it's village-wide household coverage, not confirmed for 神末797
specifically or for business-grade service. Source: 総務省 `main_content/001026064.xlsx`
("令和５年度末ＦＴＴＨ世帯カバー率（市区町村別）"), https://www.soumu.go.jp/main_sosiki/joho_tsusin/broadband/index.html.
Next step unchanged: run 神末797's exact address through NTT West's checker (flets-w.com/cart).

### First-pass desk check (2026-08-03)
- **Village ISP is not NTT — it's こまどりケーブル (Komadori Cable)**, a 3rd-sector CATV company
  (shareholders: KCN/近鉄ケーブルネットワーク as parent, 奈良県, and 16 municipalities incl.
  御杖村) serving NE + southern Nara. 御杖村 is a listed service area. Residential-grade plans:
  **光1G (¥6,050/mo, ~1 Gbps FTTH)**, 光100Mプレミアム (¥4,950/mo), and a **legacy コアキシャル
  Kブロード 1Mbps tier still on the price list** — the coax tier's survival implies FTTH may not
  yet reach every hamlet. **No business/dedicated-line/static-IP tier is publicly listed** — this
  is a consumer CATV ISP, not an enterprise carrier.
- **神末797 specifically — unconfirmed.** Komadori's public site doesn't break out coverage by
  chiku/hamlet; whether 牛峠工場 itself is on their FTTH footprint or still coax-only needs a
  direct call to Komadori (0745-xx, via their servicearea/mitsue page) or NTT West's area
  checker (flets-w.com/cart, or ☎0120-116-116) for the exact address.
- **NTT flets availability at 神末797 — not found via public search**; must query NTT West's
  area tool directly by address (can't infer from web).
- **★ Satellite (Starlink) — the strongest lead for a remote/CHP site.** Independent of local
  telco buildout and rural-grid fragility already documented in §2; SpaceX now offers a
  Business/Priority tier (higher-throughput, ~100–220+ Mbps, low latency) sized for exactly this
  kind of unmanned or lightly-staffed remote industrial site. Worth pricing as **primary or hot
  backup** ahead of chasing NTT leased-line/dark-fiber lead times.

### What we still need (open items)
1. Confirm FTTH vs coax at 神末797 specifically (call Komadori + NTT West area checker).
2. If FTTH doesn't reach it: leased-line vs dark-fiber cost/lead-time from NTT (school's 5.7 saw
   6–9 months; 神末 likely longer, more remote) vs. **Starlink Business as a faster-to-deploy
   alternative** — price both.
3. Microwave/wireless backup link feasibility — mountainous terrain, line-of-sight to a relay
   tower unassessed; the site needs a resilient comms path for remote CHP monitoring regardless
   of compute traffic.
4. Bandwidth requirement driven by the anchor compute's actual workload (training vs inference
   vs hosting) — not yet sized, GPU cluster spec still demand-led (`mitsue_evm_plan.md` §14).
   ⚠️ Do NOT assume the Koryukan/village-center node (Node 2) has better connectivity than 神末
   just because it's more central — unverified (2026-08-03). No published Wi-Fi/fiber data for
   the Koryukan itself; `mitsue_wbs.md` §5.7 already budgets ¥10M / 6–9mo NTT fiber build there,
   implying the PMB's own working assumption is it does NOT yet have an adequate pipe either.
   Confirm both addresses (Komadori + NTT West area checker) before routing workloads by node.
5. Cost this alongside the grid **事前相談** already underway for 神末 (§2) — two separate
   utility surveys for the same site, worth scheduling together.

---

## Sources (事前相談 application, added 2026-08-09)
- 事前相談・高圧系統連系 お申込み — https://www.kansai-td.co.jp/application/preliminary-consultation/index.html
- ネットワークサービスセンターのご案内 — https://www.kansai-td.co.jp/consignment/service-center.html
- 申込様式一覧 — https://www.kansai-td.co.jp/application/documents.html
- 供給側接続事前検討申込（託送供給） — https://www.kansai-td.co.jp/application/consignment/low-pressure-supply-side.html
- OCCTO 接続検討申込書 — https://www.occto.or.jp/access/kentou/youshiki.html#kentou
- OCCTO ノンファーム型接続の取組 — https://www.occto.or.jp/assets/grid/business/documents/NF_setsuzokuriyou_20240701.pdf
- 各一般送配電事業者の空き容量マップについて（資源エネルギー庁） — https://www.enecho.meti.go.jp/category/saving_and_new/saiene/grid/07_map.html
- 一般送配電事業者の出力制御見通しマッピング情報リンク集（OCCTO） — https://www.occto.or.jp/access/link/mapping.html

## Sources (connectivity, added 2026-08-03)
- こまどりケーブル 提供サービス — https://komadori.ne.jp/service/internet/
- こまどりケーブル 御杖村サービスエリア — https://www.komadori.ne.jp/servicearea/mitsue/mitsue_price.html
- こまどりケーブル会社概要 (Wikipedia) — https://ja.wikipedia.org/wiki/こまどりケーブル
- NTT西日本 フレッツ光 エリア確認 — https://flets-w.com/cart/

## Sources
- 2026年度以降の買取価格等 (METI press, 2026-03-19) — https://www.meti.go.jp/press/2025/03/20260319004/20260319004.html
- FIT/FIP ガイドブック 2026 — https://www.enecho.meti.go.jp/category/saving_and_new/saiene/data/kaitori/2026_fit_fip_guidebook.pdf
- バイオマスFIT価格推移 (新電力ネット) — https://pps-net.org/fit_kakaku-biomass
- 2026年度以降 一部バイオマスがFIT/FIP新規認定対象外 (BPA) — https://www.bpa.or.jp/news/
- 関西電力送配電 マッピング（154kV未満） — https://www.kansai-td.co.jp/consignment/disclosure/distribution-equipment/mapping.html
- 高圧系統連系 事前相談 申込 — https://www.kansai-td.co.jp/application/preliminary-consultation/index.html
- 奈良配電営業所 — https://www.kansai-td.co.jp/corporate/profile/office/nara/nara.html
- FIT制度における地域活用要件について (資源エネルギー庁) — https://www.enecho.meti.go.jp/category/saving_and_new/saiene/community/dl/20220316_fit.pdf
- 「地域活用電源」自家消費率30%・熱利用時10% (日経BP) — https://project.nikkeibp.co.jp/ms/atcl/19/news/00001/00509/
- 発電等設備の分割対策に関するQ&A (資源エネルギー庁) — https://www.enecho.meti.go.jp/category/electricity_and_gas/electric/summary/regulations/02_faq/index.html
- 事業計画策定ガイドライン（バイオマス発電） — https://www.enecho.meti.go.jp/category/saving_and_new/saiene/kaitori/dl/fit_2017/legal/guideline_biomass.pdf

## Related
- `mitsue_processing_center` (memory) — 牛峠工場 site coordinates
- `mitsue_chp_maker_shortlist.md` — plant selection (Henry advising)
- `mitsue_forest_workforce_energy_plan.md` §5 — energy stack sizing
- `mitsue_evm_plan.md` §14 — Phase-4 forward capital, incl. F4 network connectivity (this doc §3)
- `mitsue_wbs.md` 3.5 / 5.7 — school-site connectivity assessment + fiber upgrade (PMB, not F4)
