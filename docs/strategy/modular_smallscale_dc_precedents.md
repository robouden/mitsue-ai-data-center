<!-- Version: v1.0 | Last modified: 2026-07-22 -->

# Modular / Small-Scale AI Data Center Precedents — Verified Reference

Verified 2026-07-22. These are the **real peers for Mitsue's sub-1 MW village node** —
school-conversion + modular/container + high-density-cooling AI DCs — unlike the 30–50 MW
hyperscale sites in [nara_datacenter_landscape.md](nara_datacenter_landscape.md).

## 1. HIGHRESO (ハイレゾ / GPUSOROBAN) — the closest analog to Mitsue
Regional, closed-school conversion, renewable-powered, domestic engineering, + local
jobs and digital-literacy programs. This is essentially the model Mitsue is proposing.

| Site | Building | Specs | Power |
|---|---|---|---|
| **Ishikawa DC1 (Shiga-cho)** | operating since 2019 | GPUSOROBAN cloud origin | 20 kVA high-power racks |
| **Ishikawa DC2 (Shiga-cho)** | from Aug 2022 | **2,000 GPU servers** (NVIDIA RTX A4000) | 20 kVA/rack; **RE100 renewable** ("かがやきGREEN RE100") |
| **Genkai Town DC (Saga)** | ex-Aritoku Elem. (closed 2015), **~2,089 m²** | up to **120× NVIDIA RTX A4000** | opened 2025-08-22; costs "significantly reduced" by retrofit |
| **Ayagawa Town DC (Kagawa)** | ex-Ayagami JHS | planned 2025 | — |

- **Funding precedent:** received a **¥7.7 billion METI "Cloud Program" supply-assurance
  grant** for the DC project.
- **Rack density:** 20 kVA/rack (modest vs hyperscale — deliberately fits regional buildings).
- **Model to mirror:** dormant-asset reuse, renewable power, local hiring + AI/smartphone
  classes with the municipality. Directly relevant to the Koryukan/school framing
  ([[project_koryukan_workshop]], [[feedback_koryukan_dc_pitch_framing]]) and HIGHRESO is
  already an outreach target ([[project_highreso_outreach]]).

## 2. Quantum Mesh — modular "micro data center" via immersion cooling
- **KAMUI** — single-phase immersion cooling; **Japan's first commercial** deployment.
  **–32% power vs air-cooling**; cooling power cut to ≤1/10. **PUE 1.03–1.04** (with
  groundwater), patented.
- **KAMUI γ** — all-in-one immersion rack with integrated chiller, **<1 m² footprint,
  40 kVA/rack** high-density GPU. A self-contained "micro DC" — deployable in a single room.
- **Takahama, Fukui DC** under construction: AI/IoT compute for healthcare, tourism,
  disaster-prevention services.
- **IIJ + NetChart partnership (2026-04-07):** distributed **edge** DCs with KAMUI.
- **Relevance:** immersion + groundwater PUE 1.03 is a strong fit for a small village
  site; the KAMUI γ single-rack unit is a way to start at one classroom's scale. Mitsue
  has spring/onsen groundwater — worth exploring. IIJ tie-in echoes [[reference_biomass_ai_dc_precedents]].

## 3. Container / rapid-deploy modular benchmarks (sub-MW → ~1 MW)
| Operator / product | Config | Power | Cooling | Deploy time |
|---|---|---|---|---|
| **Sakura Internet — Ishikari** | 2 containers, 40 racks (20/container), **~1,000× NVIDIA H200** | **~3.5 MVA** | direct liquid cooling (5 GPU srv/rack) | planning→done ~1.5 yr |
| **Kagoshima 10-container DC** | 10 containers | **~1 MW** | — | contract→ops **4 months** |
| **GETWORKS — Yuzawa GX DC** | container | — | **Japan-first liquid cooling tower** (Dec 2024) | — |
| **PowerX — Mega Power DC** | 10-ft container + battery | — | + up to **800 kWh** storage | ~1 yr |

- **GPU power reality:** legacy racks were designed for **3–4 kW/rack**; a GPU-loaded rack
  needs **~50 kW** — the reason liquid/immersion cooling is mandatory at density.

## Takeaways for Mitsue's design
1. **Start small is proven:** 120 GPUs in one ex-school (HIGHRESO Genkai) or a single
   40 kVA KAMUI γ rack are real, sub-100 kW entry points — matches a one-classroom start.
2. **Cooling choice drives density:** air 20 kVA/rack (HIGHRESO) vs immersion 40 kVA/rack
   PUE 1.03 (Quantum Mesh). Immersion + our groundwater is the efficiency play.
3. **Container path = speed:** 4–18 months vs 3+ years for build — lets compute load
   scale to match biomass CHP output as the forest program ramps.
4. **Funding is real at this scale:** METI Cloud Program gave HIGHRESO ¥7.7B; pair with
   [[reference_nara_dc_subsidy]] and [[reference_fy2026_subsidy_tracks]].

## Sources
- HIGHRESO Genkai: https://prtimes.jp/main/html/rd/p/000000083.000058027.html · https://www.itmedia.co.jp/news/articles/2508/22/news095.html
- HIGHRESO Ishikawa DC2 / RE100: https://highreso.jp/press/722/ · https://prtimes.jp/main/html/rd/p/000000047.000058027.html
- Quantum Mesh KAMUI / KAMUI γ: https://quantummesh.jp/en · https://prtimes.jp/main/html/rd/p/000000023.000132065.html · https://quantummesh.jp/press/ZtlLtnKE
- Quantum Mesh × IIJ edge DC: https://www.iij.ad.jp/news/pressrelease/2026/0407.html
- Sakura Ishikari container: https://www.sakura.ad.jp/corporate/information/newsreleases/2025/06/11/1968219778/
- Container market/context: https://www.nikkei.com/article/DGXZQOUC0392N0T01C24A2000000/ · https://www.weeklybcn.com/journal/feature/detail/20250327_209063.html
