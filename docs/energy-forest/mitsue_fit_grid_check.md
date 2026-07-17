<!-- Version: v0.5 | Last modified: 2026-07-17 -->

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

### What we still need (open items)
1. Identify the **配電用変電所 serving 神末797** from the Nara mapping PDF (not yet pinned;
   candidates are the Haibara / Nabari-side feeders — confirm).
2. File the **事前相談** for the site → get real 空き容量 + reinforcement cost/time.
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

### What we still need (open items)
1. Current fiber/broadband reach at 神末797 — NTT consultation (same NTT engagement as
   the school's 5.7, but a separate site survey).
2. Leased-line vs dark-fiber options and indicative lead time (the school's 5.7 saw a
   6–9 month NTT lead time — 神末 may be longer given remoteness).
3. Microwave/wireless backup link feasibility, given the site already needs a resilient
   comms path for remote CHP monitoring, not just compute traffic.
4. Bandwidth requirement driven by the anchor compute's actual workload (training vs
   inference vs hosting) — not yet sized, since the GPU cluster spec itself is still
   demand-led (`mitsue_evm_plan.md` §14, GPUs + DC fit-out).
5. Cost this alongside the grid **事前相談** already underway for 神末 (§2) — two
   separate utility surveys for the same site, worth scheduling together.

---

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
