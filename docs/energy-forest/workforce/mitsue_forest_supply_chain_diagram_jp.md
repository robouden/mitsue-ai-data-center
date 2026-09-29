<!-- Version: v1.4 | Last modified: 2026-09-30 -->

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

    coopcrew["森林組合の現場班<br/>2名、平均年齢約33歳"]
    yamaguchi["個人の林業者<br/>活動を確認済み・自伐型林業<br/>地域おこし協力隊（林業部門）<br/>随時・所有者からの依頼"]
    otherindep["その他の個人林業者？<br/>村内に何人いるか<br/>2026-09-29に質問・回答待ち"]
    corps["地域おこし協力隊 自伐型林業<br/>任期最長3年<br/>過去2年は採用ゼロ"]
    loan["村の林業用重機貸与<br/>バックホウ＋ダンプ<br/>任期後最長5年・1日1,000円"]

    forest --> coopcrew
    forest --> yamaguchi
    forest -.-> otherindep
    forest -.-> corps
    corps -.-> loan
    loan -.-> yamaguchi

    leftover["林内に残置<br/>間伐は年約66haだが<br/>搬出は年約120〜300m3のみ"]
    coopcrew -->|間伐| leftover

    mill["牛峠工場<br/>組合のチップ・乾燥加工センター"]
    coopcrew -->|"年約120〜300m3"| mill
    yamaguchi -.->|"出荷先は不明・回答待ち"| mill
    otherindep -.-> mill

    niwa["丹羽製材<br/>既存のパルプ用チップ購入先<br/>CHP燃料としては仕様が不適合"]
    yamaguchi -.-> niwa
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

    class own1,forest,coopcrew,yamaguchi,leftover,mill,gA,gB,gCD known
    class own2,own3,otherindep,corps,loan,sawmkt,plymkt,niwa,onsen,othersup unknown
    class chp,dc,grid,dry,compute future
```

## 未確認事項（「現在何があるか」の実質的な答え）

1. **村有林** ― 民間との契約なしで使える村有林はあるか。2026-08-05に観光協会へ質問済み、回答なし。
2. **財産区・入会（共有地）** ― 御杖村に存在する形跡なし。確認できた例は天川村の洞川財産区のみ。御杖村にもあると想定しないこと。
3. **個人林業者が伐採した木材の行き先** ― 製材所・チップ業者・市場のどれか。2026-09-29に質問済み、回答待ち。
4. **確認済みの1名以外に、村内で活動する個人林業者は何人いるか** ― 1名の活動は確認済み、他は未確認。2026-09-30にむらづくり振興課へ問い合わせ済み。
5. **「3年／6年」の契約形態** ― 出典があるのは、地域おこし協力隊の任期上限3年と、任期後の重機貸与の5年のみ。「6年」の根拠はどの資料にもなし。
6. **B材の行き先**（合板の買い手か、CHP燃料か）― 実際のCHP燃料量に影響する。

## この図に含めていないもの（別資料に記載）

- **温泉（姫石の湯）**：現在すでに組合から木材（熱ではなく）を受け入れています。組合の貯木場の様子からA材・B材と見られますが、等級と量は記録がなく未確認です。ある地元の見方として、組合だけでは足りないため温泉は他の場所からも木材を得ているとされています（未確認、供給元は不明）。牛峠工場のCHPから温泉へ熱は送れないため、その線は描いていません。
- **許認可**：伐採届（所有者または立木の買い手が提出、伐採開始の90〜30日前）、森林経営計画（5か年計画、所有者または組合が提出、FIT加算に必要）、森林経営管理制度による村への委託（制度上は可能だが、意向調査は2020年に村長が意図的に見送り）。
- **資金**：森林環境譲与税（年2,600〜3,800万円）→ 施業放置林整備事業（村費による40%間伐、組合受託、放置林約2,600ha）、美しい森づくり補助金（50%補助、後払い、NPOも対象）。
