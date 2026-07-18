<!-- Version: v1.1 | Last modified: 2026-07-19 -->

<style>
  #write > h1 { font-size: 2.6em !important; }
  #write > h2 { font-size: 2em !important; }
  #write > p, #write > ul, #write > ol { font-size: 1.7em !important; line-height: 1.5 !important; }
</style>

# フォレストツイン — モデル相互作用図

シミュレーターの中で変数がどのように年次で流れるかを示す。入力（青）→ 3つのループ（森林／エネルギー・炭素／お金、ピンク）
→ 出力（緑）。CHPは燃料フローに応じて**自動サイジング**されるため、初期投資・運営維持費が経済性にフィードバックされる。

```mermaid
%%{init: {
  "theme": "base",
  "flowchart": { "defaultRenderer": "elk", "htmlLabels": true, "curve": "basis", "nodeSpacing": 40, "rankSpacing": 60 },
  "themeVariables": {
    "fontFamily": "'Hiragino Sans', 'Noto Sans JP', 'Helvetica Neue', Arial, sans-serif",
    "fontSize": "14px",
    "primaryColor": "#ffffff",
    "primaryBorderColor": "#8aa0c8",
    "primaryTextColor": "#1f2937",
    "lineColor": "#9aa5b1",
    "clusterBkg": "#fbfbfd",
    "clusterBorder": "#e2e5ea",
    "edgeLabelBackground": "#fbfbfd"
  }
} }%%
flowchart TD
    %% ---------- INPUTS ----------
    subgraph IN["📥 入力（データ + CONFIG）"]
        SP("species.csv<br/>成長曲線、木材密度、<br/>炭素分率、発熱量、丸太価格")
        ST("stands.csv<br/>面積、林齢、樹種")
        CF("CONFIG<br/>施業方式、伐期齢、<br/>配分比率、効率、<br/>価格、コスト、設備利用率")
    end

    %% ---------- FOREST LOOP ----------
    subgraph FOREST["🌲 1. 森林成長（林分ごと・年次）"]
        GROW("林齢 += 1<br/>ha当たり材積(林齢) = ロジスティック曲線")
        STOCK("立木材積・バイオマス<br/>（地上部+地下部）")
        HARV{"伐採方式は？"}
        CONV("転換：皆伐 X%/年<br/>→ 広葉樹に植替え（不可逆）")
        ROT("輪伐：伐採面積 / 伐期齢<br/>→ スギ再植林（持続可能）")
        MIX("混合：広葉樹とスギに<br/>分けて再植林")
        HV("伐採材積 (m³)<br/>+ 再植林面積 (ha)")
    end

    %% ---------- ALLOCATION ----------
    subgraph ALLOC["🪵 2. 木材配分"]
        AL("伐採材積を配分")
        SAW("製材用丸太 40%")
        CHPV("CHP燃料 40%")
        BIO("バイオ炭 10%")
        LOSS("損失 10%")
    end

    %% ---------- ENERGY ----------
    subgraph ENERGY["⚡ 3a. CHPエネルギー"]
        FUEL("乾燥重量(トン) → 燃料エネルギー<br/>（含水率補正）")
        ELEC("電力 = エネルギー × 発電効率<br/>（0.13、三島町で校正）")
        HEAT("熱 = エネルギー × 熱効率")
        SIZE("CHP規模設定：<br/>定格出力kWe = 最大電力 /<br/>（設備利用率 × 8760）<br/>→ 初期投資 + 運営維持費")
    end

    %% ---------- CARBON ----------
    subgraph CARBON["🌍 3b. 炭素勘定"]
        STANDC("森林蓄積炭素")
        PRODC("木材製品炭素<br/>（製材80年、バイオ炭500年）")
        AVOID("削減CO₂<br/>（系統電力+化石燃料熱の代替）")
    end

    %% ---------- ECONOMICS ----------
    subgraph MONEY["💴 4. 経済性"]
        REV("収益 =<br/>丸太 + 電力 + 熱<br/>+ バイオ炭 + カーボンクレジット")
        COST("コスト =<br/>伐採 + 運搬(距離)<br/>+ チップ化 + 乾燥 + 林道<br/>+ 植林 + CHP初期投資/運営維持費")
        PROFIT("利益 = 収益 − コスト")
    end

    %% ---------- OUTPUTS ----------
    subgraph OUT["📤 出力（年次 + 50年累計）"]
        R1("蓄積炭素、製品炭素")
        R2("電力量MWh、熱量GJ、CHP出力kWe")
        R3("削減CO₂")
        R4("利益、損益分岐森林面積")
    end

    %% ---------- EDGES ----------
    SP --> GROW
    ST --> GROW
    CF --> HARV
    GROW --> STOCK --> HARV
    HARV --> CONV & ROT & MIX
    CONV & ROT & MIX --> HV
    HV -. 再植林 .-> GROW

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
    SIZE -- "初期投資+運営維持費（フィードバック）" --> COST
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
    classDef in fill:#eaf3ff,stroke:#5b8def,stroke-width:1.5px,color:#1e3a5f,rx:10,ry:10;
    classDef out fill:#eafaf0,stroke:#3aa76d,stroke-width:1.5px,color:#134d2e,rx:10,ry:10;
    classDef dec fill:#fff3e0,stroke:#e0972a,stroke-width:1.5px,color:#5c3a09,rx:10,ry:10;
    classDef proc fill:#ffffff,stroke:#b9c2d0,stroke-width:1.3px,color:#1f2937,rx:10,ry:10;
    classDef money fill:#fdeef5,stroke:#d1608f,stroke-width:1.5px,color:#5c1c38,rx:10,ry:10;

    class SP,ST,CF in;
    class R1,R2,R3,R4 out;
    class HARV dec;
    class REV,COST,PROFIT money;
    class GROW,STOCK,CONV,ROT,MIX,HV,AL,SAW,CHPV,BIO,LOSS,FUEL,ELEC,HEAT,SIZE,STANDC,PRODC,AVOID proc;

    style IN fill:#fbfbfd,stroke:#e2e5ea,color:#374151
    style FOREST fill:#fbfbfd,stroke:#e2e5ea,color:#374151
    style ALLOC fill:#fbfbfd,stroke:#e2e5ea,color:#374151
    style ENERGY fill:#fbfbfd,stroke:#e2e5ea,color:#374151
    style CARBON fill:#fbfbfd,stroke:#e2e5ea,color:#374151
    style MONEY fill:#fbfbfd,stroke:#e2e5ea,color:#374151
    style OUT fill:#fbfbfd,stroke:#e2e5ea,color:#374151
```

## 一行でいうと

`species + stands + CONFIG` → 森林を成長させる → 伐採する（**施業方式**が燃料の持続可能性を左右する）→ 木材を配分する →
一部を燃焼して**電力+熱**にし、残りを**貯蔵炭素**として固定する → **削減CO₂**を集計する → 実際のサプライチェーン**コスト**
（最適サイズのCHPに合わせた）を差し引く → **利益**と、所定のCHP規模に必要な**森林面積**を求める。

最も重要なリンクは点線の**再植林 → 成長**の矢印である：*輪伐*モードではループが閉じ（燃料は永続的）、*転換*モードでは
閉じない（広葉樹は再伐採されないため、燃料はいずれ枯渇する）。
