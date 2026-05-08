# Mitsue Project — Stakeholders & Relations

## Entity List

### Core Team
| Name | Role |
|---|---|
| Rob Oudendijk | Founder & Project Lead (Dutch, resident Sugano since 2012) |
| Japanese Co-founder | TBD — top priority hire; rural-credible, Japanese-speaking |
| Mitsue Project (御杖プロジェクト) | Primary project entity (一般社団法人 → NPO法人) |
| YR-Design | Rob's company; project affiliation |
| Safecast | Citizen science network; philosophical foundation & open-data model |

### Advisors
| Name | Role |
|---|---|
| Joi Ito | Former MIT Media Lab Director; AI policy advisor to Japanese government; member of METI AI Strategy Council & Digital Agency advisory bodies; deep connections across Japanese tech, government, and philanthropy circles; confirmed May 5 2026 |
| Ray Ozzie | Creator of Lotus Notes; former Microsoft CSA; confirmed May 5 2026 |

### Local Stakeholders
| Name | Role |
|---|---|
| Mitsue Village Mayor | Primary government contact |
| Mitsue Village Vice Mayor | Initial informal contact (met late 2025) |
| 自治会 Leaders (Sugano + hamlets) | Community associations; trust-building target |
| Private Mountain Landowners | Sugi forest owners; harvesting partnership targets |
| Local Forestry Group | Early consultation partner (met early 2026) |
| Mitsue Elementary School | Closed building; central project asset |

### Government — Local & Regional
| Name | Role |
|---|---|
| Mitsue Village Government | Primary stakeholder; letter of interest target |
| Nara Prefecture | Regional oversight; potential grant source |

### Government — National (Grants, Permissions & Policy)

| Ministry / Agency | Grants / Funding | Permissions / Regulation | Notes |
|---|---|---|---|
| METI (経済産業省) | Green tech subsidies; data center incentives | FIT/FIP registration; 電気事業法 (power generation licensing) | Key funder for energy transition & AI infrastructure |
| NEDO | Renewable energy R&D grants; biomass technology grants | — | Arm of METI; major R&D grant source |
| 林野庁 (Forestry Agency) | Forestry subsidies; reforestation grants | 伐採届出 (cutting notification); Forest Act compliance | Critical for biomass feedstock legality |
| Cabinet Office (内閣府) | 地方創生 regional revitalization grants (¥5–50M) | — | Digital Garden City Nation Initiative policy driver |
| 総務省 (MIC — Ministry of Internal Affairs) | Rural broadband subsidies; data center regional grants | Telecom regulation; municipal digital policy | Funds rural fiber; connected to Digital Garden City strategy |
| デジタル庁 (Digital Agency) | Digital transformation grants for rural areas | Digital infrastructure standards | Joi Ito has advisory connections here; aligned with project's rural digital mission |
| 環境省 (Ministry of Environment) | Carbon credit support | J-Credit certification; environmental impact assessment (環境アセスメント) | Governs J-Credit scheme for forest carbon offsets |
| JST (Japan Science and Technology Agency) | R&D grants for green tech & AI | — | Potential Phase 2–3 R&D co-funding |
| 農業委員会 (Agricultural Commission) | — | Land use permits if agricultural land involved | Local body; Nara Prefecture jurisdiction |
| Legal Affairs Bureau (法務局) | — | Corporate registration (一般社団法人) | One-time registration |

### Diplomatic
| Name | Role |
|---|---|
| Sandra Pellegrom | Dutch Consul-General, Osaka; potential support letter; Dutch-JP bridge |
| Kingdom of the Netherlands | Rob's origin; diplomatic backing |

### Foundations
| Name | Tier | Role |
|---|---|---|
| Nippon Foundation (日本財団) | Primary | Social challenge grants; Asia's largest grantmaker |
| Japan Fund for Global Environment | Primary | Environmental conservation grants |
| Toyota Foundation | Secondary | Community & rural projects |
| MacArthur Foundation | Stretch | Through Joi Ito network |
| Rockefeller Foundation | Stretch | Through Joi Ito network |

### Japanese Corporates (potential partners)
| Name | Angle |
|---|---|
| NTT | Fiber connectivity; data center consultation (critical contact) |
| SoftBank | Data center partnership |
| Sumitomo Forestry (住友林業) | Forestry expertise & capital |
| Mitsui Bussan (三井物産) | Trading company; forestry supply chain |
| Hitachi | Industrial / infrastructure |

### Dutch Corporates (potential partners)
| Name | Angle |
|---|---|
| Philips | CSR; Dutch presence in Japan |
| ASML | CSR; Dutch presence in Japan |
| Royal HaskoningDHV | Water & infrastructure engineering |
| Arcadis | Sustainability & climate consulting |
| Heineken | CSR; Dutch presence in Japan |

### Legal & Professional Support (to hire)
| Role | Timing |
|---|---|
| 行政書士 (Administrative Scrivener) | Phase 0–1; permits, NPO setup, grants |
| 公認会計士 / 税理士 (Accountant / Tax) | Phase 1; accounting system, tax registration |
| 弁護士 (Lawyer) | Phase 1–2; landowner contracts |

---

## Relationship Flowchart

```mermaid
graph TD
    %% Core
    ROB["👤 Rob Oudendijk\nFounder & Lead"]
    COFOUND["👤 Japanese Co-founder\n(TBD — top priority)"]
    PROJ["🏗️ Mitsue Project\n御杖プロジェクト"]
    YR["🏢 YR-Design"]
    SAFECAST["🌐 Safecast\nOpen data model"]

    %% Advisors
    JOI["👤 Joi Ito\nAI Policy · MIT · Japan Govt"]
    RAY["👤 Ray Ozzie\nMicrosoft / Lotus"]

    %% Diplomatic
    CONSUL["👤 Sandra Pellegrom\nDutch Consul-General"]
    NL["🇳🇱 Kingdom of Netherlands"]

    %% Local
    MAYOR["👤 Village Mayor"]
    VMAYOR["👤 Vice Mayor"]
    JICHIKAI["👥 自治会 Leaders"]
    LANDOWNERS["👥 Private Landowners"]
    FORESTRY_LOCAL["👥 Local Forestry Group"]
    SCHOOL["🏫 Mitsue Elementary\n(closed school)"]

    %% Government
    subgraph GOV_LOCAL["Local & Regional Government"]
        VILLAGE_GOV["🏛️ Mitsue Village Govt"]
        NARA["🏛️ Nara Prefecture"]
    end

    subgraph GOV_NAT["National Government — Grants, Permissions & Policy"]
        METI["🏛️ METI 経済産業省\nFIT/FIP · green tech subsidies\n電気事業法 licensing"]
        NEDO["🏛️ NEDO\nRenewable energy R&D grants"]
        RINSHO["🏛️ 林野庁 Forestry Agency\nForestry permits · subsidies"]
        CABINET["🏛️ Cabinet Office 内閣府\n地方創生 grants\nDigital Garden City"]
        MIC["🏛️ 総務省 MIC\nRural broadband · data center grants\nTelecom regulation"]
        DIGITAL["🏛️ デジタル庁\nDigital Agency\nRural digital grants"]
        ENV["🏛️ 環境省\nJ-Credit certification\n環境アセスメント"]
        JST["🏛️ JST\nR&D grants (Phase 2–3)"]
        LEGAL_BUREAU["🏛️ Legal Affairs Bureau\nCorporate registration"]
    end

    %% Foundations
    subgraph FOUNDATIONS["Foundations"]
        NIPPON["🏦 Nippon Foundation"]
        JFGE["🏦 Japan Fund for\nGlobal Environment"]
        TOYOTA_F["🏦 Toyota Foundation"]
    end

    %% Corporates
    subgraph CORP_JP["Japanese Corporates"]
        NTT["🏢 NTT\nFiber · data center"]
        SOFTBANK["🏢 SoftBank"]
        SUMITOMO["🏢 Sumitomo Forestry"]
        MITSUI["🏢 Mitsui Bussan"]
    end

    subgraph CORP_NL["Dutch Corporates"]
        PHILIPS["🏢 Philips"]
        ASML["🏢 ASML"]
        RHDHV["🏢 Royal HaskoningDHV"]
        ARCADIS["🏢 Arcadis"]
    end

    %% Legal
    subgraph LEGAL_SUPPORT["Professional Support (to hire)"]
        GYOSEI["⚖️ 行政書士"]
        KAIKEI["⚖️ 公認会計士/税理士"]
        BENGOSHI["⚖️ 弁護士"]
    end

    %% ── Relations ──────────────────────────────────────────────────────────

    ROB -->|"co-founds"| PROJ
    COFOUND -->|"co-founds"| PROJ
    ROB -->|"affiliated with"| YR
    ROB -->|"core contributor"| SAFECAST
    SAFECAST -->|"inspires open-data model"| PROJ

    JOI -->|"advises"| PROJ
    RAY -->|"advises"| PROJ
    JOI -.->|"AI policy advisor"| METI
    JOI -.->|"advisory connections"| DIGITAL

    CONSUL -->|"potential support letter"| PROJ
    NL -->|"diplomatic backing"| CONSUL
    ROB -.->|"Dutch national\nseeks support from"| CONSUL

    ROB -->|"initial meeting (2025)"| VMAYOR
    VMAYOR -->|"gateway to"| MAYOR
    MAYOR -->|"formal approval"| VILLAGE_GOV
    VILLAGE_GOV -->|"letter of interest"| PROJ
    VILLAGE_GOV -->|"owns"| SCHOOL
    SCHOOL -->|"repurposed as\ndata center + hub"| PROJ
    JICHIKAI -->|"community buy-in"| PROJ
    LANDOWNERS -->|"sugi harvest\npartnership"| PROJ
    FORESTRY_LOCAL -->|"early consultation"| PROJ

    VILLAGE_GOV -->|"under"| NARA
    NARA -->|"regional grants"| PROJ
    LEGAL_BUREAU -->|"registers"| PROJ

    METI -->|"FIT/FIP · subsidies"| PROJ
    NEDO -->|"R&D grants"| PROJ
    RINSHO -->|"forestry permits\n+ subsidies"| PROJ
    CABINET -->|"地方創生 grants"| PROJ
    MIC -->|"rural broadband\n+ data center grants"| PROJ
    DIGITAL -->|"rural digital\ngrants"| PROJ
    ENV -->|"J-Credit · env.\npermits"| PROJ
    JST -->|"R&D grants"| PROJ

    NIPPON -->|"social grants"| PROJ
    JFGE -->|"env. grants"| PROJ
    TOYOTA_F -->|"community grants"| PROJ
    JOI -.->|"network access to"| NIPPON

    NTT -->|"fiber + data center\nconsultation"| PROJ
    SOFTBANK -->|"data center partner"| PROJ
    SUMITOMO -->|"forestry expertise"| PROJ
    MITSUI -->|"supply chain"| PROJ

    PHILIPS -->|"CSR partner"| PROJ
    ASML -->|"CSR partner"| PROJ
    RHDHV -->|"engineering"| PROJ
    ARCADIS -->|"sustainability"| PROJ
    CONSUL -.->|"introduces\nDutch corporates"| PROJ

    GYOSEI -->|"permits + NPO setup"| PROJ
    KAIKEI -->|"accounting"| PROJ
    BENGOSHI -->|"landowner contracts"| PROJ
```
