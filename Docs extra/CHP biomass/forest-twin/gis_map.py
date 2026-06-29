#!/usr/bin/env python3
"""Forest Twin — simple GIS test map (stdlib only).

Turns data/stands.csv into:
  - stands.geojson : load directly in QGIS / any GIS
  - stands_map.html: self-contained Leaflet map (open in a browser, no server)

Stands are colour-coded by harvest status (from the model's rotation logic):
  green  = growing      yellow = ready to thin
  red    = ready to cut  blue   = replanted broadleaf

NOTE: geometry is PLACEHOLDER — demo squares around Mitsue village centre until
real stand boundaries arrive from the Mitsue Kanko / LiDAR survey. The attributes
(area, age, volume, status) are real, computed by forest_model.
"""
import csv
import json
import math
import os
import random

import forest_model as fm

HERE = os.path.dirname(os.path.abspath(__file__))

# Sugano Organic, 御杖村菅野2696 (GSI-geocoded) — anchor for the demonstration area
SUGANO_LAT, SUGANO_LON = 34.482601, 136.165924
# Demo stands sit beside the village/Sugano (close to people), not in remote mountains
CENTRE_LAT, CENTRE_LON = SUGANO_LAT, SUGANO_LON
M_PER_DEG_LAT = 111_000.0


def _shoelace(pts):
    s = 0.0
    for i in range(len(pts)):
        x1, y1 = pts[i]
        x2, y2 = pts[(i + 1) % len(pts)]
        s += x1 * y2 - x2 * y1
    return abs(s) / 2.0


def organic_polygon(lat, lon, area_ha, seed=7, k=40):
    """A smooth, irregular (organic) polygon of ~area_ha centred on lat/lon.
    Radius is perturbed by a few sine harmonics with seeded phases, then the
    whole ring is rescaled so the enclosed area matches area_ha."""
    rnd = random.Random(seed)
    p2, p3, p5 = (rnd.uniform(0, 2 * math.pi) for _ in range(3))
    r0 = math.sqrt(area_ha * 10_000 / math.pi)
    pts = []
    for i in range(k):
        th = 2 * math.pi * i / k
        f = (1 + 0.18 * math.sin(3 * th + p3)
               + 0.12 * math.sin(5 * th + p5)
               + 0.09 * math.sin(2 * th + p2))
        r = r0 * max(0.45, f)
        pts.append((r * math.cos(th), r * math.sin(th)))
    scale = math.sqrt(area_ha * 10_000 / _shoelace(pts))
    pts = [(x * scale, y * scale) for x, y in pts]
    mlat = M_PER_DEG_LAT
    mlon = M_PER_DEG_LAT * math.cos(math.radians(lat))
    ring = [[lon + x / mlon, lat + y / mlat] for x, y in pts]
    ring.append(ring[0])
    return [ring]


def status_of(stand, rotation_age):
    """Colour + recommendation from species/age vs rotation age."""
    if stand["species"] != "sugi":
        return "replanted (broadleaf)", "#2b7bff", "leave to grow / wildlife"
    a = stand["age"]
    if a >= rotation_age:
        return "ready to harvest", "#e23b3b", f"harvest within {max(1,int(a-rotation_age))+1} yr"
    if a >= rotation_age * 0.6:
        return "ready to thin", "#f2c037", "thin this rotation"
    return "growing", "#3aa757", f"~{int(rotation_age-a)} yr to rotation age"


def stand_eco(stand):
    """APPROXIMATE per-stand eco scores (0-1, not measured): broadleaf forest is
    far better wildlife habitat / water infiltration than dense sugi monoculture.
    A thinned/older sugi stand scores slightly better than a dense young one."""
    if stand["species"] != "sugi":
        return 0.85, 0.90          # broadleaf: high habitat + infiltration
    age_bonus = min(0.15, stand["age"] / 400.0)   # older sugi: a little more understory
    return round(0.25 + age_bonus, 2), round(0.30, 2)


def square(lat, lon, area_ha):
    """A square polygon of the given area (ha), centred on lat/lon."""
    side_m = math.sqrt(area_ha) * 100.0          # 1 ha = 100 m × 100 m
    dlat = (side_m / 2) / M_PER_DEG_LAT
    dlon = (side_m / 2) / (M_PER_DEG_LAT * math.cos(math.radians(lat)))
    return [[
        [lon - dlon, lat - dlat], [lon + dlon, lat - dlat],
        [lon + dlon, lat + dlat], [lon - dlon, lat + dlat],
        [lon - dlon, lat - dlat],
    ]]


def build():
    species = fm.load_species(os.path.join(HERE, "data", "species.csv"))
    stands = fm.load_stands(os.path.join(HERE, "data", "stands.csv"))
    rot = fm.CONFIG["rotation_age"]

    feats = []
    # lay stands out on a simple grid around the centre
    cols = 3
    for i, s in enumerate(stands):
        row, col = divmod(i, cols)
        lat = CENTRE_LAT + (row - 1) * 0.012
        lon = CENTRE_LON + (col - 1) * 0.014
        vol = fm.volume_per_ha(species[s["species"]], s["age"]) * s["area"]
        status, color, reco = status_of(s, rot)
        biodiv, water = stand_eco(s)
        feats.append({
            "type": "Feature",
            "geometry": {"type": "Polygon", "coordinates": square(lat, lon, s["area"])},
            "properties": {
                "stand_id": s["id"], "species": s["species"],
                "area_ha": round(s["area"], 1), "age": int(s["age"]),
                "volume_m3": int(vol), "status": status,
                "recommendation": reco,
                "biodiversity": biodiv, "water": water, "color": color,
            },
        })
    fc = {"type": "FeatureCollection", "features": feats}

    gj = os.path.join(HERE, "stands.geojson")
    with open(gj, "w") as f:
        json.dump(fc, f, indent=2)

    html = os.path.join(HERE, "stands_map.html")
    with open(html, "w") as f:
        f.write(HTML_TEMPLATE.replace("__GEOJSON__", json.dumps(fc)))

    qml = os.path.join(HERE, "stands.qml")          # QGIS auto-applies this style
    with open(qml, "w") as f:
        f.write(QML_STYLE)

    print(f"wrote {gj}")
    print(f"wrote {qml}  (QGIS style — auto-applied when you add stands.geojson)")
    print(f"wrote {html}  (open in a browser)")
    print(f"\n{len(feats)} stands  (rotation age {rot} yr):")
    for ft in feats:
        p = ft["properties"]
        print(f"  {p['stand_id']:<4} {p['species']:<16} {p['area_ha']:>5} ha  "
              f"age {p['age']:>2}  {p['volume_m3']:>5} m³  → {p['status']}")


HTML_TEMPLATE = """<!DOCTYPE html>
<html><head><meta charset="utf-8"><title>Mitsue Forest Twin — stand map</title>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css"/>
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
<style>
  html,body,#map{height:100%;margin:0}
  .legend{background:#fff;padding:8px 10px;border-radius:6px;line-height:1.5;font:13px sans-serif;box-shadow:0 1px 4px rgba(0,0,0,.3)}
  .legend i{display:inline-block;width:12px;height:12px;margin-right:6px;border:1px solid #555}
</style></head><body><div id="map"></div><script>
var data = __GEOJSON__;
var map = L.map('map');
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
  {maxZoom:18, attribution:'© OpenStreetMap'}).addTo(map);
var layer = L.geoJSON(data, {
  style: f => ({color:'#333', weight:1, fillColor:f.properties.color, fillOpacity:0.6}),
  onEachFeature: (f,l) => { var p=f.properties;
    l.bindPopup('<b>'+p.stand_id+'</b> ('+p.species+')<br>'+
      p.area_ha+' ha · age '+p.age+' · '+p.volume_m3+' m³<br>'+
      '<b>'+p.status+'</b><br><i>'+p.recommendation+'</i><br>'+
      '<small>eco (approx 0-1): biodiversity '+p.biodiversity+' · water '+p.water+'</small>'); }
}).addTo(map);
map.fitBounds(layer.getBounds().pad(0.5));
var lg = L.control({position:'bottomright'});
lg.onAdd = function(){ var d=L.DomUtil.create('div','legend');
  d.innerHTML='<b>Stand status</b><br>'+
    '<i style="background:#3aa757"></i>growing<br>'+
    '<i style="background:#f2c037"></i>ready to thin<br>'+
    '<i style="background:#e23b3b"></i>ready to harvest<br>'+
    '<i style="background:#2b7bff"></i>replanted broadleaf';
  return d; };
lg.addTo(map);
</script></body></html>
"""


# QGIS style: categorise polygons by the "status" field (auto-applied sidecar)
def _sym(name, rgb):
    return (f'<symbol type="fill" name="{name}" alpha="1">'
            f'<layer class="SimpleFill">'
            f'<prop k="color" v="{rgb},150"/>'
            f'<prop k="outline_color" v="51,51,51,255"/>'
            f'<prop k="outline_width" v="0.3"/>'
            f'<prop k="style" v="solid"/></layer></symbol>')

QML_STYLE = (
    "<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>\n"
    '<qgis version="3.34" styleCategories="Symbology">\n'
    '<renderer-v2 type="categorizedSymbol" attr="status" forceraster="0" symbollevels="0" enableorderby="0">\n'
    '<categories>'
    '<category render="true" value="growing" symbol="0" label="growing"/>'
    '<category render="true" value="ready to thin" symbol="1" label="ready to thin"/>'
    '<category render="true" value="ready to harvest" symbol="2" label="ready to harvest"/>'
    '<category render="true" value="replanted (broadleaf)" symbol="3" label="replanted broadleaf"/>'
    '</categories>\n<symbols>'
    + _sym("0", "58,167,87") + _sym("1", "242,192,55")
    + _sym("2", "226,59,59") + _sym("3", "43,123,255")
    + '</symbols>\n</renderer-v2>\n<layerGeometryType>2</layerGeometryType>\n</qgis>\n'
)


# ---------------------------------------------------------------------------
# Animated timeline: fixed 1-ha parcels, simulated year by year, slider + play
COLORS = ["#3aa757", "#f2c037", "#e23b3b", "#2b7bff"]   # grow / thin / harvest / broadleaf


def _cell_color_idx(species, age, rot):
    if species != "sugi":
        return 3
    if age >= rot:
        return 2
    if age >= rot * 0.6:
        return 1
    return 0


def build_timeline(regime="mixed"):
    species = fm.load_species(os.path.join(HERE, "data", "species.csv"))
    stands = fm.load_stands(os.path.join(HERE, "data", "stands.csv"))
    rot = fm.CONFIG["rotation_age"]
    conv_frac = fm.CONFIG["convert_fraction"]
    years = fm.CONFIG["sim_years"]

    # explode stands into fixed 1-ha parcels laid out as a tiled grid
    cells = []
    for s in stands:
        for _ in range(int(round(s["area"]))):
            cells.append({"species": s["species"], "age": float(s["age"])})
    n = len(cells)
    cols = math.ceil(math.sqrt(n))
    feats = []
    for i, c in enumerate(cells):
        r, col = divmod(i, cols)
        lat = CENTRE_LAT + (r - cols / 2) * 0.00095
        lon = CENTRE_LON + (col - cols / 2) * 0.00115
        feats.append({"type": "Feature", "id": i,
                      "geometry": {"type": "Polygon", "coordinates": square(lat, lon, 1.0)}})

    # simulate; record a colour frame + stats per year
    frames, stats = [], []
    backlog = 0.0
    bl_count = 0
    for _y in range(years):
        for c in cells:
            c["age"] += 1
        backlog += n / rot
        n_cut = int(backlog)
        backlog -= n_cut
        order = sorted(range(n), key=lambda i: -cells[i]["age"])
        cut = [i for i in order if cells[i]["species"] == "sugi"][:n_cut]
        for i in cut:
            if regime == "convert":
                cells[i]["species"] = fm.CONFIG["replant_species"]
            elif regime == "mixed":
                bl_count += conv_frac
                if bl_count >= 1.0:
                    cells[i]["species"] = fm.CONFIG["replant_species"]
                    bl_count -= 1.0
                else:
                    cells[i]["species"] = "sugi"
            else:  # rotation
                cells[i]["species"] = "sugi"
            cells[i]["age"] = 0.0
        frames.append([_cell_color_idx(c["species"], c["age"], rot) for c in cells])
        bl = sum(1 for c in cells if c["species"] != "sugi")
        biod = round(0.25 + 0.55 * (bl / n), 2)
        stats.append({"bl": round(100 * bl / n), "biod": biod})

    payload = {"cells": feats, "frames": frames, "stats": stats,
               "colors": COLORS, "regime": regime, "years": years}
    out = os.path.join(HERE, "stands_timeline.html")
    with open(out, "w") as f:
        f.write(TIMELINE_HTML.replace("__PAYLOAD__", json.dumps(payload)))
    print(f"wrote {out}  (open in a browser — drag the year slider / press Play)")
    print(f"  regime '{regime}', {n} parcels, {years} yr; "
          f"broadleaf {stats[0]['bl']}% -> {stats[-1]['bl']}%, "
          f"biodiversity {stats[0]['biod']} -> {stats[-1]['biod']}")


TIMELINE_HTML = """<!DOCTYPE html>
<html><head><meta charset="utf-8"><title>Mitsue Forest Twin — 50-year animation</title>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css"/>
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
<style>
  html,body{height:100%;margin:0;font-family:sans-serif}
  #map{height:calc(100% - 70px)}
  #bar{height:70px;box-sizing:border-box;padding:8px 14px;background:#f4f4f4;border-top:1px solid #ccc}
  #bar .row{display:flex;align-items:center;gap:12px}
  #slider{flex:1}
  button{font-size:15px;padding:4px 12px;cursor:pointer}
  .legend{background:#fff;padding:6px 9px;border-radius:6px;line-height:1.5;font:12px sans-serif;box-shadow:0 1px 4px rgba(0,0,0,.3)}
  .legend i{display:inline-block;width:11px;height:11px;margin-right:5px;border:1px solid #555}
  b.kpi{font-variant-numeric:tabular-nums}
</style></head><body>
<div id="map"></div>
<div id="bar"><div class="row">
  <button id="play">▶ Play</button>
  <span>Year <b class="kpi" id="yr">1</b></span>
  <input type="range" id="slider" min="1" max="1" value="1">
  <span>Broadleaf <b class="kpi" id="bl">0</b>%</span>
  <span>Biodiversity <b class="kpi" id="biod">0</b></span>
</div></div>
<script>
var P = __PAYLOAD__;
document.getElementById('slider').max = P.years;
var map = L.map('map');
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
  {maxZoom:18, attribution:'© OpenStreetMap'}).addTo(map);
var fc = {type:'FeatureCollection', features:P.cells};
var layers = [];
var layer = L.geoJSON(fc, {
  style:{color:'#444', weight:0.5, fillOpacity:0.75},
  onEachFeature:(f,l)=>{ layers[f.id]=l; }
}).addTo(map);
map.fitBounds(layer.getBounds().pad(0.2));

function render(y){
  var frame = P.frames[y-1], st = P.stats[y-1];
  for(var i=0;i<frame.length;i++) layers[i].setStyle({fillColor:P.colors[frame[i]]});
  document.getElementById('yr').textContent = y;
  document.getElementById('bl').textContent = st.bl;
  document.getElementById('biod').textContent = st.biod.toFixed(2);
}
var slider = document.getElementById('slider');
slider.oninput = ()=>render(+slider.value);

var timer=null, btn=document.getElementById('play');
btn.onclick=function(){
  if(timer){clearInterval(timer);timer=null;btn.textContent='▶ Play';return;}
  btn.textContent='⏸ Pause';
  timer=setInterval(function(){
    var y=+slider.value; y = y>=P.years?1:y+1;
    slider.value=y; render(y);
  },350);
};
var lg=L.control({position:'topright'});
lg.onAdd=function(){var d=L.DomUtil.create('div','legend');
  d.innerHTML='<b>'+P.regime+' regime</b><br>'+
    '<i style="background:#3aa757"></i>growing<br>'+
    '<i style="background:#f2c037"></i>ready to thin<br>'+
    '<i style="background:#e23b3b"></i>ready to harvest<br>'+
    '<i style="background:#2b7bff"></i>broadleaf';
  return d;};
lg.addTo(map);
render(1);
</script></body></html>
"""


# ---------------------------------------------------------------------------
def build_sugano_area(area_ha=28.0):
    """Organic-shaped potential demonstration / thinning area around Sugano
    Organic (28 ha ~ Tokuo's forest). Writes sugano_area.geojson + a Leaflet map
    with the boundary and a marker on the factory."""
    poly = organic_polygon(SUGANO_LAT, SUGANO_LON, area_ha)
    fc = {"type": "FeatureCollection", "features": [{
        "type": "Feature",
        "geometry": {"type": "Polygon", "coordinates": poly},
        "properties": {
            "name": "Sugano Organic — potential demonstration area",
            "area_ha": area_ha,
            "note": "approximate organic boundary; refine with Tokuo / LiDAR survey",
        },
    }]}
    gj = os.path.join(HERE, "sugano_area.geojson")
    with open(gj, "w") as f:
        json.dump(fc, f, indent=2)
    html = os.path.join(HERE, "sugano_area.html")
    with open(html, "w") as f:
        f.write(SUGANO_HTML.replace("__GEOJSON__", json.dumps(fc))
                .replace("__LAT__", str(SUGANO_LAT)).replace("__LON__", str(SUGANO_LON))
                .replace("__AREA__", str(area_ha)))
    print(f"wrote {gj}")
    print(f"wrote {html}  (open in a browser)")
    print(f"  organic area ~{area_ha:.0f} ha centred on Sugano Organic "
          f"({SUGANO_LAT}, {SUGANO_LON})")


SUGANO_HTML = """<!DOCTYPE html>
<html><head><meta charset="utf-8"><title>Sugano Organic — potential demonstration area</title>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css"/>
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
<style>html,body,#map{height:100%;margin:0}
.cap{background:#fff;padding:6px 9px;border-radius:6px;font:13px sans-serif;box-shadow:0 1px 4px rgba(0,0,0,.3)}</style>
</head><body><div id="map"></div><script>
var data = __GEOJSON__;
var map = L.map('map');
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
  {maxZoom:18, attribution:'© OpenStreetMap'}).addTo(map);
var area = L.geoJSON(data, {style:{color:'#1d7a33', weight:2, fillColor:'#3aa757', fillOpacity:0.4}}).addTo(map);
L.marker([__LAT__, __LON__]).addTo(map).bindPopup('<b>Sugano Organic</b><br>御杖村菅野2696');
map.fitBounds(area.getBounds().pad(0.4));
var cap = L.control({position:'bottomleft'});
cap.onAdd=function(){var d=L.DomUtil.create('div','cap');
  d.innerHTML='<b>Potential demonstration area</b><br>~__AREA__ ha around Sugano Organic'+
    '<br><small>approximate organic boundary — refine with LiDAR</small>';return d;};
cap.addTo(map);
</script></body></html>
"""


if __name__ == "__main__":
    import sys
    if "--animate" in sys.argv:
        i = sys.argv.index("--animate")
        reg = sys.argv[i + 1] if len(sys.argv) > i + 1 and not sys.argv[i+1].startswith("-") else "mixed"
        build_timeline(reg)
    elif "--sugano" in sys.argv:
        i = sys.argv.index("--sugano")
        ha = float(sys.argv[i + 1]) if len(sys.argv) > i + 1 and not sys.argv[i+1].startswith("-") else 28.0
        build_sugano_area(ha)
    else:
        build()
