<p align="right">Version: v1.0 | Last modified: 2026-10-15</p>

# Mitsue Village Project — Biomass CHP and Small-Scale AI Compute
### Project overview for HIGHRESO Co., Ltd. / 株式会社ハイレゾ 向けプロジェクト概要

Prepared by Rob Oudendijk (YR-Design / Safecast) after the online meeting of 2026-10-15. English first, 日本語は後半 (Part 2).

> **Status:** early Phase 0 (preparation). No contracts, partnerships, funding or final site decisions exist yet. Everything below is a working concept and design assumption, not a commitment.

---

# Part 1 — English

## 1. In one paragraph

Mitsue Village (御杖村, Nara Prefecture) is about 90% forest, much of it aging sugi (cedar) plantation that is under-managed. We are preparing a 25-year project that turns thinned sugi into fuel for a **small woody-biomass gasification CHP (combined heat and power)** unit. The CHP's continuous electricity and heat power a **small, community-oriented AI compute site**. In parallel, thinned stands are replanted with native broadleaf trees. The three parts — forest, energy, compute — are one system: the more the forest is thinned and restored, the more fuel and power the village has.

## 2. Why biomass CHP, and why AI compute

- **Dispatchable baseload.** AI workloads need power 24/7. Solar alone cannot supply it without large batteries. Wood CHP runs continuously, so it is the primary source; solar, EV charging and (subject to feasibility) batteries are complementary.
- **Fuel already exists.** Thinning residues and low-grade logs (sugi, plus possibly other local species) have limited value today. A local energy outlet gives thinning an extra revenue line.
- **Heat is a second product.** CHP heat is roughly twice the electric output. It can dry the chips (needed by some gasifier models) and, where practical, serve other local uses.
- **Rural grid constraints.** The substation serving the candidate area (Kake, 掛変電所, 6.6 kV) shows local spare capacity but zero upstream spare capacity, so on-site generation matched to a local load is attractive.
- **Fit with village policy.** The village's 2025 Renewable Energy Maximisation Plan (MoE-funded) already targets local renewables and resilient energy nodes; this project is designed as a way to execute it.

## 3. Reference prototype (design assumptions)

| Item | Working assumption |
|---|---|
| CHP size | ~50 kWe gasification CHP (Japanese maker preferred; no unit selected) |
| Heat output | ~100 kWth (about 2× electric) |
| Operation | 24 h/day, about 8,000 h/yr |
| Fuel | ~1.3–1.8 t dry wood/day, i.e. 2.5–3.5 t green chips/day, about 450–600 t/yr (three estimation methods; one measured plant used as reference) |
| Fuel moisture | Depends on the unit: some need ≤12–15% (drying step), some tolerate ≤40–45% |
| Compute | About one 20 ft container, ~35 kW IT load at 50 kWe generation |
| Site | Prototype: current idea is a site of the local forestry cooperative (under discussion, **not confirmed**). Site for the full-scale plant: still being researched |
| Network | Primary fibre plus failover uplink; business-grade SLA still to be confirmed |

**Scaling in two stages.** (1) The ~50 kWe prototype above proves fuel supply, operation and the compute integration at low risk. (2) Later, a full-scale plant of about **1.2 MWe** (indicatively 2 × 0.6 MWe gasifier-gensets, for redundancy and to stay under the 1 MW FIP threshold), sized to what the local forestry crew can sustainably supply (roughly half of the forest over 25 years). Compute capacity would scale with it; the full-scale stage is Phase 4 and is not funded.

Open design questions we would value HIGHRESO's view on are listed in section 7.

## 4. The three parts of the system

**Forest.** Thinning sugi plantations and replanting native broadleaf species (oak, chestnut and similar) that provide forage for wildlife and reduce crop damage. The 25-year horizon is deliberate. The local forestry cooperative's workforce capacity is the real limit on harvest volume, so we size the energy side to what the crew can supply rather than to a fixed harvest target.

**Energy.** Wood CHP as primary source; solar, EV charging and backup power for critical facilities as complements. Output is first for local use (compute, EV charging, resilience); grid sale (FIT/FIP) only where economical.

**Compute.** A small edge / AI inference site, run for community accountability rather than hyperscale economics. Intended uses include local LLM and inference services for the village and for external customers. If sold as a service, it needs redundant connectivity, remote operations and clearly tested failover before any uptime figure is promised.

## 5. Phasing (indicative)

| Phase | Period | Focus |
|---|---|---|
| 0. Preparation | Apr–Oct 2026 | Local trust, founding team, charter draft, partner conversations |
| 1. Establishment | Oct 2026–May 2027 | Legal entity, feasibility study, expert advisors |
| 2. Pilot design | May 2027–May 2028 | Detailed engineering, partnerships, permits |
| 3. Pilot build | May 2028–Nov 2029 | First-stage construction and commissioning |
| 4. Operation / scale-up | Nov 2029 onward | Operation, monitoring, replication |

Funding is staged by gates (G1 ¥3–8M, G2 ¥30–50M, G3 ¥120–290M). **No funding is committed at this time.** Subsidy tracks we are examining include METI's regional GX programme and Ministry of the Environment data-center decarbonisation support. The legal entity (likely a non-profit incorporated association) is still open.

## 6. Principles

- Modest in scale, transparent, and replicable by other depopulating municipalities; documentation is open source.
- Local partners lead where possible; we do not restructure existing village relationships.
- Honest claims: we describe what is planned, not what exists.

## 7. Where HIGHRESO's experience would help most

1. Practical lessons from running air-cooled data centers in repurposed or non-urban buildings: cooling, PUE in humid summers, noise, dust and maintenance.
2. Small-site design: container vs. building, rack density, power-quality needs and how to ride through a CHP trip or fuel interruption.
3. Operating model for remote small sites: monitoring, on-site staffing, security and customer SLAs.
4. Whether small, distributed sites like this could connect to HIGHRESO's GPU cloud or alliance network, and what technical and commercial conditions would be needed.
5. Any engineering partners, equipment suppliers or standards you would recommend we look at.

We are not asking for any commitment. A short follow-up conversation, or sharing a reference document, would already be very helpful.

## 8. Contacts

Rob Oudendijk — YR-Design / Safecast — Project lead, 御杖村 Forest Energy Project
Tel +81 80-2260-5966 · Website https://mitsue.it · Repository https://tinyurl.com/2xv524fz

---

<div style="page-break-after:always; break-after:page; height:0;"></div>

# Part 2 — 日本語

## 1. 概要

奈良県御杖村は面積の約9割を森林が占め、その多くは十分に手入れされていない杉の人工林です。私たちは、間伐材を燃料とする**小規模な木質バイオマスガス化熱電併給（CHP）**と、その24時間の電力・熱で動かす**小規模でコミュニティ運営型のAI計算拠点**を組み合わせる、25年規模のプロジェクトを準備しています。あわせて、間伐した跡地には在来広葉樹を植え戻します。森林・エネルギー・計算拠点は一つの仕組みであり、間伐と森林再生が進むほど、村の燃料と電力が増える設計です。

## 2. なぜバイオマスCHPか、なぜAI計算拠点か

- **安定したベースロード電源。** AI計算は24時間の電力を必要とします。太陽光だけでは大容量の蓄電池なしに賄えません。木質CHPは連続運転が可能なため主電源とし、太陽光・EV充電・（フィージビリティ次第で）蓄電池を補完とします。
- **燃料が既にある。** 間伐材や低質材は現在、価値が限られています。地域内のエネルギー用途は、間伐に追加の収入源をもたらします。
- **熱も製品。** CHPの熱は電気出力の約2倍あり、機種によっては必要なチップ乾燥に使え、条件が合えば他の地域利用も可能です。
- **農村の系統制約。** 候補地域を所管する掛変電所（6.6kV）は、地域内の空き容量はあるものの上位系の空き容量が0MWであり、現地発電と現地負荷を組み合わせる意義があります。
- **村の政策との整合。** 2025年に環境省補助で策定された御杖村「再エネ導入最大化計画」を実行する手段として設計しています。

## 3. 試作機の想定（設計上の仮定）

| 項目 | 現時点の想定 |
|---|---|
| CHP規模 | 約50kWeのガス化CHP（国産メーカー優先、機種は未選定） |
| 熱出力 | 約100kWth（電気出力の約2倍） |
| 運転 | 1日24時間、年約8,000時間 |
| 燃料 | 乾燥材 約1.3〜1.8 t/日（生チップ 約2.5〜3.5 t/日、年約450〜600 t）。3通りの試算、うち1件は実稼働プラントの実績を参照 |
| 燃料含水率 | 機種により、12〜15%以下の乾燥が必要なものと、40〜45%程度まで許容するものがある |
| 計算拠点 | 20フィートコンテナ1基程度、発電50kWe時にIT負荷 約35kW |
| 設置場所 | 試作機：現時点では地元の森林組合の敷地を想定（協議中、**確定ではありません**）。本格プラントの立地：引き続き調査中 |
| ネットワーク | 主回線＋冗長回線（法人向けSLAの有無は要確認） |

**2段階のスケールアップ。** (1) 上記の約50kWe試作機で、燃料供給・運転・計算拠点との統合を低リスクで検証します。(2) その後、地元の作業班が持続的に供給できる量（25年で森林の約半分）に合わせ、約**1.2MWe**の本格プラント（目安として0.6MWe×2基のガス化発電機。冗長性と、1MW未満の枠を保つため）へ拡大します。計算能力もそれに合わせて拡大します。本格段階はフェーズ4で、資金は未確保です。

## 4. 構成要素

**森林。** 杉人工林を間伐し、野生動物の餌となるコナラ・クヌギ・クリ等の在来広葉樹へ段階的に転換します。25年という期間は意図的です。伐採量の実際の上限は地元の森林組合の作業力であるため、エネルギー側は固定の伐採目標ではなく、作業班が供給できる量に合わせて規模を決めます。

**エネルギー。** 木質CHPを主電源とし、太陽光・EV充電・重要施設向けバックアップ電源で補完します。まず地域内利用（計算拠点・EV充電・レジリエンス）を優先し、系統売電（FIT/FIP）は経済性が合う場合のみ行います。

**計算拠点。** ハイパースケールの経済性ではなく、コミュニティの説明責任に合わせた小規模エッジ／AI推論拠点です。村内向けおよび外部顧客向けのローカルLLM・推論サービスを想定しています。サービスとして提供する場合、冗長な通信回線、遠隔運用、フェイルオーバーの実証が、稼働率を約束する前に必要です。

## 5. 段階計画（目安）

| フェーズ | 期間 | 焦点 |
|---|---|---|
| 0. 設立準備 | 2026年4月〜10月 | 地域の信頼構築、創設チーム、憲章草案、関係者との対話 |
| 1. 設立 | 2026年10月〜2027年5月 | 法人設立、フィージビリティスタディ、専門家顧問 |
| 2. パイロット設計 | 2027年5月〜2028年5月 | 詳細設計、パートナーシップ、許認可 |
| 3. パイロット建設 | 2028年5月〜2029年11月 | 第1段階の建設・試運転 |
| 4. 運営・拡大 | 2029年11月以降 | 運営、モニタリング、横展開 |

資金はゲート方式です（G1 ¥3〜8M、G2 ¥30〜50M、G3 ¥120〜290M）。**現時点で確定した資金はありません。** 検討中の補助制度には、経済産業省の地域GX関連事業や、環境省のデータセンター脱炭素支援があります。法人形態（一般社団法人等）は未確定です。

## 6. 基本方針

- 規模は控えめに、透明性を保ち、他の過疎自治体が再現できる形にします。成果物はオープンソースで公開します。
- 可能な限り地元の方々が主体となり、既存の村内の関係を変えることはしません。
- 事実に基づく説明：計画していることと、既に存在することを区別して伝えます。

## 7. ハイレゾ様のご知見をいただきたい点

1. 空き施設・都市部以外の建物での空冷データセンター運営の実務：冷却、高湿度の夏季のPUE、騒音、粉じん、保守。
2. 小規模拠点の設計：コンテナか建屋か、ラック密度、電源品質、CHP停止・燃料途絶時のライドスルー。
3. 遠隔の小規模拠点の運営モデル：監視、現地要員、セキュリティ、顧客向けSLA。
4. このような小規模分散拠点が、ハイレゾ様のGPUクラウドやアライアンスのネットワークと連携し得るか、その場合の技術的・商業的条件。
5. ご紹介いただける技術パートナー、機器メーカー、参照すべき基準。

何らかのお約束をお願いするものではありません。短いフォローアップのお打合せや、参考資料のご共有だけでも大変助かります。

## 8. 連絡先

ロブ・アウデンダイク — YR-Design / Safecast — 御杖村 森林エネルギー事業 プロジェクトリード
電話 +81 80-2260-5966 · Web https://mitsue.it · リポジトリ https://tinyurl.com/2xv524fz
