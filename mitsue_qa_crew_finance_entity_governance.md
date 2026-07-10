<!-- Version: v1.1 | Last modified: 2026-07-11 -->

# BIOMASS ENERGY & AI — Q&A: Crew, Financial Model, Entity Structure, Governance

Answers to four questions raised 2026-07-09, drawing on the forest workforce plan, EVM plan, business case, stakeholders doc, and NGO-setup materials.

---

## 1. How big is the crew now, and how does it scale up?

The forestry crew belongs to **御杖村森林組合 (Mitsue Kanko)**, not the project entity — the project's role is to fund its growth, not to hire directly.

- **Current size:** very small — sources disagree slightly (3 regular staff avg. age ~33 per one recruiting interview; "2 field + 2 office" = 4 total per another listing). Either way, a 3–4 person operation.
- **Current output:** ~66–68 ha/yr thinning, only ~120–300 m³/yr recovered timber — tiny relative to the village's 7,051 ha of forest, because it's subsidized thinning, not mechanized harvest.
- **Scaling path (the plan's core mechanism):** energy revenue pays for more crew + machines (harvester/forwarder, chipper, drying) → bigger crew harvests more → feeds a bigger biomass plant — a self-funding loop modeled on Shimokawa/Nishiawakura.
  - Doubled crew → ~140 ha/yr → 50% of forest over 25 yr → ~1.15 MWe (**recommended baseline**)
  - Tripled crew, full mechanization → ~200 ha/yr → ~1.6 MWe
- **Where new people come from:** partly the co-op's own hiring, but the plan names a concrete external channel — **天川村森林塾 (Tenkawa Forest School)**, an 8-day felling/chainsaw course that has trained 60+ people since 2017 explicitly "from inside and outside the village." That's the up-skilling pipeline for the doubled crew.

---

## 2. High-level financial model

Two budget tiers exist — kept separate, not on the same books.

### Phase 0–3 build (¥220M BAC / ¥245M total, Baseline Rev 1, May 2026)

| Item | ¥M |
|---|---|
| School renovation | 38 |
| Solar PV ~100kW | 22 |
| Battery storage | 12 |
| EV charging (4 stations) | 15 |
| Data center fitout | 20 |
| Forestry (5–10ha + roads + replant) | 25 |
| Fiber connectivity | 10 |
| Testing/commissioning | 8 |
| Contingency (18%) | 27 |
| **Phase 3 total** | **177** |
| Management reserve | 25 |
| **Total project budget** | **245** |
| Funding target (unsecured; ¥0 raised/committed to date) | 192 (gap if fully realized: ¥28–53M) |

### Phase 4 forward capital (outside the PMB, funded by grants + operating revenue)

| Item | ¥M |
|---|---|
| CHP fleet (2×0.6 MWe) | ~800 |
| Fuel-prep (drying/chipping/handling) | ~120 (range 75–215) |

### Illustrative operating P&L by Year 5 (Base case)

| | Low | Base | High |
|---|---|---|---|
| Annual revenue (6 streams: FIT electricity, heat, DC hosting, EV, broadleaf/J-Credit, other) | ¥28M | ¥45M | ¥67M |
| Operating cost (~60%) | ¥18M | ¥27M | ¥35M |
| **Net surplus** | ¥10M | ¥18M | ¥32M |
| Payback on ¥200–290M capital | ~18 yr | ~14 yr | ~10 yr |

The whole build is gated (G1–G4); the village/investors never commit past what's funded and de-risked at each stage.

---

## 3. Is an NPO the right vehicle, or would a social enterprise (K.K. with capped/rededicated profit in the articles) be more suitable?

Already decided, and more specific than a straight NPO-or-KK choice: a **two-tier entity**.

- **Tier 1 — 一般社団法人 (Ippan Shadan Hojin, non-profit type)**, with a path toward NPO法人/公益認定 later (per the stakeholders doc and lawyer-meeting prep with SIIF's Yuya Kato). Holds the charter, the village 官民連携 relationship, IP, forestry programme, J-Credit registration. Receives grants/donations — legally cannot distribute profit. The draft teikan already encodes this: **Article 26 — "no distribution of surplus."**
- **Tier 2 — 合同会社 (GK, a for-profit LLC-type entity, not a K.K.)**. Holds the actual assets — DC, biomass CHP, solar, battery, FIT/hosting contracts. This is where equity investment and dividends legally live.
- **The link:** Tier 1 owns the majority of the Tier 2 GK plus a charter "mission-lock" clause, so investors get a real but minority, contracted return and can't redirect the mission or strip community assets.

The "social enterprise with capped/rededicated profit written into the articles" is essentially **what the ISH already is under Japanese law** — non-distribution is a statutory requirement of the non-profit-type ISH, not something that needs inventing via a KK's articles. A KK doing the same thing would work against the grain of its own legal form and forfeit grant/donation eligibility. Given the funding stack leans heavily on 交付金, foundation grants, and MoE subsidy (all of which require or strongly favor a non-profit recipient), the two-tier ISH+GK structure fits — a KK would only make sense if the project needed equity as its *primary* capital source, which it doesn't.

---

## 4. How is Mitsue Kanko governed, and what's the future relationship? Who holds decision power? Does the plan assume their full agreement? Should the project plan be formulated autonomously?

**Governance of Mitsue Kanko itself:** a member-owned 森林組合 under the Forestry Cooperative Act — forest-owning members (組合員) hold shares (出資金, ¥31.3M capital), elect a board (理事会) led by a representative director (代表理事組合長 — one source names Tanaka Toshihiro, unconfirmed on the public registry), with a general meeting of members as the top decision body. It belongs to the 奈良県森林組合連合会 (prefectural federation). Financials aren't public — a structural blind spot, not something either party is missing.

**Relationship to the project entity:** currently informal. The stakeholders doc lists "Local Forestry Group" as an **"Early consultation partner (met early 2026)"** — not a signed MOU, not a board seat, not a formal agreement. Mitsue Kanko is separately envisioned as the **sole operator** of planting/tending work.

**Does the plan assume full agreement/collaboration?** Yes. The business case treats "Forestry co-op / landowners" as a stakeholder who is *asked* for sugi harvesting access and restoration participation, and gets fair compensation + J-Credit income in return — via **"Phase-1 contracts"** that don't exist yet. Their formal buy-in is a Phase 1 dependency, not something already secured. The plan's entire workforce-scaling mechanism (Q1 above) depends on Mitsue Kanko agreeing to grow, mechanize, and be funded by an outside energy project — a real ask of their board/general-meeting, not a foregone conclusion.

**Should the project plan be formulated autonomously?** Drafting it solo is fine — someone has to write the first version. The overstep would be presenting it to the village, funders, or Mitsue Kanko as a settled arrangement rather than a **contingent proposal** pending the cooperative's own board/general-meeting approval. Recommend the documents keep using conditional framing ("proposed," "Phase 1 contracts pending") wherever they describe Mitsue Kanko's role, and that a direct approach to their 代表理事組合長 becomes an explicit Phase 0/1 action item if it isn't already one.
