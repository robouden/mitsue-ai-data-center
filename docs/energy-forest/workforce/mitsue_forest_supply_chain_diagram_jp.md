<!-- Version: v1.6 | Last modified: 2026-10-09 -->

# 御杖村の森林・木材の流れ ― 現在わかっていること

確認できた事実と、まだ不明な点を分けて図にしました。**実線＝出典のある事実、点線＝未確認・提案・将来。**
下流側（CHP→計算資源）は `../chp-technical/mitsue_forest_power_compute_loop.html` にあり、この図はその上流側です。

```mermaid
flowchart TD
    own1["民間の森林所有者<br/>約7,051haの90%超"]
    own2["共有地（財産区・入会）？<br/>御杖村での記録なし<br/>天川村の洞川財産区のみ確認"]
    own3["村有林？<br/>2026-08-05に観光協会へ質問<br/>回答はまだ"]

    forest["御杖村の森林 約7,051ha<br/>杉・ヒノキの戦後人工林"]

    own1 --> forest
    own2 -.-> forest
    own3 -.-> forest

    vh["役場 産業建設課<br/>伐採届は届出のみ（許可ではない）<br/>村費の間伐・村有林の事業者を選定<br/>（方法は2026-10-09に質問）"]
    forest --> vh

    coopcrew["森林組合の現場班<br/>2名、平均年齢約33歳"]
    yamaguchi["個人の林業者<br/>活動を確認済み・自伐型林業<br/>地域おこし協力隊（林業部門）<br/>随時・所有者からの依頼<br/>木材は美杉市場へ<br/>燃料供給者にはならない意向"]
    tokuda["徳田林産<br/>本社 神末・社員7名＋臨時15名<br/>山林と立木を購入し<br/>市場・製材所へ直送（桜井等）<br/>三重事務所2018年・村との関係は確認できず"]
    otherindep["その他の個人林業者<br/>10以上（本人の推測・未確認）"]
    miesup["三重側（美杉）の事業者？<br/>未確認"]
    corps["地域おこし協力隊 自伐型林業<br/>任期最長3年<br/>過去2年は採用ゼロ"]
    loan["村の林業用重機貸与<br/>バックホウ＋ダンプ<br/>任期後最長5年・1日1,000円"]

    forest --> coopcrew
    forest --> yamaguchi
    forest -.-> tokuda
    forest -.-> otherindep
    forest -.-> corps
    corps -.-> loan
    loan -.-> yamaguchi
    vh -->|"村費の間伐"| coopcrew
    vh -.-> tokuda

    leftover["林内に残置<br/>間伐は年約66haだが<br/>搬出は年約120〜300m3のみ"]
    coopcrew -->|間伐| leftover

    mill["牛峠工場<br/>組合のチップ・乾燥加工センター"]
    coopcrew -->|"年約120〜300m3"| mill

    gate["提案：オープンゲート燃料土場<br/>どの事業者もC・D材を規格どおり<br/>公表の受入価格で搬入<br/>組合＝加工・買取"]
    otherindep -.-> gate
    tokuda -.-> gate
    miesup -.-> gate
    gate -.-> mill

    machine["提案：共有ハーベスタ<br/>コマツ901XCまたは931XC試験導入<br/>所有者は未定（村・NGO・組合）<br/>全事業者に同条件"]
    machine -.-> coopcrew
    machine -.-> otherindep
    vh -.-> machine

    misugi["美杉の原木市場（西垣林業）<br/>本人の丸太の販売先"]
    yamaguchi --> misugi
    tokuda -.-> sakurai["桜井の木材市場<br/>大手製材所"]
    yamamoto["山本製材所（神末）<br/>稼働状況・量は不明"]
    forest -.-> yamamoto

    niwa["丹羽製材<br/>既存のパルプ用チップ購入先<br/>CHP燃料としては仕様が不適合"]
    coopcrew -.-> niwa

    mill --> gA["A材 製材用 約22%"]
    mill --> gB["B材 合板用 約54%<br/>行き先未定"]
    mill --> gCD["C・D材 チップ・燃料用 約24%"]

    sawmkt["製材の市場<br/>買い手は不明"]
    plymkt["合板・パルプの買い手<br/>不明"]
    onsen["姫石の湯（温泉）<br/>すでに組合から木材を受け入れ<br/>（等級・量は未確認）"]
    othersup["温泉へのその他の木材供給元？<br/>ある地元の見方：組合だけでは足りない<br/>（未確認）"]
    chp["将来のCHP燃料<br/>プラントは未建設"]
    dc["AIデータセンター（併設）<br/>CHPの電力を24時間使用<br/>需要側接続・試験規模約18kW<br/>＝CHP出力の約2%のみ"]
    grid["系統への売電（FIP）<br/>関西送配電・市場価格＋プレミアム<br/>系統事前相談が必要"]
    dry["CHPの熱でチップを乾燥<br/>牛峠工場で燃料ループに戻す"]
    compute["計算資源の収入<br/>作業班・機械の費用に充当"]

    gA -.-> sawmkt
    gB -.-> plymkt
    gB -.-> chp
    gCD -.-> chp
    gA -.->|"木材（等級はロブの観察）"| onsen
    gB -.->|"木材（等級はロブの観察）"| onsen
    othersup -.-> onsen
    chp -.->|熱| dry
    chp -.->|"電力（優先）"| dc
    chp -.->|"電力（残り）"| grid
    dc -.-> compute

    classDef known fill:#2f6f4f,stroke:#1a4530,stroke-width:1.4px,color:#ffffff
    classDef unknown fill:#4a4a4a,stroke:#999999,stroke-width:1.4px,color:#ffffff,stroke-dasharray:5 4
    classDef future fill:#3a4f7a,stroke:#22315c,stroke-width:1.4px,color:#ffffff,stroke-dasharray:5 4

    class own1,forest,coopcrew,yamaguchi,tokuda,leftover,mill,gA,gB,gCD,misugi known
    class own2,own3,vh,otherindep,miesup,corps,loan,sawmkt,sakurai,yamamoto,plymkt,niwa,onsen,othersup unknown
    class chp,dc,grid,dry,compute,gate,machine future
```

## 未確認事項（「現在何があるか」の実質的な答え）

1. **村有林はあるか？** 2026-08-05に質問、回答なし。
2. **共有地（財産区・入会）は？** 御杖村の記録なし。確認できたのは天川村のみ。
3. **木材の行き先：**個人林業者は美杉市場へ、徳田林産は製材所・桜井市場へ（同社サイト）。組合の流れは未確認。
4. **他に誰が活動しているか？** 個人林業者10以上（本人の推測）、山本製材所（神末）の状況は不明、三重側の事業者は未確認。
5. **徳田林産は村内で伐採しているか、**主に三重・桜井か？ 大場様へ2026-10-09に質問（返信待ち）。
6. **村費の間伐・村有林の事業者はどう選ばれるか？** 2026-10-09に質問。
7. **所有者：**会や意向調査の結果は？ 組合員数・面積は？ 2026-10-09に質問。
8. **組合の経営状況：**資料は未確認。「経営難」は仮説にすぎない。
9. **温泉の木材：**等級・量、組合以外の供給元は？
10. **B材の行き先**（合板か、CHP燃料か）で実際のCHP燃料量が変わる。
11. **組合と検討する提案：**オープンゲート土場、共有ハーベスタ、その所有者。

## この図に含めていないもの（別資料に記載）

- **温泉（姫石の湯）**：現在すでに組合から木材（熱ではなく）を受け入れています。組合の貯木場の様子からA材・B材と見られますが、等級と量は記録がなく未確認です。ある地元の見方として、組合だけでは足りないため温泉は他の場所からも木材を得ているとされています（未確認、供給元は不明）。牛峠工場のCHPから温泉へ熱は送れないため、その線は描いていません。
- **許認可**：伐採届（所有者または立木の買い手が提出、伐採開始の90〜30日前）、森林経営計画（5か年計画、所有者または組合が提出、FIT加算に必要）、森林経営管理制度による村への委託（制度上は可能だが、意向調査は2020年に村長が意図的に見送り）。
- **資金**：森林環境譲与税（年2,600〜3,800万円）→ 施業放置林整備事業（村費による40%間伐、組合受託、放置林約2,600ha）、美しい森づくり補助金（50%補助、後払い、NPOも対象）。
