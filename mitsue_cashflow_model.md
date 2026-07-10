<!-- Version: v1.2 | Last modified: 2026-07-11 -->

<div style="font-family:-apple-system,Helvetica,Arial,sans-serif;">
<p style="font-size:7.5pt; font-weight:600; letter-spacing:0.25em; color:#3a7a5a; margin:0 0 4mm;">PROJECT DOCUMENT</p>
<h1 style="font-size:28pt; font-weight:700; margin:0 0 2mm; border-bottom:1px solid #eee; padding-bottom:2mm;">BIOMASS ENERGY & AI</h1>
<p style="font-style:italic; color:#666; margin:1mm 0 0;">Reforesting in Mitsue</p>
<p style="font-style:italic; color:#666; margin:2mm 0 8mm;">Cashflow Model — Inflow vs. Outflow</p>
<img src="assets/logo_go.png" alt="御" width="50%" style="display:block;margin:0 auto;">
</div>

<div style="page-break-after:always; break-after:page; height:0; margin:0; padding:0;"></div>

# BIOMASS ENERGY & AI — Cashflow Model

### Reforesting in Mitsue · Inflow planned against the monthly cost baseline

*This document adds the **cash-in** side to the project's already-detailed **cash-out** timeline (the EVM monthly S-curve, `mitsue_evm_plan.md` §4). Its single design rule: **the cumulative balance must never fall to zero in any month.** Outflow is smooth and monthly; inflow arrives in **big, lumpy chunks** — founder capital, grants, subsidies, corporate/loan tranches — until operating revenue begins near the end of Phase 3.*

---

## 1. The design rule

> **Every month: cumulative cash-in − cumulative cash-out ≥ a positive working-capital floor.**

Because spending is continuous but funding arrives in lumps, each tranche must **land in or before the month the balance would otherwise breach the floor.** We target a **minimum floor of ~¥3–5M** early (Phases 0–1, when monthly burn is tiny) and a larger absolute buffer through Phase 3 (when burn peaks at ¥25M/month — a single late tranche can blow a ¥25M hole in one month).

All figures are illustrative, consistent with the EVM PMB (BAC ¥220M) and the funding stack (¥192M target, ¥28M gap if the target is fully realized). **None of the ¥192M is secured yet** — including the ¥6M founder-capital layer. They set the **shape and timing** of inflow, not vetted amounts — Phase 1 feasibility + confirmed grant awards replace them at Baseline Rev 2 (Dec 2026).

---

## 2. Cash-out recap (from EVM §4)

Monthly planned spend, front-loaded on studies/design, peaking in construction (M22–M28). Cumulative reaches the ¥220M BAC at M30.

| Phase | Months | Spend in phase | Cum. spend by phase-end |
|---|---|---|---|
| P0 Pre-Foundation | M1–M3 | ¥0.25M | ¥0.25M |
| P1 Foundation | M4–M9 | ¥5.5M | ¥5.75M |
| P2 Pilot Design | M10–M18 | ¥22.5M | ¥28.25M |
| P3 Pilot Build | M19–M30 | ¥191.75M | ¥220.0M |

Peak monthly burn: **¥25M/month at M25–M26** (Apr–May 2028).

---

## 3. Inflow tranche schedule (recommended)

Funding is drawn down as **11 lumps**, each timed to a funding gate or to the month a spend wave begins. Sources map to the funding stack (L1–L5) plus a bridge/working-capital tranche.

| Month | Cal | Tranche | ¥M | Source layer | Rationale / trigger |
|---|---|---|---|---|---|
| M1 | Apr 2026 | Seed | 6 | L1 Founders | Founder capital — sole runway for Phases 0–1 |
| M8 | Nov 2026 | Planning grant | 5 | L2 Gov | First small grant, unlocked by early feasibility work; lands before Gate 2 |
| M9 | Dec 2026 | Foundation 1 | 15 | L3 Foundations | Legal entity registered (P1) unlocks foundation grants |
| M12 | Mar 2027 | Gov grant 1 | 20 | L2 Gov | Feasibility studies unlock national/pref. grants |
| M15 | Jun 2027 | Corporate 1 | 15 | L4 Corporate | CSR / prepaid hosting / minority GK equity |
| M18 | Sep 2027 | 交付金 / Gov 2 | 30 | L2 Gov | MoE decarbonization 交付金, first disbursement via village |
| M21 | Dec 2027 | 交付金 / Gov 3 | 40 | L2 Gov | Main capex subsidy — **lands at Phase 3 start**, before peak burn |
| M23 | Feb 2028 | Corporate 2 | 22 | L4 Corporate | Equity/offtake tranche 2 (post-pilot-progress) |
| M25 | Apr 2028 | 交付金 / Gov 4 | 30 | L2 Gov | Capex subsidy tranche 2 at peak-burn month |
| M26 | May 2028 | **Bridge / gap** | 18 | Loan / MR | **Working-capital + gap-closing** (see §5) |
| M27 | Jun 2028 | Foundation 2 | 25 | L3 Foundations | Second foundation tranche / gap-closing |
| M28–M30 | Jul–Sep 2028 | Operating revenue | 3 | L5 Revenue | Pilot online — first energy/DC/EV income (¥1M/mo) |
| | | **Total in** | **229** | | Covers ¥220M BAC + ~¥9M end buffer |

---

## 4. Monthly running balance (recommended schedule)

The balance stays **positive every month**, with the thinnest point at **M7 (¥3.05M)** — just before the first grant lands.

| Month | Cal | Cash-out (mo) | Cum-out | Cash-in (mo) | Cum-in | **Balance** |
|---|---|---|---|---|---|---|
| M1 | Apr'26 | 0.05 | 0.05 | 6 | 6 | **5.95** |
| M2 | May'26 | 0.10 | 0.15 | — | 6 | 5.85 |
| M3 | Jun'26 | 0.10 | 0.25 | — | 6 | 5.75 |
| M4 | Jul'26 | 0.20 | 0.45 | — | 6 | 5.55 |
| M5 | Aug'26 | 0.50 | 0.95 | — | 6 | 5.05 |
| M6 | Sep'26 | 0.80 | 1.75 | — | 6 | 4.25 |
| M7 | Oct'26 | 1.20 | 2.95 | — | 6 | **3.05 ◀ floor** |
| M8 | Nov'26 | 1.50 | 4.45 | 5 | 11 | 6.55 |
| M9 | Dec'26 | 1.30 | 5.75 | 15 | 26 | 20.25 |
| M10 | Jan'27 | 1.50 | 7.25 | — | 26 | 18.75 |
| M11 | Feb'27 | 2.20 | 9.45 | — | 26 | 16.55 |
| M12 | Mar'27 | 2.80 | 12.25 | 20 | 46 | 33.75 |
| M13 | Apr'27 | 3.00 | 15.25 | — | 46 | 30.75 |
| M14 | May'27 | 3.00 | 18.25 | — | 46 | 27.75 |
| M15 | Jun'27 | 3.00 | 21.25 | 15 | 61 | 39.75 |
| M16 | Jul'27 | 2.50 | 23.75 | — | 61 | 37.25 |
| M17 | Aug'27 | 2.50 | 26.25 | — | 61 | 34.75 |
| M18 | Sep'27 | 2.00 | 28.25 | 30 | 91 | 62.75 |
| M19 | Oct'27 | 4.00 | 32.25 | — | 91 | 58.75 |
| M20 | Nov'27 | 7.00 | 39.25 | — | 91 | 51.75 |
| M21 | Dec'27 | 11.00 | 50.25 | 40 | 131 | 80.75 |
| M22 | Jan'28 | 16.50 | 66.75 | — | 131 | 64.25 |
| M23 | Feb'28 | 20.50 | 87.25 | 22 | 153 | 65.75 |
| M24 | Mar'28 | 20.50 | 107.75 | — | 153 | 45.25 |
| M25 | Apr'28 | 25.00 | 132.75 | 30 | 183 | 50.25 |
| M26 | May'28 | 25.00 | 157.75 | 18 | 201 | 43.25 |
| M27 | Jun'28 | 20.50 | 178.25 | 25 | 226 | 47.75 |
| M28 | Jul'28 | 20.50 | 198.75 | 1 | 227 | 28.25 |
| M29 | Aug'28 | 14.00 | 212.75 | 1 | 228 | 15.25 |
| M30 | Sep'28 | 7.25 | 220.00 | 1 | 229 | **9.00** |

**Two binding constraints the schedule is built around:**
1. **M7 (Oct 2026) — the early pinch.** Planned founder capital (¥6M, not yet committed) is modeled as the *only* money in for the first 7 months. If it is not actually secured by then, or the M8 planning grant slips, or early spend overruns, the balance breaches zero here. *Mitigant: commit founder/seed capital ≥¥6M before Phase 0 spend begins, or secure a small Gate-1 bridge by M7.*
2. **M21–M27 (Phase 3) — the burn cliff.** At ¥20–25M/month, cash-in timing risk is severe: a one-month grant delay = a ¥25M hole. Every Phase-3 tranche must be **contracted well ahead of its landing month**, because grants often pay *in arrears*. *Mitigant: front-load the 交付金 tranche to M21 (Phase-3 start) and hold the bridge (§5) as the shock absorber.*

---

## 5. The target-stack-only reality: where it runs dry

This is the **best case**, not a floor: it assumes the full ¥192M target stack lands exactly as planned, with no gap-closing tranche. **None of the ¥192M is secured today.** Even in that best case, the balance goes **negative at M28 (Jul 2028)** and bottoms at **−¥28M at M30** — i.e. the end-of-project shortfall is *exactly* the known ¥28M funding gap. If the target stack itself is not fully realized, the shortfall is larger and arrives sooner.

| Month | Cum-out | Cum-in (target stack only) | Balance |
|---|---|---|---|
| M26 | 157.75 | 171 | +13.25 |
| M27 | 178.25 | 189 | +10.75 |
| **M28** | **198.75** | **190** | **−8.75 ◀ runs dry** |
| M29 | 212.75 | 191 | −21.75 |
| M30 | 220.00 | 192 | **−28.00** (= the gap) |

**Implication:** the ¥28M gap is not an abstract "shortfall vs BAC" — it is a **cash wall in July 2028.** To keep the balance positive through construction, the gap must be **secured *and* scheduled to disburse before M28**, and prudently by **Gate 3 (M21)** given the pay-in-arrears risk. This is why §3 places a bridge/gap tranche at M26 and a foundation tranche at M27.

---

## 6. Initial inflow = chunks, not monthly

As the framing notes, early inflow is **lumpy, not monthly**:

- **Phases 0–2 (M1–M18):** 100% of inflow is founder capital + grants + subsidies + corporate/loan tranches. **Zero operating revenue.** Six lumps totalling ¥91M carry the project to the start of construction.
- **Phase 3 (M19–M30):** still dominated by lumps (¥135M across four tranches), with the **first trickle of operating revenue (¥1M/month) only from M28** as the pilot energises.
- **Phase 4 (M31+, out of this baseline):** the model flips — operating revenue (FIT electricity, heat, DC hosting, EV, broadleaf/J-Credit) becomes the primary monthly inflow and funds the CHP scale-up. See `mitsue_revenue_model.md` and EVM §14.

**Loans/bridge financing** matter precisely at the seams between lumps. Because grants commonly pay *on milestone completion* (arrears), a **bridge facility** sized to ~1 month of peak burn (**~¥25M**) lets the project spend against a *committed-but-not-yet-disbursed* grant without the balance dipping. The M26 tranche in §3 plays this role; it can be a bank bridge loan, a draw on the ¥25M Management Reserve, or an advance against a signed 交付金.

---

## 7. Recommendations

1. **Adopt the ~¥3–5M early floor and the Phase-3 buffer as hard rules** in the monthly EVM report — track *balance*, not just spend.
2. **Close the ¥28M gap before Gate 3 (M21),** not at end-of-project. Until the target stack is actually secured, the target-stack-only line (§5) is the *best-case* forecast and it still fails in M28.
3. **Contract every Phase-3 tranche 2–3 months ahead of its landing month** to absorb grant pay-in-arrears lag.
4. **Arrange a ~¥25M bridge facility** (bank line, MR draw, or grant advance) as the shock absorber for the burn cliff.
5. **Re-time this model to the live Gantt at Baseline Rev 2 (Dec 2026)** alongside the cost re-sync, and fold in confirmed 交付金 amounts and any loan terms.

> **Status — adopted.** All five are now encoded as governing rules in the EVM plan (v2.7): liquidity floor → §8.1; monthly balance-vs-floor reporting → §9; gap-before-Gate-3, tranche 2–3-month lead time, and ~¥25M bridge facility → §10 assumptions/constraints; cashflow re-time + 交付金/loan terms → §12 Rev 2 scope. The Gate-3 timing rule is also flagged in the funding flowchart (v2.8). *Remaining as a live action:* actually arranging the bridge facility (bank line / MR / grant advance) before Gate 3 — a Phase 2 funding task, not yet secured.

---

## Sources & status

Cash-out figures: `mitsue_evm_plan.md` §4 (Baseline Rev 1). Funding stack: `mitsue_phases_funding_flowchart.md` (¥192M target, ¥0 secured, ¥28M gap if fully realized). Tranche amounts and months are illustrative planning figures, not committed disbursement dates — to be replaced by confirmed grant/loan schedules at Baseline Rev 2. Operating-revenue onset per `mitsue_revenue_model.md`.

---

*Rob Oudendijk — YR-Design / Safecast · Mitsue, Nara Prefecture, Japan · July 2026*
