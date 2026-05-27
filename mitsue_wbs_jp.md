<style>
  body { font-size: 9.5pt; line-height: 1.4; font-family: 'Noto Sans JP', 'Yu Gothic', 'Hiragino Sans', sans-serif; }
  h1 { font-size: 15pt; margin: 4pt 0 2pt; }
  h2 { font-size: 11pt; margin: 8pt 0 3pt; }
  h3 { font-size: 10pt; margin: 4pt 0 2pt; }
  h4 { font-size: 9.5pt; margin: 3pt 0 2pt; font-style: italic; }
  p, li { margin: 2pt 0; }
  table { font-size: 8.5pt; border-collapse: collapse; width: 100%; }
  th, td { border: 1px solid #ccc; padding: 3pt 5pt; }
  th { background: #f0f4ff; font-weight: bold; }
  tr:nth-child(even) { background: #f9f9f9; }
  blockquote { margin: 4pt 8pt; padding: 4pt 8pt; background: #f8f8f8; border-left: 3px solid #6796e6; }
  hr { margin: 6pt 0; }
  .page-break { page-break-after: always; break-after: page; }
  @media print { body { margin: 0; } }
</style>

<p align="right">Version: v2.3 (Baseline Rev 1) &nbsp;|&nbsp; Last modified: 2026-05-27</p>

---

# 御杖プロジェクト — 作業分解構造（WBS）
### フェーズ0〜3 · 2026年4月 – 2028年9月

---

## 1. 本書の読み方

WBSはプロジェクト全体のスコープを、管理可能な個別要素に分解したものです。**最下位レベル**の各要素（ワークパッケージ）は、明確な成果物・予算・担当者が定義された限定的な作業単位を表します。

**凡例：**
- WBSコードはドット記法：`1.0`＝第1レベル、`1.2`＝第2レベル、`1.2.3`＝第3レベル
- **予算**欄は計画見積を示す；レンジは残存不確実性を示す
- **担当者**は成果責任者（必ずしも実作業者ではない）
- **成果物**はその要素を完了とみなすために存在すべきもの
- 合計BAC = **¥220.0M** | マネジメント予備費（WBS対象外）= ¥25.0M
- **ベースライン Rev 1（2026年5月）** — 太陽光発電（¥20〜30万/kW）、学校耐震改修（¥20〜50万/㎡）、商用EV急速充電器（1基¥500〜600万）、林道整備など日本国内の実勢価格と照合し再評価。BACを¥1.68億から¥2.20億へ改定。

---

## 2. WBS サマリーツリー

```
0.0  御杖プロジェクト（フェーズ0〜3）                      ¥220.0M
 │
 ├── 1.0  プロジェクト管理・ガバナンス                      ¥15.0M
 │    ├── 1.1  事業推進・報告
 │    ├── 1.2  法務・会計・コンプライアンス
 │    └── 1.3  広報・翻訳・ウェブサイト
 │
 ├── 2.0  フェーズ0 — 準備期                               ¥0.25M
 │    ├── 2.1  地域ステークホルダーエンゲージメント
 │    ├── 2.2  憲章・書類作成
 │    └── 2.3  創設チームの特定
 │
 ├── 3.0  フェーズ1 — 基盤構築期                            ¥5.5M
 │    ├── 3.1  一般社団法人設立
 │    ├── 3.2  林業フィージビリティスタディ
 │    ├── 3.3  エネルギーシステム調査
 │    ├── 3.4  建物・敷地調査
 │    ├── 3.5  通信環境調査
 │    └── 3.6  運営基盤整備
 │
 ├── 4.0  フェーズ2 — 試験設計期                           ¥22.25M
 │    ├── 4.1  建物・構造設計
 │    ├── 4.2  エネルギーシステム設計
 │    ├── 4.3  データセンター・IT設計
 │    ├── 4.4  EV充電システム設計
 │    ├── 4.5  許認可・規制対応
 │    ├── 4.6  提携・土地所有者契約
 │    ├── 4.7  補助金申請
 │    ├── 4.8  スタッフ採用・研修
 │    ├── 4.9  ベンダー事前選定
 │    └── 4.10 フェーズ2予備費
 │
 └── 5.0  フェーズ3 — 試験建設期                          ¥177.0M
      ├── 5.1  校舎改修
      ├── 5.2  太陽光発電設置
      ├── 5.3  蓄電池システム
      ├── 5.4  EV充電インフラ
      ├── 5.5  データセンター設備
      ├── 5.6  林業作業
      ├── 5.7  光ファイバー接続強化
      ├── 5.8  試験・調整・稼働開始
      └── 5.9  フェーズ3予備費
```

---

<div style="page-break-inside:avoid; margin: 10pt 0">

**図1 — プロジェクト工程表（ガントビュー、2026年4月 – 2028年9月）**

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 425" style="width:100%;display:block">
  <rect x="140" y="5" width="530" height="22" fill="#f0f4ff" stroke="#ccc" stroke-width="0.5"/>
  <text x="140" y="20" text-anchor="middle" font-size="7" fill="#444" font-family="Noto Sans JP,Yu Gothic,sans-serif">26年4月</text>
  <text x="195" y="20" text-anchor="middle" font-size="7" fill="#444" font-family="Noto Sans JP,Yu Gothic,sans-serif">26年7月</text>
  <text x="250" y="20" text-anchor="middle" font-size="7" fill="#444" font-family="Noto Sans JP,Yu Gothic,sans-serif">26年10月</text>
  <text x="305" y="20" text-anchor="middle" font-size="7" fill="#444" font-family="Noto Sans JP,Yu Gothic,sans-serif">27年1月</text>
  <text x="359" y="20" text-anchor="middle" font-size="7" fill="#444" font-family="Noto Sans JP,Yu Gothic,sans-serif">27年4月</text>
  <text x="414" y="20" text-anchor="middle" font-size="7" fill="#444" font-family="Noto Sans JP,Yu Gothic,sans-serif">27年7月</text>
  <text x="469" y="20" text-anchor="middle" font-size="7" fill="#444" font-family="Noto Sans JP,Yu Gothic,sans-serif">27年10月</text>
  <text x="524" y="20" text-anchor="middle" font-size="7" fill="#444" font-family="Noto Sans JP,Yu Gothic,sans-serif">28年1月</text>
  <text x="578" y="20" text-anchor="middle" font-size="7" fill="#444" font-family="Noto Sans JP,Yu Gothic,sans-serif">28年4月</text>
  <text x="633" y="20" text-anchor="middle" font-size="7" fill="#444" font-family="Noto Sans JP,Yu Gothic,sans-serif">28年7月</text>
  <text x="670" y="20" text-anchor="middle" font-size="7" fill="#444" font-family="Noto Sans JP,Yu Gothic,sans-serif">28年9月</text>
  <line x1="140" y1="26" x2="140" y2="335" stroke="#ddd" stroke-width="0.5"/>
  <line x1="195" y1="26" x2="195" y2="335" stroke="#ddd" stroke-width="0.5"/>
  <line x1="250" y1="26" x2="250" y2="335" stroke="#ddd" stroke-width="0.5"/>
  <line x1="305" y1="26" x2="305" y2="335" stroke="#ddd" stroke-width="0.5"/>
  <line x1="359" y1="26" x2="359" y2="335" stroke="#ddd" stroke-width="0.5"/>
  <line x1="414" y1="26" x2="414" y2="335" stroke="#ddd" stroke-width="0.5"/>
  <line x1="469" y1="26" x2="469" y2="335" stroke="#ddd" stroke-width="0.5"/>
  <line x1="524" y1="26" x2="524" y2="335" stroke="#ddd" stroke-width="0.5"/>
  <line x1="578" y1="26" x2="578" y2="335" stroke="#ddd" stroke-width="0.5"/>
  <line x1="633" y1="26" x2="633" y2="335" stroke="#ddd" stroke-width="0.5"/>
  <line x1="670" y1="26" x2="670" y2="335" stroke="#ddd" stroke-width="0.5"/>
  <rect x="0" y="27" width="700" height="22" fill="#f8f9ff"/>
  <rect x="0" y="71" width="700" height="22" fill="#f8f9ff"/>
  <rect x="0" y="115" width="700" height="22" fill="#f8f9ff"/>
  <rect x="0" y="162" width="700" height="18" fill="#fffdf8"/>
  <rect x="0" y="183" width="700" height="18" fill="#fffdf8"/>
  <rect x="0" y="204" width="700" height="18" fill="#fffdf8"/>
  <rect x="0" y="225" width="700" height="18" fill="#fffdf8"/>
  <rect x="0" y="246" width="700" height="18" fill="#fffdf8"/>
  <rect x="0" y="267" width="700" height="18" fill="#fffdf8"/>
  <rect x="0" y="288" width="700" height="18" fill="#fffdf8"/>
  <text x="135" y="41" text-anchor="end" font-size="8.5" fill="#333" font-weight="bold" font-family="Noto Sans JP,Yu Gothic,sans-serif">フェーズ0</text>
  <text x="135" y="53" text-anchor="end" font-size="7" fill="#888" font-family="Noto Sans JP,Yu Gothic,sans-serif">準備期</text>
  <text x="135" y="85" text-anchor="end" font-size="8.5" fill="#333" font-weight="bold" font-family="Noto Sans JP,Yu Gothic,sans-serif">フェーズ1</text>
  <text x="135" y="97" text-anchor="end" font-size="7" fill="#888" font-family="Noto Sans JP,Yu Gothic,sans-serif">基盤構築 ¥5.5M</text>
  <text x="135" y="129" text-anchor="end" font-size="8.5" fill="#333" font-weight="bold" font-family="Noto Sans JP,Yu Gothic,sans-serif">フェーズ2</text>
  <text x="135" y="141" text-anchor="end" font-size="7" fill="#888" font-family="Noto Sans JP,Yu Gothic,sans-serif">試験設計 ¥22.25M</text>
  <text x="135" y="173" text-anchor="end" font-size="8" fill="#333" font-family="Noto Sans JP,Yu Gothic,sans-serif">5.7 光ファイバー</text>
  <text x="135" y="194" text-anchor="end" font-size="8" fill="#333" font-family="Noto Sans JP,Yu Gothic,sans-serif">5.1 校舎改修</text>
  <text x="135" y="215" text-anchor="end" font-size="8" fill="#333" font-family="Noto Sans JP,Yu Gothic,sans-serif">5.6 林業作業</text>
  <text x="135" y="236" text-anchor="end" font-size="8" fill="#333" font-family="Noto Sans JP,Yu Gothic,sans-serif">5.2+5.3 太陽光・蓄電池</text>
  <text x="135" y="257" text-anchor="end" font-size="8" fill="#333" font-family="Noto Sans JP,Yu Gothic,sans-serif">5.4 EV充電</text>
  <text x="135" y="278" text-anchor="end" font-size="8" fill="#333" font-family="Noto Sans JP,Yu Gothic,sans-serif">5.5 データセンター</text>
  <text x="135" y="299" text-anchor="end" font-size="8" fill="#333" font-family="Noto Sans JP,Yu Gothic,sans-serif">5.8 試験・調整</text>
  <!-- Phase bars -->
  <rect x="140" y="30" width="55" height="18" rx="3" fill="#6796e6"/>
  <text x="168" y="43" text-anchor="middle" font-size="7" fill="white" font-family="Noto Sans JP,Yu Gothic,sans-serif">M1–M3  ¥0.25M</text>
  <polygon points="195,27 200,38 195,49 190,38" fill="#e58520"/>
  <rect x="195" y="74" width="110" height="18" rx="3" fill="#4a7ac4"/>
  <text x="250" y="87" text-anchor="middle" font-size="7" fill="white" font-family="Noto Sans JP,Yu Gothic,sans-serif">M4–M9  ¥5.5M</text>
  <polygon points="305,71 310,82 305,93 300,82" fill="#e58520"/>
  <rect x="305" y="118" width="164" height="18" rx="3" fill="#e58520"/>
  <text x="387" y="131" text-anchor="middle" font-size="7" fill="white" font-family="Noto Sans JP,Yu Gothic,sans-serif">M10–M18  ¥22.25M</text>
  <polygon points="469,115 474,126 469,137 464,126" fill="#e58520"/>
  <!-- Sub-activity bars -->
  <rect x="396" y="163" width="128" height="13" rx="2" fill="#9fb8e8"/>
  <text x="460" y="173" text-anchor="middle" font-size="6.5" fill="#222" font-family="Noto Sans JP,Yu Gothic,sans-serif">早期着手 — NTTリードタイム6〜9ヶ月</text>
  <rect x="469" y="184" width="91" height="13" rx="2" fill="#d94f4f"/>
  <text x="515" y="194" text-anchor="middle" font-size="7" fill="white" font-family="Noto Sans JP,Yu Gothic,sans-serif">校舎改修 ¥38M</text>
  <rect x="469" y="205" width="146" height="13" rx="2" fill="#6aaa50"/>
  <text x="542" y="215" text-anchor="middle" font-size="7" fill="white" font-family="Noto Sans JP,Yu Gothic,sans-serif">林業作業 ¥25M</text>
  <rect x="487" y="226" width="110" height="13" rx="2" fill="#d94f4f" fill-opacity="0.8"/>
  <text x="542" y="236" text-anchor="middle" font-size="7" fill="white" font-family="Noto Sans JP,Yu Gothic,sans-serif">太陽光・蓄電池 ¥34M</text>
  <rect x="524" y="247" width="91" height="13" rx="2" fill="#d94f4f" fill-opacity="0.7"/>
  <text x="570" y="257" text-anchor="middle" font-size="7" fill="white" font-family="Noto Sans JP,Yu Gothic,sans-serif">EV充電 ¥15M</text>
  <rect x="542" y="268" width="110" height="13" rx="2" fill="#d94f4f" fill-opacity="0.6"/>
  <text x="597" y="278" text-anchor="middle" font-size="7" fill="white" font-family="Noto Sans JP,Yu Gothic,sans-serif">データセンター ¥20M</text>
  <rect x="633" y="289" width="37" height="13" rx="2" fill="#333"/>
  <text x="651" y="299" text-anchor="middle" font-size="7" fill="white" font-family="Noto Sans JP,Yu Gothic,sans-serif">試験¥8M</text>
  <polygon points="670,285 676,299 670,313 664,299" fill="#4aaa60"/>
  <!-- Status date line -->
  <line x1="158" y1="26" x2="158" y2="335" stroke="#e58520" stroke-width="1.5" stroke-dasharray="4,3"/>
  <text x="160" y="343" font-size="6.5" fill="#e58520" font-weight="bold" font-family="Noto Sans JP,Yu Gothic,sans-serif">▲ 現在</text>
  <!-- Legend -->
  <rect x="140" y="318" width="10" height="8" fill="#e58520" rx="1"/>
  <text x="154" y="326" font-size="7" fill="#444" font-family="Noto Sans JP,Yu Gothic,sans-serif">資金調達ゲート</text>
  <rect x="255" y="318" width="10" height="8" fill="#d94f4f" rx="1"/>
  <text x="269" y="326" font-size="7" fill="#444" font-family="Noto Sans JP,Yu Gothic,sans-serif">P3 建設工事</text>
  <rect x="360" y="318" width="10" height="8" fill="#6aaa50" rx="1"/>
  <text x="374" y="326" font-size="7" fill="#444" font-family="Noto Sans JP,Yu Gothic,sans-serif">林業（季節制約あり）</text>
  <rect x="490" y="318" width="10" height="8" fill="#9fb8e8" rx="1"/>
  <text x="504" y="326" font-size="7" fill="#444" font-family="Noto Sans JP,Yu Gothic,sans-serif">光ファイバー（P2→P3跨ぎ）</text>
  <polygon points="620,318 624,326 620,334 616,326" fill="#4aaa60"/>
  <text x="630" y="326" font-size="7" fill="#444" font-family="Noto Sans JP,Yu Gothic,sans-serif">収益ゲート4</text>
  <!-- ゲート判断フレームワーク -->
  <line x1="5" y1="340" x2="695" y2="340" stroke="#bbb" stroke-width="0.7"/>
  <text x="350" y="351" text-anchor="middle" font-size="8" font-weight="bold" fill="#333" font-family="Noto Sans JP,Yu Gothic,sans-serif">ゲート判断フレームワーク</text>
  <text x="5"   y="363" font-size="6.5" font-weight="bold" fill="#555" font-family="Noto Sans JP,Yu Gothic,sans-serif">ゲート</text>
  <text x="190" y="363" font-size="6.5" font-weight="bold" fill="#4aaa60" font-family="Noto Sans JP,Yu Gothic,sans-serif">✓ 通過 → 次フェーズ開始</text>
  <text x="445" y="363" font-size="6.5" font-weight="bold" fill="#c06010" font-family="Noto Sans JP,Yu Gothic,sans-serif">↩ 不通過 → 保留アクション</text>
  <line x1="5" y1="366" x2="695" y2="366" stroke="#ddd" stroke-width="0.5"/>
  <text x="5"   y="377" font-size="6.5" fill="#e58520" font-weight="bold" font-family="Noto Sans JP,Yu Gothic,sans-serif">ゲート1 · M3 · ¥300〜800万</text>
  <text x="190" y="377" font-size="6.5" fill="#333" font-family="Noto Sans JP,Yu Gothic,sans-serif">フェーズ1開始；実現可能性調査・チーム契約</text>
  <text x="445" y="377" font-size="6.5" fill="#555" font-family="Noto Sans JP,Yu Gothic,sans-serif">保留・再提案；M+3で再検討</text>
  <text x="5"   y="390" font-size="6.5" fill="#e58520" font-weight="bold" font-family="Noto Sans JP,Yu Gothic,sans-serif">ゲート2 · M9 · ¥3,000〜5,000万</text>
  <text x="190" y="390" font-size="6.5" fill="#333" font-family="Noto Sans JP,Yu Gothic,sans-serif">フェーズ2開始；詳細設計・許認可・光ファイバー発注</text>
  <text x="445" y="390" font-size="6.5" fill="#555" font-family="Noto Sans JP,Yu Gothic,sans-serif">縮小検討；補助金再申請；P1を3〜6か月延長</text>
  <text x="5"   y="403" font-size="6.5" fill="#e58520" font-weight="bold" font-family="Noto Sans JP,Yu Gothic,sans-serif">ゲート3 · M18 · ¥8,000〜2億</text>
  <text x="190" y="403" font-size="6.5" fill="#333" font-family="Noto Sans JP,Yu Gothic,sans-serif">フェーズ3開始；建設フル動員</text>
  <text x="445" y="403" font-size="6.5" fill="#555" font-family="Noto Sans JP,Yu Gothic,sans-serif">段階的建設；橋渡し融資；P2±6か月延長</text>
  <text x="5"   y="416" font-size="6.5" fill="#4aaa60" font-weight="bold" font-family="Noto Sans JP,Yu Gothic,sans-serif">ゲート4 · M30 · 収益開始?</text>
  <text x="190" y="416" font-size="6.5" fill="#333" font-family="Noto Sans JP,Yu Gothic,sans-serif">フェーズ4運営；商業契約・EV充電一般開放</text>
  <text x="445" y="416" font-size="6.5" fill="#555" font-family="Noto Sans JP,Yu Gothic,sans-serif">パイロット継続；企業再提案；EAC見直し</text>
</svg>

</div>

---

## 3. WBS辞書 — 詳細

---

### 1.0 プロジェクト管理・ガバナンス — ¥15.0M

全フェーズにわたるオーバーヘッド費用。リーダーシップ、法的コンプライアンス、対外広報を含みます。

#### 1.1 事業推進・報告 — ¥8.0M

| 項目 | 内容 |
|------|------|
| スコープ | 代表理事による監督；月次EVM報告；理事会運営；ステークホルダーへの説明；リスク管理簿の維持 |
| 担当者 | 代表理事 |
| 予算 | ¥8.0M（30か月平均¥26.5万/月） |
| 成果物 | 月次EVM報告書；ゲート審査パッケージ；年次ステークホルダー報告書 |
| 受入基準 | 各ゲート審査パッケージの理事会承認 |

#### 1.2 法務・会計・コンプライアンス — ¥4.0M

| 項目 | 内容 |
|------|------|
| スコープ | 補助金・許認可対応行政書士；年次税務申告税理士；主要契約の法的確認；継続的コンプライアンス対応 |
| 担当者 | 財務・運営担当理事 |
| 予算 | ¥4.0M |
| 成果物 | 監査済み年次決算書；税務申告書；主要契約の法的確認サインオフ |

#### 1.3 広報・翻訳・ウェブサイト — ¥3.0M

| 項目 | 内容 |
|------|------|
| スコープ | 日英バイリンガルプロジェクトウェブサイト；プレス・ステークホルダー向け資料；全公式書類の翻訳；年次報告書デザイン |
| 担当者 | テクノロジー担当理事 |
| 予算 | ¥3.0M |
| 成果物 | フェーズ1終了までに稼働するバイリンガルウェブサイト；全主要書類の翻訳版 |

---

### 2.0 フェーズ0 — 準備期 — ¥0.25M

*期間：第1〜3か月（2026年4〜6月）*

低予算だが重要性の高いフェーズ。主要通貨は時間と信頼であり、金銭ではありません。公的コミットメントを行う前に社会的承認を確立することが目的です。

#### 2.1 地域ステークホルダーエンゲージメント — ¥0.10M

| 項目 | 内容 |
|------|------|
| スコープ | 村長・議員・菅野および近隣集落の自治会長との非公式会合（傾聴中心） |
| 担当者 | Rob Oudendijk ＋ 日本人共同設立者（確定後） |
| 予算 | ¥0.10M（交通費・接待・資料） |
| 成果物 | 参加者・主要反応の会合記録；村リーダーの姿勢まとめ文書 |
| 受入基準 | 村長への情報共有；積極的反対意見なし |

#### 2.2 憲章・書類作成 — ¥0.10M

| 項目 | 内容 |
|------|------|
| スコープ | 日英バイリンガル2ページ憲章草案；プロジェクト概要書（日本語）；コアコンセプト書類の翻訳 |
| 担当者 | Rob Oudendijk |
| 予算 | ¥0.10M（翻訳費・行政書士初期相談費） |
| 成果物 | 憲章草案（日本語・英語）；翻訳済みプロジェクト概要書 |
| 受入基準 | 創設チームメンバーによる憲章確認・合意 |

#### 2.3 創設チームの特定 — ¥0.05M

| 項目 | 内容 |
|------|------|
| スコープ | 3〜5名の創設チームメンバーの特定と口頭確約の取得；農村に信頼基盤を持つ日本人共同設立者を最低1名含めること |
| 担当者 | Rob Oudendijk |
| 予算 | ¥0.05M（ネットワーキング・交通費） |
| 成果物 | 口頭確約を文書化した創設チーム名簿 |
| 受入基準 | 代表理事候補の特定 |

> **フェーズ0ゲート基準：** 創設チームの口頭合意；村リーダーへの情報共有・反対意見なし；憲章草案完成。

---

### 3.0 フェーズ1 — 基盤構築期 — ¥5.5M

*期間：第4〜9か月（2026年7〜12月）*

構造的に最も重要なフェーズ。ここで作成されるフィージビリティスタディが、以降の全資金調達申請の信頼性を左右します。手を抜くことは将来の損失につながります。

#### 3.1 一般社団法人設立 — ¥0.5M

| 項目 | 内容 |
|------|------|
| スコープ | 一般社団法人設立；公証済み定款；法務局登記；銀行口座開設；会計システム設置（弥生会計等） |
| 担当者 | 財務・運営担当理事 |
| 予算 | ¥0.5M（登録税¥11万＋公証費¥5万＋行政書士¥30万＋会計設置¥4万） |
| 成果物 | 設立証明書；登録事務所住所；稼働中の銀行口座；会計システム稼働 |
| 受入基準 | 法務局登記確認；初回理事会決議記録 |

#### 3.2 林業フィージビリティスタディ — ¥1.5M

| 項目 | 内容 |
|------|------|
| スコープ | 在来種転換を目的とした候補杉林の現地調査；急峻地形からの伐採・搬出コスト分析；在来種森林再生計画および樹種選定；炭素固定量見積 |
| 担当者 | 林業・地域担当理事 |
| 予算 | ¥1.5M（¥1.5〜3Mレンジの下限） |
| 成果物 | 林業調査報告書（日本語）；バイリンガルエグゼクティブサマリー；土地区画地図 |
| 受入基準 | アドバイザリーボード承認；J-Credit事前審査結果 |

#### 3.3 エネルギーシステム調査 — ¥1.5M

| 項目 | 内容 |
|------|------|
| スコープ | 学校敷地の太陽光発電ポテンシャル；蓄電池サイジング；系統接続オプション；FIT/FIP適格性評価；EV充電負荷モデリング；停電時レジリエンスシナリオ |
| 担当者 | テクノロジー担当理事 |
| 予算 | ¥1.5M（¥2〜4Mレンジの下限） |
| 成果物 | エネルギー調査報告書；太陽光発電量モデル；蓄電池サイジング推奨書；FIT/FIP適格性確認書 |
| 受入基準 | アドバイザリーボード承認；METI事前協議完了 |

#### 3.4 建物・敷地調査 — ¥0.8M

| 項目 | 内容 |
|------|------|
| スコープ | 御杖小学校の構造状況調査；耐震基準（新耐震基準）適合評価；データセンター利用に必要な改修内容の特定；用途地域確認 |
| 担当者 | テクノロジー担当理事 |
| 予算 | ¥0.8M |
| 成果物 | 構造調査報告書；耐震適合性要約；改修スコープ概要；用途地域確認書 |
| 受入基準 | 理事会での報告書承認；フェーズ3改修予算レンジ確認 |

#### 3.5 通信環境調査 — ¥0.4M

| 項目 | 内容 |
|------|------|
| スコープ | 御杖村への現行光ファイバー容量；増強要件とコスト；NTT協議；衛星・マイクロ波バックアップオプション |
| 担当者 | テクノロジー担当理事 |
| 予算 | ¥0.4M |
| 成果物 | 通信ギャップ分析；NTT協議記録；増強費用見積；バックアップオプション検討書 |
| 受入基準 | 報告書承認；フェーズ3光ファイバー増強予算確認 |

#### 3.6 運営基盤整備 — ¥0.8M

| 項目 | 内容 |
|------|------|
| スコープ | アドバイザリーボードの正式化（伊藤穰一、Ray Ozzieほかから承諾書取得）；バイリンガルウェブサイト公開；資金調達パイプライン文書化；補助金カレンダー設定 |
| 担当者 | 代表理事 |
| 予算 | ¥0.8M |
| 成果物 | 署名済みアドバイザリーボード承諾書；ウェブサイト公開；フェーズ2補助金申請カレンダー |
| 受入基準 | 理事会によるウェブサイト確認；アドバイザリーボードの書面確認 |

> **フェーズ1ゲート基準：** 法人登記完了；全4件の調査報告書承認；¥300万〜800万円確保；御杖村役場からの支持表明書取得。

---

<div class="page-break"></div>

### 4.0 フェーズ2 — 試験設計期 — ¥22.25M

*期間：第10〜18か月（2027年1〜9月）*

フィージビリティスタディを設計の現実へと変換するフェーズ。ここで提出する許認可申請がフェーズ3開始の長期調達品目となります。

#### 4.1 建物・構造設計 — ¥2.0M

| 項目 | 内容 |
|------|------|
| スコープ | 校舎改修の完全建築図面（棟1区画）；耐震補強仕様；データセンター棟の機械・電気・配管設計；建築確認申請書類 |
| 担当者 | テクノロジー担当理事 |
| 予算 | ¥2.0M |
| 成果物 | 検印済み建築図面；MEP仕様書；建築確認申請書提出 |
| 受入基準 | 奈良県当局による申請受理 |

#### 4.2 エネルギーシステム設計 — ¥2.0M

| 項目 | 内容 |
|------|------|
| スコープ | 太陽光発電アレイ・蓄電池・EV充電統合・系統接続の詳細設計；機器仕様；潮流解析；FIT/FIP申請 |
| 担当者 | テクノロジー担当理事 |
| 予算 | ¥2.0M |
| 成果物 | エネルギーシステム詳細設計パッケージ；機器仕様書；FIT/FIP申請書提出 |
| 受入基準 | METI FIT/FIP申請受理番号取得 |
| 注意 | METIのFIT/FIP登録と建築確認がクリティカルパス — M12（2027年3月）までに申請必須 |

#### 4.3 データセンター・IT設計 — ¥1.0M

| 項目 | 内容 |
|------|------|
| スコープ | サーバー室レイアウト；サーバー10〜20台向け電源・冷却設計；ネットワーク構成；APPI準拠計画；サイバーセキュリティフレームワーク |
| 担当者 | テクノロジー担当理事 |
| 予算 | ¥1.0M |
| 成果物 | データセンター設計パッケージ；ネットワークトポロジー図；セキュリティフレームワーク文書 |

#### 4.4 EV充電システム設計 — ¥1.0M

| 項目 | 内容 |
|------|------|
| スコープ | 4基充電ステーションのレイアウト；系統統合設計；消防・電気設備許認可申請準備；標識・アクセス計画 |
| 担当者 | テクノロジー担当理事 |
| 予算 | ¥1.0M |
| 成果物 | EV充電設計図面；許認可事前申請提出 |

#### 4.5 許認可・規制対応 — ¥3.5M

| 項目 | 内容 |
|------|------|
| スコープ | 全機関への許認可申請管理：建築確認（建築基準法）、伐採届出（森林法）、FIT/FIP登録（METI）、EV充電安全許可（消防・電気）、環境影響調整 |
| 担当者 | 財務・運営担当理事（行政書士サポート） |
| 予算 | ¥3.5M（申請1件あたり¥20万〜50万の行政書士費用を含む） |
| 成果物 | 全許認可申請提出；建築確認取得；FIT/FIP登録確認 |
| 受入基準 | フェーズ3調達開始前に主要許認可取得 |

#### 4.6 提携・土地所有者契約 — ¥1.5M

| 項目 | 内容 |
|------|------|
| スコープ | 杉伐採権の土地所有者契約交渉・締結；主要技術・機関パートナーとの基本合意書；村役場との協力協定 |
| 担当者 | 代表理事 |
| 予算 | ¥1.5M（法的文書作成・交渉促進・翻訳） |
| 成果物 | 土地所有者との伐採契約2件以上；村役場MOU署名；企業パートナーMOU1件以上 |

#### 4.7 補助金申請 — ¥2.0M

| 項目 | 内容 |
|------|------|
| スコープ | 主要補助金の申請書作成・提出：地方創生関係交付金、林野庁補助金、NEDO、METI、奈良県、日本財団、地球環境基金 |
| 担当者 | 財務・運営担当理事（専門行政書士サポート） |
| 予算 | ¥2.0M（申請4〜6件；行政書士費用¥20万〜50万/件） |
| 成果物 | 最低4件の補助金申請提出；フェーズ2末時点で申請中の補助金¥3,000万以上 |

#### 4.8 スタッフ採用・研修 — ¥6.0M

| 項目 | 内容 |
|------|------|
| スコープ | 初期パートタイムスタッフ2〜3名採用（プロジェクトコーディネーター、運営・管理、地域林業連絡員）；研修・業務文書化 |
| 担当者 | 代表理事 |
| 予算 | ¥6.0M（9か月×3名×平均¥22万/月） |
| 成果物 | 2〜3名スタッフの雇用契約；研修完了；主要業務文書化 |

#### 4.9 ベンダー事前選定 — ¥1.5M

| 項目 | 内容 |
|------|------|
| スコープ | 各カテゴリーのベンダー候補絞り込みと事前選定：建設施工業者、太陽光・蓄電池サプライヤー、データセンター機器、EV充電設備；フェーズ3調達向け確定見積取得 |
| 担当者 | テクノロジー担当理事 |
| 予算 | ¥1.5M |
| 成果物 | カテゴリー別ベンダー候補リスト；確定見積取得；フェーズ3調達計画 |
| 受入基準 | ゲート3前にフェーズ3 WBS 5.x予算をEVM基準値の±15%以内で確認 |

#### 4.10 フェーズ2予備費 — ¥1.75M

| 項目 | 内容 |
|------|------|
| スコープ | フェーズ2コスト差異への備え（許認可費用超過、設計追加修正、補助金申請費用超過等） |
| 担当者 | 代表理事 |
| 予算 | ¥1.75M（フェーズ2直接費の約8%） |
| 取崩条件 | 代表理事承認；特定された差異に対してのみ取崩し可 |

> **フェーズ2ゲート基準：** ¥3,000万〜5,000万円確保；詳細設計完了；主要許認可取得（または申請受理済み）；スタッフ2名以上就任。

---

### 5.0 フェーズ3 — 試験建設期 — ¥177.0M

*期間：第19〜30か月（2027年10月〜2028年9月）*

最大かつ最も複雑なフェーズ。ピーク支出は22〜27か月目。全作業パッケージは相互依存関係にあります。

**作業順序：**
```
5.1 校舎改修 → 5.5 データセンター設備
5.2 太陽光 + 5.3 蓄電池 → 5.4 EV充電（調整）
5.6 林業作業 → 独立トラック（季節・天候依存）
5.7 光ファイバー → P2早期着手（NTTリードタイム長）
5.8 試験・調整 → 最終2か月
```

#### 5.1 校舎改修 — ¥38.0M

| 項目 | 内容 |
|------|------|
| スコープ | 棟1区画の耐震補強；データセンター・執務室利用のための内装改修；MEP設備（電源分電、冷却、スプリンクラー）；バリアフリー入口・厚生施設；外装防水工事 |
| 担当者 | テクノロジー担当理事 |
| 予算 | ¥38.0M |
| 成果物 | 建築基準法適合証明書付き改修済み棟；施工業者からの引渡し；パンチリスト完了 |
| 主要リスク | 予期せぬ構造上の問題；奈良県農村部における労働力不足 |

#### 5.2 太陽光発電設置 — ¥22.0M

| 項目 | 内容 |
|------|------|
| スコープ | 屋根置き太陽光発電（約100kW）；パワーコンディショナー；監視システム；系統接続設備；試運転・FIT/FIP引渡し書類 |
| 担当者 | テクノロジー担当理事 |
| 予算 | ¥22.0M（農村プレミアム含む約¥220K/kW設置） |
| 成果物 | 系統連系済み太陽光発電システム；FIT/FIP接続協定；監視ダッシュボード稼働 |

#### 5.3 蓄電池システム — ¥12.0M *（フィージビリティスタディでの確認が条件）*

| 項目 | 内容 |
|------|------|
| スコープ | 重要施設の12〜48時間停電バックアップに対応するリチウムイオン蓄電池；BMS（電池管理システム）；太陽光・系統との統合；安全認証。**判断ゲート：フェーズ1エネルギーフィージビリティスタディで経済的・運用的な妥当性が確認されることが本パッケージ着手の条件。** |
| 担当者 | テクノロジー担当理事 |
| 予算 | ¥12.0M |
| 成果物 | 設置・試運転・安全認証済み蓄電池システム；停電模擬試験合格 |
| 受入基準 | 消防安全証明書；設計負荷での48時間バックアップ試験 |

#### 5.4 EV充電インフラ — ¥15.0M

| 項目 | 内容 |
|------|------|
| スコープ | EV充電ステーション4基（AC普通充電・DC急速充電の組み合わせ）；ケーブル配管の土木工事；決済・管理ソフトウェア；標識；安全認証；公開 |
| 担当者 | テクノロジー担当理事 |
| 予算 | ¥15.0M |
| 成果物 | 一般公開済み4基の充電ステーション；決済システム稼働；消防・電気設備許可取得 |
| 受入基準 | 一般公開イベント；村役場による受入れ |

#### 5.5 データセンター設備 — ¥20.0M

| 項目 | 内容 |
|------|------|
| スコープ | サーバーラック・ハードウェア（10〜20台、エッジコンピューティング重点）；精密冷却；構造化配線；蓄電池システムとのUPS統合；ネットワーク機器；APPI準拠セキュリティ制御；リモート監視 |
| 担当者 | テクノロジー担当理事 |
| 予算 | ¥20.0M |
| 成果物 | 初の有料ワークロードを受け入れるデータセンター稼働；監視ダッシュボード；APPIコンプライアンス文書 |
| 受入基準 | 初の商業ホスティング契約締結；稼働率監視稼働 |

#### 5.6 林業作業 — ¥25.0M

| 項目 | 内容 |
|------|------|
| スコープ | 署名済み土地所有者契約に基づく杉5〜10ha伐採；材木は用材へ加工；在来種植栽開始；林道・排水整備；J-Credit申請書類作成 |
| 担当者 | 林業・地域担当理事 |
| 予算 | ¥25.0M |
| 成果物 | 伐採完了報告書；植栽計画実施；最初のJ-Credit申請提出 |
| 主要リスク | 季節的なアクセス制約（台風シーズンM19〜M23回避）；急峻地形への特殊機材 |

#### 5.7 光ファイバー接続強化 — ¥10.0M

| 項目 | 内容 |
|------|------|
| スコープ | NTTおよび地域ISPとの協議による御杖村向け光ファイバー容量増強；学校敷地への専用ダークファイバーまたは増強賃借回線設置；マイクロ波バックアップリンク設置 |
| 担当者 | テクノロジー担当理事 |
| 予算 | ¥10.0M |
| 成果物 | 帯域幅増強確認（目標：学校敷地への1Gbps対称以上）；バックアップリンク稼働；NTT SLA締結 |
| 注意 | NTT協議は6〜9か月のリードタイムが必要 — フェーズ2（M15まで）に着手必須 |

#### 5.8 試験・調整・稼働開始 — ¥8.0M

| 項目 | 内容 |
|------|------|
| スコープ | フェーズ3全要素の統合システム試験；パンチリスト解消；スタッフ研修；文書最終化；一般公開イベント；フェーズ4運営引渡し |
| 担当者 | 代表理事 |
| 予算 | ¥8.0M |
| 成果物 | 全システム試験・稼働確認；スタッフ研修完了；パンチリスト完了；フェーズ4運営計画承認；公開イベント開催 |
| 受入基準 | フェーズ3完了の理事会承認；フェーズ4運営計画承認 |

#### 5.9 フェーズ3予備費 — ¥27.0M

| 項目 | 内容 |
|------|------|
| スコープ | フェーズ3コスト差異への備え（主に5.1の構造上の問題、機器費用の変動、農村部人件費プレミアム、季節的遅延） |
| 担当者 | 代表理事 |
| 予算 | ¥27.0M（フェーズ3直接費の約18%） |
| 取崩条件 | ¥500万以下は代表理事承認；¥500万超は理事会承認が必要 |

> **フェーズ3ゲート基準（ゲート4）：** 全システム稼働；初の商業データセンター契約締結；EV充電一般公開；林業伐採開始；フェーズ4計画理事会承認。

---

## 4. 予算サマリー

| WBS | 項目 | 予算（¥M） | BAC比率 |
|-----|------|------------|---------|
| 1.0 | プロジェクト管理・ガバナンス | 15.00 | 6.8% |
| 2.0 | フェーズ0 — 準備期 | 0.25 | 0.1% |
| 3.0 | フェーズ1 — 基盤構築期 | 5.50 | 2.5% |
| 4.0 | フェーズ2 — 試験設計期 | 22.25 | 10.1% |
| 5.0 | フェーズ3 — 試験建設期 | 177.00 | 80.5% |
| | **合計 BAC（PMB）** | **220.00** | **100%** |
| | マネジメント予備費（PMB対象外） | 25.00 | — |
| | **総プロジェクト予算** | **245.00** | — |

<div style="page-break-inside:avoid; margin: 10pt 0">

**図2 — WBS要素別予算**

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 195" style="width:100%;display:block">
  <!-- scale: 500px = ¥245M → 2.041px/¥1M; bars from x=195 to x=695 -->
  <rect x="0" y="5" width="700" height="24" fill="#f0f4ff"/>
  <text x="190" y="21" text-anchor="end" font-size="8.5" fill="#333" font-weight="bold" font-family="Noto Sans JP,Yu Gothic,sans-serif">PM・ガバナンス</text>
  <rect x="195" y="8" width="31" height="16" rx="2" fill="#9fb8e8"/>
  <text x="229" y="20" font-size="7.5" fill="#333" font-family="Noto Sans JP,Yu Gothic,sans-serif">¥15M（6.8%）</text>
  <rect x="0" y="30" width="700" height="24" fill="#ffffff"/>
  <text x="190" y="46" text-anchor="end" font-size="8.5" fill="#333" font-weight="bold" font-family="Noto Sans JP,Yu Gothic,sans-serif">フェーズ0 — 準備期</text>
  <rect x="195" y="33" width="6" height="16" rx="2" fill="#6796e6" fill-opacity="0.4"/>
  <text x="204" y="45" font-size="7.5" fill="#333" font-family="Noto Sans JP,Yu Gothic,sans-serif">¥0.25M（0.1%）</text>
  <rect x="0" y="55" width="700" height="24" fill="#f0f4ff"/>
  <text x="190" y="71" text-anchor="end" font-size="8.5" fill="#333" font-weight="bold" font-family="Noto Sans JP,Yu Gothic,sans-serif">フェーズ1 — 基盤構築期</text>
  <rect x="195" y="58" width="11" height="16" rx="2" fill="#6796e6"/>
  <text x="209" y="70" font-size="7.5" fill="#333" font-family="Noto Sans JP,Yu Gothic,sans-serif">¥5.5M（2.5%）</text>
  <rect x="0" y="80" width="700" height="24" fill="#ffffff"/>
  <text x="190" y="96" text-anchor="end" font-size="8.5" fill="#333" font-weight="bold" font-family="Noto Sans JP,Yu Gothic,sans-serif">フェーズ2 — 試験設計期</text>
  <rect x="195" y="83" width="45" height="16" rx="2" fill="#e58520"/>
  <text x="243" y="95" font-size="7.5" fill="#333" font-family="Noto Sans JP,Yu Gothic,sans-serif">¥22.25M（10.1%）</text>
  <rect x="0" y="105" width="700" height="24" fill="#f0f4ff"/>
  <text x="190" y="121" text-anchor="end" font-size="8.5" fill="#333" font-weight="bold" font-family="Noto Sans JP,Yu Gothic,sans-serif">フェーズ3 — 試験建設期</text>
  <rect x="195" y="108" width="361" height="16" rx="2" fill="#d94f4f"/>
  <text x="376" y="120" text-anchor="middle" font-size="8.5" fill="white" font-weight="bold" font-family="Noto Sans JP,Yu Gothic,sans-serif">¥177M — BAC比率 80.5%</text>
  <rect x="0" y="130" width="700" height="24" fill="#f8f8f8"/>
  <text x="190" y="146" text-anchor="end" font-size="8.5" fill="#888" font-family="Noto Sans JP,Yu Gothic,sans-serif">マネジメント予備費（PMB対象外）</text>
  <rect x="195" y="133" width="51" height="16" rx="2" fill="#ccc"/>
  <text x="249" y="145" font-size="7.5" fill="#666" font-family="Noto Sans JP,Yu Gothic,sans-serif">¥25M — 取崩しには理事会承認が必要</text>
  <rect x="0" y="155" width="700" height="28" fill="#e8eeff"/>
  <text x="190" y="173" text-anchor="end" font-size="9" fill="#333" font-weight="bold" font-family="Noto Sans JP,Yu Gothic,sans-serif">総プロジェクト予算</text>
  <rect x="195" y="158" width="500" height="18" rx="2" fill="#4a7ac4"/>
  <text x="445" y="171" text-anchor="middle" font-size="9" fill="white" font-weight="bold" font-family="Noto Sans JP,Yu Gothic,sans-serif">¥245M 総承認予算（BAC ¥220M + 予備費 ¥25M）</text>
  <line x1="195" y1="185" x2="695" y2="185" stroke="#bbb" stroke-width="0.5"/>
  <text x="195" y="193" font-size="7" fill="#888" font-family="Noto Sans JP,Yu Gothic,sans-serif">0</text>
  <text x="297" y="193" text-anchor="middle" font-size="7" fill="#888" font-family="Noto Sans JP,Yu Gothic,sans-serif">5,000万円</text>
  <text x="399" y="193" text-anchor="middle" font-size="7" fill="#888" font-family="Noto Sans JP,Yu Gothic,sans-serif">1億円</text>
  <text x="501" y="193" text-anchor="middle" font-size="7" fill="#888" font-family="Noto Sans JP,Yu Gothic,sans-serif">1億5,000万円</text>
  <text x="603" y="193" text-anchor="middle" font-size="7" fill="#888" font-family="Noto Sans JP,Yu Gothic,sans-serif">2億円</text>
  <text x="695" y="193" text-anchor="middle" font-size="7" fill="#888" font-family="Noto Sans JP,Yu Gothic,sans-serif">2億4,500万円</text>
</svg>

</div>

### コストカテゴリー別予算（全フェーズ合計）

| カテゴリー | 予算（¥M） | 主な内容 |
|-----------|------------|---------|
| 機器・ハードウェア | ¥69.0M | 太陽光、蓄電池、EV充電器、サーバー、ネットワーク機器 |
| 建設・土木 | ¥48.0M | 校舎改修、敷地工事、EV・光ファイバー土木工事 |
| 予備費 | ¥28.75M | フェーズ2・3予備費 |
| 生態・林業 | ¥25.0M | 伐採作業、植栽、林道整備 |
| 人件費・運営 | ¥22.0M | PMチーム、スタッフ、アドバイザリーボード |
| 調査・設計 | ¥13.0M | フィージビリティスタディ、詳細設計、IT設計 |
| 許認可・コンプライアンス | ¥6.5M | 行政書士費用、許認可申請、法務 |
| 広報 | ¥3.0M | ウェブサイト、翻訳、デザイン |
| その他 | ¥4.75M | 会計、銀行、研修、公開イベント |
| **合計 BAC** | **¥220.0M** | |

<div style="page-break-inside:avoid; margin: 10pt 0">

**図3 — コストカテゴリー別予算内訳**

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 250" style="width:100%;display:block">
  <!-- scale: 400px = ¥70M (max) → 5.714px/¥1M; bars from x=205 to x=605 -->
  <rect x="0" y="5" width="700" height="22" fill="#f0f4ff"/>
  <text x="200" y="19" text-anchor="end" font-size="8" fill="#333" font-family="Noto Sans JP,Yu Gothic,sans-serif">機器・ハードウェア</text>
  <rect x="205" y="7" width="394" height="14" rx="2" fill="#d94f4f"/>
  <text x="604" y="18" text-anchor="end" font-size="8" fill="#333" font-family="Noto Sans JP,Yu Gothic,sans-serif">¥69M</text>
  <rect x="0" y="28" width="700" height="22" fill="#fff"/>
  <text x="200" y="42" text-anchor="end" font-size="8" fill="#333" font-family="Noto Sans JP,Yu Gothic,sans-serif">建設・土木</text>
  <rect x="205" y="30" width="274" height="14" rx="2" fill="#c04040"/>
  <text x="484" y="42" font-size="8" fill="#333" font-family="Noto Sans JP,Yu Gothic,sans-serif">¥48M</text>
  <rect x="0" y="51" width="700" height="22" fill="#f0f4ff"/>
  <text x="200" y="65" text-anchor="end" font-size="8" fill="#333" font-family="Noto Sans JP,Yu Gothic,sans-serif">予備費（P2+P3）</text>
  <rect x="205" y="53" width="164" height="14" rx="2" fill="#aaa"/>
  <text x="374" y="65" font-size="8" fill="#333" font-family="Noto Sans JP,Yu Gothic,sans-serif">¥28.75M</text>
  <rect x="0" y="74" width="700" height="22" fill="#fff"/>
  <text x="200" y="88" text-anchor="end" font-size="8" fill="#333" font-family="Noto Sans JP,Yu Gothic,sans-serif">生態・林業</text>
  <rect x="205" y="76" width="143" height="14" rx="2" fill="#4aaa50"/>
  <text x="352" y="88" font-size="8" fill="#333" font-family="Noto Sans JP,Yu Gothic,sans-serif">¥25M</text>
  <rect x="0" y="97" width="700" height="22" fill="#f0f4ff"/>
  <text x="200" y="111" text-anchor="end" font-size="8" fill="#333" font-family="Noto Sans JP,Yu Gothic,sans-serif">人件費・運営</text>
  <rect x="205" y="99" width="126" height="14" rx="2" fill="#6796e6"/>
  <text x="335" y="111" font-size="8" fill="#333" font-family="Noto Sans JP,Yu Gothic,sans-serif">¥22M</text>
  <rect x="0" y="120" width="700" height="22" fill="#fff"/>
  <text x="200" y="134" text-anchor="end" font-size="8" fill="#333" font-family="Noto Sans JP,Yu Gothic,sans-serif">調査・設計</text>
  <rect x="205" y="122" width="74" height="14" rx="2" fill="#4a7ac4"/>
  <text x="284" y="134" font-size="8" fill="#333" font-family="Noto Sans JP,Yu Gothic,sans-serif">¥13M</text>
  <rect x="0" y="143" width="700" height="22" fill="#f0f4ff"/>
  <text x="200" y="157" text-anchor="end" font-size="8" fill="#333" font-family="Noto Sans JP,Yu Gothic,sans-serif">許認可・コンプライアンス</text>
  <rect x="205" y="145" width="37" height="14" rx="2" fill="#9fb8e8"/>
  <text x="246" y="157" font-size="8" fill="#333" font-family="Noto Sans JP,Yu Gothic,sans-serif">¥6.5M</text>
  <rect x="0" y="166" width="700" height="22" fill="#fff"/>
  <text x="200" y="180" text-anchor="end" font-size="8" fill="#333" font-family="Noto Sans JP,Yu Gothic,sans-serif">その他・雑費</text>
  <rect x="205" y="168" width="27" height="14" rx="2" fill="#bbb"/>
  <text x="236" y="180" font-size="8" fill="#333" font-family="Noto Sans JP,Yu Gothic,sans-serif">¥4.75M</text>
  <rect x="0" y="189" width="700" height="22" fill="#f0f4ff"/>
  <text x="200" y="203" text-anchor="end" font-size="8" fill="#333" font-family="Noto Sans JP,Yu Gothic,sans-serif">広報・ウェブサイト</text>
  <rect x="205" y="191" width="17" height="14" rx="2" fill="#c8d8f0"/>
  <text x="226" y="203" font-size="8" fill="#333" font-family="Noto Sans JP,Yu Gothic,sans-serif">¥3.0M</text>
  <line x1="205" y1="215" x2="605" y2="215" stroke="#bbb" stroke-width="0.5"/>
  <text x="205" y="224" font-size="7" fill="#888" font-family="Noto Sans JP,Yu Gothic,sans-serif">0</text>
  <text x="262" y="224" text-anchor="middle" font-size="7" fill="#888" font-family="Noto Sans JP,Yu Gothic,sans-serif">1,000万</text>
  <text x="319" y="224" text-anchor="middle" font-size="7" fill="#888" font-family="Noto Sans JP,Yu Gothic,sans-serif">2,000万</text>
  <text x="376" y="224" text-anchor="middle" font-size="7" fill="#888" font-family="Noto Sans JP,Yu Gothic,sans-serif">3,000万</text>
  <text x="434" y="224" text-anchor="middle" font-size="7" fill="#888" font-family="Noto Sans JP,Yu Gothic,sans-serif">4,000万</text>
  <text x="491" y="224" text-anchor="middle" font-size="7" fill="#888" font-family="Noto Sans JP,Yu Gothic,sans-serif">5,000万</text>
  <text x="605" y="224" text-anchor="middle" font-size="7" fill="#888" font-family="Noto Sans JP,Yu Gothic,sans-serif">7,000万</text>
  <text x="400" y="240" text-anchor="middle" font-size="7.5" fill="#555" font-family="Noto Sans JP,Yu Gothic,sans-serif">支出の54%は機器＋建設（フェーズ3調達期がコスト管理の最重要期間）</text>
</svg>

</div>

---

## 5. 主要依存関係マップ

| 依存関係 | 前行作業 | 後続作業 | 遅延した場合の影響 |
|----------|----------|----------|-------------------|
| 日本人共同設立者 | 2.3 | 3.1、3.6 | 代表理事なしには法人設立不可 |
| 村役場の支持 | 2.1 | 3.1、4.6 | MOUなし；補助金申請が弱化 |
| フィージビリティスタディ | 3.2〜3.5 | 4.1〜4.4、資金調達 | P2予算の信頼性低下；補助金獲得困難 |
| METI FIT/FIP申請 | 4.2 | 5.2 試運転 | METI審査6か月 — M12までに申請必須 |
| 建築確認 | 4.1 | 5.1 建設着工 | 許可なしに建設着工不可 |
| NTT光ファイバー着手 | 4.5/4.7 | 5.7 | NTTリードタイム6〜9か月 |
| ゲート3資金確定 | 4.7 | 5.0（全作業） | ¥8,000万以上確定なしにP3着手不可 |
| 校舎改修 | 5.1 | 5.5 | 躯体完成前にデータセンター設備設置不可 |
| 太陽光＋蓄電池 | 5.2＋5.3 | 5.4 | EV充電は地域電源供給に依存 |

---

*Rob Oudendijk — YR-Design / Safecast*
*奈良県御杖村*
*2026年5月*
