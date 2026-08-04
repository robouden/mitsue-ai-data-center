<!-- Version: v1.0 | Last modified: 2026-08-03 -->

# Network Connectivity for the Mitsue AI Data Center

## Decision

If the AI data center is sold as an external product (compute/inference service to customers, not just internal batch jobs), the network design must be **redundant and SLA-aware**, not a single consumer fiber line.

## Primary line: Komadori Cable (こまどりケーブル)

- Confirmed to serve 御杖村 (Mitsue), incl. as part of the Docomo Hikari Type C coverage map (18 municipalities in Nara).
- Plans (as published on komadori.ne.jp, checked 2026-08-03):
  | Plan | Speed | Price |
  |---|---|---|
  | 光10G | 10 Gbps | ¥6,600/mo (yr 1–3) → ¥5,500/mo (yr 4+) |
  | 光5G | 5 Gbps | ¥5,500/mo (yr 1–3) → ¥4,950/mo (yr 4+) |
  | 光1G | 1 Gbps | ¥6,050/mo flat |
  | 光100Mプレミアム | 100 Mbps | ¥4,950/mo |
- Docomo Hikari 10G Type C (rides Komadori fiber): ¥6,380/mo, 2-yr 戸建て contract.
- **No 法人 (corporate) tier found** on Komadori's public site — no dedicated business menu, no listed SLA/static-IP product. Must confirm by phone (0120-667-740) whether a business-grade option exists for 御杖村 before assuming the consumer plan is sufficient.
- All plans are consumer-grade PON: best-effort, shared/contended, no published SLA, no redundancy.
- No public figure found for Komadori's total subscriber/household count, in Mitsue or overall.

## Failover: Starlink

- Kept as the planned failover uplink alongside Komadori.
- **"V3 = 10Gbps" is a network-capacity figure, not a per-site number.** Each V3 satellite adds ~1 Tbps of aggregate capacity shared across its footprint — not 10 Gbps delivered to one terminal.
- What a terminal would actually see: SpaceX's public target is **gigabit-class (~1 Gbps down) plans**, aimed at 2026, prioritizing enterprise/low-congestion areas first, not a confirmed Japan date.
- V3 satellites require Starship launches; the first V3 batch flew ~July 2026 and is still ramping.
- What has already launched in Japan (April 2026) is **Direct-to-Cell** (KDDI/SoftBank/Docomo partnerships) — satellite-to-phone emergency/remote connectivity, a different product from a business broadband terminal; not usable as a DC uplink.
- **Budget assumption**: today's Gen2/Performance Starlink terminal speeds (~200 Mbps–1 Gbps), not the 10 Gbps satellite-capacity figure. No confirmed Japan gigabit-plan date exists yet.

## Open items

- [ ] Call Komadori (0120-667-740): ask about business/SLA tier for 御杖村, static IP, dedicated bandwidth options.
- [ ] Re-check Starlink Japan gigabit-plan availability closer to procurement time — this is a fast-moving rollout.
- [ ] Don't publish uptime SLA numbers to prospective DC customers until real dual-WAN failover behavior is tested on site.

## Sources / 出典

- https://www.komadori.ne.jp/service/internet/plan.html
- https://www.komadori.ne.jp/service/internet/d-typec/index.html
- https://komadori.ne.jp/company/profile.html
- https://ja.wikipedia.org/wiki/こまどりケーブル
- https://www.theregister.com/2025/07/16/starlink_network_update/
- https://satnews.com/2026/07/13/spacex-advances-direct-to-device-constellation-matrix-with-starlink-v3-hardware/
- https://www.rsinc.com/starlink-roadmap-2026-when-is-gigabit-speed-arriving.php
- https://www.advanced-television.com/2026/04/06/japan-starlink-for-softbank-smartphones/
- https://newsroom.kddi.com/english/news/detail/kddi_nr-533_3818.html
