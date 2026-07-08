<div style="font-family:-apple-system,Helvetica,Arial,sans-serif;">
<p style="font-size:7.5pt; font-weight:600; letter-spacing:0.25em; color:#3a7a5a; margin:0 0 4mm;">PROJECT DOCUMENT</p>
<h1 style="font-size:28pt; font-weight:700; margin:0 0 2mm; border-bottom:1px solid #eee; padding-bottom:2mm;">Mitsue-kun Project</h1>
<p style="font-style:italic; color:#666; margin:2mm 0 8mm;">Implementation Plan</p>
<img src="assets/logo_go.png" alt="御" width="50%" style="display:block;margin:0 auto;">
<div style="height:105mm;"></div>
<table style="width:100%; border-collapse:collapse; font-size:9pt;">
<tr><td style="padding:3mm 4mm; border:1px solid #ccc; font-weight:bold; width:30%;">Version</td><td style="padding:3mm 4mm; border:1px solid #ccc;">v2.14</td></tr>
<tr><td style="padding:3mm 4mm; border:1px solid #ccc; font-weight:bold;">Date</td><td style="padding:3mm 4mm; border:1px solid #ccc;">2026-07-03</td></tr>
<tr><td style="padding:3mm 4mm; border:1px solid #ccc; font-weight:bold;">Author</td><td style="padding:3mm 4mm; border:1px solid #ccc;">Rob Oudendijk</td></tr>
</table>
</div>

<div style="page-break-after:always; break-after:page; height:0; margin:0; padding:0;"></div>

# Implementation Plan

## Overview

This plan breaks the implementation of the Mitsue Sustainable Energy & AI Data Center project into **five phases over the first three years**, with a clear path from concept to operational pilot. Each phase has defined deliverables, funding requirements, and risk checkpoints.

The 25-year vision remains, but the first 3 years are the make-or-break period. Get the foundations right and the rest becomes possible.

---

## Phase Overview

| Phase | Timeframe (operative — live Gantt) | Focus | Estimated Budget |
|-------|-----------|-------|------------------|
| 0. Pre-Foundation | Apr–Oct 2026 | Local trust, founding team, basic structure | ¥0–500,000 (self-funded) |
| 1. Foundation | Oct 2026 – May 2027 | NPO incorporation, feasibility studies | ¥3–8 million |
| 2. Pilot Design | May 2027 – May 2028 | Detailed engineering, partnerships, permits | ¥15–30 million |
| 3. Pilot Build | May 2028 – Nov 2029 | Construction of small first stage | ¥120–290 million |
| 4. Operation & Scale | Nov 2029+ | Operations, monitoring, expansion | Variable |

> **Schedule status (updated 2026-07-03).** The calendar above reflects the **live OpenProject Gantt**, which is the operative schedule. It runs later than the original April-2026 month-relative plan (P0 = M1–3, P1 = M4–9, etc.) because Phase 0 trust-building and co-founder confirmation are taking longer than the compressed first draft assumed. The month-relative durations are retained in the section headings below for continuity. A formal re-baseline (EVM Baseline Rev 2, due Dec 2026) will fold this schedule into the cost baseline; until then the EVM PMB monthly curve remains Rev 1. **Phase 1 formally begins only after Gate 1 clears** (JP co-founder verbal commitment + ¥3–8M) — some Phase 1 legal/NGO prep is already running ahead of the gate as research only.

These ranges are realistic for rural Japan but conservative — actual costs vary widely depending on biomass CHP and solar/EV equipment, battery storage (subject to feasibility study), fiber availability, and building condition.

---

## Phase 0 — Pre-Foundation (Apr–Oct 2026 · orig. Months 1–3)

**Goal:** Establish local trust and a small founding team before any public announcements or formal structures.

### Critical Actions
1. **Private conversations with village leadership** — village mayor, key council members. Listen first, present second.
2. **Conversations with 自治会 (community association)** leaders in Sugano and surrounding hamlets.
3. **Identify 3–5 founding team members** including at least one well-respected Japanese co-founder with rural credibility.
4. **Quiet conversations with 2–3 sympathetic landowners** to gauge interest in cedar harvesting partnerships.
5. **Draft preliminary charter** in Japanese and English (simple, 1–2 pages).

### What NOT to Do in Phase 0
- No public announcements
- No social media yet
- No press contact
- No detailed financial commitments

### Deliverables
- Founding team agreed (verbal commitments)
- Mitsue village leadership informed and supportive (or neutral)
- Draft charter document
- List of potential landowner partners

---

## Phase 1 — Foundation (Oct 2026 – May 2027 · orig. Months 4–9)

**Goal:** Establish the legal entity and complete feasibility studies that will enable serious funding applications.

### 1A. NGO Setup — Choosing the Right Structure

There are **three relevant non-profit structures** in Japan, with different tradeoffs:

#### Option A: 一般社団法人 (Ippan Shadan Hojin) — General Incorporated Association
- **Easier to set up** — registration only, no government approval needed
- **Faster** — typically 1–2 months to incorporate
- **More flexible** governance
- **Recommended for the project's first 1–2 years**

#### Option B: NPO法人 (NPO Hojin / 特定非営利活動法人) — Specified Nonprofit Corporation
- **Requires prefectural government authorization (認証)** — 4-month review period
- **More public credibility** for grants and donations
- **Stricter regulations** — minimum 10 members, 3 directors, 1 auditor; mandatory public disclosures
- **Best path for long-term legitimacy and government grants**
- **Recommendation:** Convert to this in year 2–3 when ready

#### Option C: 認定NPO法人 (Nintei NPO Hojin) — Certified NPO
- **Highest credibility tier** — donors get tax deductions
- **Available 5+ years after NPO法人 incorporation** (or special early certification one-time)
- **Strict requirements** — public donation thresholds, financial transparency
- **Long-term goal** — apply once track record is established

### 1E. Feasibility Studies to Commission

These are the **single most important documents** for unlocking serious funding. Get these right.

1. **Forestry Feasibility Study** (~¥1.5–3M)
   - Native forest restoration plan and species selection for candidate sugi plots
   - Transportation costs from steep terrain
   - Native forest restoration plan and timeline
   - Carbon sequestration estimate
   - Recommended providers: forestry consultants connected to 日本林業協会 or 林野庁

2. **Energy Systems Feasibility Study** (~¥2–4M)
   - **Biomass CHP sizing (primary source)** — gasifier or CHP unit fuelled by sugi forest thinnings, providing 24/7 baseload electricity (primary output) and heat (secondary output); sizing, capex, fuel-supply logistics, and dispatch model
   - Solar PV sizing on Koryukan rooftop and adjacent surfaces (complementary, intermittent supply)
   - EV charging capacity sizing (2–4 stations initially, scalable), powered by the local biomass+solar system
   - **Small-scale hydropower** from village water-supply intake points (explicitly cited in the village RE plan — Key Initiative 1; evaluate feasibility and output potential)
   - **V2H (Vehicle-to-Home/Building)** integration — using EV stored energy in buildings during grid outages (village RE plan Basic Policy 2.2)
   - Grid connection and FIT/FIP eligibility
   - Battery storage requirements (data center load + EV charging + 12–48h blackout backup; subject to feasibility study confirmation)

3. **Building & Site Assessment** (~¥1–2M)
   - Structural condition of Koryukan building
   - Seismic compliance requirements
   - Required renovations for data center use
   - Zoning and permit considerations

4. **Connectivity Assessment** (~¥0.3–0.5M)
   - Current fiber capacity to Mitsue
   - Upgrade requirements and costs
   - Coordination with NTT / regional providers

### Native Forest Restoration — Indicative Scope

First-order planning figures to guide the Phase 1 forestry feasibility study. Final scope, species mix, and timeline come from that study.

**Target area for sugi-to-native conversion:**

| Scenario | Area (ha) | Timeframe |
|---|---|---|
| Phase 3 pilot | 5–10 | Years 2–4 |
| Phase 4 expansion | 20–40 | Years 5–10 |
| Long-term target | 50–100+ | Years 10–25 |

Mitsue village has approximately 88% forest cover. The project focuses on replacing aged sugi (Cryptomeria japonica) monoculture with native broadleaf species — predominantly konara oak (Quercus serrata), kunugi oak (Quercus acutissima), and chestnut (Castanea crenata) — suited to the Yoshino-Kumano mountain climate zone.

**Carbon sequestration potential:**

Native broadleaf forests in the Japanese mountain climate accumulate roughly 3–6 tC/ha/yr once established. A 50 ha restored stand at maturity could sequester 150–300 tCO₂/yr, supporting J-Credit certification and providing a long-term revenue stream for participating forest landowners.

**J-Credit pathway:** Forest carbon credits under the J-Credit scheme require a certified methodology and minimum project area. Phase 1 forestry feasibility will confirm eligibility, pre-qualification path, and coordination with the Forestry Agency (林野庁).

**Data center electrical load (10–20 servers, edge compute, PUE 1.2):**

| Scenario | IT load | Facility load | Annual kWh |
|---|---|---|---|
| Lean (10 × 300 W) | 3.0 kW | 3.6 kW | ~31,500 |
| Baseline (15 × 500 W) | 7.5 kW | 9.0 kW | ~78,800 |
| AI-leaning (20 × 700 W, PUE 1.3) | 14.0 kW | 18.2 kW | ~159,500 |

PUE 1.2 is a realistic planning figure for the air-cooled repurposed-facility archetype (HIGHRESO's published target for similar deployments is <1.1).

**Sources & assumptions** (for Phase 1 feasibility study validation):

- HIGHRESO Co., Ltd. — air-cooled data centers in repurposed buildings, published PUE target <1.1: https://highreso.jp/sdgs/
- Mitsue Village forest cover and forestry programme: Grokipedia summary of village policy: https://grokipedia.com/page/mitsue_nara
- Native broadleaf species suitability for Yoshino-Kumano climate zone: 林野庁 (Forestry Agency) afforestation guidelines
- Carbon sequestration rates for native broadleaf secondary forest in Japan: Forestry and Forest Products Research Institute (森林総合研究所) reference data
- J-Credit forest carbon methodology: Japan's J-Credit Scheme — https://japancredit.go.jp/
- Server power draw (300–700 W/server) and PUE assumptions: edge data center industry references including [IAEI Magazine](https://iaeimagazine.org/electrical-fundamentals/how-much-electricity-does-a-data-center-use-complete-2025-analysis/) and [Dgtl Infra](https://dgtlinfra.com/what-is-an-edge-data-center/).
- EV charger utilization model in rural Japan: planning assumption (10–20% utilization Year 1–3, 30–50% Year 5+), to be validated in feasibility study.

### Phase 1 Deliverables
- Legal entity registered
- Feasibility studies completed
- Letter of interest from Mitsue village government
- **Coordinate with the village on its 地域脱炭素移行・再エネ推進交付金 multi-year 事業計画; position the project as the 官民連携 operating partner** (per the MoE funding ladder — village completed step 1 in Jan 2025; this is step 2)
- Bilingual project website (basic, professional)
- Initial advisory board formalized
- Bank account, accounting system in place

---

## Phase 2 — Pilot Design (May 2027 – May 2028 · orig. Months 10–18)

**Goal:** Convert feasibility studies into detailed engineering plans, secure pilot funding, and finalize partnerships.

### Key Activities
- Detailed engineering and architectural plans
- Permitting (forestry, building, electrical & fire safety for EV, FIT/FIP registration; battery storage permits if feasibility study confirms)
- Partnership agreements with landowners (template contract)
- Vendor selection for solar/EV equipment, data center hardware, IT; battery storage vendor scoping deferred pending feasibility study
- Major funding applications submitted
- Hiring of first 2–3 part-time staff

### Funding Targets — Phase 2
- Aiming for **¥30–50M secured by end of Phase 2** to cover Phase 2 costs and Phase 3 startup

---

## Phase 3 — Pilot Build (May 2028 – Nov 2029 · orig. Months 19–30)

**Goal:** Build a small but real version of the project — a functioning proof of concept.

### Suggested Pilot Scope
- **Forestry**: First 5–10 hectares of sugi harvested and replanted
- **Energy**: Biomass CHP from sugi thinnings (primary baseload electricity + heat) + complementary rooftop solar panels + EV charging stations (2–4 chargers initially, scaling with demand); battery storage to be confirmed by feasibility study
- **Building**: Renovate one wing of the chosen Phase-1 building — the former Sugano Elementary School (Koryukan) is the leading candidate, final site confirmed in Phase 1 — for office and small server room
- **Data center**: ~10–20 servers, edge computing focus
- **EV charging**: 2–4 charging stations as visible village benefit

### Why Start Small
- Demonstrates feasibility before larger spending
- Builds operational know-how
- Creates fundable success story for Phase 4 expansion
- Lowers risk if a major component proves harder than expected

> **Early visible benefits to the village.** The 25-year horizon applies to forest restoration ecology — concrete community benefits arrive much earlier. Year-by-year tangible outcomes through Phases 0–3 (Koryukan reactivation, landowner income, EV charging, blackout resilience, data center jobs) are summarized in the "Early Benefits — Visible Within Five Years" table in [`mitsue_village_government_onepager.md`](mitsue_village_government_onepager.md).

---

## Phase 4 — Operation & Scale (Nov 2029+ · orig. Months 31+)

This is when the project transitions from "construction" to "ongoing institution." Detailed planning happens in Year 2 once Phase 1 results are in — the figures below are illustrative operating-model targets.

### Operating Revenue Ramp

The revenue model is built on six streams already visible at pilot scale. A standalone one-page summary is in [`mitsue_revenue_model.md`](mitsue_revenue_model.md).

| Revenue stream | Year 1 (ops) | Year 5 | Year 10 |
|----------------|-------------|--------|---------|
| Data center hosting fees | Ramp up | ¥15–30M | ¥40–80M |
| Electricity sales (FIT/FIP — biomass CHP + solar) | Ramp up | ¥5–15M | ¥10–30M |
| EV charging fees | Ramp up | ¥1–3M | ¥3–8M |
| Carbon credits (J-Credit) | — | ¥1–3M | ¥3–10M |
| Forestry products (timber, lumber) | — | ¥3–8M | ¥10–20M |
| Education / consulting (playbook) | — | ¥1–3M | ¥3–8M |
| **Total (illustrative)** | | **¥28–67M** | **¥74–166M** |

*Biomass CHP (fuelled by sugi thinnings) remains the primary energy source; solar, battery storage, and EV charging are complementary. The circular local energy economy — forest powers village — is the core of the operating model.*

### Break-even and Surplus

- **Operating costs by Year 5**: ~¥18–35M/yr (est. 60% of revenue)
- **Net annual surplus by Year 5**: ¥10–32M
- **Approximate capital payback period**: 10–18 years (depending on grant vs. loan vs. revenue-financing mix)
- **Break-even / net-surplus year**: approximately Year 5 at base-case execution

Once the project reaches net surplus, reinvested funds go first to forestry scale-up (additional ha of sugi conversion), then data-center capacity expansion, then replication support for other villages.

*Phase 1 feasibility studies will replace these illustrative figures with vetted projections anchored to real survey data.*

---

## Funding Strategy

### Layered Funding Approach

The project should pursue **multiple funding streams in parallel**, never depending on a single source.

#### Layer 1 — Founding Capital (Phase 0–1)
- **Self-funded / founder contributions**: ¥0.5–2M
- **Friends-and-family / advisor support**: ¥1–3M
- **Small private donations**: ¥1–3M

#### Layer 2 — Government Grants (Phase 1–2)

**Most relevant programs:**

- **地方創生関係交付金 (Regional Revitalization Grants)** — Cabinet Office; for projects creating jobs and stemming rural depopulation. Typically ¥5–50M per project.
- **林野庁 / Forestry Agency subsidies** — for native forest restoration, sugi conversion, forest road infrastructure
- **NEDO grants** — New Energy and Industrial Technology Development Organization; renewable energy R&D
- **METI green technology subsidies** — for rural energy resilience and EV infrastructure
- **Nara Prefecture rural development grants** — varies by year; check 奈良県地域創造課
- **Mitsue village local subsidies** — small but politically meaningful
- **Mitsue village startup subsidy program** — partial business-cost support for new enterprises; village policy targets **5 new enterprises over 5 years** to retain youth and stem depopulation. The project should be positioned as filling one or more of those slots. *Eligibility for NPOs to be confirmed with the village 募集要項; if the program is restricted to for-profit entities, the NPO can incorporate subsidiary 合同会社 / GKs (forestry operations, EV/energy services) that apply separately.* Politically aligned with stated village policy; coordinate with the mayor before applying.
- **森林環境譲与税 (Forest Environment Transfer Tax)** — already funding the village's ongoing forestry programme; applies to native forest restoration operations and sugi plantation conversion to native broadleaf species.
- **御杖村 地域脱炭素移行・再エネ推進交付金 (Regional Decarbonization Transition & RE Promotion Grant, via village)** — Mitsue Village completed the MoE's planning-support grant (step 1 of the national funding ladder) by publishing its RE plan in January 2025. This makes the village eligible for the 交付金 (step 2): a **2/3 subsidy on eligible solar/battery/EV/private-wire capex, rising to 3/4** for batteries and private wire (自営線) because Mitsue qualifies as both a 過疎 area and a low-financial-capacity municipality. The grant is paid **to the village** and explicitly funds building the operating structure for regional RE projects through **official public-private partnership (官民連携)**. The project is positioned as that operating partner: the village brings the plan and the grant channel; we bring the operator, the capital stack, and the anchor offtaker. This is the concrete, named path to closing part of the existing ¥28M–¥53M funding gap during Phases 2–3. The village's RE plan (policy basis), the project's scope (solar + battery + EV + private wire), and the 官民連携 structure all align with this grant's requirements. See `mitsue_village_re_plan_alignment.md` for the full funding ladder analysis. Baseline Rev 2 (due M9, Dec 2026) should fold in any confirmed 交付金 amount.

  *Note: Phase 1 deliverable — coordinate with the village on its multi-year 交付金 事業計画; position the project as the 官民連携 operating partner.*

**Recommendation:** Hire a **行政書士 (administrative scrivener)** experienced in grant applications. Cost: ¥200,000–500,000 per application. Worth every yen — Japanese government grant applications are notoriously demanding.

#### Layer 3 — Foundation & Philanthropy
- **The Nippon Foundation (日本財団)** — Asia's leading grantmaker for social challenges
- **Japan Fund for Global Environment (地球環境基金)** — environmental conservation grants
- **Japan Foundation Global Partnerships grants** — rural revitalization, AI, green tech
- **Toyota Foundation** — community and rural projects
- **International foundations**: MacArthur, Rockefeller (stretch — international philanthropy alignment)

#### Layer 4 — Corporate Partnerships
- **Dutch corporates in Japan**: Philips, ASML, Heineken, Royal HaskoningDHV (water expertise), Arcadis
- **Japanese tech corporates**: SoftBank, NTT (data center / connectivity), Hitachi
- **Forestry-related**: Sumitomo Forestry, Mitsui Bussan
- **Approach**: Position as CSR / sustainability investment, not pure donation

#### Layer 5 — Revenue (Phase 3+)
- Data center hosting fees
- Electricity sales (if FIT/FIP-registered) — biomass CHP and solar surplus
- EV charging fees
- Carbon credits (J-Credit certification)
- Forestry products (timber, lumber, biomass fuel from thinnings)
- Educational tourism / consulting (sharing the playbook)

### Realistic Funding Scenario for First 3 Years

| Source | Year 1 | Year 2 | Year 3 |
|--------|--------|--------|--------|
| Founder/private | ¥3M | ¥2M | ¥1M |
| Government grants | ¥5M | ¥30M | ¥80M |
| Foundations | ¥3M | ¥10M | ¥20M |
| Corporate partnerships | ¥0 | ¥5M | ¥30M |
| Revenue | ¥0 | ¥0 | ¥3M |
| **Total** | **¥11M** | **¥47M** | **¥134M** |

These are illustrative targets, not commitments. Real numbers will depend heavily on which grants are won.

---

## Return on Investment — Quantitative and Qualitative

> A standalone revenue & payback summary is in [`mitsue_revenue_model.md`](mitsue_revenue_model.md).

A successful 25-year project must demonstrate clear value to multiple stakeholders. This section presents both the **qualitative benefits** (immediately demonstrable) and the **quantitative ROI framework** (with illustrative ranges; precise figures will come from Phase 1 feasibility studies).

### Qualitative Returns — Available from Day One

These are the benefits that funders, the village, and partners can be told about now:

**For Mitsue Village and Residents**
- New local employment in forestry, facility operations, EV charging, and administration (estimated 8–15 direct jobs by Year 5)
- Income stream for private mountain owners through fair sugi harvesting compensation
- Improved local resilience through distributed energy generation
- EV charging infrastructure preparing the village for the coming transition
- Preserved use of the former Sugano Elementary School (Mitsue Taiken Koryukan) as a community-anchored facility
- Long-term reduction in cedar pollen affecting public health
- Visible signal that Mitsue is investing in its future — supporting in-migration and reducing depopulation pressure

**For the Region (Nara Prefecture, rural Japan more broadly)**
- A documented, replicable model for rural revitalization
- Demonstration of distributed energy generation suitable for other depopulating villages
- Strengthened regional fiber and digital infrastructure
- Concrete progress against multiple SDGs simultaneously

**For Funders and Partners**
- Open data and open methodology — measurable, transparent outcomes
- Strong storytelling value (Dutch-Japanese, rural-tech, community-driven)
- Alignment with Digital Garden City Nation initiative and 地方創生 priorities
- Credible advisory bench (Ray Ozzie)

### Quantitative Returns — Framework and Illustrative Ranges

The quantitative case rests on five revenue and savings categories. **The ranges below are illustrative early-stage estimates**; Phase 1 feasibility studies will replace these with vetted figures.

| Revenue / Savings Category | Year 1 | Year 5 | Year 10 | Notes |
|----------------------------|--------|--------|---------|-------|
| Data center hosting fees | ¥0 | ¥15–30M | ¥40–80M | Edge computing / AI specialist workloads |
| Electricity sales (FIT/FIP) | ¥0 | ¥5–15M | ¥10–30M | Surplus from biomass CHP and solar generation |
| EV charging fees | ¥0 | ¥1–3M | ¥3–8M | Growing as EV fleet expands |
| Carbon credits (J-Credit) | ¥0 | ¥1–3M | ¥3–10M | From forest restoration |
| Forestry products (timber, lumber) | ¥0 | ¥3–8M | ¥10–20M | Beyond fuel-residue use |
| Education / consulting | ¥0 | ¥1–3M | ¥3–8M | "Playbook" sharing |
| **Total annual revenue (illustrative)** | **¥0** | **¥28–67M** | **¥74–166M** | |

### Cost Displacement (Comparison Baseline)

To frame the ROI, it helps to articulate what the project *replaces* or *avoids*:

- **Energy import to the village**: Mitsue residents and businesses currently import essentially 100% of their electricity. Local generation displaces approximately ¥40–60M per year of energy imports leaving the village economy.
- **Former Sugano school maintenance burden**: The Koryukan costs the village an estimated ¥3–8M per year in basic upkeep with no return. Active use generates value from a previously stranded asset.
- **Forest management deficit**: Untended sugi plantations are a liability — both ecologically (pollen, biodiversity loss) and physically (landslide risk, fire risk). Active forestry management converts this liability into an asset.
- **Rural broadband gap**: Without intervention, Mitsue's connectivity will continue to lag urban Japan. The project's fiber upgrade benefits all village users, not only the data center.

### Payback Framework

Based on the illustrative figures above and the phase budgets earlier in this plan, a rough payback model looks like:

- **Total capital deployed by Year 5**: ¥200–290M (Phases 1–3)
- **Annual revenue by Year 5**: ¥28–67M
- **Operating costs by Year 5**: ¥18–35M (estimated 60% of revenue)
- **Net annual surplus by Year 5**: ¥10–32M
- **Approximate payback period**: 10–18 years for capital recovery, depending on funding mix (grants vs. loans vs. revenue-financed)

**Important honest caveat**: These figures assume successful execution of all three project elements at their target scale. Phase 1 feasibility studies will sharpen these numbers significantly, and real-world performance will determine actual ROI. The numbers above should be read as a *framework* for evaluation, not a forecast.

### How This ROI Story Should Be Used

- **For village government**: Lead with qualitative resident benefits, then show the cost-displacement framing (energy imports leaving the village; the Koryukan as stranded asset).
- **For private funders / corporate partners**: Lead with the revenue table and payback period, supported by qualitative storytelling.
- **For government grant applications**: Lead with SDG alignment and rural revitalization metrics (jobs created, depopulation impact, replicability), supported by the quantitative framework.
Different audiences need different orderings of the same underlying story. The discipline is to always have both available.

---

## Legal & Regulatory Checklist

### Entity & Tax
- [ ] 一般社団法人 incorporation
- [ ] Tax registration (法人税, 消費税)
- [ ] Bank account opening
- [ ] Accounting system (consider 弥生会計 or equivalent)
- [ ] Annual financial reporting

### Project-Specific Permits
- [ ] **Forestry permits** — 伐採届出 (cutting notification) under Forest Act
- [ ] **Land use changes** — coordination with 農業委員会 if any agricultural land involved
- [ ] **Building conversion permits** — Building Standards Act (建築基準法)
- [ ] **Fire and safety** — EV charging infrastructure requires 消防 and 電気設備 approvals
- [ ] **Electrical equipment** — 電気事業法 compliance for power generation
- [ ] **FIT/FIP registration** — METI process for grid feed-in
- [ ] **Environmental impact** — depending on scale, may require 環境アセスメント
- [ ] **Data center compliance** — APPI (privacy), cybersecurity standards

### Recommended Professional Support
- **行政書士 (administrative scrivener)** — for permits, NPO setup, grant applications. Local Nara-based ideal.
- **公認会計士 / 税理士 (accountant / tax advisor)** — for financial setup and reporting
- **弁護士 (lawyer)** — for landowner contracts, partnership agreements (consult, don't retain full-time yet)
- **Patent attorney** — only if novel technology IP needs protection

---

## Risk Management

### Top Risks and Mitigations

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Local community resistance | Medium | High | Phase 0 trust-building before any announcements |
| Forestry economics worse than expected | High | High | Independent feasibility study early; sugi thinnings feed the biomass energy system as fuel, adding value to the forestry programme |
| Funding gaps between phases | Medium | High | Diversified funding, never depend on one source; phase budgets conservatively; Layer-1 founding capital earmarked to cover the Phase 0–1 founder stipend so early runway does not depend on unpaid time |
| Founder dependency on Rob | Medium | High | Strong co-founders, documented processes, written succession/continuity plan; **funding the Rep. Director role removes the unpaid-time dependency** (see EVM §13); **trigger: no JP co-founder verbal commitment by end of Phase 0 → Gate 1 decision is held** pending recovery assessment |
| JP co-founder not secured | Medium | High | Active outreach; warm introductions via advisory board; Gate 1 hold trigger (see above) if unresolved by end of Phase 0 |
| Building unsuitable for data center | Low | High | Early structural assessment in Phase 1 |
| Fiber connectivity insufficient | Medium | Medium | Early NTT consultation; consider satellite/microwave backup |
| Regulatory delays | High | Medium | Start permits early; build buffer into timeline |
| Team conflict / mission drift | Medium | High | Clear charter, regular reviews, term limits |

---

## Immediate Next Steps (Next 30 Days)

1. **Identify and approach the Japanese co-founder** — most important single decision
2. **Schedule informal meeting** with Mitsue village mayor
3. **Reach out to 1–2 candidate 行政書士** in Nara for initial consultations
4. **Draft a 2-page charter** in Japanese and English
5. **Confirm advisory commitments** from Ray Ozzie in writing (even informal)
6. **Open a project Slack/Signal/email list** for the founding team

---

## Recommended Reading & Resources

- **Japan NPO Center** (jnpoc.ne.jp) — primary resource for NPO setup
- **林野庁 (Forestry Agency)** website — forestry subsidies and regulations
- **NEDO** — renewable energy grant programs
- **The Nippon Foundation** — major funder for social initiatives
- **METI** — EV charging infrastructure and FIT/FIP regulations
- **Cabinet Office Regional Revitalization portal** (chisou.go.jp)

---

## Closing Note

This plan is intentionally conservative in pace and ambitious in vision. The biggest mistake similar projects make is moving too fast publicly before securing local social license, then collapsing under the weight of expectations they cannot meet.

The Mitsue-kun Project's strength is its 25-year horizon. There is no rush in year one — there is a long, careful build of trust, structure, and capability that will determine whether year 25 looks like success or failure.

**Slow is smooth. Smooth is fast.**

---

*Rob Oudendijk — YR-Design / Safecast*
*Mitsue, Nara Prefecture, Japan*
*April 2026*
