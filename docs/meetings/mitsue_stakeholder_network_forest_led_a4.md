<!-- Version: v1.0 | Last modified: 2026-09-21 -->

<style>
  html { font-size: 11px !important; }
  body { line-height: 1.28 !important; }
  p, blockquote, ul, ol, dl, table { margin: 3px 0 !important; }
  h1, h2, h3, h4, h5, h6 { margin-top: 4px !important; margin-bottom: 2px !important; }
  hr { margin: 4px 0 !important; }
  table td, table th { padding: 2px 6px !important; }
  .mermaid .edgeLabel text, .mermaid .edgeLabel tspan { fill: #1A1A1A !important; }
  .mermaid .edgeLabel, .mermaid .edgeLabel div, .mermaid .edgeLabel span, .mermaid .edgeLabel p { color: #1A1A1A !important; }
  .mermaid .node foreignObject, .mermaid .node foreignObject div, .mermaid .node foreignObject span { overflow: visible !important; max-width: none !important; white-space: nowrap !important; }
  .legend-row { font-size: 8.5pt; }
  .legend-sw { display:inline-block; width:10px; height:8px; margin-right:4px; vertical-align:middle; border-radius:2px; }
  .legend-sw.dash { background: repeating-linear-gradient(90deg,#718096 0 3px,transparent 3px 5px); height:2px; margin-top:4px; }
  .mermaid svg { max-width: 100% !important; width: 100% !important; height: auto !important; }
  .mermaid .cluster rect { fill: #ffffff !important; stroke: #cbd5e0 !important; }
  .mermaid .cluster text, .mermaid .cluster-label { fill: #4a5568 !important; font-weight: 700 !important; }
</style>

<div style="font-family:-apple-system,Helvetica,Arial,sans-serif;">
<p style="font-size:7.5pt; font-weight:600; letter-spacing:0.25em; color:#3a7a5a; margin:0 0 2mm;">PROJECT DOCUMENT · DISCUSSION DRAFT</p>
<h1 style="font-size:20pt; font-weight:700; margin:0 0 1mm;">Stakeholder Network — Forest-Led Model</h1>
<p style="font-size:10pt; color:#666; margin:0 0 1mm;">Mitsue AI Data Center &amp; Biomass Energy Project</p>
<p style="font-size:9pt; color:#888; margin:0 0 4mm;">v1.0 · 2026-09-21 · Rob Oudendijk</p>
</div>

> **Very early draft — concept only.** Nothing here is decided or agreed. Starting point for discussion, not a proposal to sign. Alternative to the NGO-led model in `mitsue_kanko_collaboration_diagrams`: here the Mitsue Village Forest Association (8-crew forestry cooperative) is the operational hub for logging, replanting and processing, with the NGO delegating day-to-day coordination rather than running it directly.

## Network diagram

```mermaid
%%{init: {'flowchart': {'nodeSpacing': 12, 'rankSpacing': 34, 'padding': 6}, 'themeVariables': {'fontSize':'17px'}}}%%
graph TB
    subgraph Government["GOVERNMENT"]
        VILLAGE["Village Hall"]
        NARA["Nara Prefecture<br/>land permits, subsidy TBD"]
        NATIONAL["METI / MoE / forestry agency<br/>NEDO / JST"]
    end
    subgraph NGO_NPO["NGO / NPO"]
        NGO["Project NGO<br/>legal/financing wrapper"]
        MORETREES["more trees"]
        FOUND["Foundations"]
    end
    subgraph Cooperative["FOREST TEAM"]
        COOP["Mitsue Village Forest Association<br/>8 crew - hub"]
    end
    subgraph Companies["COMPANIES"]
        GK["Operating Co<br/>GK/KK<br/>CHP + AI DC"]
        MIZUHO["Mizuho Securities"]
        SUGANO["Sugano Organic"]
        CORP["Corporate partners<br/>unconfirmed"]
        LEGAL["Legal (pro bono)<br/>Linklaters, TMI, Hotta"]
    end
    subgraph Academia["ACADEMIA"]
        NAIST["NAIST"]
    end

    VILLAGE -->|liaison| MORETREES
    MORETREES -->|liaison, species/method| NGO
    NGO -->|coordinates, delegates ops| COOP
    NAIST -->|logging/processing research - direct| COOP
    COOP -->|fuel-wood supply| GK
    NATIONAL -->|subsidies, via village| GK
    NATIONAL -.->|equipment grants - direct| COOP
    NARA -.->|land-use permits| GK
    NGO -->|majority owns| GK
    FOUND -->|grants| NGO
    MIZUHO -.->|financing - undecided| GK
    CORP -.->|CSR - unconfirmed| NGO
    SUGANO -.->|pilot site - exploratory| GK
    LEGAL -.->|pro bono legal advice| NGO

    classDef gov fill:#2b6cb0,color:#fff,stroke:#1a4971,stroke-width:1px
    classDef ngo fill:#276749,color:#fff,stroke:#1c4532,stroke-width:1px
    classDef co fill:#975a16,color:#fff,stroke:#7b341e,stroke-width:1px
    classDef coop fill:#6b46c1,color:#fff,stroke:#44337a,stroke-width:3px
    classDef acad fill:#b83280,color:#fff,stroke:#702459,stroke-width:1px
    class VILLAGE,NARA,NATIONAL gov
    class NGO,MORETREES,FOUND ngo
    class GK,MIZUHO,CORP,SUGANO,LEGAL co
    class COOP coop
    class NAIST acad
```

## Legend

<table style="width:100%; border:none; border-collapse:collapse; margin:2mm 0;"><tr>
<td style="border:none; padding:1mm 4mm 1mm 0; font-size:8.5pt;"><span class="legend-sw" style="background:#2b6cb0"></span>Government</td>
<td style="border:none; padding:1mm 4mm 1mm 0; font-size:8.5pt;"><span class="legend-sw" style="background:#276749"></span>NGO / NPO</td>
<td style="border:none; padding:1mm 4mm 1mm 0; font-size:8.5pt;"><span class="legend-sw" style="background:#975a16"></span>Company</td>
</tr><tr>
<td style="border:none; padding:1mm 4mm 1mm 0; font-size:8.5pt;"><span class="legend-sw" style="background:#6b46c1"></span>Forest Team (co-op)</td>
<td style="border:none; padding:1mm 4mm 1mm 0; font-size:8.5pt;"><span class="legend-sw" style="background:#b83280"></span>Academia</td>
<td style="border:none; padding:1mm 4mm 1mm 0; font-size:8.5pt;">— solid arrow: planned/structural link &nbsp;·&nbsp; <span class="legend-sw dash" style="width:20px;"></span> dashed: tentative / unconfirmed</td>
</tr></table>

**Reading the diagram:** liaison runs Village Hall → more trees → NGO; the NGO delegates day-to-day coordination to the Mitsue Village Forest Association (8-crew hub), which in turn supplies fuel-wood to the Operating Company. NAIST's research link goes direct to the Forest Team, not through the NGO. Dashed edges (equipment grants, land-use permits, Mizuho financing, corporate CSR, Sugano pilot site, pro bono legal) are not yet confirmed in writing.

## Node detail

| Node | Group | Role / status |
|---|---|---|
| Village Hall | Government | Formal liaison entry point; grants land/permits to Operating Co |
| Nara Prefecture | Government | Land-use permits, subsidy — TBD (tentative) |
| METI / MoE / forestry agency / NEDO / JST | Government | National subsidy sources; forest/RE-type via village, DC/power-type via Operating Co |
| Project NGO (一般社団法人) | NGO/NPO | Non-distributing legal/financing wrapper; majority owner of Operating Co |
| more trees | NGO/NPO | Liaison + replanting species/method partner between Village Hall and NGO |
| Foundations | NGO/NPO | Grant source into NGO — target ¥33M, ¥0 secured to date (see funding flowchart) |
| Mitsue Village Forest Association | Forest Team | 8-crew forestry cooperative; operational hub for logging, replanting, processing under this model |
| Operating Co (GK/KK) | Company | CHP + AI Data Center operating entity, majority-owned by the NGO |
| Mizuho Securities | Company | Financing option — undecided (tentative) |
| Sugano Organic | Company | Exploratory pilot CHP site (tentative) |
| Corporate partners | Company | Unconfirmed CSR/sponsorship (tentative) |
| Legal (pro bono) | Company | Linklaters (Watanabe), TMI (Nakano), likely Nishimura & Asahi (Hotta) — all confirmed pro bono, no written engagement letter |
| NAIST | Academia | Direct research link to the Forest Team (logging/processing); contact via Kubo (CDG), introduced by President Shiozaki — relationship still developing, not yet a formal MOU |

---

*This is the forest-team-led alternative to the NGO-led coordination model in `mitsue_kanko_collaboration_diagrams`. Source: repo docs (`mitsue_kanko_forest_led_diagrams_a3.html` panel 4), cross-checked against project notes as of 2026-09-21.*

<table style="width:100%; border:none; border-collapse:collapse; margin-top:2mm;"><tr>
<td style="border:none; vertical-align:middle;">
<em>Mitsue AI Data Center · Mitsue Village, Nara</em><br/>
<em>Contact: Rob Oudendijk · oudendijk.biz@gmail.com · 080-2260-5966</em>
</td>
<td style="border:none; vertical-align:middle; text-align:right; width:100px;">
<a href="https://mitsue.it"><strong>mitsue.it</strong></a><br/>
<img src="https://api.qrserver.com/v1/create-qr-code/?size=90x90&data=https://mitsue.it" alt="mitsue.it QR code" width="90" height="90"/>
</td>
</tr></table>
