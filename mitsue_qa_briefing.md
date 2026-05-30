<style>
  body { font-size: 9.5pt; line-height: 1.25; }
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

<p align="right">Version: v2.6 &nbsp;|&nbsp; Last modified: 2026-05-28</p>

# Six Questions on the Mitsue Project — Briefing Q&A
## 御杖プロジェクトに関する六つのご質問 ―― 簡易Q&A

**Working draft, May 2026 · Project Lead: Rob Oudendijk**
**作成中ドラフト 2026年5月 · 代表: ロブ・アウデンダイク**

---

This document responds to six questions raised during informal consultation. It is intended as a starting point for further discussion with the village, advisors, and stakeholders — not as a final position. Firm engineering and financial figures will follow the Phase 2 feasibility study (months 10–18).

本資料は、有志の方からいただいた六つのご質問に対する回答をまとめたものです。村役場、アドバイザー、関係各位とのさらなる対話の出発点として作成しております。最終見解ではございません。正確な技術・財務数値は、第2段階のフィージビリティスタディ(10〜18か月目)を経て確定いたします。

---

## A note before the questions / ご質問にお答えする前に

The project's **primary energy source is biomass combined heat and power (CHP)** fuelled by sugi (cedar) forest thinnings — generating electricity (primary output) and heat (secondary output). This is complemented by solar panels (intermittent, supplementary) and supports community services including EV charging stations, with battery storage and blackout resilience. Battery storage will be evaluated in the Phase 1 feasibility study and is not a confirmed install. The result is a circular local energy economy: the forest powers the village.

The forestry programme is focused on **replacing aged sugi (cedar) plantations with native broadleaf species** — ecological restoration that heals land that has been depleted for generations. Thinning the aged sugi serves both purposes: it heals the forest and generates the biomass fuel feedstock. Native broadleaf trees (konara oak, kunugi, chestnut) provide food for deer, wild boar, and bear, reducing wildlife raids on crops, and support long-term carbon sequestration via J-Credit certification.

このプロジェクトの**主たるエネルギー源は、杉（スギ）林の間伐材を燃料とするバイオマス熱電併給（CHP）**であり、電力（主たる出力）と熱（副次的な出力）を生み出します。これを太陽光発電（間欠的・補完的）が補い、EV充電ステーションをはじめとする地域サービスや蓄電池・停電レジリエンスを支えます。蓄電池はフィージビリティスタディで評価します。こうして「森が村を動かす」循環型の地域エネルギー経済が実現します。

林業の方針については：老齢化した杉の人工林を在来種の広葉樹（コナラ・クヌギ・クリなど）へ転換する**生態的な森林再生**を進めます。在来広葉樹はシカ・イノシシ・クマの食料を供給し、野生動物を森に留め、農作物への被害を軽減します。J-Creditによる炭素固定収入も山林所有者の長期的な財源となります。

---

# English

### Q1. Why EV charging? Is there really demand for this in a rural mountain village?

Yes — and rural EV owners are among the most underserved. Japan's national policy aims for plug-in vehicles to reach 30–40% of new car sales by the mid-2030s, though the total share of EVs on all roads is projected at only around 10–15% by 2036 — a gradual transition, not an overnight switch. Rural areas are at greater disadvantage in this shift: existing charging infrastructure is concentrated in cities, while rural residents who travel long distances need reliable local charging most. Key points:

- Mitsue residents who own EVs currently have no public charging within the village. Home charging requires overnight access and stable power — not always available.
- The Koryukan site, with its parking area and accessible location, is the natural hub for village charging infrastructure.
- EV charging also attracts visitors (hikers, tourism, day-trippers from Nara/Osaka) who will need to charge while visiting.
- Revenue from charging fees contributes to project sustainability from Year 3 onwards.

### Q2. How does the blackout resilience work? Is Mitsue really at risk?

Yes. Rural distribution lines in Japan are aging, and Mitsue's mountain location makes it vulnerable to outages during typhoons, heavy snowfall, and other weather events. Key points:

- The project's on-site biomass CHP generation provides 24/7 baseload power and, combined with complementary solar and battery storage (to be evaluated in Phase 1 and added if confirmed), can be configured to supply the Koryukan and adjacent facilities during a grid outage.
- This "island mode" operation keeps the data center, emergency lighting, communications equipment, and EV chargers operational even when the broader grid is down — and unlike solar alone, biomass CHP runs through the night and through extended bad-weather outages.
- Battery capacity will be specified during Phase 2 feasibility (months 10–18). Preliminary estimates suggest a system supporting 12–48 hours of critical-load operation during an outage.
- The data center's uninterruptible power supply (UPS) infrastructure, already required for its own operations, forms the backbone of this community resilience capability at minimal additional cost.

### Q3. Why a data center? What unique advantage does it provide?

The data center is what turns an energy project into a development project.

1. **Load-shape match.** A data center is one of the very few rural loads that runs 24/7/365 — a steady baseload that pairs naturally with biomass CHP (which also runs continuously) and justifies the scale of the energy investment that makes EV charging and blackout resilience feasible. Solar alone is intermittent; biomass provides the round-the-clock baseload the data center needs.
2. **Anchor revenue.** Without an anchor offtaker, rural energy projects in Japan typically fail their financials. The data center provides predictable, year-round revenue.
3. **Heat reuse.** The biomass CHP system's heat output and server waste heat can warm community spaces or greenhouses, closing a useful loop.
4. **Digital deficit.** Rural Japan has a real edge-compute and connectivity gap. Local hosting improves latency, sovereignty, and resilience for nearby municipalities and SMEs.
5. **Higher-skill jobs.** Operations and monitoring roles attract younger residents and returnees.
6. **Replicability.** With the data center, Mitsue becomes a rural-revitalization model that other depopulating municipalities can study and adapt. A community-owned AI data center powered by locally generated renewable energy sets a working example of how technological progress and ecological sustainability can be a single coherent system — not opposites.

### Q4. Are there benefits visible before 25 years?

Yes. The 25-year horizon applies to forest restoration ecology, not to community benefit. Tangible benefits arrive much sooner — see the early-benefits table in [mitsue_village_government_onepager.md](mitsue_village_government_onepager.md). Highlights:

- **Year 1**: Taiken Koryukan reactivated as datacenter hub; domestic and international media coverage; first researcher and student visits.
- **Year 2**: First forestry contracts → direct cash income to private landowners.
- **Year 3–4**: EV charging stations operational; battery storage if confirmed by feasibility study.
- **Year 4–5**: Data center hires local staff; hosting and energy revenue real; village becomes a study-tour destination.

### Q5. Solar panels already exist in Mitsue. How does the project add value beyond what's already there?

The existing solar installations belong to individual landowners and are connected to the grid via FIT (feed-in tariff) — their output goes to the national grid, not to local use. The project adds:

| | Existing solar | Project solar |
|---|---|---|
| Output destination | National grid (FIT) | Local use first, grid second |
| Battery storage | None | Subject to feasibility study |
| EV charging | None | Yes — from Year 3 |
| Community control | Individual owners | Village NPO |
| Blackout protection | None | Yes — critical facilities |

The project does not compete with existing installations — it builds a complementary community-owned system that does what individual rooftop solar cannot: pair solar with biomass CHP baseload generation, store energy, provide EV charging, and keep critical services running when the grid fails. Solar is one supplementary input to the project; the primary supply is biomass CHP from sugi thinnings.

### Q6. How will EV charging and energy infrastructure costs be recovered?

A stack of revenue streams, not a single source:

1. **EV charging fees** — residents and visitors pay per kWh or per session. At low initial volume, fees will not cover costs; by Year 5–7, when the EV fleet is larger, economics improve significantly.
2. **FIT/FIP feed-in tariff** — surplus solar sold to the grid when local demand is low.
3. **J-Credit** — carbon offset income from verified renewable generation.
4. **Data center anchor revenue** — the primary long-term income source; cross-subsidizes community energy services in early years.
5. **METI/NEDO grants** — rural energy resilience and EV infrastructure are explicit priority areas for government subsidy programs.
6. **Mitsue village startup subsidy** — the village's own program (5 new enterprises over 5 years, partial business-cost support) is a natural fit. The project, or for-profit sub-entities the NPO incorporates, can apply. Politically aligned with stated village policy on youth retention and depopulation.
7. **Phased capacity** — the funding-gate structure prevents over-scaling. EV charging begins small (2–4 stations) and expands as demand grows.

### Q7. What is the forestry plan? Why native forest restoration rather than plantation management?

Earlier conversations sometimes described the forestry component as managing sugi plantations for timber or biomass. After further development, the project is focused on **replacing aged sugi monoculture with native broadleaf forest** — ecological restoration rather than plantation management. Key points:

- **Ecological recovery, not resource extraction.** Sugi monocultures are ecologically depleted — poor biodiversity, minimal understory, and limited wildlife habitat. Replacing them with native broadleaf species (konara oak, kunugi, chestnut) restores the forest ecosystem over a 25-year horizon.
- **Wildlife pressure relief.** Native broadleaf trees produce acorns and nuts that feed deer, wild boar, and bear through winter. When the forest feeds them naturally, they stay in the forest — directly reducing the wildlife raids on surrounding crop areas that already trouble Mitsue farmers.
- **Carbon sequestration revenue.** Native broadleaf forests accumulate carbon at roughly 3–6 tC/ha/yr once established. A 50 ha restored stand could generate J-Credit carbon credits, providing long-term income for participating landowners — more durable than one-time timber revenue.
- **Thinnings become energy.** Restoration is not pure extraction, but the sugi removed during conversion is not wasted: it fuels the biomass CHP system that is the project's primary energy source. The forest is both an ecological liability to heal and an energy asset — thinning it does both at once. Solar and EV charging complement this biomass core.
- **Policy alignment.** The Forestry Agency (林野庁) and the 森林環境譲与税 framework actively support native species conversion and forest restoration projects of exactly this type.

---

# 日本語

### Q1. なぜEV充電なのでしょうか? 山間の農村にそれほど需要があるのでしょうか?

はい、そして農村部のEVオーナーほど不便な状況に置かれています。日本の国家政策は2030年代半ばまでに新車販売の30〜40%をプラグイン車にすることを目指していますが、路上全車両に占めるEVの割合は2036年時点でも10〜15%程度にとどまる見込みで、急速な転換ではなく段階的な移行です。農村部はこの変化においてとりわけ不利な立場にあります。既存の公共充電インフラは都市部に集中しており、最寄りの町まで長距離を移動する農村住民こそ、地元の充電設備を最も必要としています。

- 御杖村でEVを所有する住民が利用できる公共充電設備は、現在村内に存在しません。
- 駐車場を備えアクセスしやすい校舎跡地は、村の充電インフラの自然な拠点です。
- EV充電は、奈良・大阪からのハイカーや観光客・日帰り客も利用でき、誘客効果が期待できます。
- 充電料金収入は、3年目以降のプロジェクト持続性に貢献します。

### Q2. 停電対策はどのように機能するのでしょうか? 御杖村には本当にリスクがあるのでしょうか?

はい。日本の農村部の配電線は老朽化が進んでおり、御杖村の山間部立地により、台風・大雪・その他の気象イベント時に停電リスクが高い状況です。

- プロジェクトの現地バイオマスCHP発電は24時間の安定電源を供給し、これを補完する太陽光発電と蓄電池（フィージビリティスタディで評価し確認されれば設置）と組み合わせることで、停電時には校舎および周辺施設へ電力を供給するよう構成できます。
- この「アイランドモード」運転により、広域停電時もデータセンター、非常照明、通信機器、EV充電器を稼働させ続けることができます。太陽光だけと異なり、バイオマスCHPは夜間も悪天候による長時間停電中も稼働を続けます。
- 蓄電容量は第2段階のフィージビリティスタディ（10〜18か月目）で詳細設計します。予備試算では、停電時に重要負荷を12〜48時間程度維持できる規模を想定しています。
- データセンター自身の運営に必須の無停電電源装置（UPS）インフラが、最小限の追加コストで地域レジリエンス機能の基盤を形成します。

### Q3. データセンターとEVインフラの関係 ―― なぜデータセンターが必要なのでしょうか?

データセンターの存在こそが、エネルギー事業を地域振興事業へと転換いたします。

1. **負荷曲線の整合性。** データセンターは農村部における数少ない24時間365日稼働の負荷であり、同じく連続稼働するバイオマスCHPと自然に組み合わさる安定したベースロード需要として、EV充電や停電レジリエンスを可能にする規模のエネルギー設備投資を正当化します。太陽光だけでは間欠的ですが、バイオマスがデータセンターに必要な24時間のベースロードを供給します。
2. **基幹収益。** 安定した引き取り手なしには、農村のエネルギー事業は経済的に成立しないのが通例です。データセンターは年間を通じた予測可能な収益を提供します。
3. **排熱の再利用。** バイオマスCHPの熱出力とサーバーの排熱を地域スペースや温室の暖房に活用できます。
4. **デジタル基盤の不足。** 日本の農村部にはエッジコンピューティングと通信環境の現実的な格差があります。
5. **より高度な雇用。** 運用・監視業務は若い住民やUターン者の受け皿となります。
6. **再現可能性。** データセンターを伴うことで、御杖は他の過疎自治体が学習・展開できる農村再生のモデルとなります。

### Q4. 25年を待たずに、村にとって実感できる成果はあるのでしょうか?

ございます。25年という時間軸は森林再生の生態的な期間であり、村への効果はもっと早く現れます。

- **1年目**: 体験交流館の活用開始、国内外メディアによる発信、研究者・学生の来訪。
- **2年目**: 最初の林業契約 → 山林所有者への直接的な現金収入。
- **3〜4年目**: EV充電ステーション稼働開始、停電レジリエンス向けの蓄電池設置。
- **4〜5年目**: データセンターの地域雇用、ホスティング料・電力販売による実収入。

### Q5. 御杖村には既に太陽光パネルがあります。プロジェクトはどのような付加価値を生み出すのでしょうか?

既存の太陽光設備は個人所有であり、FIT（固定価格買取制度）により発電電力は国の系統へ送られています。プロジェクトが加えるものは:

| | 既存の太陽光 | プロジェクトの太陽光 |
|---|---|---|
| 出力先 | 国の系統（FIT） | 地産地消優先、余剰を系統へ |
| 蓄電池 | なし | フィージビリティスタディで評価 |
| EV充電 | なし | あり ―― 3年目から |
| 地域管理 | 個人所有者 | 村NPO |
| 停電対策 | なし | あり ―― 重要施設を守る |

プロジェクトは既存設備と競合するのではなく、個人の屋根置き太陽光にはできないことを実現するコミュニティ所有システムを構築します。すなわち、太陽光をバイオマスCHPのベースロード発電と組み合わせ、電力を蓄え、EV充電を提供し、停電時にも重要サービスを維持します。太陽光はプロジェクトの補完的な一入力にすぎず、主たる供給源は杉間伐材によるバイオマスCHPです。

### Q6. EV充電と蓄電池のコストはどのように回収されるのでしょうか?

単一の解決策ではなく、複数の収益源の積み重ねでございます。

1. **EV充電料金** ―― 住民・来訪者がkWh単位またはセッション単位で支払います。初期は低収入ですが、EVが普及する5〜7年目以降に経済性が大きく改善します。
2. **FIT/FIP** ―― 蓄電池満充時および地域需要低下時の余剰太陽光を系統へ売電。
3. **J-クレジット** ―― 再生可能エネルギー発電に対する炭素オフセット収入。
4. **データセンター基幹収益** ―― 最も重要な長期収入源。初期は地域エネルギーサービスを内部補助します。
5. **経産省・NEDO補助金** ―― 農村エネルギーレジリエンスとEVインフラは補助制度の優先対象分野です。
6. **御杖村 起業支援補助金** ―― 「5年で5社の新規事業創出」を掲げる村の制度。本プロジェクト本体、もしくはNPO傘下に設立する事業会社（合同会社・GK等）が対象となり得ます。若者定着・過疎対策という村の政策方針と整合します。
7. **段階的な能力拡張** ―― 充電ステーションは少数（2〜4台）から始め、需要拡大に合わせて増設します。

### Q7. 林業計画はどのようなものですか? なぜ杉林の管理ではなく在来種による森林再生なのでしょうか?

以前のご説明では、林業部門の役割として杉人工林の管理（木材・残材の利用）を想定しておりました。さらに検討を重ねた結果、プロジェクトの林業方針を**老齢化した杉の単一林を在来種の広葉樹林へ転換する生態的森林再生**に定めました。要点は以下の通りです。

- **生態系の回復を最優先に。** 杉の単一林は生態的に貧しく、生物多様性・下層植生・野生動物の生息環境が著しく損なわれています。コナラ・クヌギ・クリなどの在来広葉樹への転換により、25年という時間軸で森林生態系を回復させます。
- **野生動物被害の軽減。** 在来広葉樹はシカ・イノシシ・クマの冬の食料（どんぐり・木の実）を供給します。森が食料を提供すれば、野生動物は森の中に留まり、御杖村の農家がすでに悩まされている農作物被害が直接的に軽減されます。
- **炭素固定による収入。** 在来広葉樹林は定着後、年間約3〜6 tC/haのペースで炭素を蓄積します。50haの再生林でJ-Creditの炭素クレジット収入が見込め、参加する山林所有者に一時的な木材収益より持続的な長期収入をもたらします。
- **間伐材がエネルギーになる。** 森林再生は単なる資源採取ではありませんが、転換の過程で伐り出される杉は無駄になりません。プロジェクトの主たるエネルギー源であるバイオマスCHPの燃料となります。森は癒すべき生態的負債であると同時にエネルギー資産でもあり、間伐はその両方を同時に果たします。太陽光とEV充電はこのバイオマスの中核を補完します。
- **政策との整合。** 林野庁および森林環境譲与税の枠組みは、まさにこのような在来種への転換・森林再生事業を積極的に支援しています。

---

*Working draft / 作成中ドラフト · May 2026 / 2026年5月 · Rob Oudendijk · 御杖プロジェクト*
