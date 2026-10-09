<!-- Version: v1.8 | Last modified: 2026-10-09 -->

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

    vh["Village hall 産業建設課<br/>伐採届 = notification only, not a permit;<br/>picks operators for village-funded thinning<br/>and 村有林 (how: asked 2026-10-09)"]
    forest --> vh

    coopcrew["森林組合 field crew<br/>2 people, avg age ~33"]
    yamaguchi["Independent harvester<br/>confirmed active - 自伐型林業,<br/>協力隊 forestry division,<br/>ad hoc, owner-commissioned;<br/>sells to Misugi market;<br/>declines to be a fuel supplier"]
    tokuda["徳田林産 Tokuda Rinsan<br/>HQ 神末; 7 staff + 15 temp;<br/>buys land and timber, sells direct<br/>to mills and markets (Sakurai);<br/>Mie office 2018; no village tie found"]
    otherindep["Other independent harvesters<br/>10+ (his estimate, unverified)"]
    miesup["Mie-side operators (Misugi) ?<br/>unverified"]
    corps["地域おこし協力隊 自伐型林業 trainees<br/>max 3-yr term - 0 hires<br/>last 2 years"]
    loan["Village machinery loan<br/>backhoe + dump truck,<br/>post-term, max 5 yr, 1,000 yen/day"]

    forest --> coopcrew
    forest --> yamaguchi
    forest -.-> tokuda
    forest -.-> otherindep
    forest -.-> corps
    corps -.-> loan
    loan -.-> yamaguchi
    vh -->|"village-funded thinning"| coopcrew
    vh -.-> tokuda

    leftover["Left in the forest<br/>~66 ha/yr thinned but only<br/>~120-300 m3/yr recovered"]
    coopcrew -->|thinning| leftover

    mill["牛峠工場<br/>coop chip/dry processing centre"]
    coopcrew -->|"~120-300 m3/yr"| mill

    gate["PROPOSAL: open-gate fuel yard<br/>any operator delivers C/D wood<br/>to spec at a posted gate price;<br/>coop = processor and buyer"]
    otherindep -.-> gate
    tokuda -.-> gate
    miesup -.-> gate
    gate -.-> mill

    machine["PROPOSAL: shared harvester pool<br/>Komatsu 901XC or 931XC trial;<br/>owner open: village, NGO or coop;<br/>equal terms for all operators"]
    machine -.-> coopcrew
    machine -.-> otherindep
    vh -.-> machine

    misugi["Misugi log market 西垣林業<br/>buys his logs"]
    yamaguchi --> misugi
    tokuda -.-> sakurai["Sakurai timber market<br/>and large sawmills"]
    yamamoto["山本製材所 sawmill, 神末<br/>status and volume unknown"]
    forest -.-> yamamoto

    niwa["丹羽製材 Niwa mill<br/>existing pulp-chip buyer -<br/>wrong spec for CHP fuel"]
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

    class own1,forest,coopcrew,yamaguchi,tokuda,leftover,mill,gA,gB,gCD,misugi known
    class own2,own3,vh,otherindep,miesup,corps,loan,sawmkt,sakurai,yamamoto,plymkt,niwa,onsen,othersup unknown
    class chp,dc,grid,dry,compute,gate,machine future
```

## Open questions (this is the real answer to "what do we have")

1. **Village-owned forest (村有林)?** Asked 2026-08-05, no answer.
2. **Common-use land (財産区・入会)?** No Mitsue record; only Tenkawa confirmed.
3. **Where does wood go?** Yamaguchi to Misugi market; Tokuda to mills and Sakurai market (its own site); coop flows unverified.
4. **Who else is active?** 10+ independents (his estimate); 山本製材所 (神末) status unknown; Mie-side operators unverified.
5. **Does Tokuda cut inside Mitsue,** or mostly Mie and Sakurai? Asked Ohba-san 2026-10-09 (awaiting reply).
6. **How are operators chosen** for village-funded thinning and 村有林? Asked 2026-10-09.
7. **Owners:** any group or owner-intent survey results? Coop member count and forest area? Asked 2026-10-09.
8. **Coop finances:** no document seen; "coop in trouble" is a hypothesis only.
9. **Onsen wood:** which grades and volumes, and from whom besides the coop?
10. **B-grade destination** (plywood buyer or CHP fuel) sets real CHP fuel volume.
11. **Proposals to test with the coop:** open-gate yard, shared harvester and who owns it.

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
