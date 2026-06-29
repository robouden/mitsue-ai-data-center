# Forest Twin — model interaction diagram

How the variables flow through the simulator, one year at a time. Inputs (green)
→ the three loops (forest / energy+carbon / money) → outputs (blue). The CHP is
**auto-sized** from the fuel flow, so capex/O&M feed back into the economics.

```mermaid
flowchart TD
    %% ---------- INPUTS ----------
    subgraph IN["📥 Inputs (data + CONFIG)"]
        SP["species.csv<br/>growth curve, wood density,<br/>carbon fraction, heat value, log price"]
        ST["stands.csv<br/>area, age, species"]
        CF["CONFIG<br/>regime, rotation_age,<br/>alloc split, efficiencies,<br/>prices, costs, capacity factor"]
    end

    %% ---------- FOREST LOOP ----------
    subgraph FOREST["🌲 1. Forest growth (per stand, per year)"]
        GROW["age += 1<br/>volume_per_ha(age) = logistic curve"]
        STOCK["standing volume &amp; biomass<br/>above + below ground"]
        HARV{"Harvest regime?"}
        CONV["convert: clearfell X%/yr<br/>→ replant broadleaf (one-way)"]
        ROT["rotation: harvest area / rotation_age<br/>→ replant sugi (sustained)"]
        MIX["mixed: split replant<br/>broadleaf + sugi"]
        HV["harvest_vol (m³)<br/>+ replant_area (ha)"]
    end

    %% ---------- ALLOCATION ----------
    subgraph ALLOC["🪵 2. Wood allocation"]
        AL["split harvest_vol"]
        SAW["sawlog 40%"]
        CHPV["CHP fuel 40%"]
        BIO["biochar 10%"]
        LOSS["loss 10%"]
    end

    %% ---------- ENERGY ----------
    subgraph ENERGY["⚡ 3a. CHP energy"]
        FUEL["dry tonnes → fuel energy<br/>(moisture penalty)"]
        ELEC["electricity = energy × elec_eff<br/>(0.13, Mishima-calibrated)"]
        HEAT["heat = energy × heat_eff"]
        SIZE["CHP sizing:<br/>nameplate kWe = peak elec /<br/>(capacity_factor × 8760)<br/>→ capex + O&amp;M"]
    end

    %% ---------- CARBON ----------
    subgraph CARBON["🌍 3b. Carbon accounting"]
        STANDC["standing forest carbon"]
        PRODC["product carbon<br/>sawlog 80 yr, biochar 500 yr"]
        AVOID["avoided CO₂<br/>grid elec + fossil heat displaced"]
    end

    %% ---------- ECONOMICS ----------
    subgraph MONEY["💴 4. Economics"]
        REV["revenue =<br/>logs + electricity + heat<br/>+ biochar + carbon credits"]
        COST["costs =<br/>felling + transport(distance)<br/>+ chipping + drying + roads<br/>+ planting + CHP capex/O&amp;M"]
        PROFIT["profit = revenue − costs"]
    end

    %% ---------- OUTPUTS ----------
    subgraph OUT["📤 Outputs (per year + 50-yr totals)"]
        R1["standing C, product C"]
        R2["electricity MWh, heat GJ, CHP kWe"]
        R3["avoided CO₂"]
        R4["profit, break-even forest area"]
    end

    %% ---------- EDGES ----------
    SP --> GROW
    ST --> GROW
    CF --> HARV
    GROW --> STOCK --> HARV
    HARV --> CONV & ROT & MIX
    CONV & ROT & MIX --> HV
    HV -. replant .-> GROW

    HV --> AL --> SAW & CHPV & BIO & LOSS

    CHPV --> FUEL --> ELEC & HEAT
    ELEC --> SIZE
    SAW --> PRODC
    BIO --> PRODC
    STOCK --> STANDC
    ELEC --> AVOID
    HEAT --> AVOID

    SAW --> REV
    ELEC --> REV
    HEAT --> REV
    BIO --> REV
    AVOID --> REV
    HV --> COST
    CHPV --> COST
    SIZE -- "capex + O&amp;M (feedback)" --> COST
    REV --> PROFIT
    COST --> PROFIT

    STANDC --> R1
    PRODC --> R1
    ELEC --> R2
    HEAT --> R2
    SIZE --> R2
    AVOID --> R3
    PROFIT --> R4

    %% ---------- STYLING ----------
    classDef in fill:#d7f0d7,stroke:#3a7a3a,color:#163;
    classDef out fill:#d7e6ff,stroke:#2a5aa8,color:#134;
    classDef dec fill:#fff3cd,stroke:#a8842a,color:#530;
    class SP,ST,CF in;
    class R1,R2,R3,R4 out;
    class HARV dec;
```

## The one-line story

`species + stands + CONFIG` → grow the forest → harvest it (the **regime**
decides if fuel is sustainable) → split the wood → burn some for **power + heat**
and lock the rest as **stored carbon** → tally **avoided CO₂** → subtract real
supply-chain **costs** (sized to a right-fit CHP) → **profit** and the
**forest-area needed** for a given CHP size.

The single most important link is the dotted **replant → grow** arrow: in
*rotation* mode it closes the loop (perpetual fuel); in *convert* mode it doesn't
(broadleaf is never re-harvested → fuel runs out).
