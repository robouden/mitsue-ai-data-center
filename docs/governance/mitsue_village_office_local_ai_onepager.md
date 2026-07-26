<!-- Version: v1.1 | Last modified: 2026-07-25 -->

# Local AI for the Village Office — without your data ever leaving Mitsue

The village-owned data center can run **AI for the village office** — data never
leaves Mitsue, and there is **no per-use vendor fee**.

---

## The problem

Commercial cloud AI (ChatGPT, etc.) sends whatever you type to servers outside the
village — often overseas. **Personal data** (resident records, tax, welfare) legally
cannot go there, which is exactly why most small municipalities are stuck on AI.

## The solution

Run an **open-weight (free-to-use) AI model** inside the village data center. Data
is processed locally and never transmitted outside. Because the biomass CHP
generates the power locally, there is **zero cost per query** — no subscription that
grows with headcount.

## Example uses

- Draft 広報 (public notices), announcements, and **grant applications** (交付金)
- Summarize 議会 (assembly) minutes and other long documents
- **Translation** for foreign residents and tourists (Japanese ⇄ English and more)
- A resident-facing **services FAQ assistant**

## Scale & power

Government use is low-volume, so a small setup suffices: **1–2 GPUs, ~2–6 kW** —
easily covered by the CHP baseload. No large K3-scale cluster is needed.

## What's required first

- **Authentication, access control, and an official data-handling policy** — running
  the model locally is necessary but not automatically sufficient for safety.
- **Human-in-the-loop** — the AI assists with drafting; it does not make
  administrative decisions (this avoids the risk of AI "hallucinations").

## Why it's the village's own asset

This is not an outside vendor's service — it becomes **the village's own IT
infrastructure**, owned and transparently run, like the forest and energy pillars of
the project.

## Next step

Name one or two office tasks where this would help, and we can scope a small pilot.

---

## Sources

- Open-weight model example, Kimi K3 (Modified MIT license): https://kimi-k2.org/blog/31-kimi-k3-open-weights-july-27
- License terms explained: https://miraflow.ai/blog/kimi-k2-6-explained-moonshot-ai-open-source-model-ties-gpt-5-5-coding
- Full configuration & sizing analysis: [local_llm_serving_options.md](../strategy/local_llm_serving_options.md)
ok
