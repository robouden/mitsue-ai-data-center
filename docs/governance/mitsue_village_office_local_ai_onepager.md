<!-- Version: v1.0 | Last modified: 2026-07-25 -->

# 役場のためのローカルAI — 村のデータを外に出さずに
# Local AI for the Village Office — without your data ever leaving Mitsue

村営データセンターで、**役場専用のAI**を動かせます。データは村の外に出ず、
利用料（従量課金）もありません。
The village-owned data center can run **AI for the village office** — data never
leaves Mitsue, and there is **no per-use vendor fee**.

---

## 課題 / The problem

ChatGPT など市販のクラウドAIは便利ですが、入力したデータは村外・海外のサーバーに
送られます。住民情報・税・福祉などの**個人情報**は、そこに預けられません。
そのため多くの自治体はAI活用に踏み出せずにいます。

Commercial cloud AI (ChatGPT, etc.) sends whatever you type to servers outside the
village — often overseas. **Personal data** (resident records, tax, welfare) legally
cannot go there, which is exactly why most small municipalities are stuck on AI.

## 解決策 / The solution

村内のデータセンターで、**オープンな（無償利用可能な）AIモデル**を稼働させます。
データは村内で処理され、外部に一切送信されません。電力はバイオマスCHPが村内で
発電するため、**問い合わせごとの費用はゼロ**です。

Run an **open-weight (free-to-use) AI model** inside the village data center. Data
is processed locally and never transmitted outside. Because the biomass CHP
generates the power locally, there is **zero cost per query** — no subscription that
grows with headcount.

## 使い方の例 / Example uses

- 広報・お知らせ・**交付金申請書**の下書き / Draft 広報, notices, grant applications
- **議会議事録**などの長文要約 / Summarize 議会 minutes and long documents
- 外国人住民・観光客向けの**翻訳**（日⇄英ほか） / Translation for foreign residents & tourists
- 住民向けの**手続き案内チャット** / A resident-facing services FAQ assistant

## 規模と電力 / Scale & power

役場の利用は少量のため、小型構成で十分です。GPU 1〜2台・消費電力 約2〜6 kW ——
CHPのベースロードで賄えます。K3級の大型モデルは不要です。

Government use is low-volume, so a small setup suffices: **1–2 GPUs, ~2–6 kW** —
easily covered by the CHP baseload. No K3-scale cluster needed.

## 前提条件 / What's required first

- **認証・アクセス管理・データ取扱い方針**の整備（ローカル化は必要条件であり十分条件ではない）
  Auth, access control, and an official data-handling policy (local ≠ automatically safe)
- **人による確認**を前提とする（AIは下書き支援であり、行政判断は行わない）
  Human-in-the-loop — AI assists drafting, it does not make administrative decisions

## なぜ村にとって得か / Why it's the village's own asset

これは外部事業者のサービスではなく、**村自身のITインフラ**になります。
森林・エネルギーと同じく「地域が所有し、透明に運用する」仕組みです。
Not an outside vendor's service — **the village's own IT infrastructure**, owned and
transparently run, like the forest and energy pillars.

## 次の一歩 / Next step

役場の実務で「これに使えたら助かる」業務を1〜2件挙げていただければ、
小規模な試行（パイロット）の設計に入れます。
Name one or two office tasks where this would help, and we can scope a small pilot.

---

## 出典 / Sources

- オープンウェイトモデル例 Kimi K3（Modified MIT ライセンス）: https://kimi-k2.org/blog/31-kimi-k3-open-weights-july-27
- ライセンス条件の解説: https://miraflow.ai/blog/kimi-k2-6-explained-moonshot-ai-open-source-model-ties-gpt-5-5-coding
- 詳細な構成・規模の検討: [local_llm_serving_options.md](../strategy/local_llm_serving_options.md)
