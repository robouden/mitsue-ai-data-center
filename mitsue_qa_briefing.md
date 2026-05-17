<p align="right">Version: v2.0 &nbsp;|&nbsp; Last modified: 2026-05-17</p>

# Six Questions on the Mitsue Project — Briefing Q&A
## 御杖プロジェクトに関する六つのご質問 ―― 簡易Q&A

**Working draft, May 2026 · Project Lead: Rob Oudendijk**
**作成中ドラフト 2026年5月 · 代表: ロブ・アウデンダイク**

---

This document responds to six questions raised during informal consultation. It is intended as a starting point for further discussion with the village, advisors, and stakeholders — not as a final position. Firm engineering and financial figures will follow the Phase 2 feasibility study (months 10–18).

本資料は、有志の方からいただいた六つのご質問に対する回答をまとめたものです。村役場、アドバイザー、関係各位とのさらなる対話の出発点として作成しております。最終見解ではございません。正確な技術・財務数値は、第2段階のフィージビリティスタディ(10〜18か月目)を経て確定いたします。

---

## A note before the questions / ご質問にお答えする前に

Several early conversations assumed biomass energy generation as the project's energy component. After extensive community consultation, the project is now focusing on **EV charging infrastructure and community energy resilience** — solar panels, battery storage, and EV charging stations — rather than a biomass boiler. This reflects both what the community needs most and what is most practical to implement.

ご相談を重ねた結果、エネルギー部門の焦点を**EVインフラと地域エネルギーレジリエンス**（太陽光発電・蓄電池・EV充電ステーション）に絞ることといたしました。これは地域のニーズと実現可能性の両面から最善の選択です。

---

# English

### Q1. Why EV charging? Is there really demand for this in a rural mountain village?

Yes — and growing. Japan's national policy targets widespread EV adoption by the mid-2030s. Rural areas are actually at greater disadvantage in this transition: existing public charging infrastructure is concentrated in cities, and rural residents who commute long distances between visits to the nearest town need reliable local charging most. Key points:

- Mitsue residents who own EVs currently have no public charging within the village. Home charging requires overnight access and stable power — not always available.
- The school site, with its parking area and accessible location, is the natural hub for village charging infrastructure.
- EV charging also attracts visitors (hikers, tourism, day-trippers from Nara/Osaka) who will need to charge while visiting.
- Revenue from charging fees contributes to project sustainability from Year 3 onwards.

### Q2. How does the blackout resilience work? Is Mitsue really at risk?

Yes. Rural distribution lines in Japan are aging, and Mitsue's mountain location makes it vulnerable to outages during typhoons, heavy snowfall, and other weather events. Key points:

- The project's battery storage system — sized primarily to store solar generation for the data center — can be configured to supply the school building and adjacent facilities during a grid outage.
- This "island mode" operation keeps the data center, emergency lighting, communications equipment, and EV chargers operational even when the broader grid is down.
- Battery capacity will be specified during Phase 2 feasibility (months 10–18). Preliminary estimates suggest a system supporting 12–48 hours of critical-load operation during an outage.
- The data center's uninterruptible power supply (UPS) infrastructure, already required for its own operations, forms the backbone of this community resilience capability at minimal additional cost.

### Q3. Why a data center? What unique advantage does it provide?

The data center is what turns an energy project into a development project.

1. **Load-shape match.** Solar is intermittent. A data center is one of the very few rural loads that runs 24/7/365 — it justifies the scale of battery storage that makes EV charging and blackout resilience feasible.
2. **Anchor revenue.** Without an anchor offtaker, rural energy projects in Japan typically fail their financials. The data center provides predictable, year-round revenue.
3. **Heat reuse.** Server waste heat can warm community spaces or greenhouses, closing a useful loop.
4. **Digital deficit.** Rural Japan has a real edge-compute and connectivity gap. Local hosting improves latency, sovereignty, and resilience for nearby municipalities and SMEs.
5. **Higher-skill jobs.** Operations and monitoring roles attract younger residents and returnees.
6. **Replicability.** With the data center, Mitsue becomes a rural-revitalization model that other depopulating municipalities can study and adapt.

### Q4. Are there benefits visible before 25 years?

Yes. The 25-year horizon applies to forest restoration ecology, not to community benefit. Tangible benefits arrive much sooner — see the early-benefits table in [mitsue_village_government_onepager.md](mitsue_village_government_onepager.md). Highlights:

- **Year 1**: Closed school reactivated; domestic and international media coverage; first researcher and student visits.
- **Year 2**: First forestry contracts → direct cash income to private landowners.
- **Year 3–4**: EV charging stations operational; battery storage for community blackout resilience.
- **Year 4–5**: Data center hires local staff; hosting and energy revenue real; village becomes a study-tour destination.

### Q5. Solar panels already exist in Mitsue. How does the project add value beyond what's already there?

The existing solar installations belong to individual landowners and are connected to the grid via FIT (feed-in tariff) — their output goes to the national grid, not to local use. The project adds:

| | Existing solar | Project solar + battery |
|---|---|---|
| Output destination | National grid (FIT) | Local use first, grid second |
| Battery storage | None | Yes — enables blackout resilience |
| EV charging | None | Yes — from Year 3 |
| Community control | Individual owners | Village NPO |
| Blackout protection | None | Yes — critical facilities |

The project does not compete with existing installations — it builds a complementary community-owned system that does what individual rooftop solar cannot: store energy, provide EV charging, and keep critical services running when the grid fails.

### Q6. How will EV charging and battery storage costs be recovered?

A stack of revenue streams, not a single source:

1. **EV charging fees** — residents and visitors pay per kWh or per session. At low initial volume, fees will not cover costs; by Year 5–7, when the EV fleet is larger, economics improve significantly.
2. **FIT/FIP feed-in tariff** — surplus solar generation sold to the grid when battery is full and local demand is low.
3. **J-Credit** — carbon offset income from verified renewable generation.
4. **Data center anchor revenue** — the primary long-term income source; cross-subsidizes community energy services in early years.
5. **METI/NEDO grants** — rural energy resilience and EV infrastructure are explicit priority areas for government subsidy programs.
6. **Phased capacity** — the funding-gate structure prevents over-scaling. EV charging begins small (2–4 stations) and expands as demand grows.

---

# 日本語

### Q1. なぜEV充電なのでしょうか? 山間の農村にそれほど需要があるのでしょうか?

はい、そして需要は拡大しています。日本の国家政策は2030年代半ばまでのEV普及を目指しており、農村部はこの移行においてとりわけ不利な立場にあります。既存の公共充電インフラは都市部に集中しており、最寄りの町まで長距離を移動する農村住民こそ、地元の充電設備を最も必要としています。

- 御杖村でEVを所有する住民が利用できる公共充電設備は、現在村内に存在しません。
- 駐車場を備えアクセスしやすい校舎跡地は、村の充電インフラの自然な拠点です。
- EV充電は、奈良・大阪からのハイカーや観光客・日帰り客も利用でき、誘客効果が期待できます。
- 充電料金収入は、3年目以降のプロジェクト持続性に貢献します。

### Q2. 停電対策はどのように機能するのでしょうか? 御杖村には本当にリスクがあるのでしょうか?

はい。日本の農村部の配電線は老朽化が進んでおり、御杖村の山間部立地により、台風・大雪・その他の気象イベント時に停電リスクが高い状況です。

- プロジェクトの蓄電池システムは、主にデータセンター向けに太陽光発電を蓄電するものですが、停電時には校舎および周辺施設へ電力を供給するよう構成できます。
- この「アイランドモード」運転により、広域停電時もデータセンター、非常照明、通信機器、EV充電器を稼働させ続けることができます。
- 蓄電容量は第2段階のフィージビリティスタディ（10〜18か月目）で詳細設計します。予備試算では、停電時に重要負荷を12〜48時間程度維持できる規模を想定しています。
- データセンター自身の運営に必須の無停電電源装置（UPS）インフラが、最小限の追加コストで地域レジリエンス機能の基盤を形成します。

### Q3. データセンターとEVインフラの関係 ―― なぜデータセンターが必要なのでしょうか?

データセンターの存在こそが、エネルギー事業を地域振興事業へと転換いたします。

1. **負荷曲線の整合性。** 太陽光は間欠的でございます。データセンターは農村部における数少ない24時間365日稼働の負荷であり、EV充電や停電レジリエンスを可能にする規模の蓄電池投資を正当化します。
2. **基幹収益。** 安定した引き取り手なしには、農村のエネルギー事業は経済的に成立しないのが通例です。データセンターは年間を通じた予測可能な収益を提供します。
3. **排熱の再利用。** サーバーの排熱を地域スペースや温室の暖房に活用できます。
4. **デジタル基盤の不足。** 日本の農村部にはエッジコンピューティングと通信環境の現実的な格差があります。
5. **より高度な雇用。** 運用・監視業務は若い住民やUターン者の受け皿となります。
6. **再現可能性。** データセンターを伴うことで、御杖は他の過疎自治体が学習・展開できる農村再生のモデルとなります。

### Q4. 25年を待たずに、村にとって実感できる成果はあるのでしょうか?

ございます。25年という時間軸は森林再生の生態的な期間であり、村への効果はもっと早く現れます。

- **1年目**: 閉校舎の再活用、国内外メディアによる発信、研究者・学生の来訪。
- **2年目**: 最初の林業契約 → 山林所有者への直接的な現金収入。
- **3〜4年目**: EV充電ステーション稼働開始、停電レジリエンス向けの蓄電池設置。
- **4〜5年目**: データセンターの地域雇用、ホスティング料・電力販売による実収入。

### Q5. 御杖村には既に太陽光パネルがあります。プロジェクトはどのような付加価値を生み出すのでしょうか?

既存の太陽光設備は個人所有であり、FIT（固定価格買取制度）により発電電力は国の系統へ送られています。プロジェクトが加えるものは:

| | 既存の太陽光 | プロジェクトの太陽光＋蓄電池 |
|---|---|---|
| 出力先 | 国の系統（FIT） | 地産地消優先、余剰を系統へ |
| 蓄電池 | なし | あり ―― 停電レジリエンスを実現 |
| EV充電 | なし | あり ―― 3年目から |
| 地域管理 | 個人所有者 | 村NPO |
| 停電対策 | なし | あり ―― 重要施設を守る |

プロジェクトは既存設備と競合するのではなく、個人の屋根置き太陽光にはできないことを実現するコミュニティ所有システムを構築します。

### Q6. EV充電と蓄電池のコストはどのように回収されるのでしょうか?

単一の解決策ではなく、複数の収益源の積み重ねでございます。

1. **EV充電料金** ―― 住民・来訪者がkWh単位またはセッション単位で支払います。初期は低収入ですが、EVが普及する5〜7年目以降に経済性が大きく改善します。
2. **FIT/FIP** ―― 蓄電池満充時および地域需要低下時の余剰太陽光を系統へ売電。
3. **J-クレジット** ―― 再生可能エネルギー発電に対する炭素オフセット収入。
4. **データセンター基幹収益** ―― 最も重要な長期収入源。初期は地域エネルギーサービスを内部補助します。
5. **経産省・NEDO補助金** ―― 農村エネルギーレジリエンスとEVインフラは補助制度の優先対象分野です。
6. **段階的な能力拡張** ―― 充電ステーションは少数（2〜4台）から始め、需要拡大に合わせて増設します。

---

*Working draft / 作成中ドラフト · May 2026 / 2026年5月 · Rob Oudendijk · 御杖プロジェクト*
