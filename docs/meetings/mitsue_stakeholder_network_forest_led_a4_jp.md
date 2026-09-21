<!-- Version: v1.0 | Last modified: 2026-09-21 -->

<style>
  html { font-size: 11px !important; }
  body { line-height: 1.28 !important; }
  p, blockquote, ul, ol, dl, table { margin: 3px 0 !important; }
  h1, h2, h3, h4, h5, h6 { margin-top: 4px !important; margin-bottom: 2px !important; }
  hr { margin: 4px 0 !important; }
  table td, table th { padding: 2px 6px !important; }
  .mermaid .edgeLabel text, .mermaid .edgeLabel tspan { fill: #1A1A1A !important; }
  .mermaid .edgeLabel, .mermaid .edgeLabel div, .mermaid .edgeLabel span, .mermaid .edgeLabel p { color: #1A1A1A !important; }
  .mermaid .node foreignObject, .mermaid .node foreignObject div, .mermaid .node foreignObject span { overflow: visible !important; max-width: none !important; white-space: nowrap !important; }
  .legend-row { font-size: 8.5pt; }
  .legend-sw { display:inline-block; width:10px; height:8px; margin-right:4px; vertical-align:middle; border-radius:2px; }
  .legend-sw.dash { background: repeating-linear-gradient(90deg,#718096 0 3px,transparent 3px 5px); height:2px; margin-top:4px; }
  .mermaid svg { max-width: 100% !important; width: 100% !important; height: auto !important; }
  .mermaid .cluster rect { fill: #ffffff !important; stroke: #cbd5e0 !important; }
  .mermaid .cluster text, .mermaid .cluster-label { fill: #4a5568 !important; font-weight: 700 !important; }
</style>

<div style="font-family:-apple-system,Helvetica,Arial,sans-serif;">
<p style="font-size:7.5pt; font-weight:600; letter-spacing:0.25em; color:#3a7a5a; margin:0 0 2mm;">プロジェクト文書 ・ 検討用ドラフト</p>
<h1 style="font-size:20pt; font-weight:700; margin:0 0 1mm;">ステークホルダー関係図 — 森林チーム主導モデル</h1>
<p style="font-size:10pt; color:#666; margin:0 0 1mm;">御杖村 AIデータセンター＆バイオマスエネルギープロジェクト</p>
<p style="font-size:9pt; color:#888; margin:0 0 4mm;">v1.0 · 2026-09-21 · ロブ・アウデンダイク</p>
</div>

> **ごく初期の検討案です。** ここに記載の内容は何も確定・合意しておらず、議論のたたき台にすぎません。署名を前提とした提案ではありません。`mitsue_kanko_collaboration_diagrams`（NGO主導モデル）の代替案として、ここでは御杖村森林組合（8名クルー）を伐採・植林・加工の実務拠点とし、NGOが日常のオペレーション調整を委任する形を示しています。

## 関係図

```mermaid
%%{init: {'flowchart': {'nodeSpacing': 12, 'rankSpacing': 34, 'padding': 6}, 'themeVariables': {'fontSize':'17px'}}}%%
graph TB
    subgraph Government["政府"]
        VILLAGE["村役場"]
        NARA["奈良県<br/>土地許可・補助金未定"]
        NATIONAL["経産省/環境省/林野庁<br/>NEDO/JST"]
    end
    subgraph NGO_NPO["NGO・NPO"]
        NGO["プロジェクトNGO<br/>法務・財務ラッパー"]
        MORETREES["more trees"]
        FOUND["財団"]
    end
    subgraph Cooperative["森林チーム"]
        COOP["御杖村森林組合<br/>8名クルー - 拠点"]
    end
    subgraph Companies["企業"]
        GK["運営会社<br/>GK/KK<br/>CHP + AI DC"]
        MIZUHO["みずほ証券"]
        SUGANO["菅野オーガニック"]
        CORP["企業パートナー<br/>未確定"]
        LEGAL["法務アドバイザー・無償<br/>リンクレーターズ、TMI、堀田"]
    end
    subgraph Academia["学術機関"]
        NAIST["NAIST"]
    end

    VILLAGE -->|連携| MORETREES
    MORETREES -->|連携 樹種/手法| NGO
    NGO -->|調整 実務を委任| COOP
    NAIST -->|伐採/加工研究 - 直接| COOP
    COOP -->|燃料材供給| GK
    NATIONAL -->|補助金 - 村経由| GK
    NATIONAL -.->|設備助成 - 直接| COOP
    NARA -.->|土地利用許可| GK
    NGO -->|過半数出資| GK
    FOUND -->|助成金| NGO
    MIZUHO -.->|資金調達 - 未定| GK
    CORP -.->|CSR - 未確定| NGO
    SUGANO -.->|試験地 - 検討中| GK
    LEGAL -.->|無償法律助言| NGO

    classDef gov fill:#2b6cb0,color:#fff,stroke:#1a4971,stroke-width:1px
    classDef ngo fill:#276749,color:#fff,stroke:#1c4532,stroke-width:1px
    classDef co fill:#975a16,color:#fff,stroke:#7b341e,stroke-width:1px
    classDef coop fill:#6b46c1,color:#fff,stroke:#44337a,stroke-width:3px
    classDef acad fill:#b83280,color:#fff,stroke:#702459,stroke-width:1px
    class VILLAGE,NARA,NATIONAL gov
    class NGO,MORETREES,FOUND ngo
    class GK,MIZUHO,CORP,SUGANO,LEGAL co
    class COOP coop
    class NAIST acad
```

## 凡例

<table style="width:100%; border:none; border-collapse:collapse; margin:2mm 0;"><tr>
<td style="border:none; padding:1mm 4mm 1mm 0; font-size:8.5pt;"><span class="legend-sw" style="background:#2b6cb0"></span>政府</td>
<td style="border:none; padding:1mm 4mm 1mm 0; font-size:8.5pt;"><span class="legend-sw" style="background:#276749"></span>NGO・NPO</td>
<td style="border:none; padding:1mm 4mm 1mm 0; font-size:8.5pt;"><span class="legend-sw" style="background:#975a16"></span>企業</td>
</tr><tr>
<td style="border:none; padding:1mm 4mm 1mm 0; font-size:8.5pt;"><span class="legend-sw" style="background:#6b46c1"></span>森林チーム（組合）</td>
<td style="border:none; padding:1mm 4mm 1mm 0; font-size:8.5pt;"><span class="legend-sw" style="background:#b83280"></span>学術機関</td>
<td style="border:none; padding:1mm 4mm 1mm 0; font-size:8.5pt;">— 実線：計画・構造上のつながり &nbsp;·&nbsp; <span class="legend-sw dash" style="width:20px;"></span> 点線：未確定・検討中</td>
</tr></table>

**図の読み方：** 連携の流れは村役場 → more trees → NGO。NGOは御杖村森林組合（8名クルー拠点）に日常のオペレーション調整を委任し、組合は運営会社へ燃料材を供給します。NAISTの研究連携はNGOを介さず組合へ直接つながります。点線（設備助成、土地利用許可、みずほの資金調達、企業CSR、菅野の試験地、無償法律助言）はまだ文書で確定していない関係を示します。

## ノード詳細

| ノード | 分類 | 役割・現状 |
|---|---|---|
| 村役場 | 政府 | 正式な連携窓口。運営会社への土地・許可を付与 |
| 奈良県 | 政府 | 土地利用許可、補助金は未定（検討中） |
| 経産省・環境省・林野庁・NEDO・JST | 政府 | 国の補助金源。森林・再エネ系は村経由、DC・電力系は運営会社経由 |
| プロジェクトNGO（一般社団法人） | NGO・NPO | 非分配型の法務・財務ラッパー。運営会社の過半数出資者 |
| more trees | NGO・NPO | 村役場とNGOをつなぐ連携役、植林の樹種・手法パートナー |
| 財団 | NGO・NPO | NGOへの助成金源 — 目標¥33M、現時点の確保額¥0（資金調達フローチャート参照） |
| 御杖村森林組合 | 森林チーム | 8名クルーの森林組合。本モデルでは伐採・植林・加工の実務拠点 |
| 運営会社（GK/KK） | 企業 | CHP＋AIデータセンターの運営主体、NGOが過半数出資 |
| みずほ証券 | 企業 | 資金調達の選択肢 — 未定（検討中） |
| 菅野オーガニック | 企業 | 試験的なCHP候補地（検討中） |
| 企業パートナー | 企業 | CSR・協賛は未確定（検討中） |
| 法務アドバイザー（無償） | 企業 | リンクレーターズ（渡邊氏）、TMI（中野氏）、おそらく西村あさひ（堀田氏） — いずれも無償support確定済み、書面での契約はまだなし |
| NAIST | 学術機関 | 森林チームへの研究連携（伐採・加工）。窓口は久保氏（CDG）、塩崎学長の紹介 — 関係は発展途上で、正式なMOUはまだなし |

---

*本図は`mitsue_kanko_collaboration_diagrams`（NGO主導モデル）に対する森林チーム主導の代替案です。出典：リポジトリ内`mitsue_kanko_forest_led_diagrams_a3.html`パネル4、2026-09-21時点のプロジェクト記録と照合済み。*

<table style="width:100%; border:none; border-collapse:collapse; margin-top:2mm;"><tr>
<td style="border:none; vertical-align:middle;">
<em>御杖村 AIデータセンタープロジェクト</em><br/>
<em>連絡先：ロブ・アウデンダイク · oudendijk.biz@gmail.com · 080-2260-5966</em>
</td>
<td style="border:none; vertical-align:middle; text-align:right; width:100px;">
<a href="https://mitsue.it"><strong>mitsue.it</strong></a><br/>
<img src="https://api.qrserver.com/v1/create-qr-code/?size=90x90&data=https://mitsue.it" alt="mitsue.it QRコード" width="90" height="90"/>
</td>
</tr></table>
