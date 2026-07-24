<!-- Version: v1.0 | Last modified: 2026-07-24 -->

# FAQ + Goals: Free Compute, Transparency, and Impact Targets

Follow-up questions from Tara Brown (Safecast), 2026-07-24. Companion to
[2026-07-20_data-center-community-participation.md](2026-07-20_data-center-community-participation.md).
These answers are captured as project **principles/goals** and mapped to
OpenProject phases below.

## Q1: Why not just make community compute free for everyone and see what happens?

- **Goal adopted.** Launch community compute **free, no quotas, no login gates,
  no billing** on day one. With ~1,400 people and an aging population, real
  demand is small; a rationing system now would be over-engineering for a
  problem that may never occur.
- Add a simple per-user limit **only if** monitoring later shows one/two heavy
  users crowding others out. "Watch first, gate later."

## Q2: Is the goal to bring new people to Mitsue, or help existing residents?

- **Primary: existing residents** and the forestry co-op — give people already
  there reasons and income to stay, against ongoing depopulation.
- **Secondary/bonus: in-migration** — if forestry work + a small tech footprint
  + remote-work-friendliness later attract a few younger residents, welcome, but
  not the headline goal.

## Q3: Why build our own tree app instead of NASA's GLOBE?

- **Don't reinvent GLOBE.** It is strong for scientific tree-height measurement
  and a global dataset. Our app serves a different job: a village forest
  **inventory tied to our restoration plan** — which plots replanted, which
  native species, by which volunteer, photos over time — in a bilingual (JP/EN)
  UI simple enough for schoolkids and elderly volunteers, with locally-owned data.
- **Action:** evaluate using **GLOBE for the measurement layer** and keeping our
  lightweight app for the inventory/engagement layer, rather than duplicating
  GLOBE. (Owner: tree-survey app track.)
- Link: https://www.nasa.gov/centers-and-facilities/goddard/help-nasa-measure-trees-with-your-smartphone/

## Q4: Will you name the outside companies using the data center?

- **Goal: yes, name them.** Publish who the compute tenants are, not just
  anonymous numbers — transparency on who uses village resources is the point.
- Only exception: a tenant under a normal confidentiality clause — even then,
  disclose the aggregate and that such a tenant exists. Extends the public
  local/outside split already in the community-participation FAQ (Q3 there).

## Q5: Does this matter more for Mitsue, or as a model others copy?

- **Mitsue first** — it must work for one real village before it means anything;
  never treated as a demo.
- **But** the replicable model for other depopulating forest villages is
  arguably the bigger prize. Design for copyability without sacrificing Mitsue.

## Q6: Any people/forest targets by year, not just revenue/phases?

- **Honest status: a real gap.** Current targets skew to money and phases.
- Directional metrics to formalize: active volunteers/users, **hectares
  replanted/yr** with native broadleaf, thinnings-to-energy tonnage.
- Hectare targets to be set with **more trees** during Phase 1 forestry
  feasibility (indicative scope already: 5–10 ha Phase 3, 20–40 ha Phase 4).

---

## OpenProject Phase Mapping

Where each goal enters the operative plan (phase spine per
[implementation plan](../strategy/mitsue_implementation_plan.md)). Suggested
work packages for OpenProject (EN project id 3 / JP id 4).

| # | Goal | Phase | Suggested WP / action |
|---|------|-------|-----------------------|
| Q1 | Free-first community compute (no gating) | **P2 Pilot Design → P3 Build** | WP: "Community compute access policy — free-first, monitor-then-gate"; design in P2, ship with pilot in P3 |
| Q2 | Serve existing residents (retention) first | **P0–P1 (framing)** | Fold into project charter / stakeholder framing; no new WP, tag existing outreach WPs |
| Q3 | GLOBE-for-measurement vs own inventory app | **P1 Feasibility** | WP: "Field-data tooling review — GLOBE integration vs custom app scope"; decision in tree-survey track |
| Q4 | Name tenants / public transparency | **P2 → P4 (operate)** | WP: "Public transparency dashboard — tenant naming + local/outside split"; spec in P2, live in P4 ops |
| Q5 | Replicable model for other villages | **P4 (+ ongoing)** | Add "replicability / open playbook" as a P4 deliverable; capture lessons from P1 onward |
| Q6 | People + forest impact targets by year | **P1 Feasibility (with more trees)** | WP: "Impact KPI set — volunteers, ha replanted/yr, thinnings tonnage"; baseline in P1, into EVM Rev 2 (Dec 2026) |

**Fastest to log now (Phase 0/1 live):** Q3 (tooling review), Q6 (KPI set) — both
feed the Phase 1 feasibility studies already being scoped. Q1/Q4 are design-time
(Phase 2) but worth a placeholder WP so they aren't lost.
