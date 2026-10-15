import sys, glob, json
import xml.etree.ElementTree as ET
def ln(e): return e.tag.split('}')[-1]
feats = []
for f in sorted(glob.glob(sys.argv[1] + "/*.xml")):
    root = ET.parse(f).getroot()
    if root.findtext('{*}座標系') != '公共座標6系': continue
    pts, curves, surfs, fude = {}, {}, {}, []
    mapname = root.findtext('{*}地図名')
    for e in root.iter():
        t = ln(e)
        if t == 'GM_Point':
            x = e.find('.//{*}X'); y = e.find('.//{*}Y')
            pts[e.get('id')] = (float(y.text), float(x.text))  # E,N
        elif t == 'GM_Curve':
            seq = []
            for c in e.iter():
                if ln(c) == 'GM_Position.direct':
                    seq.append((float(c.find('{*}Y').text), float(c.find('{*}X').text)))
                elif ln(c) == 'GM_PointRef.point':
                    seq.append(c.get('idref'))
            curves[e.get('id')] = seq
        elif t == 'GM_Surface':
            ring = [c.get('idref') for c in e.iter() if ln(c) == 'GM_CompositeCurve.generator']
            surfs[e.get('id')] = ring
        elif t == '筆':
            fude.append(e)
    def resolve(s): return pts[s] if isinstance(s, str) else s
    for e in fude:
        ring = []
        for cid in surfs[e.find('{*}形状').get('idref')]:
            seg = [resolve(s) for s in curves[cid]]
            if ring and ring[-1] != seg[0] and ring[-1] == seg[-1]: seg.reverse()
            ring += seg if not ring else seg[1:] if ring[-1] == seg[0] else seg
        if len(ring) < 4: continue
        if ring[0] != ring[-1]: ring.append(ring[0])
        ll = [[x, y] for x, y in ring]
        feats.append({"type": "Feature",
            "properties": {"oaza": e.findtext('{*}大字名'), "chiban": e.findtext('{*}地番'),
                           "oaza_code": e.findtext('{*}大字コード'), "koaza_code": e.findtext('{*}小字コード'),
                           "sheet": mapname},
            "geometry": {"type": "Polygon", "coordinates": [ll]}})
json.dump({"type": "FeatureCollection", "features": feats}, open(sys.argv[2], "w"), ensure_ascii=False)
print(len(feats))
