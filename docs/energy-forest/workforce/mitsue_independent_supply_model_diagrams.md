<!-- Version: v1.0 | Last modified: 2026-10-28 -->

# Independent Supply Model — Landowners → Local Harvesters → Biomass/AI Data Center

Model: our own aggregator entity connects landowners to local harvesters and to the
biomass/CHP + data center, **without depending on the Village co-op**. The co-op stays
welcome as one supplier among others, never a required channel.

**Solid arrow = how it works in principle. Dashed arrow = optional / to verify.**
Legal points are general Japanese forestry practice, NOT yet verified for Nara. See the
checklist at the end.

## 1. Structure and contracts

```mermaid
flowchart LR
    own["Private landowners<br/>over 90% of ~7,051 ha"]
    agg["Aggregator<br/>NPO or 一般社団法人<br/>pools owners, signs contracts,<br/>schedules harvest"]
    harv["Local harvesters<br/>自伐型 crews, ex-協力隊,<br/>independent contractors"]
    opco["Operating company<br/>biomass/CHP plant<br/>buys fuel wood"]
    dc["AI data center<br/>takes power and heat"]
    vh["Village hall 産業建設課<br/>receives 伐採届<br/>possible 森林経営管理制度 partner"]
    coop["Village co-op<br/>optional supplier or partner"]
    pref["Prefecture<br/>subsidy / 林業経営体 / registration"]

    own -->|"施業委託 or 立木売買 contract"| agg
    agg -->|"work order + price"| harv
    harv -->|"chips / logs"| opco
    opco -->|"electricity + heat"| dc
    own -->|"伐採届 filed by owner or harvester"| vh
    agg -.->|"consult, keep relationship"| vh
    coop -.->|"supplies wood, equipment, crew"| agg
    agg -.->|"plan approval, subsidy"| pref

    classDef known fill:#2f6f4f,stroke:#1a4530,stroke-width:1.4px,color:#ffffff
    classDef unknown fill:#4a4a4a,stroke:#999999,stroke-width:1.4px,color:#ffffff,stroke-dasharray:5 4
    classDef future fill:#3a4f7a,stroke:#22315c,stroke-width:1.4px,color:#ffffff,stroke-dasharray:5 4
    class own,agg,harv,opco,dc known
    class vh,pref unknown
    class coop future
```

## 2. Wood and money flow for one harvest

```mermaid
sequenceDiagram
    autonumber
    participant O as Landowner
    participant A as Aggregator
    participant V as Village hall
    participant H as Harvester
    participant P as Biomass/CHP company

    O->>A: Sign contract (施業委託 or 立木売買)
    A->>V: Confirm 伐採届 is filed
    A->>H: Work order (parcel, volume, price)
    H->>H: Fell, process, chip or buck
    H->>P: Deliver fuel wood
    P->>A: Pay fuel price
    A->>H: Pay for the work
    A->>O: Pay owner share or land fee
    Note over A: Keeps a small margin for admin<br/>and scheduling
    P-->>A: Volume and quality report
```

## 3. Three ways to be allowed to handle subsidies (to verify)

```mermaid
flowchart TD
    q{"Do owners want<br/>thinning subsidies?"}
    q -->|"No, sell wood only"| r0["Route 0: direct sale<br/>just 伐採届, no subsidy<br/>simplest, start here"]
    q -->|"Yes"| r1["Route 1: aggregator becomes<br/>a 林業経営体 and writes<br/>its own 森林経営計画"]
    q -->|"Yes, unmanaged forest"| r2["Route 2: village entrusts forest<br/>under 森林経営管理制度;<br/>needs prefecture list<br/>意欲と能力のある林業経営者"]
    q -->|"Yes, simplest paperwork"| r3["Route 3: co-op writes the plan,<br/>wood still goes through us<br/>cooperation, not bypass"]

    r0 --> go["Wood flows to the biomass plant"]
    r1 --> go
    r2 --> go
    r3 --> go

    classDef known fill:#2f6f4f,stroke:#1a4530,stroke-width:1.4px,color:#ffffff
    classDef unknown fill:#4a4a4a,stroke:#999999,stroke-width:1.4px,color:#ffffff,stroke-dasharray:5 4
    classDef future fill:#3a4f7a,stroke:#22315c,stroke-width:1.4px,color:#ffffff,stroke-dasharray:5 4
    class r0,go known
    class r1,r2 unknown
    class r3 future
```

## 4. Risks of going around the co-op

```mermaid
flowchart LR
    risk["Risks"]
    risk --> a["Village politics<br/>village funds the co-op<br/>運営補助金"]
    risk --> b["Equipment gap<br/>chipper and site<br/>at 牛峠工場 belong to co-op"]
    risk --> c["Subsidy paperwork<br/>owners may still prefer<br/>the co-op's plan"]
    risk --> d["Registration<br/>素材生産業者 rules<br/>vary by prefecture"]

    a --> a2["Keep co-op as optional supplier,<br/>brief mayor and village hall early"]
    b --> b2["Rent or buy a chipper;<br/>or buy chips from co-op"]
    c --> c2["Offer Route 3 to owners<br/>who want it"]
    d --> d2["Check Nara requirements"]

    classDef unknown fill:#4a4a4a,stroke:#999999,stroke-width:1.4px,color:#ffffff,stroke-dasharray:5 4
    classDef known fill:#2f6f4f,stroke:#1a4530,stroke-width:1.4px,color:#ffffff
    class risk,a,b,c,d unknown
    class a2,b2,c2,d2 known
```

## To verify before relying on this

1. Does Nara require 素材生産業者 registration for commercial harvesting?
2. Can an NPO/一般社団法人 qualify as a 林業経営体 and submit a 森林経営計画? Minimum area?
3. How does Mitsue pick operators for 森林経営管理制度, and who is on the prefecture list?
4. Does the village require owners to use the co-op for any village-funded thinning?
5. Co-op member count and area covered (open Q1 in `meetings/village_coop_2026-10-02_prep_questions.md`).
6. Who can chip and dry fuel wood without the 牛峠 site, and at what cost per tonne?
