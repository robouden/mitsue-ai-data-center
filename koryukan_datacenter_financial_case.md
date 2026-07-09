<!-- Version: v1.0 | Last modified: 2026-07-09 -->

# Koryukan Data Center — Financial Case & Hours-of-Use Exception Request

### Making みつえ体験交流館 a financially positive facility via 24-hour data center use + waste-heat reuse

---

## 1. The ask

Two linked requests to むらづくり振興課, building on the 2026-07-08 meeting outcome ([[project_koryukan_workshop]]):

1. **Hours-of-use exception.** The Koryukan's stated hours are weekdays 9:00–17:00, fully reservation-based. But the village already grants an exception: the **Global Human Resource Development School (グローバル人材育成塾)** operates outside these hours as a village program. We request the same treatment for one room, converted to **unmanned, 24/7/365 data center use** — no different in kind from an after-hours village program already running in the building, and lower-impact (no visitors, no noise, no scheduling conflict with ECC or other daytime bookings).
2. **Room allocation.** One existing room (Agricultural Processing Experience Room or a Training Room — smallest footprint, existing power run) repurposed as an unmanned equipment room, racks + battery + small biomass-linked CHP tie-in per [[energy-pivot-2026-05]] and the Sugano hub plan (candidate site #2, `candidate_chp_sites.md`).

**Why this framing matters:** it doesn't ask the village to bend a rule — it asks them to apply a rule they've already bent once.

---

## 2. Usage record, with the data center row added

Village-supplied figures (`Docs extra/Facilities/koryukan_usage_record_2023-2025.csv`) plus a new row showing the data center runs in parallel, not in competition, with existing use — it needs no floor space during ECC/event hours it doesn't already occupy, and needs zero staff time.

| | FY2023 | FY2024 | FY2025 (partial) |
|---|---|---|---|
| ECC (annual) | 1,080 | 1,440 | 1,440 |
| Temp. childcare (annual) | 90 | 90 | 90 |
| Other users (annual) | 253 | 200 | 200 |
| Events (attendance, ad hoc) | ~540 | ~550 | ~370 |
| **Subtotal (existing, annual)** | **1,963** | **2,280** | **2,100** |
| **Data center room — hours/year (proposed)** | — | — | **8,760 (24h × 365d)** |

The last row is the point: the room would be in productive use **100% of the year**, versus the building's existing ~9:00–17:00 weekday-reservation pattern (≈2,080 possible hours/year). No other use in the table comes close to that utilization — which is exactly why it's the lever that can flip the Koryukan's finances.

---

## 3. Cost-saving case: data center waste heat → Koryukan heating

**Mechanism:** an unmanned compute room generates continuous low-grade waste heat (air-cooled IT load ≈ 1:1 electrical-to-thermal). Ducted into the Koryukan's existing spaces, it displaces some or all of the kerosene/electric heating currently paid for during the cold months (roughly Nov–Mar, when ECC, temp. childcare, and events already run).

| Item | Estimate | Basis |
|---|---|---|
| Small edge/AI compute load | 5–10 kWe | Comparable to Tokuo Aomi 10 kW prototype ([[project_tokuo_aomi]]) |
| Recoverable waste heat | ~5–10 kWth continuous | Near 1:1 for air-cooled racks |
| Heating season | ~5 months (Nov–Mar) | Matches existing booked-use months in the record |
| Heat delivered over season | ~18,000–36,000 kWh | 5–10 kWth × ~3,600 hrs |
| Kerosene-equivalent avoided | ~500–1,000 L | 灯油 heating value ≈ 9.8 kWh/L, boiler efficiency ~85% |
| Avoided kerosene cost | **~¥55,000–110,000/yr** | At ~¥110–120/L (illustrative — confirm against village's actual fuel invoices) |

**These are illustrative planning figures, not measured data** — same caveat as the Tokuo Aomi and Mishima-calibrated CHP estimates elsewhere in the project. They need village heating-fuel invoices to firm up; the village has so far declined to share Koryukan financial/business reports, so this line should be presented as a modeled saving to be verified once (if) shared, not asserted as fact.

---

## 4. Building the "financially positive" argument

Three revenue/saving lines, stacked:

1. **Room rental income** — the project pays the standard published rate (Experience/Training Room: ¥600/day full-day, per [[project_koryukan_workshop]] rate card) or a negotiated annual equivalent for guaranteed 24/7 occupancy — a new revenue line the Koryukan doesn't currently have, since none of its existing users book a room for a full year continuously.
2. **Avoided heating cost** — §3 above, offsetting a real operating expense the village currently carries.
3. **No added staffing cost** — unmanned operation means the exception doesn't add to whatever staffing gap makes the village reluctant to extend hours.

Combined, this is the first concrete lever to move the Koryukan from "unknown, suspected deficit" ([[project_koryukan_workshop]]) toward measurable net-positive — without requiring the village to disclose the financials it has declined to share. The pitch can stand on comparing *before* (existing weekday-only revenue-in-kind) vs *after* (existing use unchanged + new rental income + avoided heating cost), rather than on the village's undisclosed baseline.

---

## 5. Next steps

- Submit the hours-of-use exception request to むらづくり振興課, citing the グローバル人材育成塾 precedent explicitly.
- Propose the room + rate in the same submission (Experience Room or Training Room, published or negotiated rate).
- Ask again — narrowly this time — for **heating fuel cost/volume only** (not full financials) to convert §3 from estimate to measured saving.
- Fold into Phase 1 feasibility (WP 57 / JP 164) alongside the Sugano hub siting work already underway.

---

*Sources: village-supplied usage record (`Docs extra/Facilities/koryukan_usage_record_2023-2025.csv`); room rates and hours-of-use policy from village written reply, 2026-07-09; kerosene heating-value conversion (JIS/general reference, ≈9.8 kWh/L); compute load benchmarked against Tokuo Aomi 10 kW prototype.*
