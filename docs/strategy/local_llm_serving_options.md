<!-- Version: v1.0 | Last modified: 2026-07-25 -->

# Local LLM Serving — Options & Sizing for the Mitsue Community Data Center

Planning note: what it takes to run a **local, open-weight LLM** on the
village-owned data center, for three user segments — **residents**, the **local
government (御杖村役場)**, and **paying outside tenants**. Sizing is tied to the
biomass-CHP power budget. Figures are planning estimates for Phase-3 design; a
Phase-1/2 feasibility study replaces them with vetted numbers.

## 1. Why open-weight models change the economics

Frontier-class models are now released as **open weights** under permissive
licences, so the village can self-host with **no per-token vendor fee and no data
leaving Mitsue**. Example: **Moonshot Kimi K3** (2.8T-parameter MoE, released
2026-07-16, open weights ~2026-07-27) ships under a **Modified MIT License** —
plain MIT for anyone below ~100M monthly active users / ~$20M monthly revenue
(i.e. everyone here), with only a UI-attribution clause above that.

**Strategic asset:** an open, locally-run stack means the village's AI has no
subscription that scales with use, and sensitive data never touches an overseas
cloud. This is the same "local resource, transparently owned" story as the forest
and energy pillars — see the website Programme pillar iii.

## 2. Two-tier sizing

| | **Tier A — Right-sized (recommended)** | **Tier B — Frontier (e.g. Kimi K3)** |
|---|---|---|
| Model | 30–70B open model, Japanese-capable (Qwen2.5-72B / Llama-3.3-70B / JP-tuned), 4-bit | ~2.8T-param open-weight (Kimi K3), 4-bit ≈ ~1.4 TB weights |
| GPUs | **1–2** (2× H100 80GB, or RTX 6000 Ada / consumer for the 30B tier) | **16–24** (2–3 DGX-class nodes) |
| Power (load) | **~2–6 kW** | **~20–30 kW** |
| Capex (box) | **~$15k–60k** | **~$0.5–1M+** |
| Fits residents/gov use? | **Yes** — low concurrency, plenty good | Overkill; only for a paying tenant wanting frontier compute |

Both fit inside the CHP envelope (memory: lean ~18 kW node → 0.3–0.8 MW GPU
cluster). Tier A sips a few kW off the biomass baseload; Tier B is an industrial
deploy justified only by outside revenue.

## 3. User segments

**A. Residents (free village AI).**
Tier A model + a private local chat page on the village network. Q&A, drafting,
translation, learning tools — in Japanese, data stays in the village. Delivers the
"free community access" promise (Programme pillar iii). Ties to the tree-survey /
school-outreach threads as a "build something on the village computer" hook.

**B. Local government (御杖村役場) — arguably the strongest institutional case.**
- **Solves a real compliance blocker:** municipal data (個人情報, tax, welfare)
  can't be pasted into ChatGPT / overseas clouds. A local, air-gappable model lets
  the office use AI on documents it legally can't put in a commercial cloud.
- **No per-seat fee** on a tiny municipal budget — pays only for CHP electricity.
- **Use cases:** draft 広報/notices/交付金 applications; summarize 議会 minutes;
  translate for foreign residents/tourists; a resident-facing services FAQ bot.
- **Strategy:** flips push→pull — the DC becomes the village's *own* IT
  infrastructure, not an outsider's project (pairs with the Koryukan "facility
  should earn its keep" framing and the village-pull strategy).
- **Caveats to stay credible:** needs auth + access-control + an official
  data-handling policy first (data-stays-local is necessary, not sufficient); keep
  a **human in the loop** for anything official (hallucination risk). Low volume →
  same **Tier A** box.

**C. Paying outside tenants.**
The revenue leg. A tenant wanting frontier compute (Tier B / Kimi K3) can be hosted
with no licence fee because the weights are open; residents/gov can ride the same
hardware. This is the only case that justifies a K3-scale cluster.

## 4. Serving stack

- **Throughput:** vLLM or SGLang (also TensorRT-LLM) — what Kimi/Qwen/Llama target.
- **Simple/small-team:** Ollama or llama.cpp for the 30B tier.
- **Access:** private web chat UI, village-network-only; per-user login (reuse the
  tree-survey app's auth pattern).

## 5. Phase mapping

| Item | Phase |
|---|---|
| Tier A resident + gov pilot (30–70B, 1–2 GPUs) | **P3 Pilot Build** (spec in P2) |
| Village-office data-handling / access policy | **P2 → P3** (prereq for gov adoption) |
| Tier B / Kimi-K3-scale for paying tenant | **P4 Operate & Scale** (tenant-driven) |
| Feasibility: model choice, JP eval, real power draw | **P1–P2 feasibility** |

## Sources / 出典

- Kimi K3 specs (2.8T params, largest open-weight): https://www.tomshardware.com/tech-industry/artificial-intelligence/moonshot-releases-2-8-trillion-parameter-kimi-k3
- Kimi K3 open weights ~2026-07-27: https://kimi-k2.org/blog/31-kimi-k3-open-weights-july-27
- Kimi K2/K3 Modified MIT license terms: https://miraflow.ai/blog/kimi-k2-6-explained-moonshot-ai-open-source-model-ties-gpt-5-5-coding
- Moonshot unveils Kimi K3 (CNBC): https://www.cnbc.com/2026/07/17/moonshot-ai-kimi-k3-model-openai-anthropic-china.html
