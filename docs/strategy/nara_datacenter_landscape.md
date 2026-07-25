<!-- Version: v1.0 | Last modified: 2026-07-22 -->

# Nara / Keihanna Data Center Landscape — Verified Reference

Verified 2026-07-22 against operator sites and Nara Prefecture. **Correcting an
earlier AI-generated draft** ([nara_smallscale_dc_directory_UNVERIFIED.md](nara_smallscale_dc_directory_UNVERIFIED.md))
that invented facility names, made up "0.5–1.0 MW" power allocations, and cited
unusable Google search-UI links.

## ⚠️ Headline correction
There is **no cluster of 0.5–1.0 MW "small-scale" data centers in Nara.** Every
real facility in/near Nara is **large-to-hyperscale (30–50 MW).** The small-MW tier
in the original table was fabricated. For Mitsue's sub-1 MW biomass-powered node,
these are **context/benchmarks and funding precedents — not peers.**

## Funding — the most useful confirmed finding

**Nara Prefecture Data Center Location Promotion Subsidy** (データセンター立地促進補助金)
— [pref.nara.lg.jp/n100/63527.html](https://www.pref.nara.lg.jp/n100/63527.html)
- Grant = **5% of fixed-asset investment, capped at ¥200M (2億円).**
- Eligibility: **≥¥500M fixed-asset investment** (excludes land), **≥10 new local
  jobs**, operations to start **within 3 years** of construction start.
- Contact: Nara Pref. Industrial Creation Division (産業創造課).
- **Relevance to Mitsue:** the ¥500M capex floor and 10-job minimum are steep for a
  sub-1 MW node alone — likely need to bundle CHP + compute + fuel-prep capex, or
  treat this as a stretch/scale-up track. Worth a direct call to confirm whether a
  village-scale AI+biomass build qualifies. Pairs with our METI GX / MoE tracks
  ([[reference_fy2026_subsidy_tracks]]).

## Verified facilities (real specs)

### IDC Frontier — Nara Ikoma Data Center (奈良生駒データセンター)
[idcf.jp/datacenter/location/ikoma](https://www.idcf.jp/datacenter/location/ikoma/)
- **50 MW** total receiving capacity; ~**40,000 m²** floor area.
- Racks: air-cooled **9–30 kVA/rack**; **direct liquid cooling (DLC) 50–120 kVA/rack**.
- Hybrid air + DLC with hot-aisle containment; **built for AI/GPU**.
- Base-isolated (M6.5+), 1.8 km from active faults, 135 m elevation.
- N+1 gensets (72 hr), UPS, dual utility lines, carrier-neutral, facial-recognition.
- Opened Dec 2020. **DC business transferred to SoftBank Corp. effective 2026-04-01.**
- **Use as:** the closest real precedent for a Nara AI/GPU + liquid-cooling site;
  benchmark rack densities and resilience spec.

### Colt DCS — Osaka Keihanna Data Centre
[coltdatacentres.net → Osaka Keihanna](https://www.coltdatacentres.net/en-GB/our-locations/data-centre-locations-asia/osaka-keihanna)
- **45 MW** IT power; ~**42,000 m²** gross site; up to **2.6 MW per data hall**.
- Tier 3, **base-isolation** (withstands JMA intensity 7), peak **PUE < 1.6**.
- Keihanna Science City (Kyoto/Osaka/Nara tri-prefecture zone); live early 2023.
- **Use as:** hyperscale AI/cloud benchmark; the "avoid urban grid, keep Kansai
  latency" siting logic is real (60 min to Osaka/Kyoto/Nara).

### NTT DATA / NTT GDC — Keihanna OSK11
[services.global.ntt → Keihanna OSK11](https://services.global.ntt/en-us/services-and-products/global-data-centers/global-locations/asia-pacific/keihanna-osk11-data-center)
- **30 MW** IT capacity; **10,900 m²** server-room space.
- Located **Seika-cho, Soraku-gun, KYOTO** (~94 m elevation) — *not* Nara.
- AI-ready, N+1 air-cooled chillers, multicarrier, 24/7 security. **Opened 2026-04-09.**
- **Use as:** newest Kansai AI-ready hyperscale reference.

### Kistem Co., Ltd. (キステム株式会社, Nara HQ; ex-奈良情報システム)
[kistem.com](https://www.kistem.com/) · DC notice [frmId=78](https://www.kistem.com/contents_detail.php?co=new&frmId=78)
- Real **regional** operator; cloud-compatible DC in Nara (ops since ~2013, plus a
  newer facility). Earthquake-resistant, redundant power, BCP/security focus.
- HQ actually in Shiga; offices Nara/Osaka/Okayama. (Unrelated to a Tokyo security
  firm of the same name.)
- **Use as:** the only genuinely *regional-scale* Nara DC operator — the nearest
  analog to a small local node, and a possible peer/partner to study.

## Fabricated / unconfirmed rows from the original table (do NOT use)
- **"NTT West Omiya Node BCP Room"** and **"Fujitsu Omiya-cho Solutions Vault"** —
  no such data centers found. 大宮町 is just an address of NTT/Fujitsu **offices** in
  Nara City, not confirmed DC facilities. Power figures invented.
- All **"0.5–1.0 MW" allocations, edge-pod names, and per-site phone numbers** in the
  original — unverified/fabricated. The "<2.5 ms latency" and generic claims were
  filler.

## Sources
- https://www.pref.nara.lg.jp/n100/63527.html
- https://www.idcf.jp/datacenter/location/ikoma/
- https://www.coltdatacentres.net/en-GB/our-locations/data-centre-locations-asia/osaka-keihanna
- https://services.global.ntt/en-us/services-and-products/global-data-centers/global-locations/asia-pacific/keihanna-osk11-data-center
- https://www.kistem.com/
