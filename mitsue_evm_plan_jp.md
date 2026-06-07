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

<p align="right">Version: v2.1（基準値Rev.1） &nbsp;|&nbsp; Last modified: 2026-06-07</p>

---

# 御杖プロジェクト — アーンドバリュー管理計画
### パフォーマンス基準値 · コスト管理 · 予測フレームワーク

*フェーズ0〜3 · 2026年4月 – 2028年9月*

---

## 1. 目的と対象範囲

本EVM計画は、御杖持続可能エネルギー・AIデータセンタープロジェクトのフェーズ0〜3（30か月間）にわたる**パフォーマンス測定基準（PMB）**を確立するものです。スケジュールとコストのパフォーマンス測定方法、ステークホルダーへの進捗報告、完成時コストおよび日程の予測方法を定めています。

本計画の対象期間は**2026年4月〜2028年9月（30か月間）**です。フェーズ4（運営・拡大期、31か月目以降）は資金調達方法が異なり（事業収益による）、フェーズ1の結果確認後に翌年計画するため、基準値には含みません。

**現行基準値のデータ日付**：2026年5月18日（第2か月末）

---

## 2. EVM基本指標

| 用語 | 記号 | 計算式 | 意味 |
|------|------|--------|------|
| 計画価値 | **PV** | 時間配分済み予算 | 予定通り完了すべき作業の予算コスト |
| アーンドバリュー | **EV** | 達成率 × BAC | 実際に完了した作業の予算コスト |
| 実際コスト | **AC** | 請求書＋人件費 | 実際に支出した金額 |
| 完成時予算 | **BAC** | PV合計 | PMBの総承認予算 |
| スケジュール差異 | **SV** | EV − PV | マイナス＝計画より遅れ |
| コスト差異 | **CV** | EV − AC | マイナス＝予算超過 |
| スケジュール効率指数 | **SPI** | EV ÷ PV | 1.0未満＝遅延 |
| コスト効率指数 | **CPI** | EV ÷ AC | 1.0未満＝予算超過 |
| 完成時見積 | **EAC** | AC + (BAC−EV)÷CPI | 最終コスト予測 |
| 残作業見積 | **ETC** | EAC − AC | 残作業コスト予測 |
| 完成時差異 | **VAC** | BAC − EAC | 完了時の超過・節約予測 |
| 完了時効率指数 | **TCPI** | (BAC−EV)÷(BAC−AC) | 予算内完了に必要な効率 |

---

## 3. 予算構造

### 3.1 予算サマリー

| 区分 | 項目 | 予算（百万円） | BAC比率 |
|------|------|---------------|---------|
| 総プロジェクト予算 | | **¥245.0M** | — |
| — マネジメント予備費（約11%） | PMB対象外 | **¥25.0M** | — |
| **パフォーマンス測定基準（BAC）** | | **¥220.0M** | 100% |
| 1.0 | プロジェクト管理・ガバナンス | ¥15.0M | 6.8% |
| 2.0 | フェーズ0 — 準備期 | ¥0.25M | 0.1% |
| 3.0 | フェーズ1 — 基盤構築期 | ¥5.5M | 2.5% |
| 4.0 | フェーズ2 — 試験設計期 | ¥22.25M | 10.1% |
| 5.0 | フェーズ3 — 試験建設期 | ¥177.0M | 80.5% |

> **マネジメント予備費**（¥25M）は代表理事が管理し、**PMBには含まれません**。予見不可能なスコープへの対応のみを目的とし、理事会の承認を得た場合にのみ取り崩し可能です。

> **ベースライン Rev.1（2026年5月）** — 太陽光発電（¥20〜30万/kW）、学校耐震改修（¥20〜50万/㎡）、商用EV急速充電器（1基¥500〜600万）、林道整備など日本国内の実勢価格と照合し再評価。フェーズ3の各費目、プロジェクトマネジメント、予備費を引き上げ、BACを¥1.68億から¥2.20億へ改定。

### 3.2 作業分解構造（WBS）— 予算詳細

| WBS | 項目 | 予算（¥M） | フェーズ |
|-----|------|------------|---------|
| 1.0 | **プロジェクト管理・ガバナンス** | | |
| 1.1 | PMチーム中核（代表理事＋コーディネーター） | ¥8.0M | 全期間 |
| 1.2 | 法務・会計・行政書士費用 | ¥4.0M | 全期間 |
| 1.3 | 広報・ウェブサイト・翻訳 | ¥3.0M | 全期間 |
| | *小計 1.0* | *¥15.0M* | |
| 2.0 | **フェーズ0 — 準備期** | | |
| 2.1 | 地域ステークホルダーとの対話・交通費 | ¥0.10M | P0 |
| 2.2 | 憲章・書類作成 | ¥0.10M | P0 |
| 2.3 | 創設チームの特定 | ¥0.05M | P0 |
| | *小計 2.0* | *¥0.25M* | |
| 3.0 | **フェーズ1 — 基盤構築期** | | |
| 3.1 | 一般社団法人設立 | ¥0.5M | P1 |
| 3.2 | 林業フィージビリティスタディ | ¥1.5M | P1 |
| 3.3 | エネルギーシステム調査 | ¥1.5M | P1 |
| 3.4 | 建物・敷地調査 | ¥0.8M | P1 |
| 3.5 | 通信環境調査 | ¥0.4M | P1 |
| 3.6 | アドバイザリーボード・銀行口座・会計設立 | ¥0.8M | P1 |
| | *小計 3.0* | *¥5.5M* | |
| 4.0 | **フェーズ2 — 試験設計期** | | |
| 4.1 | 構造・建築設計 | ¥2.0M | P2 |
| 4.2 | エネルギーシステム設計 | ¥2.0M | P2 |
| 4.3 | データセンター・IT設計 | ¥1.0M | P2 |
| 4.4 | EV充電システム設計 | ¥1.0M | P2 |
| 4.5 | 許認可・規制対応（METI、FIT、林業） | ¥3.5M | P2 |
| 4.6 | 提携・土地所有者契約 | ¥1.5M | P2 |
| 4.7 | 補助金申請 | ¥2.0M | P2 |
| 4.8 | スタッフ採用・研修（パートタイム2〜3名） | ¥6.0M | P2 |
| 4.9 | ベンダー事前選定 | ¥1.5M | P2 |
| 4.10 | フェーズ2予備費 | ¥1.75M | P2 |
| | *小計 4.0* | *¥22.25M* | |
| 5.0 | **フェーズ3 — 試験建設期** | | |
| 5.1 | 校舎改修（棟1区画） | ¥38.0M | P3 |
| 5.2 | 太陽光発電設置（約100kW） | ¥22.0M | P3 |
| 5.3 | 蓄電池システム | ¥12.0M | P3 |
| 5.4 | EV充電インフラ（4基） | ¥15.0M | P3 |
| 5.5 | データセンター設備（サーバー10〜20台） | ¥20.0M | P3 |
| 5.6 | 林業作業（5〜10ha伐採・植替） | ¥25.0M | P3 |
| 5.7 | 光ファイバー接続強化 | ¥10.0M | P3 |
| 5.8 | 試験・調整・稼働開始 | ¥8.0M | P3 |
| 5.9 | フェーズ3予備費（18%） | ¥27.0M | P3 |
| | *小計 5.0* | *¥177.0M* | |
| | **合計 BAC** | **¥220.0M** | |

---

## 4. 時間配分基準値（S字曲線）

30か月にわたる月別計画支出と累積計画価値。フェーズ内の支出は調査・設計に前倒しされ、建設支出は22〜27か月目にピークを迎えます。

| 月 | 年月 | フェーズ | 月別PV（¥M） | 累積PV（¥M） | 進捗率 |
|----|------|---------|-------------|-------------|--------|
| M1 | 2026年4月 | P0 | 0.05 | 0.05 | 0.0% |
| M2 | 2026年5月 | P0 | 0.10 | 0.15 | 0.1% |
| **M2 ← 基準日** | | | | | |
| M3 | 2026年6月 | P0 | 0.10 | 0.25 | 0.1% |
| M4 | 2026年7月 | P1 | 0.20 | 0.45 | 0.2% |
| M5 | 2026年8月 | P1 | 0.50 | 0.95 | 0.4% |
| M6 | 2026年9月 | P1 | 0.80 | 1.75 | 0.8% |
| M7 | 2026年10月 | P1 | 1.20 | 2.95 | 1.3% |
| M8 | 2026年11月 | P1 | 1.50 | 4.45 | 2.0% |
| M9 | 2026年12月 | P1 | 1.30 | 5.75 | 2.6% |
| M10 | 2027年1月 | P2 | 1.50 | 7.25 | 3.3% |
| M11 | 2027年2月 | P2 | 2.20 | 9.45 | 4.3% |
| M12 | 2027年3月 | P2 | 2.80 | 12.25 | 5.6% |
| M13 | 2027年4月 | P2 | 3.00 | 15.25 | 6.9% |
| M14 | 2027年5月 | P2 | 3.00 | 18.25 | 8.3% |
| M15 | 2027年6月 | P2 | 3.00 | 21.25 | 9.7% |
| M16 | 2027年7月 | P2 | 2.50 | 23.75 | 10.8% |
| M17 | 2027年8月 | P2 | 2.50 | 26.25 | 11.9% |
| M18 | 2027年9月 | P2 | 2.00 | 28.25 | 12.8% |
| M19 | 2027年10月 | P3 | 4.00 | 32.25 | 14.7% |
| M20 | 2027年11月 | P3 | 7.00 | 39.25 | 17.8% |
| M21 | 2027年12月 | P3 | 11.00 | 50.25 | 22.8% |
| M22 | 2028年1月 | P3 | 16.50 | 66.75 | 30.3% |
| M23 | 2028年2月 | P3 | 20.50 | 87.25 | 39.7% |
| M24 | 2028年3月 | P3 | 20.50 | 107.75 | 49.0% |
| M25 | 2028年4月 | P3 | 25.00 | 132.75 | 60.3% |
| M26 | 2028年5月 | P3 | 25.00 | 157.75 | 71.7% |
| M27 | 2028年6月 | P3 | 20.50 | 178.25 | 81.0% |
| M28 | 2028年7月 | P3 | 20.50 | 198.75 | 90.3% |
| M29 | 2028年8月 | P3 | 14.00 | 212.75 | 96.7% |
| M30 | 2028年9月 | P3 | 7.25 | 220.00 | 100.0% |
| | **BAC** | | **¥220.0M** | | |

### S字曲線の形状

支出プロファイルは典型的な**緩やか→加速→緩やか**のS字曲線を描きます：
- **M1〜M9**（フェーズ0〜1）：立ち上げ期 — 法人設立、フィージビリティスタディ
- **M10〜M18**（フェーズ2）：加速期 — 詳細設計、許認可申請、補助金申請
- **M19〜M28**（フェーズ3中核）：ピーク支出期 — 建設・調達・設置工事
- **M29〜M30**（フェーズ3完了）：逓減期 — 試験調整、完了検査、引渡し

<div style="page-break-inside:avoid; margin: 10pt 0">

**図1 — 基準値S字曲線（累積計画価値）**

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 325" style="width:100%;display:block">
  <rect x="60" y="28" width="64" height="252" fill="#eef4ff"/>
  <rect x="124" y="28" width="128" height="252" fill="#dce8ff"/>
  <rect x="252" y="28" width="193" height="252" fill="#fff4e6"/>
  <rect x="445" y="28" width="235" height="252" fill="#fff0f0"/>
  <text x="92" y="42" text-anchor="middle" font-size="8" fill="#6796e6" font-weight="bold" font-family="Noto Sans JP,Yu Gothic,sans-serif">P0</text>
  <text x="188" y="42" text-anchor="middle" font-size="8" fill="#4a7ac4" font-weight="bold" font-family="Noto Sans JP,Yu Gothic,sans-serif">P1 基盤構築</text>
  <text x="348" y="42" text-anchor="middle" font-size="8" fill="#c06010" font-weight="bold" font-family="Noto Sans JP,Yu Gothic,sans-serif">P2 試験設計</text>
  <text x="562" y="42" text-anchor="middle" font-size="8" fill="#d94f4f" font-weight="bold" font-family="Noto Sans JP,Yu Gothic,sans-serif">P3 試験建設</text>
  <line x1="60" y1="280" x2="680" y2="280" stroke="#bbb" stroke-width="0.6"/>
  <line x1="60" y1="250" x2="680" y2="250" stroke="#ddd" stroke-width="0.4"/>
  <line x1="60" y1="220" x2="680" y2="220" stroke="#ddd" stroke-width="0.4"/>
  <line x1="60" y1="191" x2="680" y2="191" stroke="#ddd" stroke-width="0.4"/>
  <line x1="60" y1="161" x2="680" y2="161" stroke="#ddd" stroke-width="0.4"/>
  <line x1="60" y1="131" x2="680" y2="131" stroke="#ddd" stroke-width="0.4"/>
  <line x1="60" y1="101" x2="680" y2="101" stroke="#ddd" stroke-width="0.4"/>
  <line x1="60" y1="72" x2="680" y2="72" stroke="#ddd" stroke-width="0.4"/>
  <line x1="60" y1="42" x2="680" y2="42" stroke="#ddd" stroke-width="0.4"/>
  <line x1="167" y1="28" x2="167" y2="280" stroke="#ddd" stroke-width="0.4"/>
  <line x1="295" y1="28" x2="295" y2="280" stroke="#ddd" stroke-width="0.4"/>
  <line x1="423" y1="28" x2="423" y2="280" stroke="#ddd" stroke-width="0.4"/>
  <line x1="552" y1="28" x2="552" y2="280" stroke="#ddd" stroke-width="0.4"/>
  <line x1="680" y1="28" x2="680" y2="280" stroke="#ddd" stroke-width="0.4"/>
  <line x1="60" y1="30" x2="680" y2="30" stroke="#d94f4f" stroke-width="1" stroke-dasharray="5,4"/>
  <text x="683" y="33" font-size="7" fill="#d94f4f" font-family="Noto Sans JP,Yu Gothic,sans-serif">BAC¥220M</text>
  <line x1="103" y1="28" x2="103" y2="288" stroke="#e58520" stroke-width="1.5" stroke-dasharray="4,3"/>
  <text x="106" y="299" font-size="7" fill="#e58520" font-weight="bold" font-family="Noto Sans JP,Yu Gothic,sans-serif">▲ 基準日 2026-05-18</text>
  <text x="55" y="283" text-anchor="end" font-size="8" fill="#555" font-family="Noto Sans JP,Yu Gothic,sans-serif">0</text>
  <text x="55" y="253" text-anchor="end" font-size="8" fill="#555" font-family="Noto Sans JP,Yu Gothic,sans-serif">25</text>
  <text x="55" y="223" text-anchor="end" font-size="8" fill="#555" font-family="Noto Sans JP,Yu Gothic,sans-serif">50</text>
  <text x="55" y="194" text-anchor="end" font-size="8" fill="#555" font-family="Noto Sans JP,Yu Gothic,sans-serif">75</text>
  <text x="55" y="164" text-anchor="end" font-size="8" fill="#555" font-family="Noto Sans JP,Yu Gothic,sans-serif">100</text>
  <text x="55" y="134" text-anchor="end" font-size="8" fill="#555" font-family="Noto Sans JP,Yu Gothic,sans-serif">130</text>
  <text x="55" y="104" text-anchor="end" font-size="8" fill="#555" font-family="Noto Sans JP,Yu Gothic,sans-serif">160</text>
  <text x="55" y="75" text-anchor="end" font-size="8" fill="#555" font-family="Noto Sans JP,Yu Gothic,sans-serif">195</text>
  <text x="55" y="45" text-anchor="end" font-size="8" fill="#555" font-family="Noto Sans JP,Yu Gothic,sans-serif">220</text>
  <text x="16" y="165" text-anchor="middle" font-size="8" fill="#555" transform="rotate(-90,16,165)" font-family="Noto Sans JP,Yu Gothic,sans-serif">百万円（累計）</text>
  <text x="60" y="295" text-anchor="middle" font-size="8" fill="#555" font-family="Noto Sans JP,Yu Gothic,sans-serif">M1</text>
  <text x="167" y="295" text-anchor="middle" font-size="8" fill="#555" font-family="Noto Sans JP,Yu Gothic,sans-serif">M6</text>
  <text x="295" y="295" text-anchor="middle" font-size="8" fill="#555" font-family="Noto Sans JP,Yu Gothic,sans-serif">M12</text>
  <text x="423" y="295" text-anchor="middle" font-size="8" fill="#555" font-family="Noto Sans JP,Yu Gothic,sans-serif">M18</text>
  <text x="552" y="295" text-anchor="middle" font-size="8" fill="#555" font-family="Noto Sans JP,Yu Gothic,sans-serif">M24</text>
  <text x="680" y="295" text-anchor="middle" font-size="8" fill="#555" font-family="Noto Sans JP,Yu Gothic,sans-serif">M30</text>
  <text x="60" y="307" text-anchor="middle" font-size="7" fill="#999" font-family="Noto Sans JP,Yu Gothic,sans-serif">26年4月</text>
  <text x="167" y="307" text-anchor="middle" font-size="7" fill="#999" font-family="Noto Sans JP,Yu Gothic,sans-serif">26年9月</text>
  <text x="295" y="307" text-anchor="middle" font-size="7" fill="#999" font-family="Noto Sans JP,Yu Gothic,sans-serif">27年3月</text>
  <text x="423" y="307" text-anchor="middle" font-size="7" fill="#999" font-family="Noto Sans JP,Yu Gothic,sans-serif">27年9月</text>
  <text x="552" y="307" text-anchor="middle" font-size="7" fill="#999" font-family="Noto Sans JP,Yu Gothic,sans-serif">28年3月</text>
  <text x="680" y="307" text-anchor="middle" font-size="7" fill="#999" font-family="Noto Sans JP,Yu Gothic,sans-serif">28年9月</text>
  <line x1="60" y1="28" x2="60" y2="282" stroke="#888" stroke-width="1.5"/>
  <line x1="60" y1="280" x2="685" y2="280" stroke="#888" stroke-width="1.5"/>
  <polygon points="60,279.9 81,279.8 103,279.6 124,279.3 146,278.6 167,277.4 188,275.6 210,273.4 231,271.4 252,269.2 274,265.9 295,261.8 316,257.3 338,252.8 359,248.4 381,244.7 402,240.9 423,237.9 445,233.5 466,226.1 487,214.2 509,196.3 530,174 552,151.7 573,124.9 594,98.1 616,75.8 637,53.4 658,38.6 680,30 680,280 60,280" fill="#6796e6" fill-opacity="0.12"/>
  <polyline points="60,279.9 81,279.8 103,279.6 124,279.3 146,278.6 167,277.4 188,275.6 210,273.4 231,271.4 252,269.2 274,265.9 295,261.8 316,257.3 338,252.8 359,248.4 381,244.7 402,240.9 423,237.9 445,233.5 466,226.1 487,214.2 509,196.3 530,174 552,151.7 573,124.9 594,98.1 616,75.8 637,53.4 658,38.6 680,30" fill="none" stroke="#6796e6" stroke-width="2.5" stroke-linejoin="round"/>
  <!-- ゲートマーカー — ひし形；↩ラベルは閾値未達時の対応を示す -->
  <polygon points="124,274.3 129,279.3 124,284.3 119,279.3" fill="#4a7ac4" stroke="white" stroke-width="1.5"/>
  <text x="116" y="270" font-size="6.5" fill="#4a7ac4" font-family="Noto Sans JP,Yu Gothic,sans-serif">G1</text>
  <text x="116" y="263" font-size="5.5" fill="#4a7ac4" font-style="italic" font-family="Noto Sans JP,Yu Gothic,sans-serif">↩ 不足: 保留・再提案</text>
  <polygon points="252,264.2 257,269.2 252,274.2 247,269.2" fill="#4a7ac4" stroke="white" stroke-width="1.5"/>
  <text x="244" y="260" font-size="6.5" fill="#4a7ac4" font-family="Noto Sans JP,Yu Gothic,sans-serif">G2</text>
  <text x="244" y="253" font-size="5.5" fill="#4a7ac4" font-style="italic" font-family="Noto Sans JP,Yu Gothic,sans-serif">↩ 不足: 縮小検討</text>
  <polygon points="445,228.5 450,233.5 445,238.5 440,233.5" fill="#c06010" stroke="white" stroke-width="1.5"/>
  <text x="437" y="224" font-size="6.5" fill="#c06010" font-family="Noto Sans JP,Yu Gothic,sans-serif">G3</text>
  <text x="437" y="217" font-size="5.5" fill="#c06010" font-style="italic" font-family="Noto Sans JP,Yu Gothic,sans-serif">↩ 不足: 段階的建設</text>
  <polygon points="680,25 685,30 680,35 675,30" fill="#d94f4f" stroke="white" stroke-width="1.5"/>
  <text x="648" y="25" font-size="6.5" fill="#d94f4f" font-family="Noto Sans JP,Yu Gothic,sans-serif">G4</text>
  <text x="648" y="38" font-size="5.5" fill="#d94f4f" font-style="italic" font-family="Noto Sans JP,Yu Gothic,sans-serif">↩ 不足: 試験継続</text>
  <circle cx="103" cy="279.8" r="5" fill="#e58520" stroke="white" stroke-width="1.5"/>
  <text x="107" y="274" font-size="7" fill="#e58520" font-weight="bold" font-family="Noto Sans JP,Yu Gothic,sans-serif">EV=¥0.12M</text>
</svg>

</div>

<div style="page-break-inside:avoid; margin: 10pt 0">

**図2 — 月別計画支出（フェーズ別）**

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 240" style="width:100%;display:block">
  <line x1="60" y1="200" x2="680" y2="200" stroke="#bbb" stroke-width="0.6"/>
  <line x1="60" y1="160" x2="680" y2="160" stroke="#ddd" stroke-width="0.4"/>
  <line x1="60" y1="120" x2="680" y2="120" stroke="#ddd" stroke-width="0.4"/>
  <line x1="60" y1="80" x2="680" y2="80" stroke="#ddd" stroke-width="0.4"/>
  <line x1="60" y1="40" x2="680" y2="40" stroke="#ddd" stroke-width="0.4"/>
  <line x1="60" y1="20" x2="680" y2="20" stroke="#ddd" stroke-width="0.4"/>
  <rect x="60" y="199.5" width="18" height="0.5" fill="#b8c9ee"/>
  <rect x="81" y="199" width="18" height="1" fill="#b8c9ee"/>
  <rect x="102" y="199" width="18" height="1" fill="#b8c9ee"/>
  <rect x="122" y="198" width="18" height="2" fill="#6796e6"/>
  <rect x="143" y="195" width="18" height="5" fill="#6796e6"/>
  <rect x="163" y="192" width="18" height="8" fill="#6796e6"/>
  <rect x="184" y="188" width="18" height="12" fill="#6796e6"/>
  <rect x="205" y="185" width="18" height="15" fill="#6796e6"/>
  <rect x="225" y="187" width="18" height="13" fill="#6796e6"/>
  <rect x="246" y="185" width="18" height="15" fill="#e58520"/>
  <rect x="267" y="178" width="18" height="22" fill="#e58520"/>
  <rect x="287" y="172" width="18" height="28" fill="#e58520"/>
  <rect x="308" y="170" width="18" height="30" fill="#e58520"/>
  <rect x="329" y="170" width="18" height="30" fill="#e58520"/>
  <rect x="349" y="170" width="18" height="30" fill="#e58520"/>
  <rect x="370" y="175" width="18" height="25" fill="#e58520"/>
  <rect x="391" y="175" width="18" height="25" fill="#e58520"/>
  <rect x="411" y="180" width="18" height="20" fill="#e58520"/>
  <rect x="432" y="170" width="18" height="30" fill="#d94f4f"/>
  <rect x="453" y="150" width="18" height="50" fill="#d94f4f"/>
  <rect x="473" y="120" width="18" height="80" fill="#d94f4f"/>
  <rect x="494" y="80" width="18" height="120" fill="#d94f4f"/>
  <rect x="515" y="50" width="18" height="150" fill="#d94f4f"/>
  <rect x="535" y="50" width="18" height="150" fill="#d94f4f"/>
  <rect x="556" y="20" width="18" height="180" fill="#d94f4f"/>
  <rect x="577" y="20" width="18" height="180" fill="#d94f4f"/>
  <rect x="597" y="50" width="18" height="150" fill="#d94f4f"/>
  <rect x="618" y="50" width="18" height="150" fill="#d94f4f"/>
  <rect x="639" y="100" width="18" height="100" fill="#d94f4f"/>
  <rect x="659" y="142" width="18" height="57.5" fill="#d94f4f"/>
  <line x1="60" y1="20" x2="60" y2="202" stroke="#888" stroke-width="1.5"/>
  <line x1="60" y1="200" x2="685" y2="200" stroke="#888" stroke-width="1.5"/>
  <text x="55" y="203" text-anchor="end" font-size="8" fill="#555" font-family="Noto Sans JP,Yu Gothic,sans-serif">0</text>
  <text x="55" y="163" text-anchor="end" font-size="8" fill="#555" font-family="Noto Sans JP,Yu Gothic,sans-serif">5</text>
  <text x="55" y="123" text-anchor="end" font-size="8" fill="#555" font-family="Noto Sans JP,Yu Gothic,sans-serif">11</text>
  <text x="55" y="83" text-anchor="end" font-size="8" fill="#555" font-family="Noto Sans JP,Yu Gothic,sans-serif">17</text>
  <text x="55" y="43" text-anchor="end" font-size="8" fill="#555" font-family="Noto Sans JP,Yu Gothic,sans-serif">22</text>
  <text x="55" y="23" text-anchor="end" font-size="8" fill="#555" font-family="Noto Sans JP,Yu Gothic,sans-serif">25</text>
  <text x="16" y="120" text-anchor="middle" font-size="8" fill="#555" transform="rotate(-90,16,120)" font-family="Noto Sans JP,Yu Gothic,sans-serif">百万円／月</text>
  <text x="69" y="213" text-anchor="middle" font-size="7.5" fill="#555" font-family="Noto Sans JP,Yu Gothic,sans-serif">M1</text>
  <text x="172" y="213" text-anchor="middle" font-size="7.5" fill="#555" font-family="Noto Sans JP,Yu Gothic,sans-serif">M6</text>
  <text x="296" y="213" text-anchor="middle" font-size="7.5" fill="#555" font-family="Noto Sans JP,Yu Gothic,sans-serif">M12</text>
  <text x="420" y="213" text-anchor="middle" font-size="7.5" fill="#555" font-family="Noto Sans JP,Yu Gothic,sans-serif">M18</text>
  <text x="544" y="213" text-anchor="middle" font-size="7.5" fill="#555" font-family="Noto Sans JP,Yu Gothic,sans-serif">M24</text>
  <text x="668" y="213" text-anchor="middle" font-size="7.5" fill="#555" font-family="Noto Sans JP,Yu Gothic,sans-serif">M30</text>
  <rect x="120" y="225" width="12" height="8" fill="#b8c9ee"/><text x="136" y="233" font-size="7.5" fill="#444" font-family="Noto Sans JP,Yu Gothic,sans-serif">P0</text>
  <rect x="160" y="225" width="12" height="8" fill="#6796e6"/><text x="176" y="233" font-size="7.5" fill="#444" font-family="Noto Sans JP,Yu Gothic,sans-serif">P1</text>
  <rect x="200" y="225" width="12" height="8" fill="#e58520"/><text x="216" y="233" font-size="7.5" fill="#444" font-family="Noto Sans JP,Yu Gothic,sans-serif">P2</text>
  <rect x="240" y="225" width="12" height="8" fill="#d94f4f"/><text x="256" y="233" font-size="7.5" fill="#444" font-family="Noto Sans JP,Yu Gothic,sans-serif">P3（ピーク M25-26: 月¥25M）</text>
</svg>

</div>

---

## 5. 現状パフォーマンス

**データ日付：2026年5月18日（第2か月末）**

### 5.1 状況説明

プロジェクトは**フェーズ0 — 準備期**にあります。現在進行中の活動は、村のリーダーシップとの非公式な対話、憲章の予備草案作成、創設チーム候補者の特定です。日本人共同設立者候補の探索は継続中ですが未確定 — これがフェーズ0の最も重要な依存事項です。

支出は個人的な交通費、書類翻訳費、奈良市内の行政書士への初期相談費用のみです。主要な契約はまだ締結されていません。

### 5.2 パフォーマンス指標 — フェーズ0

| 指標 | 値 | 備考 |
|------|-----|------|
| PV（基準日時点の計画価値） | ¥0.15M | M2末時点の計画支出 |
| EV（基準日時点のアーンドバリュー） | ¥0.12M | フェーズ0作業の約80%完了 |
| AC（基準日時点の実際コスト） | ¥0.08M | 計画を下回る — 主に個人時間 |
| **SV（スケジュール差異）** | **−¥0.03M** | 共同設立者未確定のため若干遅延 |
| **CV（コスト差異）** | **+¥0.04M** | P0コスト計画より低いため予算内 |
| **SPI** | **0.80** | 計画作業の80%を予定通り達成 |
| **CPI** | **1.50** | 支出¥1につき¥1.50の価値を創出 |

<div style="page-break-inside:avoid; margin: 8pt 0">

**図3 — EVM現状ダッシュボード（基準日：2026年5月18日）**

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 115" style="width:100%;display:block">
  <rect x="10" y="10" width="150" height="90" rx="6" fill="#eef4ff" stroke="#6796e6" stroke-width="1.5"/>
  <text x="85" y="28" text-anchor="middle" font-size="8.5" fill="#4a7ac4" font-weight="bold" font-family="Noto Sans JP,Yu Gothic,sans-serif">計画価値（PV）</text>
  <text x="85" y="55" text-anchor="middle" font-size="22" fill="#4a7ac4" font-weight="bold" font-family="Noto Sans JP,Yu Gothic,sans-serif">¥0.15M</text>
  <text x="85" y="72" text-anchor="middle" font-size="7.5" fill="#888" font-family="Noto Sans JP,Yu Gothic,sans-serif">M2末時点の計画作業予算</text>
  <rect x="175" y="10" width="150" height="90" rx="6" fill="#eefff0" stroke="#4aaa60" stroke-width="1.5"/>
  <text x="250" y="28" text-anchor="middle" font-size="8.5" fill="#2a8040" font-weight="bold" font-family="Noto Sans JP,Yu Gothic,sans-serif">アーンドバリュー（EV）</text>
  <text x="250" y="55" text-anchor="middle" font-size="22" fill="#2a8040" font-weight="bold" font-family="Noto Sans JP,Yu Gothic,sans-serif">¥0.12M</text>
  <text x="250" y="72" text-anchor="middle" font-size="7.5" fill="#888" font-family="Noto Sans JP,Yu Gothic,sans-serif">完了作業の予算価値</text>
  <rect x="340" y="10" width="150" height="90" rx="6" fill="#fff8ee" stroke="#e58520" stroke-width="1.5"/>
  <text x="415" y="28" text-anchor="middle" font-size="8.5" fill="#b05000" font-weight="bold" font-family="Noto Sans JP,Yu Gothic,sans-serif">実際コスト（AC）</text>
  <text x="415" y="55" text-anchor="middle" font-size="22" fill="#b05000" font-weight="bold" font-family="Noto Sans JP,Yu Gothic,sans-serif">¥0.08M</text>
  <text x="415" y="72" text-anchor="middle" font-size="7.5" fill="#888" font-family="Noto Sans JP,Yu Gothic,sans-serif">実際の支出（交通費・行書士・書類）</text>
  <rect x="505" y="10" width="88" height="42" rx="6" fill="#fffbe6" stroke="#cca000" stroke-width="1.5"/>
  <text x="549" y="24" text-anchor="middle" font-size="8" fill="#886600" font-weight="bold" font-family="Noto Sans JP,Yu Gothic,sans-serif">SPI = 0.80</text>
  <text x="549" y="36" text-anchor="middle" font-size="7" fill="#886600" font-family="Noto Sans JP,Yu Gothic,sans-serif">🟡 若干遅延</text>
  <text x="549" y="47" text-anchor="middle" font-size="6.5" fill="#aaa" font-family="Noto Sans JP,Yu Gothic,sans-serif">共同設立者候補未確定</text>
  <rect x="505" y="60" width="88" height="42" rx="6" fill="#eefff0" stroke="#4aaa60" stroke-width="1.5"/>
  <text x="549" y="74" text-anchor="middle" font-size="8" fill="#2a8040" font-weight="bold" font-family="Noto Sans JP,Yu Gothic,sans-serif">CPI = 1.50</text>
  <text x="549" y="86" text-anchor="middle" font-size="7" fill="#2a8040" font-family="Noto Sans JP,Yu Gothic,sans-serif">🟢 予算内</text>
  <text x="549" y="97" text-anchor="middle" font-size="6.5" fill="#aaa" font-family="Noto Sans JP,Yu Gothic,sans-serif">P0個人時間効果</text>
  <text x="605" y="55" text-anchor="middle" font-size="7.5" fill="#666" font-weight="bold" font-family="Noto Sans JP,Yu Gothic,sans-serif">BAC</text>
  <text x="605" y="67" text-anchor="middle" font-size="9" fill="#333" font-weight="bold" font-family="Noto Sans JP,Yu Gothic,sans-serif">¥220M</text>
  <text x="605" y="79" text-anchor="middle" font-size="6.5" fill="#999" font-family="Noto Sans JP,Yu Gothic,sans-serif">0.04%消化</text>
</svg>

</div>

> **注意：** 第2か月時点のCPI 1.50は一部フェーズ0の特性によるものです — 価値創出の大半が予算化された支出ではなく個人時間によるものです。フェーズ1のフィージビリティスタディ契約が確定するまで、このCPIをプロジェクト全体の予測に外挿しないでください。

### 5.3 フェーズ0 予測

| 指標 | 値 |
|------|-----|
| フェーズ0 BAC | ¥0.25M |
| EAC（P0）= AC + (BAC−EV)÷CPI | ¥0.16M |
| ETC（P0）= EAC − AC | ¥0.08M |
| VAC（P0）= BAC − EAC | **+¥0.09M 予算内** |
| TCPI | 0.87 — フェーズ0を予算内完了するために必要な効率 |

---

<div class="page-break"></div>

## 6. フェーズ別予測（基準値予測）

### 6.1 フェーズ0 — 準備期

| 項目 | 値 |
|------|-----|
| 期間 | M1〜M3（2026年4〜6月） |
| BAC | ¥0.25M |
| 計画完了日 | 2026年6月30日 |
| ゲート基準 | 創設チームの口頭合意；村リーダーへの情報共有 |
| 現状予測 | 2026年6月 オンスケジュール |
| コスト予測 | ¥0.16〜0.22M |

### 6.2 フェーズ1 — 基盤構築期

| 項目 | 値 |
|------|-----|
| 期間 | M4〜M9（2026年7〜12月） |
| BAC | ¥5.5M |
| 計画完了日 | 2026年12月31日 |
| ゲート基準 | ¥300万〜800万円確保；法人登記完了；各調査完了 |
| クリティカルパス | 林業・エネルギー調査（2026年Q3発注） |
| 主要リスク | 政府補助金承認は計画より2〜3か月かかる場合が多い |
| 対応策 | 調査範囲を若干縮小；P2開始を1〜2か月延期 |

### 6.3 フェーズ2 — 試験設計期

| 項目 | 値 |
|------|-----|
| 期間 | M10〜M18（2027年1〜9月） |
| BAC | ¥22.25M |
| 計画完了日 | 2027年9月30日 |
| ゲート基準 | ¥3,000万〜5,000万円確保；詳細設計完了；主要許認可取得 |
| クリティカルパス | METI許認可・FIT登録（6か月以上かかる場合あり） |
| 主要リスク | 許認可遅延によりP3開始が2027年10月以降にずれ込む |

### 6.4 フェーズ3 — 試験建設期

| 項目 | 値 |
|------|-----|
| 期間 | M19〜M30（2027年10月〜2028年9月） |
| BAC | ¥177M |
| 計画完了日 | 2028年9月30日 |
| クリティカルパス | 校舎改修 → 太陽光・蓄電池設置 → EV充電 → 調整・稼働 |
| 主要リスク | 建物構造上の問題によるスコープ増大（現状：低確率、高影響） |
| 対応策 | WBS 5.9予備費¥27M（18%）＋ マネジメント予備費¥25M でバックアップ |

---

## 7. 三シナリオ予測

| シナリオ | 説明 | EAC | 完了日 |
|----------|------|-----|--------|
| **楽観的** | 全補助金一発採択；建物良好；許認可遅延なし；下限ベンダー見積 | ¥185M | 2028年8月 |
| **基本ケース** | 許認可1件遅延（+2か月）；補助金1件翌年繰越；CPI≈1.0；中位ベンダー見積 | **¥220M** | 2028年9月 |
| **悲観的** | 許認可2件遅延；建物補修必要；補助金不足 — MR取崩し及び追加調達 | ¥285M | 2029年3月 |

> シナリオの幅はRev.0基準値より意図的に広げています。フェーズ1フィージビリティスタディ（M9）にて校舎の構造状態、ベンダー見積、補助金採択が確定すれば、レンジは大幅に絞られます。

<div style="page-break-inside:avoid; margin: 8pt 0">

**図4 — 三シナリオ EAC 比較**

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 175" style="width:100%;display:block">
  <rect x="160" y="10" width="500" height="140" fill="#fafafa" stroke="#ddd" stroke-width="0.5" rx="3"/>
  <line x1="527" y1="10" x2="527" y2="155" stroke="#6796e6" stroke-width="1" stroke-dasharray="5,3"/>
  <text x="527" y="166" text-anchor="middle" font-size="7.5" fill="#6796e6" font-weight="bold" font-family="Noto Sans JP,Yu Gothic,sans-serif">BAC¥220M</text>
  <line x1="568" y1="10" x2="568" y2="155" stroke="#e58520" stroke-width="1" stroke-dasharray="3,3"/>
  <text x="568" y="176" text-anchor="middle" font-size="7" fill="#e58520" font-family="Noto Sans JP,Yu Gothic,sans-serif">総予算¥245M</text>
  <text x="160" y="166" text-anchor="middle" font-size="7.5" fill="#666" font-family="Noto Sans JP,Yu Gothic,sans-serif">0</text>
  <text x="285" y="166" text-anchor="middle" font-size="7.5" fill="#666" font-family="Noto Sans JP,Yu Gothic,sans-serif">75</text>
  <text x="410" y="166" text-anchor="middle" font-size="7.5" fill="#666" font-family="Noto Sans JP,Yu Gothic,sans-serif">150</text>
  <text x="535" y="166" text-anchor="middle" font-size="7.5" fill="#666" font-family="Noto Sans JP,Yu Gothic,sans-serif">225</text>
  <text x="660" y="166" text-anchor="middle" font-size="7.5" fill="#666" font-family="Noto Sans JP,Yu Gothic,sans-serif">300 ¥M</text>
  <rect x="160" y="22" width="308" height="30" fill="#4aaa60" rx="3"/>
  <text x="148" y="40" text-anchor="end" font-size="8.5" fill="#222" font-weight="bold" font-family="Noto Sans JP,Yu Gothic,sans-serif">楽観的</text>
  <text x="155" y="50" text-anchor="end" font-size="7" fill="#555" font-family="Noto Sans JP,Yu Gothic,sans-serif">2028年8月</text>
  <text x="476" y="41" font-size="9" fill="#222" font-weight="bold" font-family="Noto Sans JP,Yu Gothic,sans-serif">¥185M（BAC比−¥35M）</text>
  <rect x="160" y="62" width="367" height="30" fill="#6796e6" rx="3"/>
  <text x="148" y="80" text-anchor="end" font-size="8.5" fill="#222" font-weight="bold" font-family="Noto Sans JP,Yu Gothic,sans-serif">基本ケース</text>
  <text x="155" y="90" text-anchor="end" font-size="7" fill="#555" font-family="Noto Sans JP,Yu Gothic,sans-serif">2028年9月</text>
  <text x="535" y="81" font-size="9" fill="#222" font-weight="bold" font-family="Noto Sans JP,Yu Gothic,sans-serif">¥220M（予算通り）</text>
  <rect x="160" y="102" width="475" height="30" fill="#d94f4f" rx="3"/>
  <text x="148" y="120" text-anchor="end" font-size="8.5" fill="#222" font-weight="bold" font-family="Noto Sans JP,Yu Gothic,sans-serif">悲観的</text>
  <text x="155" y="130" text-anchor="end" font-size="7" fill="#555" font-family="Noto Sans JP,Yu Gothic,sans-serif">2029年3月</text>
  <text x="643" y="121" font-size="9" fill="#222" font-weight="bold" font-family="Noto Sans JP,Yu Gothic,sans-serif">¥285M</text>
  <text x="168" y="121" font-size="7.5" fill="white" font-family="Noto Sans JP,Yu Gothic,sans-serif">総予算を超過 — 追加資金調達またはスコープ縮小が必要</text>
  <line x1="285" y1="10" x2="285" y2="155" stroke="#ddd" stroke-width="0.4"/>
  <line x1="410" y1="10" x2="410" y2="155" stroke="#ddd" stroke-width="0.4"/>
  <line x1="535" y1="10" x2="535" y2="155" stroke="#ddd" stroke-width="0.4"/>
</svg>

</div>

> 悲観的シナリオ¥285Mは**承認総予算¥245Mを¥40M超過**し、ゲート3で意思決定が必要となります：(a) 追加の資金調達ラウンド実施、(b) フェーズ3スコープ縮小（EV充電またはファイバー強化の延期等）、(c) 工程延長と建設段階分割のいずれか。絶対的失敗シナリオ（地域抵抗、ゲート1資金未確保等）は引き続き資金調達ゲートで管理し、EVMでは管理しません。

---

## 8. パフォーマンス閾値とエスカレーション

| 閾値 | SPI または CPI | 対応 |
|------|---------------|------|
| **グリーン** | 0.95 〜 1.10 | 通常報告；対応不要 |
| **イエロー** | 0.85 〜 0.94 | 代表理事に通知；2週間以内に回復計画を作成 |
| **オレンジ** | 0.75 〜 0.84 | 理事会への報告義務；選択肢付き回復計画を提示 |
| **レッド** | 0.75未満 | 正式な理事会審査；フェーズの再スコープまたはMR取崩しを検討 |

---

## 9. EVM報告サイクル

| 頻度 | 報告書 | 宛先 | 内容 |
|------|--------|------|------|
| **月次** | EVM状況報告 | 理事会・主要資金提供者 | PV/EV/AC表；SPI/CPI；SV/CV；EAC更新；課題 |
| **ゲート毎** | ゲート審査パッケージ | 理事会＋主要資金提供者 | 完全EVM審査；シナリオ予測；進行・中止判断 |
| **四半期** | ステークホルダー要約 | 村役場・アドバイザー | コスト・スケジュール状況；マイルストーン進捗 |
| **年次** | 年度末審査 | 全ステークホルダー | 完全財務報告；EVM監査；翌年基準値 |

---

## 10. 前提条件と制約

**前提条件**
- プロジェクト開始日：2026年4月1日（第1か月）
- 全フェーズ期間は祝日を含む暦月
- 各調査は単一ベンダーに発注（分割発注なし）
- フェーズ3建設費は2026年奈良県農村部建設指数に基づく。太陽光発電、EV充電、耐震改修については、商用ベンチマークに15〜25%の農村部動員プレミアムを上乗せ
- 為替レート前提（蘭系・国際コーポレートパートナー向け）：¥150/EUR

**制約条件**
- BAC ¥220Mは**上限**；ゲート3での確定資金なしにP3は着手不可
- マネジメント予備費の取崩しには理事会承認が必要
- データはJPY（円）で報告；外貨取引は取引日レートで換算
- フェーズ1フィージビリティスタディは**全体精度の最大の決定要因** — M9以前の全EACは不確実性が高い（±40%）

---

## 11. 制限事項と正直な注意書き

1. **第2か月時点のCPI・SPIは統計的に信頼性がありません。** ¥0.08Mの実績コストデータのみでは、指数はプロジェクト全体ではなくフェーズ0の特性を反映しています。フェーズ1コスト¥200〜300Mが確定した後に初めて信頼性が高まります。

2. **フェーズ3の予算レンジは広い。** ¥1.2億〜2.9億円というレンジは、建物状態（校舎改修だけで¥30〜100Mのレンジ）・機器調達・系統接続コストの不確実性を正直に反映しています。EVM基準値はWBS 5.0に¥177Mを使用し、¥27Mのフェーズ3予備費（18%）と¥25Mのマネジメント予備費がこのレンジを吸収します。

3. **資金調達ゲートが主要管理メカニズムです。** EVMはフェーズ内の効率を監視し、ゲートは次フェーズを開始するかどうかを制御します。

4. **フェーズ1フィージビリティスタディが基準値を大幅に改定します。** M9後に正式な基準値改訂（Rev.2）を行います。改訂後のフェーズ2・3予算は、日本の市場ベンチマークではなく、校舎構造調査結果とベンダー見積に基づくものとなります。

---

## 12. 基準値改訂方針

PMBは以下の場合に正式に改訂可能：
- フェーズ1フィージビリティスタディ完了後（M9での必須改訂）
- 確定資金が計画値と±20%以上乖離した場合
- 理事会承認のスコープ変更を反映する場合
- マネジメント予備費の取崩し時

各改訂は記録：旧基準値、新基準値、理由、承認者、日付。
改訂番号：
- **Rev.0**（v1.1、2026年4月）— 当初BAC ¥168M、計画見積に基づく
- **Rev.1**（v2.0、2026年5月）— 本書。BAC ¥220M、日本国内の実勢価格（太陽光、EV充電器、学校耐震改修、林業）と照合の上で再評価。フェーズ1フィージビリティスタディに先行する予防的修正。
- **Rev.2**（計画 M9、2026年12月）— フェーズ1完了後の改訂。フィージビリティスタディ結果とベンダー見積に基づく。**確定した地域脱炭素移行・再エネ推進交付金額も折り込む予定**（太陽光・蓄電池・EV・自営線設備費の補助率2/3〜3/4、村の官民連携経由）——¥28M〜¥53Mの資金ギャップを埋める最も具体的な道筋。出典：https://policies.env.go.jp/policy/roadmap/grants/ · https://www.env.go.jp/content/900470616.pdf

---

*Rob Oudendijk — YR-Design / Safecast*
*奈良県御杖村*
*2026年5月*
