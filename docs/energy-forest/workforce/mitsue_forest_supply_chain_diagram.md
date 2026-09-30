<!-- Version: v1.7 | Last modified: 2026-09-30 -->

# Mitsue Forest Supply Chain — What We Currently Have

Same shape as Rob's reference sketch, filled in with what's actually confirmed vs.
still unknown. **Solid arrow = sourced fact. Dashed arrow = unconfirmed / proposed /
future.** Downstream half (CHP → compute) is in
`../chp-technical/mitsue_forest_power_compute_loop.html` — this diagram is the
upstream half feeding it.

```mermaid
flowchart TD
    own1["Private landowners<br/>over 90% of ~7,051 ha"]
    own2["Common-use 財産区・入会 ?<br/>no Mitsue record - only Tenkawa's<br/>洞川財産区 found"]
    own3["Village-owned 村有林 ?<br/>asked Mitsue Kanko 2026-08-05,<br/>still unanswered"]

    forest["Mitsue forest ~7,051 ha<br/>sugi/hinoki, postwar plantation"]

    own1 --> forest
    own2 -.-> forest
    own3 -.-> forest

    coopcrew["森林組合 field crew<br/>2 people, avg age ~33"]
    yamaguchi["Independent harvester<br/>confirmed active - 自伐型林業,<br/>協力隊 forestry division,<br/>ad hoc, owner-commissioned;<br/>outside the coop, sells to Misugi<br/>market; not a fuel supplier"]
    otherindep["Other independent harvesters<br/>10+ (his estimate, unverified);<br/>good logs to Sakurai timber coop?"]
    corps["地域おこし協力隊 自伐型林業 trainees<br/>max 3-yr term - 0 hires<br/>last 2 years"]
    loan["Village machinery loan<br/>backhoe + dump truck,<br/>post-term, max 5 yr, 1,000 yen/day"]

    forest --> coopcrew
    forest --> yamaguchi
    forest -.-> otherindep
    forest -.-> corps
    corps -.-> loan
    loan -.-> yamaguchi

    leftover["Left in the forest<br/>~66 ha/yr thinned but only<br/>~120-300 m3/yr recovered"]
    coopcrew -->|thinning| leftover

    mill["牛峠工場<br/>coop chip/dry processing centre"]
    coopcrew -->|"~120-300 m3/yr"| mill
    otherindep -.-> mill
    yamaguchi -.-> mill
    otherindep -.-> mill
    yamaguchi -.-> mill

    niwa["丹羽製材 Niwa mill<br/>existing pulp-chip buyer -<br/>wrong spec for CHP fuel"]
    yamaguchi -.-> niwa
    coopcrew -.-> niwa

    mill --> gA["A材 sawlog ~22%"]
    mill --> gB["B材 plywood-grade ~54%<br/>contested"]
    mill --> gCD["C/D材 chip/fuel ~24%"]

    sawmkt["Sawlog market<br/>buyer unknown"]
    plymkt["Plywood/pulp buyer<br/>unknown"]
    onsen["姫石の湯 onsen<br/>already receives wood from the coop<br/>(grade and volume unverified)"]
    othersup["Other wood suppliers to the onsen ?<br/>one local view: coop cannot supply<br/>enough (not verified)"]
    chp["Future CHP fuel<br/>plant not yet built"]
    dc["AI data center, co-located<br/>pulls CHP electricity 24/7<br/>behind-the-meter, ~18 kW pilot<br/>= only ~2% of CHP output"]
    grid["Grid export via FIP<br/>Kansai T&D, market price + premium<br/>grid pre-consultation needed"]
    dry["CHP heat dries chips<br/>at 牛峠工場, feeds fuel loop"]
    compute["Compute revenue<br/>funds crew and equipment"]

    gA -.-> sawmkt
    gB -.-> plymkt
    gB -.-> chp
    gCD -.-> chp
    gA -.->|"wood, grade per Rob observation"| onsen
    gB -.->|"wood, grade per Rob observation"| onsen
    othersup -.-> onsen
    chp -.->|heat| dry
    chp -.->|"electricity, first call"| dc
    chp -.->|"electricity, remainder"| grid
    dc -.-> compute

    classDef known fill:#2f6f4f,stroke:#1a4530,stroke-width:1.4px,color:#ffffff
    classDef unknown fill:#4a4a4a,stroke:#999999,stroke-width:1.4px,color:#ffffff,stroke-dasharray:5 4
    classDef future fill:#3a4f7a,stroke:#22315c,stroke-width:1.4px,color:#ffffff,stroke-dasharray:5 4

    class own1,forest,coopcrew,yamaguchi,leftover,mill,gA,gB,gCD known
    class own2,own3,otherindep,corps,loan,sawmkt,plymkt,niwa,onsen,othersup unknown
    class chp,dc,grid,dry,compute future
```

## Open questions (this is the real answer to "what do we have")

1. **村有林** — any village-owned forest usable without private contracts? Asked
   Mitsue Kanko 2026-08-05, still unanswered.
2. **財産区/入会 (common-use land)** — no evidence any exists in Mitsue; only
   confirmed example is Tenkawa's 洞川財産区. Don't assume Mitsue has an
   equivalent.
3. **Where does the independent harvester's felled timber actually go?** — answered 2026-09-30:
   his own wood goes to Misugi market (西垣林業); others reportedly send good logs to
   桜井木材共同組合 members. Coop/other operators' flows still unverified.
4. **How many *other* independent harvesters work the Mitsue area?** — one is confirmed
   active; he estimates 10+ operators exist (unverified, may not all be active).
   Village hall inquiry (2026-09-30) pending.
5. **The "3-year / 6-year" contract structure** — only sourced term found is
   地域おこし協力隊's national 3-year cap, plus the village machinery-loan
   ordinance's separate 5-year post-term loan window. No "6-year" figure exists
   in any doc or memory — if you have a source for that number, it needs adding.
6. **Does the coop actually thin members' forest, or do owners deal with harvesters directly?** —
   the confirmed harvester bypassed the coop (owner deal + joint 伐採届). Ask 2026-10-02.
7. **Reforestation in Mitsue** — 神末 clear-cut replanted with cherry; 土屋原 large clear-cut
   reportedly to be replanted (species unknown). Who funded/did it? Ask 2026-10-02.
8. **B-grade destination** (plywood buyer vs. CHP-by-default) — open per
   `mitsue_forest_workforce_energy_plan.md` §4a, affects real CHP fuel volume.

## Not shown here (separate, sourced elsewhere)

- **Onsen (姫石の湯)**: already receives wood (not heat) from the coop today. Rob's observation
  of the coop's storage suggests A and B grade; grade and volume are not documented. One local view is that the coop cannot supply enough, so the onsen also gets wood from other places (unverified; suppliers unknown). CHP heat
  cannot be piped from 牛峠工場 to the onsen, so that link is not shown.
- **Scale check**: the data center is a small load (~18 kW, about 2% of a ~1.15 MWe plant).
  Its value is stable 24/7 baseload and a high-value use for the CHP's electrons, not volume.
  Most output goes to the grid via FIP. Source: `mitsue_forest_workforce_energy_plan.md` §5.
- **Permits/authorization**: 伐採届 (owner/buyer files, 90–30 days pre-felling),
  森林経営計画 (5-yr plan, owner or coop-filed, unlocks FIT premium),
  森林経営管理制度 consignment to village (legally available, owner-intent survey
  deliberately not run per Mayor 2020) — see `mitsue_forest_permit_subsidy_fit_reference.md`.
- **Money**: 森林環境譲与税 (¥26–38M/yr) → 施業放置林整備事業 (village-funded
  40% thinning, coop-contracted, ~2,600 ha backlog) and 美しい森づくり補助金
  (50% reimbursement, NPOs eligible) — see
  `../history/council_minutes_forestry_findings.md` §2.1–2.3 and
  `mitsue_forest_permit_subsidy_fit_reference.md`.
