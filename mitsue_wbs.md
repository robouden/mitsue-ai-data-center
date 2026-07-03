<div style="font-family:-apple-system,Helvetica,Arial,sans-serif;">
<p style="font-size:7.5pt; font-weight:600; letter-spacing:0.25em; color:#3a7a5a; margin:0 0 4mm;">PROJECT DOCUMENT</p>
<h1 style="font-size:28pt; font-weight:700; margin:0 0 2mm; border-bottom:1px solid #eee; padding-bottom:2mm;">Mitsue Project</h1>
<p style="font-style:italic; color:#666; margin:2mm 0 8mm;">Work Breakdown Structure</p>
<img src="assets/logo_go.png" alt="御" width="50%" style="display:block;margin:0 auto;">
<div style="height:105mm;"></div>
<table style="width:100%; border-collapse:collapse; font-size:9pt;">
<tr><td style="padding:3mm 4mm; border:1px solid #ccc; font-weight:bold; width:30%;">Version</td><td style="padding:3mm 4mm; border:1px solid #ccc;">v2.7</td></tr>
<tr><td style="padding:3mm 4mm; border:1px solid #ccc; font-weight:bold;">Date</td><td style="padding:3mm 4mm; border:1px solid #ccc;">2026-07-04</td></tr>
<tr><td style="padding:3mm 4mm; border:1px solid #ccc; font-weight:bold;">Author</td><td style="padding:3mm 4mm; border:1px solid #ccc;">Rob Oudendijk</td></tr>
</table>
</div>

<div style="page-break-after:always; break-after:page; height:0; margin:0; padding:0;"></div>

---

# Mitsue Project — Work Breakdown Structure
### Phases 0–3 · April 2026 – September 2028

---

## 1. How to Read This Document

The WBS decomposes the entire project scope into discrete, manageable elements. Each element at the **lowest level** (the work package) represents a bounded unit of work with a defined deliverable, budget, and responsible party.

**Conventions used:**
- WBS codes use dot notation: `1.0` = Level 1, `1.2` = Level 2, `1.2.3` = Level 3
- **Budget** columns show the planning estimate; ranges indicate remaining uncertainty
- **Owner** is the person accountable for delivery (not necessarily the doer)
- **Deliverable** is what must exist / be accepted for the element to be marked complete
- Total BAC = **¥220.0M** | Management Reserve (not in WBS) = ¥25.0M
- **Baseline Rev 1 (May 2026)** — Reality-checked against real-world Japan benchmarks for solar PV (¥200–300K/kW), school seismic retrofit (¥200–500K/㎡), commercial EV fast-chargers (¥5–6M each), and forestry road works. BAC raised from ¥168M to ¥220M.

---

## 2. WBS Summary Tree

```
0.0  MITSUE PROJECT (Phases 0–3)                          ¥220.0M
 │
 ├── 1.0  Project Management & Governance                  ¥15.0M
 │    ├── 1.1  Programme direction & reporting
 │    ├── 1.2  Legal, accounting & compliance
 │    └── 1.3  Communications, translation & website
 │
 ├── 2.0  Phase 0 — Pre-Foundation                          ¥0.25M
 │    ├── 2.1  Community stakeholder engagement
 │    ├── 2.2  Founding charter & documents
 │    └── 2.3  Founding team identification
 │
 ├── 3.0  Phase 1 — Foundation                              ¥5.5M
 │    ├── 3.1  Legal entity setup (一般社団法人)
 │    ├── 3.2  Forestry feasibility study
 │    ├── 3.3  Energy systems feasibility study
 │    ├── 3.4  Building & site assessment
 │    ├── 3.5  Connectivity assessment
 │    ├── 3.6  Operations setup
 │    └── 3.7  Village RE plan alignment & 交付金 事業計画 co-development (官民連携)
 │
 ├── 4.0  Phase 2 — Pilot Design                           ¥22.25M
 │    ├── 4.1  Building & structural design
 │    ├── 4.2  Energy systems engineering
 │    ├── 4.3  Data center & IT architecture
 │    ├── 4.4  EV charging system design
 │    ├── 4.5  Permitting & regulatory
 │    ├── 4.6  Partnership & landowner agreements
 │    ├── 4.7  Grant writing & funding applications
 │    ├── 4.8  Staff recruitment & onboarding
 │    ├── 4.9  Vendor pre-qualification
 │    └── 4.10 Phase 2 contingency
 │
 └── 5.0  Phase 3 — Pilot Build                           ¥177.0M
      ├── 5.1  School building renovation
      ├── 5.2  Solar PV installation
      ├── 5.3  Battery storage system
      ├── 5.4  EV charging infrastructure
      ├── 5.5  Data center fitout
      ├── 5.6  Forestry operations
      ├── 5.7  Fiber connectivity upgrade
      ├── 5.8  Testing, commissioning & startup
      └── 5.9  Phase 3 contingency
```

---

<div style="page-break-inside:avoid; margin: 10pt 0">

**Figure 1 — Project Phase Timeline (Gantt View, Apr 2026 – Sep 2028)**

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 425" style="width:100%;display:block">
  <!-- Month header background -->
  <rect x="140" y="5" width="530" height="22" fill="#f0f4ff" stroke="#ccc" stroke-width="0.5"/>
  <!-- Month tick labels every 3rd month -->
  <!-- M1=Apr'26 x=140, M4=Jul'26, M7=Oct'26, M10=Jan'27, M13=Apr'27, M16=Jul'27, M19=Oct'27, M22=Jan'28, M25=Apr'28, M28=Jul'28, M30=Sep'28=670 -->
  <!-- step = 530/29 = 18.28 per month; M_n x = 140+(n-1)*18.28 -->
  <!-- M1=140, M4=194.8, M7=249.6, M10=304.5, M13=359.3, M16=414.1, M19=468.9, M22=523.7, M25=578.5, M28=633.3, M30=670 -->
  <text x="140" y="20" text-anchor="middle" font-size="7" fill="#444" font-family="Segoe UI,sans-serif">Apr'26</text>
  <text x="195" y="20" text-anchor="middle" font-size="7" fill="#444" font-family="Segoe UI,sans-serif">Jul'26</text>
  <text x="250" y="20" text-anchor="middle" font-size="7" fill="#444" font-family="Segoe UI,sans-serif">Oct'26</text>
  <text x="305" y="20" text-anchor="middle" font-size="7" fill="#444" font-family="Segoe UI,sans-serif">Jan'27</text>
  <text x="359" y="20" text-anchor="middle" font-size="7" fill="#444" font-family="Segoe UI,sans-serif">Apr'27</text>
  <text x="414" y="20" text-anchor="middle" font-size="7" fill="#444" font-family="Segoe UI,sans-serif">Jul'27</text>
  <text x="469" y="20" text-anchor="middle" font-size="7" fill="#444" font-family="Segoe UI,sans-serif">Oct'27</text>
  <text x="524" y="20" text-anchor="middle" font-size="7" fill="#444" font-family="Segoe UI,sans-serif">Jan'28</text>
  <text x="578" y="20" text-anchor="middle" font-size="7" fill="#444" font-family="Segoe UI,sans-serif">Apr'28</text>
  <text x="633" y="20" text-anchor="middle" font-size="7" fill="#444" font-family="Segoe UI,sans-serif">Jul'28</text>
  <text x="670" y="20" text-anchor="middle" font-size="7" fill="#444" font-family="Segoe UI,sans-serif">Sep'28</text>
  <!-- Vertical gridlines at tick positions -->
  <line x1="140" y1="26" x2="140" y2="335" stroke="#ddd" stroke-width="0.5"/>
  <line x1="195" y1="26" x2="195" y2="335" stroke="#ddd" stroke-width="0.5"/>
  <line x1="250" y1="26" x2="250" y2="335" stroke="#ddd" stroke-width="0.5"/>
  <line x1="305" y1="26" x2="305" y2="335" stroke="#ddd" stroke-width="0.5"/>
  <line x1="359" y1="26" x2="359" y2="335" stroke="#ddd" stroke-width="0.5"/>
  <line x1="414" y1="26" x2="414" y2="335" stroke="#ddd" stroke-width="0.5"/>
  <line x1="469" y1="26" x2="469" y2="335" stroke="#ddd" stroke-width="0.5"/>
  <line x1="524" y1="26" x2="524" y2="335" stroke="#ddd" stroke-width="0.5"/>
  <line x1="578" y1="26" x2="578" y2="335" stroke="#ddd" stroke-width="0.5"/>
  <line x1="633" y1="26" x2="633" y2="335" stroke="#ddd" stroke-width="0.5"/>
  <line x1="670" y1="26" x2="670" y2="335" stroke="#ddd" stroke-width="0.5"/>
  <!-- Row backgrounds (alternating) -->
  <rect x="0" y="27" width="700" height="22" fill="#f8f9ff"/>
  <rect x="0" y="71" width="700" height="22" fill="#f8f9ff"/>
  <rect x="0" y="115" width="700" height="22" fill="#f8f9ff"/>
  <rect x="0" y="162" width="700" height="18" fill="#fffdf8"/>
  <rect x="0" y="183" width="700" height="18" fill="#fffdf8"/>
  <rect x="0" y="204" width="700" height="18" fill="#fffdf8"/>
  <rect x="0" y="225" width="700" height="18" fill="#fffdf8"/>
  <rect x="0" y="246" width="700" height="18" fill="#fffdf8"/>
  <rect x="0" y="267" width="700" height="18" fill="#fffdf8"/>
  <rect x="0" y="288" width="700" height="18" fill="#fffdf8"/>
  <!-- Row labels -->
  <text x="135" y="41" text-anchor="end" font-size="8.5" fill="#333" font-weight="bold" font-family="Segoe UI,sans-serif">Phase 0</text>
  <text x="135" y="53" text-anchor="end" font-size="7" fill="#888" font-family="Segoe UI,sans-serif">Pre-Foundation</text>
  <text x="135" y="85" text-anchor="end" font-size="8.5" fill="#333" font-weight="bold" font-family="Segoe UI,sans-serif">Phase 1</text>
  <text x="135" y="97" text-anchor="end" font-size="7" fill="#888" font-family="Segoe UI,sans-serif">Foundation ¥5.5M</text>
  <text x="135" y="129" text-anchor="end" font-size="8.5" fill="#333" font-weight="bold" font-family="Segoe UI,sans-serif">Phase 2</text>
  <text x="135" y="141" text-anchor="end" font-size="7" fill="#888" font-family="Segoe UI,sans-serif">Pilot Design ¥22.25M</text>
  <text x="135" y="173" text-anchor="end" font-size="8" fill="#333" font-family="Segoe UI,sans-serif">5.7 Fiber Upgrade</text>
  <text x="135" y="194" text-anchor="end" font-size="8" fill="#333" font-family="Segoe UI,sans-serif">5.1 Building Reno</text>
  <text x="135" y="215" text-anchor="end" font-size="8" fill="#333" font-family="Segoe UI,sans-serif">5.6 Forestry Ops</text>
  <text x="135" y="236" text-anchor="end" font-size="8" fill="#333" font-family="Segoe UI,sans-serif">5.2+5.3 Solar/Battery</text>
  <text x="135" y="257" text-anchor="end" font-size="8" fill="#333" font-family="Segoe UI,sans-serif">5.4 EV Charging</text>
  <text x="135" y="278" text-anchor="end" font-size="8" fill="#333" font-family="Segoe UI,sans-serif">5.5 Data Center</text>
  <text x="135" y="299" text-anchor="end" font-size="8" fill="#333" font-family="Segoe UI,sans-serif">5.8 Testing &amp; Comm.</text>
  <!-- Phase 0 bar: M1-M3, x=140 w=3*18.28=54.8 -->
  <rect x="140" y="30" width="55" height="18" rx="3" fill="#6796e6"/>
  <text x="168" y="43" text-anchor="middle" font-size="7" fill="white" font-family="Segoe UI,sans-serif">M1–M3  ¥0.25M</text>
  <!-- Gate 1 diamond: x=195 -->
  <polygon points="195,27 200,38 195,49 190,38" fill="#e58520"/>
  <!-- Phase 1 bar: M4-M9, x=195 w=6*18.28=109.7 -->
  <rect x="195" y="74" width="110" height="18" rx="3" fill="#4a7ac4"/>
  <text x="250" y="87" text-anchor="middle" font-size="7" fill="white" font-family="Segoe UI,sans-serif">M4–M9  ¥5.5M</text>
  <!-- Gate 2 diamond: x=305 -->
  <polygon points="305,71 310,82 305,93 300,82" fill="#e58520"/>
  <!-- Phase 2 bar: M10-M18, x=305 w=9*18.28=164.5 -->
  <rect x="305" y="118" width="164" height="18" rx="3" fill="#e58520"/>
  <text x="387" y="131" text-anchor="middle" font-size="7" fill="white" font-family="Segoe UI,sans-serif">M10–M18  ¥22.25M</text>
  <!-- Gate 3 diamond: x=469 -->
  <polygon points="469,115 474,126 469,137 464,126" fill="#e58520"/>
  <!-- 5.7 Fiber (M15-M22): starts at M15 x=140+(14)*18.28=396, ends M22 x=523.7 -->
  <rect x="396" y="163" width="128" height="13" rx="2" fill="#9fb8e8"/>
  <text x="460" y="173" text-anchor="middle" font-size="6.5" fill="#222" font-family="Segoe UI,sans-serif">Start early — NTT lead time 6–9 mo</text>
  <!-- 5.1 Building Reno (M19-M24): x=469 w=5*18.28=91.4 -->
  <rect x="469" y="184" width="91" height="13" rx="2" fill="#d94f4f"/>
  <text x="515" y="194" text-anchor="middle" font-size="7" fill="white" font-family="Segoe UI,sans-serif">Building Reno  ¥38M</text>
  <!-- 5.6 Forestry (M19-M27): x=469 w=8*18.28=146.2 -->
  <rect x="469" y="205" width="146" height="13" rx="2" fill="#6aaa50"/>
  <text x="542" y="215" text-anchor="middle" font-size="7" fill="white" font-family="Segoe UI,sans-serif">Forestry Ops  ¥25M</text>
  <!-- 5.2+5.3 Solar+Battery (M20-M26): x=487.3 w=6*18.28=109.7 -->
  <rect x="487" y="226" width="110" height="13" rx="2" fill="#d94f4f" fill-opacity="0.8"/>
  <text x="542" y="236" text-anchor="middle" font-size="7" fill="white" font-family="Segoe UI,sans-serif">Solar+Battery  ¥34M</text>
  <!-- 5.4 EV Charging (M22-M27): x=524 w=5*18.28=91.4 -->
  <rect x="524" y="247" width="91" height="13" rx="2" fill="#d94f4f" fill-opacity="0.7"/>
  <text x="570" y="257" text-anchor="middle" font-size="7" fill="white" font-family="Segoe UI,sans-serif">EV Charging  ¥15M</text>
  <!-- 5.5 Data Center (M23-M29): x=542.3 w=6*18.28=109.7 -->
  <rect x="542" y="268" width="110" height="13" rx="2" fill="#d94f4f" fill-opacity="0.6"/>
  <text x="597" y="278" text-anchor="middle" font-size="7" fill="white" font-family="Segoe UI,sans-serif">Data Center  ¥20M</text>
  <!-- 5.8 Testing (M29-M30): x=633.3 w=1.5*18.28=27.4 -->
  <rect x="633" y="289" width="37" height="13" rx="2" fill="#333"/>
  <text x="651" y="299" text-anchor="middle" font-size="7" fill="white" font-family="Segoe UI,sans-serif">Test ¥8M</text>
  <!-- Gate 4 diamond: x=670 -->
  <polygon points="670,285 676,299 670,313 664,299" fill="#4aaa60"/>
  <!-- Status date line -->
  <line x1="158" y1="26" x2="158" y2="335" stroke="#e58520" stroke-width="1.5" stroke-dasharray="4,3"/>
  <text x="160" y="343" font-size="6.5" fill="#e58520" font-weight="bold" font-family="Segoe UI,sans-serif">▲ Today</text>
  <!-- Legend -->
  <rect x="140" y="318" width="10" height="8" fill="#e58520" rx="1"/>
  <text x="154" y="326" font-size="7" fill="#444" font-family="Segoe UI,sans-serif">Funding Gate</text>
  <rect x="240" y="318" width="10" height="8" fill="#d94f4f" rx="1"/>
  <text x="254" y="326" font-size="7" fill="#444" font-family="Segoe UI,sans-serif">Phase 3 Construction</text>
  <rect x="380" y="318" width="10" height="8" fill="#6aaa50" rx="1"/>
  <text x="394" y="326" font-size="7" fill="#444" font-family="Segoe UI,sans-serif">Forestry (seasonal)</text>
  <rect x="490" y="318" width="10" height="8" fill="#9fb8e8" rx="1"/>
  <text x="504" y="326" font-size="7" fill="#444" font-family="Segoe UI,sans-serif">Fiber (spans P2→P3)</text>
  <polygon points="600,318 604,326 600,334 596,326" fill="#4aaa60"/>
  <text x="610" y="326" font-size="7" fill="#444" font-family="Segoe UI,sans-serif">Revenue Gate 4</text>
  <!-- Gate Decision Framework -->
  <line x1="5" y1="340" x2="695" y2="340" stroke="#bbb" stroke-width="0.7"/>
  <text x="350" y="351" text-anchor="middle" font-size="8" font-weight="bold" fill="#333" font-family="Segoe UI,sans-serif">Gate Decision Framework</text>
  <text x="5"   y="363" font-size="6.5" font-weight="bold" fill="#555" font-family="Segoe UI,sans-serif">Gate</text>
  <text x="190" y="363" font-size="6.5" font-weight="bold" fill="#4aaa60" font-family="Segoe UI,sans-serif">✓ PASS → Proceed</text>
  <text x="445" y="363" font-size="6.5" font-weight="bold" fill="#c06010" font-family="Segoe UI,sans-serif">↩ FAIL → Hold action</text>
  <line x1="5" y1="366" x2="695" y2="366" stroke="#ddd" stroke-width="0.5"/>
  <text x="5"   y="377" font-size="6.5" fill="#e58520" font-weight="bold" font-family="Segoe UI,sans-serif">Gate 1 · M3 · ¥3–8M</text>
  <text x="190" y="377" font-size="6.5" fill="#333" font-family="Segoe UI,sans-serif">Phase 1 begins; feasibility studies &amp; team contracts start</text>
  <text x="445" y="377" font-size="6.5" fill="#555" font-family="Segoe UI,sans-serif">Hold &amp; re-pitch founders; revisit at M+3</text>
  <text x="5"   y="390" font-size="6.5" fill="#e58520" font-weight="bold" font-family="Segoe UI,sans-serif">Gate 2 · M9 · ¥30–50M</text>
  <text x="190" y="390" font-size="6.5" fill="#333" font-family="Segoe UI,sans-serif">Phase 2 begins; engineering, permits &amp; Fiber order placed</text>
  <text x="445" y="390" font-size="6.5" fill="#555" font-family="Segoe UI,sans-serif">Descope; re-apply grants; extend Phase 1 by 3–6 months</text>
  <text x="5"   y="403" font-size="6.5" fill="#e58520" font-weight="bold" font-family="Segoe UI,sans-serif">Gate 3 · M18 · ¥80–200M</text>
  <text x="190" y="403" font-size="6.5" fill="#333" font-family="Segoe UI,sans-serif">Phase 3 begins; full construction programme mobilised</text>
  <text x="445" y="403" font-size="6.5" fill="#555" font-family="Segoe UI,sans-serif">Stage build; seek bridge finance; Phase 2 extension ±6 mo</text>
  <text x="5"   y="416" font-size="6.5" fill="#4aaa60" font-weight="bold" font-family="Segoe UI,sans-serif">Gate 4 · M30 · Revenue online?</text>
  <text x="190" y="416" font-size="6.5" fill="#333" font-family="Segoe UI,sans-serif">Phase 4 operations; commercial contracts &amp; EV charging open</text>
  <text x="445" y="416" font-size="6.5" fill="#555" font-family="Segoe UI,sans-serif">Pilot mode; re-pitch corporates; EAC review</text>
</svg>

</div>

---

## 3. WBS Dictionary — Full Detail

---

### 1.0 Project Management & Governance — ¥15.0M

Cross-phase overhead covering leadership, legal compliance, and external communications. These costs are time-phased across all 30 months and do not correspond to a single phase.

#### 1.1 Programme Direction & Reporting — ¥8.0M

| Item | Detail |
|------|--------|
| Scope | Representative Director oversight; monthly EVM reporting; board meetings; stakeholder briefings; risk register maintenance |
| Owner | Representative Director (代表理事) |
| Budget | ¥8.0M (¥265K/month average across 30 months) |
| Deliverables | Monthly EVM status reports; gate review packages; annual stakeholder reports |
| Acceptance | Board approval of each gate review package |

**Work packages:**
- Monthly EVM status reports (M1–M30)
- Quarterly stakeholder briefings (8 reports)
- Four gate review packages (Gate 1–4)
- Annual year-end reviews (2026, 2027, 2028)
- Risk register (maintained monthly)
- OpenProject administration

#### 1.2 Legal, Accounting & Compliance — ¥4.0M

| Item | Detail |
|------|--------|
| Scope | 行政書士 retainer for grants & permits; 税理士 for annual tax filing; legal counsel for contracts; ongoing compliance |
| Owner | Director — Finance/Operations |
| Budget | ¥4.0M |
| Deliverables | Audited annual accounts; tax filings; legal review sign-offs on all major contracts |
| Acceptance | Annual accounts accepted by auditor (監事) |

**Work packages:**
- 行政書士 retainer (Phase 1–3)
- 税理士 / 公認会計士 annual engagement
- Annual financial report & audit
- Contract legal review (landowner, vendor, partnership agreements)

#### 1.3 Communications, Translation & Website — ¥3.0M

| Item | Detail |
|------|--------|
| Scope | Bilingual project website; press & stakeholder materials; translation of all formal documents; annual report design |
| Owner | Director — Technology |
| Budget | ¥3.0M |
| Deliverables | Live bilingual website (by end of Phase 1); translated versions of all key documents; annual impact report |
| Acceptance | Website live and reviewed by board before Phase 1 close |

---

<div class="page-break"></div>

### 2.0 Phase 0 — Pre-Foundation — ¥0.25M

*Duration: Month 1–3 (April–June 2026)*

Low-budget, high-importance phase. The primary currency is time and trust, not money. Goal is to establish social license before any public commitments are made.

#### 2.1 Community Stakeholder Engagement — ¥0.10M

| Item | Detail |
|------|--------|
| Scope | Private meetings with village mayor, council members, 自治会 leaders in Sugano and nearby hamlets; listening sessions (not pitching) |
| Owner | Rob Oudendijk + Japanese co-founder (when identified) |
| Budget | ¥0.10M (travel, hospitality, materials) |
| Deliverables | Meeting log with attendees and key reactions; summary memo of village leadership posture (supportive / neutral / cautious) |
| Acceptance | Village mayor informed; no active opposition identified |

#### 2.2 Founding Charter & Documents — ¥0.10M

| Item | Detail |
|------|--------|
| Scope | Draft 2-page bilingual charter; preliminary project description in Japanese; translation of core concept documents |
| Owner | Rob Oudendijk |
| Budget | ¥0.10M (translation fees, 行政書士 preliminary consultation) |
| Deliverables | Draft charter (日本語・英語); translated project concept note |
| Acceptance | Charter reviewed and agreed by founding team members |

#### 2.3 Founding Team Identification — ¥0.05M

| Item | Detail |
|------|--------|
| Scope | Identify and secure verbal commitments from 3–5 founding team members; at minimum one well-respected Japanese co-founder with rural credibility |
| Owner | Rob Oudendijk |
| Budget | ¥0.05M (networking, travel) |
| Deliverables | Named list of founding team with verbal commitments documented |
| Acceptance | Japanese Representative Director candidate identified |

> **Phase 0 Gate Criterion:** Founding team agreed (verbal); village leadership informed and not opposed; draft charter complete.

---

### 3.0 Phase 1 — Foundation — ¥5.5M

*Duration: Month 4–9 (July–December 2026)*

The most structurally important phase. The feasibility studies produced here determine the credibility of all subsequent funding applications and Phase 2/3 budgets. Cutting corners here is false economy.

#### 3.1 Legal Entity Setup — ¥0.5M

| Item | Detail |
|------|--------|
| Scope | 一般社団法人 incorporation; notarized 定款; Legal Affairs Bureau (法務局) registration; opening bank account; accounting system setup (弥生会計 or equivalent) |
| Owner | Director — Finance/Operations |
| Budget | ¥0.5M (¥110K registration + ¥50K notary + ¥300K scrivener + ¥40K accounting setup) |
| Deliverables | Certificate of incorporation; registered office address; operational bank account; accounting system active |
| Acceptance | 法務局 registration confirmed; first board resolution recorded |

#### 3.2 Forestry Feasibility Study — ¥1.5M

| Item | Detail |
|------|--------|
| Scope | Field survey of candidate sugi plots for native species conversion; transportation and extraction cost analysis from steep terrain; native forest restoration plan, species selection, and timeline; carbon sequestration estimate; coordination with 日本林業協会 / 林野庁 advisors |
| Owner | Director — Forestry/Local |
| Budget | ¥1.5M (lower end of ¥1.5–3M range; full range covered by Phase 1 contingency if needed) |
| Deliverables | Forestry feasibility report (Japanese); executive summary (bilingual); land parcel map; carbon estimate methodology |
| Acceptance | Report accepted by advisory board; J-Credit pre-qualification confirmed or ruled out |

#### 3.3 Energy Systems Feasibility Study — ¥1.5M

| Item | Detail |
|------|--------|
| Scope | Biomass CHP sizing (primary source) fuelled by sugi thinnings — baseload electricity + heat, fuel-supply logistics; complementary solar generation potential at school site; battery storage sizing; grid connection options; FIT/FIP eligibility assessment; EV charging load modelling; blackout resilience scenarios |
| Owner | Director — Technology |
| Budget | ¥1.5M (lower end of ¥2–4M range) |
| Deliverables | Energy feasibility report; biomass CHP sizing and dispatch model; solar yield model; battery sizing recommendation; grid connection options memo; FIT/FIP eligibility letter |
| Acceptance | Report accepted by advisory board; METI pre-consultation completed |

#### 3.4 Building & Site Assessment — ¥0.8M

| Item | Detail |
|------|--------|
| Scope | Structural condition survey of the former Sugano Elementary School (Mitsue Taiken Koryukan) and candidate factory building; seismic compliance assessment (新耐震基準); identification of required renovations for data center use; zoning review |
| Owner | Director — Technology |
| Budget | ¥0.8M (mid of ¥1–2M range for single-building survey) |
| Deliverables | Structural survey report; seismic compliance summary; renovation scope outline; zoning confirmation memo |
| Acceptance | Report accepted by board; Phase 3 renovation budget range confirmed |

#### 3.5 Connectivity Assessment — ¥0.4M

| Item | Detail |
|------|--------|
| Scope | Current fiber capacity reaching Mitsue; upgrade requirements and costs; NTT consultation; satellite/microwave fallback options |
| Owner | Director — Technology |
| Budget | ¥0.4M (mid of ¥0.3–0.5M range) |
| Deliverables | Connectivity gap analysis; NTT meeting notes; upgrade cost estimate; backup options memo |
| Acceptance | Report accepted; Phase 3 fiber upgrade budget confirmed |

#### 3.6 Operations Setup — ¥0.8M

| Item | Detail |
|------|--------|
| Scope | Advisory board formalization (letters of commitment from Ray Ozzie and others); initial bilingual website live; funding pipeline documentation; grant calendar setup |
| Owner | Representative Director |
| Budget | ¥0.8M |
| Deliverables | Signed advisory board letters; live website; grant application calendar for Phase 2 |
| Acceptance | Website reviewed by board; advisory board confirmed in writing |

#### 3.7 Village RE Plan Alignment & 交付金 事業計画 Co-development (官民連携) — ¥0 (PM overhead)

| Item | Detail |
|------|--------|
| Scope | Map project deliverables to the village's official RE plan (御杖村再エネ導入最大化計画) Basic Policies & indicators (incl. the "one resilient site" target); co-develop the village's multi-year 地域脱炭素移行・再エネ推進交付金 事業計画; position the project as the 官民連携 operating partner. Spans into Phase 2 grant writing (see 4.7). |
| Owner | Representative Director + Japanese co-founder |
| Budget | ¥0 — absorbed in 1.0 PM & governance / 4.7 grant writing (no new BAC line) |
| Deliverables | Deliverable-to-plan mapping document; draft 交付金 事業計画 input prepared with the village; 官民連携 role confirmed |
| Acceptance | Village confirms the project's operating-partner role for its 交付金 application |

> **Note:** The village completed step 1 of the MoE funding ladder (planning-support grant → RE plan, Jan 2025). This task advances step 2 (交付金, 2/3–3/4 subsidy on solar/battery/EV/private-wire, via village). See `mitsue_village_re_plan_alignment.md`.

> **Phase 1 Gate Criterion:** Legal entity registered; all four feasibility studies accepted; ¥3–8M secured; letter of support from Mitsue village government.

---

<div class="page-break"></div>

### 4.0 Phase 2 — Pilot Design — ¥22.25M

*Duration: Month 10–18 (January–September 2027)*

Converts feasibility into engineering reality. The permit applications submitted here are the long-lead items that drive Phase 3 start. Staffing up in this phase is critical.

#### 4.1 Building & Structural Design — ¥2.0M

| Item | Detail |
|------|--------|
| Scope | Full architectural drawings for school renovation (1 wing); seismic retrofit specifications; mechanical/electrical/plumbing for data center wing; building permit application package |
| Owner | Director — Technology |
| Budget | ¥2.0M |
| Deliverables | Stamped architectural drawings; MEP specs; building permit application submitted |
| Acceptance | Building permit application accepted by 奈良県 authorities |

#### 4.2 Energy Systems Engineering — ¥2.0M

| Item | Detail |
|------|--------|
| Scope | Detailed design for solar PV array, battery storage, EV charging integration, and grid connection; equipment specifications; load flow analysis; FIT/FIP application |
| Owner | Director — Technology |
| Budget | ¥2.0M |
| Deliverables | Detailed energy system design package; equipment spec sheets; FIT/FIP application submitted to METI |
| Acceptance | METI FIT/FIP application reference number received |

#### 4.3 Data Center & IT Architecture — ¥1.0M

| Item | Detail |
|------|--------|
| Scope | Server room layout; power and cooling design for 10–20 servers; network architecture; APPI compliance plan; cybersecurity framework |
| Owner | Director — Technology |
| Budget | ¥1.0M |
| Deliverables | Data center design package; network topology diagram; security framework document |
| Acceptance | Design reviewed and accepted by technical advisory committee |

#### 4.4 EV Charging System Design — ¥1.0M

| Item | Detail |
|------|--------|
| Scope | Charging station layout for 4 units; grid integration design; 消防 and 電気設備 permit preparation; signage and access plan |
| Owner | Director — Technology |
| Budget | ¥1.0M |
| Deliverables | EV charging design drawings; permit pre-application submitted |
| Acceptance | Fire department and electrical safety pre-consultation completed |

#### 4.5 Permitting & Regulatory — ¥3.5M

| Item | Detail |
|------|--------|
| Scope | Manage all permit applications across agencies: building permit (建築基準法), forestry cutting notification (伐採届出), FIT/FIP registration (METI), EV charging safety permits (消防・電気), environmental review coordination |
| Owner | Director — Finance/Operations (supported by 行政書士) |
| Budget | ¥3.5M (includes 行政書士 fees of ¥200–500K per application) |
| Deliverables | All permit applications submitted; building permit issued; FIT/FIP registration confirmed |
| Acceptance | Core permits in hand before Phase 3 procurement begins |

> **Note:** METI FIT/FIP registration and building permits are the critical-path items — typical lead time 4–6 months. Applications must be submitted no later than M12 (March 2027).

#### 4.6 Partnership & Landowner Agreements — ¥1.5M

| Item | Detail |
|------|--------|
| Scope | Negotiate and execute landowner contracts for sugi harvesting rights; memoranda of understanding with key technical and institutional partners; village government cooperation agreement |
| Owner | Representative Director |
| Budget | ¥1.5M (legal drafting, negotiation facilitation, translation) |
| Deliverables | Minimum 2 signed landowner harvest agreements; village government MOU signed; at least 1 corporate partner MOU |
| Acceptance | Legal review sign-off on all agreements; board approval |

#### 4.7 Grant Writing & Funding Applications — ¥2.0M

| Item | Detail |
|------|--------|
| Scope | Prepare and submit applications for major grants: 地方創生関係交付金, 林野庁 subsidies, NEDO, METI green tech, Nara Prefecture, Nippon Foundation, Japan Fund for Global Environment; **support the village's 地域脱炭素移行・再エネ推進交付金 事業計画 (2/3–3/4 subsidy on solar/battery/EV/private-wire, via village 官民連携 — continues task 3.7)** |
| Owner | Director — Finance/Operations (supported by specialist 行政書士) |
| Budget | ¥2.0M (行政書士 fees ¥200–500K each; 4–6 applications) |
| Deliverables | Minimum 4 grant applications submitted; at least ¥30M in pending applications by end of Phase 2; village 交付金 事業計画 input contributed |
| Acceptance | Applications submitted; Gate 3 funding of ¥80–200M confirmed or committed |

#### 4.8 Staff Recruitment & Onboarding — ¥6.0M

| Item | Detail |
|------|--------|
| Scope | Hire first 2–3 part-time staff (project coordinator, operations/admin, possibly local forestry liaison); onboarding and process documentation |
| Owner | Representative Director |
| Budget | ¥6.0M (9 months × 3 × ~¥220K/month blended part-time) |
| Deliverables | 2–3 staff under contract; onboarding complete; key processes documented |
| Acceptance | Staff in post and contributing before Phase 3 begins |

#### 4.9 Vendor Pre-Qualification — ¥1.5M

| Item | Detail |
|------|--------|
| Scope | Shortlist and pre-qualify vendors for: building renovation contractor, solar/battery supplier, data center hardware, EV charging equipment, and the biomass gasification-CHP unit; obtain binding budget quotes for Phase 3 procurement |
| Owner | Director — Technology |
| Budget | ¥1.5M |
| Deliverables | Vendor shortlist per category; budget quotes received; Phase 3 procurement plan |
| Acceptance | Phase 3 WBS 5.x budgets confirmed within ±15% of EVM baseline before Gate 3 |

> **Biomass CHP — Japanese manufacturer only.** The gasification-CHP unit must be a domestic maker (shortlist: 中外炉工業 lead; 神鋼環境ソリューション / 静岡製機 / ネオナイト) — for domestic service/parts, simpler FIT + 交付金 paperwork, and the local supply-chain story. Imported units (FORTES/Spanner/Burkhardt) are benchmark-only. The full CHP fleet + fuel-prep are **Phase 4 scale** (out of this PMB) — see `mitsue_forest_workforce_energy_plan.md` and EVM §14.

#### 4.10 Phase 2 Contingency — ¥1.75M

| Item | Detail |
|------|--------|
| Scope | Reserve for Phase 2 cost variances — particularly permit fees higher than estimated, additional engineering iterations, or grant application costs exceeding plan |
| Owner | Representative Director |
| Budget | ¥1.75M (~8% of Phase 2 direct costs) |
| Access | Requires Representative Director approval; drawn down only against specific identified variances |

> **Phase 2 Gate Criterion:** ¥30–50M secured; detailed engineering complete; key permits in hand (or application submitted with favourable pre-consultation); 2 staff in post.

---

<div class="page-break"></div>

### 5.0 Phase 3 — Pilot Build — ¥177.0M

*Duration: Month 19–30 (October 2027 – September 2028)*

The largest and most complex phase. Peak spend is in Months 22–27. All Phase 3 work packages are interdependent — building renovation must precede data center fitout; solar/battery must precede EV commissioning.

**Sequencing logic:**
```
5.1 Building Renovation → 5.5 Data Center Fitout
5.2 Solar PV + 5.3 Battery → 5.4 EV Charging commissioning
5.6 Forestry Operations → independent track (weather/season dependent)
5.7 Fiber → early in P3 (long lead time with NTT)
5.8 Testing & Commissioning → final 2 months
```

#### 5.1 School Building Renovation — ¥38.0M

| Item | Detail |
|------|--------|
| Scope | Seismic retrofit of 1 wing; internal renovation for data center and office use; MEP installation (power distribution, cooling, fire suppression); accessible entrance and welfare facilities; exterior weatherproofing |
| Owner | Director — Technology |
| Budget | ¥38.0M |
| Deliverables | Renovated wing with 建築基準法 compliance certificate; handover from contractor; punch-list sign-off |
| Acceptance | Building inspector sign-off; internal acceptance by project board |
| Key risks | Unforeseen structural issues adding scope; labour shortage in rural Nara |

**Work packages:**
- Seismic retrofit (structural steel/concrete)
- MEP rough-in (power, cooling, fire suppression)
- Internal partitioning and fit-out
- Exterior repairs and weatherproofing
- Site works (access road, parking, landscaping for EV)
- Final inspections and compliance certificates

#### 5.2 Solar PV Installation — ¥22.0M

| Item | Detail |
|------|--------|
| Scope | Rooftop solar PV (~100 kW); inverters; monitoring system; grid connection infrastructure; commissioning and FIT/FIP handover documentation |
| Owner | Director — Technology |
| Budget | ¥22.0M (approx. ¥220K/kW installed, rural premium) |
| Deliverables | Grid-connected solar array generating power; FIT/FIP connection agreement in place; monitoring dashboard live |
| Acceptance | METI FIT/FIP connection confirmed; generation data logging active |

#### 5.3 Battery Storage System — ¥12.0M *(subject to feasibility study confirmation)*

| Item | Detail |
|------|--------|
| Scope | Lithium-ion battery storage system sized for 12–48 hours critical-facility backup; BMS; integration with solar and grid; safety certifications. **Decision gate: Phase 1 energy feasibility study must confirm economic and operational case before this work package proceeds.** |
| Owner | Director — Technology |
| Budget | ¥12.0M |
| Deliverables | Battery system installed, commissioned, and safety-certified; blackout simulation test passed |
| Acceptance | 消防 safety certificate; 48-hour backup test at design load |

#### 5.4 EV Charging Infrastructure — ¥15.0M

| Item | Detail |
|------|--------|
| Scope | 4 EV charging stations (mix of standard AC and fast DC); civil works for cable trenching; payment/management software; signage; safety approvals; public launch |
| Owner | Director — Technology |
| Budget | ¥15.0M |
| Deliverables | 4 operational charging stations open to public; payment system live; 消防・電気設備 approvals in hand |
| Acceptance | Public launch event; village government acceptance |

#### 5.5 Data Center Fitout — ¥20.0M

| Item | Detail |
|------|--------|
| Scope | Server racks and hardware (10–20 servers, edge computing focus); precision cooling; structured cabling; UPS backup integration with battery system; network equipment; APPI-compliant security controls; remote monitoring |
| Owner | Director — Technology |
| Budget | ¥20.0M |
| Deliverables | Operational data center accepting first paying workloads; monitoring dashboard live; APPI compliance documentation complete |
| Acceptance | First commercial hosting contract signed; uptime monitoring active |

#### 5.6 Forestry Operations — ¥25.0M

| Item | Detail |
|------|--------|
| Scope | First 5–10 ha of sugi harvested under signed landowner agreements; timber processed for lumber; native species replanting commenced; forest road and drainage improvements; J-Credit documentation initiated |
| Owner | Director — Forestry/Local |
| Budget | ¥25.0M |
| Deliverables | Harvest completion report; replanting plan executed for cleared area; first J-Credit application submitted |
| Acceptance | 伐採届出 (cutting notification) filed and acknowledged; replanting confirmed by site inspection |
| Key risks | Seasonal access (avoid typhoon season M19–M23); steep terrain requiring specialised equipment |

#### 5.7 Fiber Connectivity Upgrade — ¥10.0M

| Item | Detail |
|------|--------|
| Scope | Upgrade fiber capacity to Mitsue in coordination with NTT and/or regional ISP; install dedicated dark fiber or upgraded leased line to school site; microwave backup link installation |
| Owner | Director — Technology |
| Budget | ¥10.0M |
| Deliverables | Confirmed bandwidth upgrade (target: 1 Gbps symmetric minimum to school site); backup link live; NTT SLA in place |
| Acceptance | Bandwidth test confirming contracted speeds; failover test on backup link |
| Note | NTT coordination has 6–9 month lead time — initiate in Phase 2 (M15 at latest) |

#### 5.8 Testing, Commissioning & Startup — ¥8.0M

| Item | Detail |
|------|--------|
| Scope | Integrated system testing across all Phase 3 elements; punch-list resolution; staff training; documentation finalisation; public launch event; Phase 4 operational handover |
| Owner | Representative Director |
| Budget | ¥8.0M |
| Deliverables | All systems tested and operational; staff trained; punch-list closed; Phase 4 operational plan approved; launch event completed |
| Acceptance | Board acceptance of Phase 3 completion; Phase 4 operational plan approved |

**Sub-work packages:**
- Solar + battery integrated test (blackout simulation)
- Data center stress test and security audit
- EV charging operational test (all 4 stations)
- Forestry first-year progress review
- Fiber latency and failover test
- Staff training programme (data center ops, EV maintenance, forestry coordination)
- Phase 3 completion documentation package
- Public launch event (village + media + funders)

#### 5.9 Phase 3 Contingency — ¥27.0M

| Item | Detail |
|------|--------|
| Scope | Reserve for Phase 3 cost variances — primarily structural findings in 5.1, equipment cost movements, rural labour premiums, or seasonal delays |
| Owner | Representative Director |
| Budget | ¥27.0M (~18% of Phase 3 direct costs) |
| Access | Representative Director approval for draws up to ¥5M; board approval required above ¥5M |

> **Phase 3 Gate Criterion (Gate 4):** All systems operational; first commercial data center contract signed; EV charging open to public; forestry harvest commenced; Phase 4 plan approved by board.

---

## 4. Budget Summary

| WBS | Element | Budget (¥M) | % of BAC |
|-----|---------|-------------|----------|
| 1.0 | Project Management & Governance | 15.00 | 6.8% |
| 2.0 | Phase 0 — Pre-Foundation | 0.25 | 0.1% |
| 3.0 | Phase 1 — Foundation | 5.50 | 2.5% |
| 4.0 | Phase 2 — Pilot Design | 22.25 | 10.1% |
| 5.0 | Phase 3 — Pilot Build | 177.00 | 80.5% |
| | **Total BAC (PMB)** | **220.00** | **100%** |
| | Management Reserve (not in PMB) | 25.00 | — |
| | **Total Project Budget** | **245.00** | — |

<div style="page-break-inside:avoid; margin: 10pt 0">

**Figure 2 — Budget by WBS Element**

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 195" style="width:100%;display:block">
  <!-- scale: 500px = ¥245M → 2.041px/¥1M; bars from x=195 to x=695 -->
  <!-- Row 1: PM & Gov ¥15M → w=31 -->
  <rect x="0" y="5" width="700" height="24" fill="#f0f4ff"/>
  <text x="190" y="21" text-anchor="end" font-size="8.5" fill="#333" font-weight="bold" font-family="Segoe UI,sans-serif">PM &amp; Governance</text>
  <rect x="195" y="8" width="31" height="16" rx="2" fill="#9fb8e8"/>
  <text x="229" y="20" font-size="7.5" fill="#333" font-family="Segoe UI,sans-serif">¥15M (6.8%)</text>
  <!-- Row 2: Phase 0 ¥0.25M → w=0.5 (show minimum 6px) -->
  <rect x="0" y="30" width="700" height="24" fill="#ffffff"/>
  <text x="190" y="46" text-anchor="end" font-size="8.5" fill="#333" font-weight="bold" font-family="Segoe UI,sans-serif">Phase 0 — Pre-Foundation</text>
  <rect x="195" y="33" width="6" height="16" rx="2" fill="#6796e6" fill-opacity="0.4"/>
  <text x="204" y="45" font-size="7.5" fill="#333" font-family="Segoe UI,sans-serif">¥0.25M (0.1%)</text>
  <!-- Row 3: Phase 1 ¥5.5M → w=11 -->
  <rect x="0" y="55" width="700" height="24" fill="#f0f4ff"/>
  <text x="190" y="71" text-anchor="end" font-size="8.5" fill="#333" font-weight="bold" font-family="Segoe UI,sans-serif">Phase 1 — Foundation</text>
  <rect x="195" y="58" width="11" height="16" rx="2" fill="#6796e6"/>
  <text x="209" y="70" font-size="7.5" fill="#333" font-family="Segoe UI,sans-serif">¥5.5M (2.5%)</text>
  <!-- Row 4: Phase 2 ¥22.25M → w=45 -->
  <rect x="0" y="80" width="700" height="24" fill="#ffffff"/>
  <text x="190" y="96" text-anchor="end" font-size="8.5" fill="#333" font-weight="bold" font-family="Segoe UI,sans-serif">Phase 2 — Pilot Design</text>
  <rect x="195" y="83" width="45" height="16" rx="2" fill="#e58520"/>
  <text x="243" y="95" font-size="7.5" fill="#333" font-family="Segoe UI,sans-serif">¥22.25M (10.1%)</text>
  <!-- Row 5: Phase 3 ¥177M → w=361 -->
  <rect x="0" y="105" width="700" height="24" fill="#f0f4ff"/>
  <text x="190" y="121" text-anchor="end" font-size="8.5" fill="#333" font-weight="bold" font-family="Segoe UI,sans-serif">Phase 3 — Pilot Build</text>
  <rect x="195" y="108" width="361" height="16" rx="2" fill="#d94f4f"/>
  <text x="376" y="120" text-anchor="middle" font-size="8.5" fill="white" font-weight="bold" font-family="Segoe UI,sans-serif">¥177M — 80.5% of BAC</text>
  <!-- Row 6: MR ¥25M → w=51 (greyed, not in PMB) -->
  <rect x="0" y="130" width="700" height="24" fill="#f8f8f8"/>
  <text x="190" y="146" text-anchor="end" font-size="8.5" fill="#888" font-family="Segoe UI,sans-serif">Management Reserve (outside PMB)</text>
  <rect x="195" y="133" width="51" height="16" rx="2" fill="#ccc"/>
  <text x="249" y="145" font-size="7.5" fill="#666" font-family="Segoe UI,sans-serif">¥25M — Board approval required to access</text>
  <!-- Total bar -->
  <rect x="0" y="155" width="700" height="28" fill="#e8eeff"/>
  <text x="190" y="173" text-anchor="end" font-size="9" fill="#333" font-weight="bold" font-family="Segoe UI,sans-serif">TOTAL PROJECT BUDGET</text>
  <rect x="195" y="158" width="500" height="18" rx="2" fill="#4a7ac4"/>
  <text x="445" y="171" text-anchor="middle" font-size="9" fill="white" font-weight="bold" font-family="Segoe UI,sans-serif">¥245M Total Approved Budget (BAC ¥220M + MR ¥25M)</text>
  <!-- Scale line -->
  <line x1="195" y1="185" x2="695" y2="185" stroke="#bbb" stroke-width="0.5"/>
  <text x="195" y="193" font-size="7" fill="#888" font-family="Segoe UI,sans-serif">0</text>
  <text x="297" y="193" text-anchor="middle" font-size="7" fill="#888" font-family="Segoe UI,sans-serif">50M</text>
  <text x="399" y="193" text-anchor="middle" font-size="7" fill="#888" font-family="Segoe UI,sans-serif">100M</text>
  <text x="501" y="193" text-anchor="middle" font-size="7" fill="#888" font-family="Segoe UI,sans-serif">150M</text>
  <text x="603" y="193" text-anchor="middle" font-size="7" fill="#888" font-family="Segoe UI,sans-serif">200M</text>
  <text x="695" y="193" text-anchor="middle" font-size="7" fill="#888" font-family="Segoe UI,sans-serif">245M</text>
</svg>

</div>

### Budget by Category (across all phases)

| Category | Budget (¥M) | Examples |
|----------|-------------|---------|
| Studies & design | ¥13.0M | Feasibility studies, engineering design, IT architecture |
| Construction & civil | ¥48.0M | Building renovation, site works, civil for EV/fiber |
| Equipment & hardware | ¥69.0M | Solar, battery, EV chargers, servers, network gear |
| Ecology & forestry | ¥25.0M | Harvest operations, replanting, forest roads |
| Permits & compliance | ¥6.5M | 行政書士 fees, permit applications, legal |
| People & operations | ¥22.0M | PM team, hired staff, advisory board |
| Contingencies | ¥28.75M | Phase 2 and Phase 3 contingency reserves |
| Communications | ¥3.0M | Website, translation, design |
| Other / miscellaneous | ¥4.75M | Accounting, banking, training, launch event |
| **Total BAC** | **¥220.0M** | |

<div style="page-break-inside:avoid; margin: 10pt 0">

**Figure 3 — Budget Breakdown by Cost Category**

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 250" style="width:100%;display:block">
  <!-- scale: 400px = ¥70M (max) → 5.714px/¥1M; bars from x=205 to x=605 -->
  <!-- Equipment ¥69M → w=394 -->
  <rect x="0" y="5" width="700" height="22" fill="#f0f4ff"/>
  <text x="200" y="19" text-anchor="end" font-size="8" fill="#333" font-family="Segoe UI,sans-serif">Equipment &amp; hardware</text>
  <rect x="205" y="7" width="394" height="14" rx="2" fill="#d94f4f"/>
  <text x="604" y="18" text-anchor="end" font-size="8" fill="#333" font-family="Segoe UI,sans-serif">¥69M</text>
  <!-- Construction ¥48M → w=274 -->
  <rect x="0" y="28" width="700" height="22" fill="#fff"/>
  <text x="200" y="42" text-anchor="end" font-size="8" fill="#333" font-family="Segoe UI,sans-serif">Construction &amp; civil</text>
  <rect x="205" y="30" width="274" height="14" rx="2" fill="#c04040"/>
  <text x="484" y="42" font-size="8" fill="#333" font-family="Segoe UI,sans-serif">¥48M</text>
  <!-- Contingencies ¥28.75M → w=164 -->
  <rect x="0" y="51" width="700" height="22" fill="#f0f4ff"/>
  <text x="200" y="65" text-anchor="end" font-size="8" fill="#333" font-family="Segoe UI,sans-serif">Contingencies (P2+P3)</text>
  <rect x="205" y="53" width="164" height="14" rx="2" fill="#aaa"/>
  <text x="374" y="65" font-size="8" fill="#333" font-family="Segoe UI,sans-serif">¥28.75M</text>
  <!-- Ecology ¥25M → w=143 -->
  <rect x="0" y="74" width="700" height="22" fill="#fff"/>
  <text x="200" y="88" text-anchor="end" font-size="8" fill="#333" font-family="Segoe UI,sans-serif">Ecology &amp; forestry</text>
  <rect x="205" y="76" width="143" height="14" rx="2" fill="#4aaa50"/>
  <text x="352" y="88" font-size="8" fill="#333" font-family="Segoe UI,sans-serif">¥25M</text>
  <!-- People ¥22M → w=126 -->
  <rect x="0" y="97" width="700" height="22" fill="#f0f4ff"/>
  <text x="200" y="111" text-anchor="end" font-size="8" fill="#333" font-family="Segoe UI,sans-serif">People &amp; operations</text>
  <rect x="205" y="99" width="126" height="14" rx="2" fill="#6796e6"/>
  <text x="335" y="111" font-size="8" fill="#333" font-family="Segoe UI,sans-serif">¥22M</text>
  <!-- Studies & design ¥13M → w=74 -->
  <rect x="0" y="120" width="700" height="22" fill="#fff"/>
  <text x="200" y="134" text-anchor="end" font-size="8" fill="#333" font-family="Segoe UI,sans-serif">Studies &amp; design</text>
  <rect x="205" y="122" width="74" height="14" rx="2" fill="#4a7ac4"/>
  <text x="284" y="134" font-size="8" fill="#333" font-family="Segoe UI,sans-serif">¥13M</text>
  <!-- Permits ¥6.5M → w=37 -->
  <rect x="0" y="143" width="700" height="22" fill="#f0f4ff"/>
  <text x="200" y="157" text-anchor="end" font-size="8" fill="#333" font-family="Segoe UI,sans-serif">Permits &amp; compliance</text>
  <rect x="205" y="145" width="37" height="14" rx="2" fill="#9fb8e8"/>
  <text x="246" y="157" font-size="8" fill="#333" font-family="Segoe UI,sans-serif">¥6.5M</text>
  <!-- Other ¥4.75M → w=27 -->
  <rect x="0" y="166" width="700" height="22" fill="#fff"/>
  <text x="200" y="180" text-anchor="end" font-size="8" fill="#333" font-family="Segoe UI,sans-serif">Other / miscellaneous</text>
  <rect x="205" y="168" width="27" height="14" rx="2" fill="#bbb"/>
  <text x="236" y="180" font-size="8" fill="#333" font-family="Segoe UI,sans-serif">¥4.75M</text>
  <!-- Communications ¥3.0M → w=17 -->
  <rect x="0" y="189" width="700" height="22" fill="#f0f4ff"/>
  <text x="200" y="203" text-anchor="end" font-size="8" fill="#333" font-family="Segoe UI,sans-serif">Communications &amp; website</text>
  <rect x="205" y="191" width="17" height="14" rx="2" fill="#c8d8f0"/>
  <text x="226" y="203" font-size="8" fill="#333" font-family="Segoe UI,sans-serif">¥3.0M</text>
  <!-- Total line -->
  <line x1="205" y1="215" x2="605" y2="215" stroke="#bbb" stroke-width="0.5"/>
  <text x="205" y="224" font-size="7" fill="#888" font-family="Segoe UI,sans-serif">0</text>
  <text x="262" y="224" text-anchor="middle" font-size="7" fill="#888" font-family="Segoe UI,sans-serif">10M</text>
  <text x="319" y="224" text-anchor="middle" font-size="7" fill="#888" font-family="Segoe UI,sans-serif">20M</text>
  <text x="376" y="224" text-anchor="middle" font-size="7" fill="#888" font-family="Segoe UI,sans-serif">30M</text>
  <text x="434" y="224" text-anchor="middle" font-size="7" fill="#888" font-family="Segoe UI,sans-serif">40M</text>
  <text x="491" y="224" text-anchor="middle" font-size="7" fill="#888" font-family="Segoe UI,sans-serif">50M</text>
  <text x="605" y="224" text-anchor="middle" font-size="7" fill="#888" font-family="Segoe UI,sans-serif">70M</text>
  <text x="400" y="240" text-anchor="middle" font-size="7.5" fill="#555" font-family="Segoe UI,sans-serif">54% of spend is equipment + construction (Phase 3 procurement is the critical cost-control period)</text>
</svg>

</div>

---

## 5. Key Dependencies Map

| Dependency | Predecessor | Successor | Consequence if late |
|------------|-------------|-----------|---------------------|
| Japanese co-founder | 2.3 | 3.1, 3.6 | Cannot incorporate without Rep. Director |
| Village govt support | 2.1 | 3.1, 4.6 | No MOU; weakens grant applications |
| Feasibility studies | 3.2–3.5 | 4.1–4.4, gate funding | Phase 2 budgets unreliable; grants harder |
| METI FIT/FIP application | 4.2 | 5.2 commissioning | 6-month METI review — must submit by M12 |
| Building permit | 4.1 | 5.1 construction start | Cannot commence construction without it |
| NTT fiber initiation | 4.5 / 4.7 | 5.7 | 6–9 month NTT lead time |
| Gate 3 funding | 4.7 | 5.0 (all) | Phase 3 cannot start without confirmed ¥80M+ |
| Building renovation | 5.1 | 5.5 | Data center cannot be fitted before shell complete |
| Solar + battery | 5.2 + 5.3 | 5.4 | EV charging dependent on local power supply |

---

*Rob Oudendijk — YR-Design / Safecast*
*Mitsue, Nara Prefecture, Japan*
*May 2026*
