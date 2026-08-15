**Reconstructing the real 6.6 kV distribution network in Mitsue Village (御杖村) is feasible and high-value for the biomass CHP + edge data center project**, especially for blackout resilience, interconnection studies, and siting. Official Kansai Transmission & Distribution (関西電力送配電) maps stop at higher voltages or aggregate levels; the 6.6 kV feeder network is denser, more local, and largely overhead in this mountainous rural area.

Your five source categories are solid. Here is a practical prioritization and how to extract usable geometry, topology, and attributes from each.

### 1. Kansai T&D public mapping (already obtained – baseline)

They publish 154 kV-and-below mapping PDFs and capacity/constraint overlays. Nara Prefecture sheets explicitly cover 御杖村 / 宇陀 / 曽爾. These show:

- 77 kV and 22/33 kV lines and substations.
- Approximate locations of distribution substations that step down to 6.6 kV.
- Constraint coloring (red/green) that flags congested or limited 6.6 kV areas.

**Limitation**: They do **not** publish detailed 6.6 kV feeder routes, pole-by-pole geometry, or named feeders publicly. Treat these as the high-level skeleton (which substation feeds which valley) and fill in the rest with the methods below.

### 2. Geospatial / open mapping data (highest immediate ROI for geometry)

- **OpenStreetMap (OSM)**: Query power=minor_line + voltage=6600 (or untagged but visually 3-wire), power=pole, power=transformer, power=substation. Coverage in rural Nara is incomplete but improving; valleys often have partial tracing. Use Overpass Turbo or download the Kansai extract (Geofabrik). Japanese mappers commonly tag 6.6 kV as power=minor_line + voltage=6600 + cables=3 + frequency=60.
- **GSI (国土地理院) aerial/ortho imagery + digital elevation**: Best free high-resolution base for tracing. Combine with recent satellite (Google, Bing, ESRI, or paid high-res) to follow the characteristic 3-wire corridors along roads, forest tracks, and ridge lines.
- **Other**: Some community Google My Maps or personal power-system maps exist for Kansai (search for 関西 送電系統図 or similar enthusiast layers), but verify against primary sources. No comprehensive official open 6.6 kV vector layer is publicly released.

**Workflow tip**: Start in QGIS or JOSM. Load OSM power layers + GSI tiles + hillshade. Manually or semi-automatically trace visible 3-phase overhead lines. Tag voltage where you can confirm (insulator count/style, conductor size, presence of cutouts/transformers).

### 3. Mitsue Village documents (local ground truth)

Target these specifically:

- Disaster prevention / regional resilience plans (地域防災計画, 地区防災計画) – often include critical facility power supply routes or backup generator interconnection points.
- Road works, forest road, and utility relocation notices (道路工事、林道、占用許可、移設協議).
- Public facility and school construction / renovation documents (especially the former Sugano Elementary / 体験交流館 candidate site).
- Any village renewable-energy or decarbonization plan materials (the project already aligns with the village’s MoE-funded RE plan).

These rarely contain full feeder maps, but they frequently show local pole numbers, switching points, or “from which high-voltage line” notes for specific buildings. Freedom-of-information or direct request to the village office (or cooperation via the project’s community engagement) is realistic for a non-profit rural revitalization effort.

### 4. Historical Kansai Electric / T&D documents

Older distribution maps, feeder names, and switching diagrams occasionally appear in:

- Past construction reports, environmental assessments, or local newspaper archives.
- Technical papers or industry association materials that used Mitsue/Uda as case studies.
- Any residual paper maps held by local contractors, former employees, or the village itself.

Feeder names and switching-point locations are gold for topology even if geometry is approximate. These are harder to obtain systematically but high-value when found.

### 5. Aerial / satellite imagery (ground-truth tracing)

This is the decisive layer for actual 6.6 kV corridors:

- 6.6 kV is almost always 3-wire (sometimes with neutral or underbuilt LV/comms).
- It follows roads and forest tracks through the valleys far more closely than higher-voltage lines.
- Look for pole shadows, insulator strings, transformers (cylindrical cans), cutouts, and switchgear.
- Seasonal leaf-off imagery (winter) is far better in sugi forest.
- Stereo or multi-date imagery helps confirm continuity across canopy gaps.

Combine with GSI 1:25,000 / 1:10,000 topographic maps and recent orthophotos. In practice, a motivated mapper can recover 70–90 % of the main feeder geometry this way in a rural area the size of Mitsue.

### Recommended reconstruction pipeline

1. **Skeleton** – Place the known 77/22–33 kV substations and lines from Kansai T&D maps.
2. **OSM + imagery baseline** – Pull existing power features; systematically trace missing 3-wire corridors along all valleys and roads.
3. **Local documents** – Overlay known poles, transformers serving public facilities, and any named feeders or switching points.
4. **Field validation (selective)** – Photograph pole numbers, transformer nameplates, switchgear, and insulator configurations at key junctions and the candidate data-center site. (Stay safe; do not approach energized equipment.)
5. **Topology & attributes** – Infer radial vs. looped structure, estimate typical conductor sizes, and note any existing automation (reclosers, remote switches) visible in imagery or documents.
6. **Publish openly** – Since the Mitsue project emphasizes open knowledge, release the resulting GeoJSON/GeoPackage under an open license (with clear “reconstructed / not official” disclaimer). This also invites corrections from locals or other mappers.

### Practical next steps you can take immediately

- Download the latest Kansai OSM extract and run targeted Overpass queries for power features inside the village bounding box.
- Load GSI tiles + recent satellite in QGIS and begin tracing the main valleys feeding the Sugano / central area.
- Request the relevant sections of the village’s disaster plan and any recent utility-related construction documents.
- Check whether the Nara distribution office (or local contractors) will share non-confidential feeder schematic sketches under a research/non-commercial agreement tied to the village’s own RE plan.

This approach will give you a usable, citable 6.6 kV network model far beyond the official high-level maps—exactly what is needed for interconnection feasibility, resilience analysis, and transparent community documentation. If you share a specific sub-area (e.g., around the candidate school site) or already-have layers, I can help refine queries, tagging conventions, or processing steps.