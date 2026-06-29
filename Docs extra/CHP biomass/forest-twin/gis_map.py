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

import forest_model as fm

HERE = os.path.dirname(os.path.abspath(__file__))

# Mitsue Village (御杖村), Nara — approximate centre
CENTRE_LAT, CENTRE_LON = 34.4626, 136.1799
M_PER_DEG_LAT = 111_000.0


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
        feats.append({
            "type": "Feature",
            "geometry": {"type": "Polygon", "coordinates": square(lat, lon, s["area"])},
            "properties": {
                "stand_id": s["id"], "species": s["species"],
                "area_ha": round(s["area"], 1), "age": int(s["age"]),
                "volume_m3": int(vol), "status": status,
                "recommendation": reco, "color": color,
            },
        })
    fc = {"type": "FeatureCollection", "features": feats}

    gj = os.path.join(HERE, "stands.geojson")
    with open(gj, "w") as f:
        json.dump(fc, f, indent=2)

    html = os.path.join(HERE, "stands_map.html")
    with open(html, "w") as f:
        f.write(HTML_TEMPLATE.replace("__GEOJSON__", json.dumps(fc)))

    print(f"wrote {gj}")
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
      '<b>'+p.status+'</b><br><i>'+p.recommendation+'</i>'); }
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


if __name__ == "__main__":
    build()
