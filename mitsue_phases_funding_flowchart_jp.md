<style>
  body { font-size: 9.5pt; line-height: 1.25; font-family: 'Noto Sans JP', 'Yu Gothic', 'Hiragino Sans', sans-serif; }
  h1 { font-size: 14pt; margin: 3pt 0 1pt; }
  h2 { font-size: 10pt; margin: 5pt 0 1pt; }
  h3 { font-size: 9.5pt; margin: 2pt 0; }
  p, li { margin: 1pt 0; }
  ul, ol { margin: 2pt 0; padding-left: 18pt; }
  blockquote { margin: 3pt 0; }
  hr { margin: 3pt 0; }
  .page-break { page-break-after: always; break-after: page; height: 0; margin: 0; padding: 0; }
  @media print { body { margin: 0; } }
</style>

<p align="right">バージョン: v2.0 (Baseline Rev 1) &nbsp;|&nbsp; 最終更新: 2026-05-18</p>

# 三津江プロジェクト — フェーズ・資金調達フローチャート



## 図1 — フェーズ構造と資金調達ゲート

```mermaid
%%{init: {'theme':'base','flowchart':{'htmlLabels':true},'themeVariables':{
  'background':'#404040',
  'primaryColor':'#6796e6','primaryTextColor':'#FFFFFF','primaryBorderColor':'#3655b5',
  'lineColor':'#A8A8A8','textColor':'#DEDEDE',
  'edgeLabelBackground':'#FCEB6C',
  'fontFamily':'Noto Sans JP, Yu Gothic, sans-serif'
}}}%%
flowchart LR
    P0["フェーズ0<br/>基礎準備<br/>M 1–3"]
    P1["フェーズ1<br/>基盤構築<br/>M 4–9"]
    P2["フェーズ2<br/>パイロット設計<br/>M 10–18"]
    P3["フェーズ3<br/>パイロット建設<br/>M 19–30"]
    P4["フェーズ4<br/>運用・拡大<br/>M 31+"]

    G1{"ゲート1<br/>¥3–8M"}
    G2{"ゲート2<br/>¥30–50M"}
    G3{"ゲート3<br/>¥120–290M"}
    G4{"ゲート4<br/>収益<br/>開始?"}

    H1["保留・再提案"]
    H2["保留・縮小"]
    H3["段階的建設"]

    P0 --> G1
    G1 -->|通過| P1
    P1 --> G2
    G2 -->|通過| P2
    P2 --> G3
    G3 -->|通過| P3
    P3 --> G4
    G4 -->|はい| P4

    G1 -->|資金不足| H1 -.-> G1
    G2 -->|資金不足| H2 -.-> G2
    G3 -->|資金不足| H3 -.-> G3
    G4 -->|一部開始| P3

    classDef phase fill:#6796e6,stroke:#3655b5,stroke-width:1px,color:#FFFFFF,font-weight:bold
    classDef gate  fill:#e58520,stroke:#A85C10,stroke-width:1px,color:#FFFFFF,font-weight:bold
    classDef hold  fill:#353535,stroke:#FCEB6C,stroke-width:1px,color:#DEDEDE,stroke-dasharray:4 3
    class P0,P1,P2,P3,P4 phase
    class G1,G2,G3,G4 gate
    class H1,H2,H3 hold

    linkStyle default stroke:#A8A8A8,stroke-width:1.4px,color:#000000
    linkStyle 1,3,5,7 stroke:#FCEB6C,stroke-width:2.5px,color:#000000
```

---

## 図2 — 各ゲートへの資金調達ソース

```mermaid
%%{init: {'theme':'base','themeVariables':{
  'background':'#404040',
  'primaryColor':'#6796e6','primaryTextColor':'#FFFFFF','primaryBorderColor':'#3655b5',
  'lineColor':'#A8A8A8','textColor':'#DEDEDE',
  'fontFamily':'Noto Sans JP, Yu Gothic, sans-serif',
  'edgeLabelBackground':'#FCEB6C'
}}}%%
flowchart TB
    P0["フェーズ0<br/>基礎準備"] --> G1{"ゲート1<br/>¥3–8M"}
    G1 --> P1["フェーズ1<br/>基盤構築"] --> G2{"ゲート2<br/>¥30–50M"}
    G2 --> P2["フェーズ2<br/>パイロット設計"] --> G3{"ゲート3<br/>¥80–200M"}
    G3 --> P3["フェーズ3<br/>パイロット建設"] --> G4{"ゲート4<br/>収益"}
    G4 --> P4["フェーズ4<br/>運用・拡大"]

    F1["L1 — 創設者<br/>¥3M"]
    F2["L2 — 政府<br/>補助金"]
    F3["L3 — 財団"]
    F4["L4 — 企業<br/>パートナー"]
    F5["L5 — 運営<br/>収益"]

    F1 --> G1
    F2 --> G2
    F3 --> G2
    F2 --> G3
    F3 --> G3
    F4 --> G3
    F5 --> G4

    P1 -.->|実現可能性調査が<br/>補助金を解放| F2
    P1 -.->|法人設立が<br/>財団を解放| F3
    P3 -.->|動作パイロットが<br/>企業を解放| F4
    P3 -.->|運営開始で<br/>収益創出| F5

    classDef phase fill:#6796e6,stroke:#3655b5,stroke-width:1px,color:#FFFFFF,font-weight:bold
    classDef gate  fill:#e58520,stroke:#A85C10,stroke-width:1px,color:#FFFFFF,font-weight:bold
    classDef fund  fill:#505050,stroke:#6796e6,stroke-width:1.4px,color:#DEDEDE
    class P0,P1,P2,P3,P4 phase
    class G1,G2,G3,G4 gate
    class F1,F2,F3,F4,F5 fund

    linkStyle default stroke:#A8A8A8,stroke-width:1.4px,color:#000000
    linkStyle 1,3,5,7 stroke:#FCEB6C,stroke-width:2.5px,color:#000000
```

---

## 凡例

| 形状・色 | 意味 |
|---|---|
| **水色ボックス** (`#6796e6`) | プロジェクトフェーズ — 実施内容 |
| **オレンジ色ひし形** (`#e58520`) | 資金調達ゲート — フェーズ間のチェックポイント |
| **スレートボックス・水色ボーダー** (`#505050` / `#6796e6`) | 資金調達ソース・レイヤー |
| **暗いダッシュボックス・黄色ボーダー** | ゲート不通過時の保留・縮小アクション |
| **実線矢印** | 順次フロー / 資金流入 |
| **点線矢印** | フィードバックループ — フェーズ成果物が次の資金レイヤーを解放 |

## 読み方

1. **上段を左から右へ読む** — これがプロジェクトの5フェーズを通じた前進パスです。
2. **黄色ひし形は判断ゲートです。** 各ゲートは「次のフェーズを開始するのに十分な資金を確保できたか？」を問います。通過 → 前進。資金不足 → 灰色の保留・縮小ボックスに入り、再提案します。
3. **下段は資金調達スタックです。** 矢印は各資金ソースが解放するゲートに向かって上方向に伸びます。
4. **点線矢印がループを閉じます。** フェーズを完了すると成果物（実現可能性調査、法人設立、動作パイロット）が生まれ、それ自体が次の資金レイヤーを解放します。これがプロジェクトのエンジンです。

---

---

## 資金調達スタック — 現状（Baseline Rev 1、2026年5月）

| 資金レイヤー | 調達元 | 金額（¥M） |
|---|---|---|
| L1 — 設立者 | 設立者出資（Rob Oudendijk） | ¥6M |
| L2 — 政府補助金 | 国・県・市町村補助金 | ¥115M |
| L3 — 財団 | 慈善財団 | ¥33M |
| L4 — 企業パートナー | 企業サステナビリティ・CSR | ¥35M |
| L5 — 事業収益 | データセンター・EV充電初期収益 | ¥3M |
| **調達済み・確約合計** | | **¥192M** |
| | | |
| **BAC（PMB）** | プロジェクト予算ベースライン | **¥220M** |
| **マネジメント予備費** | 理事会管理予備費 | ¥25M |
| **総プロジェクト予算** | | **¥245M** |
| | | |
| **BAC対資金不足額** | BAC充足に必要な追加調達額 | **¥28M** |
| **総予算対資金不足額** | 予備費含む充足に必要な追加調達額 | **¥53M** |

> **注記：** ¥28M〜¥53Mの資金不足は、フェーズ2（M10〜M18）において追加の政府補助金・新規企業提携・つなぎ融資により補填する計画です。上記の資金調達スタックは、2026年5月時点の確約・見込みを反映したものです。ステークホルダーへの透明性確保のため、不足額は明示しています。数字を人為的に嵩上げすることはいたしません。

---

*`mitsue_implementation_plan_jp.md` より引用 — 2026年5月*
