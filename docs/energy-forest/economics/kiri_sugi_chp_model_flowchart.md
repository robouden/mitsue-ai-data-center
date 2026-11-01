the <p align="right">Version: v1.1 | Last modified: 2026-10-31</p>

# How the Financial Model Fits Together

Maps the sheets in the Excel model [kiri_sugi_chp_financial_model_2026-10-31.xlsx](kiri_sugi_chp_financial_model_2026-10-31.xlsx) (full path: /home/rob/Documents/Mitsue/Mitsue Village Project AI data center/docs/energy-forest/economics/kiri_sugi_chp_financial_model_2026-10-31.xlsx). Change its blue input cells to test other fuel prices, subsidies or yields. A3 PDFs: [EN](kiri_sugi_chp_model_flowchart_a3_en.pdf), [JP](kiri_sugi_chp_model_flowchart_a3_jp.pdf). Blue = inputs, green = results, red = the decisive lever. All costs are placeholders. Split into three charts so lines stay short and uncrossed.

## 1. Overview: what feeds what

```mermaid
%%{init: {'flowchart': {'curve': 'basis', 'nodeSpacing': 70, 'rankSpacing': 110, 'padding': 20}, 'themeVariables': {'fontSize': '16px'}}}%%
flowchart LR
    IN["<b>Inputs</b><br/>hours, efficiency,<br/>electricity price,<br/>subsidy, loan rate"]
    FP["<b>Fuel price</b><br/>¥/t fresh"]
    PLANT["<b>Plant50 / Plant12</b><br/>fuel need, revenue,<br/>opex, capex"]
    KIRI["<b>Kiri per hectare</b><br/>yield, planting cost"]
    CO2["<b>CO2 credits</b><br/>uptake, displaced grid power"]
    OUT1["<b>EBITDA, payback,<br/>break-even price</b>"]
    OUT2["<b>Kiri net ¥/ha,<br/>break-even fuel price</b>"]
    OUT3["<b>Credit value ¥M/yr</b>"]

    IN --> PLANT
    FP --> PLANT
    FP --> KIRI
    IN --> CO2
    KIRI --> CO2
    PLANT --> CO2
    PLANT --> OUT1
    KIRI --> OUT2
    CO2 --> OUT3

    classDef inp fill:#1f4e79,stroke:#0b2a47,color:#ffffff
    classDef calc fill:#37474f,stroke:#1c2a30,color:#ffffff
    classDef res fill:#1b5e20,stroke:#0d3b11,color:#ffffff
    classDef key fill:#b71c1c,stroke:#7f0000,color:#ffffff
    class IN inp
    class FP key
    class PLANT,KIRI,CO2 calc
    class OUT1,OUT2,OUT3 res
```

## 2. Plant sheets (Plant50 and Plant12)

```mermaid
%%{init: {'flowchart': {'curve': 'basis', 'nodeSpacing': 60, 'rankSpacing': 100, 'padding': 20}, 'themeVariables': {'fontSize': '16px'}}}%%
flowchart LR
    A["Rated kW<br/>x hours"] --> B["Electricity<br/>MWh/yr"]
    B --> C["Dry fuel t/yr<br/>(efficiency, LHV)"]
    C --> D["Fresh fuel t/yr<br/>(x2 at 50% moisture)"]
    D --> E["Fuel cost"]
    P["Fuel price<br/>¥/t fresh"] --> E
    B --> F["Revenue<br/>MWh x price"]
    X["Heat + compute<br/>(50 kWe only)"] --> F
    E --> G["Total opex<br/>+ O&M, staff, rent"]
    F --> H["EBITDA"]
    G --> H
    H --> I["Payback years"]
    J["Capex<br/>- subsidy"] --> K["Net capex"]
    K --> I
    K --> L["Capital charge<br/>per year"]
    H --> M["Result after<br/>capital"]
    L --> M

    classDef inp fill:#1f4e79,stroke:#0b2a47,color:#ffffff
    classDef calc fill:#37474f,stroke:#1c2a30,color:#ffffff
    classDef res fill:#1b5e20,stroke:#0d3b11,color:#ffffff
    classDef key fill:#b71c1c,stroke:#7f0000,color:#ffffff
    class A,X,J inp
    class P,E key
    class H,I,M res
    class B,C,D,F,G,K,L calc
```

## 3. Kiri per hectare and CO2

```mermaid
%%{init: {'flowchart': {'curve': 'basis', 'nodeSpacing': 60, 'rankSpacing': 100, 'padding': 20}, 'themeVariables': {'fontSize': '16px'}}}%%
flowchart LR
    Y["Kiri yield 4.9 t/ha/yr<br/>x 5-year rotation"] --> F["Fresh t<br/>per harvest"]
    F --> R["Fuel revenue<br/>per harvest"]
    P["Fuel price<br/>¥/t fresh"] --> R
    C["Planting, fence,<br/>upkeep per cycle"] --> N["Net ¥/ha"]
    R --> N
    F --> BE["Break-even<br/>fuel price"]
    C --> BE

    Y --> U["Kiri uptake<br/>t-CO2/ha/yr"]
    U --> S["Average stock:<br/>one-off credit only"]
    PC["J-Credit price<br/>¥5,600/t"] --> S
    M["Plant MWh/yr<br/>x grid factor 0.45"] --> D["Grid CO2<br/>displaced"]
    D --> V["Credit value ¥M/yr<br/>(self-consumed only,<br/>not with FIT)"]
    PC --> V

    classDef inp fill:#1f4e79,stroke:#0b2a47,color:#ffffff
    classDef calc fill:#37474f,stroke:#1c2a30,color:#ffffff
    classDef res fill:#1b5e20,stroke:#0d3b11,color:#ffffff
    classDef key fill:#b71c1c,stroke:#7f0000,color:#ffffff
    class Y,C,PC,M inp
    class P key
    class F,R,U,S,D calc
    class N,BE,V res
```

## Reading it
- **Fuel price is the red lever.** It sets fuel cost (the largest opex line), so it drives EBITDA, payback and break-even price, and it also sets kiri's value per hectare.
- **Hours and efficiency** set MWh, which sets fuel need, O&M and CO2 displaced.
- **Subsidy and loan rate** only touch the capital side.
- **CO2 credits** sit outside the EBITDA chain: they count only if the power is self-consumed, and kiri stock credits are one-off.
